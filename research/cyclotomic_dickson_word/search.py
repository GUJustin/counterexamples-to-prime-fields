"""Exact above-capacity support test for W=(X^k-1)^2/2 on mu_(4k).

For k+1 distinct nodes, a degree<k interpolant exists exactly when
the complete homogeneous symmetric polynomial h_k on those nodes is 2.
A split-prime filter safely discards nonzero characteristic-zero values;
all survivors are checked modulo the integer cyclotomic polynomial.
"""
from pathlib import Path
from itertools import combinations,islice
from math import comb
import argparse,json,time
import numpy as np
import sympy as s


def exact_test(exponents,n,k,cyclo):
    h=[[0]*n for _ in range(k+1)];h[0][0]=1
    for e in exponents:
        for j in range(1,k+1):
            prev=h[j-1]
            h[j]=[h[j][i]+prev[(i-e)%n] for i in range(n)]
    out=h[k];out[0]-=2
    degree=len(cyclo)-1
    for j in range(n-1,degree-1,-1):
        q=out[j]
        if q:
            for i,c in enumerate(cyclo):out[j-degree+i]-=q*c
    return out[:degree]


def scan(k,batch):
    start=time.monotonic();n=4*k
    q=((1000000+n-1)//n)*n+1
    while not s.isprime(q):q+=n
    generator=int(s.primitive_root(q));z=pow(generator,(q-1)//n,q)
    assert len({pow(z,i,q) for i in range(n)})==n
    roots=np.array([pow(z,i,q) for i in range(n)],dtype=np.int64)
    X=s.symbols('X');cyclo=list(reversed([int(c) for c in s.Poly(s.cyclotomic_poly(n,X),X).all_coeffs()]))
    total=0;survivors=[];exact=[]
    stream=combinations(range(n),k+1)
    while True:
        items=list(islice(stream,batch))
        if not items:break
        ind=np.array(items,dtype=np.int64);values=roots[ind]
        h=np.zeros((len(items),k+1),dtype=np.int64);h[:,0]=1
        for t in range(k+1):
            for j in range(1,k+1):h[:,j]=(h[:,j]+values[:,t]*h[:,j-1])%q
        for row in np.flatnonzero(h[:,k]==2):
            exponents=items[int(row)];remainder=exact_test(exponents,n,k,cyclo)
            survivors.append(dict(exponents=exponents,remainder=remainder))
            if not any(remainder):exact.append(exponents)
        total+=len(items)
    assert total==comb(n,k+1)
    return dict(n=n,k=k,split_prime=q,primitive_nth_root=z,
                supports_checked=total,modular_survivors=len(survivors),
                exact_above_capacity_supports=len(exact),exact_supports=exact,
                survivor_certificates=survivors,cyclotomic_coefficients=cyclo,
                seconds=time.monotonic()-start)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--dimensions',nargs='+',type=int,default=list(range(1,8)))
    ap.add_argument('--batch',type=int,default=8192)
    ap.add_argument('--output',default='research/cyclotomic_dickson_word/search.json')
    args=ap.parse_args();out={'scope':'Finite exact characteristic-zero support census for one cyclic word. No general growing-length conclusion.','fixtures':[]}
    for k in args.dimensions:
        row=scan(k,args.batch);out['fixtures'].append(row)
        Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({a:b for a,b in row.items() if a not in ('exact_supports','survivor_certificates','cyclotomic_coefficients')}),flush=True)


if __name__=='__main__':main()
