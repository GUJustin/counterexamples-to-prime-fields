# Different source geometry: audited wedge mechanism

The fully reconstructed target exceeds its MCA allowance by **21042194961366305**, about **7.65%**. The binding singleton is **288191873412750740**. Any mechanism aimed solely at that singleton needs a substantial change; dividing the full excess by its value gives about 7.3%, a scale indicator rather than a sufficient or necessary global propagation theorem.

## Ranked routes

1. **Nonrectangular Newton support with a matching restricted-rank calculation.** Immediately testable with rigorous finite counts. The first weighted-wedge test below is negative.
2. **Shared-image savings across evaluation-point constraints.** Potentially larger than per-point improvements, but needs an explicit common cokernel identity valid for arbitrary received-word-dependent translations. Domain symmetry alone does not establish it.
3. **Several sources with a joint avoidance argument.** Needs a bound on the intersection of exceptional loci; summing source kernel dimensions does not provide that bound.

## Exact weighted-wedge formula

Use source monomials `X^e Y^i R^j Z^z` satisfying

- `e+w*i+(w−1)*j<D`, with `D=m*A`;
- `i+j+z≤L`, `j≤S`;
- `i+κ*j≤H`, where κ is a positive integer.

Their exact count is

`C=Σ_j Σ_i (L+1−i−j) max(D−w*i−(w−1)*j,0)`,

with the sums restricted by these caps. The primary first-jet extraction in pinned `LowerFoundation.lean:16185` replaces `Y^i` by terms `(u0+u1*Z)^(i−f)*a^f`, where `f≤i`; it leaves slope exponent `j` unchanged. Therefore every local term satisfies `aExponent+κ*bExponent≤H`, uniformly in the received word.

Define

`B(M,L,S,H)=Σ_(a≤M,b≤S,a+b≤L,a+κb≤H) (L+1−a−b)`.

For local block r, let `M=min(r,L)` and `h=m−r`. Its enclosing block jet kernel consists exactly of multiples of `(a−b)^h`. The individual a/b degrees and total degree of this factor are h, and its `(1,κ)` weighted degree is κh. Polynomial degree additivity gives exact enclosing-block rank

`B(M,L,S,H)−B(M−h,L−h,S−h,H−κh)`,

with the second term zero if any eroded cap is negative. This divisibility and degree argument is characteristic independent. Summing these ranks is a valid upper bound on the actual extracted constraint rank; it does not assert that the extraction fills every block. The resulting kernel lower bound is `C−n*R`.

For avoidance, a factor with YS degree y and slope degree r has weighted degree at least `max(y,κr)`. This lower bound is sharp from those two degrees alone, so stronger erosion cannot be assumed. Exact slab layers use quotient cap `H−h*max(y,κr)` and actual contact budget. The slab evaluator is verified against `C(D)−C(D−delta)`.

## Bounded experiment and stop

At `m=1000,L=60000,S=310,A=181275`, seven explicitly selected wedges were tested. The unrestricted baseline has kernel lower bound `5182612110404058`. The only nontrivial positive tested wedge, `κ=2,H=1538`, has lower bound `771941716506871`; stronger wedges fail even positivity.

At the critical factor degrees `(r,y,z)=(12,55,3206)`, the baseline exact routing margin is `−569607903263369`. The surviving wedge margin is **`−4874617488590315`**: source dimension shrinks much faster than its safe quotient-band budget. At z2975 it also worsens. No larger scan or full certificate propagation was justified.

`wedge_probe.py/json` records 90 brute block-count and 24 brute coefficient-count checks. `wedge_route_probe.py/json` records 36 exact slab-difference checks. Both guarded jobs used under one second and 10 MiB. These are finite-shape diagnostics, not an impossibility theorem, Lean port, or better.codes improvement.

A remaining distinct refinement is to condition routing on the factor's **actual** weighted Newton degree and partition all possible values. High-degree classes then permit stronger quotient erosion, while the class at the sharp minimum must still be handled. A certificate must cover that minimum class; no optimistic erosion may be substituted for it.

The bounded endpoint test `wedge_partition_endpoint.py/json` closes that partition for the **specific surviving wedge tested here**: at the strongest possible actual factor degree 67, the margin is still `−4683366658290986`. Since slab cost decreases as this degree increases, all 13 possible classes 55 through 67 fail the same routing gate. This does not exclude different wedge parameters or Newton polygons.
