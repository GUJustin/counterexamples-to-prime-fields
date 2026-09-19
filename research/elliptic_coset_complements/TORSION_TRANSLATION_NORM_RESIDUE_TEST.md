# Even torsion translation: an exact high-degree residue test

2026-09-18. Bounded symbolic candidate test, with no scan. Read alongside FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md and ISOGENY_WRONSKIAN_MOVING_EXTRA_TEST.md.

Let E:y²=F(X)=X³+AX+B be nonsingular in characteristic p>3, and let ell≥23 be an odd prime different from p with full rational ell-torsion. Let Φ(X) be the monic locator of the n=(ell²−1)/2 distinct nonzero torsion x-coordinates. Fix nonzero P∈E[ell], put a=x(P), and regard Q as a variable point.

## The concrete addition candidate

The elementary even addition formula is

    x(Q+P)+x(Q−P)
      =2[a X²+(a²+A)X+Aa+2B]/(X−a)², X=x(Q).

By itself this is a bounded-pole function and cannot supply the required high-threshold far pencil. To retain the high-degree torsion residue, instead consider the even norm

    R_P(Q)=Φ(x(Q+P)) Φ(x(Q−P))/Φ(x(Q))².

This is invariant under Q↦−Q, so belongs to the rational function field in X. There is an exact identity

    R_P(X)=−4F(a) Φ'(a)² /(X−a)^(ell²).                 (1)

This uses the entire torsion locator, not a low-degree source substituted in its place.

## Proof and normalization

On the elliptic curve, the divisor of Φ(x(Q)) is

    sum_(T∈E[ell], T≠O) [T] − (ell²−1)[O].

Translation by P permutes E[ell]. Therefore the divisor of Φ(x(Q+P))/Φ(x(Q)) is ell²([O]−[−P]); the analogous divisor for −P is ell²([O]−[P]). Their product has divisor ell²(2[O]−[P]−[−P]), which is the divisor of (X−a)^(−ell²). Their ratio is a nonzero constant.

For a normalized local parameter t at O, X=t^(−2)+O(1), and x(Q±P)=a±2y(P)t+O(t²), with the choice of the two signs immaterial. Thus the numerator is −4F(a)Φ'(a)² t²+O(t³), while Φ(X)²=t^(−4n)(1+O(t)). Since 4n+2=2ell², this proves the constant in (1). Both F(a) and Φ'(a) are nonzero because the domain is squarefree and contains no nonzero two-torsion.

## What its high-degree logarithmic residue actually produces

Taking the logarithmic derivative of (1) in X and multiplying by Φ gives the polynomial identity

    Φ(X) R_P'(X)/R_P(X)=−ell² Φ(X)/(X−a).              (2)

The characteristic assumption ensures ell² is nonzero. Although the original norm is high degree, its logarithmic residue is exactly a moving coordinate spike: on the evaluation domain (2) vanishes everywhere except a and has value −ell²Φ'(a) there. Its normalized syndrome is

    −ell² (1,a,...,a^(4ell−2)).

This is a useful exact identity, but it supplies only the already available Vandermonde columns. The moving locator is J=X−a, with no relation to the subgroup-dependent two-fiber factor L0. A sum of d such residues gives at most d spikes; for distinct positions with nonzero coefficients its reduced extra locator is their product. This introduces no new quintic recurrence compatibility across different H.

In particular, a two-dimensional syndrome subspace contains at most two of these distinct spike points: any three parity-check columns are independent. More generally, if a received affine line contains two distinct words each equivalent modulo the code to errors on at most five coordinates, every word on that line is equivalent to an error supported on their union of at most ten coordinates. Then every word has agreement at least n−10, greater than the proposed threshold n−2ell−5. Such a line cannot furnish the desired far endpoints. This observation concerns the spike-only mechanism, not words with additional two-fiber errors.

Adding these spikes to subgroup-dependent quotient words remains exactly the unresolved moving-quintic system: the same global syndrome pair must satisfy equation (3) of FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md. Identity (1) gives no identity linking its arbitrary position a to those two-fiber annihilators, and (2) does not merge the previously disjoint subgroup planes.

## Decision and scope

The literal high-degree even norm of a translated division locator collapses to one pole; its logarithmic residue gives a freely moving single-coordinate error, not a shared high-degree received pencil with the required two-fiber bank. This tests a concrete addition-law candidate and explains precisely what it does provide. It does not exclude asymmetric translations, other high-degree combinations, derivatives not reduced to (2), or a future identity coupling the moving positions to L0. No computation or broader classification is claimed.
