#!/usr/bin/env python3
"""One exact p=13,e=8 cstar competitor; no parameter or codeword scan."""

import hashlib
import json
from pathlib import Path
import resource
import time


def main():
    started = time.monotonic()
    p, e = 13, 8
    assert all(p % d for d in range(2, 4))
    n, D, K, m = p*p, p*p-p, p*p-2*p, p+e
    L = (n-1)//m
    assert (n-1) % m == 0 and 2 <= e < p
    assert p % 5 in (2, 3) and (e-p) % 5 == 0
    rp = next(r for r in range(2, p) if r*r-r+1 >= p)

    # B=Fp[v]/(v^2-d), E=B[w]/(w^2-epsilon).
    d = next(x for x in range(2, p) if pow(x, (p-1)//2, p) == p-1)
    ba = [[((a % p+b % p) % p)+p*((a//p+b//p) % p)
           for b in range(n)] for a in range(n)]
    bm = [[((a % p)*(b % p)+d*(a//p)*(b//p)) % p
           +p*(((a % p)*(b//p)+(a//p)*(b % p)) % p)
           for b in range(n)] for a in range(n)]
    bn = [(-(a % p) % p)+p*((-(a//p)) % p) for a in range(n)]

    def bpower(a, exponent):
        value = 1
        while exponent:
            if exponent & 1:
                value = bm[value][a]
            a = bm[a][a]
            exponent >>= 1
        return value

    epsilon = next(a for a in range(1, n) if bpower(a, (n-1)//2) == p-1)
    binverse = [0]+[bpower(a, n-2) for a in range(1, n)]

    def add(a, b):
        return ba[a % n][b % n]+n*ba[a//n][b//n]

    def neg(a):
        return bn[a % n]+n*bn[a//n]

    def sub(a, b):
        return add(a, neg(b))

    def mul(a, b):
        a0, a1, b0, b1 = a % n, a//n, b % n, b//n
        return ba[bm[a0][b0]][bm[epsilon][bm[a1][b1]]]+n*ba[bm[a0][b1]][bm[a1][b0]]

    def power(a, exponent):
        value = 1
        while exponent:
            if exponent & 1:
                value = mul(value, a)
            a = mul(a, a)
            exponent >>= 1
        return value

    def inv(a):
        assert a
        a0, a1 = a % n, a//n
        denominator = ba[bm[a0][a0]][bn[bm[epsilon][bm[a1][a1]]]]
        assert denominator
        result = bm[a0][binverse[denominator]]+n*bm[bn[a1]][binverse[denominator]]
        assert mul(a, result) == 1
        return result

    def divide(a, b):
        return mul(a, inv(b))

    assert all(power(a, n) == a for a in range(n))
    beta = n
    assert power(beta, n) == neg(beta) and power(beta, n*n) == beta
    assert (n*n-1) % 5 == 0
    for root_seed in range(n, n*n):
        t = power(root_seed, (n*n-1)//5)
        if t != 1:
            break
    assert t != 1 and power(t, 5) == 1 and power(t, n) != t
    assert power(t, p**3+e) == 1
    u = inv(t)
    gamma = divide(sub(beta, power(beta, n)), sub(u, power(u, n)))
    b = sub(beta, mul(gamma, u))
    assert b < n and 0 < gamma < n
    assert add(b, divide(gamma, t)) == beta

    def trim(poly):
        while len(poly) > 1 and poly[-1] == 0:
            poly.pop()
        return poly

    def padd(a, b):
        result = a[:] + [0]*max(0, len(b)-len(a))
        for j, coefficient in enumerate(b):
            result[j] = add(result[j], coefficient)
        return trim(result)

    def pscale(a, scalar):
        return trim([mul(coefficient, scalar) for coefficient in a])

    def psub(a, b):
        return padd(a, pscale(b, p-1))

    def pmul(a, b):
        result = [0]*(len(a)+len(b)-1)
        for i, av in enumerate(a):
            if av:
                for j, bv in enumerate(b):
                    if bv:
                        result[i+j] = add(result[i+j], mul(av, bv))
        return trim(result)

    def ppower(a, exponent):
        result = [1]
        while exponent:
            if exponent & 1:
                result = pmul(result, a)
            a = pmul(a, a)
            exponent >>= 1
        return result

    def pdiv(a, b):
        remainder = trim(a[:])
        quotient = [0]*max(1, len(a)-len(b)+1)
        inverse_leading = inv(b[-1])
        while remainder != [0] and len(remainder) >= len(b):
            offset = len(remainder)-len(b)
            coefficient = mul(remainder[-1], inverse_leading)
            quotient[offset] = coefficient
            for j, value in enumerate(b):
                remainder[offset+j] = sub(remainder[offset+j], mul(coefficient, value))
            trim(remainder)
        return trim(quotient), remainder

    def pgcd(a, b):
        while b != [0]:
            _, remainder = pdiv(a, b)
            a, b = b, remainder
        return pscale(a, inv(a[-1]))

    def evaluate(poly, x):
        value = 0
        for coefficient in reversed(poly):
            value = add(mul(value, x), coefficient)
        return value

    q = [neg(b), 1]
    G = psub(ppower(q, m), [power(gamma, m)])
    F = ppower(q, e)
    A = psub(pscale(F, neg(power(b, p))), [power(gamma, m)])
    assert G[-1] == F[-1] == 1
    assert len(G)-1 == m and len(F)-1 == e and len(A)-1 <= e
    assert all(coefficient < n for poly in (G, F, A) for coefficient in poly)
    assert G == padd([0]*p+F, A)
    assert pgcd(F, G) == [1]
    assert evaluate(F, beta) != 0
    rational_value_at_beta = neg(divide(evaluate(A, beta), evaluate(F, beta)))
    assert rational_value_at_beta == power(beta, p**3)

    roots_of_unity = [x for x in range(n) if power(x, m) == 1]
    assert len(roots_of_unity) == m
    omitted_roots = sorted(add(b, divide(gamma, x)) for x in roots_of_unity)
    assert len(set(omitted_roots)) == m
    assert omitted_roots == [x for x in range(n) if evaluate(G, x) == 0]
    Lambda = [0]*(n+1)
    Lambda[1], Lambda[n] = p-1, 1
    V, remainder = pdiv(Lambda, G)
    assert remainder == [0]
    P = pmul(F, V)
    assert len(P)-1 == D and P[-1] == 1
    lambda_at_beta = sub(power(beta, n), beta)
    frobenius_scale = power(lambda_at_beta, p-1)
    cstar = power(frobenius_scale, p**3)
    assert power(cstar, p) == frobenius_scale
    assert evaluate(P, beta) == cstar
    head = [0]*D+[1]
    correction = psub(P, head)
    assert len(correction)-1 <= K
    assert pmul(P, G) == pmul(Lambda, F)
    Hnumerator = psub(head, P)
    Hnumerator[0] = add(Hnumerator[0], sub(cstar, power(beta, D)))
    H, remainder = pdiv(Hnumerator, [neg(beta), 1])
    assert remainder == [0] and len(H)-1 < K
    agreement_points = []
    for x in range(n):
        source = divide(add(sub(power(x, D), power(beta, D)), cstar), sub(x, beta))
        residual = sub(source, evaluate(H, x))
        assert residual == divide(evaluate(P, x), sub(x, beta))
        if residual == 0:
            agreement_points.append(x)
    assert len(agreement_points) == D-e
    assert set(agreement_points) == set(range(n))-set(omitted_roots)

    result = dict(
        task="single exact Mobius competitor for the Hermitian cstar endpoint",
        p=p, e=e, n=n, q=n*n, dimension=K, D=D, m=m, L=L, rp=rp,
        native_quadratic_modulus_v2_minus=d,
        extension_quadratic_modulus_w2_minus_encoded=epsilon,
        encoding="B: a+b*p; E: a+b*p^2 with a,b in B",
        beta_encoded=beta,
        fifth_root_seed_encoded=root_seed,
        fifth_root_seed_candidates=root_seed-n+1,
        t_encoded=t, b_encoded=b, gamma_encoded=gamma,
        cstar_encoded=cstar,
        frobenius_scale_encoded=frobenius_scale,
        rational_map_at_beta_encoded=rational_value_at_beta,
        G_coefficients_ascending=G,
        F_coefficients_ascending=F,
        A_coefficients_ascending=A,
        omitted_native_points=omitted_roots,
        witness_coefficients_ascending=H,
        witness_degree=len(H)-1,
        exact_witness_agreement=len(agreement_points),
        source_agreement_lower=D-e,
        source_agreement_upper_from_general_theorem=D-rp,
        tested_threshold=D-2,
        source_gap_upper=e-2,
        capacity_margin=(D-2)-K,
        source_gap_to_margin_ratio_upper=f"{e-2}/{p-2}",
        all_polynomial_and_native_residual_checks_pass=True,
        scope="one explicit construction; no parameter or codeword enumeration",
        verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        pass_all_checks=True,
    )
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
