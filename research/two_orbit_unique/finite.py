"""Exact candidate existence bounds for the function-field two-orbit argument.

The character/norm lemma is audited in PROOF_AUDIT.md. These are existence
certificates, not explicit sampled domains or efficient witness algorithms.
"""
from pathlib import Path
from math import comb,isqrt
import json,time
BASE=Path(__file__).resolve().parent

def ll(b):
 assert all(b%q for q in range(2,isqrt(b)+1));p=(1<<b)-1;s=4
 for _ in range(b-2):
  v=s*s-2;s=(v&p)+(v>>b)
  if s>=p:s-=p
  if s<0:s+=p
 assert s==0;return p

def bounds(p,d,m,D,c):
 M=m+c;n=d*(m+2)+c;K=d*D-1;U=(M+1)**2;T=M*(M+1)//2
 assert p>d**(d-1) and p>M+1 and (p-1)%d==0
 sqrt=isqrt(p)+1
 split=(p-U)//d**(M+1)-U*(sqrt+1)
 root=(T+1)*((2**d-1)**M-1)
 Jtotal=comb(m,D);Smax=D*(2*m-D+1)//2;R=D*(m-D)
 collision=Smax*comb(Jtotal,2);order=R*(R+1)//2
 good=split-root-collision-order
 J=(Jtotal+R)//(R+1)
 assert n==2*K
 q=-1
 left=J**(2*d+1);base=n**(2*d+1)
 while left>base*(1<<(2*n+(q+1)*(2*d+1))):q+=1
 return dict(b=p.bit_length(),d=d,m=m,D=D,c=c,n=n,K=K,nearby_count_lower=str(J),
  good_parameter_exists=good>0,split_lower_bits=max(0,split.bit_length()),
  bad_root_upper_bits=root.bit_length(),bad_collision_upper_bits=collision.bit_length(),
  good_parameter_lower_bits=max(0,good.bit_length()-1),
  ratio_to_c2_two_greater_than_power_two=q,separation=f'{2*d}/{2*d+1}')

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for b,d in [(521,2),(1279,3),(9689,5),(23209,7),(44497,19)]:
  p=ll(b);best=None
  for m in range(21,min(2401,b//d),2):
   D=(m+3)//2;c=d-2
   row=bounds(p,d,m,D,c)
   if row['good_parameter_exists'] and row['ratio_to_c2_two_greater_than_power_two']>=0:
    if best is None or row['ratio_to_c2_two_greater_than_power_two']>best['ratio_to_c2_two_greater_than_power_two']:best=row
  assert best is not None,(b,d);rows.append(best);print(json.dumps(best),flush=True)
 out=dict(status='parameter_checks_passed',rows=rows,seconds=time.monotonic()-start,scope='Exact arithmetic for the audited character/norm existence lemma. No actual domain is enumerated or sampled; independent replay is in verify_finite.py.')
 (BASE/'finite_candidates.json').write_text(json.dumps(out,indent=2)+'\n')
