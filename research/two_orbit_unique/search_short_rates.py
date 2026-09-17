"""Exact finite search for a shorter non-half-rate two-orbit certificate."""
from pathlib import Path
from fractions import Fraction
from math import comb
import json,time
from short_finite import classes,find_proth,existence
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();tested=0;winner=None
 for m in range(10,112):
  n=2*m+4;best=None
  for D in range(2,m//2+1):
   coeff=classes(m,D);J=max(coeff);index=coeff.index(J)
   for DD in sorted({D,m-D}):
    K=2*DD-1;entropy_den=(K**K*(n-K)**(n-K))
    left=J**5*entropy_den**2;right=n**(2*n+5);tested+=1
    if left<=right:continue
    ratio=Fraction(left,right)
    if best is None or ratio>best[0]:best=(ratio,DD,K,J,index+DD*(DD+1)//2,entropy_den)
  if best:
   ratio,D,K,J,S,E=best;winner=(m,D,n,K,J,S,E)
   print('first successful length',n,'dimension',K,flush=True);break
 assert winner is not None
 m,D,n,K,J,S,E=winner;k,e,a,offset=find_proth(m,D);p=(k<<e)+1
 h=100
 while (100*J)**5*E**2>((h+1)*n)**5*n**(2*n):h+=1
 q=-1
 while J**5*E>n**(n+5)*2**(5*(q+1)):q+=1
 assert h>=100 and existence(p,m,D)>0 and 5*(p.bit_length()-1)>n
 out=dict(status='passed',m=m,D=D,d=2,c=0,n=n,K=K,selected_sum=S,exact_class_size=str(J),
  proth_k=k,proth_exponent=e,proth_base=a,prime_bits=p.bit_length(),
  good_parameter_lower=str(existence(p,m,D)),ratio_greater_than_hundredths=h,
  original_prescription_ratio_power_two=q,parameter_pairs_tested=tested,seconds=time.monotonic()-start,
  scope='An explicit-field finite existence row at non-half rate. Exact class counts and entropy comparisons; no domain parameter is specified. Search minimality is limited to the scanned d=2 two-orbit family and is not a general lower bound.')
 (BASE/'short_rate_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
