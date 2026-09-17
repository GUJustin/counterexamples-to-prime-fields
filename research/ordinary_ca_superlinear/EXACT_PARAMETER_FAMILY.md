# An exact-parameter family in large characteristic

September 17, 2026. This generalizes the exact-gap normalization; it does
not change the prime-field or first-order limitations.

For each b in {2,3,4,5} and integer d>=b+7, there are unbounded-length
families over F_(p^e) with

    rate = b/d, capacity gap = 1/d,
    at least ceil((b+1)n^2/(4d^3)) nearby labels,
    no ordinary correlated agreement at that threshold,
    p > message degree, and e <= n^b.

They are strictly below characteristic-based Elias for large enough p.
In particular b=2,d=9 gives exact rate2/9, gap1/9, at least ceil(n^2/972)
nearby labels, and extension degree at most n^2.
The new case b=5,d=12 gives rate5/12, gap1/12, at least ceil(n^2/1152)
nearby labels, and extension degree at most n^5.

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

## Extension degree

Work first over F_(p^2), which supplies all u new base-field coordinates
for sufficiently large r (b,d are fixed). Add the noise in one block,
costing extension degree u+1. Perform one single common-zero operation,
costing degree2. There remain h=bDelta-r common zeros, where

    1<=h<=(b-1)Delta.

Partition these into at most b-1 nonempty blocks of size at most Delta.
At each stage maximum minus dimension plus one is still Delta, so the
translated-root block lemma applies. If a block has size h_j and the
current dimension is K_j, its field-degree cost is K_j+2h_j. Since the
final source dimension is bDelta+1, each cost is at most
(b+1)Delta+1 <= (b+2)Delta.

Moreover u+1<=(d-b-3)Delta. Therefore

    e <= 4(d-b-3)(b+2)^(b-1) Delta^b <= (dDelta)^b = n^b.

The last inequality holds for b=2,3,4,5 and d>=b+7: the function
(d-b-3)/d^b decreases beyond d=b(b+3)/(b-1); check the initial integer
values d=9,10 for b=2, d=10 for b=3, d=11 for b=4, and d=12 for b=5. The resulting
field has size at least p^4, exceeding2N'r for large r. The compiler
therefore needs no further extension.

This proof relies on the already established nearest-source theorem,
preservation operations, and label compiler. The new finite parameter
checker verifies only their arithmetic combination, not those underlying
lemmas or the existence of the asymptotic source.
