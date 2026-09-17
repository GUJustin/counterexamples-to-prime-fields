"""Target-A auxiliary root envelopes derived from Profile.bound.

For each group, bound = MAX of four affine lines. Across eligible groups,
any one group may be chosen, so the singleton solver takes MIN across groups.
This is arithmetic for the target-parameter port; not an existing Lean theorem.
"""
from pathlib import Path
import json,math
from functools import lru_cache
ROOT=Path(__file__).resolve().parent
MANIFEST=json.loads((ROOT/'auxiliary_source_replacements.json').read_text())
SOURCES=[x['replacement'] for x in MANIFEST['sources']]
GROUPS=[x['sources'] for x in MANIFEST['groups']]
A=181275;N=262144;W=131071;GAP=A-W;ERROR_PLUS_ONE=N-A+1
DIRECTIONS=((1,0,0),(0,1,0),(0,0,1))

def mixed(p,q,r):
 a,b,c=p;d,e,f=q;g,h,i=r
 return c*f*i+a*f*i+d*c*i+g*c*f+b*f*i+e*c*i+h*c*f+c*e*h+f*b*h+i*b*e+a*e*i+a*h*f+d*b*i+d*h*c+g*b*f+g*e*c

def flag(P):
 m,B,s,U,L,k,n0=P
 return L-U,U-B+n0,B-2*(n0-k-1)

def graph_value(params,r,v,z):
 scale=math.lcm(*(P[5]+1 for P in params))
 f=(z,v,r)
 first=(131070*z,131070*v-131071,131070*(r-2))
 normal=(131074*z,131074*v-131072,131074*(r-1))
 raw=(131073*z,131073*v,131073*r-1)
 ans=scale*mixed(f,first,normal)
 for j,P in enumerate(params):
  ans+=(W*normal[j]+65539*raw[j])*(scale//(P[5]+1))*mixed(f,DIRECTIONS[j],flag(P))
 return ans,scale

def pair_numerator(r,y,t,capR,capY,capT,A=A):
 gap=A-W;errors=N-A
 my=r*capT+t*capR;mr=y*capT+t*capY;mz=y*capR+r*capY
 return (N-W)*((1+2*W*y)*my+W*(2*r-1)*mr+(1+2*W*t)*mz)+(errors+1)*gap*mz

def numerators(group,r,v,z):
 assert 0<=group<16 and r>=3 and v>=2
 params=[SOURCES[j] for j in GROUPS[group]];y=r+v;t=y+z
 helpers=[];coefficient_sum=0
 for P in params:
  m,B,s,U,L,k,n0=P
  helpers.append(pair_numerator(r,y,t,B+s*(r-1),U+s*(y-1),L+s*(t-1)))
  coefficient_sum+=pair_numerator(r,y,t,B,U,L)
 graph,scale=graph_value(params,r,v,z)
 # floor(graph/scale)+sum floor(coeff/gap) <= floor(combined/(scale*gap)).
 return tuple((q,GAP) for q in helpers)+((GAP*graph+scale*coefficient_sum,GAP*scale),)

def ceildiv(a,b):return (a+b-1)//b

@lru_cache(None)
def root_lines(group,r,v):
 """Return four (integer slope,integer intercept) lines; take their MAX."""
 a=numerators(group,r,v,0);b=numerators(group,r,v,1)
 lines=[]
 for (q0,den),(q1,den1) in zip(a,b):
  assert den==den1 and q1>=q0>=0
  lines.append((ceildiv(q1-q0,den),ceildiv(q0,den)))
 return tuple(lines)

def root_domain(group,r,v):
 """Inclusive (lo,hi) z interval, or None; retains current geometric domain."""
 if not(0<=group<16 and 3<=r<=31 and v>=2 and r+v<=142):return None
 lo=max(3,max(SOURCES[j][4] for j in GROUPS[group])-r-v+1)
 hi=7501-r-v
 return (lo,hi) if lo<=hi else None

def root_upper(group,r,v,z):
 return max(a*z+b for a,b in root_lines(group,r,v))
