"""Replay the selected scalar collision certificate using stored exact duals.

The preceding incidence verifier recounts the selected coordinates. This
check does not call a floating optimizer or rely on its claimed extrema.
"""
from fractions import Fraction as F
from math import comb, ceil, floor
from pathlib import Path
import json
from rational_circle_bounds import ln, ln2, entropy, div, elias
from verify_exact_support_incidences import coefficient


def main():
    source = json.loads(Path('exact_support_incidences_n82_t12_q486.json').read_text())
    check = json.loads(Path(source['separate_verification_file']).read_text())
    assert check['status'] == 'passed'
    saved = json.loads(Path('third_coefficient_collision_verification.json').read_text())
    row = next(r for r in saved['results'] if r['n'] == 82)
    n, t, q, Y, N, p, k = (row[x] for x in ('n','t','q','Y','source_words','p','k'))
    assert N == source['source_words'] == coefficient(n,t,q,Y)
    assert row['incidences'] == source['incidences']
    bounds = {}
    for certificate in row['rational_dual_certificates']:
        sign = certificate['sign']
        lam = list(map(F, certificate['multipliers']))
        bound = lam[0]*t + lam[1]*q + lam[2]*Y
        for x in range(n):
            residual = sign*comb(x,3)-lam[0]-lam[1]*x-lam[2]*comb(x,2)
            bound += min(F(0),residual)
        assert bound == F(certificate['bound'])
        bounds[sign] = bound
    low, high = ceil(bounds[1]), floor(-bounds[-1])
    assert (low,high) == (222145,276503)
    bins = min(p,high-low+1)
    def pairs(objects,classes):
        a,b = divmod(objects,classes)
        return classes*comb(a,2)+a*b
    shared = sum(comb(c,2) for c in row['incidences'])
    saving = pairs(N,bins)
    cap = (k*comb(N,2)-shared-saving)//(p-n)
    J = row['distinct_labels']
    assert J == 138752510 and pairs(N,J)<=cap<pairs(N,J-1)
    rho,eta = F(k,n),F(t-k,n)
    assert elias(rho,eta)[0]>0
    a,b,h = ln(F(J)),ln(F(n)),entropy(rho)
    excess = div((a[0]-b[1]-h[1]/eta,a[1]-b[0]-h[0]/eta),ln2)
    assert list(map(str,excess)) == row['exact_excess_bits']
    assert excess[0]>F('7.04613')
    result = dict(status='passed',n=n,k=k,t=t,source_words=N,
                  distinct_labels=J,third_moment_bounds=[low,high],
                  exact_saved_duals_replayed=True,
                  source_count_recomputed=True,excess_bits_lower=float(excess[0]))
    Path('saved_scalar_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
