"""Bounded exact search for shorter complete-coverage certificates at half rate."""
from fractions import Fraction as F
from math import comb,isqrt,prod
from pathlib import Path
import json,time
from verify_finite_certificate import h,c
BASE=Path(__file__).resolve().parent


def search(b):
 p=h.lucas_lehmer(b);U=p-1;root=isqrt(p)+1;hits=[];tried=0
 for n in range(b+(b%2),2*b+1,2):
  K=n//2;t=K+2
  if not(p**2*t**t*(n-t)**(n-t)>n**n):continue
  for m in range(t+1,n):
   tried+=1
   L0,_,_=h.gram_bound(m,t,3);L=h.ceil(F(t*L0,m))
   if L<U//2:continue
   N=m-1;R=p-N;q=n-N
   B=F(p+(t-1)*(t-2)*root+3*t**4,p-comb(m,2))
   M=F(L*R)/(R+(L-1)*B);miss=1-M/U
   if not U*miss**q<1:continue
   boxden=prod(comb(m,j+1)-comb(m-t,j+1)-comb(t,j+1)+1 for j in (1,2,3))
   boxnum=comb(m-1,t-1);Lbox=-(-boxnum//boxden)
   Bbox=F(p+(t-1)*(t-2)*root+5*t**5,p-comb(m,2))
   Mbox=F(Lbox*R)/(R+(Lbox-1)*Bbox)
   box_pass=0<Mbox<U and U*(1-Mbox/U)**q<1
   hits.append(dict(b=b,n=n,K=K,m=m,t=t,s=1,q=q,list_bits=L.bit_length(),
                    independent_box_pass=box_pass,beats_prescription=(n*(1<<(n//2))<U),box_list_bits=Lbox.bit_length(),
                    image_fraction_lower=c.decimal_lower(M/U,8)))
 return dict(prime_exponent=b,cases=tried,hits=len(hits),
             smallest_n=next(iter(sorted(hits,key=lambda x:(x['n'],-x['q']))),None),
             smallest_box_verified_n=next(iter(sorted((x for x in hits if x['independent_box_pass']),key=lambda x:(x['n'],-x['q']))),None))

if __name__=='__main__':
 start=time.monotonic();rows=[search(b) for b in (31,61,89,107,127)]
 out=dict(status='completed',fields=rows,seconds=time.monotonic()-start,
          scope='Exact sufficient-condition search, s1 and half rate, b<=n<=2b. Absence of a certificate is not nonexistence.')
 (BASE/'small_certificate_search.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
