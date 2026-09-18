# Cubic remainder: differential syzygy and the archived profile

Let K=k(Z), work in K[X], and write the monic cubic after centering as

    H=Y^3+pY+q,   Delta=-4p^3-27q^2,
    W=3p' q-2p q'.

Assume characteristic zero or characteristic greater than6w; this includes the pinned prime. The caps are deg p<=2w and deg q<=3w. Unless W=0, **deg W<=5w-2**: the naive bound is5w-1, but if both degrees attain their maxima its leading coefficient cancels, while otherwise the sum of degrees is at most5w-1.

## Exact local rule, including cancellation

Suppose p,q,Delta are nonzero and put alpha=ord_x p, beta=ord_x q, gamma=ord_x Delta. Differentiation is in X over K. The polynomial identity

    27qW = p Delta' - 3p' Delta

is exact (and `4p^2 W=2q' Delta-q Delta'`). Therefore:

* If3alpha!=2beta, then gamma=min(3alpha,2beta) and ord W=alpha+beta-1.
* If alpha=2k,beta=3k and gamma=6k, then ord W>=5k.
* If alpha=2k,beta=3k and gamma>6k, then ord W=gamma-k-1.

For the first line the leading derivative coefficient is3alpha-2beta, nonzero under the characteristic guard. For the second, write p=t^(2k)u and q=t^(3k)v with units u,v; cancellation gives W=t^(5k)(3u'v-2uv'). For the third, the displayed syzygy has leading coefficient gamma-3alpha, which is nonzero. These bounds are locally sharp: choose generic units in the second line. In particular one must not ignore the balanced case with alpha=beta=0 and a positive discriminant order; it contributes gamma-1.

## Exact archived-profile evaluation

`gate.py` reads the ten-row quartic/remainder counterprofile. Its locally generic centered orders are

    alpha=min(ord h1,2 ord h2),
    beta=min(ord h0,ord h1+ord h2,3 ord h2),

and the discriminant orders are those already independently verified in the archived profile. Applying the proved rule gives total forced order

    524275 <= 655353 = 5w-2,

leaving131078 degrees of slack. The bound is therefore valid but does not exclude the profile. The computation is exact integer arithmetic and performs no optimization or scan. Detailed rows are in `gate.json`.

## Mason-type normalization does not close this profile

Set g=gcd(p^3,q^2). Dividing the discriminant identity by g gives three pairwise coprime terms. The selected local data force

    deg g >=655347,
    zero totals of p^3/g, q^2/g, Delta/g =131070,131069,131068.

Each normalized polynomial has degree at most6w-655347=131079. The selected radical support of the three coprime terms already has262140 points. Thus the ordinary polynomial abc degree inequality (maximum degree at most radical degree minus one, in the separable case) is far from contradictory. This is only a scoped check of that inequality, not a claim that all global differential identities have been exhausted.

## The W=0 branch

It cannot simply be discarded. If p and q are nonzero, W=0 says that the derivative of p^3/q^2 is zero. In characteristic zero this ratio lies in K. In positive characteristic its reduced rational-function degree is at most6w<characteristic; a nonconstant element of K(X^p) would have degree at least p, so it again lies in K.

Unique factorization then gives

    p=a h^2, q=b h^3,  a,b in K*, h in K[X], deg h<=w.

Over an algebraic closure of K this cubic is a product of three polynomial graphs Y=lambda_i h. Over K=k(Z), however, the constant cubic T^3+aT+b may be irreducible. Thus isotriviality does NOT imply a K-rational graph or contradict irreducibility of H. Any routing argument must account for this constant-field extension.

For the particular archived profile, both p and q are nonzero and simultaneously vanish on196604 distinct selected X coordinates. The displayed representation would force196604 zeros of h, exceeding deg h<=131071. Hence W=0 cannot realize this profile. This observation only justifies using the nonzero-W degree budget here; the surviving positive slack remains.

If p=0, W vanishes identically and H=Y^3+q can be irreducible; no representation q=b h^3 follows without an additional hypothesis. This pure-cubic branch requires separate treatment in a universal optimization. If q=0, the depressed cubic has a linear factor. If Delta=0, a cubic in characteristic other than2,3 is likewise reducible. These degenerate cases are not hidden inside the finite-order table.

## Outcome

The new differential inequality is rigorous, and the balanced discriminant-cancellation contribution is included exactly. It does not close the archived G4^10 H3 resource profile. No new LP or benchmark claim is justified by this test alone; a combined quartic/cubic or further simultaneous global-invariant constraint remains necessary.
