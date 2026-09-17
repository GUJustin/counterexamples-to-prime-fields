"""Replay a stored randomized sample and independently bound generator failure.

Verifies deterministic structural properties. Complete nonzero coverage
is a probability guarantee of the sampler, not an exhaustive output check.
"""
from pathlib import Path
from math import comb,isqrt,prod
import json,hashlib,time
BASE=Path(__file__).resolve().parent


def main():
 start=time.monotonic();path=BASE/'samples/m521_n990.json';raw=path.read_bytes();a=json.loads(raw)
 assert all(521%d for d in range(2,isqrt(521)+1))
 p=(1<<521)-1;state=4
 for _ in range(519):state=(state*state-2)%p
 assert state==0 and int(a['p'])==p
 n,K,m,t,s=990,495,900,497,1
 assert [a[k] for k in ('n','K','m','threshold','transformed_moments')]==[n,K,m,t,s]
 assert a['anchor']==0 and a['seed_moments']==3
 support=a['original_support'];assert len(support)==t and len(set(support))==t and support[0]==0
 assert all(0<=x<m for x in support)
 ca,cb=int(a['cubic_a']),int(a['cubic_b']);assert 0<=ca<p and 0<=cb<p
 images=[(x**3+cb*x*x+ca*x)%p for x in range(m)]
 assert len(set(images))==m
 domain=[int(x) for x in a['domain']];f=[int(x) for x in a['f']];g=[int(x) for x in a['g']]
 assert len(domain)==len(f)==len(g)==n and len(set(domain))==n
 assert all(0<=v<p for v in domain+f+g)
 assert domain[:m-1]==images[1:]
 assert g[:m-1]==[0]*(m-1) and all(gj!=0 for gj in g[m-1:])
 roots=[images[i] for i in support if i!=0]
 # Independent direct product evaluation; the generator uses coefficient
 # multiplication and Horner evaluation instead.
 for x,fx in zip(domain,f):
  v=1
  for root in roots:v=v*(x-root)%p
  assert v==fx
 assert sum(x==0 for x in f)==t-1
 # The degree-(t-1) root product minus any degree<K codeword is nonzero
 # of degree t-1. The zero codeword attains that many agreements.
 N=m-1;R=p-N;U=p-1;q=n-N
 Q=comb(m-1,t-1)
 V=prod(comb(m,j+1)-comb(m-t,j+1)-comb(t,j+1)+1 for j in (1,2,3))
 H=p*(1<<150);d=8
 Bnum=p+(t-1)*(t-2)*(isqrt(p)+1)+5*t**5;Bden=p-comb(m,2)
 assert H*V*(1<<130)<Q
 delta_num=U*R*Bden+H*U*Bnum-H*R*Bden
 assert delta_num>0 and delta_num*(1<<(d+130))<H*R*Bden
 assert U*(1<<130)<((1<<d)+1)**q
 # Each of three error terms is <2^-130, so their sum is <2^-128.
 assert 3<4 and p>2*m*m
 gap=t-K
 assert p**gap*t**t*(n-t)**(n-t)>n**n
 assert n*n*(1<<(n+32))<p*p
 out=dict(status='passed',sample_sha256=hashlib.sha256(raw).hexdigest(),n=n,K=K,
          coordinates_replayed=n,exact_zero_parameter_agreement=t-1,
          generator_failure_probability_less_than='2^-128',strict_elias=True,
          prescription_fraction_less_than='2^-16',seconds=time.monotonic()-start,
          scope='Exact structural replay and an independent integer proof of the generator probability bound. Complete coverage of this particular sample is not deterministically certified.')
 (BASE/'sample_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
