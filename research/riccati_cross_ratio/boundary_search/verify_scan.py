"""Independently enumerate the maximizing witnesses from the C++ scan."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('riccati',BASE.parent/'verify.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)

def main():
    rows=[]
    for p in (3,5):
        record=json.loads((BASE/f'p{p}_verification.json').read_text())
        D=record['D'];q=p**(D+1)
        assert record['complete'] and record['p']==p and D==p-1
        assert record['monic_centers']==(q-1)//(p-1)
        assert record['pairs_examined']==record['monic_centers']*(q-2)
        witness=record['witness']
        assert witness[0]==[0] and len(witness)==record['maximum_solutions']==p+2
        eq=h.equation_from_pencil(witness[1],witness[2],[1],[0],p)
        found={tuple(h.trim(c)) for c in itertools.product(range(p),repeat=D+1)
               if h.residual(h.trim(c),eq,p)==[0]}
        assert found=={tuple(c) for c in witness}
        rows.append(dict(p=p,D=D,polynomials_enumerated=q,solutions=len(found),
                         scan_pairs=record['pairs_examined']))
    output=dict(status='PASS',fixtures=rows,
                scan_source_sha256=hashlib.sha256((BASE/'scan.cpp').read_bytes()).hexdigest(),
                scope='Checks full solution sets of the displayed maximizing equations and the scan coverage counters. Exhaustiveness over equations additionally relies on scan.cpp and the normalization argument in PROOF.md; no arbitrary-prime upper bound is inferred.')
    (BASE/'independent_verification.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
