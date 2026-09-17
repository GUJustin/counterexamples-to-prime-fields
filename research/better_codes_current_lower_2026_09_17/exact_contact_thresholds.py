"""Use actual interpolation contact budget D in the generic thin-band theorem."""
import json
from pathlib import Path
ROOT=Path(__file__).parent
A=181275;W=131071;DELTA=A-W+1

def channel(T,Y,S):
 U=min(T,Y);B=T+1-U;k=min(S,U);nn=U-k
 C=(S+1)*(B+S+1)-(S+1)*S//2
 return B*(k+2)*(k+1)//2+(k+2)*(k+1)*k//6+nn*C+(S+1)*nn*(nn-1)//2

def passes(source,r,v,z,total=9678):
 D,T,Y,S,gap=source
 if z>total-r-v:return True
 t=r+v+z;y=r+v
 if t>T or y>Y or r>S:return False
 fuel=min(T//t,Y//y,S//r);dc=W*y-r;Dh=max(0,D-dc);thin=0
 for h in range(1,fuel+1):
  ss=S-h*r;limit=max(0,Dh+ss-1)//W
  thin+=DELTA*channel(T-h*t,min(Y-h*y,limit),ss)
  if thin>=gap:return False
  Dh=max(0,Dh-DELTA-dc)
 return True

def threshold(source,r,v,total=9678,upper=None):
 lo,hi=0,total+1-r-v if upper is None else min(upper,total+1-r-v)
 assert passes(source,r,v,hi,total)
 while lo<hi:
  mid=(lo+hi)//2
  if passes(source,r,v,mid,total):hi=mid
  else:lo=mid+1
 assert passes(source,r,v,lo,total)
 if lo:assert not passes(source,r,v,lo-1,total)
 return lo

def sources():
 kernels={x['name']:x for x in json.loads((ROOT/'phase_kernel_replay.json').read_text())}
 old=json.loads((ROOT/'target_thresholds_1_7.json').read_text())['sources']
 out=[[kernels[f'Source{j:02}']['m']*A,*row] for j,row in enumerate(old)]
 new=json.loads((ROOT/'new_phase_refined_finalist_0.json').read_text())['candidate']
 out.append([new['m']*A,new['L'],new['Y'],new['s'],new['gap']])
 return out

if __name__=='__main__':
 import sys
 r,v=12,43
 rows=[]
 old=next(x for x in json.loads((ROOT/'regenerated_singletons_1_12.json').read_text())['rows'] if (x['r'],x['v'])==(r,v))
 for j,source in enumerate(sources()):
  D,T,Y,S,g=source
  z=threshold(source,r,v,upper=old['threshold'][j])
  rows.append(dict(source=j,D=D,shape_contact_upper=W*(Y+1)-S,contact_slack=W*(Y+1)-S-D,old_threshold=old['threshold'][j],exact_D_threshold=z))
 (ROOT/'exact_contact_critical.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
