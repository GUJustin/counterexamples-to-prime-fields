"""Exact local profile obstruction. No global polynomial gluing is asserted."""
import json
from pathlib import Path
n=262144;w=131071;T=181275;C=6802316684345;cap=3261;r=12;p=2130706433
def mul(f,g):
 out={}
 for (i,j),v in f.items():
  for (k,l),z in g.items():out[i+k,j+l]=out.get((i+k,j+l),0)+v*z
 return {m:c for m,c in out.items() if c}
def power(f,e):
 out={(0,0):1}
 for _ in range(e):out=mul(out,f)
 return out
def add(f,g):
 out=f.copy()
 for m,c in g.items():out[m]=out.get(m,0)+c
 return {m:c for m,c in out.items() if c}
def scale(f,c):return {m:c*v for m,v in f.items() if c*v}
def ord_x(f):return min(i for (i,j),c in f.items() if c%p)
def eval_zero(f):return {(i,0):c for (i,j),c in f.items() if j==0 and c%p}
Y={(0,1):1}
def Yminus(k,c=1):return {(0,1):1,(k,0):-c}
H9={(0,17):1,(9,0):-1}
G1=mul(Yminus(1),Yminus(0))
Gram={(0,2):1,(1,0):-1}
G2=mul(Yminus(1),Yminus(1,2))
G3=mul(Yminus(1),Yminus(2))
local=[(30,0,1,9,G1,H9),(42,1,1,17,Gram,power(Yminus(1),17)),(43,2,2,9,G2,H9),(43,2,3,9,G3,H9)]
checked=[]
for a,delta,u,v,G,H in local:
 A=mul(power(G,13),H)
 contact=min(i+j+min(i,r) for (i,j),c in A.items() if c%p)
 b={(i,0):c for (i,j),c in G.items() if j==1}
 c=eval_zero(G)
 disc=add(mul(b,b),scale(c,-4))
 assert contact==a
 assert ord_x(disc)==delta
 assert ord_x(eval_zero(G))==u
 assert ord_x(eval_zero(H))==v
 assert max(j for i,j in A)==43
 checked.append(dict(a=a,delta=delta,u=u,v=v,terms=len(A)))
def box(a,b,h):return a*b*(cap+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
def rank(a):return sum(box(k+1,r+1,0)-box(max(0,2*k+1-a),max(0,r+1-a+k),a-k) for k in range(a))
profile=[(1,30,0,1,9,53342),(0,42,1,0,0,80869),(1,42,1,1,17,74593),(1,43,2,2,9,25813),(1,43,2,3,9,27527)]
tallies=dict(nodes=sum(c for s,a,d,u,v,c in profile),matches=sum(s*c for s,a,d,u,v,c in profile),discriminant=sum(d*c for s,a,d,u,v,c in profile),G_value=sum(u*c for s,a,d,u,v,c in profile),H_value=sum(v*c for s,a,d,u,v,c in profile),rank=sum(rank(a)*c for s,a,d,u,v,c in profile))
assert tallies['nodes']==n and tallies['matches']==T
assert tallies['discriminant']==tallies['G_value']==2*w
assert tallies['H_value']==17*w+12
assert tallies['rank']>=C-1
out=dict(status='PASS: joint local resources remain feasible; no global source or benchmark gain',prime=p,local_germs=checked,profile=profile,tallies=tallies,rank_required=C-1,rank_surplus=tallies['rank']-(C-1))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
