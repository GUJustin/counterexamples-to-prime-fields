# Small prime-field graph lifts: what the inspected incidence theorems imply

2026-09-19. Bounded primary-theorem check, not an exhaustive literature
classification. No new upper bound or computation is claimed.

**Outcome.** The lifted quadratic graph has no three collinear points, but
the inspected prime-field point-plane theorems still permit incidence order
`n^(3/2)` in the balanced case. They therefore do not prove a sublinear
maximum list at agreement `T=c sqrt(n)`, even when `n<p` and
`sqrt(3/2)<c<sqrt(2)`. In particular an unspecified constant in `O(...)`
cannot be compared with either of those threshold constants.

## 1. Exact RS incidence model

Let `D subset Fp` have `n<p` distinct elements and let `f:D->Fp` be any
received word. Lift its graph to

    P = {(x,x^2,f(x)) : x in D} subset Fp^3.

A quadratic `q(X)=aX^2+bX+c` corresponds to the plane

    Pi_q: Z=aY+bX+c.

Distinct polynomials give distinct planes, and incidences are exactly
agreements. A bank of `L` quadratics with agreement at least `T` gives

    I(P,{Pi_q}) >= L T.                                    (1)

No three points of `P` are collinear. Indeed their projection onto the
first two coordinates lies on `Y=X^2`; three distinct projected points
are noncollinear by the Vandermonde determinant. A spatial line cannot
project to a point containing two such coordinates either.
Consequently two distinct planes share at most two points of `P`, and
the incidence graph is `K_(3,2)`-free, in particular `K_(3,3)`-free.

## 2. Rudnev: the small-field-size hypothesis is already satisfied

Rudnev's Theorem 3, in its dual form, states that for `n` points and
`L>=n` planes in odd characteristic, with `n=O(p^2)` and maximum point
collinearity `k_col`,

    I = O(L sqrt(n)+k_col L).

Here `k_col=2` and the characteristic condition follows from `n<p`.
It yields only `T=O(sqrt(n))` after (1); it gives no upper bound on `L`
at a fixed square-root threshold. The stronger assumption `n<p` does
not insert an extra saving into the displayed theorem.
[Rudnev, Theorem 3, arXiv:1407.0426v5](https://arxiv.org/pdf/1407.0426v5).

In particular, `T>sqrt(3n/2)` does not contradict this result, and its
implicit constant is not one. The theorem also does not assert that its
constant can be decreased using the parabolic-cylinder condition.

## 3. Two other general results do not supply the missing saving

**Forbidden-subgraph method.** Milojevic, Sudakov and Tomon prove a
point-hyperplane bound over arbitrary fields. Their balanced Theorem 1.1
at dimension three, with fixed forbidden `K_(s,s)`, has exponent `3/2`.
Our lift satisfies the hypothesis with `s=3`, so it gives
`I=O(n^(3/2))` for `L=n`, without a smaller exponent. In the relevant
unbalanced range `n<=L<=n^(3/2)`, their Theorem 1.2 again gives
`O(L sqrt(n))`. This is an applicable result, not a small-prime-size
refinement of the needed kind.
[Milojevic–Sudakov–Tomon, Theorems 1.1–1.2, author PDF arXiv:2401.06670v1](https://aleksa-milojevic.github.io/publications/PointHyperplaneIncidences.pdf).

**VC-dimension method.** Theorem 1.4 of the accessible author preprint
by Iosevich, Pham, Senger and Tait, version 1 dated 1 March 2023,
gives

    I << n L / p^alpha + n p^(2alpha)

for `0<alpha<1`, assuming planes are normalized as `a dot x=1`,
no line containing `k_0` of the points lies in two selected planes,
and `n>=2 k_0 p^alpha`. In our balanced case `L=n<p`, an origin
outside all selected planes exists: their union has at most `n p^2<p^3`
points. Translating to that origin permits the required normalization.
The no-three-collinear property permits `k_0=3`. Taking
`p^alpha=n^(1/3)` satisfies the size hypothesis for sufficiently large
`n` and gives `I=O(n^(5/3))`. Thus this theorem does not improve the
balanced Rudnev estimate. This comparison uses only the stated
author-preprint version.
[Iosevich–Pham–Senger–Tait, Theorem 1.4, arXiv:2303.00330v1](https://arxiv.org/html/2303.00330v1).

### Richness does not force VC dimension two

An additional hypothesis of VC dimension at most two would not follow
just from the RS lift, even if every selected plane is rich. Choose three
domain coordinates and set
`f=0` there. For each of their eight subsets `S`, interpolate the unique
quadratic `q_S` taking value zero on `S` and value one at the other chosen
coordinates. The eight polynomials are distinct and their planes shatter
the three lifted points. Allocate a disjoint block of `T` additional
coordinates to each polynomial and set `f=q_S` on that block. Whenever
`n>=8T+3` and `p>n`, all eight planes are `T`-rich. This includes
`T=ceil(c sqrt(n))` for any fixed `c` and sufficiently large `n`.
It is a counterexample to the automatic VC-dimension hypothesis, not a
large-list construction or a counterexample to any incidence theorem.

## 4. Sharp examples must be compared in the correct size regime

The assertion that a general point-plane estimate is sharp does not
automatically settle the present graph problem. An elementary example
shows the distinction. Let `eta` be a nonsquare in `Fp` and take

    P_0={(u,v,u^2-eta v^2):u,v in Fp}.

It has `p^2` points and no three collinear: a contained line would need
its projected direction `(a,b)` to satisfy `a^2-eta b^2=0`, forcing
`a=b=0`, after which the graph condition excludes a vertical line.
Any other line meets the quadratic surface at at most two points.

A plane `Z=A U+B V+C` meets this surface in `p+1` points unless its
completed norm level is zero, in which case it meets it in one point.
For each `(A,B)` exactly one `C` gives the latter case. Thus there are
`p^2(p-1)` planes with `p+1` incidences each. Selecting `L=p^2` of them
gives incidence order `L sqrt(|P_0|)` with maximum collinearity two.

However `|P_0|=p^2`, not `<p`, and this set is not the RS graph lift above:
its first coordinate repeats `p` times. It does not disprove an improved
theorem for `n<p` graph lifts. Conversely the no-three-collinear
assumption by itself, without the small-size and graph restrictions,
cannot imply such an improvement.

The general arbitrary-field sharpness statements also allow the field
to vary with the configuration. They cannot be silently specialized to
this fixed prime-field graph regime.

## 5. What remains missing

The directly applicable point-parabola theorem inspected in the
[existing rich-core audit](PRIME_QUADRATIC_RICH_CORE_INCIDENCE_GATE.md)
gives only `L=O_c(n^(11/8))` at `T=c sqrt(n)` under `n<=p`; this is not
sublinear either. It does not supply the desired universal improvement.

A sufficient new statement would be a balanced estimate

    I({(x,x^2,f(x)):x in D}, n quadratic planes)
        = O(n^(3/2-epsilon))

for some fixed `epsilon>0` in the intended prime-field size range,
uniformly in `f`. Selecting `n` rich planes would first exclude lists
of size at least `n`; padding a smaller selected plane set to size `n`
would then yield `L=O_c(n^(1-epsilon))` from (1).

No inspected primary theorem supplies this graph-specific power saving,
and no claim that it is impossible is made. The bounded check therefore
ends here: the usual point-plane lift is not, by itself, an established
sublinear-list theorem above the first-order constant. No hidden-constant
comparison, manuscript edit, or computational scan was used.
