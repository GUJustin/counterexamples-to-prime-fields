# Three scaled cubic covers: independent proof audit

**PASS, with a sign correction.** Let k have characteristic zero or p>3, and let q(X) in k(X) be nonconstant. There are at most two distinct nonzero constants c in k for which

`Y(X)² (Y(X)+1) = c q(X)`

has a rational solution Y in k(X). The nonzero branch value used in the proposed proof is **+4/(27c)**, not its negative. The sign correction does not change the argument or genus.

Extend k to its algebraic closure; this preserves any proposed rational solutions and the nonconstancy of q. For three distinct nonzero constants c_1,c_2,c_3, consider the three covers of the t-line

`f(Y_i)=c_i t`, with `f(Y)=Y²(Y+1)`.

Each is a separable degree-three cover. The derivative is Y(3Y+2). Its branch values are 0, 4/(27c_i), and infinity, with cycle types respectively a transposition, a transposition, and a three-cycle. Thus its Galois closure has group S_3: a transitive group on three letters containing a transposition must be S_3.

## Independence of the three covers

Let L be the compositum of the three Galois closures over k(t). Its Galois group G embeds in S_3³ and projects surjectively onto each factor. At the branch point 4/(27c_i), the other two Galois closures are unramified. Inertia in L is therefore a nontrivial transposition supported only in factor i. Conjugating this element by G gives all transpositions in that factor, because the projection of G onto that S_3 is surjective. These transpositions generate the full isolated S_3 factor. Doing this for all i proves G=S_3³.

This argument does not assume that the same chosen infinity generator conjugates all factors in a prescribed way. It uses only unique branch points and surjective projections. Galois closure does not introduce new branch locations, and all ramification is tame: the group order216 has prime factors only2 and3.

The fiber product of the original cubic covers is consequently connected of degree27. Indeed S_3³ acts transitively on the product of their three-element sheets. Equivalently, the point stabilizer has index3³. Let C be its smooth projective normalization.

## Exact Riemann–Hurwitz computation

At t=0 the inertia order is two and its action is a transposition in each factor. On the27 sheets it fixes one and pairs the remaining26. Its index is13.

At infinity inertia has order three and acts by a three-cycle in each factor. It has nine orbits and index18.

At each of the three separate nonzero branch points, inertia is a transposition in one factor and the identity in the other two. It fixes nine sheets, pairs the remaining18, and has index9. There are no other branch points. Tame Riemann–Hurwitz gives

`2g(C)−2 = −2*27 + 13 + 18 + 3*9 = 4`,

so g(C)=3.

## Obstruction to rational simultaneous solutions

Three rational functions Y_i(X) satisfying the proposed equations would define a nonconstant rational map P¹_X to C, with t=q(X). Nonconstant t makes this map dominant and gives an inclusion k(C) into k(X). Lüroth's theorem forces every such intermediate one-variable function field to be rational, contradicting genus3. This argument also excludes inseparable dominant maps; no separability assumption on q(X) is needed.

The statement controls the number of distinct nonzero labels, not the number of solutions at one label. Each fixed label has at most three rational Y-solutions, so an immediate total bound is six across the nonzero labels. Applying this lemma to a normalized cubic pencil still requires verifying its normalization and that the resulting q is nonconstant; those are separate hypotheses.
