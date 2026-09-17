"""Floating discovery only; exact rational replay required."""
from pathlib import Path
from math import log,log2,lgamma,exp,pi,comb,prod
import heapq,json,time

def main():
 start=time.monotonic();best={};count=0
 for b in [31,61,127,521,1279]:
  heaps={str(r)+":"+str(bits):[] for r in [2,3] for bits in [1,10,40,100]}
  step=max(2,2*(b//50))
  for n in range(max(20,2*(b//4)),40*b+1,step):
   K=n//2
   for percent in range(52,99,2):
    m=round(K/(percent/100));N=m-1;q=n-N
    if q<4:continue
    normsum=lnnorm=0.
    for s in range(1,min(64,m-K-2)+1):
     t=K+1+s;D=t-1
     lnnorm=(log((m*m-1)/12) if s==1 else lnnorm+log(m*m-s*s)-log(4*(2*s-1)*(2*s+1)))
     normsum+=lnnorm
     lnDen=s/2*log(pi)-lgamma(s/2+1)+s/2*log(s+2)+(normsum+s*log(t*(m-t)/(m-1)))/2
     lnL=lgamma(m+1)-lgamma(t+1)-lgamma(m-t+1)-lnDen+log(t/m)
     tau=K-1-D*D/N;e=K-1-max(0,2*D-N)
     if tau<=0 or e<1:continue
     for r in [2,3]:
      A=D+r;gap=A-K
      if A>=n:continue
      ent=-A*log2(A/n)-(n-A)*log2(1-A/n)
      pred=log2(n)+n/gap-b
      if b*gap<=ent or pred>=-1:continue
      if r*b*log(2)-lnL>100:continue
      ratio=0.
      for a in range(r+1):
       if not 0<=r-a<=q-r:continue
       v=comb(r,a)*comb(q-r,r-a)/comb(q,r)
       ratio+=v if a==0 else v*(exp(a*b*log(2)-lnL)+tau*prod(e-j for j in range(1,a)))
      density=1/ratio
      count+=1
      row=(density,n,K,A,m,s,r,lnL/log(2),pred)
      for bits in [1,10,40,100]:
       if pred>=-bits:continue
       heap=heaps[str(r)+":"+str(bits)]
       if len(heap)<5:heapq.heappush(heap,row)
       elif row>heap[0]:heapq.heapreplace(heap,row)
  best[str(b)]={r:[dict(density=x[0],n=x[1],K=x[2],A=x[3],m=x[4],s=x[5],r=x[6],log2L=x[7],prescription_log2_fraction=x[8]) for x in sorted(h,reverse=True)] for r,h in heaps.items()}
 out=dict(scope='Floating discovery only, no optimality claim; exact replay required.',cases=count,seconds=time.monotonic()-start,best=best)
 Path(__file__).with_name('multi_match_search.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(cases=count,seconds=out['seconds'],best={b:{r:rows[0] if rows else None for r,rows in rr.items()} for b,rr in best.items()}),indent=2))
if __name__=='__main__':main()
