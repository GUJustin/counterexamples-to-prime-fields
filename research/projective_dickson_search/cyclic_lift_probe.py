"""Test fixed cyclotomic-domain lifts of the certified p41 supports.

A failure at one other split prime excludes the characteristic-zero
configuration with the SAME root-of-unity node labels and word formula.
It does not obstruct deforming the domain or the received word.
"""
from pathlib import Path
import json
from verify_samples import interpolate,evaluate


def primitive(p):
    return next(g for g in range(2,p) if len({pow(g,i,p) for i in range(p-1)})==p-1)


def main():
    base=Path(__file__).resolve().parent
    data=json.loads((base/'sample_verification.json').read_text())
    p=data['p'];n=data['n'];k=data['k'];g=primitive(p)
    logarithm={pow(g,i,p):i for i in range(n)}
    rows=[]
    for item in data['orbits']:
        exponents=[logarithm[x] for x in item['support']]
        probes=[]
        for q in (241,281,401):
            assert (q-1)%n==0
            z=pow(primitive(q),(q-1)//n,q)
            nodes=[pow(z,i,q) for i in exponents]
            word=[(pow(x,k,q)-1)**2*pow(2,-1,q)%q for x in nodes]
            c=interpolate(nodes[:k],word[:k],q)
            residuals=[(evaluate(c,x,q)-y)%q for x,y in zip(nodes,word)]
            probes.append(dict(prime=q,primitive_nth_root=z,residuals=residuals))
        rows.append(dict(representative=item['representative'],support_exponents=exponents,probes=probes,excluded_fixed_cyclotomic_lift=any(any(z['residuals']) for z in probes)))
    result=dict(source_prime=p,source_primitive_root=g,orbits_tested=len(rows),
                excluded_orbits=sum(r['excluded_fixed_cyclotomic_lift'] for r in rows),
                rows=rows,scope='Only the same cyclotomic nodes and word formula in characteristic zero are excluded; arbitrary deformations remain untested.')
    (base/'cyclic_lift_probe.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))


if __name__=='__main__':main()
