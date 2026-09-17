# Quartic persistent singularities: an additional actual-solution condition

No superlinear prime-field counterexample is constructed here. The positive result is a derivative-consistency reduction: a locally squared quartic does not automatically give two usable singular jets. A concrete remaining algebraic identity is isolated below.

Throughout, work in characteristic zero or characteristic greater than four. Algebraic classification is over an algebraically closed constant field; actual finite-field solutions may then be selected from it. This excludes inseparable quartic factors and makes the displayed divisions by two valid.

## 1. Every singular solution satisfies a second equation

LetQ(X,z,u,v) have derivative degree≤4 and letP be an actual polynomial solutionQ(X,z,P,P')=0. Differentiation inX gives

 Q_X(X,z,P,P')+P'Q_u(X,z,P,P')+P''Q_v(X,z,P,P')=0.

At a singular agreement coordinate, Q_v=0. Thus its derivative valuev=P'(x) must satisfy both

 F_x(z,v)=Q(x,z,f_x+zg_x,v)=0,

 S_x(z,v)=Q_X(x,z,f_x+zg_x,v)+vQ_u(x,z,f_x+zg_x,v)=0,

as well as(F_x)_v=0. This uses the partialX derivative of the common equation, not an undefined derivative of the received vector. The challengez is held constant.

IfQ has total jet degree≤B0 and challenge degree≤H0, all coefficient polynomials ofF_x andS_x have z-degree≤h=B0+H0. The degree in v ofS_x is at most5. UnrestrictedX degrees do not invalidate this local identity.

## 2. Persistent two-double-root quartics often reduce to one rational jet

The genuinely two-jet generic quartic case is

 F_x=a4(v²+av+b)²

witha4 nonzero and the quadratic squarefree overF(z). Cases with only one distinct repeated root already have one rational singular jet (uniqueness makes it invariant under algebraic conjugation).

For the two-double-root case, form the explicit scaled quadratic

 R_x(v)=8a4²v²+4a4a3v+(4a4a2−a3²),

wherea_i is the coefficient ofv^i inF_x. This is8a4² times the monic repeated-root quadratic. All its coefficients have z-degree≤2h. Its discriminant is nonzero generically in the two-distinct-root case; the monic discriminant is(3a3²−8a4a2)/(4a4²).

ReduceS_x moduloR_x overF(z). There are three outcomes:

- Nonzero constant remainder: generically neither singular jet is compatible with an actual solution.
- Nonzero linear remainder: at most one compatible jet survives, and it is a rational function ofz.
- Zero remainder: both repeated roots survive first differential consistency. This is the genuine ambiguous core for this step.

For the middle case, a pseudo-remainder obtained by multiplyingS_x by the fourth power of the quadratic leading coefficient has coefficients of degree≤9h. Its root therefore has numerator/denominator degree≤9h. Excluding zeros ofa4, the quadratic discriminant numerator, and the linear remainder's leading coefficient costs at most12h labels per such coordinate. This supplies a concrete bounded-height rational jet to the existing Hermite argument. The nonzero-constant case has a comparable bound from its numerator. No numerical scan is needed for this reduction.

Consequently, mere derivative degreefour is not enough to escape the single-rational-jet theorem: on a positive set of problematic coordinates the repeated quadratic must also divideS_x overF(z). Generic squarefree-factor/subresultant classification can package the other quartic cases; no complete new global theorem with optimized constants is asserted in this note.

## 3. A concrete locally squared model and a degree gate

LetA(X)=product_i(X−x_i), which is squarefree of degreen. Consider

 Q=R(X,z,u,v)²+A(X)S(X,z,u,v),

withR quadratic in the jet variables. This is locally a square at all evaluation coordinates and need not have a repeated global factor. Nevertheless, for every actual polynomial solution,

 A divides R(X,z,P,P')²,

henceA dividesR(X,z,P,P'). Ifdeg_X R(X,z,P,P')<n, this forcesR(X,z,P,P')=0 identically. Thus all such actual solutions already satisfy one common quadratic derivative equation, and the audited quadratic theorem applies whenever its own ordinary-core/signed-margin conditions hold.

A sufficient degree condition isT_R+2D<n, whereT_R bounds theX degree ofR's coefficients anddegP≤D. At degree rateD/n≈1/4, an escape through this model therefore needsT_R at least aboutn/2, or a different structure. The unrestrictedX-degree setting permits this, but the required high-degree identity must actually be supplied.

Moreover at a singular agreement, differentiatingQ givesA'(x)S(x,z,P,P')=0 becauseA(x)=R(x,z,P,P')=0. SinceA is squarefree, S(x,z,P,P')=0. This is exactly the additional prolongation condition above and may eliminate one or both locally available jets.

## 4. A model that defeats the first prolongation, and the missing identity

The strengthened construction

 Q=R²−A²S

makes the first prolongation vanish automatically onA=R=0. It can be globally squarefree even though every evaluation specialization is a square. For an actual solution one still hasA|R(P,P'), so there must exist a polynomialH_P with

 R(X,z,P,P')=A(X)H_P(X),
 S(X,z,P,P')=H_P(X)².

These two identities, simultaneously for a large candidate family, are a precise positive construction target. IfT_R+2D<n they collapse toR(P,P')=S(P,P')=0. At the boundaryT_R+2D≈n, H_P has very small degree; above it, the extra quotient must be controlled. Choosing S independent of the jet variables and nonsquare in the polynomial ring over the chosen constant field produces no solutions, while choosingS as a global square factorsQ into quadratic equations and returns to the solved setting.

Thus a useful quartic counterexample would need a non-globally-squareS that becomes a square along many actual bounded-degree differential graphs, whileR evaluates to the corresponding quotientA·H_P and those graphs generate many full-support bad labels. No such family is established here. The sparse Reynolds bank alone supplies no differential identity of this form.

## Scope and next discriminating lemma

The immediate theorem target is to bound or construct the family of simultaneous solutionsR(P,P')=A H andS(P,P')=H² with bounded-degreeH. The immediate local test is whether the repeated quadratic dividesQ_X+vQ_u after substituting the received value. These are concrete derivative-consistency requirements beyond the naive two-valued Hermite list-recovery count. They do not prove a universal quartic linear bound and do not assert a prime-field lower bound.
