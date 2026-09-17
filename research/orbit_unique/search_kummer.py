"""Parameter search only; finite primality and root certificates are separate."""
from math import comb,log2
from pathlib import Path
import json

def row(b,d,m,D,c):
 n=d*(m+1)+c;K=d*D-1;E=D*(2*m-D+3)//2
 A=n*(1<<((m+c+d)//d))
 if E>=b or A**(d*(d-1))>=(1<<b)-1:return None
 if not 0<K<n or D>=m:return None
 J=comb(m,D);rho=K/n;H=-rho*log2(rho)-(1-rho)*log2(1-rho)
 q=int(log2(J)-log2(n)-n*H/(d+1))
 if q<0:return None
 left=J**(d+1)*K**K*(n-K)**(n-K)
 right=n**(n+d+1)
 while q>=0 and left<=right*(1<<(q*(d+1))):q-=1
 if q<0:return None
 while left>right*(1<<((q+1)*(d+1))):q+=1
 return dict(b=b,d=d,n=n,K=K,m=m,D=D,c=c,product_exponent=E,norm_bound_bits=(A**(d*(d-1))).bit_length(),nearby_count=str(J),ratio_greater_than_power_two=q,separation_fraction=f'{d}/{d+1}')

if __name__=='__main__':
 rows=[]
 for b,d in [(521,2),(1279,3),(9689,5),(23209,13),(44497,19)]:
  assert ((1<<b)-2)%d==0
  best=None
  # Optimize the finite ratio; first use floating entropy as a search aid,
  # then certify each retained result by exact integer powers.
  for m in range(2,800):
   for D in range(max(1,m//8),min(m,2*m//3+1)):
    E=D*(2*m-D+3)//2
    if E>=b:continue
    n=d*(m+1);K=d*D-1;rho=K/n
    H=-rho*log2(rho)-(1-rho)*log2(1-rho)
    score=log2(comb(m,D))-log2(n)-n*H/(d+1)
    if score<0 or (best is not None and score<best['ratio_greater_than_power_two']):continue
    candidate=row(b,d,m,D,0)
    if candidate and (best is None or candidate['ratio_greater_than_power_two']>best['ratio_greater_than_power_two']):best=candidate
  assert best is not None,(b,d)
  rows.append(best);print(best,flush=True)
 Path(__file__).with_name('kummer_search.json').write_text(json.dumps(rows,indent=2)+'\n')
