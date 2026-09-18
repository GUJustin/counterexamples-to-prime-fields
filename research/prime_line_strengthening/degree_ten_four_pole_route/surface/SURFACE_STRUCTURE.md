# Surface structure of the degree-ten norm net

This note separates exact intersection-theoretic consequences from an identification with a named surface family. It produces a useful bicanonical pencil, but not a rational member of the degree-ten net.

## Blowup and the seven curves

Let X be F3 blown up at the fourteen word points. Write C0 for the negative section, F for a fiber, and E_x for the exceptional curves. The seven old cubic graphs have strict transforms

    B_i=C0+3F-sum_{x matched by i}E_x.

Each is a smooth rational (-4)-curve. They are pairwise disjoint: each pair of old cubics has exactly three distinct common points, exhausting its intersection number3, so those intersections are transverse and the single blowup separates them. Let B=sum B_i. Then

    K_X=-2C0-5F+sum E_x, K_X^2=-6,
    B=7C0+21F-4 sum_Q E_x-3 sum_T E_x,
    B_i^2=-4, K_X.B_i=2.

The target linear system has class

    D=10C0+34F-4 sum_Q E_x-6 sum_T E_x.

Direct calculation gives

    D^2=16, K_X.D=12, p_a(D)=15, D.B_i=0.

A member not containing B_i is disjoint from it. Contracting the seven disjoint (-4)-curves produces cyclic quotient singularities1/4(1,1), with discrepancy -1/2. Thus, writing pi:X->Y,

    pi^*K_Y=K_X+B/2, K_Y^2=1.

The singularities are rational, so pg(Y)=q(Y)=0. This is the numerical setting of singular Godeaux degenerations, not Campedelli (whose canonical square is2). These numerical facts alone do not prove a Q-Gorenstein smoothing or identify a known family.

## This is not a Coble surface

If -2K_X had an effective representative, its intersection with every B_i would be -4, forcing all seven B_i as components. After subtracting B, its intersection with the nef fiber would be4-7=-3, impossible. Hence |-2K_X| is empty. More generally every antipluricanonical system is empty: an effective -mK_X contains at least ceil(m/2) copies of every B_i, leaving fiber degree2m-7ceil(m/2)<0.

Thus it fails the defining anti-bicanonical-effectivity condition of Coble surfaces. The resemblance between seven disjoint (-4)-curves and a Coble boundary is insufficient and would be misleading here.

## An explicit bicanonical pencil

Set

    L=2K_X+B=3C0+11F-2 sum_Q E_x-sum_T E_x.

Then L.B_i=0, L^2=4, K_X.L=2, chi(O_X(L))=2. In the affine chart, sections are degree-three polynomials in Y with coefficient flags

    deg A_j<=3j+2, j=0..3.

There are30 coefficients, with double-point conditions at the seven quadruple word points (21 equations) and simple conditions at the seven triple points (7 equations). Thus h0(L)>=2 without any computation.

`pencil.py/json` computes these28-by30 matrices for both banks and finds rank28. Their normalized two-vector kernels lift integrally to characteristic zero by a nonzero maximal minor. The two reductions have gcd1 in the affine chart. In addition, the script checks:

* some section has degree exactly3 in Y, so C0 is not fixed;
* the actual maximum coefficient excess deg A_j-3j is2, so the infinity fiber is not fixed;
* at each blown-up point, some section has exactly the imposed order, so no exceptional divisor is fixed.

Consequently the reduced pencil has no fixed component on the proper blown-up surface. This also excludes a characteristic-zero fixed component: its closure in the smooth proper blowup model over the relevant DVR would have a nonempty effective special fiber, contained in the zero divisor of both reduced sections. This argument includes components that could escape the affine chart; that is why the boundary checks are essential. The computation is exact but has not yet received a separate implementation replay.

It follows that L has no fixed component in characteristic zero. A divisor moving in such a pencil is nef: for any curve choose a member not containing it. Since L^2=4, it is also big. Thus K_X+B/2=L/2 is nef and big. The quotient has nef and big canonical divisor; its canonical model, allowing contraction of any additional K-trivial curves, has canonical square1 and pg=q=0. This is a justified numerical-Godeaux connection. Smoothability and an identification with a named published construction remain unproved.

The pencil's generic arithmetic genus is4; its four units of self-intersection may be consumed by base points, including infinitely near ones. No claim that its general normalization has genus4 or that it is already a fibration without further blowups is made.

## What this says about the requested rational member

D descends away from the seven quotient singularities and D.K_Y=12. Riemann--Roch gives chi(O_X(D))=3, matching the verified h0(D)=3; the net is not made unusually large by this numerical calculation. Its arithmetic genus is15. An immersed rational normalization in class D would have normal bundle of degree

    -K_X.D-2=-14,

so it is rigid as an immersed map. The expected dimension of its rational-curve locus is dim|D|-15=-13. These are explanations of why a generic member is not rational, not nonexistence proofs for special members. Cuspidal members require the normal-sheaf torsion to be tracked and are not excluded by the immersion statement.

A concrete geometric coordinate system is now available: the ratio of the two bicanonical-pencil sections defines a rational map to P1. Its intersection with D is L.D=24. A sought rational member would give a degree24 map to this pencil's base after resolving base points and adjusting for any intersections there. This may help eliminate or construct special members, but there is no automatic Cremona or Riemann--Roch operation producing one. Independent work on tangent cones and boundary genus is recorded in the sibling `genus` directory and is not duplicated here.

## Primary literature checked, and identification limits

* I. Dolgachev and D.-Q. Zhang, *Coble Rational Surfaces*, American Journal of Mathematics123 (2001),79--114: https://arxiv.org/abs/math/9909135 . Their definition requires empty anti-canonical and nonempty anti-bicanonical systems; the latter fails here by the elementary argument above.
* S. Coughlan and G. Urzua, *On Z/3-Godeaux surfaces*: https://arxiv.org/abs/1609.02177 . This supplies a genuine nearby literature context: stable degenerations with1/4(1,1) singularities and rational degenerations. It does not identify our seven-singularity configuration, establish its smoothing, or classify rational curves in this norm net.

No primary source located in the bounded search identifies this exact seven-curve configuration as a standard named example. Calling it a Coble, Campedelli, or a known Godeaux surface without these qualifications would overstate the evidence.
