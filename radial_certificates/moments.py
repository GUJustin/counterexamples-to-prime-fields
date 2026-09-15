"""Exact symmetric-pair subset moment DP; no simulation or floating point."""
from itertools import combinations
from math import comb
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent


def exact_moments(n, t, degree=18):
    assert n % 2 == 0 and (n*n-1) % 3 == 0
    center = (n*n-1)//3
    indices = [(i,j) for i in range(0,degree+1,2) for j in range(degree-i+1)]
    index = {ij:z for z,ij in enumerate(indices)}
    dp = [[0]*len(indices) for _ in range(t+1)]
    dp[0][index[0,0]] = 1
    for stage,u in enumerate(range(1,n,2)):
        v = (u*u-center)//4
        assert (u*u-center) % 4 == 0
        up = [u**i for i in range(degree+1)]
        vp = [v**j for j in range(degree+1)]
        one, two = [], []
        for i,j in indices:
            one.append([(index[p,q],2*comb(i,p)*comb(j,q)*up[i-p]*vp[j-q])
                        for p in range(0,i+1,2) for q in range(j+1)])
            two.append([(index[i,q],comb(j,q)*(2*v)**(j-q)) for q in range(j+1)])
        nxt = [row.copy() for row in dp]
        for size in range(min(t,2*stage)+1):
            old = dp[size]
            if size+1 <= t:
                dest = nxt[size+1]
                for z,terms in enumerate(one):
                    dest[z] += sum(old[w]*c for w,c in terms)
            if size+2 <= t:
                dest = nxt[size+2]
                for z,terms in enumerate(two):
                    dest[z] += sum(old[w]*c for w,c in terms)
        dp=nxt
    return dict(zip(indices,dp[t]))


def validate_small():
    checks=0
    fixtures=[]
    for n,t in [(4,2),(8,3),(8,4),(10,4)]:
        got=exact_moments(n,t)
        direct={ij:0 for ij in got}
        center=(n*n-1)//3
        for subset in combinations(range(n),t):
            x=sum(2*a-(n-1) for a in subset)
            y=sum(((2*a-(n-1))**2-center)//4 for a in subset)
            for i,j in direct:
                direct[i,j] += x**i*y**j
        assert got==direct,(n,t)
        checks+=len(got)
        fixtures.append({'n':n,'t':t,'subsets':comb(n,t),'moments':len(got)})
    return {'fixtures':fixtures,'exact_moment_checks':checks}


def main():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--degree',type=int,default=18)
    args=parser.parse_args()
    degree=args.degree
    start=time.time()
    small=validate_small()
    print('Small exhaustive checks passed:',small,flush=True)
    raw=exact_moments(64,30,degree)
    assert raw[0,0]==comb(64,30)
    qnum=[]
    for k in range(degree//2+1):
        z=sum(comb(k,a)*341**a*5**(k-a)*raw[2*a,2*(k-a)] for a in range(k+1))
        assert z % (4**k) == 0
        qnum.append(z//(4**k))
    D=1884025
    assert qnum[1] == 2*D*comb(64,30)
    assert raw[2,0] == 4*5525*comb(64,30)
    assert raw[0,2] == 4*376805*comb(64,30)
    result={'n':64,'t':30,'complement_t':34,'total_degree':degree,
            'subset_count':comb(64,30),'Q_denominator':D,
            'Q_numerator_moment_sums':[str(x) for x in qnum],
            'raw_XY_moments':{f'{i},{j}':str(v) for (i,j),v in raw.items()},
            'small_exhaustive_validation':small}
    output=ROOT/('moments_exact.json' if degree==18 else f'moments_degree{degree}.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print('Saved',output.name,'elapsed seconds',time.time()-start,flush=True)


if __name__=='__main__':
    main()
