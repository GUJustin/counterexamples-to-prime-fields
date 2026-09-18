# Finite DKT exceptional-count comparison for correlated covers

This evaluates one concrete, valid finite support and optimizes its regular incidence threshold. It does not assert global optimality among all DKT supports or transfers.

## Exact finite inputs

Let L be the bank size and s the cover degree. Set
n=s(2L²−2L+1), D=2s, k=D+1, T=s(2L−1), B=4L−2.
The source/common agreement is A=T−s. In DKT's formulas, the agreement input is T, not this source agreement A.

Use multiplicity4 and derivative cap2. The exact source and weighted source counts are
G=3sB²−(s−1)(3B−2),
W=sB³+(3/2)B²+(3/2−3s)B+2s−2.
The local rank bound is23 with weighted total43. For L≥14 the surplus G−23n is positive, and a valid all-active challenge cap is
H=max{B, floor((W−43n)/(G−23n))}.
The strict row inequality is (H+1)(G−23n)>W−43n. Uniformly for s≥1,
H=8B+149−180/s+O(1/B).
The characteristic guard is p>2s.

In Eqs54–55 of DKT2026/2056, put
tau=4s−3,
u=1+tau(B−1), v=6s−3,
F=(14s−9)B+14−20s,
S=3B−4, H_s=3H,
J=H(2uv−v²)+2(1+tau H)F,
lambda=(n−2s)/(T−2s).
These are exact for the stated large-L range.

For any integer r∈[2s+1,T], the regular contribution is
E_reg(r)=[(n−r+1)/(T−r+1)] lambda J
         +[(n−r)(n−2s)/(r−2s)] F.
Writing a=lambda J(n−T), b=(n−2s)²F, the real minimizer satisfies
r−2s=(T+1−2s) sqrt(b)/(sqrt(a)+sqrt(b)).
The minimizing integer is one of its neighboring integers, since the objective is convex after rewriting it as a constant+a/(T+1−r)+b/(r−2s).

A valid ordinary contribution uses r0=2s+1:
Psi=1+(4s−1)(2S−1)+2 max(S−4s−1,0),
E_ord=(2S−1)H_s +[(n−r0+1)/(T−r0+1)](S+H_s Psi)+(n−r0)S.
The resulting exceptional budget is E_reg(r)+E_ord. `evaluate.py/json` evaluate these formulas exactly with rational arithmetic; no source-gap substitution or O_rho constant is used.

## Leading scale: no saving in the dominant term

For s=Theta(L^b),0<b≤1, with the stated small proportionality constant at b=1,
F~(14s−9)B,
J~8(160s²−216s+72)B².
At regular incidence threshold r~xT, division by n² gives
[5120−6912/s+2304/s²]/(1−x) + [28−18/s]/x + O(1/L).
Consequently this certificate yields
E≤C_s n²+O(n²/L),
C_s=(sqrt(5120−6912/s+2304/s²)+sqrt(28−18/s))².
C_1≈665.10835, and C_s→5905.25821 as s→infinity.

The ordinary term alone is O(sL³)=O(n^(3/2)/sqrt(s)), which DOES improve by a cover-degree factor, but it is subleading. The dominant regular term remains quadratic in n. The Taylor image degree grows as s²L², exactly preventing an s-saving in that term. The fixed-word list budget lambda F+S is (28−18/s+o(1))n.

The O(n²/L) remainder includes regular reconstruction terms; it should not be replaced by the smaller ordinary-tail scale when s grows.

## Honest lower/upper comparison

The construction has M=Theta(L³), while this DKT certificate has E=Theta(s²L⁴). Their ratio is Theta(s²L). In terms of gamma=b/(b+2), the lower is n^(3(1−gamma)/2), so the exponent gap to n² is 1/2+3gamma/2. This grows from1/2 toward1 as gamma approaches1/3.

For the positive-density prime choice p=Theta(L³), E is much larger than p, so the actual available upper bound is min(p,E)=p. The DKT certificate therefore gives no nontrivial failure-probability estimate on these examples. Choosing a much larger prime can make the DKT budget nonvacuous, but does not remove the exponent/cover-degree gap.

A separate, construction-specific upper bound is much sharper: the canonical witnesses lie in a conic bank with actual common agreement A, and the audited bank incidence theorem gives asymptotic upper4L³. This matches the lower's order. It is a restricted-bank result, not an improvement to the general DKT certificate. Apply it in the canonical coordinates (f,g); the final two-far-endpoint reparametrization bijects labels and scales witnesses, so its cardinality conclusion transfers. In the canonical bank U=1, there are no common U,V zeros, and the stronger denominator T(T−A) is available; the same4L³ leading term results.

No source-gap factor s appears in published Eq55 beyond its role in the chosen T and n. The normalized source gap is s/n~1/(2L²), while rho~1/L² and the first-order curve margin is of order1/L. These are distinct quantities.
