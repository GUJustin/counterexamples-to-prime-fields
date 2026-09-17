"""Exhaustive small-field check of direction-only CA exclusion and line labels."""
from itertools import product
from pathlib import Path
from math import comb
import json
p=11;old=(1,2,3,4);new=(0,5,6);points=old+new;K=2;T=3
word=tuple(pow(x,-1,p) for x in old)
polys=list(product(range(p),repeat=K))
values={P:tuple((P[0]+P[1]*x)%p for x in points) for P in polys}
M=max(sum(v==w for v,w in zip(values[P],word)) for P in polys);assert M==T-1
bank=[P for P in polys if sum(v==w for v,w in zip(values[P],word))==M];assert len(bank)==6
good=[];hist={}
for tail in product(range(1,p),repeat=len(new)):
 direction=(0,)*len(old)+tail
 maximum=max(sum(v==d for v,d in zip(values[P],direction)) for P in polys if P!=(0,0))
 hist[maximum]=hist.get(maximum,0)+1
 if maximum<T:good.append(tail)
assert len(good)==140
tail=good[0];direction=(0,)*len(old)+tail
best=-1;chosen=None;chosen_labels=None
for intercept in product(range(p),repeat=len(new)):
 labels=set()
 for j,(d,f) in enumerate(zip(tail,intercept),start=len(old)):
  labels.update((values[P][j]-f)*pow(d,-1,p)%p for P in bank)
 if len(labels)>best:best=len(labels);chosen=intercept;chosen_labels=labels
received=word+chosen
near=[]
for t in range(p):
 wt=tuple((f+t*d)%p for f,d in zip(received,direction))
 mx=max(sum(v==w for v,w in zip(values[P],wt)) for P in polys)
 if mx>=T:near.append(t)
assert chosen_labels.issubset(near)
ordinary_max=max(sum(a==f and b==d for a,b,f,d in zip(values[A],values[B],received,direction)) for A in polys for B in polys)
assert ordinary_max<T
# Exact parameter inequalities, including the special n^2/192 constant.
cases=0
for r in range(40,401):
 for m in range((3*r+1)//2,5*r//3+1):
  Delta=m-r+1;s=2*Delta-r+1;Nc=3*r+2*Delta;t=14*Delta-3*r
  assert 1<=s<=Delta and Nc+t==16*Delta
  assert t>=8*Delta and t<=7*r
  assert 9*r>=2*(3*r+2*Delta+1) # ell >= 2Delta/3
  assert (4*r+1)**2-Nc>=r*(2*Delta-1)
  assert t*r<=2*(4*r+1)**2
  for b in (2,3,4,5):
   assert b*Delta-1<4*r+1
   assert b*Delta-r+1<=(b-1)*Delta
   assert 3*r+b*Delta+1<=(b+6)*Delta
   assert (4*r+1)**2-(3*r+b*Delta)>=r*(b*Delta-1)
  cases+=1
out=dict(status='passed',p=p,length=len(points),dimension=K,threshold=T,core_maximum=M,core_nearest_list=len(bank),nonzero_direction_assignments=(p-1)**len(new),good_direction_assignments=len(good),nonzero_polynomial_direction_maximum_histogram=hist,chosen_direction=direction,chosen_intercept=received,counted_labels=sorted(chosen_labels),all_near_labels=near,maximum_ordinary_correlated_agreement=ordinary_max,parameter_cases=cases,scope='All1000 nonzero direction assignments and all polynomial witnesses checked over F11; chosen line independently checked for all labels and all121^2 ordinary-CA witness pairs. Parameter checks do not substitute for asymptotic probability proof.')
Path(__file__).with_name('random_direction_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
