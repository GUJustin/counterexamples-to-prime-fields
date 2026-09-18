"""Exact root-incidence census and up-to-three-coordinate padding optimization."""
import json,itertools,time
from pathlib import Path
import sympy as s
P=Path(__file__).parent;start=time.monotonic();data=json.loads((P/'pair_padding_gate.json').read_text());base=json.loads((P/'rational_seed.json').read_text());x=s.Symbol('x');cs=[s.Poly(sum(s.Rational(v)*x**j for j,v in enumerate(r['coefficients'])),x) for r in data['candidates']];old=list(map(s.Rational,base['affine_nodes']));factors={}
for i,j in itertools.combinations(range(8),2):
 for f,e in s.factor_list(cs[i]-cs[j])[1]:
  f=f.monic()
  if any(f.eval(a)==0 for a in old):continue
  factors[tuple(f.all_coeffs())]=f
records=[];options=[]
for z,(key,f) in enumerate(factors.items()):
 classes={}
 for i,c in enumerate(cs):classes.setdefault(tuple(c.rem(f).all_coeffs()),[]).append(i)
 groups=[g for g in classes.values() if len(g)>1]
 records.append({'factor':str(f.as_expr()),'degree':f.degree(),'groups':groups})
 for root in range(f.degree()):
  for g in groups:options.append(((z,root),sum(1<<i for i in g)))
# Infinity is a legitimate fresh projective node; values are cubic leading coefficients.
inf={}
for i,c in enumerate(cs):inf.setdefault(c.nth(3),[]).append(i)
ig=list(inf.values())
for g in ig:options.append((('infinity',0),sum(1<<i for i in g)))
# Generic singleton nodes can always be selected avoiding all finite intersections.
for i in range(8):
 for k in range(3):options.append((('generic',i,k),1<<i))
best={}
for n in [1,2,3]:
 mx=-1;examples=[]
 for inds in itertools.combinations(range(len(options)),n):
  chosen=[options[i] for i in inds]
  if len({a for a,b in chosen})<n:continue
  counts=[sum((mask>>i)&1 for _,mask in chosen) for i in range(8)];prom=[i for i,v in enumerate(counts) if v>=2]
  if len(prom)>mx:mx=len(prom);examples=[]
  if len(prom)==mx and len(examples)<20:examples.append({'options':inds,'promoted':prom,'counts':counts})
 best[n]={'maximum_promoted':mx,'examples':examples}
out={'factor_incidence':records,'infinity_groups':ig,'options':[{'coordinate':a,'mask':b} for a,b in options],'best':best,'seconds':time.monotonic()-start}
(P/'batch_padding_gate.json').write_text(json.dumps(out,indent=2));print('factors',len(records),'maxgroup',max(len(g) for r in records for g in r['groups']));print('infinity',ig);print({n:v['maximum_promoted'] for n,v in best.items()});print('seconds',out['seconds'])
