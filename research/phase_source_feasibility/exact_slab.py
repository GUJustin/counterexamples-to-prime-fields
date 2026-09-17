"""Exact thin slab, retaining caps and strict weighted-degree endpoints."""
def channel(T,Y,S):
 if min(T,Y,S)<0:return 0
 U=min(T,Y);B=T+1-U;k=min(S,U);nn=U-k
 C=(S+1)*(B+S+1)-(S+1)*S//2
 return B*(k+2)*(k+1)//2+(k+2)*(k+1)*k//6+nn*C+(S+1)*nn*(nn-1)//2

def positive_sum(b,k):
 lo=max(0,1-b)
 if lo>k:return 0
 n=k-lo+1
 return n*b+(lo+k)*n//2

def slab(D,T,Y,S,width,w=131071):
 if D<=0 or min(T,Y,S)<0:return 0
 U=min(T,Y);full=min(U,(D-width)//w)
 ans=width*channel(T,full,S) if full>=0 else 0
 end=min(U,(D+S-1)//w)
 for u in range(max(0,full+1),end+1):
  k=min(S,u);b=D-w*u
  ans+=(T+1-u)*(positive_sum(b,k)-positive_sum(b-width,k))
 return ans

def thin(D,L,Y,S,r,v,z,width,w=131071,exact=True):
 y=r+v;t=y+z
 if t>L or y>Y or r>S:return 0
 fuel=min(L//t,Y//y,S//r);dc=w*y-r;Dh=max(0,D-dc);total=0
 for h in range(1,fuel+1):
  TT=L-h*t;YY=Y-h*y;SS=S-h*r
  if exact:total+=slab(Dh,TT,YY,SS,width,w)
  else:total+=width*channel(TT,min(YY,max(0,Dh+SS-1)//w),SS)
  Dh=max(0,Dh-width-dc)
 return total

if __name__=='__main__':
 # Independent brute monomial sums, including multi-channel boundaries.
 checks=0
 for w in [3,7]:
  for width in range(1,w+3):
   for D in range(0,25):
    for T,Y,S in [(0,0,0),(4,2,3),(3,6,4),(6,6,6)]:
     direct=sum((T+1-i-j)*min(width,max(0,D-w*i-(w-1)*j)) for j in range(min(S,Y,T)+1) for i in range(min(Y,T)-j+1))
     assert slab(D,T,Y,S,width,w)==direct,(w,width,D,T,Y,S)
     checks+=1
 print('Exact slab checks:',checks)
