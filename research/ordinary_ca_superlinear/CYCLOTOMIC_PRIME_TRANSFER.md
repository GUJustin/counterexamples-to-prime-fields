# A sufficient characteristic-zero source for prime-field ordinary CA

September 17, 2026. Conditional transfer theorem, not an asserted source
construction. This isolates a positive target independent of the finite-
field Dickson orbit argument.

## Source hypothesis and conclusion

Fix c>0. Suppose a sequence of received words over cyclotomic number
fields has N distinct evaluation coordinates, RS dimension 1<=K<=N,
true nearest agreement M, and at least L distinct nearest polynomials,
with

    M-K >= c*N,       L -> infinity.

The cyclotomic field may vary with the source. The true nearest maximum
may be computed over an algebraic closure: since M>=K, all candidates
with at least K agreements already have coefficients in the source field.
Then there are prime-field affine-line examples, at ONE fixed rational
rate and ONE fixed positive capacity gap, with superlinearly many nearby
labels and NO ordinary correlated agreement at that threshold.
Specifically choose fixed integers

    b=ceil(1/c),       d=b+ceil(2/c).

One obtains exact rate b/d, exact gap 1/d, lengths n=Theta_c(N), and
at least Omega_c(N*L) nearby labels. Thus J/n -> infinity even when
L=o(N). If L=Omega(N), the conclusion is quadratic in length.
The characteristic exceeds the message degree and the radius is
strictly below characteristic-based Elias for sufficiently large primes.

## Specialization preserves the full nearest boundary

For each source, let F=Q(zeta_h) contain its coordinates and word values.
Consider every K-subset of the N coordinates and its unique interpolant
of degree <K. All their coefficients lie in F. These finitely many
interpolants include every candidate with at least K agreements.
Record their residuals on all N coordinates, their coefficient
differences, the coordinate differences, and all necessary denominators.
After excluding finitely many primes dividing their nonzero norms or
denominators, reduction at any prime above p preserves every zero and
nonzero in this finite record. Therefore it preserves the full nearest
maximum M and at least the selected L distinct nearest polynomials.
There can be no new higher-agreement polynomial after reduction: K of
its matches determine one of the already recorded interpolants.

Dirichlet gives arbitrarily large primes p=1 mod h outside this finite
exceptional set. These primes split the cyclotomic field, so all the
reduced data lie in F_p. For each fixed source we may require p to
exceed any further finite bound, before advancing to the next source.
This freedom is absent when N itself is defined as p-1.

## Exact normalization using only the same prime field

Put Delta=M-K+1, so cN<=Delta<=N. Choose

    s=b*Delta-K+1.

Since b*c>=1 and K<=N, s>=1. Use the same-field common-zero lemma of
PRIME_RANDOM_DIRECTION_TRANSFER.md s times. It preserves the exact
maximum and the selected L candidates. This is possible by requiring
p>N+s+2^(N+s) when choosing the splitting prime; s=O_c(N).
The new source parameters are

    N'=N+b*Delta-K+1,
    K'=b*Delta+1,
    M'=(b+1)*Delta.

One agreement anchor retains at least ell=M'*L/N' candidates.
Since N'<=N+b*Delta+1<=(b+2)N and Delta>=cN,

    ell >= [(b+1)c/(b+2)]*L.

Subtract the anchor value and divide by its linear factor. The core
has length N_c=N+b*Delta-K, dimension b*Delta, and true maximum
(b+1)*Delta-1. Append

    t=(d-b)*Delta-(N-K)

fresh points. Since (d-b)c>=2, t>=N+K>=N. Also t=O_c(N).
The final n=d*Delta=Theta_c(N), dimension b*Delta and threshold
T=(b+1)*Delta give exact rate b/d and exact gap 1/d. No asymptotic
rounding or passage to a varying rate is hidden in this normalization.

## Directions, diversity, and number of labels

Choose p still larger if necessary so that p-N_c exceeds both t and
(ell-1)(b*Delta-1). Then pairwise-root counting gives mean diversity
at least ell/2 on the fresh coordinates. Select the t most diverse
coordinates. The random nonzero-direction failure probability is at
most

    2^n * p^(-Delta) * (1-1/p)^(-t).

It is less than one for sufficiently large p; indeed for a fixed source
it tends to zero as p grows. Choose a good direction. Its certificate
excludes all nonzero ordinary-CA directions independently of intercepts;
a zero direction has only core agreements, at most T-1.
Require also p>=t*ell/2. Independent fresh intercept translations then
produce at least t*ell/4 distinct nearby labels. Hence

    J >= [(b+1)c/(4(b+2))]*N*L.

All prime-size requirements are finite and may be included in the
splitting-prime choice. Polynomial distinctness and maximum preservation
were secured before padding; the common-zero operation preserves both.
The final code dimension is O_c(N), so p may also exceed its degree.
As the exact gap is 1/d, the characteristic-Elias inequality follows
for large p. L->infinity forces N->infinity, since L<=binom(N,K).

## What is missing for the cyclic Dickson word

The characteristic-zero specialization argument itself is valid.
What is unavailable is a source with BOTH a fixed linear nearest margin
and an unbounded nearest bank. The finite-field Dickson lower bound
M>=3K/2 uses characteristic-dependent identities and does not carry to
fixed characteristic-zero cyclic domains. Exact existing censuses show
that the cyclic word has maximum K at K=2,4,5, and maximum 8 at K=6;
these already refute a universal characteristic-zero 3K/2 lower bound.
At cyclic lengths 12 and24 there are fixed-gap banks of sizes 3 and9,
but the larger structured lifts found so far are compositions with
bounded bank size. These do not supply L->infinity.

The positive research target is therefore: over varying cyclotomic
fields, construct true nearest lists with a fixed positive margin
(M-K)/N and L->infinity. Exact nearestness is essential for excluding
the zero correlated direction; a large sublist at a nonmaximal threshold
alone does not meet this transfer theorem's hypothesis.
