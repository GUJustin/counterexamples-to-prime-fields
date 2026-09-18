# Universal factors: an actual collapse of the challenge-degree cap

## A certified near-codeword-direction consequence

Retain n262144,w131071,m118,s36,D=m*181275=21390450. Increase the primary joint-degree cap from L176421 to L176938. This is an explicit single-shape repair, not a parameter search.

The exact source count with strict weight cutoff D−2 and this enlarged L exceeds the standard local-constraint bound by1055943. The affine dependence on L and minimality are independently checkable from the direct coefficient and local-rank sums in `interior_L_reserve.py/json`. At D−1 the minimal L is176679; at D−2 it is176938. Thus the two-unit interior reserve costs517 units of L, approximately0.293% of the old cap.

Suppose the received direction is the evaluation of a polynomial h of degree at most w+1. Let V be the FULL primary kernel with cutoff D and joint cap176938, and let irreducible F divide every member of V. If 3wt(F)≥D, the interior-source derivation lemma in `UNIVERSAL_FACTOR_DERIVATION.md` gives

    delta_h F=0,
    delta_h=partial_Z+h partial_Y+h' partial_R.

Here characteristic p>L suffices to turn derivative-zero into independence of Z after the jet translation. Consequently

    F=F0(X,Y−Zh(X),R−Zh'(X)),

where F0 is independent of Z. Translation by X-dependent multiples of Z preserves the joint (Y,R,Z)-degree and preserves the degree in(Y,R) when coefficients are viewed over k(X,Z). Since F0 has no Z variable, this gives the exact conclusion

    totalDegree_(Y,R,Z)(F)=degree_(Y,R)(F).

In the receipt notation, t(F)=y(F), hence z(F)=0. This is a genuine restriction on UNIVERSAL factors, not on an arbitrarily chosen interpolant.

In particular every universal factor with y≥55 and r≤36 has

    wt(F)≥wy−r≥55*131071−36=7208869,
    3wt(F)>D.

The binding carrier y55,r12,t3261 therefore cannot occur in this near-codeword-direction class after the explicit primary-L repair. More generally all such high-y universal factors leave the positive-z carrier regime. This is stronger than ruling out the earlier illustrative countermodels, which were never universal factors to begin with.

**Scope.** The full primary kernel has been enlarged, so the assertion is about its universal factors. It is not an assertion that the old kernel's gcd is unchanged. All modified primary helper/complement costs would have to be propagated for a numerical theorem on this subclass. An arbitrary received direction need not have degree at most w+1, so no full better.codes improvement follows.

## A general Hermite--Padé contact-preserving operator

For arbitrary direction values g_i at distinct nodes x_i, seek polynomials a,b,c satisfying

    b(x_i)=a(x_i)g_i,
    c(x_i)=b'(x_i)−a'(x_i)g_i.                 (1)

Then

    delta=a(X)partial_Z+b(X)partial_Y+c(X)partial_R

preserves every first-jet contact filtration. Indeed, with t=X−x_i and J=Y−f_i−Zg_i−tR, one has delta(t)=0 and

    delta(J)=b(X)−a(X)g_i−t c(X),

which is divisible by t² exactly by(1). Thus substituting J=t²E gives another polynomial expression in the local variables; no bound on contact multiplicity is needed for this preservation statement.

If deg a≤Delta, deg b≤w+Delta, and deg c≤w−1+Delta, the operator raises contact weight by at most Delta, lowers joint degree by one, and does not increase R-degree. There are3Delta+2w+2 coefficients and at most2n homogeneous linear constraints. Therefore a nonzero operator exists whenever

    3Delta+2w+2>2n.

At the pinned parameters Delta87382 suffices. Since deg b,deg c<n at this value, any nonzero solution has a≠0: a=0 would force first b and then c to vanish at all n nodes.

For any a≠0, work over k(X) and change coordinates to

    W=Y−(b/a)Z, U=R−(c/a)Z.

Then delta=a partial_Z. The same interior-source universal-factor proof applies; when it establishes delta(F)=0 and p>L, it again forces t(F)=y(F). The operator need not be the jet translation of a rational function: only the two finite-domain Hermite conditions(1) are required.

## Why this does not yet remove the generic binding carrier

The current shape would require a2Delta=174764 interior weight reserve for a binding factor of multiplicity at most two. Increasing L cannot repair its standard dimension gate. At cutoff D the scalar coefficient-minus-rank slope in L is3696226. Throughout the cutoff interval down to D−174764 there are at least5328 admissible(Y,R) monomials, so lowering the cutoff decreases that slope by at least

    174764*5328=931142592.

The new slope is therefore at most−927446366. Thus the same affine-in-L certificate cannot establish a generic interior source at ANY sufficiently large L. This is a failure of the given count bound, not proof of a zero kernel.

For comparison the exact direct test at the ordinary polynomial-interpolant direction cost n−1−w gives reserve262144 and slope−1399772863. The Hermite--Padé operator genuinely improves the universal degree cost from roughly n/2 to n/3, but still misses the available source margin by a large amount.

The productive remaining question is whether a different source/contact-rank mechanism can provide this interior reserve without increasing the geometric cost beyond the proper-helper savings. Another possibility is a sharper upper bound on the multiplicity of a universal factor in a suitable kernel element. Neither follows merely from the positive dimension of the full primary kernel, and neither is claimed here.
