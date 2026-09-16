# A quantitative obstruction to transferring the binary quadratic family

September 16, 2026. Deduction from the published binary-affine locator theorem.
Twice self-reviewed; exact checks passed. Integrated as Corollary F.2.
No independent coauthor review or novelty claim is asserted.

## Statement

Let V=F_2^m, N=2^m, m>=4. Injectively label V\{0} by elements of a
field F of characteristic different from two. Let C be a collection
of codimension-two linear subspaces W of V such that the monic locators
of the labeled punctured supports W\{0} share their first s=N/8-1
coefficients below the leading term. Set

    M_N = floor((1+sqrt(4N-7))/2).

Then

    |C| <= floor((N-1)*M_N/3) = O(N^(3/2)).        (1)

The condition m>=4 ensures s>=1. The full binary family has
(N-1)(N-2)/6 members, so a positive asymptotic fraction cannot preserve
this prefix under any odd-characteristic relabeling. This is a barrier
to transferring that support-and-locator mechanism, not to all methods
involving binary fields, and not an upper bound for arbitrary RS lists.

## 1. Fix a containing hyperplane

Identify V* with its binary dual. Fix nonzero a in V*. The codimension-two
subspaces with a in W-perp are precisely

    W_b = ker(a) intersect ker(b),

where b ranges over the nonzero elements of Q=V*/<a>, with |Q|=N/2.
Write S_a for the subset of these b corresponding to members of C.

The indicator of W_b on ker(a) is 1+b(x) over F_2 and is zero outside
ker(a). As b varies, this is an injective affine map into binary
indicator vectors. Puncturing the origin, which is always selected,
preserves affine dimensions and makes every weight t=N/4-1.

If S_a contained an affine binary plane, the four corresponding
punctured supports would be an affine family of dimension two and
constant weight t. The published binary-affine locator theorem would
give

    2 <= floor(t/(s+1)) = floor((N/4-1)/(N/8)) = 1,

a contradiction. Thus S_a contains no affine plane.

## 2. A plane-free binary set is Sidon

In a vector space over F_2, equality of the sums of two distinct
unordered pairs of distinct elements forces four distinct elements
forming an affine plane. Hence all binom(|S_a|,2) pair sums are distinct
and nonzero. There are only |Q|-1=N/2-1 possible sums, so

    |S_a|*(|S_a|-1) <= N-2,

which gives |S_a|<=M_N.

Every codimension-two W has exactly three nonzero elements of W-perp.
Double-counting (a,W) gives 3|C|=sum_(a!=0)|S_a|<=(N-1)M_N and proves (1).

## Relation to the supplied binary construction

The Dropbox draft's quadratic obstruction uses N=16K and the locators

    L_W=X^(4K)+a_W X^(2K)+b_W X^K+V_W.

After division by X, the punctured locator has degree 4K-1, and its
first 2K-1=N/8-1 coefficients vanish. Thus its entire quadratic
support family has exactly the prefix property excluded above in odd
characteristic. The argument permits arbitrary injective relabeling;
it does not assume that the binary addition law is preserved.

The source is the user-supplied Dropbox draft, section "A quadratic
obstruction on arbitrary additive domains". The proof here is a
combinatorial consequence of Appendix F of the official prime-field
paper; it does not use or reproduce protocol behavior.

## More general fixed prefixes

For any 0<=s<N/4-1, put R=floor((N/4-1)/(s+1)). Then S_a contains no affine
(R+1)-flat. If A is such a flat-free subset of a binary group of size q,
then |A|<=4*q^(1-2^(-R)) for R>=1 (the R=0 case is |A|<=1).
One elementary induction proves this: for each nonzero h, pair A along
the cosets of <h>. The occupied pairs define a subset of the quotient
containing no affine R-flat. Summing their sizes gives

    |A|*(|A|-1) = sum_(h!=0) |A intersect (A+h)|.

Apply the induction hypothesis on the quotient of size q/2 and take
a square root. The constant four is preserved because
sqrt(2^(2^(1-R))*4)+1<=4. For R=1, the exact Sidon count above is sharper.

Consequently, for every fixed positive fractional prefix s/N, the
number of codimension-two supports in one odd-field prefix class is
O(N^(2-2^(-R))), with exponent strictly below two. The explicit
N^(3/2) bound uses the prefix length of the supplied quadratic family.

## Verification

The standard-library checker tests 24,825 prefix classes in 390 injective
relabelings of binary domains of sizes 16, 32, and 64. It checks every
local dual star for the Sidon property and verifies the global incidence
count. This includes 20 F_81 relabelings in characteristic three at
prefix length three. Separately, it verifies 14,364 affine-plane
parameterizations and the full shared-prefix binary families of sizes
35 and 155 over F_16 and F_32, respectively. Both exceed the corresponding
odd-characteristic upper bounds 20 and 62.

The sequential run completed under a 384 MiB watchdog in less than one
second. Its RSS sampling interval did not capture the child process's
high-water usage, so no exact peak-memory claim is made. Finite checks
supplement the combinatorial proof rather than establish it.
