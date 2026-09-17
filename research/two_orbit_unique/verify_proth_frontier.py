"""Independent Python-integer replay of compact Proth-field certificates."""
from pathlib import Path
from math import comb,isqrt
import json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();source=json.loads((BASE/'proth_frontier_certificates.json').read_text());rows=[]
 for r in source['rows']:
  d,m,D,c=(r[k] for k in ('d','m','D','c'));k,e,a=(r[k] for k in ('proth_k','proth_exponent','proth_base'))
  p=k*2**e+1
  assert all(d%q for q in range(2,isqrt(d)+1)) and k%2==1 and 0<k<2**e
  assert pow(a,(p-1)//2,p)==p-1 # Deterministic Proth proof, independent of GMP search.
  M=m+c;n=d*(m+2)+c;K=d*D-1
  assert 0<=c<d and 1<=D<m and n==r['n']==2*K and K==r['K']
  assert (p-1)%d==0 and p>max(n,d**(d-1)) and p.bit_length()==r['prime_bits']
  A=comb(m,D);V=D*(m-D)*(m+1);J=isqrt((A*A-1)//(V+1))+1
  assert str(J)==r['nearby_count_lower']
  U=(M+1)**2;T=sum(range(1,M+1));span=D*(m-D);S=sum(range(m-D+1,m+1))
  root_lower=(p-U)//d**(M+1)-U*(isqrt(p)+2)
  bad_upper=(T+1)*((2**d-1)**M-1)+S*A*(A-1)//2+span*(span+1)//2
  assert root_lower>bad_upper and bad_upper*2**r['conditional_failure_less_than_power_two_minus']<root_lower
  power=2*d+1;w=r['ratio_to_c2_two_power_two'];v=r['ratio_to_c2_one_power_two']
  assert J**power>n**power*2**(2*n+w*power)
  assert J**power>n**power*2**(n+v*power)
  assert power*(p.bit_length()-1)>n
  out=dict(d=d,n=n,K=K,prime_bits=p.bit_length(),separation=r['separation'],
   doubled_exponent_ratio_power_two=w,original_exponent_ratio_power_two=v,
   conditional_failure_power_two_minus=r['conditional_failure_less_than_power_two_minus'],status='passed')
  rows.append(out);print(json.dumps(out),flush=True)
 result=dict(status='passed',search_status=source['status'],rows=rows,seconds=time.monotonic()-start,
  scope='Independent Python pow primality certificates, integer concentration/existence bounds, and ratios. The prime fields are explicit; the domains remain existential.')
 (BASE/'proth_frontier_verification.json').write_text(json.dumps(result,indent=2)+'\n')
