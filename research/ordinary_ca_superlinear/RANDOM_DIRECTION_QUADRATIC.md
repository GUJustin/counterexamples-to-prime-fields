# Random padding directions remove the noise-field extension

September 17, 2026. Proof independently audited in RANDOM_DIRECTION_AUDIT.md; finite checks
are recorded in random_direction_verification.json.

## A direction exclusion lemma

Let the old core have N distinct coordinates over a field E of size H,
dimension K, and true nearest agreement T-1 for received word w.
Let Delta=T-K>0. Choose t distinct fresh coordinates, and set the line
direction to zero on the old core and independent uniform nonzero
values on the t fresh coordinates.

The probability that a nonzero polynomial G of degree<K agrees with
this direction in at least T coordinates is at most

    sum_(0<=z<K) binom(N,z) binom(t,T-z)
                         H^(K-z)/(H-1)^(T-z)
    <= 2^(N+t) H^(-Delta) (1-1/H)^(-t).             (1)

For a fixed support with z old coordinates, G must vanish there, leaving
at most H^(K-z) polynomials. Its required T-z new values are hit with
probability at most (H-1)^(-(T-z)). Nonzero G has at most K-1 old zeros.
This proves the union bound, with impossible supports omitted.

If (1)<1, choose a direction for which no such G exists. Ordinary CA at
threshold T is then absent for EVERY choice of new intercept values:
nonzero explaining directions fail the direction condition alone;
the zero explaining direction can match only the old core, where its
intercept polynomial has at most T-1 agreements.

This permits t much larger than Delta. The previous all-ones direction
proof only used the coarse sufficient restriction t<=Delta.

## Nearby-label counting is unchanged by nonzero direction values

Keep ell nearest core polynomials P_i. At a fresh coordinate x with
nonzero direction d_x, the labels they supply are

    {(P_i(x)-f_0(x))/d_x : i=1,...,ell}.

Their number equals the distinct evaluation count at x. Varying f_0(x)
uniformly and independently gives uniform independent translations of
these sets, just as for direction one. Thus one can first choose diverse
coordinates, then a good direction, then intercept translations. The
direction certificate remains valid throughout. All counted labels have
T-1 old agreements and at least one new one.

## Exact rate1/8, gap1/16 over F_(p^2)

Use the descended source N=4r, dimension r, true maximum m, and r
selected nearest polynomials. Set Delta=m-r+1, so

    r/2+1 <= Delta <= 2r/3+1.

Add s=2Delta-r+1 common zeros in ONE quadratic extension, using the
conjugate-avoiding block lemma. For large r, 1<=s<=Delta. The new source
has N'=3r+2Delta+1, K'=2Delta+1, M'=3Delta. Anchor once and divide,
retaining ell>=3Delta*r/(3r+2Delta+1) selected nearest polynomials.
The core has N_c=3r+2Delta, dimension K=2Delta, and maximum T-1=3Delta-1.

Append t=14Delta-3r fresh coordinates of E=F_(p^2). Then n=16Delta,
so rate1/8 and gap1/16 are exact. Here H=p^2>=16r^2, n=O(r), and
Delta>=r/2, so (1) tends to zero. A good nonzero direction exists.

The pairwise-root diversity bound over the H-N_c fresh points gives
mean diversity at least ell/2 for large r, since K=O(r), ell<=r, and
H>=16r^2. Choose the t most diverse coordinates. We have t<=7r for
large r, hence t*ell/(2H)<=7/32<1. Independent intercept translations
therefore give at least t*ell/4 distinct nearby labels.

For sufficiently large r, r<=2Delta-2 gives t>=8Delta. Also
r>=(3/2)(Delta-1) gives ell>=2Delta/3 once Delta>=13. Consequently

    J >= t*ell/4 >= 4Delta^2/3 = n^2/192.

The characteristic exceeds K-1, and the fixed gap is strictly below
characteristic-based Elias for large p. Thus the strengthened
conclusion is ceil(n^2/192) exceptions with no ordinary CA over F_(p^2).

## Exact parameter family

For b in {2,3,4,5}, d>=b+7, add only s=bDelta-r+1 common zeros, using
at most b-1 quadratic blocks. After one anchor the core length is
3r+bDelta, dimension bDelta, maximum (b+1)Delta-1. Append

    t=(d-b)Delta-3r >= Delta

coordinates. The final n=dDelta, threshold (b+1)Delta, and rate/gap are
b/d and1/d. Use a fixed field E=F_(p^(2^(b-1))); all zero-block degrees
divide this degree. The direction bound (1) tends to zero because the
field size is at least p^2 and n=O_(b,d)(r).

For a uniform simple count, select Delta diverse padding coordinates
for counting and fill the rest arbitrarily. The anchor retains

    ell >= (b+1)Delta*r/(3r+bDelta+1)
        >= (b+1)r/(b+6),

using r<=2Delta-2. The usual translation bound on these Delta counted
coordinates gives

    J >= Delta*ell/4
      >= (b+1)n^2/[4(b+6)d^2],

since r>=Delta for large r. Direction nonzero values do not affect this
count. Ordinary CA exclusion and the characteristic guard are as above.
This strengthens both the fixed field degree and the constant in
the previous exact-parameter family. Prime ambient fields and intrinsic
first-order tightness remain outside this argument.
