"""Target primary-B, residual-pair and derivative-chain arithmetic."""
from functools import lru_cache
A=181275;N=262144;W=131071;PRIME=2130706433;GAP=A-W;ERROR_PLUS_ONE=N-A+1
TAIL_ALLOWANCE=9000000000000

def mixed(left,right):
 y,r,t=left;Y,R,T=right
 return r*T+t*R,y*T+t*Y,y*R+r*Y

def agreement(caps):
 y,r,t=caps
 return 1+2*W*y,W*max(0,2*r-1),2*W*t+1

def residual_pair(left,right,A=A):
 g=A-W;e=N-A;v=mixed(left,right);a=tuple(max(x,y) for x,y in zip(agreement(left),agreement(right)))
 return ((N-W)*sum(x*y for x,y in zip(a,v))+(e+1)*g*v[2])//g

def tight_tail(D,L,A=A):
 Y=(D-1)//W;g=A-W;e=N-A
 av=(1+2*W*Y,W,2*W*L+1);cost=(L,2*Y*L,Y)
 return ((N-W)*sum(x*y for x,y in zip(av,cost))+(e+1)*g*Y+2*L*L*g)//g

@lru_cache(None)
def unit_coeff(y,d,A=A,tail=TAIL_ALLOWANCE):
 g=A-W;e=N-A;dm=max(0,d-1)
 zc=dm*(3*d*(N-W)*(1+4*W*y)+4*(N-W)*W*y*dm)
 co=dm*3*d*((N-W)+g*(e+1))*y+2*g*tail
 den=2*g*d
 return (zc//den+1,co//den+1) if den else (1,1)

def unit(y,z,d,A=A,tail=TAIL_ALLOWANCE):
 slope,intercept=unit_coeff(y,d,A,tail)
 return max(tail,slope*z+intercept)

def initial_potential(wideY,wideR,total,source=(176421,163,36),A=A):
 L,Y,R=source;g=A-W;e=N-A
 ay=1+2*W*wideY;ar=W*(2*wideR-1);az=1+2*W*total
 nums=((N-W)*(ay*R+ar*Y),(N-W)*(ar*L+az*R)+(e+1)*g*R,(N-W)*(ay*L+az*Y)+(e+1)*g*Y)
 return tuple((v+g-1)//g for v in nums)

def complement(r,y,t,wideY,wideR,total,potential):
 tt=max(0,total-t);yy=max(0,wideY-y);rr=max(0,wideR-r)
 nr=min(tt,yy,rr);nv=min(tt-nr,yy-nr)
 return potential[0]*tt+potential[1]*(nr+nv)+potential[2]*nr

def ledger_overhead(r,y,t,B=(185,40,22192),T=(312,70,9682),total=9678,A_source=(176421,163,36),A=A,tail=TAIL_ALLOWANCE):
 Y,R,L=B
 pot=initial_potential(Y,R,total,A_source,A)
 return (complement(r,y,t,Y,R,total,pot)+r*unit(y,t,r,A,tail)
 +(R-r)*unit(Y-y,L-t,R-r,A,tail)+2*tail+residual_pair(B,T,A))
