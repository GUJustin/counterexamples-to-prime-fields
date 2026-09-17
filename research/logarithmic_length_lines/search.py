"""Discovery scan of pure finite-field coding bounds; approximate ranking only."""
import math,json,time
from pathlib import Path
start=time.monotonic()
ln2=math.log(2)
bests={b:[] for b in (31,61,124,127)}
count=0
for n in range(12,513):
    gram=[]
    prodlog=0.0
    for j in range(1,17):
        prodlog+=math.log(n*n-j*j) if j<n else 0
        gram.append(prodlog-math.log(2*j+1)-2*(math.lgamma(2*j+1)-math.lgamma(j+1)))
    for k in range(1,n-2):
        entropy=(n*math.log(n)-k*math.log(k)-(n-k)*math.log(n-k))/ln2
        for r in range(2,min(17,n-k)):
            m=r-1;t=k+r
            if t>=n:continue
            variance_factor=math.log(t*(n-t)/(n-1))
            lv=[variance_factor+gram[j] for j in range(m)]
            ld=m/2*math.log(math.pi)-math.lgamma(m/2+1)+m/2*math.log(m+2)
            ld+=sum(.5*(v+math.log1p(math.exp(-v)/12)) for v in lv)
            logN=math.lgamma(n+1)-math.lgamma(t+1)-math.lgamma(n-t+1)-ld
            if logN<0:continue
            effective=k-t*t/n
            if effective<=0:continue
            for b in bests:
                characteristic_bits=31 if b==124 else b
                agreement_entropy=(n*math.log(n)-t*math.log(t)-(n-t)*math.log(n-t))/ln2
                if r*characteristic_bits <= agreement_entropy: continue
                # Stable log of N*p/(p+N*effective+r).
                term=logN+math.log(effective)-b*ln2
                logJ=logN-(max(0,term)+math.log1p(math.exp(-abs(term))))
                excess=logJ/ln2-math.log2(n)-entropy/r
                if len(bests[b])<12 or excess>bests[b][-1]['approx_excess_bits']:
                    row=dict(n=n,k=k,t=t,r=r,m=m,approx_excess_bits=excess,approx_log2_N=logN/ln2)
                    bests[b].append(row);bests[b].sort(key=lambda x:-x['approx_excess_bits']);bests[b]=bests[b][:12]
            count+=1
out=dict(scope='Approximate discovery only, finite bounds require exact replay.',candidates=count,seconds=time.monotonic()-start,best=bests)
Path(__file__).with_name('search_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
