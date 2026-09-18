# Uniform target-subset second moment: independent audit

2026-09-18. **PASS.** This lemma controls a fixed, distinguished target subset directly; no target translation or averaging over cosets is needed.

Let Γ be a finite abelian group of order M. Let X1,…,Xs be independent samples from a distribution ν with |Eχ(X)|≤ε for every nontrivial character χ, where 0≤ε≤1. Assume 1≤r≤s, and put L=binom(s,r). For z∈Γ let Zz count r-element index subsets whose product is z, and Wz=M Zz/L. Define

    V = (M−1)/L · Σu binom(r,u)binom(s−r,u) ε^(2u)
      + (M−1)(M−2)/L · Σu binom(r,u)binom(s−r,u) ε^(r+u),

where 0≤u≤min(r,s−r), and ε^0=1 even when ε=0. Then, uniformly in z,

    E[(Wz−1)^2] ≤ V.

## Exact Fourier derivation

Write aχ=Eχ(X). Character orthogonality gives

    Wz−1 = L^−1 Σ|S|=r Σχ≠1 χ(z)^−1 ∏i∈S χ(Xi).

Thus the two single-trivial-character terms need not be bounded or estimated: they cancel exactly when subtracting one before squaring. The square is the ordinary real square, since Wz is real. Expanding it without conjugation is legitimate; the character pairs that cancel are ψ=χ^−1.

For ordered supports S,T with |S\T|=|T\S|=u and |S∩T|=r−u, independence makes their character-pair contribution

    χ(z)^−1 ψ(z)^−1 · aχψ^(r−u) aχ^u aψ^u.

There are L binom(r,u)binom(s−r,u) ordered support pairs of this overlap type. Among ordered pairs χ,ψ≠1, exactly M−1 satisfy χψ=1. Their contribution has absolute value at most ε^(2u), including u=0. The other (M−1)(M−2) pairs have χψ≠1 and absolute value at most ε^(r+u). Triangle inequality proves the claimed formula. No character-order hypothesis, prime-order group hypothesis, or reality assumption on individual Fourier means is used.

This bound is a second moment around the uniform mean one; EWz itself need not equal one. The off-diagonal term is precisely what accounts for that lack of uniformity. Dropping it without another argument would generally be invalid.

## Fixed target subset and distinctness

For any fixed B⊂Γ, on the event Zz=0 one has (Wz−1)^2=1. Hence

    E[# {z∈B: Zz=0}] ≤ |B| V.

Now additionally suppose ν is uniform on an actual P-element subset A⊂Γ. If

    a = 1−binom(s,2)/P > 0,

the union bound gives Pr[all Xi distinct]≥a. The missing-target count is nonnegative, so its conditional expectation on this event is at most |B|V/a. Consequently there exists an s-element tag set from A covering at least

    |B| − floor(|B| V/a)

members of B (and in particular at least (1−V/a)|B|). If this expression is negative it is merely vacuous. If |B|V/a<1, every element of B is covered.

The distinctness assertion requires a uniform subset population, or a separately justified collision-probability bound. It does not follow just from a nominal population size if the group elements are sampled with multiplicities or a nonuniform law. The unrestricted iid Fourier-moment statement itself holds for any ν satisfying the stated bias bound.

## Compiler scope

One may take B to be a distinguished multiplicative subgroup, such as the nonzero elements of a subfield, and choose the tag set to retain the stated fraction of precisely those labels. This avoids the loss of meaning caused by replacing B with an arbitrary translated coset. It does not, by itself, verify a norm-pole compiler's signs, the correspondence between products and its scalar labels, its source-distance bounds, or the field of the coefficients. Those remain separate algebraic premises. Nor does this lemma assert that every distinguished label is represented unless the stronger integer inequality above holds.
