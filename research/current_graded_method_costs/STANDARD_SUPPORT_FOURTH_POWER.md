**Scope update:** `ORDER_IDEAL_FOURTH_POWER.md` now extends this result to all coordinatewise monomial order ideals, and covers both Eq63 and Eq64. The restrictions below describe this original proof only. Eq64 also covers supports downward only in Y0; Eq63 on that larger class remains open.

# Fourth-power necessity for the current graded standard support ledger

September17,2026. This closes the missing moment step for the STANDARD
first-order supports in current ePrint Eq60: a derivative cap and a total
jet-degree cap, with all permitted coefficient monomials. It does not
extend the graded argument to arbitrary downward supports or nonmonomial
spaces. These are costs of the stated numerical proof ledger, not lower
bounds for actual lists or exceptions.

## Theorem

Let n>=12 be divisible by4, D=n/4-1, D+1<A<=n be an integer,
and 0<=b<=B. Consider exactly the support

    X^x Y0^u Y1^v, 0<=v<=b, u+v<=B,
    x+D u+(D-1)v<mA, x,u,v>=0.

Assume characteristic zero or exceeding every retained total jet degree,
and let G_q,R_q be its exact source dimension and local rank on total jet
degree q. Set

    a*=(An-8)/(n(n-8)), epsilon*=a*-a0,
    a0=(3+sqrt(133))/31, c0=(1-2a0)/8.

Suppose 0<epsilon*<=1/2000 and an integer H>=0 satisfies the CURRENT
Eq63 graded row test for an affine received line:

    sum_q (H-q+1)_+ (G_q-nR_q)>0.                    (1)

Then

    m>c0/epsilon*, B>m/4, b>=m/8,
    H+1>m/(36864 epsilon*),
    H>m/(73728 epsilon*).                          (2)

Consequently the current squarefree list ledger Eq56 costs
Omega(D/(epsilon*)²), and the current regular-family MCA ledger Eq55
costs Omega(D²/(epsilon*)⁴), even after optimizing its incidence threshold.
The same necessity applies to their coarser Eqs57--58. The assumptions
and reconstruction bounds yield matching powers with the current upper
orders; this is a restricted METHOD statement, never intrinsic tightness.

## Proof: every positive prefix is expensive

Normalize prefix surpluses by n:

    P_j=sum_(q<=j)(G_q/n-R_q).

By summing each degree contribution H-q+1 times, (1) is equivalent to
sum_(j=0)^H P_j>0. Therefore some prefix P_j is positive. Total-degree
truncation preserves the standard support form and the hypotheses of the
existing exact finite-length cost theorem in
`../first_order_support_audit/FINITE_LENGTH_GAP_COSTS.md`.
For that prefix it gives m>c0/epsilon*, its maximum Y0 exponent>m/4,
and its maximum Y1 exponent>m/4-1. Thus m>=16, B>m/4, b>=m/8.
Its total degree is at most j<=H, so also H>m/4-1>=m/8.

We need a uniform upper bound on the positive surplus of EVERY prefix.
Apply the exact finite-length reduction to a prefix, whether or not its
surplus is positive. Discard its final diagonals with
L_q=mA-(D-1)q<m. The half-rank lemma proves they have nonpositive surplus,
so the retained support S0 has normalized surplus at least P_j. Its exact
coefficient benefit is bounded above by the saturated leading benefit at
a*, and each retained monomial has positive such benefit. Hence its total
degree is <4ma*<2m. The critical support converse gives

    P_j <= B_(a*)(S0)-R(S0)
         <= m epsilon* |S0| <=3 epsilon* m³.          (3)

The middle inequality uses B_(a0)(S0)-R(S0)<=0; it remains true if some
benefits at a0 are nonpositive, by deleting those monomials. The last
inequality follows from the number of nonnegative pairs of total degree
<2m: 2m²+m<=3m². This reduction and (3) hold also for empty S0.

## Proof: a mandatory low-degree triangle supplies the negative area

Put J=floor(m/8). Since b>=m/8 and B>m/4, the support contains ALL q+1
jet monomials on each degree q<=J. Their coefficient prefixes are nonempty
and saturated locally: L_q>=m, because A>=D+2 and q<=m/8 imply

    L_q>=m(A-(D-1)/8)>=m.

For each such degree, its exact local rank is

    R_q=sum_(ell=0)^(m-1) min(min(q,ell)+1,m-ell).

Taking only ell=q,...,m-q-1 gives

    R_q >=(m-2q)(q+1) >=3m(q+1)/4.

The exact-to-leading coefficient comparison gives
G_q/n<=ma*(q+1). Since a*<47/100, it follows that

    G_q/n-R_q <=-m(q+1)/4.

Consequently, for 0<=j<=J,

    P_j<=-m(j+1)(j+2)/8.

As H>=J, the total negative prefix area in the graded sum is therefore
at least

    -sum_(j=0)^J P_j
       >=m(J+1)(J+2)(J+3)/24
       >m⁴/12288.                                  (4)

On the other hand (3) bounds each positive prefix by3 epsilon* m³.
Positivity of the full graded sum implies

    3 epsilon* m³(H+1)>m⁴/12288,

which proves the H+1 bound in (2). Since H>=m/8>=2, H>=(H+1)/2 gives
the displayed H bound. No compactness, uniqueness of the critical
optimizer, or preservation of grading under sorting is needed.

## Current reconstruction formulas

Let tau=2D-3, u=1+tau(B-1), v=min(u,tau(b-1)+D), and
F=Bv+b(u-v), as in current Eq54. As shown in README.md,

    F>=DBb/4 >Dm²/128.

For the joint degree bound

    Jreg=H(2uv-v²)+2(1+tau H)F,

we have 0<=v<=u and tau>=D/2, so

    Jreg>=D²HBb/4
         >D²m³/(9437184 epsilon*)
         >D²c0³/(9437184 (epsilon*)⁴).

Every multiplier of Jreg in Eq55 is at least1 for every permitted
incidence threshold. Thus minimizing that threshold does not evade the
lower cost. The list budget lambda*F+S likewise exceeds Dc0²/(128(epsilon*)²).
These inequalities concern the DECLARED degree-based upper-bound formulas;
the actual component degrees or true lists may be much smaller.

## Restrictions

* This proof uses a mandatory low-degree triangle, so it applies to Eq60
  standard supports, not arbitrary downward supports with missing small
  derivative exponents. It does not resolve the general graded moment
  problem posed in README.md.
* It concerns the Eq63 graded row test. No claim is made about its Eq64
  alternative, arbitrary global kernel dependencies, stronger rank
  estimates, several equations, or actual-degree component accounting.
* The exact finite reduction retains its stronger characteristic guard
  (larger than all retained jet degrees), not merely the reconstruction
  guard p>max(D,b).
* For epsilon>=1/n the corrected epsilon* is of order epsilon; close to
  integer rounding one must keep the explicit corrected quantity.
* The local verifier corroborates the low-degree rank and negative-area
  arithmetic. The quantified proof imports the previously audited
  critical-support and finite-reduction theorems; no independent human
  referee or formal verification is claimed.
