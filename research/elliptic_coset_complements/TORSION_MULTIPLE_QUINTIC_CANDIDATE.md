# A torsion-parameterized quintic candidate for the common-pencil problem

**Status: closed as a superlinear counterexample target.** The arbitrary-label bound in [TORSION_QUINTIC_SUNFLOWER_BOUND.md](TORSION_QUINTIC_SUNFLOWER_BOUND.md) proves at most 2n exceptional challenges for every far-source line using these supports. The proposal and finite test below record how this family was investigated.

Root proposal, 2026-09-19. This is a concrete construction target, not a proximity-gap theorem. The shared affine line and challenge injectivity are unproved. The first prescribed norm-label formula fails the exact finite test recorded below.

Let E be an elliptic curve in odd characteristic with full rational ell-torsion, ell an odd prime larger than 14 and different from the characteristic. For nonzero P in E[ell], the five signed points

    P, [2]P, [6]P, [-4]P, [-5]P

sum to O. Their x-coordinates are distinct: the absolute multipliers are 1,2,4,5,6, and no two are equal up to sign modulo ell. Hence

    J_P(X)=product_{j in {1,2,4,5,6}} (X-x([j]P))

is a squarefree native quintic. The signed-divisor construction places J_P in the norm-quintic family from L(5O). Dependence on P is by multiplication maps of bounded degree independent of ell. This is an explicit elliptic curve of parameters, rather than five arbitrary extra coordinates.

For an order-ell subgroup H, take the two isogeny fiber tags corresponding to [3]phi_H(P) and [7]phi_H(P), with P outside H. For every prime ell>14, the tags are nonzero and distinct up to sign, and neither tag coincides up to sign with any of the five extra-point images. Thus the five extras are outside both selected fibers; the support-count audit proves these exclusions directly.

The intended supports are the union of these two paired fibers and the five extra x-coordinates. P and -P give the same support. There are order ell^2 candidate parameters per H and order ell subgroups. The subsequent independent proof in TORSION_MULTIPLE_QUINTIC_SUPPORT_COUNT_AUDIT.md establishes exactly ell*n distinct complete supports for every prime ell>14, including 6072 at ell=23. This remains a support count, not a distinct-challenge count.

The constructive question is whether the exact norm-quintic Pade equations vanish along this parameter curve for some shared global syndrome pencil with far endpoints. A positive-dimensional incidence component alone does not prove this: the component must contain the displayed torsion points and its challenge projection must give enough distinct labels.

Any bounded linear-algebra test must state its challenge-label ansatz explicitly. A label depending only on phi_H(P) has only order ell possibilities per H and cannot by itself yield a superlinear total in n~ell^2. A useful label must distinguish many points within an H-coset. The current ell23 prime fixture has only 1657 field labels, so its field size itself caps any finite count; an asymptotic argument cannot assume all order ell^3 proposed labels are distinct in that fixture.

No claim of a valid common pencil is made in this note.

## Norm identity and the first concrete label test

Order the signed extras as P,6P,-4P,2P,-5P. Their partial sums are7P,3P,5P, so the Miller expression for u_P has the denominator (x-x(7P))(x-x(3P)). On the quotient curve the same expression uses Q=phi_H(P). With normalized Velu isogeny and u_P=A_2+y(X+b) having leading yx coefficient1, divisor comparison gives

Norm_(phi_H)(u_P)=kappa_H(P) u_Q.

Comparing at O gives kappa=product_(T in H except O)u_P(T). Pairing T and-T and swapping the monic resultant cancels both signs, yielding

kappa_H(P)=product_(j in {1,2,4,5,6}) V_H(x([j]P)),

where V_H is the monic kernel x-locator. This is nonzero for P outside H. Root and Practical independently checked the normalization/sign calculation. The exact norm identity is detailed in TORSION_QUINTIC_NORM_DISTRIBUTION_TARGET.md.

The first bounded test sets lambda=kappa_H(P) and asks whether one pair of syndrome vectors fits the proposed supports. At ell23,n264,k173, the syndrome dimension is91. Each51-point support yields40 recurrence equations, linear in182 unknown source-syndrome entries. Full column rank for a finite collection would reject this label formula on that collection. A kernel would still require independent source directions, enough distinct labels, and far endpoints. Neither outcome by itself settles arbitrary labels or the asymptotic construction.

## Exact finite outcome: the prescribed norm label fails

The verifier in `ell23_fixture/kappa_pencil/verify.py` constructs the actual supports and their monic locator polynomials over F_1657. The first 25 selected supports, with 25 distinct norm labels, give rank 182 in the 182 source-syndrome unknowns. An independently rerun square minor has nonzero determinant. Only six support records are needed for its 182 original rows.

Consequently no nonzero syndrome pair meets all these prescribed support/label constraints; in particular the complete 6072-support bank cannot work with this label formula in this fixture. Any invertible projective reparameterization of the same labels is excluded by the identical calculation after a change of source basis.

This does not exclude a subbank omitting some of these constraints, different labels, a different curve or torsion order, or other moving quintics. The multiplicative norm identity remains true but does not supply the needed additive common-line identity. The subsequent sunflower argument settles arbitrary labels and every subbank: at most 2n exceptional challenges are possible. The proposed larger Plucker test is therefore unnecessary for this family.
