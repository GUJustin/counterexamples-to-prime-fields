from pathlib import Path
import json,random,math
import numpy as np
BASE=Path(__file__).resolve().parent
p=41;k=10;xs=[pow(6,j,p) for j in range(40)]
word=[((1+pow(x,20,p))*21-pow(x,10,p))%p for x in xs]
bank=set()
for j in range(4):
 data=json.loads((BASE.parent/'dickson_nearest_threshold'/f'bank_coset{j}.log').read_text().splitlines()[0]);bank.update(tuple(a) for a in data['values'])
def coeff(vals):
 a=list(vals[:10])
 for h in range(1,10):
  for j in range(9,h-1,-1):a[j]=(a[j]-a[j-1])*pow(xs[j]-xs[j-h],-1,p)%p
 out=[a[-1]]
 for j in range(8,-1,-1):
  z=[0]*(len(out)+1)
  for t,b in enumerate(out):z[t]=(z[t]-xs[j]*b)%p;z[t+1]=(z[t+1]+b)%p
  z[0]=(z[0]+a[j])%p;out=z
 return out
def ev(c,x,mod):
 v=0
 for a in reversed(c):v=(v*x+a)%mod
 return v
polys=[coeff(v) for v in sorted(bank)]
assert len(polys)==210
supports=[{j for j,x in enumerate(xs) if ev(c,x,p)==word[j]} for c in polys]
assert all(len(s)==15 for s in supports)
dickson={tuple(math.comb(21,2*j+1)*pow(a,20-2*j,p)%p for j in range(10)) for a in range(1,21)}
non=[i for i,c in enumerate(polys) if tuple(c) not in dickson]
rng=random.Random(20260917);patterns=[]
# Eight broad samples; eight overlap-clustered; eight balanced coverage designs.
for mode in ['broad','clustered','balanced']:
 for trial in range(8):
  selected=[non[(trial*23+(0 if mode=='broad' else 7 if mode=='clustered' else 13))%len(non)]]
  while len(selected)<16:
   candidates=[i for i in range(210) if i not in selected]
   if mode=='broad':chosen=rng.choice(candidates)
   elif mode=='clustered':
    chosen=max(candidates,key=lambda i:(sum(len(supports[i]&supports[j])**2 for j in selected),rng.random()))
   else:
    counts=[sum(x in supports[j] for j in selected) for x in range(40)]
    chosen=min(candidates,key=lambda i:(sum((counts[x]+(x in supports[i]))**2 for x in range(40)),rng.random()))
   selected.append(chosen)
  patterns.append((mode,trial,sorted(selected)))
assert len({tuple(v) for _,_,v in patterns})==24

def solve(J,b):
 rows,v=J.shape;mat=np.column_stack((J,b));ops=np.eye(rows,dtype=np.int64);pivot=[];rank=0
 for col in range(v):
  idx=np.flatnonzero(mat[rank:,col])
  if not len(idx):continue
  q=rank+int(idx[0]);mat[[rank,q]]=mat[[q,rank]];ops[[rank,q]]=ops[[q,rank]]
  inv=pow(int(mat[rank,col]),-1,p);mat[rank]=mat[rank]*inv%p;ops[rank]=ops[rank]*inv%p
  factors=mat[:,col].copy();factors[rank]=0
  mat=(mat-factors[:,None]*mat[rank])%p;ops=(ops-factors[:,None]*ops[rank])%p
  pivot.append(col);rank+=1
  if rank==rows:break
 bad=next((j for j in range(rank,rows) if mat[j,-1]),None)
 if bad is not None:
  witness=ops[bad];assert np.all(witness@J%p==0)
  return dict(rank=rank,status='obstructed_mod_p_squared',left_kernel=witness.tolist(),obstruction=int(witness@b%p))
 sol=np.zeros(v,dtype=np.int64)
 for j,col in enumerate(pivot):sol[col]=mat[j,-1]
 assert np.all(J@sol%p==b)
 return dict(rank=rank,status='first_correction_exists',correction=sol.tolist())
results=[]
for mode,trial,ids in patterns:
 cs=[polys[i] for i in ids];eq=[];rows=[];rhs=[]
 for j,x in enumerate(xs):
  inc=[a for a,i in enumerate(ids) if j in supports[i]]
  if not inc:continue
  ref=inc[0]
  for a in inc[1:]:
   row=[0]*200;row[j]=sum(t*(cs[a][t]-cs[ref][t])*pow(x,t-1,p) for t in range(1,10))%p
   for t in range(10):row[40+10*a+t]=pow(x,t,p);row[40+10*ref+t]=-pow(x,t,p)%p
   res=(ev(cs[a],x,p*p)-ev(cs[ref],x,p*p))%(p*p);assert res%p==0
   rows.append(row);rhs.append(-res//p%p);eq.append([j,a,ref])
 result=dict(mode=mode,trial=trial,ids=ids,outside_dickson=sum(i in non for i in ids),row_count=len(rows),equations=eq,**solve(np.array(rows,dtype=np.int64),np.array(rhs,dtype=np.int64)))
 results.append(result)
 print(mode,trial,result['rank'],result['status'],flush=True)
 (BASE/'results.json').write_text(json.dumps(dict(p=p,k=k,n=40,A=15,L=16,nodes=xs,polynomials=polys,rows=results,complete=len(results)==24),indent=2)+'\n')
