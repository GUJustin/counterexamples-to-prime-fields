"""Exact restored asymmetric second-jet costs with explicit agreement parameter."""
import json
from pathlib import Path
N=262144; W=131071; PRIME=2130706433

def flag_mixed(p,q,r):
 pz,py,pa=p;qz,qy,qa=q;rz,ry,ra=r
 return (pa*qa*ra+pz*qa*ra+qz*pa*ra+rz*pa*qa
  +py*qa*ra+qy*pa*ra+ry*pa*qa
  +pa*qy*ry+qa*py*ry+ra*py*qy
  +pz*qy*ra+pz*ry*qa+qz*py*ra+qz*ry*pa+rz*py*qa+rz*qy*pa)

def left_pair(r,y,t,R,Y,T,A):
 mix=(r*T+t*R,y*T+t*Y,y*R+r*Y)
 agreement=(1+2*W*y,W*(2*r-1),1+2*W*t)
 num=(N-W)*sum(x*y for x,y in zip(agreement,mix))+(N-A+1)*(A-W)*mix[2]
 return num//(A-W),mix

def bound(r,v,z,B,U,L,s,k,n0,A):
 y=r+v;t=y+z
 proper,pm=left_pair(r,y,t,B+s*(r-1),U+s*(y-1),L+s*(t-1),A)
 coefficient,cm=left_pair(r,y,t,B,U,L,A)
 first=(N*z,1+N*v,N*max(r-1,0))
 rational=((W+3)*z,(W+3)*max(v-1,0)+2,(W+3)*max(r-2,0)+3)
 normal=flag_mixed((z,v,r),first,rational)
 q=(max(L-U,0),max(U-B,0)+n0,max(B-2*max(n0-(k+1),0),0))
 moving=flag_mixed((z,v,r),first,q)
 retained=normal+(W+5)*((moving+k)//(k+1))+coefficient
 return dict(r=r,v=v,z=z,total=t,active=L<t,proper=proper,normal=normal,moving=moving,coefficient=coefficient,retained=retained,bound=max(proper,retained),winner='retained' if retained>=proper else 'proper',budget_flag=q,mixed_proper=pm,mixed_coefficient=cm,char_gates=max(pm+cm+(r,y,t))<PRIME)

if __name__=='__main__':
 old=bound(10,37,2276,47,155,2255,21,5,7,181353)
 assert old['bound']==268923679246212987,old
 profiles=[dict(name='108',m=108,B=41,s=19,U=146,k=4,n0=7,L=2557),dict(name='114',m=114,B=47,s=21,U=155,k=5,n0=7,L=2777),dict(name='116',m=116,B=47,s=21,U=157,k=5,n0=7,L=2721),dict(name='96',m=96,B=38,s=17,U=130,k=4,n0=5,L=2698)]
 rows=[]
 for prof in profiles:
  row=bound(12,43,3206,*(prof[x] for x in ['B','U','L','s','k','n0']),181275)
  row['profile']=prof;rows.append(row)
 out=dict(scope='Exact target-A arithmetic for restored proper AND retained branches; no full propagated receipt yet.',old_primary_fixture=old,rows=rows)
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
