"""Search sufficient certificates with fine upward rounding and weaker constants.

Binary search is a heuristic for locating short sufficient rows, not a claim
of global optimality. Each returned row is checked by its integer schedule.
"""
from search_completion_precise import certify
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def find(b,r,target):
 def at(n):
  for t in range(1,2*r+25):
   budget=0 if target is None else target+(t+1).bit_length()
   row=certify(b,r,n,t,budget,4,8)
   if row:return row
  return None
 lo=(2*r*b-2)//4;hi=(2*r*b+4*b+400-2)//4
 if not at(4*hi+2):return dict(b=b,r=r,failure_bits=target,found=False)
 while hi-lo>1:
  mid=(lo+hi)//2
  if at(4*mid+2):hi=mid
  else:lo=mid
 row=at(4*hi+2);n=row['n'];p=2**b-1;A=2*r+1
 w=(A*b-n)//A-n.bit_length()-1
 while n**A*2**max(0,n+(w+1)*A)<p**A and n+(w+1)*A>=0:w+=1
 while n+w*A<0 or n**A*2**(n+w*A)>=p**A:w-=1
 row.update(failure_bits=target,prescription_fraction_less_than_power_two=-w,strict_elias_sufficient=A*(b-1)>n)
 return row

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for b,r in [(61,1),(127,1),(521,1),(521,2),(1279,3),(1279,10)]:
  for target in [None,32,64]:
   row=find(b,r,target);rows.append(row)
   print(json.dumps({k:v for k,v in row.items() if k!='scaled_missing'}),flush=True)
 out=dict(status='completed',rows=rows,seconds=time.monotonic()-start,scope='Sufficient fixed-point certificates, not a proof of optimality. All rows use weaker C=4r+4 and conditioning p-8. Negative prescription exponents beat one; only strict-Elias rows are promotable.')
 (BASE/'optimized_completion.json').write_text(json.dumps(out,indent=2)+'\n')
