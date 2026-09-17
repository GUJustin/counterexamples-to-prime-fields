"""Exact affine-in-L thin-route certificate on an explicit saturated interval.
No I/O on import; source parameters (m,s), factor parameters (r,y,t).
Returns an exact minimum feasibleL within that interval, not globally.
"""
import ast
from pathlib import Path
from fast_firstjet_count import coefficient_count
_ns={};_tree=ast.parse((Path(__file__).parent/'replay_phase_kernels.py').read_text());exec(compile(ast.Module(body=[x for x in _tree.body if isinstance(x,ast.FunctionDef) and x.name=='rank'],type_ignores=[]),'rank','exec'),_ns);rank=_ns['rank']

def channel(T,Y,S):
 assert 0<=Y<=T and S>=0
 k=min(S,Y);n=Y-k;B=T+1-Y
 C=(S+1)*(B+S+1)-(S+1)*S//2
 return B*(k+2)*(k+1)//2+(k+2)*(k+1)*k//6+n*C+(S+1)*n*(n-1)//2

def solve(m,s,r,y,t,A=181275,n=262144,w=131071,p=2130706433,gate_t=None,exact_degree=False):
 assert 1<=r<=y<=t and 0<=s and 2*s<=m and m<p and A>w and n>=A
 D=A*m;q=D//w;Y=(D+s-1)//w;delta=A-w+1
 assert s<=q and D+s<=w*(Y+1)
 if s<r or Y<y:return dict(feasible=False,reason='source cannot cover factor')
 fuel=min(Y//y,s//r);dc=w*y-r;Dh=max(0,(D if exact_degree else w*(Y+1)-s)-dc);channels=[]
 for h in range(1,fuel+1):
  ss=s-h*r;eff=min(Y-h*y,max(0,Dh+ss-1)//w);channels.append((h,eff,ss));Dh=max(0,Dh-delta-dc)
 lower=max(Y,m+s-1,t,fuel*t,max(h*t+eff for h,eff,ss in channels))
 T=t if gate_t is None else gate_t
 assert T>=t
 upper=min((p-1-T*s)//r,(p-1-T*Y)//y)
 if max(r,y,T,y*s+r*Y)>=p:return dict(feasible=False,reason='nonL characteristic gate')
 def value(L):
  assert L>=lower
  C=coefficient_count(D,L,s,w);R=rank(m,L,s);band=delta*sum(channel(L-h*t,eff,ss) for h,eff,ss in channels)
  return C-n*R-band
 f0=value(lower);slope=value(lower+1)-f0
 base=dict(m=m,s=s,Y=Y,exact_degree=exact_degree,r=r,y=y,t=t,gate_t=T,fuel=fuel,affine_lower_L=lower,characteristic_upper_L=upper,value_at_lower=f0,slope=slope)
 if upper<lower:return dict(**base,feasible=False,reason='empty affine-characteristic interval')
 if slope>0:
  minimum=max(lower,lower+(-f0)//slope+1)
 elif f0>0:minimum=lower
 else:return dict(**base,feasible=False,reason='nonpositive nonincreasing margin')
 if minimum>upper:return dict(**base,feasible=False,reason='strict gate starts beyond characteristic endpoint',required_L=minimum,value_at_upper=f0+slope*(upper-lower))
 assert value(minimum)>0
 if minimum>lower:assert value(minimum-1)<=0
 maximum=upper if slope>=0 else min(upper,lower+(f0-1)//(-slope))
 return dict(**base,feasible=True,minimum_L=minimum,maximum_L=maximum,strict_margin=value(minimum),value_at_upper=f0+slope*(upper-lower))
