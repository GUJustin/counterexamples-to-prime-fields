# Exact scalar criterion for the five-dimensional locator labels

September 18, 2026. Root proof, independently admitted in D5_SCALAR_CUBIC_INDEPENDENT_ADMISSION_AUDIT_2026_09_18.md. The polynomial identities pass `verify_d5_scalar_tangency.py`. No new classification theorem for scattered linear sets is assumed.

Fix a prime p, E=Fp^5, theta=1, and the canonical labels from all three-dimensional Fp subspaces W of E. Write

    L_W=X^(p³)+a1 X^(p²)+a2 X^p+a3 X,
    z_W=a1+a2^p-a1^(p+1),
    H(Z)=Z³+2Z²+3Z+1.

**Scalar theorem.** For z in Fp, z is absent from this label image if and only if z!=1 and H(z)=0. This statement holds in every characteristic. The properness and tangent computations below use integer polynomial identities and divisions only by z−1. The special point z=1 is attained by any three-space in the kernel of the trace E→Fp: on that space the trace polynomial gives the compiler identity with label1.

## Exact compiler and dual-section bridge

Let U=W-perp for the nondegenerate trace pairing. For a basis x,y of U, set Pij=x^(p^i)y^(p^j)-x^(p^j)y^(p^i). Complementary Moore minors give a1=P24/P34 and a2=P14/P34. The Plucker relation then gives

    z_W=(P24-P23)/P34.

P34 is nonzero at every rational two-space. Frobenius conjugation supplies five linear equations on the descended Grassmannian Gr(2,5). Their dual alternating forms, after cyclic reindexing, are

    ell_j=e_j wedge e_(j+2) - e_j wedge e_(j+1)
          - z e_(j+1) wedge e_(j+2),  j mod5.

These forms are linearly independent: each diagonal coordinate e_j wedge e_(j+2) occurs in just one form. The primal section C has Fp points exactly when z is an attained compiler label. Put A=span(ell_0,...,ell_4) and D=Gr(2,V*) intersect P(A).

The equality #C(Fp)=#D(Fp) does not require properness. Here is the finite incidence proof, also appearing as Lu Lemma2.3. Write G=#Gr(2,5)(Fp), Pj=#P^j(Fp). Count pairs (U,[omega]) with omega vanishing on U. Projection to U gives GP3+p^4#C. A rank-four alternating form vanishes on I4=P3+p²(p+1)(p²+1) two-spaces; a rank-two form on I2=G−p^6. Direct Gaussian arithmetic gives I2−I4=p^4 and P4 I4=G P3. Since rank-two forms in P(A) are precisely D, projection to omega gives GP3+p^4#D. Equality proves the claim. This argument is valid also in characteristic two.

## Exact properness and tangency

Use coordinates t0,...,t4 on P(A), and let the alternating matrix be M=sum_j t_j ell_j. Its five principal four-by-four Pfaffians, with the increasing-index sign convention, are recorded in the verifier JSON. Each coordinate vertex belongs to D, and Frobenius cyclically permutes them. At e0, the Jacobian in t1,...,t4 is

    [ 0,    z²,    z,     0 ]
    [ 0,    -z,   -1,     0 ]
    [ 0,     z,    1,     0 ]
    [ 0,    -1,  -z²,   1-z ]
    [ z-1,   1,    z,     0 ].

Rows 1,3,4 and columns 0,2,3 (zero-based) have determinant (z−1)². Thus for z!=1 the tangent space at every vertex has projective dimension one. On the plane t0=t1=0, the Pfaffians generate set-theoretically

    t2*t4=0, (1-z)*t2*t3=0, (z-1)*t3*t4=0.

Their zero set consists of the three coordinate vertices. Every geometric component of the Grassmannian section has dimension at least one. A component of dimension at least two would meet this plane by projective dimension, but every such intersection vertex has local dimension one, a contradiction. Therefore D is a proper curve, its Pfaffian ideal has height three, and the vertices are smooth.

The height-three Pfaffian resolution

    0 → R(-5) → R(-3)^5 → R(-2)^5 → R → R/I → 0

gives a pure Cohen–Macaulay degree-five arithmetic-genus-one curve. It also gives geometric connectedness. These are exactly the hypotheses checked in the companion point-free-fiber criterion. No generic-fiber or unverified smoothness claim is used.

At e0 take the polynomial tangent direction

    v=(0,z+1,1,-z,Q),  Q=z²+z+1.

The five Pfaffians at v are exactly

    (z H, -H, H, -H, z² H).

The linear terms at e0 vanish by the tangent equations. Thus its tangent line is contained in D if and only if H(z)=0.

If D has no Fp point, the smooth point e0 lies on a unique geometric component. Frobenius^5 fixes e0, so the component orbit has length one or five. In the latter case degree five forces the components to be lines, and the tangent line is contained in D. In the former case that component contains all five spanning vertices. Its normalization has genus at most one: its degree is4 or5 and it has at least five independent sections of O(1), so Riemann–Roch and Clifford exclude higher genus. Hasse–Weil then gives an Fp point, a contradiction. Consequently point-freeness forces H(z)=0. This is the independently checked smooth-orbit argument in Lu Lemma3.1; the companion broader component criterion gives the same implication.

Conversely suppose H(z)=0 and z!=1. All five conjugate tangent lines are contained in D. The four-column minor of e0,v,e1,Frob(v) on rows0,1,2,3 equals −Q. Since H mod Q=Z, H and Q have no common root, so this minor is nonzero. Hence the first line and its Frobenius image are disjoint. Its Frobenius orbit has length five (it is defined over E), and the five lines exhaust the degree-five curve. Purity excludes extra isolated points. An Fp point on any component would lie on all five conjugates, contradicting the disjointness. Thus D, and therefore C, has no Fp point. This proves the scalar theorem.

## Consequence after the separately audited off-scalar input

Published Montanucci–Zanella Proposition4.3 / Theorem5.5 supplies the off-scalar exclusion of scattered L_(z,1) for p>=37. The exact Hodge/scattered bridge and those primary hypotheses are recorded separately in `D5_PLUCKER_SCATTERED_COMPILER_BRIDGE_2026_09_18.md` and the literature audit. Combining THAT INPUT with the scalar theorem gives the following admitted statement:

    for p>=37, image(z_W)=E minus {z in Fp : H(z)=0}.

Here H(1)=7, so z1 is not a root for p>=37. At most three labels are missing. In particular, every label occurs whenever H has no root modp.

Over Q, H is irreducible by the rational-root test and has discriminant−23. Its Galois group is S3. Chebotarev therefore supplies a density1/3 set of primes where H is irreducible modp, hence root-free. Only infinitude is needed for the counterexample. Alternatively the all-label statement can be left conditional on the explicit root-free prime test, without stating a density.

Use the previously audited internal-padding theorem at d=5,s=2 and theta=1. For every fixed rate rho and sufficiently large p, it preserves all canonical labels and gives N=p^5, J=floor(rho N), agr_J(g)=CA_J(f,g)=J, and threshold at least J+floor((1-rho)p³/2). Thus the admitted theorem has at least N−3 bad native labels for every sufficiently large p, and ALL N on the infinite root-free prime sequence. Characteristic is N^(1/5), absolute gap Theta_rho(N^(3/5)), and normalized gap Theta_rho(N^(-2/5)).

This strengthens the existing extension-field transfer; p remains far smaller than J. Native all-label coverage includes zero, so the first source is near. It supplies no prime-alphabet DKT tightness or better.codes improvement. The mathematical geometry is related to existing scattered-linear-set work and is not claimed as a new classification method.

## Sources and validation

- Published Montanucci–Zanella, *A class of linear sets in PG(1,q^5)*, Finite Fields Appl.78 (2022), 101983, https://doi.org/10.1016/j.ffa.2021.101983. Parameter-specific input requires the separate audit.
- Lu, September2026 preprint, https://shunqilu.github.io/publications/classification_maximum_scattered_linear_sets_PG1q5.pdf, Lemmas2.3 and3.1–3.3. Only the explicitly replayed incidence/tangent arguments are used, not its full classification.
- Exact integer identities: `verify_d5_scalar_tangency.py/.json`.
- Direct finite examples: `check_d5_theta_one.py/.json`, independently checked against actual three-space locators for p3,p5 in the separate locator audit.
