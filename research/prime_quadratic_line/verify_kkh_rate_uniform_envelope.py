#!/usr/bin/env python3
"""Exact symbolic receipts for the scoped KKH canonical-bank envelope.

No asymptotic parameter scan. The proof of the infinite inequalities is in
KKH_RATE_UNIFORM_CANONICAL_ENVELOPE.md; this verifies their algebra and the
fixed exceptional cases.
"""
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import sympy as sp


def check_zero(expression):
    assert sp.cancel(expression) == 0, sp.factor(expression)


s, m, t, r = sp.symbols("s m t r")
a, rho, b, delta = sp.symbols("a rho b delta")
F = lambda aa, rr: (8 - rr) * aa**2 - 6 * rr * aa + rr * (4 * rr - 5)
H = 4*s*s*(t-2) - 3*s*t*t - 16*s - t**3 - 2*t*t
E = m*s*s - 7*m*m*s + 4*m*s - 4*m*m + m - s

check_zero(F((s-t)/s, (s-t-2)/s) + H/s**3)
check_zero(F((s-2)/s, ((s-4)*m+1)/(s*m)) + 4*E/(m*m*s**3))
check_zero(sp.diff(H, t, 2) - (-6*s-6*t-4))
check_zero(H.subs(t, 3) - (4*s*s-43*s-45))
check_zero(H.subs(t, s-3) - (5*s*s-58*s+9))
check_zero(E - (m*s*(s-7*m) + 3*s-3 + (m-1)*(4*s-4*m-3)))
check_zero(F(b, 2*b*b) - 2*b*b*(7*b+1)*(b-1))
check_zero(sp.diff(F(a, rho), rho) - (8*rho-a*a-6*a-5))
check_zero(F(rho, rho) + rho*(1-rho)*(5-rho))

# Each endpoint polynomial is increasing and positive for s >= 16.
endpoint_proofs = []
for polynomial in [4*s*s-43*s-45, 5*s*s-58*s+9]:
    shifted = sp.Poly(sp.expand(polynomial.subs(s, s+16)), s)
    assert all(coefficient > 0 for coefficient in shifted.all_coeffs())
    endpoint_proofs.append(str(shifted.as_expr()))

# The low-branch r>=6 inequality has positive coefficients after r -> r+6.
low_rank_polynomial = sp.Poly(sp.expand((5*r*r-32*r+32).subs(r, r+6)), r)
assert all(coefficient > 0 for coefficient in low_rank_polynomial.all_coeffs())
assert Fraction(173,16)**2 < 9*13  # rho_c < 3/16.

u0 = 6*b-1
check_zero(b-u0*u0*(u0+3) - (19*b-216*b**3-2))
check_zero((19*b-216*b**3-2).subs(b, 1/sp.sqrt(2*s))
           - ((19-108/s)/sp.sqrt(2*s)-2))
low_exceptions = []
for ss in (16,17):
    slack = (19*ss-108)**2 - 8*ss**3
    assert 19*ss-108 > 0 and slack > 0
    low_exceptions.append({"s":ss,"r":3,"integer_squared_slack":slack})

# s=4 is immediate; for s=8, M>=2n implies m<8, hence m=1,2,4.
assert all(comb(4,rr) < 2*4 for rr in (2,3))
assert max(comb(8,rr) for rr in range(2,8)) < 2*8*8
small_cases = []
for mm in (1,2,4):
    for rr in range(2,8):
        bank = comb(8,rr)
        if bank < 2*8*mm:
            continue
        rate = Fraction((rr-2)*mm+1,8*mm)
        agreement = Fraction(rr,8)
        if (mm,rr)==(1,2):
            assert agreement**2 == rate/2
            reason = "agreement=sqrt(rate/2)<a1(rate)"
            value = None
        else:
            assert rate >= Fraction(3,16)
            value = F(agreement,rate)
            assert value < 0
            reason = "high-branch F<0"
        small_cases.append({"s":8,"m":mm,"r":rr,"n":8*mm,
                            "bank":bank,"rate":str(rate),
                            "reason":reason,"F":None if value is None else str(value)})
assert len(small_cases)==9

# Exact curve expansion; no finite comparison relies on a truncated series.
curve = (3*rho+2*sp.sqrt(rho*(5-rho)*(2-rho)))/(8-rho)
series = sp.series(curve.subs(rho,1-delta),delta,0,3).removeO()
check_zero(series - (1-delta/2-7*delta**2/32))
check_zero((s*m-2*m)**2 - s*m*((s-4)*m) - 4*m*m)

# Cancellation of the canonical top head leaves degree-two equations.
alpha, beta, pole, sigma, tau, A, B, C = sp.symbols(
    "alpha beta pole sigma tau A B C")
quotient_equation = (sigma-alpha-beta-A)*(pole-alpha)*(pole-beta)-B*C
quotient_as_poly = sp.Poly(quotient_equation,beta)
assert quotient_as_poly.degree()==2
check_zero(quotient_as_poly.LC()-(pole-alpha))
u, v = alpha+beta, alpha*beta
direct_equation = tau-sigma*u+u*u-v-A-B*(sigma-u)
direct_as_poly = sp.Poly(direct_equation,beta)
assert direct_as_poly.degree()==2
assert direct_as_poly.LC()==1

source = Path('/Users/jthaler/Dropbox/Documents-full-2026-09-16/Documents/'
              'stwo_audit_2026-09-15/sources/actual_list_literature/kkh2026_782.txt')
source_hash = sha256(source.read_bytes()).hexdigest()
assert source_hash == 'de6e244b8e7d86c88b133a0f85bfacb76c460b4de5e38cd58c6b8f6293599d78'
receipt = {
    "status":"PASS",
    "scope":"canonical KKH full-fiber subsets; not all nearby line labels",
    "ledger":{"n":"s*m","dimension":"(r-2)*m+1","near_agreement":"r*m",
              "direction_and_common_agreement":"(r-1)*m","canonical_bank":"binomial(s,r)"},
    "conclusion_arbitrary_integer_s_ge_16":"T/n>a1(k/n) implies bank<4*n",
    "conclusion_power_of_two_s_and_m":"T/n>a1(k/n) implies bank<2*n",
    "source_path":str(source),"source_sha256":source_hash,
    "interior_factor":str(sp.factor(F((s-t)/s,(s-t-2)/s))),
    "endpoint_factor":str(sp.factor(F((s-2)/s,((s-4)*m+1)/(s*m)))),
    "high_endpoint_polynomials_after_s_plus_16":endpoint_proofs,
    "low_rank_polynomial_after_r_plus_6":str(low_rank_polynomial.as_expr()),
    "low_branch_exceptions":low_exceptions,
    "small_power_of_two_cases":small_cases,
    "near_rate_one_series_through_order_two":str(series),
    "quotient_head_equation_beta_leading_coefficient":str(quotient_as_poly.LC()),
    "direct_head_equation_beta_leading_coefficient":str(direct_as_poly.LC()),
    "cancellation_conclusion":"At most s unordered omitted pairs survive an affine top-head cancellation",
    "growing_parameter_scan":False,
}
destination = Path(__file__).with_name('kkh_rate_uniform_envelope_receipt.json')
destination.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
