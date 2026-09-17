"""Distinct high-L/m branch at exact global characteristic gate."""
import ast,json,math
from fractions import Fraction
from pathlib import Path
import fast_firstjet_count as fast
import trace_singleton_contacts as contact
ROOT=Path(__file__).parent
for filename,names in [('replay_phase_kernels.py',{'rank'}),('search_new_phase.py',{'channel','threshold'}),('search_early_phase.py',{'potential','evaluate'})]:
 tree=ast.parse((ROOT/filename).read_text().replace('9275','9678').replace('9276','9679'));exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),filename,'exec'))
A=181275;n=262144;w=131071;delta=A-w+1;p=2130706433
r,v=12,43;y=r+v;finish=9679-y;segments=contact.segments;oldpoints=contact.points
oldcache={z:min(a*z+b for lo,hi,a,b in segments if lo<=z<=hi) for z in oldpoints}
results=[];tested=0
for m in [500,750,1000,1500,2000,2500,3000,3500,4000,4500,4700,5000,5500,6000,7000,8000,10000,12000,16000,24000,32000]:
 for ds in range(-3,4):
  s=(3046214*m+5000000)//10000000+ds;Y=(A*m+s-1)//w
  L=min((p-1-9678*Y)//163,(p-1-9678*s)//36)
  tested+=1;got=evaluate(m,L,s)
  if got:results.append(got)
results.sort(key=lambda x:x['singleton_bound'])

def thin(L,Y,S,r,v,z):
 t=r+v+z;y=r+v;fuel=min(L//t,Y//y,S//r);dc=w*y-r;Dh=max(0,w*(Y+1)-S-dc);answer=0
 for h in range(1,fuel+1):
  ss=S-h*r;limit=max(0,Dh+ss-1)//w
  answer+=delta*channel(L-h*t,min(Y-h*y,limit),ss)
  Dh=max(0,Dh-delta-dc)
 return answer
samples=[]
for m in [14000,28000]:
 s=round(.3046214*m);L=260*m;Y=(A*m+s-1)//w;gap=fast.coefficient_count(A*m,L,s)-n*rank(m,L,s);band=thin(L,Y,s,r,v,3206)
 f=Fraction(gap-band,w*m**4)
 samples.append(dict(m=m,L=L,s=s,Y=Y,gap=gap,thin_at_z3206=band,normalized_margin=str(f),normalized_float=float(f),threshold=threshold(L,Y,s,gap,r,v)))
out=dict(tested=tested,earlier_valid_sources=len(results),best=results[:30],continuum_samples=samples,scope='Exactcharlimited highlambda singleton filter; fullpropagation required.')
(ROOT/'char_limited_phase_grid.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'best':results[:5]},indent=2))
