"""Exact candidate existence bounds for the function-field two-orbit argument.

The character/norm lemma is audited in PROOF_AUDIT.md. These are existence
certificates, not explicit sampled domains or efficient witness algorithms.
"""
from pathlib import Path
from math import comb,isqrt
import json,time
BASE=Path(__file__).resolve().parent

def ll(b):
 assert all(b%q for q in range(2,isqrt(b)+1));p=(1<<b)-1
 try:
  from gmpy2 import mpz
 except ImportError:
  s=4
 else:
  p=mpz(p);s=mpz(4)
 for _ in range(b-2):
  v=s*s-2;s=(v&p)+(v>>b)
  if s>=p:s-=p
  if s<0:s+=p
 assert s==0;return int(p)

def bounds(p,d,m,D,c):
 M=m+c;n=d*(m+2)+c;K=d*D-1;U=(M+1)**2;T=M*(M+1)//2
 assert p>d**(d-1) and p>M+1 and (p-1)%d==0
 sqrt=isqrt(p)+1
 split=(p-U)//d**(M+1)-U*(sqrt+1)
 root=(T+1)*((2**d-1)**M-1)
 Jtotal=comb(m,D);Smax=D*(2*m-D+1)//2;R=D*(m-D)
 collision=Smax*comb(Jtotal,2);order=R*(R+1)//2
 good=split-root-collision-order
 V=D*(m-D)*(m+1)
 J=max((Jtotal+R)//(R+1),isqrt((Jtotal*Jtotal-1)//(V+1))+1)
 assert n==2*K
 left=J**(2*d+1);base=n**(2*d+1)
 q=max(-1,(((left-1)//base).bit_length()-1-2*n)//(2*d+1))
 return dict(b=p.bit_length(),d=d,m=m,D=D,c=c,n=n,K=K,nearby_count_lower=str(J),
  good_parameter_exists=good>0,split_lower_bits=max(0,split.bit_length()),
  bad_root_upper_bits=root.bit_length(),bad_collision_upper_bits=collision.bit_length(),
  good_parameter_lower_bits=max(0,good.bit_length()-1),
  ratio_to_c2_two_greater_than_power_two=q,separation=f'{2*d}/{2*d+1}',class_bound='variance')

def choose(p,d):
 # The existence lower bound decreases and every exclusion bound increases
 # when m increases by two and D=(m+3)/2. Binary search the last valid row.
 lo=10;hi=p.bit_length()//(2*d)+1
 while lo+1<hi:
  mid=(lo+hi)//2;m=2*mid+1
  row=bounds(p,d,m,(m+3)//2,d-2)
  if row['good_parameter_exists']:lo=mid
  else:hi=mid
 m=2*lo+1;row=bounds(p,d,m,(m+3)//2,d-2)
 assert row['good_parameter_exists'] and row['ratio_to_c2_two_greater_than_power_two']>=0
 return row

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for b,d in [(521,2),(1279,3),(9689,5),(23209,7),(44497,19),(216091,43)]:
  p=ll(b);row=choose(p,d);rows.append(row)
  print(json.dumps({k:v for k,v in row.items() if k!='nearby_count_lower'}),flush=True)
 out=dict(status='parameter_checks_passed',rows=rows,seconds=time.monotonic()-start,scope='Exact arithmetic for the audited character/norm existence lemma. No actual domain is enumerated or sampled; independent replay is in verify_finite.py.')
 (BASE/'finite_candidates.json').write_text(json.dumps(out,indent=2)+'\n')
