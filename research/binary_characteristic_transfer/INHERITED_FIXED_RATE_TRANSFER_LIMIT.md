# Inherited puncturing and shortening of the p^5 locator seed

Status: independently audited PASS; see `INHERITED_TRANSFER_INDEPENDENT_AUDIT.md`. This concerns the canonical witnesses of `EXPLICIT_LOW_RATE_LARGE_CHARACTERISTIC.md`; it is not an impossibility theorem for new witnesses or new received lines.

Write D for the polynomial degree cap (code dimension D+1). Common agreement C means the maximum number of coordinates on which both received sources admit simultaneous degree-at-most-D polynomial explanations. There are M distinct labels z_i, each with a designated witness agreeing on at least A coordinates. Always assume C<A.

## Exact seed structure

The seed domain is F_(p^5), D=p-1. Each three-dimensional F_p-subspace W has a distinct label and a witness

    H_W(X)=u_W X^(p-1)+v_W,

of exact degree p-1 and exact agreement support W\{0}. Every two-dimensional F_p-subspace U has simultaneous degree-at-most-p-1 explanations of the sources on U\{0}. These statements follow from the locator formulas in `GOLD_AND_NEAR_JOHNSON_LEDGER.md`; a shift of the source along its direction preserves them after relabeling.

## 1. Common-zero lengthening alone

Adding z common zeros, and multiplying every witness and both sources by their locator, changes

    (N,D,A) -> (N+z,D+z,A+z).

With rho=D/N and a=A/N, the exact identity is

    a_new-rho_new=(1-rho_new)(a-rho)/(1-rho).

For the seed, rho=(p-1)/p^5 and a=(p^3-1)/p^5. At any fixed resulting rate below one the agreement excess tends to zero as O(p^-2). Thus this operation alone does not retain a fixed margin above a first-order curve strictly above capacity. Moreover, exact witness degree p-1 means any nonzero lengthening violates p>D unless degree was first saved by shortening.

## 2. Arbitrary puncturing, retaining canonical witnesses

Let S be any retained set of n coordinates. Put s_U=|S intersection (U\{0})|. The common explanations imply s_U<=C for every two-plane U.

A rich W has at least A retained nonzero points. If A>p-1, it contains at least A(A-p+1) ordered linearly independent pairs: after the first point, its nonzero F_p-line contains at most p-1 points. Every such pair determines U. Distinct three-spaces W containing U intersect exactly in U. Their retained points outside U are therefore disjoint, and their number is at most

    (n-s_U)/(A-s_U) <= (n-C)/(A-C).

Double counting the independent pairs gives the exact bound

    M <= n(n-1)(n-C) / [A(A-p+1)(A-C)].                 (1)

A complementary independent-triple count gives

    M <= n^3 / [A(A-C)^2].                            (2)

Indeed after choosing the first support point, each forbidden span of dimension one or two lies in a two-plane with at most C retained points. Thus each rich W contributes at least A(A-C)^2 independent ordered triples, and each triple determines W uniquely.

In particular, if A>=alpha*n and A-(p-1)>=delta*n for fixed positive alpha,delta, (1) yields M=O(n/(A-C)). Strict integer common-agreement gap implies M=O(n); a fixed fractional gap implies M=O(1). These are bounds on inherited labels, not on additional witnesses which may appear after puncturing.

## 3. A scalar-witness lemma

Over any field, suppose the designated witnesses, after subtracting a common affine-in-label polynomial explanation, are

    h_i=u_i Q(X),   deg Q<=D,

with distinct z_i. If Q is nonzero and A>D, then

    (M(A-D)-n)(A-C) <= n(n-1).                        (3)

Proof. In the parameter plane (z,u), a coordinate x imposes the affine equation

    u Q(x)-z g(x)=f(x).

Every candidate matches at least A-D coordinates where Q(x) is nonzero. Such a coordinate defines a nonvertical line. Call it private if the line contains only one retained parameter point, and public otherwise. There are at most n private incidences in total.

A public line contains two parameter points with distinct labels. Solving their two equations expresses the received f and g as scalar multiples of Q at every coordinate with that same constraint line, and at every universal constraint (f=g=Q=0). Consequently a candidate has at most C matching coordinates with a constraint proportional to the public line or universal. For each public matching first coordinate there are at least A-C matching second coordinates with independent constraints. An ordered pair of independent constraints determines at most one parameter point. There are at most n(n-1) ordered coordinate pairs. The number of public first incidences is at least M(A-D)-n, proving (3). If that lower bound is negative the claimed inequality is automatic.

Vertical constraints cause no issue: they contain at most one retained label and can occur as the second coordinate. The explanations above have degree at most D. Subtracting affine-in-label degree-at-most-D polynomials preserves both agreement and common agreement.

If Q=0, each coordinate is either universal or matches at most one label. There are at most C universal coordinates, whence

    M(A-C)<=n-C.                                     (4)

More generally (4) holds whenever all witnesses are affine in the label, after subtracting that affine explanation.

## 4. Coordinated common-root shortening

Choose a nonempty set B matched by every retained canonical witness. Shorten by subtracting simultaneous polynomial explanations on B and dividing sources and witnesses by its locator. Then allow arbitrary puncturing and common-zero lengthening. We prove that (3) or (4) applies to the resulting inherited family, with its final degree cap D.

Fix x0 in B. It is nonzero. Put V=X^(p-1)-x0^(p-1). Agreement at x0 rewrites every witness as

    H_i=f(x0)+z_i g(x0)+u_i V.

The roots of V are exactly x0 F_p^*. Both source polynomials are constant on each such nonzero F_p-line: their exponents are p^j-1.

If B is contained in that line, subtract the constant explanations f(x0),g(x0). Every shortened witness is u_i V/A_B. Any subsequent common-zero lengthening multiplies this fixed polynomial by the same locator, and arbitrary puncturing preserves the scalar-witness form. Its degree is at most the final cap, so (3) applies. Choosing different valid explanations on B only adds affine-in-label polynomial terms after division, which can be subtracted again.

If B contains x with V(x) nonzero, agreement there forces u_i to be affine in z_i. Therefore H_i=H_0+z_i H_1 globally. At two or more distinct labels, their simultaneous agreement on B forces H_0,H_1 to be valid common explanations there. Shortening and lengthening preserve an affine-in-label witness family; subtract it and use (4). A family of at most one label is harmless.

This proves the stated operation order: shorten the original canonical family on common matched coordinates, then puncture and lengthen. It also allows initial puncturing, provided shortening uses retained common matched coordinates. No assertion about arbitrary operations creating new witnesses is implicit.

## Fixed-rate conclusion and remaining escape

For final A-D>=delta*n with fixed delta>0, (3) gives

    M <= 1/delta + (n-1)/[delta(A-C)].

Thus all the inherited routes above have at most linear population whenever the common-agreement gap is positive, and bounded population if A-C>=epsilon*n for fixed epsilon>0. A fixed-rate fixed margin above first order in particular has a fixed positive margin above capacity and falls within this conclusion.

The original vanishing-rate family evades these bounds quantitatively: both its agreement density and its excess over capacity tend to zero. The theorem does not rule out a new source construction, a different support geometry, or fresh low-degree witnesses created by puncturing/shortening. Those are genuine noninherited escape routes. It also does not claim that an arbitrary smooth-lifting dimension count excludes structured dependent incidence systems.
