"""Check every forced evaluation pattern for the all-prime boundary family."""
import importlib.util
import itertools
import json
from pathlib import Path
BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('riccati',BASE.parent/'verify.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)

def main():
    rows=[]
    for p in (2,3,5,7,11,13):
        a=[0]*(p+1);a[1]=p-1;a[p]=1
        equation=(a,[0],[p-1],[p-1])
        indicators=[]
        for r in range(p):
            q,rem=h.divide(a,[-r%p,1],p)
            assert rem==[0]
            assert [h.evaluate(q,x,p) for x in range(p)]==[p-1 if x==r else 0 for x in range(p)]
            indicators.append(q)
        solutions=[]
        for bits in itertools.product((0,1),repeat=p):
            P=[0]
            f=[1]
            for r,b in enumerate(bits):
                if b:
                    P=h.add(P,indicators[r],p)
                    f=h.mul(f,[-r%p,1],p)
            actual=h.residual(P,equation,p)==[0]
            assert actual==(h.derivative(h.derivative(f,p),p)==[0])
            assert actual==(sum(bits) in (0,1,p))
            if actual:solutions.append(P)
        assert len(solutions)==p+2
        assert len({tuple(P) for P in solutions})==p+2
        rows.append(dict(p=p,D=p-1,patterns_checked=2**p,exact_solution_count=len(solutions)))
    result=dict(status='PASS',fixtures=rows,scope='All necessary prime-field evaluation patterns; the proof also excludes extra solutions over extension fields.')
    (BASE/'family_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
