"""Exact parameter checks for the dyadic density/separation tradeoff.

No finite-prime existence claim: the asymptotic construction is proved
in gap_scale_far.tex. Checks its sufficient rational inequalities.
"""
from fractions import Fraction as F
from pathlib import Path
import json

rows=[]
for rho in (F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)):
 for c2 in (F(1),F(2),F(5,2),F(10)):
  for v in (2,3,4,8,16,32,64,128,256,512,1024):
   threshold=max(2/(1-rho),2*rho*(v+1)/(1-rho))
   q=2
   while q<threshold:q*=2
   assert threshold<=q<2*threshold
   ell=q.bit_length()-1;beta=1-F(1,q);alpha=rho/beta
   C=2*q/(rho*ell);u=(C*c2).__floor__()+2
   lam=(beta-rho)/(rho*beta*(1-beta))
   assert beta>rho and C*alpha*F(ell,q)>1
   assert F(u,1)/C>c2 and F(1,u)>=1/(C*c2+2)
   assert lam>(1-rho)*q/(2*rho)>=v+1
   # e>2 implies exp(-lambda)<2^(-v-1); the asymptotic
   # o(1) can then be absorbed in the remaining half of delta.
   rows.append(dict(rho=str(rho),c2=str(c2),density_deficit_bits=v,q=q,
                    C=str(C),separation_denominator=u,lambda_=str(lam)))
out=dict(status='passed',parameter_fixtures=len(rows),rows=rows,
         scope='Exact rational parameter inequalities for the asymptotic tradeoff, not finite-prime certificates.')
Path(__file__).with_name('density_separation_tradeoff_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
