# Elliptic coset complements: parameter window, not a construction

Let ell be an odd prime and suppose an elliptic curve over F_p has full rational
ell-torsion, with p different from ell and 2. Its nonzero torsion x-coordinates
form a domain of size n=(ell^2-1)/2. The proposed dimension is
k=n-4ell+1. This note checks only the numerical target. No received line,
source farness, or exceptional parameter bank is established here.

For a cyclic subgroup H of order ell, a nonzero coset together with its negative
has ell distinct x-coordinates. There are (ell-1)/2 such pairs of cosets.
Choosing two distinct pairs gives an omitted set of size 2ell. Counting these
choices over the ell+1 subgroups gives

    (ell+1)(ell-1)(ell-3)/8 = Theta(ell^3).

For ell>=5 these are distinct supports: lift each x-support to its four cosets
in E[ell]. Cosets of different cyclic subgroups intersect in exactly one
point, so two such lifted unions intersect in at most 16 points, whereas
each union has 4ell>16 points. Within one subgroup the chosen coset pairs
are also recoverable from their union. This counts distinct supports, not
distinct challenge parameters. A shared received line and distinct line labels
are separate requirements. In particular this is not a counterexample count.

## The unslacked target is above Johnson

T0=n-2ell satisfies T0^2-n(k-1)=4ell^2>0. Thus agreement on the
retained complement by itself does not give the desired below-Johnson test.
For T=n-2ell-d,

    n(k-1)-T^2=(d-4)ell^2-4d ell-d^2-d.

The smallest fixed integer d allowing this expression to be positive for
arbitrarily large ell is 5. At d=5 the expression is ell^2-20ell-30,
positive for ell>=23. One may test an existing stronger agreement bank at
this weaker threshold: five extra omitted roots are NOT necessary just to
lower the threshold. They may expand the possible bank, but change the
algebraic construction problem and must be handled explicitly.

## The corrected threshold is above the full first-order curve

Set d=5 and ell>=23. Then 0<k<T<n and rho=k/n>1/2, so the high-rate
branch of the first-order curve applies. With a=T/n, this curve is the positive
root of F(a,rho)=(8-rho)a^2-6rho a+rho(4rho-5). Direct expansion gives

    n^3 F(T/n,k/n)
      =(6ell^4-4ell^3+387ell^2+196ell-291)/2 > 0.

Positivity follows already for ell>=1 by grouping the first two terms as
2ell^3(3ell-2), and the remaining terms as
387(ell^2-1)+196(ell-1)+292. Hence

    n a_1(k/n) < n-2ell-5 < sqrt(n(k-1)).

At ell=23: n=264, k=173, T=213, squared Johnson slack=39,
and the indexed two-coset choice count is 1320. These are target parameters,
not a finite counterexample.

## What a successful construction would still need

A common line with superlinear many distinct labels and agreement at least T;
a bound A<T on both endpoint agreements and on common agreement; and the
claimed list profile, if needed. The threshold alone proves none of these.
For example a hypothetical A=n-3ell would yield
(T-A)/(T-k)=(ell-5)/(2ell-6), tending to 1/2, but no such A bound is known.
Even that hypothetical family has rate tending to one and normalized loss
Theta(1/ell), rather than a fixed fractional loss at a prescribed rate.

`verify_parameter_window.py` checks the identities symbolically and the first
usable fixture with exact rational arithmetic. No elliptic construction is
claimed by its PASS receipt.
