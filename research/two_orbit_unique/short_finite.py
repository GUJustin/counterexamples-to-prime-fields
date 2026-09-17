"""A short doubled-exponent certificate using a Proth prime and exact class.

The field is explicit; the evaluation domain is still an existence claim.
"""
from pathlib import Path
from math import comb,isqrt
import json,time
BASE=Path(__file__).resolve().parent

def classes(m,D):
 R=D*(m-D);a=[1]+[0]*R
 # Gaussian binomial product, as a truncated formal power series.
 for i in range(1,D+1):
  for j in range(i,R+1):a[j]+=a[j-i]
  shift=m-D+i
  for j in range(R,shift-1,-1):a[j]-=a[j-shift]
 assert all(x>=0 for x in a) and sum(a)==comb(m,D)
 return a

def existence(p,m,D):
 d=2;M=m;n=2*(m+2);U=(M+1)**2;T=M*(M+1)//2
 A=comb(m,D);R=D*(m-D);S=D*(2*m-D+1)//2
 available=(p-U)//2**(M+1)-U*(isqrt(p)+2)
 bad=(T+1)*(3**M-1)+S*A*(A-1)//2+R*(R+1)//2
 return available-bad

def find_proth(m,D,e=320):
 lo=1;hi=1<<22
 while lo+1<hi:
  mid=(lo+hi)//2
  if existence((mid<<e)+1,m,D)>0:hi=mid
  else:lo=mid
 k=hi|1;start=k
 small=[q for q in range(3,1000,2) if all(q%a for a in range(2,isqrt(q)+1))]
 while k<1<<e:
  p=(k<<e)+1
  if all(p%q for q in small):
   for a in (3,5,7,11,13,17,19,23,29,31,37):
    if pow(a,(p-1)//2,p)==p-1:return k,e,a,k-start
  k+=2
 raise AssertionError('no prime found')

if __name__=='__main__':
 start=time.monotonic();m=111;D=57;counts=classes(m,D);J=max(counts);S=counts.index(J)+D*(D+1)//2
 n=2*(m+2);K=2*D-1;assert n==2*K
 k,e,a,offset=find_proth(m,D);p=(k<<e)+1
 assert k%2==1 and k<2**e and pow(a,(p-1)//2,p)==p-1
 assert existence(p,m,D)>0 and 5*(p.bit_length()-1)>n
 # A rational lower factor of the c1=1,c2=2 prescription, no logs.
 hundredths=100
 while (100*J)**5>((hundredths+1)*n)**5*2**(2*n):hundredths+=1
 assert hundredths>100
 assert J**5>n**5*2**(n+5*45)
 out=dict(status='passed',m=m,D=D,d=2,c=0,n=n,K=K,selected_sum=S,
  exact_class_size=str(J),proth_k=k,proth_exponent=e,proth_base=a,prime_bits=p.bit_length(),
  good_parameter_lower=str(existence(p,m,D)),ratio_greater_than_hundredths=hundredths,
  original_prescription_ratio_power_two=45,class_coefficient_count=len(counts),search_offset=offset,seconds=time.monotonic()-start,
  scope='Explicit Proth-prime certificate and exact largest index-sum class; a good parameter and evaluation domain exist by the finite lemma but are not specified.')
 (BASE/'short_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
