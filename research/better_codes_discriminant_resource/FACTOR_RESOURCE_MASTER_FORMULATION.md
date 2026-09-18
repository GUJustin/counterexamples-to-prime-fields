# A concrete factor-resource optimization and its remaining routing obligations

This is a proposed exact finite feasibility formulation, not a completed search or a replacement benchmark ledger. It incorporates the new centroid invariants and compatibility between different factor centroids. No parameter grid is proposed.

## Global factor data

Factor the leading coefficient over k(Z)[X,Y], clearing scalar Z-denominators by Gauss:

  A=H0(X,Z) product_i G_i(X,Y,Z)^{e_i},
  d_i=deg_Y G_i>=1, sum_i e_i d_i=43,
  wt(G_i)=d_i w+delta_i,
  deg_X H0=delta0,
  delta0+sum_i e_i delta_i<=12.

Take each G_i primitive and irreducible of positive Y-degree. At the benchmark characteristic p>43 they are separable. The integer factor-degree/multiplicity patterns and nonnegative integer delta allocations are finite.

For every i, the following nonzero global polynomials have degree bounds:

- Disc_Y G_i: d_i(d_i-1)w+2(d_i-1)delta_i.
- Res_Y(G_i,G_j): d_i d_j w+d_i delta_j+d_j delta_i.
- Cleared centroid value J_i, for d_i>1: d_i(w+delta_i).

For the last invariant, writing B_i=lc_Y G_i and C_i=[Y^{d_i-1}]G_i, use

  J_i=d_i^{d_i} B_i^{d_i-1} G_i(-C_i/(d_i B_i)).

It is a polynomial after cancellation of the top term. It is nonzero for an irreducible factor of degree greater than one, since otherwise the rational centroid would be a root. Its degree bound follows term by term from the weighted coefficient bounds. Unlike arbitrary other centered coefficients, nonvanishing of this invariant is automatic under irreducibility.

Other cleared centered coefficients may also be used, but their identically-zero branches must be retained explicitly; they cannot be assigned a nonzero-polynomial zero budget by assumption.

## Local state, not an averaged contact guess

At a coordinate x let a be the actual F-contact. For each factor record its integral Newton polygon after translating Y by the received symbol, including the leading-coefficient valuation b_i. Record b0=ord_x H0. The product polygon is the Minkowski sum with multiplicities, and must satisfy the proved bound

  NP_A(j)>=max(0,(a-j)/2,a-12-j),  0<=j<=43.

Also a<=43+2b, where b=b0+sum e_i b_i. Globally sum_x b<=12. This controls the exceptional leading-coefficient places rather than discarding them for free.

At leading-unit places the polygons are monic integral-coefficient polygons. Their vertices have integer coordinates. This integrality is crucial: the quartic example below has a larger invariant cost than a continuous root-allocation relaxation suggests.

For roots with valuations v_{i,1}<=...<=v_{i,d_i}, the safe local lower costs are

  D_i=(2d_i-2)b_i+2 sum_k(d_i-k)v_{i,k},
  R_ij=d_j b_i+d_i b_j+sum_{k,l}min(v_{i,k},v_{j,l}).

Take nonnegative integer ceilings when applying polynomial-order budgets. These are lower bounds; equality of leading root coefficients can only increase actual discriminant/resultant orders.

Centroid-value costs can be bounded directly from coefficient valuations. At a leading-unit place, if beta_k lower-bounds the coefficient of Y^k and mu=beta_{d_i-1}, then

  ord J_i >= min_k(beta_k+k*mu).

Use the actual centered formula if it improves this bound. At leading-nonunit places retain the B_i powers in the cleared invariant; do not use the monic formula without correction.

## Linear feasibility system

For each allowed local state tau and contact a, introduce a nonnegative count x_(a,tau). The initial relaxation has rational counts; integral counts can be imposed after a useful dual or extremal profile is found.

Constraints are:

1. Total count n.
2. Own-system rank sum at least C-1.
3. Total leading-order resource at most12.
4. Each individual discriminant budget above.
5. Each pair-resultant budget above.
6. Each guaranteed-nonzero centroid-value budget above.

An infeasible relaxation gives a rigorous exclusion certificate. A feasible profile is only a profile consistent with these scalar resources, not a polynomial/source construction. The explicit G21-square profile in `REPEATED_SQUARE_LOCAL_MODELS.md` illustrates this distinction.

A practical first implementation should use the leading-unit states and a rigorously relaxed exceptional-place budget, then refine only a surviving extremal profile. The exact all68 contact/rank table already supplies the exceptional rank envelope. There is no need to start by enumerating arbitrary source coefficients.

## Global centroid compatibility: an essential additional constraint

Let

  P_i=N_i/B_i=-C_i/(d_i B_i),
  deg_X B_i<=delta_i, deg_X N_i<=w+delta_i.

A local state in which all d_i roots reduce to the received symbol forces P_i(x,Z)=f_x+Zg_x whenever B_i(x,Z) is nonzero. Track this indicator in the local state.

If P_i and P_j are distinct rational functions over k(Z), then their simultaneous persistent coalescence set has size at most

  deg_X(N_i B_j-N_j B_i)<=w+delta_i+delta_j.

If they are identical, the UNION of their coalescence supports belongs to one helper. Thus the optimization must branch on the equivalence relation of equal centroids, impose intersection bounds between distinct classes, and track union support for each equal-centroid class. Summing only individual coalescence counts misses this global information.

For any class choose a representative with smallest delta. If its persistent union support T satisfies

  T>n-Aagreement+w+delta,

then every nearby degree-at-most-w polynomial P satisfies B(X,lambda)P(X)=N(X,lambda). This follows by more than w+delta common evaluation roots. The following polynomiality gate makes that a genuine cheap routing alternative.

## Rational-centroid polynomiality gate, including degree drops

Suppose deg_X B<=delta, deg_X N<=w+delta, B is generically nonzero, and their Z-degrees are at most h_B,h_N. Consider multiplication by B on the space of X-polynomials of degree at most w. Its coefficient matrix has w+1 columns and rank w+1 over k(Z), since multiplication by a nonzero polynomial is injective.

If N is not generically in that image, the augmented matrix has a nonzero (w+2)-minor. That minor is a polynomial in Z of degree at most

  (w+1)h_B+h_N.

Every label at which N_lambda=B_lambda P for some deg P<=w makes the augmented columns dependent, so it kills the minor. This remains true when B loses degree or vanishes entirely at the label. No constant-denominator assumption or resultant-coprimality assumption is needed.

If N is generically in the image, its quotient has X-degree at most w. Persistent agreement at w+1 nodes then identifies the quotient with P0(X)+ZP1(X), by interpolation. The polynomial identity extends through every apparent coefficient denominator.

For the quartic multiplicity10 case, the joint degree of A is at most t-r=3249. Its remainder has Y-degree3, so jointdeg G<=324. Hence h_B<=320,h_N<=321 and the label bound is at most41943361. This is a conditional routing bound, not an already propagated ledger contribution.

## Highest-leverage next pattern

After high repeated linear/quadratic factors and the cubic invariant exclusions, degree4 multiplicity10 with degree3 remainder is the next targeted pattern. It has genuine integral-Newton jumps and a small rational-centroid denominator (delta_G<=1).

At a leading-unit node, selecting repeated G roots gives

  NP_G(j)>=g_a(3+10j)/10.

For a=34,35 this forces coefficient valuations at least(2,2,1,1,0); for a>=36 at least(3,2,1,1,0). Therefore its cleared centroid value has order at least2 for a34/35 and at least3 for a>=36, while its global degree is at most4(w+1)=524288.

This scalar bound alone is not enough: a mixture near two-thirds contact43 and one-third contact33 can still satisfy the rank and G-resource bounds. But the degree3 remainder then often coalesces at the received word too. Its own invariants and the centroid-intersection/union constraints are the next concrete tests. They address a missing GLOBAL compatibility, rather than merely tightening a single discriminant estimate.

The G21-square branch is a contrasting residual: its explicit contact39/40 profile has no full G-coalescence and too few H-graph nodes, and survives the current discriminant/resultant budgets. Removing other repeated patterns alone therefore does not lower the worst normal cost of the binding cell. To claim benchmark progress, every surviving pattern needs a certified cheaper routing bound, or the whole unreduced branch must be excluded. The optimization is a diagnostic toward that partition, not a substitute for the full ledger.
