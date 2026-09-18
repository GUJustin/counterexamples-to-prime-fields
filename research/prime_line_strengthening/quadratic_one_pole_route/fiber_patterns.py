from itertools import combinations
from pathlib import Path
import json
p=29;z=pow(2,4,p);assert pow(z,7,p)==1 and z!=1
eta=sum(pow(z,j,p) for j in [1,2,4])%p;alpha=(eta-1)*pow(2,-1,p)%p;c=3*(eta+3)*pow(4,-1,p)%p
base=[pow(z,i,p) for i in range(7)]+[alpha*pow(z,i,p)%p for i in range(7)]
word=[pow(z,5*i,p) for i in range(7)]+[c*pow(z,5*i,p)%p for i in range(7)]
def P(x):return (eta*x**3+x*x+x-1-eta)%p
masks=[[i for i in range(7) if pow(z,5*i,p)*P(x*pow(z,-i,p)%p)%p==y] for x,y in zip(base,word)]
assert list(map(len,masks))==[4]*7+[3]*7
patterns=[];counts=[]
for f in range(4):
 n=0
 for F in combinations(range(14),f):
  left=[sum(i in masks[j] for j in F) for i in range(7)]
  for E in combinations([j for j in range(14) if j not in F],f):
   right=[sum(i in masks[j] for j in E) for i in range(7)]
   if all(a<=b for a,b in zip(left,right)):
    patterns.append(dict(full=F,empty=E));n+=1
 counts.append(dict(full=f,patterns=n,signed_assignments=n*2**(14-2*f)))
out=dict(p=p,zeta=z,eta=eta,alpha=alpha,c=c,base=base,word=word,masks=masks,counts=counts,patterns=patterns)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(counts)
