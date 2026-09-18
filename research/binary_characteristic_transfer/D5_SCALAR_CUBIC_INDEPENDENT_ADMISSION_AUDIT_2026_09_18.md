# Independent admission audit of the scalar cubic label theorem

September 18, 2026. **PASS for the scalar theorem in every characteristic.** Independently checked the mathematics in `D5_SCALAR_CUBIC_LABEL_CRITERION_2026_09_18.md`, including the original locator bridge, finite incidence equality, properness, descent, and the conjugate-line converse. No full scattered-set classification is needed.

For E=F_(p^5), theta=1, and labels from all three-dimensional Fp-subspaces,

    z in Fp is missing iff z!=1 and H(z)=z^3+2z^2+3z+1=0.

The full-image statement for p>=37 additionally uses the separately audited published Montanucci--Zanella off-scalar input. That external parameter bound is not silently included in this scalar admission.

## 1. Original-label and dual-incidence checks

The prior `D5_TRACE_DUAL_LOCATOR_INDEPENDENT_AUDIT_2026_09_18.md` proves the signs

    a1=P24/P34, a2=P14/P34,
    z_W=(P24-P23)/P34,

and verifies them for every actual three-space at p=3,5. P34 cannot vanish on an Fp-rational independent two-space. The five conjugate label equations therefore encode exactly the desired original locator fiber, with no rational points lost at a denominator.

After the stated cyclic reindexing their alternating forms are

    ell_j=e_j wedge e_(j+2)-e_j wedge e_(j+1)
          -z e_(j+1) wedge e_(j+2).

The five distance-two exterior coordinates each occur in exactly one form, so the forms are independent for every scalar z and in every characteristic. Frobenius cyclically permutes them. Reversing cyclic indexing only reverses that action and has no effect on the argument.

The primal--dual equality is an elementary incidence identity, not a properness assumption. For q=p write P3=q^3+q^2+q+1, P4=q^4+P3 and G=[5 choose 2]_q=P4(q^2+1). A rank-four alternating form has a one-dimensional radical. Its isotropic two-spaces consist of P3 spaces containing that radical, and q^2 lifts of each of the (q+1)(q^2+1) Lagrangian planes in the symplectic quotient. Thus I4=(q^2+1)P3. A rank-two form has a three-dimensional radical, and its nonisotropic two-spaces are the q^6 graphs onto the symplectic quotient, so I2=G-q^6. Consequently

    I2-I4=q^4, P4 I4=G P3.

Counting incident two-spaces and projective forms in either order gives #C(Fq)=#D(Fq). Alternating forms in odd dimension have even rank, including in characteristic two; all nonzero forms here have rank two or four. The same incidence proof appears in Lu's [September 2026 preprint](https://shunqilu.github.io/publications/classification_maximum_scattered_linear_sets_PG1q5.pdf), Lemma 2.3. Only this explicitly checked finite count is used.

## 2. Properness is verified at every z!=1

I independently reconstructed the matrix from the Hodge-derived original forms and obtained its principal Pfaffians by recursive Pfaffian expansion. Exact symbolic arithmetic over Z[z] reproduced the displayed Jacobian minor (z-1)^2, the tangent direction, tangent residuals, and the three plane-restriction identities. It also separately checked the two Gaussian incidence identities above. The root's replayable integer-identity receipt is `verify_d5_scalar_tangency.py/.json`.

The nonzero Jacobian minor at each vertex gives rank at least three. The displayed nonzero tangent vector, whose third coordinate is 1, gives rank at most three, so the projective tangent dimension is exactly one. Every component of Gr(2,5) intersect P4 has dimension at least one. Thus each vertex is a regular one-dimensional point.

On t0=t1=0, when z!=1, the equations force all three pairwise products among t2,t3,t4 to vanish. The intersection with that plane consists of the three vertices. Every geometric component of dimension at least two would meet the plane, contradicting the one-dimensional local rings there. Hence the section has pure expected support dimension one and Pfaffian height three. The Pfaffian resolution gives Cohen--Macaulayness, degree five, arithmetic genus one, and geometric connectedness, so embedded or isolated extra points cannot be introduced later in the proof.

## 3. Necessity and sufficiency of the cubic

At e0, with v=(0,z+1,1,-z,Q) and Q=z^2+z+1, all tangent polar terms vanish, and the five quadratic evaluations are

    (zH,-H,H,-H,z^2H).

Since the second entry is -H, tangent-line containment is equivalent to H=0 in every characteristic, not merely implied by it.

For necessity, the already proved properness permits the point-free-fiber criterion in `DEGREE_FIVE_PFAFFIAN_POINTLESS_FIBER_CRITERION_2026_09_18.md`: a point-free curve must be a reduced Frobenius-transitive pentagon, so its tangent at any smooth vertex is a contained line. This forces H=0. The root's alternate smooth-orbit proof also checks: the component orbit through e0 has length one or five; in the fixed case it contains five spanning vertices, and Riemann--Roch/Clifford bound its normalization genus by one. A rational normalization point exists by Hasse--Weil and descends to the section, contradicting point-freeness. This is the same scoped argument as Lu Lemma 3.1; no general classification theorem is imported.

For sufficiency, H=0 puts all conjugate tangent lines in the curve scheme-theoretically. The minor of e0,v,e1,shift(v) is -Q. The identity H=(Z+1)Q+Z shows H and Q have no common root over any field. Therefore consecutive conjugate lines are disjoint. The first line is defined over E, so its Frobenius orbit has length one or five; disjointness excludes length one. These five distinct lines exhaust degree five. Cohen--Macaulayness excludes additional isolated or embedded support. A rational point on one component would lie on all its conjugates, contradicting disjointness. Thus the dual section, and by incidence the original locator fiber, has no rational point.

The special label z=1 is indeed attained. The trace map E->Fp is nonzero and has a four-dimensional kernel, even in characteristic five. Any three-space inside that kernel has a locator right-dividing the trace p-polynomial. The monic degree-p composition quotient forces its two leading compiler coefficients to be theta=1 and z=1. Linearized division leaves a remainder of degree at most p^2 vanishing on p^3 roots, so the divisibility is exact. This also handles the scalar root H(1)=0 in characteristic seven without a false missing-label conclusion.

## 4. Admission boundary and resulting ledger

Admit the scalar theorem without restrictions on characteristic. Combined with a separately valid off-scalar coverage theorem for p>=37, it gives exactly E minus the scalar roots of H; H(1)=7 is then nonzero. The cubic is irreducible over Q and has discriminant -23, so its Galois group is S3. Chebotarev gives infinitely many root-free primes (density 1/3), if that standard arithmetic theorem is invoked.

Applying the previously audited internal-padding result at d=5,s=2 then gives, for fixed rho and sufficiently large p, N=p^5, J=floor(rho N), agr_J(g)=CA_J(f,g)=J, at least N-3 guaranteed native bad labels, and agreement threshold at least J+floor((1-rho)p^3/2). Every native label is guaranteed along the root-free prime sequence. This ledger remains over an extension field with p much smaller than J; it is not a both-far, prime-alphabet, first-order-tightness, or better.codes assertion.
