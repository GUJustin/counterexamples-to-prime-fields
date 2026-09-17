import json
from pathlib import Path
import repaired_primary_chain as P
ROOT=Path(__file__).resolve().parent
ns={'__file__':str(ROOT/'audit_primary_sensitivity.py')};exec((ROOT/'audit_primary_sensitivity.py').read_text().split('rows=[]')[0],ns)
C=ns['coeff'];R=ns['rank'];n=P.N;w=P.W;A=P.A
assert P.residual_pair((185,40,18992),(312,70,9281),181284)==1057030663884726
# Check polynomial chain numerator against explicit sum of asymmetric stages.
def leftnum(y,z,d,j,A):
 g=A-w;e=n-A;v=P.mixed((y,d-j,z),(y,d,z));av=P.agreement((y,d-j,z))
 return (n-w)*sum(x*y for x,y in zip(v,av))+(e+1)*g*v[2]
for A0 in [181284,A]:
 for y,z in [(1,1),(185,22192),(189,18812)]:
  for d in range(1,43):
   k=(n-w)*(z+y+4*w*y*z)+(A0-w)*(n-A0+1)*y;m=(n-w)*w*y*z
   assert 2*sum(leftnum(y,z,d,j,A0) for j in range(1,d))==(d-1)*(3*d*k+4*m*(d-1))
rows=[]
for name,m,L,s in [('preserve_B_caps',134,22192,40),('smaller_B_total',137,18812,42)]:
 D=m*A;Y=(D-1)//w;c=C(A,m,L,s);rank=R(m,L,s);assert c>n*rank
 tail=P.tight_tail(D,L);assert tail<=P.TAIL_ALLOWANCE
 pair=P.residual_pair((Y,s,L),(312,70,9682));mix=P.mixed((Y,s,L),(312,70,9682))
 gates=dict(positive_kernel=c>n*rank,shape=D+s<=w*(Y+1),weighted_below_char=D<P.PRIME,left_degrees_below_char=max(Y,s,L)<P.PRIME,pair_mixed_below_char=max(mix)<P.PRIME,chain_mixed_below_char=max(2*s*L,2*Y*L,2*Y*s)<P.PRIME,tail_mixed_below_char=2*Y*L<P.PRIME,tail_allowance_retained=tail<=P.TAIL_ALLOWANCE)
 assert all(gates.values())
 pot=P.initial_potential(Y,s,9678)
 locs=[(35,159,9249),(36,163,9253),(36,163,9678)]
 rows.append(dict(name=name,m=m,s=s,Y=Y,L=L,D=D,coefficients=c,rank=rank,nullity=c-n*rank,tail_exact_cap=tail,tail_allowance=P.TAIL_ALLOWANCE,residual_pair_cap=pair,pair_mixed=mix,initial_A_potential=pot,gates=gates,overheads=[dict(r=r,y=y,t=t,value=P.ledger_overhead(r,y,t,B=(Y,s,L))) for r,y,t in locs]))
out=dict(target_A=A,TCap=dict(Y=312,s=70,L=9682,total=9678),primary_A=dict(Y=163,s=36,L=176421),candidates=rows,chain_sum_identity_checked_through_d=42,scope='Exact source, pair, tail, chain arithmetic and stated characteristic gates; no Lean target port or final ledger claim.')
(ROOT/'primary_B_chain_repair.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(rows,indent=2))
