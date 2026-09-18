import json,itertools
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).parent;s=json.loads((P/'rational_nine.json').read_text())
for p in [101,103,107,109,127,1009,10847]:
 def red(a):a=F(a);return a.numerator*pow(a.denominator,-1,p)%p
 try:xs=list(map(red,s['nodes']));ys=list(map(red,s['word']));ps=[tuple(map(red,c)) for c in s['polynomials']]
 except ValueError:continue
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
out={'p':p,'nodes':xs,'word':ys,'polynomials':ps,'histogram':hist,'complete_nearest_list':9,'maximum_agreement':7};(P/'rational_nine_modular.json').write_text(json.dumps(out,indent=2)+'\n');print('prime',p,'hist',hist)
