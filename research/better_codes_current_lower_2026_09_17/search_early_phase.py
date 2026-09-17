"""Search source00-scale source shapes against the actual binding singleton."""
import ast,json,math
from pathlib import Path
import fast_firstjet_count as fast
import trace_singleton_contacts as contact
ROOT=Path(__file__).parent
# Pure exact source math, with target total cap9678.
for filename,names in [('replay_phase_kernels.py',{'rank','count'}),('search_new_phase.py',{'channel','threshold'})]:
 tree=ast.parse((ROOT/filename).read_text().replace('9275','9678').replace('9276','9679'));exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),filename,'exec'))
A=181275;n=262144;w=131071;delta=A-w+1;p=2130706433
# Independent direct sum checks include residue crossings omitted by oldclosed formula.
for m in [1,7,250,350,1000,8000,32000,64000,88000]:
 for s in [m//4,m//3]:
  D=A*m;L=max(2*m,math.ceil(D/w))
  assert fast.coefficient_count(D,L,s)==count(D,L,s),(m,s)

def potential(L,Y,S):
 cy,cr,cz=1+2*w*163,w*71,1+2*w*9678
 terms=[((n-w)*(cy*S+cr*Y),0),((n-w)*(cr*L+cz*S),(n-A+1)*S),((n-w)*(cy*L+cz*Y),(n-A+1)*Y)]
 return tuple((a+A-w-1)//(A-w)+b for a,b in terms)

r,v=12,43;y=r+v;finish=9679-y
segments=contact.segments;oldpoints=contact.points
oldcache={z:min(a*z+b for lo,hi,a,b in segments if lo<=z<=hi) for z in oldpoints}
def evaluate(m,L,s):
 Y=(A*m+s-1)//w
 mixed=[36*L+9678*s,163*L+9678*Y,163*s+36*Y]
 if max(mixed)>=p:return None
 gap=fast.coefficient_count(A*m,L,s)-n*rank(m,L,s)
 if gap<=0:return None
 th=threshold(L,Y,s,gap,r,v)
 if th>=3207:return None
 a,b,c=potential(L,Y,s);intercept=(a+b)*y+c*r
 points=set(oldpoints)
 points.update(z for z in [th-1,th,finish-1] if 0<=z<finish)
 for lo,hi,aa,bb in segments:
  if a!=aa:
   cross=(bb-intercept)//(a-aa)
   points.update(z for z in [cross,cross+1] if max(lo,th)<=z<=hi)
 best=-1;where=None
 for z in points:
  old=oldcache.get(z)
  if old is None:old=min(aa*z+bb for lo,hi,aa,bb in segments if lo<=z<=hi)
  value=min(old,a*z+intercept) if z>=th else old
  if value>best:best=value;where=z
 return dict(m=m,L=L,s=s,Y=Y,gap=gap,threshold=th,potential=[a,b,c],singleton_bound=best,binding_z=where,char_mixed=mixed)
known=json.loads((ROOT/'target_thresholds_1_7.json').read_text())['sources'][0]
assert fast.coefficient_count(A*64000,3840000,19840)-n*rank(64000,3840000,19840)==known[3]
assert threshold(*known,r,v)==contact.ts[0]==3207
assert potential(*known[:3])==tuple(contact.pot[0])
results=[];tested=0
for m in [16000,32000,48000,64000,80000,88000]:
 for sr in [285,295,300,305,310,315,320,325,335]:
  for lr in [40,45,50,55,60,65,70,75,80,90]:
   tested+=1;got=evaluate(m,m*lr,m*sr//1000)
   if got:results.append(got)
results.sort(key=lambda x:x['singleton_bound'])
out=dict(tested=tested,earlier_valid_sources=len(results),baseline_singleton=contact.record['own'][0],best=results[:40],scope='Exactlocal singleton envelope improvement only;global singleton/packing/phase propagationstillrequired.')
(ROOT/'early_phase_grid.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'best':results[:5]},indent=2))
