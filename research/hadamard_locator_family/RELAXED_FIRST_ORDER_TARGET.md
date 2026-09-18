# Relaxing saturation while preserving the first-order regime

The n=4(L-1), k=L-1, A=2(L-1) target is stronger than necessary for the intended
first-order lower-bound question. Set n=c k while retaining A=2k. The audited
high-rate first-order curve is the positive root of
F_rho(a)=(8-rho)a^2-6rho*a+rho(4rho-5).
Substitution gives F_rho(2rho)=rho*(-4rho^2+24rho-5). Consequently the agreement
stays strictly above this curve whenever

4 <= c < (12+2 sqrt(31))/5 = 4.627105745132009... .

All these rates lie above the high-rate branch cutoff11-3sqrt(13), so the
branch formula applies. Unlike c=4, any c>4 puts agreement strictly BELOW the
rate-based Johnson curve: a^2=4rho^2<rho. The capacity gap is rho, hence fixed
positive for a fixed c. An unbounded construction with L comparable to k would
therefore address the intended first-order list question. A single finite
example would only supply a seed, not asymptotic tightness.

For L8,k7,A14, every n from28 through32 remains above the curve. The exact
ledger in relaxed_target_ledger.json records n32's positive polynomial margin
105/8192 and agreement margin approximately0.00233984. At n32 the minimal
pair-incidence count is144 against the sextic pair budget168, leaving24;
at n28 it is168 with no slack. Thus the saturated locator and symmetry
obstructions cannot simply be carried over to n32.

The incidence system has56 polynomial coefficients plus2n node/word values,
and112 requested equalities. Its raw dimension is2n-56. There are11 gauge
directions (seven common-polynomial shifts, one common nonzero scaling, three
projective parameter changes). At n28 this count requires at least11 equation
dependencies; at n32 it requires only3. This is a diagnostic, not an existence
argument or an assertion that the constraints are independent.

One concrete family to revisit is the preserved four-quadratic seed on12nodes.
Duplicating P_i as P_i+c_i M_i and P_i+d_i M_i retains six old agreements per
candidate. Each needs eight new agreements. On20 new nodes, four fourfold and
sixteen triple transversal blocks give64 new incidences. The n28 obstruction
used a balanced orthogonal16-row sign pattern; this relaxed incidence pattern
need not satisfy that hypothesis. It remains necessary to solve the actual
polynomial matching equations and check distinctness; no realization is known.
