"""Direct replay of primary equations (61)--(63), not a received-word scan."""
import json
from pathlib import Path
out=[]
for p in (7,11,19,41,101):
 m,c,B,N,A=6,3,12*p,9*p*p,4*p
 H=40*B
 by_t=[sum(max(m*A-2*t+b,0) for b in range(min(t,c)+1)) for t in range(B+1)]
 ranks=[sum(int(s+t<m*A)*min(m-s,max(0,min(t,s)-max(0,t-c)+1)) for t in range(B+1)) for s in range(m)]
 rt=[sum(int(s+t<m*A)*min(m-s,max(0,min(t,s)-max(0,t-c)+1)) for s in range(m)) for t in range(B+1)]
 G=sum(by_t);R=sum(ranks)
 assert G==4*B*B-2*B and ranks==[4,8,12,15,14,9] and R==62
 conservative=(H-B+1)*G-(H+1)*N*R
 assert conservative==B*(144*p*p-936*p)+18*p*p-24*p>0
 exact=sum((H-t+1)*(g-N*r) for t,g,r in zip(range(B+1),by_t,rt))
 assert exact>=conservative
 out.append(dict(p=p,G=G,R=R,local_ranks=ranks,conservative_margin=conservative,graded_margin=exact))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
