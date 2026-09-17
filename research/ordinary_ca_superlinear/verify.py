"""Independent complete p17 nearest-list census and ordinary-CA padding replay."""
from itertools import product
from fractions import Fraction
from math import ceil
from pathlib import Path
import json,random
p=17;d=3;N=16;k=4;Q=p*p
add=lambda a,b:((a[0]+b[0])%p,(a[1]+b[1])%p)
sub=lambda a,b:((a[0]-b[0])%p,(a[1]-b[1])%p)
mul=lambda a,b:((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def ev(c,x):
 v=(0,0)
 for a in reversed(c):v=add(mul(v,x),(a,0))
 return v
def base_ev(c,x):
 v=0
 for a in reversed(c):v=(v*x+a)%p
 return v
word={x:(pow(x,2*k,p)+1-2*pow(x,k,p))*pow(2,-1,p)%p for x in range(1,p)}
M=-1;bank=[]
for c in product(range(p),repeat=k):
 S=[x for x in word if base_ev(c,x)==word[x]]
 if len(S)>M:M=len(S);bank=[(c,S)]
 elif len(S)==M:bank.append((c,S))
assert M==6 and len(bank)==22
anchor=max(word,key=lambda x:sum(x in S for c,S in bank))
qs=[]
for c,S in bank:
 if anchor not in S:continue
 q=[0]*(k-1);q[-1]=c[-1]
 for j in range(k-2,0,-1):q[j-1]=(c[j]+anchor*q[j])%p
 assert (c[0]-word[anchor]+anchor*q[0])%p==0
 qs.append(q)
old=[x for x in word if x!=anchor]
f={x:(word[x]-word[anchor])*pow(x-anchor,-1,p)%p for x in old}
# Independently exhaust ALL base-field quotients, not just selected ones.
oldmax=max(sum(base_ev(c,x)==f[x] for x in old) for c in product(range(p),repeat=k-1))
assert oldmax==M-1
# Matching k-1 base points forces base coefficients, so this old maximum
# also holds over F_(p^2). This is an interpolation argument, not an
# enumeration of the extension code.
qpad=M-k+1
universe=list(product(range(p),repeat=2))
unused=[x for x in universe if x not in [(t,0) for t in word]]
values={x:[ev(c,x) for c in qs] for x in unused}
pads=sorted(unused,key=lambda x:len(set(values[x])),reverse=True)[:qpad]
expectation=Q*(1-__import__('functools').reduce(lambda a,x:a*(1-Fraction(len(set(values[x])),Q)),pads,Fraction(1)))
rng=random.Random(20260917)
for attempt in range(100):
 fp={x:rng.choice(universe) for x in pads};witness={}
 for x in pads:
  for i,v in enumerate(values[x]):witness[sub(v,fp[x])]=(i,x)
 if len(witness)>=ceil(expectation):break
assert len(witness)>=ceil(expectation)
for z,(i,x0) in witness.items():
 c=qs[i]
 count=sum(ev(c,(x,0))==(f[x],0) for x in old)+sum(ev(c,x)==add(fp[x],z) for x in pads)
 assert count>=M and ev(c,x0)==add(fp[x0],z)
assert k-2+qpad==M-1
# Universal exact parameter identities, not a finite prime-distribution test.
parameter_cases=0
for kk in range(22,10001,12):
 qq=(kk-10)//3;nn=4*kk-1+qq
 assert 3*nn==13*(kk-1) and Fraction(kk//2+1,nn)>Fraction(3,26)
 assert qq>=Fraction(kk,6) and qq<=kk//2+1
 assert Fraction(qq*3*kk,2*4*4*kk)>=Fraction(nn,300)
 parameter_cases+=1
result=dict(status='passed',p=p,n=len(old)+qpad,dimension=k-1,threshold=M,source_polynomials_enumerated=p**k,source_maximum_agreement=M,source_nearest_list=len(bank),anchor=anchor,anchored_list=len(qs),old_quotients_enumerated=p**(k-1),old_maximum_agreement=oldmax,padding_points=pads,padding_values=[fp[x] for x in pads],exceptional_labels=sorted(witness),exceptional_count=len(witness),exact_expected_union=dict(numerator=expectation.numerator,denominator=expectation.denominator),nonzero_direction_joint_agreement_upper=k-2+qpad,parameter_cases=parameter_cases,scope='Complete finite nearest census and exact witness replay; ordinary-CA exclusion additionally uses the stated interpolation/root-count arguments. Does not numerically verify the asymptotic sieve theorem or assert this small fixture is below Elias.')
Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('padding_points','padding_values','exceptional_labels')},indent=2))
