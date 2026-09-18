"""Complete exact 7-of-14 support test for a proper numerator-degree<=4 pole."""
import runpy,json,itertools,time
from pathlib import Path
r=Path(__file__).parent;s=runpy.run_path(str(r/'orbit2_independent_field_audit.py'));K=s['K'];xs=s['tnodes'];ys=s['word'];start=time.monotonic()
# Precompute all nonzero reciprocal node differences.
di={(i,j):(xs[i]-xs[j]).inv() for i in range(14) for j in range(14) if i!=j}
def prod(vals):
 a=K(1)
 for x in vals:a=a*x
 return a
infinity_hits=[];hits=[];supports=0;bases=0;polynomial_bases=0
for base in itertools.combinations(range(12),5):
 bases+=1;last=base[-1]
 weights=[prod(di[i,j] for j in base if j!=i) for i in base]
 lc=sum((ys[i]*a for i,a in zip(base,weights)),K(0))
 extra=list(range(last+1,14));supports+=len(extra)*(len(extra)-1)//2
 if not lc:
  polynomial_bases+=1;continue
 poles={};infinity_matches=[]
 for t in extra:
  L=prod(xs[t]-xs[i] for i in base)
  val=L*sum((ys[i]*a*di[t,i] for i,a in zip(base,weights)),K(0))
  den=val-ys[t]
  if not den:
   infinity_matches.append(t);continue
  pole=xs[t]-lc*L/den
  poles.setdefault(pole.a,[]).append(t)
 if len(infinity_matches)>=2:
  infinity_hits.append({"base":base,"extra":infinity_matches})
 for key,ext in poles.items():
  if len(ext)<2:continue
  pole=K(key)
  if any(pole==x for x in xs):continue
  # Build W and L explicitly only for a potential hit.
  W=[K(0)]*5;Lpoly=[K(1)]
  def mulroot(a,x):
   b=[K(0)]*(len(a)+1)
   for j,c in enumerate(a):b[j]=b[j]-x*c;b[j+1]=b[j+1]+c
   return b
  for i,a in zip(base,weights):
   term=[K(1)]
   for j in base:
    if j!=i:term=mulroot(term,xs[j])
   for j,c in enumerate(term):W[j]=W[j]+ys[i]*a*c
  for i in base:Lpoly=mulroot(Lpoly,xs[i])
  N=mulroot(W,pole);N=[a-lc*b for a,b in zip(N,Lpoly)];assert not N[5];N=N[:5]
  def ev(a,x):
   y=K(0)
   for c in reversed(a):y=y*x+c
   return y
  assert ev(N,pole)
  matches=[i for i in range(14) if ev(N,xs[i])==(xs[i]-pole)*ys[i]]
  assert len(matches)>=7
  hit={'base':base,'matches':matches,'pole':pole.out(),'numerator':[a.out() for a in N]}
  if not any(h['pole']==hit['pole'] and h['numerator']==hit['numerator'] for h in hits):hits.append(hit);print('HIT',json.dumps(hit),flush=True)
assert supports==3432
out={'complete':True,'supports':supports,'bases':bases,'polynomial_bases':polynomial_bases,'hits':hits,'quartic_at_infinity_supports':infinity_hits,'seconds':time.monotonic()-start,'scope':'Exact second cubic-number-field coefficients; proper finite pole off the 14-node affine domain, numerator degree at most four.'}
(r/'orbit2_one_pole.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
