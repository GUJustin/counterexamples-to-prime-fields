import json,itertools
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).parent;s=json.loads((P/'rational_seed.json').read_text());t=json.loads((P/'ten_cubic_certificate.json').read_text());s={'nodes':s['affine_nodes'],'word':s['affine_word'],'polynomials':s['affine_polynomials']+t['new_candidate_coefficients']}
for p in [101,103,107,109,127,1009,10847]:
 def red(a):a=F(a);return a.numerator*pow(a.denominator,-1,p)%p
 try:xs=list(map(red,s['nodes']));ys=list(map(red,s['word']));ps=[tuple(map(red,c)) for c in s['polynomials']]
 except ValueError:continue
 roots=[u for u in range(p) if (358*u*u+125*u-25)%p==0]
 if len(roots)!=2 or any(u in xs for u in roots):continue
 xs+=roots;ys+=[(-104594*u-51075)*pow(32041,-1,p)%p for u in roots]
 if len(set(xs))!=18:continue
 seen=set();hist={};near=[]
 for S in itertools.combinations(range(18),4):
  a=[[pow(xs[i],j,p) for j in range(4)]+[ys[i]] for i in S]
  for c in range(4):
   z=next(i for i in range(c,4) if a[i][c]);a[z],a[c]=a[c],a[z];iv=pow(a[c][c],-1,p);a[c]=[v*iv%p for v in a[c]]
   for i in range(4):
    if i!=c:
     t=a[i][c];a[i]=[(v-t*w)%p for v,w in zip(a[i],a[c])]
  cc=tuple(r[4] for r in a)
  if cc in seen:continue
  seen.add(cc);n=sum(sum(v*pow(x,j,p) for j,v in enumerate(cc))%p==y for x,y in zip(xs,ys));hist[n]=hist.get(n,0)+1
  if n>=7:near.append(cc)
 if set(near)==set(ps) and max(hist)==7:break
assert set(near)==set(ps) and max(hist)==7
out={'p':p,'nodes':xs,'word':ys,'polynomials':ps,'histogram':hist,'complete_nearest_list':10,'maximum_agreement':7};(P/'ten_cubic_modular.json').write_text(json.dumps(out,indent=2)+'\n');print('prime',p,'hist',hist)
