#!/usr/bin/env python3
"""Check Taylor numerators and actual curve examples; not a geometry proof."""
import json
import math
import random
from pathlib import Path
import sympy as s
from arithmetic import add, mul, scale, deriv, trim

X, z, u, v = s.symbols("X z u v")
gens = (X, z, u, v)


def degrees(poly):
    terms = s.Poly(poly, *gens).terms()
    return (max((m[2]+m[3] for m, c in terms if c), default=0),
            max((m[1] for m, c in terms if c), default=0))


def ev(poly, vals, p):
    total = 0
    for powers, coeff in s.Poly(poly, *gens).terms():
        term = int(coeff) % p
        for a, e in zip(vals, powers):
            term = term*pow(a, e, p) % p
        total = (total+term) % p
    return total


def pow_poly(a, e, p):
    ans = [1]
    for _ in range(e):
        ans = mul(ans, a, p)
    return ans


def substitute(Q, t, zz, P, p):
    Pd = deriv(P, p)
    ans = [0]
    for (a, b, c, d), coeff in s.Poly(Q, *gens).terms():
        term = mul(mul(pow_poly([t, 1], a, p), pow_poly(P, c, p), p),
                   pow_poly(Pd, d, p), p)
        ans = add(ans, scale(term, int(coeff)*pow(zz, b, p), p), p)
    return ans


def run():
    rng = random.Random(2026091602)
    specs = [
        (v-u*u-z*X, 2, 1, 6),
        (v*v+u*v+z*u*u+X*u-z*X*X, 2, 1, 4),
        (z*v*v+(X+z)*u*v+u*u+v+z*X, 2, 1, 4),
        ((1+z*X)*v+(X*X+z)*u+z*z*X**3, 1, 2, 6),
        (v**3+z*u*u*v+X*u+z, 3, 1, 4),
    ]
    records = []
    finite_tests = 0
    for Q, B, H, Dmax in specs:
        S = s.diff(Q, v)
        T = s.diff(Q, X)+v*s.diff(Q, u)
        Ns = {0: u, 1: v, 2: -T}
        exps = {0: 0, 1: 0, 2: 1}
        for j in range(2, Dmax):
            N, e = Ns[j], exps[j]
            Ns[j+1] = s.expand(S*S*(s.diff(N, X)+v*s.diff(N, u))
                              -T*S*s.diff(N, v)
                              -e*N*(S*(s.diff(S, X)+v*s.diff(S, u))
                                    -T*s.diff(S, v)))
            exps[j+1] = e+2
        bounds = []
        for j in range(2, Dmax+1):
            jet, chal = degrees(Ns[j])
            assert jet <= 1+(2*j-3)*(B-1)
            assert chal <= (2*j-3)*H
            bounds.append({"derivative": j, "jet_degree": jet,
                           "challenge_degree": chal,
                           "denominator_exponent": exps[j]})
        for D in range(1, Dmax+1):
            tau = max(0, 2*D-3)
            common = {j: s.expand(Ns[j]*S**(tau-exps[j]))
                      for j in range(D+1)}
            for N in common.values():
                jet, chal = degrees(N)
                assert jet <= 1+tau*(B-1) and chal <= tau*H
            for p in (101, 1009):
                completed = 0
                while completed < 12:
                    vals = [rng.randrange(p) for _ in gens]
                    ss = ev(S, vals, p)
                    if not ss:
                        continue
                    t, zz, uu, vv = vals
                    P = [ev(common[j], vals, p)*pow(ss, -tau, p)
                         *pow(math.factorial(j), -1, p) % p
                         for j in range(D+1)]
                    assert P[0] == uu and P[1] == vv
                    out = substitute(Q, t, zz, P, p)
                    assert out[0] == ev(Q, vals, p)
                    assert all((out[i] if i < len(out) else 0) == 0
                               for i in range(1, D))
                    finite_tests += 1
                    completed += 1
        records.append({"Q": str(Q), "B": B, "H": H,
                        "max_degree": Dmax, "numerator_degrees": bounds})
    curves = []
    for D in range(1, 41):
        p = 1009
        for zz in (1, 2, 3, 11):
            P = [0]*(D+1)
            for j in range(D+1):
                P[D-j] = (-1)**j*math.factorial(D)//math.factorial(D-j)
                P[D-j] = P[D-j]*pow(zz, -j-1, p) % p
            assert add(deriv(P, p), scale(P, zz, p), p) == [0]*D+[1]
        # A generic hyperplane section becomes degree D+2 after clearing
        # the common denominator; its constant term is nonzero. Check that
        # a concrete section is also reduced (squarefree).
        for _ in range(100):
            t, lam, c = [rng.randrange(1, p) for _ in range(3)]
            coeffs = [0]*(D+3)
            coeffs[D+2], coeffs[D+1] = lam, -c % p
            for j in range(D+1):
                coeffs[D-j] = ((-1)**j*math.factorial(D)//math.factorial(D-j)
                               *pow(t, D-j, p)) % p
            poly = s.Poly.from_list(list(reversed(coeffs)), z, modulus=p)
            if s.gcd(poly, poly.diff()).degree() == 0:
                break
        else:
            raise AssertionError("failed to find reduced generic section")
        assert poly.degree() == D+2 and coeffs[0] != 0
        tau = max(0, 2*D-3)
        theoretical_bound = 2*(tau+2)
        assert D+2 <= theoretical_bound
        curves.append({"D": D, "degree": D+2, "bound": theoretical_bound,
                       "p": p, "section": {"t": t, "lambda": lam, "c": c}})
    result = {"status": "PASS", "equations": len(specs),
              "finite_taylor_tests": finite_tests, "curve_examples": len(curves),
              "scope": "Taylor recurrence and example checks; not a proof of generic geometry",
              "records": records, "curves": curves}
    Path(__file__).with_name("first_order_reconstruction_verification.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("records", "curves")}, indent=2))


if __name__ == "__main__":
    run()
