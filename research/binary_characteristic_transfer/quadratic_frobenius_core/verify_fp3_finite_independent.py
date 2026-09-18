"""Independent coefficient-prefix and local-block replay of the Fp3 certificate."""
import json
from math import isqrt
from pathlib import Path
rows=json.loads(Path(__file__).with_name('fp3_finite_certificate.json').read_text())
out=[]
for old in rows:
 p=old['p']; ceil4=1+isqrt(16*p-1)
 N=2*p*p-p-1; A=2*p-ceil4-2; B=3*A; H=40*B
 # Sum each derivative-column X-prefix separately, retaining joint cap.
 counts=[]
 for j in range(4):
  max_i=min(B-j,(2*B-j-1)//2)
  number=max_i+1
  counts.append(number*(2*B-j)-number*(number-1))
 G=sum(counts)
 ranks=[]
 for ell in range(6):
  rank=0
  for degree in range(ell+4):
   eligible=sum(i<=ell and degree-i<=3 for i in range(degree+1))
   if ell+degree<2*B: rank+=min(6-ell,eligible)
  ranks.append(rank)
 R=sum(ranks)
 margin=(H-B+1)*G-(H+1)*N*R
 assert G==4*B*B-2*B and ranks==[4,8,12,15,14,9]
 assert all(old[k]==v for k,v in dict(N=N,A=A,B=B,H=H,G=G,R=R,conservative_margin=margin).items())
 assert 5*B>=29*p and 39*G>40*N*R and margin>0
 assert A*A<2*N and A>p and (A-p)**2>4*p
 out.append(dict(p=p,derivative_column_counts=counts,local_blocks=ranks,
                 margin=margin,scalar_margin=39*G-40*N*R,passed=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
