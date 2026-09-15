"""Deterministic, standard-library-only end-to-end certificate verification.

Run: python3 verify_publication.py
Recomputes every moment; reads but does not modify proof artifacts.
"""
import json
from pathlib import Path
from math import comb
from moments import exact_moments,validate_small
from verify import certify
from crosscheck_saved_certificate import crosscheck
from verify_factored import certify_factored

ROOT=Path(__file__).resolve().parent


def main():
    data=json.loads((ROOT/'moments_degree50.json').read_text())
    saved=json.loads((ROOT/'certificate_degree12.json').read_text())
    assert (data['n'],data['t'],data['complement_t'],data['total_degree'])==(64,30,34,50)
    assert data['Q_denominator']==1884025
    assert data['subset_count']==comb(64,30)
    small=validate_small()
    assert small==data['small_exhaustive_validation']
    raw=exact_moments(64,30,50)
    assert {f'{i},{j}':str(v) for (i,j),v in raw.items()}==data['raw_XY_moments']
    aggregate=[]
    for k in range(26):
        total=sum(comb(k,a)*341**a*5**(k-a)*raw[2*a,2*(k-a)] for a in range(k+1))
        assert total % 4**k==0
        aggregate.append(total//4**k)
    assert list(map(str,aggregate))==data['Q_numerator_moment_sums']
    assert raw[0,0]==comb(64,30)
    assert raw[2,0]==4*5525*comb(64,30)
    assert raw[0,2]==4*376805*comb(64,30)
    assert aggregate[1]==2*1884025*comb(64,30)
    computed=certify(data,saved)
    assert computed==saved
    independent=crosscheck(data,saved)
    assert saved['certified_class_lower_bound']==5133798314667
    factored=json.loads((ROOT/'certificate_factored.json').read_text())
    assert certify_factored(data)==factored
    assert factored['certified_class_lower_bound']==saved['certified_class_lower_bound']
    report={'verified':True,'n':64,'t':34,
            'recomputed_mixed_moments':len(raw),
            'recomputed_radial_moments':len(aggregate),
            'small_exhaustive_moment_checks':small['exact_moment_checks'],
            'certified_class_lower_bound':saved['certified_class_lower_bound'],
            'factored_alternative_verified':True,
            **independent}
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=='__main__': main()
