"""Exact finite interpolation counts; no numerical optimization or score claim."""
import json
from pathlib import Path
n=10000;D=2500;A=4220;L=100;e=100;u=0;s=n
b=A-u-(L-1)-e
rows=[]
for M in [16,32]:
 T=M*b-1;B=T//D;V=sum(T-D*j+1 for j in range(B+1));c=(M+1)**2//4
 assert c==sum(M-2*j for j in range((M-1)//2+1))
 gap=V-s*c;assert gap>0
 H=s*c*B//gap
 unknowns=(H+1)*V;constraints=s*c*(H+B+1)
 assert unknowns>constraints and T<M*b
 rows.append(dict(M=M,T=T,B=B,H=H,coefficient_volume=V,local_conditions=c,unknowns=unknowns,constraint_upper_bound=constraints,strict_dimension_slack=unknowns-constraints))
out=dict(n=n,D=D,A=A,regular_cutoff=L,outside_singular_allowance=e,ordinary_core=u,Hermite_core=s,forced_jet_matches=b,Johnson_slack_twice=2*b*b-D*s,rows=rows,scope='Exact interpolation existence only; specialization-safe algebraic-root theorem supplies full-support line bound. Not a numerical better.codes improvement.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
