from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
import json,time
base=Path(__file__).parent;t0=time.monotonic();p=2130706433;S=1<<160
# Alternating-series enclosure of Machin's pi identity.
def atan_bounds(q):
 a=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(40)),F(0))
 return a,a+F(1,81*q**81)
a,b=atan_bounds(5);c,d=atan_bounds(239);pl=16*a-4*d;pu=16*b-4*c
floor=lambda x:x.numerator//x.denominator
ceil=lambda x:-((-x.numerator)//x.denominator)
PI=(floor(S*pl),ceil(S*pu))
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v)//S,-((-max(v))//S)
def div(a,n):return a[0]//n,-((-a[1])//n)
def neg(a):return -a[1],-a[0]
def add(a,b):return a[0]+b[0],a[1]+b[1]
rem=ceil(F(S*7**62,factorial(62)))
cache={}
def enclose(r):
 if r in cache:return cache[r]
 x=(2*PI[0]*r//p,-((-2*PI[1]*r)//p));x2=mul(x,x)
 sn=x;cs=(S,S);st=x;ct=(S,S)
 for k in range(1,31):
  st=neg(div(mul(st,x2),(2*k)*(2*k+1)));ct=neg(div(mul(ct,x2),(2*k-1)*(2*k)))
  sn=add(sn,st);cs=add(cs,ct)
 result=((cs[0]-rem,cs[1]+rem),(sn[0]-rem,sn[1]+rem));cache[r]=result;return result
lines=(base/'phases.txt').read_text().splitlines();assert lines[0]=='META 1 1';count=0
for line in lines[1:]:
 ell,h,j,r,re,im=line.split();intervals=enclose(int(r))
 for text,(lo,hi) in zip((re,im),intervals):
  v=F.from_float(float(text));assert abs(v-F(lo,S))<=F(1,2*10**10) and abs(v-F(hi,S))<=F(1,2*10**10)
 count+=1
assert count==6*8*255
# Pathwise DP error: deliberately very conservative factor per input stage.
N=comb(255,136);delta=F(1,10**9);E=((1+delta)**255-1)*N+1
raw=json.loads((base/'coefficients.json').read_text());H={(r['direction'],r['harmonic']):r['values'] for r in raw['coefficients']}
nh=[int(x) for x in json.loads((base.parents[1]/'better_codes_revisit_2026_09_17/product_distribution.json').read_text())['counts']]
target=274980728111395088;maxratio=F(0);arg=None
for ell in range(1,7):
 for h in range(256):
  bound=F(nh[h])
  for k in range(1,9):
   re,im=H[ell,k][h];amp=abs(F.from_float(re))+abs(F.from_float(im))+E
   bound+=2*F(9-k,9)*amp
  assert bound<(target-1)*p**6
  ratio=bound/(p**6*target)
  if ratio>maxratio:maxratio=ratio;arg=[ell,h]
out={'phase_enclosures':'exact fixed-point integer intervals; Machin alternating series and Taylor remainder','phase_samples_checked':count,'distinct_phase_arguments':len(cache),'phase_complex_absolute_error_bound':'1e-10','per_stage_pathwise_error_factor':'1+1e-9','DP_absolute_error_bound_formula':'((1+1e-9)^255-1)*C(255,136)+1','relative_error_to_total_support_count_upper':float(E/N),'certified_all_center_upper_ratio_to_target':float(maxratio),'maximizer':arg,'certified_directions':6,'product_classes_each':256,'harmonics':8,'verdict':'all tested Fejer certificates strictly below target at every center','arithmetic_assumptions':'recorded IEEE binary64, round-to-nearest; compiled -O2 without fast-math; standard complex add/multiply; no overflow; underflow covered by +1','seconds':time.monotonic()-t0}
(base/'certified.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
