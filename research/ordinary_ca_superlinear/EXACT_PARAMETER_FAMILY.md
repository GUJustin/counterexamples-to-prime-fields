# An exact-parameter family in large characteristic

**Stronger current result:** RANDOM_DIRECTION_QUADRATIC.md and the main
paper now give the exact-gap result over F_(p^2), with n^2/192 labels,
and the parameter family over degree2^(b-1). The padding-only argument
below remains valid but is superseded in field degree and constants.


September 17, 2026. This generalizes the exact-gap normalization; it does
not change the prime-field or first-order limitations.

For each b in {2,3,4,5} and integer d>=b+7, there are unbounded-length
families over F_(p^e) with

    rate = b/d, capacity gap = 1/d,
    at least ceil((b+1)n^2/(4d^3)) nearby labels,
    no ordinary correlated agreement at that threshold,
    p > message degree, and fixed extension degree e = 2^b.

They are strictly below characteristic-based Elias for large enough p.
In particular b=2,d=9 gives exact rate2/9, gap1/9, at least ceil(n^2/972)
nearby labels, and extension degree four.
The new case b=5,d=12 gives rate5/12, gap1/12, at least ceil(n^2/1152)
nearby labels, and extension degree32.

## Source upper bound and the characteristic guard

The descended source has N=4r, dimension r, nearest maximum m>=3r/2,
and r selected nearest polynomials. The quadratic-indicator rigidity
proof in ../quadratic_indicator_nearest/NEAR_RIGIDITY.md now gives
m<=5r/3: apply its Dickson-word corollary on the original full field,
then divide both the domain size and maximum by the stabilizer size.
Hence Delta=m-r+1 satisfies r/2+1<=Delta<=2r/3+1<=r for r>=3.
For r>5, b<=5 gives bDelta-1<=5(2r/3+1)-1<4r+1<=p.
This extends the previous parameter family from b<=4 to b<=5.

## Parameters and label count

Put

    u=(d-b-1)Delta-3r, s=bDelta-r+1.

They are nonnegative: d-b-1>=6 and Delta>=r/2+1 imply u>=6, while
b>=2 gives s>=3. Apply the new-value operation u times and the common-zero
operation s times, preserving the selected true nearest list. The resulting
source has

    N'=(d-1)Delta+1, K'=bDelta+1, M'=(b+1)Delta.

Choose an agreement anchor incident to ell>=M'r/N'>=(b+1)r/d selected
candidates. Divide by its linear factor. The old core has maximum M'-1
and dimension bDelta. Append q=Delta challenge coordinates. The established
root-count/translation compiler, over a field of size Q>=2N'r, gives

    J>=q*ell/4 >= (b+1)Delta*r/(4d)
      >= (b+1)Delta^2/(4d) = (b+1)n^2/(4d^3),

where n=dDelta. The agreement threshold is T=(b+1)Delta and the dimension
is bDelta. A zero explaining direction has at most T-1 joint agreements
on the core; a nonzero direction has at most bDelta-1 core zeros plus
Delta new agreements, again T-1. Ordinary CA is absent.

The message degree is bDelta-1<=5(2r/3+1)-1<4r+1<=p for r>5. Also T/n-rate=1/d is fixed,
so H_p(1-T/n)<=1-T/n+1/log_2(p)<1-rate for sufficiently large p.

## Fixed extension degree

CONSTANT_EXTENSION_PADDING.md strengthens the field conclusion. The
common-zero blocks are performed BEFORE the noise block, so the first
zero block also supplies a field with enough fresh noise coordinates.

Since Delta<=r-1 for large r, s=bDelta-r+1<=(b-1)Delta. Partition the
common zeros into at most b-1 blocks of size at most Delta. Each needs
one quadratic extension: choose new roots without both members of a
Frobenius conjugate pair. Rational interpolation proves that the maximum
increases exactly by the block size. At least one block is used, so the
resulting field has size at least p^2.

Append all noise in one further quadratic extension. A union bound over
agreement supports proves that some outside-base-field value assignment
preserves the maximum; its failure bound tends to zero for fixed b,d.
The total degree is at most2^b. All tower degrees are powers of two, so
enlarge to F_(p^(2^b)) before the final label compiler. Interpolation
preserves the maximum under enlargement. The degree is fixed independently
of n. The older polynomial-degree argument is superseded.

This proof relies on the already established nearest-source theorem,
preservation operations, and label compiler. The new finite parameter
checker verifies only their arithmetic combination, not those underlying
lemmas or the existence of the asymptotic source.
