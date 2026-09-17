# Hermite–Johnson control of singular-heavy quadratic solutions

This note combines explicit interpolation with the specialization-safe algebraic-root lemma being audited separately. It concerns actual polynomial solutions of one common equation; it does not assert that an arbitrary first-order interpolant has this quadratic form.

## Statement and full-support convention

Let F have characteristic zero or sufficiently large positive characteristic as specified below. Fix n distinct coordinates, a received line `f+zg`, and polynomials P of degree at most D. A pair `(z,P)` has full value-agreement support `S(z,P)`. It is bad when `|S(z,P)|≥A>D` and no degree-at-most-D polynomial G agrees with g on **all** of S(z,P).

Consider actual solutions of the challenge-independent equation

`Q(X,u,v)=a(X)v²+(b(X)u+d(X))v+c(X)u²+e(X)u+f0(X)=0`.

The coefficient X-degrees are unrestricted. Define the fixed Hermite core S1 and ordinary core S0 as in `../hermite_singular_cover/PROOF.md`; write their sizes as s,u. Assume a fixed positive rate lower bound `D/n≥ρ_min>0` and fixed positive margins

`A−D≥ηn`, and `A−u≥sqrt(D*s/2)+εn`.

Then the number of bad labels possessing such an actual solution is `O_(ρ_min,η,ε)(n)`, subject to the algebraic-root lemma and its fixed-degree characteristic threshold. In particular, if a is nonzero at every coordinate, u=0 and the sufficient uniform condition is

`A²>Dn/2`

with fixed quadratic slack. More generally the stronger-than-needed condition `A−u≥sqrt(D*(n−u)/2)+εn` suffices. Zeros of a need not all belong to the ordinary core; the actual u is the appropriate loss.

## 1. Split regular and exceptional singular incidences

Choose positive integers L,e so that

`b*=A−u−(L−1)−e > sqrt(D*s/2)`

with fixed normalized slack. Fixed η,ε allow `L,e=Θ_(η,ε)(n)` for sufficiently large n.

The existing regular-incidence theorem removes at most

`(n/L) C_reg`,

where

`T0=1+max(0,2D−3)`,
`C_reg=4T0+2T0*(n−D)/(A−D)+2n`.

This counts labels with **any** bad witness having L regular agreements. For all other labels every bad witness has fewer than L such agreements.

Outside S0∪S1, singular agreement can occur at at most two labels per coordinate: its discriminant, or the relevant degenerate coefficient polynomial, is a nonzero polynomial in z of degree at most two. Consequently at most `2n/(e+1)` labels have more than e such coordinates. This count is uniform over candidates.

A remaining bad witness therefore has at least b* singular agreements in S1. At every x∈S1 these prescribe both jets

`P(x)=f_x+z g_x`,
`P'(x)=h_x+z k_x`,

where `h_x=−(b(x)f_x+d(x))/(2a(x))` and `k_x=−b(x)g_x/(2a(x))`.

If b*>s there are no remaining witnesses. Otherwise apply the interpolation below.

## 2. Exact finite Hermite interpolation gate

Choose positive M, put `T=M*b*−1`, `B=floor(T/D)`, and

`V=Σ_(j=0)^B (T−D*j+1)`,
`c_M=Σ_(j=0)^floor((M−1)/2)(M−2j)=floor((M+1)²/4)`.

Assume `V>s*c_M`. Set, for example,

`H=floor(s*c_M*B/(V−s*c_M))`.

There is a nonzero polynomial `R(X,z,Y)` with Y-degree at most B, z-degree at most H, and `(1,D)` weighted X,Y degree at most T, satisfying the following constraints at every x∈S1. In the expansion

`R(x+t,z,f_x+zg_x+(h_x+zk_x)t+U)`,

every coefficient of `t^a U^j` with `a+2j<M` is identically zero as a polynomial in z.

Indeed the unknown space has dimension `(H+1)V`. There are c_M local conditions, each a z-polynomial of degree at most H+B. Thus the number of scalar linear equations is at most `s*c_M*(H+B+1)`, strictly less than the number of unknowns by the displayed choice of H.

If P matches both jets at x, then `P(x+t)−P(x)−P'(x)t` is divisible by t². Every surviving local term has t-order at least M after substitution. Hence `R(X,z,P(X))` vanishes to order at least M at each of its b* jet matches. Its degree is at most T<M*b*, so it is identically zero.

This interpolation argument works in every characteristic: it uses first formal derivatives and polynomial divisibility, not division by factorials. Distinct coordinates make the local zero multiplicities additive.

## 3. Why the Johnson threshold is exact for this gate

For fixed positive D/n and b*/n,

`V = M²(b*)²/(2D)+O(Mn)` and `s*c_M = s*M²/4+O(Ms)`.

Thus `(b*)²>D*s/2` with fixed slack permits a constant M, and consequently constant B and H, independent of n. The finite inequalities above, rather than an asymptotic assertion, are the certificate when parameters are specified. If D/n is allowed to approach zero, the resulting constants can depend on that rate; the stated fixed-rate application has D/n=1/4.

## 4. Algebraic root covering and original full supports

Apply the specialization-safe algebraic-root lemma to R: its Y and challenge degrees are constants, while `deg_X R≤T=O(n)`. The lemma covers every degree-D polynomial root at every nonexceptional label by coefficient curves of total degree `O_(B,H)(D)`, with `O_(B,H)(deg_X R+D)` isolated/exceptional labels. This includes polynomial roots appearing only at specialization; they cannot simply be assumed to extend a generic polynomial branch.

For any retained coefficient curve, agreement at an original domain coordinate is a linear hyperplane equation `P(x)=f_x+zg_x`. If more than D distinct such hyperplanes contain a curve, interpolation forces its entire family to be an affine codeword pencil `P=F+zG`.

For a nonaffine curve at most D agreement hyperplanes are persistent. Each candidate with A full-support agreements must therefore meet at least A−D nonpersistent ones. Bézout and incidence counting give at most `degree(curve)*(n−D)/(A−D)` such labels.

On an affine pencil, let I be its persistent value-agreement set. A bad pair must have an agreement outside I; otherwise G agrees with g on its entire full support. Each coordinate outside I contributes at most one label. Thus each pencil contributes at most n bad labels. Constantly many pencils give O(n).

All these incidences use the candidate's **original full value-agreement support**. No derivative match is assumed at regular coordinates or at additional agreements. Consequently the result is a full-support correlated-agreement bound, not merely a list-size bound on the Hermite core.

Combining the three pieces gives

`#bad ≤ (n/L)C_reg + 2n/(e+1) + C_alg(B,H)*(deg_X R+D+n*(n−D)/(A−D)+n)`,

for the constant supplied by the algebraic-root lemma. At fixed margins and rate this is O(n).

## Characteristic and scope

The quadratic-core decomposition requires characteristic not two. The existing regular theorem requires characteristic zero or p>D. The algebraic-root step requires its additional bounded-degree separability condition (for example p>B after squarefree/content reduction); this is a fixed threshold at fixed margins. No dependence on the arbitrary X-degree of the original quadratic equation is introduced. A full manuscript claim should cite the audited algebraic-root lemma and its exact hypotheses.

This controls every quadratic derivative identity with nonvanishing leading v² coefficient on the domain under the Hermite–Johnson agreement condition. It is stronger than the earlier triple-intersection singular-cover criterion and does not assume a small persistent Hermite core. A large ordinary core remains a genuine limitation, quantified by u above.
