#!/usr/bin/env python3
"""Exact rational regressions for growing Gram degree beyond sqrt(n).

No floating point, third-party libraries, or protocol-specific calculations.
Logarithms are enclosed by a positive Taylor sum and a geometric tail.
"""
from fractions import Fraction
from math import comb, factorial, isqrt
from pathlib import Path
import json


def decimal_enclosure(lower, upper, places=8):
    scale = 10**places
    a = lower.numerator*scale//lower.denominator
    b = -(-upper.numerator*scale//upper.denominator)
    def show(v):
        return f"{v//scale}.{v%scale:0{places}d}"
    return {"lower": show(a), "upper": show(b)}


def log_correction(n, m, power, half=False, terms=16):
    """Enclose sum_i (m+1-i)*[-log(1-(i/n)^power)].

    For 0<=x<=r<1, after K terms the tail lies between zero and
    x^(K+1)/((K+1)*(1-r)). Aggregate the power sums exactly first.
    """
    factor = Fraction(1, 2) if half else Fraction(1)
    r = Fraction(m, n)**power
    sums = [sum((m+1-i)*i**(power*k) for i in range(1,m+1))
            for k in range(1,terms+2)]
    lower = factor*sum((Fraction(sums[k-1],k*n**(power*k))
                        for k in range(1,terms+1)), Fraction())
    upper = lower+factor*Fraction(sums[-1],
                (terms+1)*n**(power*(terms+1)))/(1-r)
    first_order = factor*Fraction(sums[0],n**power)
    envelope = first_order/(1-r)
    assert first_order < lower <= upper <= envelope
    if power == 2:
        assert sums[0] == m*(m+1)**2*(m+2)//12
        assert envelope == Fraction(m*(m+1)**2*(m+2),
                                     24*n*n)/(1-r)
    else:
        assert sums[0] == m*(m+1)*(m+2)//6
        assert envelope == Fraction(m*(m+1)*(m+2),6*n)/(1-r)
    return lower, upper, envelope


def independent_norm(n, j):
    # Classical exact norm in its convolution/binomial form.
    return Fraction(factorial(j)**2*comb(n+j,2*j+1),
                    n*factorial(2*j))


fixtures = []
recurrence_steps = norm_checks = variance_checks = 0
for n, m in [(512,64), (4096,256), (32768,1024),
             (262144,4096), (1024,240)]:
    assert m*m > n
    assert 17*m*m <= n*n+4
    samples = {1,2,isqrt(n),m//2,m}
    sigma = Fraction(n*n-1,12)
    first_sigma = sigma
    minimum_ratio = None
    for j in range(1,m+1):
        if j > 1:
            ratio = Fraction(n*n-j*j,4*(2*j-1)*(2*j+1))
            assert ratio >= 1
            minimum_ratio = ratio if minimum_ratio is None else min(minimum_ratio,ratio)
            sigma *= ratio
            recurrence_steps += 1
        assert sigma >= first_sigma
        if j in samples:
            assert sigma == independent_norm(n,j)
            norm_checks += 1
            for t in [n//4,n//2,3*n//4]:
                assert 1 <= m < t < n
                v = Fraction(t*(n-t),n-1)*sigma
                v1 = Fraction(t*(n-t)*(n+1),12)
                assert v >= v1
                # The published smoothed-variance bound follows after
                # summing these pointwise rational upper bounds.
                assert Fraction(1,24)/v <= Fraction(1,24)/v1
                z = (m+2)*v
                h = isqrt(z.numerator//z.denominator)
                if h*h < z:
                    h += 1
                assert (h-1)**2 < z <= h*h
                # Exact rounding enclosure, before taking logarithms.
                assert 4*z <= (2*h+1)**2
                assert (2*h-2)**2 < 4*z
                variance_checks += 1
    gl, gu, ge = log_correction(n,m,2,half=True)
    rl, ru, re = log_correction(n,m,1)
    fixtures.append({
        "n": n, "m": m, "m_squared_over_n": str(Fraction(m*m,n)),
        "m_over_n": str(Fraction(m,n)),
        "fixture_type": "m=n^(2/3)" if m**3==n*n else "near_monotonicity_threshold",
        "minimum_variance_ratio": str(minimum_ratio),
        "gram_grid_loss_natural_log": decimal_enclosure(gl,gu),
        "gram_grid_loss_over_m_squared": decimal_enclosure(gl/(m*m),gu/(m*m)),
        "gram_grid_envelope": decimal_enclosure(ge,ge),
        "range_grid_loss_natural_log": decimal_enclosure(rl,ru),
        "range_grid_loss_over_m_squared": decimal_enclosure(rl/(m*m),ru/(m*m)),
        "range_grid_envelope": decimal_enclosure(re,re),
    })

# Boundary control: monotonicity really can fail just outside the
# sufficient threshold; do not silently omit its hypothesis.
assert 17*25**2 > 100**2+4
assert Fraction(100**2-25**2,4*(2*25-1)*(2*25+1)) < 1

result = {
    "status": "all exact assertions passed",
    "arithmetic": "integers and rational numbers only",
    "log_enclosures": "16-term positive Taylor sums with rational geometric tails",
    "recurrence_steps": recurrence_steps,
    "independent_norm_checks": norm_checks,
    "density_and_rounding_checks": variance_checks,
    "outside_threshold_negative_control": "passed",
    "fixtures": fixtures,
    "limits": "Finite regressions verify these fixtures and formulas, not asymptotic convergence or uniformity. The analytic proof remains necessary.",
}
destination = Path(__file__).with_name("wide_regime_verified.json")
destination.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
