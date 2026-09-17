"""Root-side exact audit of the early-phase candidate's numeric adapter gates.
Uses a direct per-slope monomial sum instead of the fast phase count formula.
Does not certify a routing threshold, full ledger, or Lean theorem port.
"""
import ast,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
m,L,s,Y=80000,5600000,24800,110642
A,n,w,p=181275,262144,131071,2130706433
D=m*A
C=0
for j in range(s+1):
    d=D-(w-1)*j
    k=min(L-j,(d-1)//w)
    if k<0:continue
    c=L+1-j
    C+=(k+1)*d*c-(d+w*c)*k*(k+1)//2+w*k*(k+1)*(2*k+1)//6
# Independently instantiate the published closed local-rank polynomial.
a=(s+1)*m*(m+1)*(6*(L+1)-2*(m-1)-3*s)
c=2*L+2-m-s;p0=(m+1)*(s+1);p1=-(m+2*s+3)
b=6*p0*c*s+3*(p0+p1*c)*s*(s+1)+(p1+2*c)*s*(s+1)*(2*s+1)+3*s*s*(s+1)*(s+1)
assert (a-b)%12==0
R=(a-b)//12;gap=C-n*R
assert gap==322751773311079926570022
assert s<=m<p and 2*s<=m and m+s<=L+1
assert D+s<=w*(Y+1)
q,rem=divmod(D,w)
assert s<=q<=L
# Direct count above also permits crossing the one-residue boundary.
capR,capY,capT=36,163,9678
mixed=[capR*L+capT*s,capY*L+capT*Y,capY*s+capR*Y]
assert max(mixed+[capR,capY,capT])<p
cy,cr,cz=1+2*w*capY,w*(2*capR-1),1+2*w*capT
g=A-w
nums=[(n-w)*(cy*s+cr*Y),(n-w)*(cr*L+cz*s)+(n-A+1)*g*s,(n-w)*(cy*L+cz*Y)+(n-A+1)*g*Y]
potential=[5454817957487,300327636571218,1357584972166939]
slacks=[g*b-a for a,b in zip(nums,potential)]
assert min(slacks)>=0
out=dict(parameters=dict(m=m,L=L,s=s,Y=Y),A=A,coefficients=C,local_rank=R,nullity=gap,weighted_shape_slack=w*(Y+1)-D-s,division_remainder=rem,one_residue_condition=rem+s<=w,global_box=dict(r=capR,y=capY,t=capT),mixed=mixed,characteristic_slack=p-max(mixed),potential=potential,potential_slacks=slacks,scope='Exact numeric adapter gates. Direct slope-sum global count and published local-rank polynomial. No routing or full certificate assertion.')
(ROOT/'early_phase_candidate_root_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
