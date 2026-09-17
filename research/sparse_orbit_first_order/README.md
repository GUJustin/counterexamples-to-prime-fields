# Sparse multiplicative orbits and the first-order target

September 17, 2026. Complete finite search, no asymptotic impossibility claim.

For p=4k+1, let H=mu_k act on degree-<k polynomials by input scaling.
The domain is all F_p*. We enumerate every polynomial with at most three
nonconstant terms, up to output translation and nonzero scaling. The
constant coefficient is set to zero and the highest coefficient to one;
these normalizations preserve all agreement counts and orbit sizes.

For each polynomial P, its orbit size is

    L = k/gcd(k, all nonzero exponents of P).

On each of the four H-cosets, choose a most frequent value of P. The sum
M of the four mode frequencies is the largest possible minimum agreement
of the FULL orbit with any received word on this fixed domain. Indeed,
the value histogram of the orbit at each coordinate is the corresponding
coset histogram, with a uniform multiplicity factor. Coordinatewise modes
maximize average agreement. The coset-constant modal word makes every
orbit member have the same agreement M, attaining that average upper bound.
The optimization therefore permits arbitrary received words, not just
coset-constant ones. It does not optimize proper subsets of the orbit or
other evaluation domains.

At quarter rate, the audited continuum first-order curve is crossed
exactly when 31M^2-6Mn-4n^2>0. This is only a regime test; a finite example
above the curve need not contradict any upper bound, and the finite
characteristic requirements of a particular theorem must still be checked.

| p | Normalized polynomials checked | Orbit size : optimal maximum agreement |
|---|---:|---|
|17|307|2:8, 4:7|
|41|135,849|2:20, 5:14, 10:12|
|73|3,534,929|2:36, 3:30, 6:24, 9:24, 18:17|

Only the two-element orbit crosses the curve in these searches. It is
represented by P=X^(k/2), with agreement n/2. There is no growing-orbit
first-order candidate here. Over F17 the three-term search is the entire
space of degree-<4 nonconstant polynomials modulo output affine changes.
Over F41 and F73 it excludes dense polynomials; in particular the known
dense Dickson orbit has better agreement than the displayed sparse maximum.

`scan.cpp` records a maximizing witness, every coset mode/frequency, and
counts for each orbit size. There are exactly
sum_{s=1}^3 binomial(k-1,s)*(p-1)^(s-1) normalized cases. Every modular
calculation is exact. Compile with C++17, -O2, and assertions enabled;
the local run used the Zig wrapper with target aarch64-macos.14.0.
Invoke the executable separately with p=17,41,73, sequentially under the
repository384MiB/60-second watchdog. `p*.log` files contain the outputs.

`verify.py` independently computes case counts by exponent gcd, replays
all recorded witness orbits and agreements, and independently exhausts
all307 normalized F17 polynomials. All checks pass. No paper theorem or
better.codes improvement follows from this finite negative search.
