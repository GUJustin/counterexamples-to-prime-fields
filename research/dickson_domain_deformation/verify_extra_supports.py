"""Independent all-five-support replay, using interpolation residual gradients."""
from pathlib import Path
from itertools import combinations
from math import comb
import json
BASE=Path(__file__).resolve().parent

def ev(c,x,p):
 out=0
 for a in reversed(c):out=(out*x+a)%p
 return out

def derivative(c,x,p):return sum(i*c[i]*pow(x,i-1,p) for i in range(1,len(c)))%p

def interp(xs,ys,p):
 # Solve a Vandermonde system instead of the generator's Lagrange routine.
 n=len(xs);mat=[[pow(x,j,p) for j in range(n)]+[y] for x,y in zip(xs,ys)]
 for j in range(n):
  z=next(z for z in range(j,n) if mat[z][j]);mat[z],mat[j]=mat[j],mat[z]
  inv=pow(mat[j][j],-1,p);mat[j]=[a*inv%p for a in mat[j]]
  for i in range(n):
   if i!=j:
    f=mat[i][j];mat[i]=[(a-f*b)%p for a,b in zip(mat[i],mat[j])]
 return tuple(r[-1] for r in mat)

def main():
 data=json.loads((BASE/'extra_support_probe.json').read_text());p=17;k=4;n=16;v=48
 xs=list(range(1,p));polys=[tuple(comb(9,2*j+1)*a**(8-2*j)%p for j in range(k)) for a in range(1,9)]
 word=[((1+(1 if pow(x,8,p)==1 else -1))//2-pow(x,4,p))%p for x in xs]
 refs=[next(i for i,c in enumerate(polys) if ev(c,x,p)==y) for x,y in zip(xs,word)]
 basis=data['kernel_basis'];assert len(basis)==16 and all(len(z)==v for z in basis)
 # Check each supplied tangent vector directly against every incidence.
 for z in basis:
  for u,(x,y) in enumerate(zip(xs,word)):
   changes=[]
   for i,c in enumerate(polys):
    if ev(c,x,p)==y:changes.append((ev(z[n+i*k:n+(i+1)*k],x,p)+derivative(c,x,p)*z[u])%p)
   assert len(set(changes))==1
 selected=set(polys);saved={tuple(r['support']):r for r in data['supports']}
 checked=set();allowed=0;inconsistent=0
 for S in combinations(range(n),5):
  I=S[:4];u=S[4];x=xs[u]
  c=interp([xs[i] for i in I],[word[i] for i in I],p)
  if ev(c,x,p)!=word[u]:inconsistent+=1;continue
  if c in selected:allowed+=1;continue
  assert S in saved and tuple(saved[S]['polynomial'])==c
  # F=w_last-P_interpolated(x_last); differentiate at the seed.
  weights={u:1}
  for i in I:
   numerator=1;denominator=1
   for j in I:
    if j!=i:numerator=numerator*(x-xs[j])%p;denominator=denominator*(xs[i]-xs[j])%p
   weights[i]=-numerator*pow(denominator,-1,p)%p
  residuals=[]
  for z in basis:
   change=0
   for i,weight in weights.items():
    ref=refs[i];xx=xs[i]
    delta_word=ev(z[n+ref*k:n+(ref+1)*k],xx,p)+derivative(polys[ref],xx,p)*z[i]
    change+=weight*(delta_word-derivative(c,xx,p)*z[i])
   residuals.append(change%p)
  factor=1
  for i in I:factor=factor*(x-xs[i])%p
  assert residuals==[factor*a%p for a in saved[S]['kernel_derivatives']]
  assert any(residuals)
  checked.add(S)
 assert checked==set(saved) and len(checked)==208 and allowed==48 and inconsistent==4112
 out=dict(status='passed',all_five_supports=comb(n,5),already_inconsistent=inconsistent,
  selected_candidate_supports=allowed,unwanted_supports_with_verified_nonzero_tangent=len(checked),
  claimed_generic_profile=dict(n=16,dimension=4,complete_above_capacity_list=8,agreement_each=6,all_other_candidates_at_most=4),
  scope='Together with the separately certified full-row-rank Hensel lift, all unwanted five-point incidences can be avoided on one characteristic-zero deformation. This is a finite exact-profile example, not a growing-list construction.')
 (BASE/'extra_support_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
