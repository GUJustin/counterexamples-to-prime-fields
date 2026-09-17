"""Complete n=16 boundary-list census in selected split prime fields."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from math import comb
import json
import time
import sympy as sym


def scan(p):
    n,A=16,8
    root=next(x for x in range(2,p) if pow(x,n,p)==1 and pow(x,n//2,p)!=1)
    nodes=[pow(root,r,p) for r in range(n)]
    powers=[[pow(x,j,p) for j in range(1,A)] for x in nodes]
    counts=[Counter() for s in range(1,A)]
    for subset in combinations(range(n),A):
        moments=tuple(sum(powers[i][j] for i in subset)%p for j in range(A-1))
        for s in range(1,A):
            counts[s-1][moments[:s]]+=1
    rows=[]
    for s,counter in enumerate(counts,1):
        K=A-s;h=1
        while h<=s:h*=2
        q=n//h;char0=comb(q,q//2)
        key,maximum=max(counter.items(),key=lambda item:item[1])
        below=n**n*(p-1)**(n-A)<(n-A)**(n-A)*A**A*p**(n-K)
        rows.append(dict(p=p,root=root,n=n,A=A,K=K,s=s,
                         maximum_list=maximum,zero_moment_list=counter[(0,)*s],
                         characteristic_zero_upper=char0,
                         strict_Elias=below,exceeds_char0=maximum>char0,
                         maximizing_moments=list(key)))
    return rows


def main():
    start=time.monotonic()
    primes=[p for p in range(17,1001,16) if sym.isprime(p)]+[2017,40961,65537]
    assert all(sym.isprime(p) and p%16==1 for p in primes)
    rows=[row for p in primes for row in scan(p)]
    hits=[row for row in rows if row['strict_Elias'] and row['exceeds_char0']]
    result=dict(status='PASS',rows=rows,below_Elias_exceptions=hits,
                subsets_per_field=comb(16,8),fields=len(primes),
                seconds=time.monotonic()-start,
                scope='Complete degree-at-most-8 word boundary classes on mu_16 in the listed primes; not arbitrary received words or an asymptotic result.')
    Path(__file__).with_name('subgroup_exception_scan.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))


if __name__=='__main__':main()
