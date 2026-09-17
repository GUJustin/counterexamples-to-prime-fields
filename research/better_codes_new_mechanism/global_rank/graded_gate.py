"""Exact universal Hermite saturation and safe familywise rank-cap gate."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'better_codes_current_lower_2026_09_17'))
from affine_local_source_gate import rank
m,L,S=64000,3840000,19840;A=181275;w=131071;n=262144
D=m*A
R=min(m-1,L-S,(D-(w-1)*S)//n-1)
assert R>=0 and D-(w-1)*S>=n*(R+1)
# These first blocks have h=m-r>S, hence blockJet injective.
assert m-R>S
# Sum_{r<=R} Sum_{a<=r} Sum_{b<=S} (L+1-a-b).
K=R+1
sum_a=R*(R+1)//2;sum_a2=R*(R+1)*(2*R+1)//6
# Σa(R+1-a)*(L+1-a-S/2)*(S+1), denominator2.
saturated_twice=(S+1)*((2*(L+1)-S)*(K*K-sum_a)-2*(K*sum_a-sum_a2))
assert saturated_twice%2==0
sat=saturated_twice//2;full=rank(m,L,S)
out=dict(m=m,L=L,S=S,D=D,n=n,saturated_r_inclusive=[0,R],local_saturated_rank=sat,local_total_rank_bound=full,global_saturated_rank=n*sat,global_total_rank_bound=n*full,saturated_fraction=sat/full,source_max_X_coefficient_dimension=D,Hermite_jet_dimension_per_family=n*m,familywise_Hermite_cap_savings=0,scope='Universal surjectivity of the stated initial block projection for all distinct nodes and arbitrary received values; full-map rank is not asserted. Safe familywise min(d_ij,n*m) caps give no improvement because D<n*m.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
