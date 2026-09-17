"""Exact prime-field verification of the tie-flip line and all its labels."""
from pathlib import Path
from math import comb
import json
rows=[]
for p in [17,41,73,97,257]:
 k=(p-1)//4;n=p-1;chi=[0]*p
 for x in range(1,p):chi[x]=1 if pow(x,(p-1)//2,p)==1 else -1
 for a in [1,2]:
  G={x:sum(comb(2*k+1,2*j+1)*pow(a,2*k-2*j,p)*pow(x,j,p) for j in range(k+1))%p for x in range(1,p)}
  Wp={};Wm={}
  for x in range(1,p):
   if chi[x]<0:Wp[x]=Wm[x]=0
   else:
    s=next(s for s in range(1,p) if s*s%p==x)
    ss=chi[(s+a)%p]+chi[(s-a)%p]
    Wp[x]=1 if ss>=0 else p-1
    Wm[x]=1 if ss>0 else p-1
  T={x for x in range(1,p) if Wp[x]!=Wm[x]}
  persistent={x for x in range(1,p) if Wp[x]==Wm[x]==G[x]}
  assert len(T)==k and len(persistent)==2*k
  labels={(1-G[x])*pow(2,-1,p)%p for x in T}
  assert len(labels)==k and not labels.intersection({0,1,pow(2,-1,p)})
  counts=[]
  for z in range(p):
   support={x for x in range(1,p) if (Wp[x]+z*(Wm[x]-Wp[x]))%p==G[x]}
   assert persistent<=support and len(support)==2*k+(z in labels)
   counts.append(len(support))
  rows.append(dict(p=p,a=a,n=n,k=k,persistent_agreements=len(persistent),bad_labels=len(labels),bad_agreement=2*k+1,all_challenges_checked=p))
Path(__file__).with_name('majority_line_checks.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
