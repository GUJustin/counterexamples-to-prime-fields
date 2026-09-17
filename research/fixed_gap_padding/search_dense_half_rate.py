"""Floating discovery of half-rate high-density padding; exact replay required."""
from pathlib import Path
import math,json,time,heapq


def H(x):return -x*math.log2(x)-(1-x)*math.log2(1-x)


def main():
 start=time.monotonic();best={str(b):[] for b in (31,61,127,521)};restricted={str(b):[] for b in (31,61,127,521)};count=0;bybits={str(c):{str(b):[] for b in (31,61,127,521)} for c in (10,20,40)}
 def keep(heap,row):
  if len(heap)<6:heapq.heappush(heap,row)
  elif row>heap[0]:heapq.heapreplace(heap,row)
 for n in range(40,4001,2):
  K=n//2
  for percent in range(52,99):
   m=round(K/(percent/100));N=m-1;q=n-N
   if q<=0:continue
   normsum=0.;lnnorm=0.
   for s in range(1,min(32,m-K-2)+1):
    A=K+1+s
    lnnorm=(math.log((m*m-1)/12) if s==1 else lnnorm+math.log(m*m-s*s)-math.log(4*(2*s-1)*(2*s+1)))
    normsum+=lnnorm
    lnD=s/2*math.log(math.pi)-math.lgamma(s/2+1)+s/2*math.log(s+2)+(normsum+s*math.log(A*(m-A)/(m-1)))/2
    lnL=math.lgamma(m+1)-math.lgamma(A+1)-math.lgamma(m-A+1)-lnD+math.log(A/m)
    residual=K-1-(A-1)**2/N
    if residual<=0 or lnL<=0:continue
    count+=1;gap=A-K;entropy=n*H(A/n)
    for b in (31,61,127,521):
     if b*gap<=entropy:continue
     if b*math.log(2)-lnL>700:continue
     x=1/(residual+math.exp(b*math.log(2)-lnL)+(A-K)*math.exp(-lnL))
     if not 0<x<1:continue
     score=-q*math.log1p(-x)/math.log(2)
     pred=math.log2(n)+n/gap-b
     row=(score,n,K,A,m,s,lnL/math.log(2),pred)
     keep(best[str(b)],row)
     if pred<-1:keep(restricted[str(b)],row)
     for c,heaps in bybits.items():
      if pred<-int(c):keep(heaps[str(b)],row)
 def rows(data):return {b:[dict(missing_fraction_log2_upper=-r[0],n=r[1],K=r[2],A=r[3],m=r[4],s=r[5],log2_list=r[6],prescription_log2_fraction=r[7]) for r in sorted(rs,reverse=True)] for b,rs in data.items()}
 out=dict(scope='Floating search, not an optimality proof. Exact moment counts, density, direction and Elias checks required.',cases=count,seconds=time.monotonic()-start,best=rows(best),prescription_below_half=rows(restricted),by_prescription_bits={c:rows(rs) for c,rs in bybits.items()})
 Path(__file__).with_name('dense_half_rate_search.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(cases=count,seconds=out['seconds'],best={b:r[0] for b,r in out['best'].items()},restricted={b:r[0] for b,r in out['prescription_below_half'].items() if r}),indent=2))
if __name__=='__main__':main()
