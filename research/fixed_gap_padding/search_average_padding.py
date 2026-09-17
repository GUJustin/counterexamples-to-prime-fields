"""Floating-point discovery only; exact certificates are separately replayed."""
from pathlib import Path
import math,json,time,heapq


def entropy(x):return -x*math.log2(x)-(1-x)*math.log2(1-x)


def main():
 start=time.monotonic();best={b:[] for b in (31,61,127,521)};cases=0
 for m in range(20,1601):
  normsum=0.;lnnorm=0.;dens={}
  for s in range(1,min(25,m//3)+1):
   lnnorm=(math.log((m*m-1)/12) if s==1 else lnnorm+math.log(m*m-s*s)-math.log(4*(2*s-1)*(2*s+1)))
   normsum+=lnnorm
   dens[s]=s/2*math.log(math.pi)-math.lgamma(s/2+1)+s/2*math.log(s+2)+normsum/2
  for k in range(2,m-1,1 if m<=600 else 4):
   for s,denbase in dens.items():
    t=k+s
    if t>=m:continue
    n=m+s;K=k-1;q=s+1;D=k-2
    D=D-(t-1)**2/(m-1)
    if D<=0:continue
    lnL=(math.lgamma(m+1)-math.lgamma(t+1)-math.lgamma(m-t+1)
         -denbase-s/2*math.log(t*(m-t)/(m-1))+math.log(t/m))
    if lnL<=0:continue
    cases+=1;threshold=math.log2(n)+entropy(K/n)*n/q
    for b,heap in best.items():
     if m>600 and b!=521:continue
     if q*b<=n*entropy(t/n):continue
     lnratio=b*math.log(2)-lnL
     if lnratio>700:continue
     inv=math.exp(lnratio)
     z=1/(D+inv)
     logJ=b+math.log2(-math.expm1(q*math.log1p(-z)))
     score=logJ-threshold
     row=(score,m,k,t,lnL/math.log(2),logJ)
     if len(heap)<8:heapq.heappush(heap,row)
     elif row>heap[0]:heapq.heapreplace(heap,row)
 result=dict(scope='Floating discovery, ignores negligible Gram smoothing in ranking; exact replay required. Not an optimality proof.',cases=cases,seconds=time.monotonic()-start,
             best={str(b):[dict(excess_bits=r[0],m=r[1],k=r[2],t=r[3],log2_anchored_list=r[4],log2_labels=r[5]) for r in sorted(rows,reverse=True)] for b,rows in best.items()})
 Path(__file__).with_name('average_padding_search.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
