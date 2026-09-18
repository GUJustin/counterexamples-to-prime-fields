# Prescribed subgroup: infinity exceptions do not save a full square-root term

The refined mixed-character estimate still does not prove nontrivial
character bias on the benchmark subgroup. The saving from a removable
point at infinity occurs for at most one of the 8128 twists, so averaging
dilutes it by that index. This calculation does not rule out additional
cancellation between twists. Independently, the ordinary one-pole compiler
with degree bound 131071 supplies at most 131073 agreements, short of the
target139782 by8709.

No field construction, subset search, or compute allocation is used below.
The arithmetic receipt is `verify_practical_subgroup_twists.py/json`.

## Setup and the exact centered mixed bound

Let p=2130706433, E=Fp^6, and b have degree6 over Fp. Let

    D=mu_262144 subset Fp*,
    n=262144,
    I=(p-1)/n=8128,
    H={base-field characters psi: psi|D=1}.

Thus |H|=I. Fix a nontrivial multiplicative character chi of E*, put
rho=chi|Fp*, and define

    S(chi,psi)=sum_{a in Fp*} chi(b-a) psi(a).

For every base-field character psi, define

    delta_0 = 1 if psi=1, otherwise0,
    delta_inf = 1 if rho*psi=1, otherwise0.

The refined rank-one bound is

    | S(chi,psi) + delta_0*chi(b) + delta_inf*chi(-1) |
        <= (6-delta_0-delta_inf) sqrt(p).          (1)

In particular the generic mixed bound is6sqrt(p), not5sqrt(p).
The cases are:

| Conditions | Bound on the uncentered absolute value |
| --- | --- |
| psi!=1 and rho*psi!=1 | 6sqrt(p) |
| Exactly one of psi=1, rho*psi=1 | 5sqrt(p)+1 |
| psi=1 and rho=1 | 4sqrt(p)+2 |

These are upper bounds; no sharpness claim for this particular p,b is made.

### Derivation of the boundary corrections

Apply the rank-one sheaf construction in Katz's proof to the finite etale
algebra E x Fp, the regular element (b,0), and the character chi x psi.
The corresponding affine-line trace, after multiplication by chi(-1),
is S(chi,psi). The algebra has dimension7, giving the unrefined6sqrt(p)
bound. [Katz, An Estimate for Character Sums, Theorem 2 and its proof,
pp.197-199](https://web.math.princeton.edu/~nmk/old/estcharsums.pdf).

Over the algebraic closure, the line has six conjugate b-punctures, plus
0 and infinity. At each b-puncture the local character is a Frobenius
conjugate of chi and remains nontrivial. The sheaf is therefore
geometrically nontrivial for every nontrivial chi. It is tame, and compactly
supported H^1 on the line with these eight points removed has dimension6.

The local character at0 is psi. The local character at infinity is
the product of the finite local characters, namely rho*psi (up to
inversion, which does not affect triviality). One can see the restriction
rho directly by pulling the Lang character back along diagonal scalar
multiplication Fp* -> E*. Equivalently, the finite local exponents sum to
the exponent of chi restricted to Fp*.

When psi=1, the sheaf extends through0 and the Frobenius trace there is
chi(b). When rho*psi=1, it extends through infinity and its trace there
is chi(-1): in the coordinate u=1/a, factor
(b-a,a)=(-1,1)*u^(-1)*(1-bu,1); the scalar factor has trivial character
rho*psi and (1-bu,1) specializes to the identity at u=0.

Each such removable puncture contributes a one-dimensional weight-zero
boundary term to compactly supported H^1. The remaining middle-extension
H^1 has dimension6-delta_0-delta_inf and is pure of weight1. This purity
can be seen by realizing the finite-order tame character sheaf in the
cohomology of its finite cover and then taking the smooth projective
compactification. The nontrivial local monodromy at the b-punctures excludes
H^0 and H^2 contributions. The trace formula, including the two possible
boundary terms with their minus signs, gives(1).

This is a refinement of Katz's proof, not an assertion that its displayed
Theorem2 already states these boundary corrections.

## Averaging over the subgroup index

Character orthogonality gives

    S_D(chi):=sum_{a in D} chi(b-a)
       = I^(-1) sum_{psi in H} S(chi,psi).

Exactly one twist in H has delta_0=1. There is a twist in H with
delta_inf=1 precisely when rho^(-1) belongs to H, equivalently when
chi|D=1. If it exists it is unique. Define epsilon=1 in that case and0
otherwise. If rho=1, the infinity exception coincides with the trivial
twist; it still contributes one additional dimension saving, not I of them.

Summing the centered estimate(1) therefore gives the exact bound

    | S_D(chi) + [chi(b)+epsilon*chi(-1)]/I |
        <= [6-(1+epsilon)/I] sqrt(p).             (2)

Consequently

    |S_D(chi)|
        <= 6sqrt(p) - (1+epsilon)(sqrt(p)-1)/8128. (3)

For epsilon=1, chi(-1)=1 since -1 is in D. Retaining the phase chi(b)
in(2) can improve the additive boundary correction but not the leading
square-root coefficient.

The exact expression in(3) has the following values (rounded):

| Infinity exception among the twists | Bound from(3) | Excess over n |
| --- | ---: | ---: |
| No (epsilon=0) | 276951.7755140741 | 14807.7755140741 |
| Yes (epsilon=1) | 276946.0965554440 | 14802.0965554440 |

Thus even the stronger case exceeds262144. Intersecting this with the
trivial bound merely gives |S_D|<=n, which leaves no positive s-B in
the fixed-cardinality Cauchy exponent. This method does not establish
product surjectivity on D. A uniform5sqrt(p)+O(1) bound cannot be justified
by counting the infinity exceptions: all but at most two twists retain
the generic rank6, and at most two dimensions are saved across the whole
8128-term average. Additional cancellation would need an additional theorem.

Both types of chi occur: restriction E* -> D is surjective on character
groups. In particular it is not valid to restrict the product-surjectivity
Fourier sum to characters with epsilon=1. Even doing so would not make(3)
smaller than n.

## Independent one-pole agreement cap

Write k=131072 for the strict degree bound, so witnesses have degree<=k-1.
For any b outside D, set

    f(X)=(X^(k+1)-b^(k+1))/(X-b),
    g(X)=-1/(X-b).

The first word is a monic polynomial of degree k. For a degree<k witness h
and lambda!=0, the agreement equation f+lambda*g=h is the vanishing of

    (X-b)(f(X)-h(X))-lambda.

This is a nonzero polynomial of degree k+1: evaluating it at b gives
-lambda, and its leading term is X^(k+1). It therefore has at most
k+1=131073 roots in D. This bound holds regardless of how well products
of b-a are distributed.

The usual subset-product construction attains k+1 for a representable
label by choosing |S|=k+1, V_S=prod_{a in S}(X-a), P_S=X^(k+1)-V_S,
lambda=-V_S(b), and

    h_S=(P_S(X)-P_S(b))/(X-b),
    deg h_S<=k-1.

Its residual is V_S(X)/(X-b). The sources f and g each have exact
agreement k, and common agreement k, by root counting plus interpolation
on any k coordinates. Thus even full product coverage would give a
one-coordinate source gap and capacity margin1/n, whereas the benchmark
requires agreement139782 and capacity margin8710/n.

Taking |S|=139782 in this unmodified construction would require a witness
of generic degree139780, exceeding131071 by8709. Product coverage alone
does not impose the additional high-coefficient cancellations needed to
lower that degree. Those would be a new coefficient-fiber problem.

The two gates are independent: the refined character bound does not prove
coverage, and coverage for the one-pole compiler would still miss the
requested agreement threshold. This does not rule out a different compiler
or a new estimate exploiting cancellation between the mixed twists.
