"""Exact checks of both boundary-preserving operations, with a negative control."""
from itertools import product
from fractions import Fraction
from pathlib import Path
import json
p=5;d=2
zero=(0,0);theta=(0,1)
F=list(product(range(p),repeat=2))
add=lambda a,b:((a[0]+b[0])%p,(a[1]+b[1])%p)
sub=lambda a,b:((a[0]-b[0])%p,(a[1]-b[1])%p)
mul=lambda a,b:((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def ev(c,x):
 y=zero
 for a in reversed(c):y=add(mul(y,x),a)
 return y
def census(domain,word,dim,alphabet):
 maximum=-1;bank=[]
 for c in product(alphabet,repeat=dim):
  count=sum(ev(c,x)==y for x,y in zip(domain,word))
  if count>maximum:maximum=count;bank=[c]
  elif count==maximum:bank.append(c)
 return maximum,bank
base=[(a,0) for a in range(p)]
D=[(a,0) for a in range(1,p)]
w=[(pow(a,-1,p),0) for a in range(1,p)]
M,bank=census(D,w,2,base)
assert M==2
extension_max,_=census(D,w,2,F);assert extension_max==M
noise_max,_=census(D+[zero],w+[theta],2,F);assert noise_max==M
newword=[mul(sub(x,theta),y) for x,y in zip(D,w)]+[zero]
zero_max,_=census(D+[theta],newword,3,F);assert zero_max==M+1
for c in bank:
 assert sum(ev(c,x)==y for x,y in zip(D+[zero],w+[theta]))==M
 lifted=[mul(sub(zero,theta),c[0]),sub(c[0],mul(theta,c[1])),c[1]]
 assert sum(ev(lifted,x)==y for x,y in zip(D+[theta],newword))==M+1
# Choosing the common-zero point inside the field need NOT preserve M+1.
badword=[mul(x,y) for x,y in zip(D,w)]+[zero]
inside_max,_=census(D+[zero],badword,3,base)
assert inside_max==4>M+1
cases=0
for r in range(40,2501):
 for m in sorted({(3*r+1)//2,(7*r)//4,2*r}):
  Delta=m-r+1;u=13*Delta-3*r;s=2*Delta-r+1
  assert u>=0 and s>=0
  assert 4*r+u+s==15*Delta+1 and r+s==2*Delta+1 and m+s==3*Delta
  n=16*Delta;K=2*Delta;T=3*Delta
  assert Fraction(K,n)==Fraction(1,8) and Fraction(T-K,n)==Fraction(1,16)
  assert Fraction(3*Delta,15*Delta+1)>=Fraction(1,6)
  assert r>=Fraction(3*Delta,4) and 4*r+1>K-1
  assert Fraction(Delta*r,24)>=Fraction(n*n,8192)
  cases+=1
result=dict(status='passed',p=p,quadratic_nonresidue=d,source_length=4,source_dimension=2,source_maximum=M,source_nearest_list=len(bank),maximum_after_extension=extension_max,maximum_after_new_value=noise_max,maximum_after_external_common_zero=zero_max,internal_common_zero_negative_control=inside_max,external_common_zero_polynomials_enumerated=25**3,parameter_cases=cases,scope='Complete independent finite checks of the two individual operations, preservation of every selected nearest witness, and an essential-hypothesis negative control. Iteration and asymptotic conclusions rely on the proved lemmas, not these finite checks.')
Path(__file__).with_name('normalization_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
