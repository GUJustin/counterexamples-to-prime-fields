# Independent audit of the four-word one-pole extension

**PASS.** The explicit witness, finite search completeness, and the resulting
five-word (n=28, degree<=6, agreement>=14) bank are correct. This is a genuine
positive finite construction, not a repeatable induction or an unbounded bank.

## Independent exact arithmetic

`independent_witness.py` uses only Python Fraction arithmetic in the basis
1,q,q^2,q^3 modulo q^4-q^2+1. It does not use the original Sympy algebraic-number
implementation. The displayed constants convert to

    a=(3-6q+9q^2+8q^3)/13,
    c=(8-3q+11q^2-9q^3)/13,

using i=q^3 and sqrt(3)=2q-q^3. The independent check confirms q is primitive
of order12, all twelve seed pair incidences, exactly six matches per old word,
and the translated zero set {0,1,2,6,7,8}. It verifies the exact polynomial
identities cV(x)=(x-a)w0(x) precisely at indices0,1,2,3,4,5, and nowhere else.
It also verifies c!=0, V(a)!=0, a outside mu12, a!=0, a!=4, and a^12!=1.
The bounded run completed in0.57seconds with peak RSS14704KiB under the
384MiB/60second guard. Results and resource receipt are saved alongside it.

## The exhaustive reduction is valid over extension fields

A proper degree-at-most-three numerator over X-a differs from every old
quadratic by a nonzero degree-at-most-three numerator. Thus it has at most
three intersections with each old word. Every new agreement with the received
word gives two such intersections, since exactly two old candidates match
at each node. Six agreements exhaust the total four-times-three budget;
there can be no seventh, and every old candidate has exactly three of those
intersections.

Subtract the designated old quadratic. The translated numerator has exactly
three roots among its six zero coordinates, and degree exactly three, so it
is c times their monic locator. Its other three agreement coordinates lie
among the six nonzero received values. Any two determine the affine function
(X-a)/c uniquely. Its slope is nonzero for an actual proper candidate. Thus
all candidates arise in the20 times15 cases, even if initially allowed over
an arbitrary extension field. Interpolation recovers a and c in Q(q).

The saved original result reports300 cases,152 proper candidates counted with
repetition, and histogram116 five-match /36 six-match cases. Its twelve distinct
hits have twelve distinct poles. The source's deduplication key is valid: a
proper rational function determines its pole, monic cubic zero locator, and
scale uniquely. The independent run above verifies the first witness rather
than repeating the full300-case census; the exhaustive reduction itself has
been independently audited.

## Lift and prime-field scope

The24 preimages of mu12 under T^2 are mu24. Since a!=0 and a is outside mu12,
its two square roots are distinct and outside mu24. The added points0,2 are
distinct from both fibers:4 is neither in mu12 nor equal to a. Thus the domain
has exactly28 points over the indicated number field.

The four old lifted polynomials (T^2-a)H_u(T^2) have degree at most6 and
are distinct. N(T^2) has degree at most6 and differs from all four because
otherwise N=(X-a)H_u, contrary to properness. Each old candidate receives
12 inherited matches plus two pole-fiber matches; the new one receives
12 inherited matches plus the two individually assigned added coordinates.
Hence all five have at least14 agreements. The code dimension is7, exactly
one quarter of28. No claim of a true nearest-codeword certificate is needed
or established here.

Take the normal closure of a number field containing all coefficients and
coordinates. Infinitely many primes split completely in that normal closure;
after excluding finitely many denominator and nonzero-guard primes, reduction
preserves all five words, domain distinctness, degree caps, and displayed
agreements in the prime field. This justifies arbitrarily large prime-field
realizations of this FIXED bank. It does not imply an unbounded family or
characteristic-zero lifting of the native full-length Dickson construction.
