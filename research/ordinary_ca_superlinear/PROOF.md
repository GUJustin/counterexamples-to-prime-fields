# Quadratically many ordinary-CA failures over quadratic extensions

September 17, 2026. This strengthens the earlier n^(5/4-epsilon) result
and removes its quantitative sieve input. No novelty claim. The argument
uses Dirichlet's theorem, the checked eight-point certificate, orbit
descent, and boundary padding. The old valid argument is preserved in
SIEVE_VARIANT.md. This is NOT a prime-ambient-field theorem.

## Statement

For unbounded lengths n there are primes p and RS codes over F_(p^2),
of exact rate3/13, with a received affine line having at least ceil(n^2/4096)
nearby labels at an agreement threshold T, but NO ordinary correlated
agreement of size T. The capacity gap T/n-3/13 is greater than3/26.
The radius is strictly below the characteristic-p Elias radius for all
sufficiently large members. The characteristic satisfies p>K-1.

The gap is bounded below, NOT fixed exactly. The characteristic need not
be proportional to output length. No first-order-regime or better.codes
claim follows. This excludes linear ordinary-CA bounds uniform over gaps
bounded below in the large-characteristic field class.

## 1. Arbitrarily large nearest-polynomial orbits

Fix R>=40. Let B_R be the product of odd primes <=R. The CRT class
p=9 mod16, p=-1 mod B_R is coprime to16 B_R, so Dirichlet supplies
arbitrarily large primes in it. Set k=(p-1)/4. Then v_2(k)=1, k=1 mod3,
and no odd prime <=R divides k.

Use W_k(X)=(1+X^(2k))/2-X^k on F_p^*. Its maximum agreement M with
degree-<k polynomials is at least3k/2 by the full Dickson construction,
and at most2k by degree. Multiplication by H=mu_k preserves this word.
Take one nearest polynomial and let r be the size of its H-orbit.
The integer r divides k. If r<=R, it must be1 or2, forcing the polynomial
to have form a+b X^(k/2). On Y=X^(k/2), each of the8 fibers has sizek/2.
The exact eight-point determinant certificate shows that no affine
polynomial agrees at three points with (1+Y^4)/2-Y^2 for p>17.
Thus such a polynomial agrees at most k times, a contradiction.
Consequently r>R and r is not divisible by3.

The certificate is ../dickson_fixed_gap/verify_two_orbit.py. Its56
nonzero integral determinants have norms with prime factors only
2,3,5,7,17; it was independently replayed for the present deduction.

## 2. Descent makes the nearest list linear in its own domain length

Put d=k/r. The stabilizer of the selected polynomial is mu_d, so it is
P(X)=V(X^d) for a polynomial V of degree<r. The map X->X^d from F_p^*
onto mu_(4r) has fibers of size d, and W_k(X)=W_r(X^d). Therefore
M=d*m, where m is V's agreement with W_r on mu_(4r), and m>=3r/2.
Any degree-<r polynomial with more than m agreements would lift to a
degree-<k polynomial with more than M agreements, impossible.

The mu_r-orbit of V has exactly r members, all nearest at m. We have
obtained a TRUE nearest source list of size L=r, on N=4r points, of
dimension r, over the SAME prime field. This is the essential new step:
we measure length after descent, instead of keeping the full p-1 domain.
We know p>=4r+1, but do not know that p/r tends to infinity.
Nearest agreement stays m over F_(p^2), since r matching base-field
coordinates force base-field polynomial coefficients by interpolation.

## 3. At most two anchors enforce one exact rate

Choose t in {1,2} with t=r mod3. Repeatedly choose an agreement anchor
incident to the largest number of remaining selected candidates, then
divide candidate and word minus their anchor value by X-anchor.
At stage j=0 or1, each selected candidate has m-j agreements among
4r-j coordinates. Since r>=4, (m-j)/(4r-j)>=1/3. After t anchors,
at least ell>=r/9 selected quotients remain.

Their degrees are <K=r-t. The old core has length4r-t and true maximum
agreement m-t, achieved by every selected quotient. A closer quotient
would lift, after restoring the anchors, to a closer original polynomial.
This boundary claim holds over F_(p^2) by the same interpolation argument.

Set q=(r-10t)/3, which is an integer, and use q new coordinates.
For r>=40, q>=r/6>0 and q<=r/3<=m-r+1. The final parameters are

    n=4r-t+q=13(r-t)/3, K=r-t, T=m-t+1.

Thus K/n=3/13 and (T-K)/n=(m-r+1)/n>3/26.

## 4. Quadratic label count and ordinary-CA exclusion

Let Q=p^2. On the Q-4r points outside the original domain, pairwise
root counting gives mean distinct-value count at least

    mu=ell*(Q-4r)/(Q-4r+(ell-1)*(K-1)) >=ell/2,

because Q>=16r^2 and ell<=r. Choose the q points with largest diversity
and independently translate their value sets. The expected union is
at least Q[1-(1-mu/Q)^q]>=q*ell/4. The latter follows from
1-u<=exp(-u), mu>=ell/2, and q*ell/(2Q)<=1/4.
Consequently there is a choice with at least

    J>=q*ell/4>=r^2/216>=n^2/4056>n^2/4096

nearby labels at threshold T. Direction is zero on the old core and
one on every new coordinate; every counted label adds a new agreement.

If a putative common witness direction G is zero, its joint agreements
are confined to the old core and number at most m-t=T-1. If G!=0,
there are at most K-1 old zeros and at most q new joint agreements.
Their total is at most r-t-1+(m-r+1)=m-t=T-1. This excludes ordinary
correlated agreement, not only full agreement-set MCA.

Finally p>=4r+1>K-1, and
H_p(1-T/n)<=1-T/n+1/log_2(p)<1-K/n for sufficiently large p.
Taking R unbounded gives unbounded r and n, proving the statement.

## What would turn the descent into a prime-field result?

If these nearest orbits can be chosen with r/p tending to zero, the same
descent DOES give a prime-field superlinear full-support MCA theorem at
one fixed exact rate and gap. For r even set b=1; for r odd set b=2.
Since v_2(k)=1, in both cases br divides k. Compose the descended bank
with X^b, on mu_(4br). It has r candidates, dimension br, and at least
3br/2 agreements; this integer threshold has exact rate1/4 and gap1/8.

When p>=8br+1, the prime-field exact-halving compiler gives length
n'=8br, exact rate1/8 and gap1/16, with

    J>=min((3br/2)*r,p)/4,
    J/n'>=min(r,p/r)/64.

Thus r->infinity and r/p->0 suffice. Neither condition on the ratio is
proved by the orbit argument. The unconditional quadratic ordinary-CA
result above uses F_(p^2) and does not require this ratio condition.
