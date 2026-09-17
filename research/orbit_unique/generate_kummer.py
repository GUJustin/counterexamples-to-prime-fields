"""Certify Kummer parameters and save roots; generation is zero-error."""
from pathlib import Path
from math import comb,isqrt
import json,secrets,time,hashlib
from verify_parameters import mersenne_prime
from generate_roots import modpow
BASE=Path(__file__).resolve().parent

if __name__=='__main__':
 start=time.monotonic();out=[]
 for row in json.loads((BASE/'kummer_search.json').read_text()):
  t0=time.monotonic();b=row['b'];d=row['d'];m=row['m'];D=row['D'];c=row['c'];n=row['n'];K=row['K'];p=mersenne_prime(b)
  assert all(d%q for q in range(2,isqrt(d)+1)) and (p-1)%d==0 and b!=d
  assert n==d*(m+1)+c and K==d*D-1 and 0<=c<d and 1<=D<m
  A=n*(1<<((m+c+d)//d));E=D*(2*m-D+3)//2
  assert p>A**(d*(d-1)) and p>1<<E
  J=comb(m,D);q=row['ratio_greater_than_power_two']
  assert J**(d+1)*K**K*(n-K)**(n-K)>(1<<(q*(d+1)))*n**(n+d+1)
  assert (d+1)*(b-1)>n
  v=pow(d,-1,b);alpha=1<<v;assert pow(alpha,d,p)==2
  trials=0
  if d==2:omega=p-1
  else:
   while True:
    h=secrets.randbelow(p-1)+1;trials+=1;omega=modpow(h,(p-1)//d,p,b)
    if omega!=1:break
  assert pow(omega,d,p)==1 and 1<omega<p
  entry=dict(**row,alpha_power_two_exponent=v,omega_hex=hex(omega),root_trials=trials,
   omega_sha256=hashlib.sha256(omega.to_bytes((b+7)//8,'big')).hexdigest(),seconds=time.monotonic()-t0)
  out.append(entry)
  (BASE/'kummer_certificates.json').write_text(json.dumps(dict(status='passed',rows=out,seconds=time.monotonic()-start,scope='Exact root and parameter certificates, including primality. Independent domain and witness replay is separate.'),indent=2)+'\n')
  print(f'CERTIFIED b={b} d={d} n={n} K={K} ratio>2^{q} seconds={entry["seconds"]:.2f}',flush=True)
