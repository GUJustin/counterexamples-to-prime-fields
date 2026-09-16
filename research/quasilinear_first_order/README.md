# Linear first-order MCA with nonsingular agreement coordinates

For a first-order equation of bounded jet and challenge degrees, a fixed
positive agreement gap, and characteristic larger than the candidate
degree, bad labels with a witness having a positive fraction of
nonsingular agreement coordinates number **O(n)**. This includes implicit
equations and solution surfaces. `REGULAR_AGREEMENTS.md` gives the proof;
`appendix.tex` is the manuscript version.

As a corollary, for equations `R(X,z)P'=A(X,z,P)`, all bad labels number
O(n) if both the candidate degree and `deg_X R` lie a fixed positive
fraction below the agreement threshold. This imposes no restriction on
the value degree of A beyond the fixed jet-degree bound. Ordinary lists
are constant-sized under the same separant-degree condition.

A nonlinear equation with exactly two polynomial solutions gives
**n/2 bad labels** at rate tending to 1/4 and agreement gap 1/4, showing
sharp linear order. The general first-order conjecture remains open:
interpolation equations can be singular at many agreement coordinates.
There is no quadratic construction or better.codes score gain here.

`PROOF.md` retains an earlier, longer argument for nonlinear
value-independent-separant equations, with a different explicit bound.
The broader local proof supersedes it as the main result. Both are
self-reviewed; no independent review or literature priority is claimed.

## Reproduce

```sh
python3 research/quasilinear_first_order/verify.py
```

The exact checker exhausts small-field polynomial--challenge pairs,
checks nonsingular uniqueness, ordinary lists, full-support badness and
incidence counts, and includes implicit equations with solution-dependent
separants and actual surfaces. Five lower fixtures have 6, 12, 18, 24,
and 48 bad labels. A characteristic-three negative control shows why
uniqueness cannot simply omit the characteristic condition. Finite
checks supplement the proof; they do not establish the general theorem.
