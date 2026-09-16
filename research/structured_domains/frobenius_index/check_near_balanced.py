#!/usr/bin/env python3
"""Finite-deletion rational rigidity: exact inequalities and complete enumeration."""
import json
import subprocess
import tempfile
from collections import Counter
from pathlib import Path


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def planted(p,n,b):
    assert (p-1)%n==0 and n%b==0 and (p-1)//n>=6
    gen=next(a for a in range(2,p) if pow(a,n,p)==1 and
             all(pow(a,d,p)!=1 for d in divisors(n) if d<n))
    domain=[pow(gen,j,p) for j in range(n)]
    B=2*b
    counts=Counter((pow(x,b,p)+pow(pow(x,b,p),-1,p))%p for x in domain)
    covered=sum(v for v in counts.values() if v==B)
    c=n-covered
    assert n>6*(B-1+c)
    assert set(counts.values())<={B,B//2}
    assert c>=B//2 and c>0
    return dict(p=p,n=n,B=B,coverage=covered,defect=c,
                fiber_size_histogram=dict(sorted(Counter(counts.values()).items())),
                B_divides_n=n%B==0,free_action_cutoff_fails=2*c>=B)


def arithmetic():
    count=0
    for B in range(2,42):
        for c in range(21):
            n=6*(B-1+c)+1
            for ell in (6,7,12,8128):
                for epsilon in (-1,1):
                    p=ell*n+epsilon
                    assert 2*ell*B<p
                    for a,b in ((1,B-1),(B-1,1),(B-1,B-1), (max(1,B//2),B-1)):
                        assert 6*a*b+3*c*(a+b)<n*max(a,b)
                        count+=1
    return count


def run():
    source=Path(__file__).with_name('check_near_balanced_pencils.cpp')
    with tempfile.TemporaryDirectory(prefix='near-balanced-') as tmp:
        exe=Path(tmp)/'check'
        subprocess.run(['clang++','-O2','-std=c++17',str(source),'-o',str(exe)],check=True)
        lines=subprocess.check_output([str(exe)],text=True).splitlines()
    rows=[json.loads(line) for line in lines]
    assert len(rows)==4
    result={'status':'PASS','arithmetic_inequalities':arithmetic(),
            'exhaustive_fixtures':rows,
            'planted_ramified_fixtures':[planted(181,15,1),planted(421,42,2),planted(449,64,2)],
            'scope':'Exact arithmetic, complete small-domain rational-pencil enumeration, and positive-defect examples. The general geometric argument is supplied by the proof, not by finite enumeration.'}
    Path(__file__).with_name('near_balanced_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':run()
