"""Compact explicit-field existence certificates at larger separations.

Proth congruences prove primality. Domains remain existential.
"""
from pathlib import Path
from math import comb,isqrt
import json,time
from gmpy2 import mpz,powmod,jacobi
BASE=Path(__file__).resolve().parent

def geometry(d):
 for m in range(21,10001,2):
  D=(m+3)//2;c=d-2;n=d*(m+2)+c;K=d*D-1;A=comb(m,D);V=D*(m-D)*(m+1)
  J=isqrt((A*A-1)//(V+1))+1
  if J**(2*d+1)>n**(2*d+1)*2**(2*n+2*d+1):return m,D,c,n,K,J
 raise AssertionError('no geometry')

def count(p,d,m,D,c):
 M=m+c;U=(M+1)**2;T=M*(M+1)//2;A=comb(m,D);R=D*(m-D);S=D*(2*m-D+1)//2
 available=(p-U)//d**(M+1)-U*(isqrt(p)+2)
 bad=(T+1)*((2**d-1)**M-1)+S*comb(A,2)+R*(R+1)//2
 return available,bad

def primes(n):
 sieve=bytearray(b'\1')*(n+1);sieve[:2]=b'\0\0'
 for q in range(2,isqrt(n)+1):
  if sieve[q]:sieve[q*q::q]=b'\0'*((n-q*q)//q+1)
 return [q for q in range(3,n+1,2) if sieve[q]]

if __name__=='__main__':
 start=time.monotonic();rows=[];small=primes(10000)
 for d in (3,5,7,11,19):
  m,D,c,n,K,J=geometry(d);M=m+c
  _,bad=count(1<<100,d,m,D,c)
  bit_target=(bad*d**(M+1)).bit_length()+4;e=max(64,bit_target-16)
  step=2*d;k=((2**16+d-1)//d)|1;k*=d;attempts=0;sieved=0;rowstart=time.monotonic();found=None
  print(json.dumps(dict(stage='prime_search',d=d,m=m,n=n,target_bits=bit_target)),flush=True)
  while found is None:
   size=4096;ok=bytearray(b'\1')*size
   for l in small:
    t=pow(2,e,l);a=step*t%l;b=(k*t+1)%l
    if a:
     j=(-b*pow(a,-1,l))%l;ok[j::l]=b'\0'*((size-1-j)//l+1) if j<size else b''
    elif b==0:ok=bytearray(size);break
   for j,flag in enumerate(ok):
    if not flag:continue
    kk=k+step*j;p=(kk<<e)+1;attempts+=1
    base=next(a for a in (3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73) if jacobi(a,p)==-1)
    if powmod(base,(p-1)//2,p)==p-1:found=(kk,p,base);break
   if found is None:k+=step*size
   sieved+=size
  k,p,a=found;available,bad=count(p,d,m,D,c)
  assert k%2 and k<2**e and (p-1)%d==0 and available>bad and (2*d+1)*(p.bit_length()-1)>n
  q=(((J**(2*d+1)-1)//n**(2*d+1)).bit_length()-1-2*n)//(2*d+1)
  original=(((J**(2*d+1)-1)//n**(2*d+1)).bit_length()-1-n)//(2*d+1)
  fail=0
  while (bad<<(fail+1))<available:fail+=1
  row=dict(d=d,m=m,D=D,c=c,n=n,K=K,nearby_count_lower=str(J),proth_k=k,proth_exponent=e,proth_base=a,
   prime_bits=p.bit_length(),ratio_to_c2_two_power_two=q,ratio_to_c2_one_power_two=original,
   conditional_failure_less_than_power_two_minus=fail,separation=f'{2*d}/{2*d+1}',
   primality_candidates_tested=attempts,sieve_window_count=sieved,seconds=time.monotonic()-rowstart)
  rows.append(row);print(json.dumps({k:v for k,v in row.items() if k!='nearby_count_lower'}),flush=True)
  (BASE/'proth_frontier_certificates.json').write_text(json.dumps(dict(status='partial' if d!=19 else 'passed',rows=rows,seconds=time.monotonic()-start,scope='Explicit prime fields with finite existence bounds. No particular domain parameter or efficient sampler is supplied.'),indent=2)+'\n')
