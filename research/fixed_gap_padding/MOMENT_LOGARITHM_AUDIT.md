# What would remove the logarithm from the interval seed bound?

September 17, 2026. Research-direction audit; no improved lower bound.

The exact-range and Gram estimates already retain the factorial savings.
Their leading logarithmic denominator is (s^2/2) log(n/s). The Gram
improvement changes the order-s^2 term, not this leading term. Thus
re-optimizing the same range or covariance estimate does not remove
the logarithm in the inverse-gap exponent.

## A quadratic ceiling for this integer seed mechanism

Let two distinct subsets S,T of {0,...,n-1}, of the same cardinality,
have identical INTEGER moments of orders 1,...,s. Define

    F(Z)=sum_{i in S} Z^i - sum_{i in T} Z^i.

This is a nonzero polynomial with coefficients in {-1,0,1}. Equality
of the cardinality and binomial moments of orders 1,...,s is equivalent
to divisibility by (Z-1)^(s+1). After removing the initial zero
coefficients and possibly changing sign, its constant coefficient is1
and all coefficients have absolute value at most1.

The bounded-coefficient zero estimate gives s+1<=C sqrt(n), for an
absolute constant C. One primary modern source is Erdelyi's Theorem3.1,
which explicitly attributes its M=1 case to Borwein--Erdelyi--Kos,
Theorem4.1 (1999):
https://arxiv.org/html/2409.09553v5

Consequently, if the exact seed gap is eta=s/n and its integer moment
class has at least two members, n<=C^2/eta^2. Its cardinality is at
most2^n, so its logarithm is O(eta^-2). Our lower bound
Omega(eta^-2/log(1/eta)) is within a logarithmic factor of this ceiling.
This is a limitation of INTEGER interval moment classes, not an upper
bound for arbitrary received words, arbitrary domains, or modular
moment collisions. It is not a new analytic zero theorem.

## Why a stronger pair construction would still not be enough

A log-free exponential-size class at length n=Theta(s^2) would in
particular supply a height-one polynomial of degree O(s^2) with a zero
of order s+1 at1. Borwein and Mossinghoff's primary paper records the
classical degree bounds of order at least m^2 and at most m^2 log m
for a single height-one polynomial with multiplicity m:
https://www.cecm.sfu.ca/~pborwein/PAPERS/P153.pdf

Those bounds are quoted as the scope of that source, not as a claim
that a literature search proves the exact problem remains open today.
The 2024 paper's sharpness statements allow real coefficients and do
not provide the required {-1,0,1} construction, much less an
exponentially large common moment class. No source checked in this
audit supplies that stronger many-subset input.

Even finding one especially efficient pair would not establish the
desired list lower bound. Independently choosing between translated
copies of one pair on disjoint blocks produces only 2^r choices.
Each nonzero switch has at least s+2 support positions: otherwise the
Vandermonde system for moments0,...,s would make the switch zero.
Hence r(s+2)<=n and log2(list_size)=r<1/eta. This binary disjoint-block
amplification cannot even reproduce the current nearly quadratic
exponent. A useful improvement needs many compatible overlapping
relations, not merely isolated high-order pairs.

The present work therefore retains the verified logarithmic factor.
The promising target is a new large integer moment fiber, or a
different construction; another covariance-constant optimization is
not a route to changing the leading order.
