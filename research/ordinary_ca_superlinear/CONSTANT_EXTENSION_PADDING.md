# Exact rate and gap over a fixed-degree extension

September 17, 2026. Two padding refinements replace extension degrees
growing with length by constant extension degrees. Proof and finite
checks are kept separate. This still does not give prime ambient fields.

## 1. A common-zero block in one quadratic extension

Let F=F_q, let a word w on N distinct F-points have maximum agreement M
with degree-<K polynomials, and put Delta=M-K+1>=1. Take 1<=s<=Delta.
In E=F_(q^2), choose s distinct elements A outside F with

    A intersect A^q = empty.

There are (q^2-q)/2 available conjugate pairs, so this is possible when
s is at most that number. Put Z=product_(a in A)(X-a). Replace w(x)
by Z(x)w(x), append the s coordinates A with value zero, and increase
the dimension to K+s. The new maximum is exactly M+s, and every old
nearest polynomial P lifts to the nearest polynomial ZP.

Proof. The lower bound is immediate. Suppose Q of degree<K+s has at
least M+s+1 agreements. Let T be its j matched new coordinates, let
Z_T be their locator, and put h=s-j, Z_0=Z/Z_T, R=Q/Z_T. On at least

    ell=M+h+1=K+Delta+h >= K+2h

old coordinates we have R(x)=Z_0(x)w(x), and deg R<K+h, deg Z_0=h.
Apply coefficientwise q-Frobenius. Since these coordinates and w-values
are in F, both rational functions R/Z_0 and R^q/Z_0^q interpolate w.
Their cross difference has degree less than K+2h and at least ell
roots, so it vanishes identically. The reduced rational function is
therefore in F(X): normalizing its denominator to be monic, uniqueness
of the reduced expression makes numerator and denominator Frobenius-fixed.
Its denominator divides both Z_0 and Z_0^q. These are coprime by the
choice of A, so the denominator is constant. Hence R/Z_0 is a polynomial
of degree<K agreeing with w on ell>M old coordinates, a contradiction.

The maximum also persists over further coefficient extensions: K+s
matching E-points and values force coefficients into E by interpolation.
The conjugate-pair exclusion is essential; a finite negative control
below shows that merely choosing new roots outside F is insufficient.

## 2. A noise block in one quadratic extension

Let the source be over F_q with the same N,K,M,Delta. Choose u distinct
fresh evaluation points in F_q, requiring N+u<=q. Assign each an
independent uniform received value in E minus F, where E=F_(q^2) and
Q=q^2. Every selected old nearest polynomial retains M agreements.

A candidate with M+1 agreements and at least K old agreements would
have coefficients in F and cannot match any new value; without a new
match it contradicts the old maximum. For a fixed support with l<K
old and j=M+1-l new coordinates, the old constraints allow Q^(K-l)
polynomials. Thus the probability that this support is interpolated is
at most Q^(K-l)/(Q-q)^j. Union bounding gives failure probability at most

    sum_(0<=l<K) binom(N,l) binom(u,M+1-l)
                       Q^(K-l)/(Q-q)^(M+1-l)
    <= 2^(N+u) Q^(-Delta) (1-1/q)^(-u).             (1)

Terms with impossible j are zero. If either bound is below one, some
choice preserves the exact maximum M. This argument includes every
degree-<K polynomial over E, not just the selected list. As before,
interpolation makes the resulting maximum stable under further extensions.

## 3. Consequence for the exact-parameter family

Fix b in {2,3,4,5} and d>=b+7. Use the descended source of length4r,
dimension r, nearest maximum m, and selected list size r. We have

    r/2+1 <= Delta=m-r+1 <= 2r/3+1,
    u=(d-b-1)Delta-3r, s=bDelta-r+1.

Perform the COMMON-ZERO blocks first. For large r, Delta<=r-1, hence
s<=(b-1)Delta. Partition s into at most b-1 blocks of size at most Delta.
Each uses one quadratic extension and preserves Delta. At least one
block is used, so the resulting field F_q has q>=p^2>=16r^2. The
required conjugate pairs exist at every stage.

This field supplies all u fresh noise coordinates for large r. Apply
the noise lemma in its quadratic extension. After the zero blocks,
N+u=(d-1)Delta+1=O_d(r), Delta>=r/2, and q>=16r^2, so bound (1)
tends to zero. Its logarithm has a negative term -Omega(r log r) and
a positive term O_d(r). Thus the noise block succeeds for large r.

The total extension degree over F_p is at most

    e <= 2^(b-1)*2 = 2^b.

One may enlarge to F_(p^(2^b)) to make the degree fixed exactly. All
tower degrees are powers of two, and interpolation preserves the nearest
maximum under enlargement. The label compiler then operates in this
same field, whose size is at least p^4 and exceeds 2N'r for large r.
Adding zeros first saves one quadratic extension relative to starting
with noise in a pre-enlarged base field.

The original exact parameter and ordinary-CA arguments are unchanged:
rate b/d, gap1/d, at least ceil((b+1)n^2/(4d^3)) exceptional challenges,
no ordinary correlated agreement, and characteristic greater than message
degree. Thus these examples exist over the FIXED extension
F_(p^(2^b)), with growing prime p.

In particular:

* b=2,d=16: exact rate1/8 and gap1/16 over F_(p^4), with at least
  ceil(3n^2/16384) challenges (also implying the earlier n^2/8192 bound).
* b=2,d=9: rate2/9, gap1/9, ceil(n^2/972) challenges over F_(p^4).
* b=5,d=12: rate5/12, gap1/12, ceil(n^2/1152) challenges over F_(p^32).

This strengthens the ambient-field conclusion of the exact-gap results.
It does not change their quadratic length exponent, place them in the
first-order regime, or yield a better.codes improvement.
