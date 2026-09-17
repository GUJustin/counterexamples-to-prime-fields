# A primitive characteristic-zero orbit, with shrinking surplus

Let r>=3 satisfy r=3 modulo4. On mu_(4r), put

    W(X)=(X^r-1)^2/2,
    P(X)=1+X+...+X^(r-1)=(X^r-1)/(X-1).

Then P has degree r-1 and agrees with W at exactly r+1 points.

Proof. At the r-th roots other than1, both values are zero. At1,
P(1)=r is nonzero whereas W(1)=0. At any other domain point x, write
z=x^r in {i,-1,-i}. Agreement is equivalent to

    1/(x-1)=(z-1)/2, hence x=1+2/(z-1).

For z=-1 this gives x=0, outside the domain. For z=i and z=-i it
gives x=-i and x=i, respectively. These have the required r-th powers
because r=3 modulo4. Thus there are exactly two additional matches.

The received word is invariant under X -> aX for a in mu_r. The
polynomials P(aX) form an orbit of size r, since their X coefficients
are the distinct values a. Consequently this gives an explicit list
of r polynomials, each with exactly r+1 agreements, over characteristic
zero. This is not merely a composition lift of a fixed smaller orbit.

If r is prime, every true nearest polynomial also has orbit size r.
Indeed constants have at most r agreements (the four word values are
distinct and each occurs r times), while the displayed polynomial has
r+1. A nearest polynomial is therefore nonconstant. Under the group
mu_r of prime order its orbit size is1 or r; orbit size1 would force
every nonconstant exponent below r to vanish, making it constant.
There are arbitrarily large primes r=3 modulo4, so true nearest orbits
are unbounded in this characteristic-zero cyclic model.

This establishes the growing-orbit part of the desired source, but
not the fixed-gap part. The guaranteed agreement fraction is
1/4+1/(4r); its surplus above rate shrinks to zero. No fixed positive
capacity gap, superlinear fixed-gap prime-field ordinary-CA family,
or better.codes improvement follows.

## A concrete extension tested

For a t-element subset A of mu_r let S_A be its locator and consider

    P_A,c(X)=c*(X^r-1)/S_A(X), c nonzero.

Its zero-word agreements number exactly r-t. On the other3r nodes,
agreement is equivalent to

    c=(x^r-1)*S_A(x)/2.

Thus a new surplus arises from a repeated value of this explicit
function. The t=1 construction above is the initial example. For
composite r, choosing S_A=X^t-1 can give composition lifts; these do
not by themselves supply growing orbits at fixed surplus.

`geometric_kernel_probe.py` examines t<=5 for r=11,19,23,31 over
one split prime per r. It fixes one root of S_A at1, which covers all
subsets up to the exact mu_r rotation symmetry. A modular exclusion
is valid in characteristic zero: all nodes and relevant values are
cyclotomic algebraic integers with denominator at most2, and a true
equality survives at the chosen odd split prime. Positive modular
matches would require separate exact cyclotomic verification before
claiming a characteristic-zero construction.

The completed probe found no improvement: t=1 gives r+1 in all four
cases, while every t=2,...,5 candidate has modular agreement at most r.
This excludes improvement in this restricted constant-numerator class
at these lengths, and says nothing about arbitrary residual numerators
or asymptotic t. The run completed in2.97 seconds with sampled RSS
below59MiB; the complete per-parameter counts and witnesses are saved
in `geometric_kernel_probe.json`.
