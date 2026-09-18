# Centroid routing strengthens the repeated-factor dichotomy

Status: exact finite LP certificates plus a polynomial interpolation argument. This is a binding-shape subcase theorem, not a completed better.codes certificate. The centroid observation is the root's; its local and finite-profile consequences are independently checked here.

Continue with n=262144,w=131071,A0=181275,C=6802316684345 and the exact universal-factor caps from OWN_SYSTEM_RIGIDITY.md. Suppose lc_R F=G^e H, deg_Y G=d, de+h=43, e>12. Weighted additivity forces wtG=dw, and after normalization G is monic over k(Z)[X]. Its centroid

    P_c(X,Z)=-[Y^(d-1)]G/d

has X-degree at most w. Assume characteristic>d.

Outside at most12 zeros of lc_Y H, contact a>e(d-1)+h=43-e forces all d roots of G to specialize to the received symbol. Therefore P_c(x,Z)=f_x+Zg_x at every such coordinate. This is a coefficient identity, requiring no choice of roots or specialization of algebraic branches.

If the number N of these good centroid coordinates exceeds211940=n-A0+w, interpolate on w+1 of them to obtain P_c=P_0+ZP_1 with P_i in the original field and degree<=w. This removes all rational-in-Z denominators. Every degree<=w candidate with A0 agreements then coincides with this affine codeword pencil, since its agreement set overlaps the centroid coordinates in more than w points. The reconstructed identity holds at all labels, without exceptional specializations.

## Joint rank/discriminant LP

Use the quadratic costs from REPEATED_QUADRATIC_DISCRIMINANT_GATE.md and the cubic costs from REPEATED_CUBIC_DISCRIMINANT_GATE.md. At good nodes a<=43 and their total cost is at most d(d-1)w if DiscG is nonzero. Bad nodes contribute at most12R(67); pad their places with zero-contact fictitious good nodes. The n-state relaxed LP therefore obeys

    sum R(a)>=K=C-1-12R(67),
    sum cost(a)<=d(d-1)w.

The objective is the count a>=44-e. Exact duals have the form

    1[a>=44-e] >= alpha R(a)-beta cost(a)+gamma

for every a=0,...,43, with alpha,beta>=0. Summing yields the certified lower bound alpha K-beta*d(d-1)w+gamma*n. The script uses a numerical optimizer only to identify three active states, then solves both primal and dual systems with exact fractions and verifies every state inequality. The JSON records exact primal masses as well as the dual, so the relaxed LP optimum is certified on both sides.

| d | e | clean centroid-node lower bound | exceeds211940? |
|---:|---:|---:|:---|
|3|13|198518|no|
|3|14|222498|yes|
|2|13|193753|no|
|2|14|215640|yes|
|2|15|245476|yes|

For cubic e14 the dual is

    alpha=3/41670434,
    beta=118175/1602709,
    gamma=-1278824/1602709,

and its lower bound is4635781641730/20835217, giving222498 after rounding up. For quadratic e14 it is1276777031510/5920889, giving215640. The threshold requires211941, so these are not borderline rounding results.

## Combined consequences and scope

A cubic factor of multiplicity14 routes all A0-agreement candidates to one affine codeword pencil. A quadratic factor of multiplicity14 or15 does likewise; multiplicities16--21 were already excluded when their discriminants are nonzero by the previous rank bound. If the quadratic discriminant is zero, it is a squared linear graph and the existing linear multiplicity>=27 theorem applies. If the cubic discriminant is zero, characteristic>3 implies a repeated linear factor; at e14 that linear factor has multiplicity at least28 in A, so the same theorem applies. These facts follow over k(Z)[X] by monicity/Gauss factorization, with weighted additivity forcing each normalized linear factor's weight to be w.

Thus the new centroid argument closes the cubic14 and quadratic14--15 routing cases that a rank-feasibility test alone left open. The earlier cubic contact40 profile is correctly feasible for its resource inequalities, but it places almost every node in the centroid class and therefore cannot evade this pencil conclusion. Cubic13 and quadratic13 remain unclosed by this particular joint LP; its exact feasible relaxed profiles are saved, not asserted to be global polynomial examples.

No unrestricted zero-discriminant theorem, remaining-factor classification, or new final score is claimed. The appropriate no-large-selected-pencil hypothesis must still be invoked in the surrounding benchmark argument.

Artifacts: centroid_discriminant_lp.py/json.

## Further global upgrade: irreducible cubic13 and14 are excluded

The following root observation strengthens the preceding routing conclusion. Let G be irreducible of Y-degree3 and multiplicity e=13 or14. Define

    J(X,Z)=G(X,P_c(X,Z),Z).

It is a polynomial in X over k(Z), degree at most3w. It is nonzero, since otherwise Y-P_c divides G. Also DiscG is nonzero: an irreducible cubic is separable in characteristic>3.

At every good centroid node write G in the translated variable Y'=Y-word as Y'^3+bY'^2+cY'+d. All b,c,d vanish at the node. In fact ord d>=2. Otherwise the cubic Newton polygon has all root valuations1/3; choosing their3e copies gives NP_A(h)<=e, whereas a>43-e=h+2e requires the lower ordinate (a-h)/2>e. This is impossible.

Now P_c-word=-b/3, and direct evaluation gives

    J=d-bc/3+2b³/27.

Every term has order at least2. Hence J has at least two zeros at each good centroid node. The exact e13 LP lower bound198518 therefore forces

    deg_X J>=397036>393213=3w.

This contradiction excludes an irreducible cubic factor repeated13 times. For e14 the stronger count222498 excludes it as well. No new numerical optimization or pointwise slope assumption is needed. The earlier statement that cubic13 remains below the *pencil overlap* threshold is still true; the independent scalar polynomial J supplies a smaller threshold and closes the irreducible cubic case outright. Reducible cubic factors are not automatically covered by this new argument, because J may be identically zero; they must be treated through their lower-degree factors.
