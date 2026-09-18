# Correction: characteristic-zero rich-core lifting is excluded

**Corrected September 18, 2026.** This filename is retained for history. The earlier version incorrectly described the following number-field rich-core assertion as an open construction target. It is excluded by an existing complex incidence theorem. The reduction-to-primes observation was conditionally correct, but its proposed growing characteristic-zero input cannot exist.

## Primary theorem and application

Sheffer, Szabó and Zahl, *Point-curve incidences in the complex plane*, Theorem 1.3, [arXiv:1502.07003v4](https://arxiv.org/html/1502.07003v4), gives the bound

    I = O_epsilon(m^(3/5+epsilon) L^(4/5) + m + L)

for degree-at-most-two complex curves with three degrees of freedom and multiplicity type two. The theorem does not require transverse intersections. Its constant depends only on these fixed parameters and epsilon.

Apply it to the received points (x_j,w_j) and graphs y=P_i(x) of distinct degree-at-most-two polynomials. Distinct x_j ensure three received points determine at most one quadratic; two distinct quadratic graphs meet at at most two points. Their degrees are at most two. Thus all hypotheses hold, including for linear or constant members of the bank.

Suppose m=Theta(s²), L=Theta(s²), and each polynomial has Omega(s) matches, with uniform positive constants. Then I=Omega(s³). Choose epsilon=1/20. The theorem instead gives

    I=O(s^(14/5+2epsilon)+s²)=O(s^(29/10))=o(s³),

a contradiction for sufficiently large s. Every number field embeds in C. The fields may vary with s: the incidence constant is independent of their degrees, coefficients, and coordinate heights.

Therefore a growing characteristic-zero quadratic rich core at these scales is impossible. This is not merely a failure of a full-rank Jacobian or a particular finite-plane design. No singular lifting, varying number field, or splitting-prime choice repairs this proposed characteristic-zero route while retaining those incidence scales.

## What remains valid and what remains open

Any *fixed* algebraic configuration can still be reduced at sufficiently large splitting primes after protecting its finitely many nonzero guards. This does not supply the impossible growing family above. In particular, finite seed realizations do not justify the proposed asymptotic transfer.

The theorem is over C and gives no blanket obstruction to intrinsically modular configurations over prime fields. A modular prime-field construction must generate its dense incidence pattern in positive characteristic, rather than reduce an equally dense characteristic-zero configuration. It need not preserve the full affine-plane design. The exact design note `research/prime_quadratic_line/REGULAR_JOHNSON_DESIGN_GATE.md` excludes one duplicated-projective-plane model, not all positive-characteristic quadratic banks.

A concrete modular target remains: on mu_n in a prime field, find a full-coefficient quadratic agreeing with a monomial word X^m at c*sqrt(n) points at the required constant, uniformly along a growing family, with enough field/domain room and a usable nonbank bound. Multiplicative scaling would then give n distinct quadratics. Existing small cyclic gates and the F49 gate prove isolated orbits, not that uniform root-count assertion. No larger scan is justified by those examples alone.

Finally, even a modular rich core does not automatically provide the strong affine-label population. The two-block extension construction uses the additional identity z=b−eta*v for two intercepts in the same F_p-line. A prime-field replacement must also supply compatible repeated labels, sufficient distinctness, and source control. The proven prime-field conic-cover tradeoffs remain valid but do not realize these stronger parameters.

**Revised assessment:** the arithmetic/number-field rich-core route is closed by Theorem 1.3. The remaining constructive route is intrinsically modular, with a separate label-pairing requirement. No general prime-field impossibility is claimed.
