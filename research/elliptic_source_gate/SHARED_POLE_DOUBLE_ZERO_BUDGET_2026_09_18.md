# Shared-pole Paley bank: double-zero budget closes its full-bank quarter-rate target

September 18, 2026. Symbolic result, no new finite-field scan. This supersedes the proposed offpole common-remainder target for the FULL bank in `SHARED_POLE_PALEY_TRANSLATION_TARGET.md`. It does not exclude arbitrary subbanks, altered coefficient arrays, or other elliptic families.

## Statement

Use the exact bank Q_S of that note, indexed by H/{±1}, H=E[ell], for an odd prime ell≥5. Put M=ell² and L=(M+1)/2. Work in characteristic zero or characteristic p>5 with p≠ell, over a field containing the torsion data. These L distinct polynomials have degree at most M. For ANY 4M distinct affine evaluation coordinates and ANY received word, the entire bank cannot meet the dimension-(M+1) first-order agreement threshold.

In fact its minimum agreement is asymptotically at most

    [(1+sqrt(35))/4] M + O(1),

or agreement fraction at most (1+sqrt(35))/16+o(1), approximately0.4323. The quarter-rate first-order fraction is (3+sqrt(133))/31, approximately0.4688.

## 1. Equal values at poles force double zeros

Write P=(M−1)/2 for the number of finite torsion-pole coordinates t_T, and let D0(X)=product_T(X−t_T)². At a fixed pole t_T, the value of Q_S is a fixed nonzero scalar times

    c_(T−S)+c_(T+S).

If two candidates have the same value there, their coefficients of the WHOLE rational summand R_(t_T) agree. Subtracting cancels both its double and simple pole parts. The rational difference is regular at t_T; multiplication by D0 therefore gives a zero of order at least two. This conclusion uses the cleared rational formula, not only pointwise equality.

The archived exact pole buckets have sizes

    r=(M−1)/4 at value0,
    h=(M−1)/8 each at values+2 and−2,
    1 at value c_T.

Their values are distinct in the stated characteristics. Thus the number of equal-valued unordered candidate pairs at EACH pole is

    E_pole=binom(r,2)+2binom(h,2)
          =(M−1)(3M−19)/64.

Summing over all poles, even those absent from the chosen evaluation domain, forces at least 2P E_pole zeros counted with multiplicity among all pair differences. Since each distinct pair difference has degree at most M, the aggregate number of possible offpole pair-equality coordinates is at most

    B = M*binom(L,2) − 2P E_pole
      = (5M³+25M²−49M+19)/64.

The bank's distinctness is proved in the target note, so no zero polynomial invalidates the degree count.

## 2. Uniform incidence bound on an arbitrary domain

Suppose q≤P selected coordinates are poles, and m=4M−q are offpoles. At each selected pole, a received value matches at most r candidates. Let S be the total candidate/word incidences offpole and k_x their bucket sizes. Then

    sum_x binom(k_x,2) <=B,
    S² <=m sum_x k_x² <=m(S+2B).

If every candidate has at least A matches, it follows that

    L*A <=q*r + f(4M−q),
    f(m)=(m+sqrt(m²+8mB))/2.

This upper bound is maximized by q=P. Indeed, m≥(7M+1)/2 and B<M³/8. Direct differentiation gives

    f'(m) <=1+sqrt(B/(2m)) <1+M/7 <(M−1)/4=r

for M≥25. Hence q*r+f(4M−q) is increasing in q. We obtain the field- and received-word-independent bound

    L*A <=P*r + (m+sqrt(m²+8mB))/2,
    m=(7M+1)/2.

Expanding its leading term yields the asymptotic claim. The argument already accounts for all possible choices of which poles to include; it is not restricted to the rational-elliptic x-domain or a special word.

## 3. Exact exclusion at every ell≥5

For M≥49, suppose A≥15M/8, and set S0=L*(15M/8)−P*r. A necessary condition from the preceding quadratic inequality would be S0²−m*S0−2mB≤0. Instead,

    S0²−m*S0−2mB
      =(29M⁴−954M³+413M²−452M−56)/256 >0.

For u=M−49≥0, the numerator is

    29u⁴+4730u³+277949u²+6815644u+55911492,

which is strictly positive. Thus the full bank cannot even have minimum agreement 15M/8.

The exact first-order threshold at rate (M+1)/(4M) is larger than 15M/8. At rate1/4, insert agreement fraction15/32 into the high-branch polynomial

    F_rho(a)=(8−rho)a²−6rho*a+rho*(4rho−5).

It gives −1/4096. This remains negative as rho increases through [1/4,26/100], while F is increasing in a near the relevant positive root. Therefore a1((M+1)/(4M))>15/32 for every M≥25, proving the desired exclusion for M≥49.

The remaining odd-prime square M=25 has N=100,K=26. The first-order root is above47/100, so its integer threshold is at least48. Here L=13,P=12,r=6,m=88,B=1446. With A=48, S0=13*48−12*6=552 and

    S0²−88*S0−2*88*1446=1632>0.

This closes the last case. (The finite fixture had the much stronger bound17, but no fixture data are needed here.)

## Consequence for common-remainder proposals

Any offpole common factors G_j shared by candidate subsets must satisfy the reduced pair-degree budget B above, after subtracting the forced DOUBLE zeros at every torsion pole. At quarter rate the balanced coverage needed by the entire bank exceeds that budget. Consequently no proposed offpole common-remainder identity can rescue the full bank in this parameter regime, even if its roots live in a larger extension or in characteristic zero.

What remains outside the statement: changing the coefficient array c, selecting a substantially different subbank and redoing its exact pole buckets, changing the rate/length regime, or finding a genuinely different shared-pole family. The current full-bank quarter-rate target should stop; this proof does not justify another torsion fixture scan or assert a general elliptic obstruction.
