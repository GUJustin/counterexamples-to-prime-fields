"""Context-local singleton sources; no global phase characteristic restriction."""
import ast,json,math
from fractions import Fraction
from pathlib import Path
import fast_firstjet_count as fast
import trace_singleton_contacts as contact
import repaired_auxiliary_roots as roots
ROOT=Path(__file__).parent
for filename,names in [('replay_phase_kernels.py',{'rank'}),('search_new_phase.py',{'channel','threshold'}),('search_char_limited_phase.py',{'thin'})]:
 tree=ast.parse((ROOT/filename).read_text().replace('9275','9678').replace('9276','9679'));exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),filename,'exec'))
A=181275;n=262144;w=131071;delta=A-w+1;p=2130706433
r,v=12,43;y=r+v;finish=9679-y;segments=contact.segments;oldpoints=contact.points
oldcache={z:min(a*z+b for lo,hi,a,b in segments if lo<=z<=hi) for z in oldpoints}

def evaluate(m,L,s):
 Y=(A*m+s-1)//w
 mixed=[r*L+9678*s,y*L+9678*Y,y*s+r*Y]
 if max(mixed)>=p:return None
 gap=fast.coefficient_count(A*m,L,s)-n*rank(m,L,s)
 if gap<=0:return None
 th=threshold(L,Y,s,gap,r,v)
 if th>=3207:return None
 g=A-w;num0=roots.pair_numerator(r,y,y,s,Y,L);num1=roots.pair_numerator(r,y,y+1,s,Y,L)
 a=(num1-num0+g-1)//g;b=(num0+g-1)//g
 points=set(oldpoints);points.update(z for z in [th-1,th,finish-1] if 0<=z<finish)
 for lo,hi,aa,bb in segments:
  if a!=aa:
   cross=(bb-b)//(a-aa);points.update(z for z in [cross,cross+1] if max(lo,th)<=z<=hi)
 best=-1;where=None
 for z in points:
  old=oldcache.get(z)
  if old is None:old=min(aa*z+bb for lo,hi,aa,bb in segments if lo<=z<=hi)
  value=min(old,a*z+b) if z>=th else old
  if value>best:best=value;where=z
 return dict(m=m,L=L,s=s,Y=Y,gap=gap,threshold=th,helper_line=[a,b],singleton_bound=best,binding_z=where,char_mixed_at_total9678=mixed)

results=[];tested=0;seen=set()
for m in [1000,2000,4000,8000,14000,20000,28000,40000,64000,80000,100000,120000,140000]:
 for sigma in [3046214,3097500]:
  for ds in [-2,0,2]:
   s=(sigma*m+5000000)//10000000+ds;Y=(A*m+s-1)//w
   Lmax=min((p-1-9678*Y)//y,(p-1-9678*s)//r)
   for L in set([Lmax]+[min(Lmax,k*m) for k in [70,130,260,520]]):
    if L<(A*m)//w or(m,L,s) in seen:continue
    seen.add((m,L,s));tested+=1;got=evaluate(m,L,s)
    if got:results.append(got)
results.sort(key=lambda x:x['singleton_bound'])
samples=[]
for lam in [130,260,520]:
 m=28000;s=8529;L=lam*m;Y=(A*m+s-1)//w;gap=fast.coefficient_count(A*m,L,s)-n*rank(m,L,s);band=thin(L,Y,s,r,v,3206)
 f=Fraction(gap-band,w*m**4)
 samples.append(dict(m=m,L=L,s=s,Y=Y,normalized_margin=str(f),normalized_float=float(f),threshold=threshold(L,Y,s,gap,r,v)))
out=dict(tested=tested,earlier_valid_sources=len(results),best=results[:30],finite_correction_samples=samples,scope='Exact local singleton candidate, needs local A={F} adapter and global envelope/packing replay; not globalphase or scorecertificate.')
(ROOT/'local_singleton_source_grid.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'best':results[:5]},indent=2))
