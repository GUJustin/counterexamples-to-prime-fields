"""Exhaust all parameters of two million-element prime-field fixtures."""
from pathlib import Path
from math import comb,isqrt,prod
from itertools import combinations,product
from array import array
import json,time,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'paired_domain_warp'))
from verify_extension_profile import interpolate,evaluate
BASE=Path(__file__).resolve().parent

def replay_line(p,d,m,D,c,q,roots,omega):
 M=m+c;mu=[pow(omega,j,p) for j in range(d)];a=roots[:m];extra=roots[m:M];t=roots[-1]
 domain=[x*w%p for x in a for w in mu]+extra+mu+[t*w%p for w in mu];n=len(domain);K=d*D-1
 assert n==d*(m+2)+c and len(set(domain))==n
 hist={}
 for I in combinations(range(1,m+1),D):hist.setdefault(sum(I),[]).append(I)
 S=max(hist,key=lambda s:len(hist[s]));supports=hist[S]
 Ri=[pow(x,d,p) for x in a]
 def loc(I,x):return prod((pow(x,d,p)-Ri[i-1])%p for i in I)%p
 f=[loc(tuple(range(1,D+1)),x) for x in domain];g=[0]*(d*m+c)+[pow(q,S,p)]*d+[1]*d
 expected={}
 for I in supports:
  z=-loc(I,t)%p;assert loc(I,1)*pow(loc(I,t),-1,p)%p==pow(q,S,p)
  expected[z]=tuple((v-loc(I,x))%p for v,x in zip(f,domain))
 assert len(expected)==len(supports)
 actual={};far_agreement=0
 for I in combinations(range(n),K):
  xs=[domain[i] for i in I];A=interpolate(xs,[f[i] for i in I],p);B=interpolate(xs,[g[i] for i in I],p)
  av=[evaluate(A,x,p) for x in domain];bv=[evaluate(B,x,p) for x in domain];common=0;zs={}
  for aa,bb,v,u in zip(av,bv,f,g):
   if bb==u:common+=aa==v
   else:
    z=(v-aa)*pow(bb-u,-1,p)%p;zs[z]=zs.get(z,0)+1
  assert common<K+1+2*d;far_agreement=max(far_agreement,common+zs.get(0,0))
  for z,count in zs.items():
   if common+count>=K+1+2*d:actual.setdefault(z,set()).add(tuple((aa+z*bb)%p for aa,bb in zip(av,bv)))
 assert far_agreement==K+1 and set(actual)==set(expected)
 assert all(actual[z]=={v} for z,v in expected.items())
 return dict(p=p,d=d,m=m,D=D,c=c,q=q,n=n,K=K,selected_sum=S,nearby_count=len(actual),interpolation_pencils=comb(n,K),all_nearby_unique=True,core_roots=a,extra_roots=extra,padding_radical=t,omega=omega)

def audit(p,d,m,D,c,inverses,require_positive_bound=True,replay=True):
 M=m+c;start=time.monotonic();root=array('I',[0])*p
 for x in range(1,p):root[pow(x,d,p)]=x
 omega=root[1];assert omega!=1 and pow(omega,d,p)==1;mu=[pow(omega,j,p) for j in range(d)]
 coeffs=sorted({sum(mu[j] for j in range(d) if mask>>j&1)%p for mask in range(1<<d)})
 assert len(coeffs)==2**d-1
 patterns=[v for v in product(coeffs,repeat=M) if any(v)]
 # Quotient by global nonzero scalar for faster exact zero-sum checks.
 normalized=set()
 for v in patterns:
  first=next(a for a in v if a);inv=pow(first,-1,p);normalized.add(tuple(a*inv%p for a in v))
 terms=[[(i,a) for i,a in enumerate(v) if a] for v in normalized]
 allsupports=list(combinations(range(1,m+1),D));R=D*(m-D);admitting=badroot=badproduct=badorder=good=0;firstgood=None;firstbad={}
 for q in range(1,p):
  t=root[q]
  if not t:continue
  powers=[1];x=1
  for _ in range(M+1):x=x*q%p;powers.append(x)
  if any(x==1 for x in powers[1:]):continue
  aa=[]
  for i in range(1,M+1):
   v=(powers[i+1]-1)*inverses[(powers[i]-1)%p]%p;a=root[v]
   if not a:break
   aa.append(a)
  if len(aa)!=M:continue
  admitting+=1
  br=any(sum(a*aa[i] for i,a in row)%p==0 for row in terms)
  labels=[prod((powers[i]-1)%p for i in I)%p for I in allsupports];bp=len(set(labels))<len(labels)
  bo=any(pow(q,h,p)==1 for h in range(1,R+1))
  badroot+=br;badproduct+=bp;badorder+=bo
  for kind,flag in (('root',br),('product',bp),('order',bo)):
   if flag and kind not in firstbad:firstbad[kind]=q
  if not(br or bp or bo):
   good+=1
   if firstgood is None:firstgood=(q,aa+[t])
 U=(M+1)**2;T=M*(M+1)//2;A0=comb(m,D);Smax=D*(2*m-D+1)//2
 Q0=(p-U)//d**(M+1)-U*(isqrt(p)+2)
 B1=(T+1)*((2**d-1)**M-1);B2=Smax*comb(A0,2);B3=R*(R+1)//2
 assert admitting>=Q0 and badroot<=B1 and badproduct<=B2 and badorder<=B3
 assert good>=Q0-B1-B2-B3
 if require_positive_bound:assert Q0>B1+B2+B3 and firstgood is not None
 line=replay_line(p,d,m,D,c,*firstgood,omega) if firstgood and replay else None
 return dict(p=p,d=d,m=m,D=D,c=c,parameters_scanned=p-1,root_admitting=admitting,bad_root_parameters=badroot,bad_product_parameters=badproduct,bad_order_parameters=badorder,good_parameters=good,certified_root_admitting_lower=Q0,root_bad_upper=B1,product_bad_upper=B2,order_bad_upper=B3,positive_existence_bound=Q0>B1+B2+B3,first_bad_parameters=firstbad,exhaustive_line=line,seconds=time.monotonic()-start)

if __name__=='__main__':
 start=time.monotonic();p=1000003;assert all(p%q for q in range(2,isqrt(p)+1))
 inverses=array('I',[0])*p;inverses[1]=1
 for i in range(2,p):inverses[i]=p-(p//i)*inverses[p%i]%p
 rows=[]
 for args in [(2,4,2,0),(3,2,1,0)]:
  row=audit(p,*args,inverses);rows.append(row);print(json.dumps(row),flush=True)
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,scope='Every field parameter examined, including bad parameters, independently of the asymptotic proof. All potentially nearby codewords classified on one good line per row. Toy geometry does not itself violate the numerical prescription.')
 (BASE/'exhaustive_verification.json').write_text(json.dumps(out,indent=2)+'\n')
