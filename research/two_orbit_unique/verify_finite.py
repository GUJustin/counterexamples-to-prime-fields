"""Independently replay the finite two-orbit existence certificates.

No root-admitting parameter is sampled: these are existence bounds, not
certificates for specified evaluation domains.
"""
from pathlib import Path
from math import comb,isqrt
import json,time
BASE=Path(__file__).resolve().parent

def mersenne_prime(b):
 assert b>=3 and all(b%a for a in range(2,isqrt(b)+1))
 p=2**b-1;v=4
 for _ in range(b-2):
  v=v*v-2
  while v>p:v=(v&p)+(v>>b)
  if v==p:v=0
 assert v==0
 return p

def check(row):
 b,d,m,D,c=(row[k] for k in ('b','d','m','D','c'))
 p=mersenne_prime(b)
 assert all(d%a for a in range(2,isqrt(d)+1))
 n=d*(m+2)+c;K=d*D-1;M=m+c
 assert 1<=D<m and 0<=c<d and n==row['n']==2*K and K==row['K']
 assert p>max(n,d**(d-1)) and (p-1)%d==0
 U=(M+1)**2;T=sum(range(1,M+1));A=comb(m,D)
 span=D*(m-D);maxsum=sum(range(m-D+1,m+1))
 ceiling_sqrt=isqrt(p)
 if ceiling_sqrt**2<p:ceiling_sqrt+=1
 available=(p-U)//d**(M+1)-U*(ceiling_sqrt+1)
 excluded=(T+1)*((2**d-1)**M-1)+maxsum*A*(A-1)//2+span*(span+1)//2
 assert available>excluded
 J=(A+span)//(span+1)
 assert str(J)==row['nearby_count_lower']
 w=row['ratio_to_c2_two_greater_than_power_two']
 assert J**(2*d+1)>n**(2*d+1)*2**(2*n+w*(2*d+1))
 assert not J**(2*d+1)>n**(2*d+1)*2**(2*n+(w+1)*(2*d+1))
 # H_p(theta) <= theta + 1/log_2(p); eta log_2(p)>1 suffices.
 assert (2*d+1)*(b-1)>n
 assert 0<n-K-(2*d+1)<n
 assert (available-excluded).bit_length()-1==row['good_parameter_lower_bits']
 return dict(b=b,d=d,n=n,K=K,certified_ratio_power_two=w,
  separation=f'{2*d}/{2*d+1}',strict_Elias=True,
  good_parameters_more_than_power_two=(available-excluded).bit_length()-1,
  status='passed')

if __name__=='__main__':
 start=time.monotonic();data=json.loads((BASE/'finite_candidates.json').read_text());rows=[]
 for row in data['rows']:
  result=check(row);rows.append(result);print(json.dumps(result),flush=True)
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,
  scope='Independent Lucas-Lehmer and exact integer replay of finite existence bounds. No explicit parameter, domain, witness, or efficient sampler certified.')
 (BASE/'finite_verification.json').write_text(json.dumps(out,indent=2)+'\n')
