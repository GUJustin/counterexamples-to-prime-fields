"""Independent exhaustive polynomial identities and actual domain agreements."""
from itertools import product
from pathlib import Path
import json

def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a

def add(a,b,p):return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p for i in range(max(len(a),len(b)))])
def neg(a,p):return [(-v)%p for v in a]
def mul(a,b,p):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
 return trim(out)
def scale(a,c,p):return trim([v*c%p for v in a])
def deriv(a,p):return trim([i*a[i]%p for i in range(1,len(a))] or [0])
def ev(a,x,p):
 out=0
 for v in a[::-1]:out=(out*x+v)%p
 return out

def mon(d,c=1):return [0]*d+[c]
def locator(nodes,p):
 T=[1]
 for x in nodes:T=mul(T,[-x%p,1],p)
 return T

def solve(p,D,T,RS,nodes,recv):
 sols=[];tested=0
 data=[RS(z) for z in range(p)]
 for coeff in product(range(p),repeat=D+1):
  P=list(coeff);base=add(mul(T,deriv(P,p),p),neg(mul(P,P,p),p),p)
  for z,(R,S) in enumerate(data):
   tested+=1
   E=add(add(base,mul(R,P,p),p),neg(S,p),p)
   if any(E):continue
   vals=recv(z)
   agree=[x for x,w in zip(nodes,vals) if ev(P,x,p)==w]
   sols.append((z,coeff,agree))
 return sols,tested
out=[]
for p,D in [(7,1),(11,2)]:
 t=4*D+1;nodes=list(range(t));T=locator(nodes,p)
 def branches(z):return scale(mon(D+1),z,p),add(add(mon(t-2,1+z),[1],p),mon(1,z),p)
 def RS(z):
  F,G=branches(z);return add(F,G,p),mul(F,G,p)
 sols,tested=solve(p,D,T,RS,nodes,lambda z:[ev(branches(z)[0],x,p) for x in nodes])
 assert any(z==0 and not any(P) for z,P,_ in sols)
 assert len({z for z,_,_ in sols})<=4*D+4
 out.append({'kind':'two-high-branches','p':p,'D':D,'pairs_tested':tested,'solutions':len(sols),'labels':sorted({z for z,_,_ in sols}),'agreement_counts':[len(a) for _,_,a in sols]})
# Low-branch persistent pencils, with actual agreement on the other branch.
p=7;D=1;nodes=list(range(5));T=locator(nodes,p);TdivX=T[1:]
def lowRS(z):
 G=add(mon(1,z),neg(TdivX,p),p);return G,[0]
sols,tested=solve(p,D,T,lowRS,nodes,lambda z:[ev(lowRS(z)[0],x,p) for x in nodes])
nonlow=[(z,P,a) for z,P,a in sols if any(P)]
assert len({z for z,_,_ in nonlow})>=3
assert all(P==(0,z) for z,P,_ in nonlow)
assert all(len(a)>=len(nodes)-D for _,_,a in nonlow)
out.append({'kind':'persistent-two-pencils','p':p,'D':D,'pairs_tested':tested,'solutions':len(sols),'nonzero_solutions':len(nonlow),'nonzero_agreements':[len(a) for _,_,a in nonlow]})
# Nonlinear persistent component in the general triangular family.
p=11;D=2;nodes=list(range(9));T=locator(nodes,p)
def nonlinearRS(z):
 Q=mon(2,z);R=scale(Q,2,p);S=add(add(mul(T,deriv(Q,p),p),mul(Q,Q,p),p),[-z%p],p)
 return R,S
sols,tested=solve(p,D,T,nonlinearRS,nodes,lambda z:[z*x*x%p for x in nodes])
expected={(c*c%p,(c,0,c*c%p)) for c in range(p)}
assert {(z,P) for z,P,_ in sols}==expected
assert all(len(a)==(len(nodes) if P[0]==0 else 0) for _,P,a in sols)
out.append({'kind':'persistent-nonlinear-component','p':p,'D':D,'pairs_tested':tested,'solutions':len(sols),'near_labels_at_A3':sorted({z for z,P,a in sols if len(a)>=3})})
result={'fixtures':out,'total_pairs':sum(r['pairs_tested'] for r in out)}
Path(__file__).with_name('finite_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
