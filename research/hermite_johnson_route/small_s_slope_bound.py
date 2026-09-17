"""Exact rational upper bound on full-box affine-L nullity slope for all m."""
from fractions import Fraction as F
from pathlib import Path
import json
n=262144;w=131071;A=181275;c=F(w-1,w)
rows=[]
for s in range(4):
 a=F(A*A,w)-n
 b=A*(1-c*s)-n*(1-s)
 cc=w*(-c*s/2+c*c*s*(2*s+1)/6+F(1,4))-F(n*s*(2*s+1),3)
 lower=max(1,2*s)
 vertex=-b/(2*a)
 point=max(F(lower),vertex)
 maximum=a*point*point+b*point+cc
 assert a<0 and maximum<0
 rows.append(dict(S=s,m_lower=lower,quadratic=[str(a),str(b),str(cc)],maximizer_on_real_domain=str(point),upper_bound_maximum=str(maximum),upper_bound_float=float(maximum)))
out=dict(target_A=A,target_agreement_fraction=A/n,small_S_best_tested_A=183960,small_S_best_tested_fraction=183960/n,rows=rows,scope='For automatic untrimmed source and m>=max(1,2S), proves affine-L nullity slope negative for all multiplicities. Does not alone exclude positive intercept at smaller L or all trimmed supports.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
