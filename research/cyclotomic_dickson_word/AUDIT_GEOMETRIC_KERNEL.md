# Independent audit of the geometric kernel family

September 17, 2026. GEOMETRIC_KERNEL_FAMILY.md and the probe source and
saved JSON were independently inspected. The mathematical claims and
the stated modular-exclusion interpretation are sound.

For P=(X^r-1)/(X-1), the r-1 nonidentity r-th roots are zero agreements.
The removable value at 1 is r, hence is not an agreement in characteristic
zero. Off those roots, cancellation reduces agreement to
x=1+2/(z-1), z=x^r in {i,-1,-i}. The three possibilities are -i, 0, i,
respectively. Exactly the two nonzero possibilities lie in the required
fibers when r=3 mod4, proving exactly r+1 agreements. The linear
coefficient of P(aX) is a, so the selected orbit has size r.

The true-nearest argument for prime r is valid. The four word values
0,2,-i,i are distinct, each on r nodes. Thus constants have at most r
matches and cannot be nearest. A degree-<r polynomial fixed by mu_r is
constant; prime-order orbit-stabilizer therefore gives orbit size r for
every nearest polynomial. The nearest maximum need not equal r+1;
only its lower bound is used. This establishes unbounded true nearest
orbits, not a uniform positive normalized margin.

For general deleted-root supports A of size t, the polynomial has
exactly r-t zero-word matches. At a deleted root a its removable value
is c*r*a^(r-1)/product_(b in A,b!=a)(a-b), which is nonzero in
characteristic zero and in the probe primes. Off mu_r, matching is
exactly c=(x^r-1)*S_A(x)/2. Thus histogram multiplicity is the exact
maximum number of additional matches for that support.

Rotation normalization is complete. Every nonempty A can be rotated
to contain 1. Under x=a*y with a in mu_r, S_A(a*y)=a^t*S_(a^-1 A)(y),
so the scalar c changes by a nonzero factor a^-t; all c remain allowed.
Enumerating every (t-1)-subset of the other r-1 roots therefore covers
all candidates, with harmless redundant orbit representatives.

The split-prime exclusion is rigorous. Cyclotomic node differences
remain nonzero because the chosen root retains exact order 4r. For any
characteristic-zero improvement there is at least one off-zero match,
so c is one of the displayed cyclotomic values, with denominator at
most 2. It reduces to a nonzero scalar because every factor remains
nonzero. All additional characteristic-zero equalities survive
reduction. Thus modular maxima are upper bounds for characteristic-zero
maxima in this restricted class. Modular positive constructions alone
would not certify a characteristic-zero lift.

A lightweight independent replay verified every one of the 20 saved
rows: primality and exact root order, anchored-support count binom(r-1,t-1),
and the saved witness polynomial evaluated directly on ALL 4r nodes,
including removable values at deleted roots. All stated witness counts
and the bounds r+1 for t=1 and at most r for t=2,...,5 pass. The complete
search coverage follows from the inspected combinations loop and
rotation argument; this audit did not rerun the full census. No claim
is made about other residual numerators, other lengths, or growing t.
