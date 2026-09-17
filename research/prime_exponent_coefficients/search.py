"""Rank half-rate interval list certificates; floating-point discovery only."""
from pathlib import Path
import json
import math

def main():
    output={}
    for b in (31,61,127,521):
        rows=[]
        for m in range(1,b+1):
            n=2*((b*m)//2);k=n//2;t=k+m
            if t>=n:continue
            logv=math.log(t*(n-t)*(n+1)/12)
            variance_sum=0.0
            for j in range(1,m+1):
                if j>1:logv+=math.log(n*n-j*j)-math.log(4*(2*j-1)*(2*j+1))
                variance_sum+=logv+math.log1p(math.exp(-logv)/12)
            logden=m/2*math.log(math.pi)-math.lgamma(m/2+1)+m/2*math.log(m+2)+variance_sum/2
            logcount=(math.lgamma(n+1)-math.lgamma(t+1)-math.lgamma(n-t+1)-logden)/math.log(2)
            rows.append(dict(prime_exponent=b,n=n,k=k,m=m,t=t,
                             approximate_log2_list=logcount,approximate_forced_c2=m*logcount/n))
        rows.sort(key=lambda r:-r['approximate_forced_c2'])
        output[b]=rows[:5]
    data={'scope':'Discovery among half-rate n=largest even integer at most b*m, not an optimality proof. Exact Elias replay required.','best':output}
    Path(__file__).with_name('search_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__':main()
