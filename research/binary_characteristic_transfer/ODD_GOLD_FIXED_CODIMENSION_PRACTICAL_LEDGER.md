# Exact Gold kernel versus fixed-codimension practical domains

Bounded independent audit, 2026-09-19. Read-only primary source: binary_field_counterexamples/sections/constructions/fullfield-elliptic.tex, cor:elliptic-fixed-codimension and its odd-ambient proof. This is a scope and uniform-parameter ledger for these particular compilers, not a general impossibility theorem.

## 1. What the primary corollary actually quantifies

Its base p, codimension h, and challenge extension j are fixed before ambient dimension m tends to infinity. It assumes j≥1, and j≥2 when h=0. Its unspecified sufficiently-large-m onset and constants may depend on p,h,j. They cannot be applied directly to m=4 or 5 while p is billions.

Write m=2v+1 and a=j+h (renaming the primary proof’s auxiliary s). The constructed quadratic rank is m−2a=2t+1 with t=v−a. The prescribed additive domain has dimension m−h and length N=p^(m−h). The construction uses a-spaces W containing the h-space U, so a≥h. For a fixed W the odd-characteristic parameter condition has at most C=binom(a+1,2) quadratic equations over Fp. The proof’s indicator product has degree at most 2(p−1)C=(p−1)a(a+1). Its explicit elementary support argument therefore only certifies at least

    p^[m−(p−1)a(a+1)]−1

nonzero scaling parameters, before the two-to-one conversion to quadratic coefficients. To get a positive bound from this particular estimate requires m>(p−1)a(a+1). This is a sufficient certificate, not a necessary condition for the equations to have nonzero solutions. No actual nonexistence follows merely when the bound becomes vacuous.

An explicit uniform form count furnished by the same argument is at least

    ([m−h choose a−h]_p / [2a−h choose a−h]_p)
    · (p^[m−(p−1)a(a+1)]−1)/2,

whenever the final factor is positive and the rank/dimension conditions hold. Translation and half-level selection can then be applied as in the source. This spells out the dependence hidden by its fixed-p Ω notation; it does not improve that estimate.

## 2. Exact method’s domain and field requirements

All these fixed-codimension quotients use an Fp-linear evaluation domain D. Every nontrivial such domain has cardinality p^d≥p. An affine translate has the same size. The practical prescribed length 262144 is less than BabyBear p=2013265921, M31 p=2147483647, and Goldilocks p=2^64−2^32+1. Therefore it cannot be the whole nontrivial additive domain required by this quotient construction. Moreover 262144 is not a power of any of these odd primes. A further arbitrary puncturing would be a new step: the present full-domain level counts and locator differential identity do not automatically survive it.

For the exact above-first-order full-field families now proved, even trace–norm needs native degree 2s≥4 and an exterior pole in an extension of relative degree at least two; its alphabet therefore has prime-field degree at least eight. Odd Gold needs native degree 2s+1≥5; its quadratic kernel theorem needs alphabet degree at least ten, and the cubic singleton theorem at least fifteen. In a proposed alphabet F_(p^e), native subfield degree m must divide e, and an exterior pole requires e/m≥2. Thus degree-two Goldilocks and degree-four/five BabyBear or M31 cannot host these exact above-first-order towers. Degree five can contain the native degree-five Gold field, but has no exterior pole over it. The existing degree-four Hermitian s=1 family is a different, below-first-order case on a p²-sized native domain.

These tower bounds are for the actual exact theorems, not a prohibition against another compiler over the same fields. In particular, proper-domain constructions can put poles in the ambient field outside D rather than outside B; they do not inherit the current B₂/B₃ kernel proof for free.

## 3. Why the one-dimensional evaluation kernel is not yet a pullback theorem

The exact Gold proof uses two special full-field facts: Λ=X^(p^m)−X, and the p^s-th root of the derivative is the two-term operator a^(p^(s+1))X+a^pX^p. This operator has a one-dimensional geometric kernel, every nonnative critical root is in B₂, and evaluation on the Gold-plus-linear-trace space consequently has exactly a one-dimensional kernel at a quadratic exterior pole.

After radical creation and quotienting by an h-space, the primary proof only guarantees derivative Frobenius indices in [t,m−h−t]. Their width is m−h−2t=2a+1−h. It can exceed one. Therefore its reduced linearized derivative may have degree as large as p^(2a+1−h), and neither a one-dimensional evaluation kernel nor quadratic splitting follows from the former two-term argument. Proving a kernel bound for that larger family is a separate algebraic problem; simply substituting the shorter domain length into the full-field theorem is invalid.

For the same odd-rank large-level placement mechanism, rank at least five is the established above-first-order regime. Within this particular radical pullback, m−2a≥5 and a≥h imply m≥2h+5, hence native domain dimension m−h≥h+5. Thus introducing positive codimension does not create a dimension-two/three instance of the proved high-rank mechanism. This rank ledger does not rule out a different low-dimensional identity, which the parallel audit is checking separately.

## 4. Concrete bounded next test and priority

A mathematically well-defined extension test is to compute the evaluation-kernel dimension for the descended trace-form coefficient space, using the actual additive locator and derivative indices above, before counting supports or renting computation. Success would require a bound uniform in p and sufficiently small to retain more than linear labels, together with the same strict-degree source and threshold inequalities. It would extend the theorem to additive domains; it would still not solve the named short multiplicative-domain task because N≥p remains.

For the named fields and prescribed length, this exact additive-pullback route therefore has no presently valid numerical instance to test. A useful positive bridge must first produce a nonadditive-domain locator/compiler identity, or a proved puncturing mechanism preserving the bank at n<p. The quadratic-kernel improvement alone supplies neither. No field or curve scan is justified by the current ledger.

## 5. Exact arbitrary-domain gate for the untwisted Frobenius identity

Let K be any field of characteristic p, let D be a nonempty set of n distinct elements in a containing field, and work over a field containing D. Write Λ_D=∏_(x∈D)(X−x). Suppose polynomial G and nonzero polynomial F satisfy the exact identity

    G^p−G=Λ_D F^p.

Then G is nonconstant: a constant left side cannot have the positive degree of the nonzero right side. Put g=degG and f=degF. Leading degrees give

    pg=n+pf.

In particular p divides n. This necessity holds WITHOUT the extra hypothesis degG<n. It already excludes every nonempty domain of size n<p and every power-of-two domain in odd characteristic, irrespective of whether its elements lie in the prime field or an extension.

The domain locator is squarefree, so Λ_D′≠0. Differentiation yields

    −G′=Λ_D′ F^p,
    degΛ_D′+pf=degG′≤g−1.

In particular G′≠0, and combining the two degree relations gives the stronger coefficient-support constraint

    degΛ_D′≤n−(p−1)g−1≤n/p−1.

The original simpler argument is also valid: if p does not divide n, then degΛ_D′=n−1, which contradicts the derivative bound whenever degG<n. The leading-degree argument shows that the divisibility obstruction does not actually require that degree restriction.

This is a necessary-condition theorem only for the exact untwisted polynomial identity displayed above, with F≠0. It does not rule out rational identities, identities only modulo the domain locator, a nonconstant multiplier in G^p−uG, or a different compiler. In particular it is not a theorem about arbitrary received pencils or prime-alphabet counterexamples. The natural next algebraic escape is a genuinely modified identity, not replacement of X^(p^m)−X by the desired NTT locator in the same formula.
