"""Cubic Kuranishi coefficient test for the previously selected pattern only."""
from pathlib import Path
from itertools import combinations_with_replacement
import json
import numpy as np
from ramified_quadratic_one import rref
BASE=Path(__file__).resolve().parent;p=41;h=5;zero=(0,)*h

def exponent(ids):
 z=[0]*h
 for i in ids:z[i]+=1
 return tuple(z)
mons={d:[exponent(ids) for ids in combinations_with_replacement(range(h),d)] for d in range(4)}
def mul(a,b,cap):
 out={}
 for x,u in a.items():
  for y,v in b.items():
   z=tuple(i+j for i,j in zip(x,y))
   if sum(z)<=cap:out[z]=(out.get(z,0)+u*v)%p
 return {z:v for z,v in out.items() if v}
def add(a,b):
 out=dict(a)
 for z,v in b.items():out[z]=(out.get(z,0)+v)%p
 return {z:v for z,v in out.items() if v}
def main():
 data=json.loads((BASE/'results.json').read_text());cert=json.loads((BASE/'ramified_quadratic_one.json').read_text());pat=data['rows'][cert['pattern_index']];xs=data['nodes'];cs=[data['polynomials'][i] for i in pat['ids']];eq=pat['equations'];Z=np.array(cert['kernel'],dtype=np.int64);J=[];rhs=[]
 for node,a,b in eq:
  x=xs[node];row=[0]*200
  row[node]=sum(j*(cs[a][j]-cs[b][j])*pow(x,j-1,p) for j in range(1,10))%p
  for j in range(10):row[40+10*a+j]=pow(x,j,p);row[40+10*b+j]=-pow(x,j,p)%p
  val=sum((cs[a][j]-cs[b][j])*pow(x,j,p*p) for j in range(10))%(p*p)
  assert val%p==0;J.append(row);rhs.append(-val//p%p)
 for c in cert['gauge_columns']:
  row=[0]*200;row[c]=1;J.append(row);rhs.append(0)
 J=np.array(J,dtype=np.int64);rhs=np.array(rhs,dtype=np.int64);R,piv,U=rref(J);rank=len(piv);C=U[rank:]
 constants=xs+[v for c in cs for v in c]
 def evaluate(W,cap):
  vars=[]
  for i,c in enumerate(constants):
   a={zero:c%p}
   for j,mon in enumerate(mons[1]):a[mon]=int(Z[i,j])
   if W is not None:
    for j,mon in enumerate(mons[2]):a[mon]=int(W[i,j])
   vars.append({z:v for z,v in a.items() if v})
  powers=[]
  for node in range(40):
   row=[{zero:1}]
   for j in range(1,10):row.append(mul(row[-1],vars[node],cap))
   powers.append(row)
  out=[]
  for node,a,b in eq:
   val={}
   for j in range(10):
    diff=add(vars[40+10*a+j],{z:-v%p for z,v in vars[40+10*b+j].items()})
    val=add(val,mul(diff,powers[node][j],cap))
   out.append(val)
  for c in cert['gauge_columns']:out.append(add(vars[c],{zero:-constants[c]%p}))
  return out
 old=evaluate(None,2);Q=np.array([[row.get(mon,0) for mon in mons[2]] for row in old],dtype=np.int64)
 assert not np.any(C@Q%p)
 W=np.zeros((200,len(mons[2])),dtype=np.int64);target=-U@Q%p
 for i,col in enumerate(piv):W[col]=target[i]
 assert not np.any((J@W+Q)%p)
 new=evaluate(W,3)
 assert all(row.get(mon,0)==0 for row in new for d in range(3) for mon in mons[d])
 T=np.array([[row.get(mon,0) for mon in mons[3]] for row in new],dtype=np.int64)
 O=C@T%p;c=C@rhs%p;OR,op,OU=rref(O);orank=len(op)
 obs=[]
 for v in OU[orank:]:
  if int(v@c%p):
   lam=v@C%p;assert not np.any(lam@J%p);assert not np.any(lam@T%p)
   obs=[dict(lambda_vector=lam.tolist(),residual=int(lam@rhs%p))];break
 out=dict(pattern_index=cert['pattern_index'],normalized_rank=rank,tangent_dimension=h,quadratic_monomials=mons[2],cubic_monomials=mons[3],quadratic_correction=W.tolist(),cubic_coefficients=T.tolist(),cubic_cokernel_coefficients=O.tolist(),cubic_cokernel_rank=orank,constant_obstruction=obs,status='constant_residual_outside_cubic_span' if obs else 'span_compatible_only')
 (BASE/'ramified_cubic_one.json').write_text(json.dumps(out,indent=2)+'\n')
 print(dict(pattern_index=out['pattern_index'],cubic_cokernel_rank=orank,cubic_monomials=len(mons[3]),status=out['status'],residual=obs[0]['residual'] if obs else None))
if __name__=='__main__':main()
