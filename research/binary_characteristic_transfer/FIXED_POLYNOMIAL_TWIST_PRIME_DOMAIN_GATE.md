# Fixed polynomial twists on prime-field domains

September 19, 2026. Exact algebraic gate; no scan or manuscript edit.

Let D be a set of n distinct points of Fp, with 0<n<p, and let
Λ=∏_{x∈D}(X−x). Fix any polynomial A over a containing field E.
This note concerns the exact polynomial identity

    G^p − A G = Λ F^p.                                      (1)

The twist A is shared by the family. Allowing A to depend arbitrarily
on G makes (1) tautological and is outside this conclusion.

## 1. Prime-field coefficient solution space

For an integer 0≤g0<n, let S_A(g0) be the set of G∈Fp[X] of degree
at most g0 for which (1) holds for some F∈E[X], allowing F=0.
It is an Fp-linear space: the pth-power map is additive and the
corresponding F is unique.

**Proposition.** Its dimension is at most two. If it has two distinct
nonzero degrees g>h, then

    deg A = (p−1)g,   lc(A)=1,   h=g+n−p.                    (2)

Consequently dim S_A(g0)≤1 whenever g0<p−n. In particular
p≥2n implies dim S_A(g0)≤1 for every g0<n.

**Proof.** The case A=0 has no nonzero solution, because a nonzero
right side has degree n modulo p, whereas deg(G^p) is zero modulo p.
Suppose a=deg A and e=deg G. If a<(p−1)e, the same comparison
rules out a nonzero right side; a zero right side is also impossible.
If a>(p−1)e, the left side has degree a+e, so

    e ≡ n−a (mod p).                                       (3)

There is at most one such degree in [0,g0], because g0<p.
The only remaining possibility is a=(p−1)e. Cancellation of the
leading terms is necessary, and because G has coefficients in Fp
it requires lc(A)=1. This gives at most one additional degree
g=a/(p−1). A nonzero solution with F=0 also has precisely this
degree and leading coefficient condition.

An Fp-linear polynomial space has dimension at most the number of
degrees appearing among its nonzero elements: elimination of leading
coefficients gives a basis of distinct degrees. Thus its dimension
is at most two. If both degrees g>h occur, (3) gives h≡n+g mod p.
The inequalities 0≤h<g<n<p force h=n+g−p, proving (2).
If g≤g0<p−n, this is negative and impossible. ∎

This argument does not bound deg A and does not assume A∈Fp[X].
It also does not assume the solutions split over Fp.

## 2. Scaled native locators

Suppose instead that each G_i=γ_i V_i, where γ_i∈E* and V_i is
a monic divisor of Λ of degree at most g0. Assume 2g0<n, so the
complements of every two root sets intersect. At a point x in such
an intersection, (1) gives

    A(x)=γ_i^(p−1)=γ_j^(p−1),

because V_i(x),V_j(x) are nonzero elements of Fp. Hence
γ_i/γ_j∈Fp*. Divide the entire family by one fixed γ and replace
A by Aγ^(1−p). All resulting G_i have prime-field coefficients
and lie in the space in Section 1.

Thus if also g0<p−n, there is at most one projective locator and
one root set in such a family. In particular this applies whenever
p≥2n and the regular-level locators omit fewer than half the
coordinates. It is directly applicable to the named short NTT
length n=262144 in the large prime characteristics considered in
this project. This is a restriction on a shared-twist compiler,
not a theorem about arbitrary received lines.

If the family is normalized monic from the start, the condition
2g0<n is unnecessary.

## 3. Low-degree twists

There is an even simpler obstruction if deg A<n<p: no identity (1)
with F≠0 is possible, for any polynomial G of any degree or
coefficient field. For deg G=e≥1, the inequality
deg A<p−1≤(p−1)e makes G^p the unique leading term, forcing p|n.
For e=0 the left side has degree below n. Neither case permits
a nonzero right side. This needs no extra residual-degree hypothesis.

## 4. Independent check of the monomial subgroup case

Let D=μ_n⊂Fp*, write p−1=un, and suppose u≥2. For q≥0, consider
A=X^(qn), deg G<n, and F≠0. Reduction modulo X^n−1 forces G
to have coefficients in Fp. For a nonzero coefficient at X^i,
the quotient of X^(pi)−X^(i+qn) by X^n−1 is a geometric chain
of length |ui−q|, supported on exponents congruent to i modulo n.
Chains for different i cannot cancel each other.

A pth-power polynomial can have only exponents divisible by p.
Since p is coprime to n, a chain of length at least two is impossible.
The length-one case q=ui−1 has exponent pi−n and is impossible;
q=ui+1 gives the permissible monomial −X^(pi). The case q=ui
contributes zero. If a nonzero chain occurs and u≥2, no canceled
index can coexist with it. Thus G is a single monomial, with no
nonzero native roots. In particular no nonconstant split locator
dividing X^n−1 works.

For u=1, a neighboring canceled term may coexist, giving a
monomial times a linear polynomial; this is the full-Fp* edge case.
The general shared-twist proposition above is stronger when p≥2n.

## 5. What remains open

A varying twist A_i can escape the fixed-space bound. It must still
satisfy the shared received-head condition, not merely (1). For
Q_i=Λ/G_i and residual P_i=F_i Q_i, the exact equation is

    P_i^p + A_i Q_i^(p−1) = Λ^(p−1).                        (4)

Thus a proposed low-dimensional family A_i must make the high-degree
part of A_i Q_i^(p−1) equal to a fixed pth-power head, or to an
affine pencil of such heads, while preserving the native split
condition G_i|Λ. No such new family is supplied by the fixed-twist
argument. The unrestricted definition
A_i=G_i^(p−1)−Q_i F_i^p is only a rearrangement of (4), not a
constructor.

