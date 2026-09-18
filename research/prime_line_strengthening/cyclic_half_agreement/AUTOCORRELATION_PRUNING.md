# Exact autocorrelation pruning for the cyclic half-agreement search

Let q be odd and r=(q-1)/2. In a valid cyclic bank, let S be its first-coset
matching indices, of size r+1, and T its second-coset matching indices,
of size r. Put C=(Z/qZ) minus S and define

    lambda_U(d)=|U intersect (U+d)|.

Every pair of distinct rotated candidates has exactly r common agreements,
by the saturated root count. Thus lambda_S(d)+lambda_T(d)=r for every
nonzero d. Since lambda_S(d)=1+lambda_C(d), necessarily

    lambda_C(d)+lambda_T(d)=r-1,    d !=0.

Also lambda_U(d)=lambda_U(-d), so the r entries d=1,...,r determine the
entire profile. Profiles are invariant under translation. Every size-r or
size-(r+1) subset has full translation orbit q, because both sizes are
coprime to q. It is therefore safe to enumerate exactly one cyclic-rotation
representative of every r-subset and look up the complementary profile.

The independent C++ generator uses the complete fixed-popcount traversal,
checks all rotations, and encodes the r profile digits in base r+1. At q23
the integer key is below12^11, safely within64bits. A first support is
retained exactly when its complementary target profile occurs.

|q|All canonical supports|Compatible supports|Ordered compatible canonical(C,T)pairs|
|---|---:|---:|---:|
|7|5|2|4|
|11|42|17|24|
|13|132|18|42|
|17|1430|146|322|
|19|4862|209|448|
|23|58786|1113|2336|

The q23 first-support loop shrinks by a factor52.82; q19 by23.26.
Files `profiles_q*.json` contain all retained profiles, their target keys,
canonical C/T masks, and allowed canonical first-support S masks. The
C++ census completed in0.55seconds under the watchdog. A separate Python
set-intersection verifier exhaustively recomputed the q7/11/13 censuses and
checked every retained profile, pairing, and canonical complement through
q23. The q7 allowed S masks are exactly23 and29, reproducing the existing
positive witnesses. Files `profile_pruning.*` and `profile_independent.*`
record both checks. No field-specific assumption enters this pruning.

## Replacing the alpha scan by a compatible-target gcd

For an allowed S, its interpolant P, a twist h, and a compatible canonical
T, choose t0 in T and form, for every other t in T,

    G_t(A)=zeta^(-ht) P(A zeta^t)
           -zeta^(-ht0) P(A zeta^t0).

Every admissible alpha is a common root of these degree-at-most-r
polynomials. Compute their polynomial gcd, discard alpha=0 and alpha^q=1,
and find its remaining roots in the prime field. The value c is then
zeta^(-ht0)P(alpha zeta^t0). Usually the gcd should become constant before
root finding. This avoids a scan over all field cosets.

For q>=5 at least one G_t is nonzero. If all were zero, any nonzero
coefficient P_d would make zeta^((d-h)t) constant over T; this confines T
to a coset of a proper subgroup of size at most q/3. But |T|=(q-1)/2>q/3.
Here d-h is nonzero modulo q since d<=r<h<q. Thus the gcd has degree at
most r. (The q3 case needs separate handling.)

Crucial normalization: after canonicalizing the rotation of T, alpha must
range over ALL roots of that gcd, not only canonical coset representatives.
Changing alpha by a q-th root rotates T; canonicalizing both would lose
solutions. The simpler existing field scan can use the first-support filter
alone without any change to its correctness proof.

For a Singer complement C with constant autocorrelation, compatible T need
not itself be in a Singer multiplier class: any cyclic difference set with
the same parameters is compatible. In particular q31 Paley QR/NQR targets
remain a distinct possible test unless explicitly included in an exact
Singer-source classification.
