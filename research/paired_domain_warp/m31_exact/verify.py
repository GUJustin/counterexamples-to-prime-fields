"""Replay deterministic M31 instances with independent image enumerators."""
from pathlib import Path
from math import comb,prod
from itertools import combinations
import json,os,subprocess,tempfile,time
BASE=Path(__file__).resolve().parent

def poly_mul(a,b,p):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return c

def poly_eval(a,x,p):
 v=0
 for t in reversed(a):v=(v*x+t)%p
 return v

def right_bank(factors,p):
 m=len(factors);half=m//2
 right=[{} for _ in range(m-half+1)]
 for size in range(m-half+1):
  for I in combinations(range(half,m),size):
   right[size].setdefault(prod(factors[i] for i in I)%p,I)
 return right

def find_support(target,factors,D,p,right):
 # Search only the explicit locator bank, not all possible nearby codewords.
 half=len(factors)//2
 for size in range(half+1):
  needed=D-size
  if not 0<=needed<len(right):continue
  for I in combinations(range(half),size):
   value=prod(factors[i] for i in I)%p
   J=right[needed].get(target*pow(value,-1,p)%p)
   if J is not None:return I+J
 return None

def geometry(a):
 p=a['p'];n=a['n'];K=a['K'];D=a['D'];reps=a['core_representatives'];m=len(reps)
 assert p==2**31-1 and n==2*(m+1) and K==2*D-1
 assert len(set(reps))==m and all(1<x<=(p-1)//2 for x in reps)
 assert a['supports']==comb(m,D)
 count=a['distinct_products']
 # Cubing eliminates the entropy exponent exactly:
 # (n * 2^(H2(K/n)/(3/n)))^3 = n^(n+3)/(K^K*(n-K)^(n-K)).
 lhs=count**3*K**K*(n-K)**(n-K);rhs=n**(n+3)
 assert lhs>rhs
 multiplier=2 if n==68 else 1;assert lhs>multiplier**3*rhs
 assert 3*30>n # Strict Elias using log2(p)>30 and binary entropy<=1.
 domain=[x for b in reps+[1] for x in (b,p-b)]
 w=[1]
 for b in reps[:D]:w=poly_mul(w,[-b*b,0,1],p)
 assert len(w)==K+2 and w[-1]==1 and w[-2]==0
 f=[poly_eval(w,x,p) for x in domain];g=[0]*(2*m)+[1,1]
 assert sum(v==0 for v in f)==K+1 and len(set(domain))==n
 factors=[(1-b*b)%p for b in reps];right=right_bank(factors,p)
 targets=[prod(factors[i] for i in range(j,j+D))%p for j in sorted({0,1,(m-D)//2,m-D})]
 witnesses=[]
 for target in targets:
  I=find_support(target,factors,D,p,right);assert I is not None and len(I)==len(set(I))==D
  H=[1]
  for i in I:H=poly_mul(H,[-reps[i]*reps[i],0,1],p)
  q=[(b-c)%p for b,c in zip(w,H)];assert q[K:]==[0,0]
  z=-target%p;values=[poly_eval(q,x,p) for x in domain]
  assert sum((b+z*c)%p!=v for b,c,v in zip(f,g,values))==n-K-3
  witnesses.append(dict(parameter=z,support_indices=I,polynomial_coefficients=q[:K]))
 instance=dict(p=p,n=n,K=K,domain=domain,f=f,g=g,certified_nearby_parameters=count,witnesses=witnesses)
 summary=dict(n=n,K=K,certified_nearby_parameters=count,violated_prefactor=multiplier,
  far_distance_numerator=n-K-1,nearby_distance_numerator=n-K-3,direction_weight=2,
  explicit_witnesses_recovered=len(witnesses))
 return instance,summary

if __name__=='__main__':
 start=time.monotonic();claims=[json.loads((BASE/'count.json').read_text())]+json.loads((BASE/'nearby_lengths.json').read_text())
 p=2**31-1;ll=4
 for _ in range(29):ll=(ll*ll-2)%p
 assert ll==0
 with tempfile.TemporaryDirectory(prefix='paired-m31-') as temp:
  for source in ['count','replay']:
   binary=Path(temp)/source
   subprocess.run([os.environ.get('CXX','c++'),'-O3','-UNDEBUG','-std=c++17',str(BASE/(source+'.cpp')),'-o',str(binary)],check=True)
  instances=[];rows=[]
  for a in claims:
   args=[str(len(a['core_representatives'])),str(a['D'])]
   for source in ['count','replay']:
    inp=None if source=='count' else ' '.join(map(str,a['core_representatives']))
    result=json.loads(subprocess.check_output([str(Path(temp)/source),*args],input=inp,text=True))
    assert all(result[k]==a[k] for k in ['supports','distinct_products','bitmap_word_fingerprint'])
    if source=='count':assert result['core_representatives']==a['core_representatives']
   instance,row=geometry(a);instances.append(instance);rows.append(row)
   print('PASS n='+str(a['n'])+' K='+str(a['K']),flush=True)
 (BASE/'instance.json').write_text(json.dumps(instances[0],indent=2)+'\n')
 (BASE/'instances.json').write_text(json.dumps(instances,indent=2)+'\n')
 out=dict(status='passed',p=p,rows=rows,independent_enumerators=2,seconds=time.monotonic()-start,
  scope='Deterministic exact image counts for the displayed locator families. These lower-bound total nearby parameters; additional codewords may give additional nearby parameters. No prescribed FFT-domain transfer.')
 (BASE/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
