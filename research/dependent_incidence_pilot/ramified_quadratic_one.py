"""One prescribed saved pattern: maximal tangent dimension, no seed search."""
from pathlib import Path
import json
import numpy as np
BASE=Path(__file__).resolve().parent
P=41

def rref(a):
 a=np.array(a,dtype=np.int64)%P;m,n=a.shape;ops=np.eye(m,dtype=np.int64);piv=[];r=0
 for col in range(n):
  ix=np.flatnonzero(a[r:,col])
  if not len(ix):continue
  j=r+int(ix[0]);a[[r,j]]=a[[j,r]];ops[[r,j]]=ops[[j,r]]
  inv=pow(int(a[r,col]),-1,P);a[r]=a[r]*inv%P;ops[r]=ops[r]*inv%P
  v=a[:,col].copy();v[r]=0;a=(a-v[:,None]*a[r])%P;ops=(ops-v[:,None]*ops[r])%P
  piv.append(col);r+=1
  if r==m:break
 return a,piv,ops

def main():
 data=json.loads((BASE/'results.json').read_text());idx=min(range(len(data['rows'])),key=lambda i:(data['rows'][i]['rank'],i));pat=data['rows'][idx]
 xs=data['nodes'];cs=[data['polynomials'][i] for i in pat['ids']];eq=pat['equations'];rows=[];rhs=[]
 for xidx,a,b in eq:
  x=xs[xidx];row=[0]*200
  row[xidx]=sum(j*(cs[a][j]-cs[b][j])*pow(x,j-1,P) for j in range(1,10))%P
  for j in range(10):row[40+10*a+j]=pow(x,j,P);row[40+10*b+j]=-pow(x,j,P)%P
  val=sum((cs[a][j]-cs[b][j])*pow(x,j,P*P) for j in range(10))%(P*P)
  assert val%P==0;rhs.append(-val//P%P);rows.append(row)
 gauge=[xs.index(x) for x in [1,2,3]]+list(range(40,50))
 j=next(j for j in range(10) if (cs[1][j]-cs[0][j])%P);gauge.append(50+j)
 for col in gauge:
  row=[0]*200;row[col]=1;rows.append(row);rhs.append(0)
 J=np.array(rows,dtype=np.int64);b=np.array(rhs,dtype=np.int64)
 R,piv,U=rref(J);rank=len(piv);free=[j for j in range(200) if j not in piv];h=len(free)
 Z=np.zeros((200,h),dtype=np.int64)
 for t,col in enumerate(free):
  Z[col,t]=1
  for i,c in enumerate(piv):Z[c,t]=-R[i,col]%P
 assert not np.any(J@Z%P)
 mons=[(i,j) for i in range(h) for j in range(i,h)]
 def quad(v):
  out=[]
  for xidx,a,b in eq:
   x=xs[xidx];vx=int(v[xidx])
   sec=sum(j*(j-1)//2*(cs[a][j]-cs[b][j])*pow(x,j-2,P) for j in range(2,10))
   cross=sum(j*(int(v[40+10*a+j])-int(v[40+10*b+j]))*pow(x,j-1,P) for j in range(1,10))
   out.append((sec*vx*vx+cross*vx)%P)
  return np.array(out+[0]*14,dtype=np.int64)
 diag=[quad(Z[:,i]) for i in range(h)]
 Q=np.column_stack([diag[i] if i==j else (quad(Z[:,i]+Z[:,j])-diag[i]-diag[j])%P for i,j in mons])
 C=U[rank:];T=C@Q%P;c=C@b%P
 TR,tp,TU=rref(T);trank=len(tp)
 witnesses=[]
 for row in TU[trank:]:
  if int(row@c%P):
   lam=row@C%P;assert not np.any(lam@J%P);assert not np.any(lam@Q%P)
   witnesses.append(dict(lambda_vector=lam.tolist(),residual=int(lam@b%P)));break
 # Express each square as a linear combination of cokernel quadratic forms.
 RR,pp,UU=rref(T.T)
 squares=[]
 for i in range(h):
  target=np.array([int(a==b==i) for a,b in mons],dtype=np.int64)
  ub=UU@target%P
  if any(ub[j] for j in range(len(pp),len(ub))):continue
  sol=np.zeros(T.shape[0],dtype=np.int64)
  for j,col in enumerate(pp):sol[col]=ub[j]
  assert np.array_equal(sol@T%P,target)
  lam=sol@C%P;squares.append(dict(index=i,lambda_vector=lam.tolist()))
 out=dict(pattern_index=idx,mode=pat['mode'],trial=pat['trial'],ids=pat['ids'],original_rank=pat['rank'],normalized_rank=rank,gauge_columns=gauge,tangent_dimension=h,quadratic_monomials=mons,cokernel_dimension=len(C),quadratic_rank=trank,kernel=Z.tolist(),constant_obstruction=witnesses,square_certificates=squares,all_tangent_squares_certified=len(squares)==h)
 (BASE/'ramified_quadratic_one.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['ids','kernel','constant_obstruction','square_certificates','quadratic_monomials']}))
 print('constant obstruction',bool(witnesses),'squares',len(squares),'of',h)
if __name__=='__main__':main()
