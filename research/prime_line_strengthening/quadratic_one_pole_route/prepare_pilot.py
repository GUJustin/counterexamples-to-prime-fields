import json
from pathlib import Path
P=Path(__file__).parent;d=json.loads((P/'fiber_patterns.json').read_text());p=29
mul=lambda x,y:((x%p)*(y%p)+2*(x//p)*(y//p))%p+p*(((x%p)*(y//p)+(x//p)*(y%p))%p)
neg=lambda x:(-x%p)%p+p*(-(x//p)%p)
fibers=[]
for x in d['base']:
 roots=[u for u in range(p*p) if mul(u,u)==x];assert len(roots)==2;fibers.append(roots)
patterns=[]
for x in d['patterns']:
 key=(tuple(x['full']),tuple(x['empty']))
 rot=lambda a,k:tuple(sorted((j//7)*7+(j%7+k)%7 for j in a))
 if key==min((rot(key[0],k),rot(key[1],k)) for k in range(7)):patterns.append(x)
nodes=[u for f in fibers for u in f];words=[v for v in d['word'] for _ in range(2)]
assert len(set(nodes))==28
with (P/'pilot.in').open('w') as f:
 print(len(patterns),file=f)
 for u,v in zip(nodes,words):print(u,v,file=f)
 for pat in patterns:
  print(len(pat['full']),*pat['full'],*pat['empty'],file=f)
(P/'pilot_bank.json').write_text(json.dumps(dict(**d,cover='U^2',field='F29[j]/(j^2-2)',fibers=fibers,nodes=nodes,values=words,representative_patterns=patterns),indent=2))
print({'patterns':len(patterns),'signed_after_global_sign':sum(2**(13-2*len(x['full'])) for x in patterns)})
