"""Independent replay of the completed-image sample and dyadic probability bound."""
from pathlib import Path
from math import comb,isqrt
import hashlib,json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();path=BASE/'completed_samples/m521_r2_n2518.json';raw=path.read_bytes();s=json.loads(raw)
 p=2**521-1;assert int(s['p'])==p
 assert all(521%d for d in range(2,isqrt(521)+1));ll=4
 for _ in range(519):ll=(ll*ll-2)%p
 assert ll==0
 n,K,r,m,d,t,D=(s[k] for k in ['n','K','r','base_orbits','base_support','sprinkling_pairs','D'])
 assert (n,K,r,m,d,t,D)==(2518,1259,2,1241,622,8,630)
 x=list(map(int,s['domain']));f=list(map(int,s['f']));g=list(map(int,s['g']))
 assert len(x)==len(f)==len(g)==n and len(set(x))==n
 assert all(0<a<p for a in x) and all(0<=a<p for a in f+g)
 reps=x[::2];assert reps[-r:]==[1,2]
 reference=reps[:d]+[reps[m+2*j] for j in range(t)];assert len(reference)==D
 roots=[a*a%p for a in reference]
 for j,a in enumerate(reps):
  assert 1<=a<=(p-1)//2 and x[2*j+1]==p-a
  value=1
  for root in roots:value=value*(a*a-root)%p
  assert f[2*j]==f[2*j+1]==value
  assert g[2*j]==g[2*j+1]==(0 if j<m+2*t else -value%p)
 assert sum(v==0 for v in f)==K+1
 assert sum(v!=0 for v in g)==2*r
 assert sum((a+b)%p==0 for a,b in zip(f,g))==K+2*r+1
 # Monic degreeK+1 proves far distance; Lipschitz plus zero codeword
 # proves the exact parameter-one distance for every output.
 C=4*r+4;L=comb(m,d);assert p>(n+1)**2 and p>C*C
 seq=[101,109,125,157,221,349,605,1026,1447];budget=92
 num=p**r*(p-2*m*m)+L*(C**(2*r+2)+2*m*m);den=L*(p-2*m*m)
 assert num*2**(seq[0]+budget)<den
 for a,b in zip(seq,seq[1:]):assert (p+C*C*2**a)*2**(b+budget)<(p-8)*2**(2*a)
 assert (p-1)**r<2**seq[-1] and (t+1)*2**88<2**budget
 assert (2*r+1)*520>n
 assert n**(2*r+1)*2**(n+6*(2*r+1))<p**(2*r+1)
 out=dict(status='passed',sha256=hashlib.sha256(raw).hexdigest(),n=n,K=K,direction_weight=2*r,far_distance_numerator=n-K-1,parameter_one_exact_distance_numerator=n-K-2*r-1,known_nearby_codeword='zero',affine_dimension=r,generator_completion_failure_less_than='2^-88',prescription_less_than='2^-6',seconds=time.monotonic()-start,scope='All coordinates replayed by direct root products. Distances at parameters0 and1 and direction support are deterministic. Full affine-space/line profile is guaranteed over generator randomness, not individually certified for this stored sample.')
 (BASE/'completed_sample_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
