"""Reduce the independent affine certificate at a short fixed list of primes."""
import json
from fractions import Fraction
from pathlib import Path
r=Path(__file__).parent;d=json.loads((r/'orbit7_independent_field_audit.json').read_text());out=[]
for p in [97,113,127,139,167,181,223,239]:
 for w in range(p):
  if (w**3+2*w*w-w-1)%p:continue
  def e(v):
   ans=0
   for i,s in enumerate(v):
    a=Fraction(s);ans+=a.numerator*pow(a.denominator,-1,p)*pow(w,i,p)
   return ans%p
  try:
   xs=list(map(e,d['affine_nodes']));ps=[[e(c) for c in q] for q in d['affine_polynomials']];ys=list(map(e,d['affine_word']))
   masks=[[i+1 for i,q in enumerate(ps) if sum(c*pow(x,j,p) for j,c in enumerate(q))%p==y] for x,y in zip(xs,ys)]
   good=len(set(xs))==14 and masks==d['agreement_masks'] and len({tuple(q) for q in ps})==7
   out.append({'prime':p,'w':w,'pass':good,'nodes':xs,'polynomials':ps,'word':ys,'masks':masks})
  except ValueError:out.append({'prime':p,'w':w,'pass':False,'reason':'denominator'})
(r/'orbit7_prime_realizations.json').write_text(json.dumps(out,indent=2)+'\n')
assert len(out)==24 and all(a['pass'] for a in out)
print('PASS: 24 conjugate reductions at eight fixed primes')
