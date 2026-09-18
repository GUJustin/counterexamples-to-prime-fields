# Independent audit of the finite-geometry completion answer

Source audited: `research/astra_strategy_2026_09_18/finite_geometry_prime_finish.answer.md`.
Result: PASS, with the fixed-degree and random-sampling scope below.

## Johnson-edge bound

Let r≥1 and the atom inflation κ be fixed constants. Let B distinct
degree-at-most-r polynomials each have A core agreements; T=A+d,
n=floor(T²/r)+1, t=n−n0, and p≥n. For growing A the root-count and
Cauchy–Schwarz calculation gives

    n0 ≥ B A²/(A+r(B−1)).

If A≥r, subtracting this bound from A²/r gives exactly

    A²(A−r)/[r(A+r(B−1))] ≤ A³/(r²B).

If A<r, that difference is nonpositive, so the upper bound remains valid.
Since A≤T=O_r(sqrt n) and d≤sqrt n, it follows that

    t ≤ C_r(d sqrt n+n^(3/2)/B).

For a fixed label, independence and maximum atom κ/p imply

    E Z ≤ B(κt/p)^d/d!.

When B≤sqrt n use t≤p. Otherwise split the two terms in the t bound.
The first term is bounded using

    B(d sqrt n/p)^d ≤ p^(r+1−d)d^d n^(d/2)
                    ≤ n^(r+1)(d/sqrt n)^d,

where d≥r+1 is essential to the second inequality. The second term obeys

    B(n^(3/2)/(Bp))^d ≤ sqrt n

using B>sqrt n and p≥n. This proves the claimed bound (1), including its
constant C^d/d!. For d=(c+o(1))log n/loglog n, it becomes
n^(1/2−c+o(1))+o(1). Summing over parameters and applying Markov proves
that for c>1/2 the sampled completion has o(p) qualifying labels with
probability tending to one.

This is not a deterministic impossibility theorem. It is not uniform in
growing polynomial degree r, growing κ, or arbitrary correlated sampling.
Its extension to n−T²/r=O(d sqrt n) is valid. The argument is independent
of primality of the field.

## Integer-sheet claim

The use of the real point–curve incidence bound is legitimate. Distinct
modular bank polynomials have distinct integer coefficient lifts; their real
graphs have no common components. Any r+1 points determine at most one such
graph (points with repeated x and unequal y determine none), and two distinct
graphs meet at most r times. With N≤nK lifted points the bound is

    BA = O_r(N^((r+1)/(2r+1)) B^(2r/(2r+1))+N+B).

For A≥a sqrt n, the first term yields B=O_{r,a}(sqrt n K^(r+1)); the
N term yields the weaker B=O_a(sqrt n K), and the B term is absorbed for
large n. For even quadratics, (x,y)→(x²,y) has multiplicity at most two
on the lifted point set, so the line-incidence bound gives
B=O_a(sqrt n K²). Thus the claimed modular-sheet consequences follow.

Primary incidence source: J. Pach and M. Sharir, *On the Number of Incidences
Between Points and Curves*, Combinatorics, Probability and Computing 7 (1998),
89–99, [DOI 10.1017/S0963548397003192](https://doi.org/10.1017/S0963548397003192).
The bounded-degree curves/degrees-of-freedom formulation is also stated in
Theorem 1.3 of [Sharir et al., Incidences with curves in R^d](https://www.math.tau.ac.il/~michas/esasss18.pdf).

## Precise off-edge target; no construction obtained

For degree two, let T~tau sqrt n with sqrt(3/2)<tau<sqrt 2 and d=o(sqrt n).
Write beta=n0/n. If B grows faster than sqrt n, the same core bound forces

    beta ≥ tau²/2+o(1).

Thus the core consumes more than three quarters of the coordinates, while
there is still a positive padding fraction available if beta<1. A bank
B=n^(b+o(1)) with b>1/2 could in principle improve the leading logarithmic
gap coefficient under independent completion. The Johnson-edge obstruction
does not rule this out.

But the core must also control nonbank witnesses. If every selected core
bucket has size at least m, a nonbank quadratic has at most 2B/m matches,
by root counting against the bank. For a uniform incidence design,
m=BA/n0, this generic certificate is 2n0/A. To certify this is no larger
than A requires beta≤tau²/2+o(1). Thus using only this certificate forces
asymptotic Johnson equality for the core, even though the final padded code
is strictly off the Johnson edge. A nonuniform design or a stronger nonbank
argument may evade this last condition.

The resulting concrete target is a prime-field quadratic bank with
B≫sqrt n, A~tau sqrt n, and a core near n0=A²/2, with dense, nearly
uniform matching buckets and verified nonbank control. At exact pair-count
saturation every pair of bank polynomials must share its two roots among
the core buckets; this is a stringent polynomial realization problem, not
an arbitrary abstract block design. The real-incidence bound proves that
a bounded-wrap rational or integer lift cannot supply it. No such modular
bank construction is established by the external answer or by this audit.
