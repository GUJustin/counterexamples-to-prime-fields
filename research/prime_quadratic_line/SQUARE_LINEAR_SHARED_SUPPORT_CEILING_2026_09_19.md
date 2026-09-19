# Square-linear witnesses with arbitrary shared fresh supports

September 19, 2026. A scoped consequence of Stevens--de Zeeuw's existing
point-line theorem, derived in a bounded construction audit. No construction,
manuscript edit, computation, or literature-novelty claim.

The existing square-linear block theorem has `n=128t^2+1`, common and
endpoint agreement `A=14t`, tested agreement `T=16t`, and `t^2+1`
successful labels. Its disjoint-block resource proof gives only a linear
count. The result below allows arbitrary shared fresh supports and counts
every square-linear witness, including ones outside the named bank.
It gives `O(n^(11/8))` labels when `T-A=Omega(sqrt(n))`, over any field
of characteristic zero or characteristic at least the domain length.
Thus this entire proportional-fresh-word square-linear architecture cannot
retain the strongest existing `n^(3/2)` exceptional exponent at a constant
loss-to-capacity-margin ratio. It does NOT exclude every superlinear count.

## 1. Statement

Let `D subset F` have `n` distinct coordinates, where `F` has
characteristic zero, or odd prime characteristic `p` with `n<=p`.
Let the message polynomials have degree at most two. Write

    A = CA_3(f,g), T>A, d=T-A.

Suppose there are a fixed quadratic `H` and scalar `c` such that

    f(x)-H(x)=c g(x)  whenever g(x)!=0.                 (1)

There is no restriction on `f` where `g=0`, and no restriction on the
nonzero values of `g`. In particular, fresh supports may overlap in any
way; no partition into blocks, uniform block sizes, or fixed bank is assumed.

Count labels having a degree-at-most-two witness of the form

    Q=H+R,  R=u(aX+b)^2, u in F^*, a,b in F,            (2)

and also permit `R=0`. The representation is not counted: witnesses are
distinct polynomials. These are all scalar multiples of squared linear
polynomials, including constant polynomials, after the one common
translation `H`.

For every fixed `delta>0`, if `d>=delta sqrt(n)`, the number of counted
labels is

    B = O_delta(n^(11/8)) + 1.                        (3)

The possible extra label is `lambda=-c`. All constants are independent
of the field, the words, the support geometry, and the number of different
representations of a scalar-square polynomial.

This bounds ALL qualifying witnesses in (2); singleton lists are not
required. It bounds the entire exceptional population only if every
qualifying witness belongs to this translated cone. Arbitrary quadratics
outside (2) are not covered.

## 2. A large-characteristic square-linear list bound

Fix a word `v` on at most `n` coordinates of `F`, and let `L` distinct
nonzero scalar-square polynomials have at least `delta sqrt(n)` matches
to that word. Then

    L=O_delta(n^(7/8)).                                (4)

Work in an algebraic closure `K` of `F`. Choose one of the two signed
linear square roots `L_R` of each nonzero polynomial `R`; these exist
because the scalar `u` has a square root in `K`. Distinct polynomials
give distinct affine lines

    Y=L_R(X).

Use the planar point set

    P={(x,y) in K^2: x is a word coordinate, y^2=v(x)}.

There are at most `2n` points. Every polynomial agreement gives precisely
one incidence of its selected line with this point set. Choosing both
square roots in the POINT set avoids a loss from independently chosen
signs. Zero word values give one point, which causes no difficulty.

Pad the point set to exactly `N=2n` distinct points of `K^2`; this is
always possible. Padding cannot reduce richness. For the remainder of
this incidence calculation write `J` for the number of selected lines.

Stevens--de Zeeuw, Theorem 3, states

    I(P,L) << N^(11/15) J^(11/15)

when `N^(7/8)<J<N^(8/7)` and, in positive characteristic,
`N^(-2)J^13 << p^15`. The theorem permits the extension field `K`;
its restriction involves characteristic, not field cardinality.
If `J>=N`, take exactly `N` lines. They would give

    delta sqrt(n) N <= I << N^(22/15),

which is impossible for all sufficiently large `n`, depending only on
`delta`. In positive characteristic the condition has ample slack:
`N^11<=2^11 p^11=o(p^15)`.
In characteristic zero there is no characteristic condition.
Consequently `J<N` for sufficiently large `n`.

If `J<=N^(7/8)`, (4) follows immediately. Otherwise Theorem 3 applies
with the actual `J`, again with `N^(-2)J^13<N^11` when needed, and gives

    delta sqrt(n) J << N^(11/15) J^(11/15),
    J <<_delta N^(11/4) n^(-15/8)=O_delta(n^(7/8)).

There is one selected line per polynomial, so this proves (4) for sufficiently large
`n`, depending only on `delta`, which is the range used below. For bounded
`n`, a requirement of only one or two agreements would not bound the
square-linear list independently of `p`; no such small-agreement list
bound is asserted.

Primary source checked directly on September 19, 2026:
Sophie Stevens and Frank de Zeeuw, *An Improved Point-Line Incidence
Bound Over Arbitrary Fields*, Theorem 3, page 2, arXiv v4 (2017),
[primary PDF](https://arxiv.org/pdf/1609.06284).
Only that incidence theorem is external; (4) is its elementary
square-root application. In positive characteristic the `n<=p`
hypothesis supplies the characteristic-size check used here. Passing
to the algebraic closure changes neither characteristic nor the number
of points and lines; no prime-alphabet or finite-field square-class
assumption is used in this strengthened proof.

## 3. Richness is forced on both sides

Subtract `H` from the intercept and change the label to `mu=lambda+c`.
This preserves common agreement and maps the witness `Q` to `R`.
The resulting pencil is

    w_mu=h+mu g,
    E={x:g(x)!=0}, Z=D minus E,
    h=0 on E, g=0 on Z.

Fix `mu!=0` and a qualifying nonzero `R` from (2). Define its actual
matching counts

    r_Z=|{x in Z:h(x)=R(x)}|,
    r_E=|{x in E:mu g(x)=R(x)}|.

Each count is at most `A`:

* `(R,0)` simultaneously explains `h,g` at every counted point of `Z`.
* `(0,R/mu)` simultaneously explains `h,g` at every counted point of `E`.

Since `r_Z+r_E>=T=A+d`, BOTH `r_Z` and `r_E` are at least `d`.
This is the feature missing from a generic fixed-bank budget: all
successful square-linear witnesses automatically lie in a rich list
around the single core word `h|Z`. It is not necessary to assume that
the named bank exhausts the rich core in advance.

By (4), the collection `R_core` of all such nonzero polynomials has

    |R_core|=O_delta(n^(7/8)).

For each fixed `R` and each `x in E`, the agreement equation determines
at most one label, namely `mu=R(x)/g(x)`. Therefore the number of
nonzero labels at which this `R` has at least `d` fresh matches is at
most `|E|/d`. Summing over the complete core list gives

    B_nonzero d <= |R_core| |E|,
    B_nonzero = O_delta(n^(11/8)).

Different witnesses for one label only increase the right-hand count,
so this is a bound on distinct labels, without any uniqueness premise.
At `mu!=0`, `R=0` has no matches in `E` and at most `A` in `Z`, so it
cannot qualify. The excluded `mu=0` contributes at most one further
label, proving (3).

For completeness, bounded `n` can be absorbed into (3) without invoking
an invalid one- or two-agreement list bound. Every successful quadratic
has at least four matches, since `CA>=3` for `n>=3`. Choose three of its
matching coordinates. Interpolating the received pencil there gives a
unique affine polynomial trajectory `F+mu G`. If all other matches were
persistent on this trajectory, its simultaneous explaining pair would
give `CA>=T`, a contradiction. Thus some fourth coordinate imposes a
nonconstant affine equation on `mu`, determining it uniquely. There are
at most `binom(n,3)(n-3)` such choices. This elementary field-independent
bound handles all bounded `n`; when `n<4`, `T>CA` is impossible.

## 4. What the result changes, and what it leaves open

For the existing square-linear parameters,

    n=128t^2+1, A=14t, T=16t, d=2t,

the bound is `O(t^(11/4))` labels. It permits growth above the existing
`t^2+1` labels, but excludes a `Theta(t^3)` upgrade by arbitrary shared
fresh-coordinate reuse while retaining proportional fresh words and
translated scalar-square witnesses.

In particular the prime-field corollary is unchanged. The same bound
now also holds on domains of length `n<=p` over extensions of the prime
field. Increasing the alphabet extension degree alone does not avoid
this obstruction. The implicit constants and onset do not give a
numerical security estimate for any particular finite parameter choice.

This is stronger in scope than the disjoint-block resource inequality:
`g` may vary arbitrarily, witnesses can match several overlapping support
sets, scalar rays can be arbitrarily populated, and nonbank rank-one
witnesses are all included. It differs from the old proportional-word
conic bound because the fresh point-line reduction can have unbounded
scalar multiplicity. The proof instead applies point-line incidence to
the CORE, where distinct quadratic witnesses yield distinct lines after
choosing square roots.

A fixed number of different common translations `H` can be handled by
summing (3), provided (1) holds for each translated family being counted.
No claim follows for a growing number of translations, unrestricted
quadratic witnesses, nonproportional fresh values, or witnesses whose
core agreement is not forced by the two simultaneous explanations.

Individual-source separation also entails the used CA bound: if both
chosen endpoint agreements are at most `A_src<T`, their common agreement
is at most `A_src`. Thus `d>=T-A_src`, and a source loss comparable to
the dimension-three capacity-margin scale `Theta(sqrt(n))` activates
this bound. No new endpoint profile, global list classification, or
positive counterexample is asserted.
