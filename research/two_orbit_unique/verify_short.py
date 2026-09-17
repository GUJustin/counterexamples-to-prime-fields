"""Independent dynamic-programming replay of the short existence row."""
from pathlib import Path
from math import comb,isqrt
import json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();r=json.loads((BASE/'short_certificate.json').read_text())
 m,D=r['m'],r['D'];k,e,a=(r[x] for x in ('proth_k','proth_exponent','proth_base'));p=k*2**e+1
 assert k%2==1 and k<2**e and pow(a,(p-1)//2,p)==p-1
 # Any prime divisor q of p must have 2^e | q-1, hence q>sqrt(p).
 # This is a deterministic primality proof, not a probable-prime test.
 maxsum=D*(2*m-D+1)//2
 dp=[[0]*(maxsum+1) for _ in range(D+1)];dp[0][0]=1
 for x in range(1,m+1):
  for j in range(min(D,x),0,-1):
   top=min(maxsum,j*(2*x-j+1)//2);bottom=j*(j+1)//2
   for s in range(top,max(x,bottom)-1,-1):dp[j][s]+=dp[j-1][s-x]
 row=dp[D];J=max(row)
 assert sum(row)==comb(m,D) and J==int(r['exact_class_size']) and row[r['selected_sum']]==J
 n=2*m+4;K=2*D-1;assert n==r['n']==2*K and K==r['K']
 U=(m+1)**2;T=m*(m+1)//2;A=comb(m,D);span=D*(m-D)
 available=(p-U)//2**(m+1)-U*(isqrt(p)+2)
 bad=(T+1)*(3**m-1)+maxsum*comb(A,2)+span*(span+1)//2
 assert available-bad==int(r['good_parameter_lower'])>0
 w=r['ratio_greater_than_hundredths']
 assert J**5>n**5*2**(n+5*r['original_prescription_ratio_power_two'])
 assert (100*J)**5>(w*n)**5*2**(2*n) and 5*(p.bit_length()-1)>n
 out=dict(status='passed',seconds=time.monotonic()-start,n=n,K=K,prime_bits=p.bit_length(),
  exact_class_size=str(J),ratio_greater_than_hundredths=w,primality='Proth certificate',
  scope='Independent subset-count DP, deterministic primality proof, and exact finite existence inequalities; no specified domain.')
 (BASE/'short_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
