"""Independent ascending-label, complementary-subset distribution recurrence."""
from collections import Counter
import csv
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path
import subprocess
import tempfile
import time
import numpy as np

ROOT=Path(__file__).resolve().parent

def histogram(n,t,q):
    rows={(0,0):(0,np.array([1],dtype=np.uint64))}
    peak_cells=1
    for a in range(n):
        nxt={}
        for (size,total),(low,counts) in rows.items():
            for take in (0,1):
                s=size+take; z=total+take*a; need=t-s
                if not 0<=need<=n-a-1: continue
                minimum=need*(2*(a+1)+need-1)//2
                maximum=need*(2*n-need-1)//2
                if not z+minimum<=q<=z+maximum: continue
                lo=low+take*comb(a,2); key=(s,z)
                if key not in nxt:
                    nxt[key]=(lo,counts.copy()); continue
                oldlo,old=nxt[key]
                newlo=min(lo,oldlo); newhi=max(lo+len(counts),oldlo+len(old))
                new=np.zeros(newhi-newlo,dtype=np.uint64)
                new[oldlo-newlo:oldlo-newlo+len(old)]=old
                new[lo-newlo:lo-newlo+len(counts)]+=counts
                nxt[key]=(newlo,new)
        rows=nxt
        peak_cells=max(peak_cells,sum(len(v[1]) for v in rows.values()))
    if (t,q) not in rows: return {},peak_cells
    lo,counts=rows[t,q]
    return {lo+j:int(v) for j,v in enumerate(counts) if v},peak_cells

def read(path):
    with open(path) as f:
        return {int(r['y']):int(r['count']) for r in csv.DictReader(f)}

def main():
    started=time.perf_counter()
    # All intermediate counts are <= binom(64,32), below uint64 maximum.
    assert comb(64,32)<2**64
    small=0
    with tempfile.TemporaryDirectory() as tmp:
        output=Path(tmp)/'hist.csv'
        for n in range(3,10):
            for t in range(1,n):
                expected={}
                for subset in combinations(range(n),t):
                    expected.setdefault(sum(subset),Counter())[sum(comb(a,2) for a in subset)]+=1
                for q,h in expected.items():
                    actual,_=histogram(n,t,q)
                    assert actual==h
                    subprocess.run([str(ROOT/'exact_distribution'),str(n),str(t),str(q),str(output)],
                                   check=True,stderr=subprocess.DEVNULL)
                    assert read(output)==h
                    small+=1
    original=read(ROOT/'exact_distribution.csv')
    complement,peak=histogram(64,30,945)
    reflected={comb(64,3)-y:c for y,c in complement.items()}
    assert reflected==original
    moments=json.loads((ROOT/'moments128.json').read_text())
    assert all(sum(c*(y-moments['center'])**j for y,c in original.items())==value
               for j,value in enumerate(moments['centered_moments']))
    maximum=max(original.values())
    result=dict(status='passed',small_exhaustive_classes=small,
                independent_recurrence='ascending labels, complementary 30-subsets',
                moments_matched=129,n=64,t=34,q=1071,maximum=maximum,
                maximizing_y=[y for y,c in original.items() if c==maximum],
                total=sum(original.values()),nonempty_fibers=len(original),
                support_min=min(original),support_max=max(original),
                verifier_peak_live_cells=peak,seconds=time.perf_counter()-started,
                distribution_sha256=sha256((ROOT/'exact_distribution.csv').read_bytes()).hexdigest())
    (ROOT/'exact_distribution_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__': main()
