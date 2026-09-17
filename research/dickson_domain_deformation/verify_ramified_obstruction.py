"""Stdlib-only verification, reconstructing the p41 incidence equations."""
from math import comb
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent


def ev(c,x,mod):
 v=0
 for a in reversed(c):v=(v*x+a)%mod
 return v


def matrix_rank(rows,p):
 a=[row[:] for row in rows];r=0
 for c in range(len(a[0])):
  z=next((z for z in range(r,len(a)) if a[z][c]%p),None)
  if z is None:continue
  a[r],a[z]=a[z],a[r]
  inv=pow(a[r][c],-1,p);a[r]=[x*inv%p for x in a[r]]
  for z in range(r+1,len(a)):
   f=a[z][c]%p
   if f:a[z]=[(x-f*y)%p for x,y in zip(a[z],a[r])]
  r+=1
  if r==len(a):break
 return r


def main():
 certificate=json.loads((BASE/'ramified_obstruction.json').read_text())
 p=41;n=40;k=10;L=20;variables=n+k*L;e=21
 cs=[[comb(e,2*j+1)*pow(a,e-2*j-1,p)%p for j in range(k)] for a in range(1,L+1)]
 xs=list(range(1,p))
 word=[((1+(1 if pow(x,20,p)==1 else -1))//2-pow(x,k,p))%p for x in xs]
 equations=[];J=[];rhs=[];second=[]
 for u,x in enumerate(xs):
  incident=[i for i,c in enumerate(cs) if ev(c,x,p)==word[u]]
  assert incident
  ref=incident[0]
  for i in incident[1:]:
   equations.append((u,i,ref));row=[0]*variables
   row[u]=sum(t*(cs[i][t]-cs[ref][t])*pow(x,t-1,p) for t in range(1,k))%p
   for t in range(k):row[n+i*k+t]=pow(x,t,p);row[n+ref*k+t]=-pow(x,t,p)%p
   J.append(row)
   residual=(ev(cs[i],x,p*p)-ev(cs[ref],x,p*p))%(p*p)
   assert residual%p==0
   rhs.append(-residual//p%p)
   second.append(sum(comb(t,2)*(cs[i][t]-cs[ref][t])*pow(x,t-2,p) for t in range(2,k))%p)
 assert len(J)==260
 t=next(t for t in range(k) if (cs[1][t]-cs[0][t])%p)
 fixed=[0,1,2]+list(range(n,n+k))+[n+k+t]
 assert fixed==certificate['gauge_fixed_columns']
 assert (cs[1][t]-cs[0][t])%p != 0
 orbit=[]
 for j in range(k):
  z=[0]*variables
  for i in range(L):z[n+i*k+j]=1
  orbit.append(z)
 orbit.append([0]*n+[a for c in cs for a in c])
 translation=[-1%p]*n+[(j+1)*c[j+1]%p if j+1<k else 0 for c in cs for j in range(k)]
 dilation=[-x%p for x in xs]+[j*c[j]%p for c in cs for j in range(k)]
 projective=[x*x%p for x in xs]+[(k-j)*c[j-1]%p if j else 0 for c in cs for j in range(k)]
 orbit += [translation,dilation,projective]
 assert all(sum(x*y for x,y in zip(row,z))%p==0 for row in J for z in orbit)
 gauge_rank=matrix_rank([[z[j] for z in orbit] for j in fixed],p)
 assert gauge_rank==14
 for col in fixed:
  J.append([int(j==col) for j in range(variables)]);rhs.append(0)
 rank=matrix_rank(J,p);assert rank==230
 Z=certificate['kernel_basis'];free=certificate['free_columns']
 assert len(Z)==len(free)==10
 assert all(sum(x*y for x,y in zip(row,z))%p==0 for row in J for z in Z)
 assert all(z[free[j]]==int(i==j) for i,z in enumerate(Z) for j in range(10))
 # These ten independent kernel vectors span the whole kernel, by rank230.
 pairs=[(a,b) for a in range(10) for b in range(a,10)]
 quadratic=[]
 for row,(u,i,ref) in enumerate(equations):
  x=xs[u]
  derivatives=[sum(t*(z[n+i*k+t]-z[n+ref*k+t])*pow(x,t-1,p) for t in range(1,k))%p for z in Z]
  coefficients=[]
  for a,b in pairs:
   if a==b:q=Z[a][u]*derivatives[a]+second[row]*Z[a][u]**2
   else:q=Z[a][u]*derivatives[b]+Z[b][u]*derivatives[a]+2*second[row]*Z[a][u]*Z[b][u]
   coefficients.append(q%p)
  quadratic.append(coefficients)
 quadratic += [[0]*len(pairs) for _ in fixed]
 weights=certificate['quadratic_witness_rows']
 obstruction=certificate['quadratic_left_witness']
 for lam in weights+[obstruction]:
  assert len(lam)==len(J)
  assert all(sum(lam[i]*J[i][j] for i in range(len(J)))%p==0 for j in range(variables))
 forms=[[sum(lam[i]*quadratic[i][j] for i in range(len(J)))%p for j in range(len(pairs))] for lam in weights]
 assert forms==certificate['quadratic_forms']
 constants=[16,29,14,31,23,35,34,14,30]
 expected=[]
 for i in range(10):
  expected.append([(int((a,b)==(i,i))+(constants[i]*int((a,b)==(i,9)) if i<9 else 0))%p for a,b in pairs])
 assert forms==expected
 assert all(sum(obstruction[i]*quadratic[i][j] for i in range(len(J)))%p==0 for j in range(len(pairs)))
 obstruction_value=sum(x*y for x,y in zip(obstruction,rhs))%p
 assert obstruction_value==certificate['rhs_obstruction']==8
 out=dict(status='passed',p=p,incidence_equations=260,gauge_equations=14,variables=240,
  independently_computed_gauged_rank=rank,geometric_gauge_rank=gauge_rank,kernel_dimension=10,quadratic_coefficient_checks=11*len(pairs),
  quadratic_forms=['z%d^2+%d*z%d*z9'%(i,c,i) for i,c in enumerate(constants)]+['z9^2'],
  nonzero_constant_obstruction=obstruction_value,
  scope='Exact finite identities over F41, valid after every residue-field extension. The written valuation and gauge arguments exclude all mixed-characteristic DVR lifts reducing to this seed; no other seed is excluded.')
 (BASE/'ramified_obstruction_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
