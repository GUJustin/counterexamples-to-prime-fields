# Characteristic-zero comparison for quadratic lists

2026-09-19. A consequence of established incidence theory, not a new
prime-field theorem.

For n distinct complex evaluation coordinates and an arbitrary word f,
let L distinct quadratics each agree at T>=c sqrt(n), with fixed c>0.
Their graphs have degree at most two, three degrees of freedom, and
multiplicity type two: three graph points determine at most one quadratic,
and distinct quadratics intersect at most twice.

[Sheffer–Szabo–Zahl, Theorem 1.3](https://arxiv.org/html/1502.07003v4)
therefore gives, for every epsilon>0,

    L T <= C_epsilon (n^(3/5+epsilon) L^(4/5)+n+L).

For sufficiently large n absorb the final L term. If the n term dominates,
L=O_c(sqrt(n)); otherwise divide by L^(4/5) and raise to the fifth power:

    L=O_(c,epsilon)(n^(1/2+5epsilon)).

Thus for every eta>0 the complex-field bound is O_(c,eta)(n^(1/2+eta)).
The corresponding real incidence theorem gives O_c(sqrt(n)).

A polynomially larger prime-field list at this agreement scale therefore
cannot arise from a characteristic-zero configuration preserving these
incidences. This does not prohibit additional incidences after reduction
modulo a prime, supply a quantitative characteristic threshold, or establish
the same bound over prime fields.
