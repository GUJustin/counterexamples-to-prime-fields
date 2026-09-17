"""Independent direct-product replay and integer probability certificate."""
from pathlib import Path
from math import prod,comb,isqrt
import json,hashlib,time
BASE=Path(__file__).resolve().parent

def main():
 start=time.monotonic();path=BASE/'samples/m521_r2_n2518.json';raw=path.read_bytes();s=json.loads(raw)
 p=2**521-1;assert int(s['p'])==p and s['mersenne_exponent']==521
 assert all(521%j for j in range(2,isqrt(521)+1));z=4
 for _ in range(519):z=(z*z-2)%p
 assert z==0
 n,K,m,D,r,q=(s[x] for x in ['n','K','m','D','r','blocks'])
 assert (n,K,m,D,r,q)==(2518,1259,1211,630,2,24)
 domain=list(map(int,s['domain']));f=list(map(int,s['f']));g=list(map(int,s['g']))
 assert len(domain)==len(f)==len(g)==n and len(set(domain))==n
 assert all(0<x<p for x in domain) and all(0<=x<p for x in f+g)
 roots=[domain[2*i]**2%p for i in range(D)]
 for i in range(n//2):
  a=domain[2*i];assert 1<=a<=(p-1)//2 and domain[2*i+1]==p-a
  v=1
  for root in roots:v=v*(a*a-root)%p
  assert f[2*i]==f[2*i+1]==v
  assert g[2*i]==g[2*i+1]
  assert (g[2*i]==0)==(i<m)
 assert sum(x==0 for x in f)==2*D==K+1
 assert m+r*q==n//2 and 2*D+2*r==K+2*r+1
 # Independently prove both error terms <2^-129, hence sum <2^-128.
 L=comb(m,D);c=4*r+2;assert p>c*c and p>2*m*m
 den=L*(p-2*m*m);num=p**r*(p-2*m*m)+L*(c**(2*r+2)+2*m*m)
 d=28
 assert q*num*2**(d+129)<den
 assert (p-1)*2**129<(2**d+1)**q
 assert (2*r+1)*520>n
 assert n**(2*r+1)*2**(n+6*(2*r+1))<p**(2*r+1)
 out=dict(status='passed',sha256=hashlib.sha256(raw).hexdigest(),n=n,K=K,prime_verified=True,far_max_agreement=K+1,far_distance_numerator=n-K-1,nearby_agreement_threshold=K+2*r+1,far_fraction='4/5',generator_failure_less_than='2^-128',prescription_less_than='2^-6',seconds=time.monotonic()-start,scope='All coordinates replayed by direct root products; monic degree proves exact far distance and no correlated agreement. Probability certificate concerns generator randomness, not deterministic complete coverage of this stored sample.')
 (BASE/'sample_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
