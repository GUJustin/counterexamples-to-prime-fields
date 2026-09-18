"""Reverse accumulation cancels internal rational denominators before clearing."""
import gzip,json,time,math
from pathlib import Path
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import sympy as S
r=Path(__file__).parent;start=time.monotonic();R,*vs=ring('t,v,w,z',QQ);d=json.load(gzip.open(r/'orbit7_identity_certificate.json.gz','rt'))
def dec(a):return R.from_dict({tuple(m):QQ(int(n),int(z)) for m,n,z in a})
def enc(p):return [[list(m),str(c.numerator),str(c.denominator)] for m,c in sorted(p.items())]
P=[dec(a['polynomial']) for a in d['nodes']];terms=[[(j,dec(c)) for j,c in a.get('terms',[])] for a in d['nodes']]
targets=['(z-1)*(w*w+w-z)','(z-1)*(w*z-2*w+z-1)','(z-1)*(v-z+1)'];cert=[];summ=[]
for text in targets:
 target=R.from_expr(S.sympify(text));idx=next(i for i in d['outputs'] if P[i]==target);weights={idx:R.one};inputs={}
 for i in reversed(range(idx+1)):
  a=weights.pop(i,None)
  if a is None or not a:continue
  if d['nodes'][i]['kind']=='input':inputs[i]=a;continue
  for j,c in terms[i]:
   weights[j]=weights.get(j,R.zero)+a*c
 assert not weights
 assert sum((a*P[i] for i,a in inputs.items()),R.zero)==target
 den=math.lcm(*(int(c.denominator) for a in inputs.values() for c in a.values()))
 # Integer identity: den*target=sum(integer_multiplier*input).
 integer={i:a*den for i,a in inputs.items()};assert all(c.denominator==1 for a in integer.values() for c in a.values())
 rec={'target':text,'denominator':str(den),'terms':[{'input_index':i,'label':d['nodes'][i]['label'],'input':enc(P[i]),'integer_multiplier':enc(a)} for i,a in integer.items()]};cert.append(rec)
 summ.append({'target':text,'denominator':str(den) if len(str(den))<500 else None,'denominator_digits':len(str(den)),'inputs':len(inputs),'total_multiplier_monomials':sum(len(a) for a in inputs.values()),'seconds':time.monotonic()-start})
 print(json.dumps(summ[-1]),flush=True)
with gzip.open(r/'orbit7_expanded_integer_certificate.json.gz','wt') as f:json.dump({'variables':['t','v','w','z'],'identities':cert},f,separators=(',',':'))
(r/'orbit7_expanded_integer_summary.json').write_text(json.dumps(summ,indent=2)+'\n')
