import json
from pathlib import Path
from fractions import Fraction
P=Path(__file__).parent;ns={'Fraction':Fraction};src=(P/'lift15.py').read_text();exec(src[src.index('class Ring:'):src.index('r=Ring(17)')],ns);Ring=ns['Ring'];r=Ring(17)
d=json.loads((P/'lift15.json').read_text());case=d['cases'][8];seed=json.loads((P.parent/'rational_seed.json').read_text());support=case['support'];Uraw=[seed['affine_nodes'][i//3] for i in support];Wraw=[seed['affine_word'][i//3] for i in support]
v=[tuple(x%17 for x in t) for t in case['normalized_lift_coefficients']]+[(15,0),(0,0),(0,0),(11,0),(0,0),(0,0),(0,0)]+[tuple(x%17 for x in d['lifted_nodes'][i]) for i in support]
free=[12,13,14];cols=[i for i in range(32) if i not in free]
def system(R,v,jac=False):
 rows=[];values=[];A=v[10:14];B=[(1,0)]+v[14:17];H=v[:10];da=[R.mul((j,0),A[j]) for j in range(1,4)];db=[R.mul((j,0),B[j]) for j in range(1,4)];dh=[R.mul((j,0),H[j]) for j in range(1,10)]
 for k,t in enumerate(v[17:]):
  u=R.rat(Uraw[k]);w=R.rat(Wraw[k]);b=R.ev(B,t);powt=[R.pow(t,j) for j in range(10)]
  values.append(R.sub(R.ev(A,t),R.mul(u,b)));values.append(R.sub(R.ev(H,t),R.mul(w,R.pow(b,3))))
  if jac:
   rr=[(0,0)]*32;ss=[(0,0)]*32
   for j in range(4):rr[10+j]=powt[j]
   for j in range(1,4):rr[13+j]=R.n(R.mul(u,powt[j]));ss[13+j]=R.n(R.mul(R.mul((3,0),R.mul(w,R.pow(b,2))),powt[j]))
   rr[17+k]=R.sub(R.ev(da,t),R.mul(u,R.ev(db,t)));ss[17+k]=R.sub(R.ev(dh,t),R.mul(R.mul((3,0),R.mul(w,R.pow(b,2))),R.ev(db,t)))
   for j in range(10):ss[j]=powt[j]
   rows.extend([[rr[c] for c in cols],[ss[c] for c in cols]])
 return values,rows
vals,J=system(r,v,True);assert all(x==(0,0) for x in vals);a=[row[:] for row in J];E=[[(int(i==j),0) for j in range(30)] for i in range(30)];rank=0
for c in range(29):
 z=next(i for i in range(rank,30) if a[i][c]!=(0,0));a[z],a[rank]=a[rank],a[z];E[z],E[rank]=E[rank],E[z];iv=r.inv(a[rank][c]);a[rank]=[r.mul(x,iv) for x in a[rank]];E[rank]=[r.mul(x,iv) for x in E[rank]]
 for i in range(30):
  if i!=rank:
   t=a[i][c];a[i]=[r.sub(x,r.mul(t,y)) for x,y in zip(a[i],a[rank])];E[i]=[r.sub(x,r.mul(t,y)) for x,y in zip(E[i],E[rank])]
 rank+=1
M=17;checks=[];obstruction=None
for exponent in range(2,33):
 RR=Ring(M*17);res,_=system(RR,v)
 assert all(x%M==0 for t in res for x in t)
 rhs=[r.n(tuple(x//M for x in t)) for t in res];corr=[]
 for row in E:
  z=(0,0)
  for x,y in zip(row,rhs):z=r.a(z,r.mul(x,y))
  corr.append(z)
 if corr[29]!=(0,0):obstruction={'next_exponent':exponent,'left_null_rhs':corr[29],'defect_div_previous_modulus':[tuple(x//M for x in t) for t in res]};break
 for c,delta in zip(cols,corr[:29]):v[c]=tuple(a+M*b for a,b in zip(v[c],delta))
 M*=17;res,_=system(Ring(M),v);assert all(t==(0,0) for t in res);checks.append(exponent)
out={'case':8,'support':support,'fixed_variables':free,'fixed_values':[v[c] for c in free],'rank':rank,'modulus':M,'verified_exponents':checks,'obstruction':obstruction,'coordinates':v,'variable_order':'H0..9,A0..3,B1..3,15 matched T-nodes','left_null':E[29]};(P/'lift15_general_hensel.json').write_text(json.dumps(out,indent=2)+'\n');print('verified',checks,'obstruction',obstruction)
