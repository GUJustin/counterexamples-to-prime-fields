# Padding without introducing any new nearest polynomials

September 17, 2026. A strengthening of CONSTANT_EXTENSION_PADDING.md.
This refines the padding mechanism; it does not lower the ambient
extension degree below four or improve the exception exponent.

## Strict common-zero blocks

Use the notation of the common-zero lemma, but require s<=Delta-1.
Then the ENTIRE new nearest list is exactly {ZP: P is old-nearest}.

Indeed, for a candidate with M+s agreements, divide out j matched new
factors and put h=s-j. It matches at least M+h old coordinates. Since
h<=s<=Delta-1, we have

    M+h = K+Delta+h-1 >= K+2h.

The same Frobenius cross-difference proof forces its reduced quotient
R/Z_0 to be a degree-<K polynomial B over the old field. Thus Q=ZB;
Q matches every new zero, and B is old-nearest. Conversely each such
lift is nearest by the original lemma. The map P->ZP is injective.

The strict inequality is needed for this stronger conclusion. The
existing F7-to-F49 fixtures with s=Delta=2 preserve the maximum but
sometimes increase the nearest-list size from4 to6 or7. In contrast,
the extended verifier checks all42 outside-base-field single roots
with s=1<Delta and finds exactly the four lifted nearest polynomials.

## Exact-list noise blocks

In the noise lemma, exclude new candidates with at least M agreements
and at least one new match. Those with K or more old matches remain
impossible. For l<K old matches and j=M-l new ones, the union bound is

    sum_(0<=l<K) binom(N,l) binom(u,M-l)
                         Q^(K-l)/(Q-q)^(M-l)
    <= 2^(N+u) Q^(-(Delta-1)) (1-1/q)^(-u).

If this bound is below one, the entire nearest list is unchanged, not
merely the maximum and the selected old witnesses. For the asymptotic
source Delta>=r/2+1, the exponent Delta-1 is still at least r/2, so
the same O(r) versus Omega(r log r) comparison gives existence.

## Compatibility with the fixed-degree construction

For fixed b in {2,3,4,5} and large r, the source bound gives
Delta<=2r/3+1<=r-b. Hence

    s=bDelta-r+1 <= (b-1)(Delta-1).

Partition the common zeros into at most b-1 nonempty blocks of size
at most Delta-1, and use the stronger noise event above. The same
fixed extension F_(p^(2^b)) therefore suffices while preserving the
ENTIRE nearest list, through multiplication by the cumulative locator.
An agreement anchor subsequently selects exactly the subset of this
list incident to that coordinate; the quotient correspondence is bijective.

This does not provide a uniform upper bound on the original source's
unknown nearest-list size. In particular it does not yet justify doing
the noise step in the same field as the zero blocks: avoiding the values
of every nearest candidate at fresh extension-field points is a separate
problem. No quadratic-extension exact-gap theorem follows here.
