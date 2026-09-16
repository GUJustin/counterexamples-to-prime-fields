"""Exact global comparison for the one-anchor product/joint-count formula.

Old discovery rows are only a finite index. Rational inequalities certify
their exclusions, every omitted reserve tail, and complete dyadic coverage.
All product exponents are considered through their 2-adic valuation orbits.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import json
from rational_circle_bounds import ln,ln2,div,entropy,elias,raw_upper
from exact_circle_product_classes import strengthened

ROOT=Path(__file__).resolve().parent
P=2**31-1


def valuation(c,m):
    c%=m
    return m.bit_length()-1 if c==0 else (c&-c).bit_length()-1


@lru_cache(None)
def product_orbits(m,k):
    """C_k(c), indexed by v_2(c), with c=0 last."""
    assert m>=2 and m&(m-1)==0 and 0<=k<m
    ell=m.bit_length()-1
    traces=[comb(m-1,k)]+[(-1)**(k+k//(1<<j))*comb((m>>j)-1,k//(1<<j))
                              for j in range(1,ell+1)]
    result=[]
    for v in range(ell+1):
        total=traces[0]+sum((1<<(j-1))*traces[j] for j in range(1,v+1))
        if v<ell:total-=(1<<v)*traces[v+1]
        assert total%m==0 and total>=0
        result.append(total//m)
    assert sum(result[v]*(m>>(v+1)) for v in range(ell))+result[ell]==comb(m-1,k)
    if 1<=k<=m-2:
        # The proof of the 2-average ceiling is in CIRCLE_PRODUCT_DYADIC.md.
        central=comb(m//2-1,k//2)
        assert all(abs(a)<=central for a in traces[1:])
        assert (m-1)*central<=comb(m-1,k)
        assert m*max(result)<=2*comb(m-1,k)
    return tuple(result)


@lru_cache(None)
def incidence_histogram(m,h,v):
    c=0 if v==m.bit_length()-1 else 1<<v
    N=product_orbits(m,h-1)[v]
    rows=[product_orbits(m,k) for k in range(h-1)]
    histogram=defaultdict(int);histogram[N]+=1
    total=N
    for a in range(1,m):
        value=sum((-1)**j*rows[h-2-j][valuation(c-(j+1)*a,m)] for j in range(h-1))
        assert 0<=value<=N
        total+=value;histogram[value]+=1
    assert total==N*h and sum(histogram.values())==m
    return tuple(sorted(histogram.items()))


@lru_cache(None)
def candidates(m,h,d,r):
    result=[]
    for v,population in enumerate(product_orbits(m,h-1)):
        denominator=P**(2*r);N=(population+denominator-1)//denominator
        if not N:continue
        # Multiplication by an odd unit carries any product exponent to
        # the representative of its valuation orbit, preserving incidence.
        if r==0:
            hist=incidence_histogram(m,h,v)
            incidences=[N]
            for value,count in hist:
                incidences.extend([value]*(count-(value==N)))
            assert len(incidences)==m
        else:incidences=None
        values={kind:strengthened(P,m,h,d+1,N,ext,incidences)
                for kind,ext in [('CM31',2),('QM31',4)]}
        result.append(dict(product_valuation=v,product_exponent=0 if v==m.bit_length()-1 else 1<<v,
                           product_population=population,N=N,values=values,
                           incidence_histogram=hist if r==0 else None))
    return result


def excess(row,J):
    rho=F(row['d'],row['M']);eta=F(2*row['r']+3,row['M'])-F(2,row['n'])
    H=div(entropy(rho),ln2);logJ=div(ln(F(J)),ln2);logn=row['n'].bit_length()-1
    return logJ[0]-logn-H[1]/eta,logJ[1]-logn-H[0]/eta


def main():
    data=json.loads((ROOT/'circle_dyadic_discovery.json').read_text());assert data['p']==P
    # Verified existing examples give a screening floor. A floor cannot
    # exclude a challenger to the final winner, which is at least as good.
    seed_params={'CM31':(512,8,8,0),'QM31':(256,32,32,1)}
    winners={};floors={}
    for kind,key in seed_params.items():
        row=next(x for x in data['rows'] if tuple(x[k] for k in ('M','B','d','r'))==key)
        choice=max(candidates(row['M'],row['h'],row['d'],row['r']),key=lambda x:x['values'][kind]['J'])
        interval=excess(row,choice['values'][kind]['J'])
        floors[kind]=interval[0]
    groups=defaultdict(list);computed=[];exclusions=[];radius_tests=0
    for row in data['rows']:
        m,b,d,r,n,h=(row[k] for k in ('M','B','d','r','n','h'))
        groups[m,b,d].append(row)
        rho=F(d,m);eta=F(2*r+3,m)-F(2,n);H=div(entropy(rho),ln2)
        if r==row['rmin']:
            assert elias(rho,eta)[0]>0
            if r:assert elias(rho,F(2*r+1,m)-F(2,n))[1]<0
            radius_tests+=1
        u=raw_upper(m,h,r)
        # C_max <= 2*binom(m-1,h-1)/m. Thus ceil(C_max/p^(2r))
        # is at most 2^max(0,ceil(u)+1), including raw counts below one.
        power=max(0,-((-u.numerator)//u.denominator)+1)
        upper=power-(n.bit_length()-1)-H[0]/eta
        if all(upper<floors[kind] for kind in floors):
            exclusions.append(dict(M=m,B=b,d=d,r=r,raw_power_upper=power,excess_upper=str(upper)))
            continue
        options=candidates(m,h,d,r)
        record=dict(**row,product_classes=options)
        computed.append(record)
        for kind in floors:
            choice=max(options,key=lambda x:x['values'][kind]['J']);J=choice['values'][kind]['J']
            interval=excess(row,J)
            candidate=dict(M=m,B=b,n=n,d=d,r=r,h=h,K=d*b,T=h*b-2,
                           N=choice['N'],J=J,product_exponent=choice['product_exponent'],
                           excess_lower=str(interval[0]),excess_upper=str(interval[1]),
                           excess_lower_float=float(interval[0]),
                           projected_concurrency_upper=(m-d-1)//(h-d-1))
            if kind not in winners or interval[0]>F(winners[kind]['excess_lower']):winners[kind]=candidate
        print('exact candidate',m,b,d,r,'classes',len(options),flush=True)
    comparisons=0
    for row in computed:
        for kind,w in winners.items():
            for choice in row['product_classes']:
                interval=excess(row,choice['values'][kind]['J'])
                is_winner=all(row[k]==w[k] for k in ('M','B','d','r')) and choice['values'][kind]['J']==w['J']
                if not is_winner:assert interval[1]<F(w['excess_lower']),(kind,row,choice)
                comparisons+=1
    tails=empty=0
    for lm in range(2,30):
        m=1<<lm
        for ld in range(lm):
            d=1<<ld;rho=F(d,m);rmax=(m-d-4)//2
            for lb in range(1,31-lm):
                b=1<<lb;n=m*b;rows=groups.get((m,b,d))
                if not rows:
                    if rmax>=0:assert elias(rho,F(2*rmax+3,m)-F(2,n))[1]<0
                    empty+=1;continue
                assert [v['r'] for v in rows]==list(range(rows[0]['r'],rows[-1]['r']+1))
                last=rows[-1]
                if last['r']==rmax:continue
                assert m<P
                u=raw_upper(m,last['h'],last['r'])
                power=max(0,-((-u.numerator)//u.denominator)+1)
                assert all(power-lm-lb<F(w['excess_lower']) for w in winners.values())
                tails+=1
    for kind,w in winners.items():
        rho=F(w['K'],w['n']);eta=F(w['T']-w['K'],w['n'])
        assert elias(rho,eta)[0]>0
        w['Elias_margin_lower']=str(elias(rho,eta)[0])
    result=dict(status='passed',p=P,winners=winners,radius_groups=radius_tests,empty_groups=empty,
                reserve_tail_exclusions=tails,raw_excluded_rows=len(exclusions),
                computed_rows=len(computed),product_class_comparisons=comparisons,
                scope='One anchor; all dyadic M,B,d with MB<=2^30; every strict-Elias reserve; all product exponents. Full exact product classes at r=0; ceil(product population/p^(2r)) and balanced incidences at r>0. Optimizes this certified formula, not actual prefix classes or arbitrary subsets.',
                exact_rows=computed,raw_exclusions=exclusions)
    (ROOT/'circle_product_dyadic_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('exact_rows','raw_exclusions')},indent=2),flush=True)


if __name__=='__main__':main()
