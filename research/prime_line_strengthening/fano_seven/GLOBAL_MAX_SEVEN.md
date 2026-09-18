# Sharp global bound for cubic lists on fourteen coordinates

## Theorem

Over every field of characteristic zero, for every fourteen-point evaluation domain and every received word, at most seven distinct polynomials of degree at most three agree with the word on at least seven coordinates. The bound is attained over a number field, and over arbitrarily large prime fields, by `orbit7_appendix.tex`. The universal upper bound also holds in all but finitely many positive characteristics.

The characteristic-zero statement includes arbitrary algebraic extensions. The finite-characteristic upper-bound assertion is presently “outside a finite set,” not “every odd characteristic.” The three negative incidence cases hold in every characteristic other than two, but the orbit7 classification uses rational polynomial identities whose denominators must be excluded.

## 1. Eight candidates force exact incidence saturation

If at least eight candidates exist, choose eight. Write s_x for their matching multiplicity at coordinate x. Then sum s_x≥56 and

    sum binom(s_x,2) ≤ 3 binom(8,2)=84.

Convexity forces the opposite bound, with equality only when every s_x=4, every candidate has exactly7 matches, and every pair has exactly3 common matches. Thus the fourteen matching sets form a 2-(8,4,3) incidence design.

For completeness, these blocks cannot repeat. Fix one block B. Among the other13 blocks, let j=|B intersect B'|. The design equations give sum j=24 and sum binom(j,2)=12, hence

    sum (j−1)(j−2)/2=1.

Every summand is nonnegative for j=0,...,4, and a repeated block would contribute3.

Delete any one candidate. There are seven triple columns T (the blocks previously containing it) and seven quadruple columns. Let C be the complements of the latter in the remaining seven candidates. Both T and C are three-regular collections of seven triples, and for every candidate pair

    pairMultiplicity_T + pairMultiplicity_C = 2.

Conversely the combinatorial eighth-candidate extension is uniquely determined: append the eighth index to every T triple, and leave every complementary-C quadruple unchanged.

## 2. Exact finite enumeration and the useful deletion table

Enumerate nondecreasing seven-element lists from the35 triples of a seven-element set. Retain those with each vertex degree3 and pair multiplicities at most2; repeated triples are permitted. There are12780 such labelled halves. Encode the21 pair multiplicities in base3. For each half T, the compatible halves C are precisely those with digitwise complementary key. This produces6150 ordered labelled pairs. Quotient by simultaneous S7 relabeling, without swapping T and C: exactly eight orbits result.

This exhaustive algorithm has no heuristic pruning: partial vertex/pair degrees exceeding their final bounds and vertices unable to reach degree3 are the only rejections. `designs.cpp` performs the enumeration. The independently written `independent_design_set.py` verifies literal equality of all6150 labelled pairs with the disjoint union of the eight listed representative orbits, not merely matching counts.

For each of the eight representatives, construct its unique eight-candidate incidence extension and delete each candidate in turn. Exact relabeling gives the following possible deletion types:

| Starting seven-type | All types appearing among its eight deletions |
|---|---|
|0|0,3,6|
|1|1,5|
|2|2,7|
|3|0,3,6|
|4|4|
|5|1,5|
|6|0,3,6|
|7|2,7|

The full ordered deletion table and explicit incidence lists are in `eight_bank_removal_types.py/json`. In particular every hypothetical eight-cubic bank has a seven-cubic subbank of type4,5,6,or7. The separate exclusions of types0,1,3 are therefore unnecessary for this theorem.

## 3. Types4,5,6 are impossible outside characteristic two

These are algebraic exclusions with all coordinate and amplitude exceptions handled, not numerical tests:

- Type4: `OBSTRUCTION.md`. Normalize three quadruple nodes to infinity,0,1. Three dependent-quadratic determinants satisfy E3−E5−E2=2(z−v), contradicting distinctness.
- Type5: `ORBIT5_OBSTRUCTION.md` and `ORBIT5_INDEPENDENT_AUDIT.md`. The complete quadruple-compatible cubic family is parametrized by three amplitudes. After excluding only extra quadruple matches and node collisions, two triple determinants force F_+=F_-=0 with F_+−F_-=2(z−w)l. Here l≠0, giving a contradiction.
- Type6: `ORBIT6_OBSTRUCTION.md`, independently checked by the root agent. The generic amplitude branch creates an extra infinity agreement. The remaining branch u=w/s,v=z/s, s=w+z−1, has determinants forcing A+H=0 and then F3=F4=0, where H≠0. The latter imply (w−z)s=0, contradicting the node guards.

All these arguments work projectively with binary cubics. Every pair already has three distinct prescribed agreement coordinates, so an extra outsider equality at a quadruple is indeed forbidden. The parametrizations are complete for each normalized node configuration, and the exceptional branch in type6 is included.

Consequently an eight-cubic bank must contain a type7 subbank.

## 4. Complete classification of admissible type7 subbanks

Use the ordered incidence lists and the complete three-amplitude family in `ORBIT7_REDUCTION.md`. Normalize the quadruple coordinates to infinity,0,1,u,v,w,z and subtract P1. All node guards u,v,w,z, their differences from1, and pairwise differences are nonzero. The three amplitudes j,k,l are nonzero because candidate1 is outside the respective quadruples.

Dividing pair differences by their two prescribed quadruple roots leaves linear forms. Their common-root determinants, after dividing the explicitly identified nonzero outsider-quadruple factors, give the exact7-by3 linear amplitude matrix in `orbit7_generic.json`. Any realization makes every3-by3 minor vanish.

Minor(0,1,3), up to nonzero guards, factors as

    [(w−1)(z−v)u+vw(w−v)]
    *[(v(w+z−1)−wz)u+wz(1−v)].

The second branch has nonzero denominator (otherwise wz(1−v)=0). Its substituted minors(0,1,2) and(0,3,4) force respectively

    [v(w+z−1)−2wz+z]^2=0,
    [v(w+z−1)−z]^2=0,

contradicting 2z(1−w)≠0. Therefore every realization satisfies

    u=vw(v−w)/[(w−1)(z−v)].                 (I)

The same conclusion applies after any permutation preserving the ordered pair(T,C) and subsequent projective renormalization. `orbit7_symmetry.py` supplies21 such verified permutations and the resulting necessary identities; group completeness is not needed, only validity of each listed permutation. All divided factors are numerators of mandatory node guards after(I), hence nonzero.

Introduce t with t(v−z)(w−1)=1. From the resulting necessary polynomial identities, the explicit rational-identity certificate proves

    (z−1)(w²+w−z)=0,
    (z−1)(wz−2w+z−1)=0,
    (z−1)(v−z+1)=0.                        (II)

Since z≠1, these imply

    z=w²+w, v=z−1, w³+2w²−w−1=0,

and(I) then gives u=w². This is the full admissible node locus, not merely a discovered example. On this cubic locus the first two rows of the amplitude matrix, in columns(j,k), have a nonzero minor equal to

    6w²−2w−2.

It is nonzero by irreducibility of w³+2w²−w−1. This minor and the claimed null vector were independently checked in `global_seven_independent_checks.py/json`. Thus the amplitude matrix has rank2. Scaling j=1 gives uniquely

    k=3w²+4w−5, l=3w²+4w−6.

Consequently every admissible type7 realization is one of the three conjugates of the explicit construction, up to candidate relabeling, a projective coordinate change, a common cubic translation, and nonzero value scaling. All these operations preserve existence of an eighth cubic.

### What the arithmetic certificate verifies

`orbit7_tracked_certificate.py` records each polynomial remainder, S-polynomial, and monic normalization as an explicit rational-polynomial linear combination of prior nodes. The final gzip artifact contains380 nodes. Its input expressions are linked exactly to the previously justified minor and symmetry equations, together with t(v−z)(w−1)−1.

The independent verifier `orbit7_certificate_independent.py` uses sparse dictionaries and Python `fractions.Fraction`, without SymPy. It checks every input against the necessary-equation files and every one of the359 subsequent linear identities, and identifies the three outputs(II) exactly. Thus the proof requires only elementary rational polynomial identities; neither correctness nor completeness of a Groebner implementation is a trusted step. `orbit7_certificate_independent.json` records PASS and the certificate SHA256.

## 5. The classified type7 word cannot admit an eighth cubic

The explicit seven triple nodes and received values appear in `orbit7_appendix.tex`. Their degree-at-most-six interpolant has leading coefficient

    (42w²+81w−30)/8 ≠ 0.

Any eighth cubic would be forced by the equality case in Section1 to agree on precisely these seven triple nodes. Such a cubic does not exist. This holds for all three conjugates, and survives the normalizing equivalences. It contradicts the type7 subbank forced in Section3, proving the universal upper bound.

## 6. Positive characteristic and integration scope

Take the finite union of primes dividing rational denominators in the verified identity DAG and the preceding exact minor/symmetry identities, the denominators in the displayed normalization formulas, and the nonzero integer resultants ensuring that f has no common root with the rank minor and interpolation obstruction. Outside that set (and characteristic2), the same proof works over an algebraic closure of any field. No explicit minimal exceptional-prime set is presently claimed. The positive number-field construction reduces at infinitely many splitting primes, so the global bound is attained over arbitrarily large prime fields.

For paper integration, a bare corollary pointing to an unexplained computation would be insufficient. A compact computer-assisted appendix should include Sections1–2, the three negative-case identities with their complete parametrization references/proofs, the two-branch type7 reduction and(II), and the independent identity-checking algorithm. Approximately4–6 additional pages should suffice if the already-developed Fano case proofs are consolidated rather than repeated. The earlier negative type0/1/3 proofs and the unsuccessful discovery Groebner calculations need not be included in the mathematical dependency chain.
