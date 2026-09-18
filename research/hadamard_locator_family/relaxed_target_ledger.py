"""Exact parameter ledger; no construction claim."""
from fractions import Fraction as F
import json,math
from pathlib import Path
rows=[]
L=8;k=7;A=14;D=6
for n in range(28,35):
 r=F(k,n);a=F(A,n)
 margin=(8-r)*a*a-6*r*a+r*(4*r-5)
 q,rem=divmod(L*A,n)
 pairmin=(n-rem)*q*(q-1)//2+rem*q*(q+1)//2
 threshold=(6*float(r)+math.sqrt(36*float(r)**2-4*(8-float(r))*float(r)*(4*float(r)-5)))/(2*(8-float(r)))
 rows.append({'n':n,'k':k,'A':A,'L':L,'rho':str(r),'agreement':str(a),'first_order_polynomial':str(margin),'above_first_order':margin>0,'agreement_margin_approx':float(a)-threshold,'min_pair_incidence':pairmin,'pair_budget':L*(L-1)//2*D,'pair_slack':L*(L-1)//2*D-pairmin,'raw_equation_dimension':L*k+2*n-L*A,'generic_gauge_dimension':k+4})
out={'scalable_parameters':'k=L-1,A=2k,n=c*k','first_order_expression':'F_rho(2rho)=rho*(-4rho^2+24rho-5)','allowed_ratio':'4 <= c < (12+2*sqrt(31))/5','ratio_bound_approx':(12+2*math.sqrt(31))/5,'finite_rows':rows,'scope':'Parameter feasibility only; neither incidence realization nor independence of constraints is asserted.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
