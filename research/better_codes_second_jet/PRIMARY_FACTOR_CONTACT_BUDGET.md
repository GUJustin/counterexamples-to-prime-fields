# A universal first-jet contact budget for primary factors

This proves a quantitative constraint supplied by the primary
interpolant, beyond merely bounding a factor's weighted degree. It
applies to arbitrary received words and affine received lines. It does
not yet convert first-tail component multiplicities into a smaller
normal term.

## 1. Many matching subsets force many affine jet-line factors

Let n distinct nodes x be given over a field, with received symbols
w_x (possibly in k(Z), including w_x=f_x+Zg_x). Fix w>=2 and n>=w.
Let J(X,Y,R,Z) be a nonzero polynomial with weighted degree W for
weights X=1,Y=w,R=w-1,Z=0. Suppose its formal first-jet contact at x
is at least u_x, meaning

    J(x+t,w_x+tR+t^2E,R,Z)=0 mod t^(u_x)

as an identity in formal R,E,Z. Then

    #{T subset nodes: |T|=w, sum_(x in T)u_x>W}
       <=floor(W/(w-1)).                         (1)

**Proof.** Work over the coefficient field k(Z), extending constants
or adjoining indeterminates as needed. For each w-element T let P_T
be the interpolating polynomial of degree at most w-1 through the
received symbols on T, and H_T=product_(x in T)(X-x). Every polynomial

    P_T+c H_T

has degree at most w and agrees at T. Formal first-jet contact implies
J(X,P_T+cH_T,P_T'+cH_T',Z) has those roots with multiplicities u_x.
Its X degree is at most W. If their sum exceeds W, this substituted
polynomial is identically zero, with c an indeterminate.

Over k(X,Z), J therefore vanishes on the affine line

    R=P_T'+(H_T'/H_T)(Y-P_T).

The corresponding monic linear polynomial in R divides J. Distinct
sets T yield distinct slopes: the rational function H_T'/H_T has a
simple pole of residue one at exactly the nodes in T. This argument
works in positive characteristic as well. Consequently all these
distinct linear factors divide J over k(X,Z)[Y,R]. Its total (Y,R)
degree is at most floor(W/(w-1)), proving (1). No generic rank or
finite-field point-density assumption enters the proof.

A weaker but convenient form fixes w-1 nodes B. Write S_B=sum_B u_x.
Then

    #{x outside B: u_x>W-S_B}<=floor(W/(w-1)).      (2)

This follows either directly by the same pencil construction or from
(1). Choosing B among nodes of largest contact gives a useful test
for a nonuniform contact profile.

## 2. Uniform contact lower bound

If every u_x>=u, a nonzero J satisfies

    W>=min{u*w,(n-w+1)(w-1)}.                    (3)

Indeed, if W<u*w, all the n-w+1 subsets containing one fixed set B
of size w-1 qualify in (2). Thus W>=(n-w+1)(w-1). One can replace
n-w+1 by binom(n,w) using (1), but the weaker form already covers
the benchmark budget by a wide margin.

Crucially, this is not restricted to codeword received lines. P_T is
interpolated separately for each T; its coefficients may depend on Z.
Only its X degree and the distinct line directions are needed.

## 3. Contact-excess budget for a divisor of the primary source

Let Q0 be a nonzero primary first-jet interpolant with uniform contact
at least m and weighted degree W0<m*A. Assume

    m*A < (n-w+1)(w-1).                           (4)

Let F divide Q0, put V=wt(F), and let a_x be its ACTUAL formal contact
order at node x. The substitution into the formal local polynomial
ring is injective, and that ring is a domain, so contact orders of
nonzero products add. The quotient J=Q0/F therefore has contact at
least max(0,m-a_x), not m minus the minimum of the a_x.
Weighted degrees also add under multiplication. Put a=max_x a_x.
If a<m, (3) and (4) give

    W0-V=wt(J)>=(m-a)w.

If a>=m, use only V<=W0. Both cases imply

    V-a*w < m(A-w).                              (5)

For a product F=product F_i with specified multiplicities, use
V=sum wt(F_i) and a=max_x sum ord_x(F_i). In particular, when every
factor has uniform contact a_i, this is the additive resource bound

    sum_i [wt(F_i)-a_i*w] < m(A-w).               (6)

The summands need not be positive for arbitrary factors, so (6) is
not automatically a bound on their number. It is a genuine constraint
on positive contact-excess families.

There is also a direct nonuniform consequence without taking maxima.
Let WJ=W0-V and u_x=max(0,m-a_x). Then

    #{T: |T|=w, sum_T u_x>WJ}<=floor(WJ/(w-1)).   (7)

These inequalities retain the actual local profile; they do not assign
contact to geometric first-tail components without an additional lemma.

## 3a. Exact average-contact and nonnegative additive budget

Write C=binom(n,w), d=floor(W/(w-1)), and suppose 0<=u_x<=U.
If

    C > n*d*w*U,                                  (11)

then (1) implies the exact inequality

    W >= (w/n) sum_x u_x.                          (12)

Indeed, if the right side exceeds the integer W, the excess is at
least 1/n. Summing sum_T u_x-W over all C subsets gives at least C/n.
At most d summands are positive by (1), and each is at most wU.
This contradicts (11). Negative summands only strengthen the argument.
For d=0 or U=0 the same proof applies without any division by them.

Apply this first to J=Q0/F with u_x=max(0,m-a_x), U=m. Whenever
(11) holds, it gives the sharper primary-factor constraint

    V - (w/n) sum_x min(a_x,m) < m(A-w).           (13)

Replacing min(a_x,m) by a_x gives a weaker but convenient additive
version. More strongly, apply (12) separately to every factor F_i,
using its actual contacts a_ix. These satisfy a_ix<=V_i=wt(F_i):
the injective local substitution has t-degree at most V_i, since
Y maps to a polynomial of t-degree two and w>=2. Thus under (11)
with W=U=V_i the excess

    e_i=V_i-(w/n)sum_x a_ix

is NONNEGATIVE. Contacts and weights add exactly in the factorization
of Q0 (including multiplicities). Since Q0 has contact at least m
at each node, all its irreducible factors consequently satisfy

    0 <= sum_i multiplicity_i*e_i < m(A-w).        (14)

In particular this bounds every subcollection by the same resource.
This assertion requires the displayed combinatorial range condition;
there is no claim of nonnegativity for arbitrary huge weighted degrees.

The benchmark satisfies these conditions with substantial room. Here
n=2^18, w=2^17-1, and every V_i,WJ<mA<2^25. We have d<2^9,
U<=2^25 even when using actual factor contacts. Hence
n*d*w*U<2^69. On the other hand 5<=w<=n-5 and
C>=binom(n,5)>=(n/5)^5>2^75. This verifies all average bounds
simultaneously without computing an enormous binomial coefficient.
The same bound covers quotient U=m=118.

The nonnegative charge (14) is a genuine strengthening of (6).
It still charges polynomial factors, not individual codimension-two
first-tail components; the missing geometric bridge remains.

## 4. What this does and does not exclude in the simple-tail model

The model in RETAINED_SIMPLE_COMPONENT_MODEL.md extends to exact
carrier caps (r,y,t), with y>=r+2, by setting

    E=max(2r,y), W=Y-Z,
    T=Lambda R-Lambda'W,
    F=Lambda^(E-2r)T^r+Lambda^(E-2)T
       +Lambda^(E-y)W^y+Lambda^E Z^t.             (8)

For sufficiently large t the same irreducibility, active regular seed,
and multiplicity-one tail arguments apply. The carrier has weighted
degree exactly E*n and actual first-jet contact exactly E at every
node. Exactness of contact follows from the unique high-challenge
term Lambda^E Z^t: its leading local coefficient cannot cancel.
Thus (5) requires

    E(n-w)<m(A-w).                               (9)

At the binding context (r,y,t)=(12,55,3261), E=55. For the proposed
target primary multiplicity m=118, n=262144,w=131071,A=181275:

    wt(F)=55*n=14417920 < m*A=21390450,
    55(n-w)=7209015 > 118(A-w)=5924072.

The primary weighted cap alone permits the carrier, but (9) rules it
out as a primary factor. Equivalently, its quotient would have weight
strictly below6972530 while its remaining contact63 requires weight
at least63*w=8257473. The deficit is1284943. This is an exact symbolic
exclusion, not a parameter scan.

However the ORIGINAL small model r=3,y=5,t=29 has E=6 and is NOT
excluded, even at the target primary parameters. In fact an explicit
target primary source containing it is

    Q0=F*(Y-Z)^112.

Its first-jet contact is118, and

    wt(Q0)=6*n+112*w=16252816<21390450.

Its slope cap is3, joint Y/R cap117, and joint Y/R/Z cap141, all
within the proposed primary bounds (36,163,176421). Thus a legitimate
target primary source can have a factor with an active simple first-tail
component. What fails in the full model is the SECOND-JET retained
source's target degree budget, not primary-factor membership.

For (8), Q=Lambda delta F-E Lambda'F has full contact E+1 and
weighted degree E*n+w-2, after canceling the Z^t term. Even without
any derivative reserve, its target source gate would require

    E(n-A)<A-w+2.                                (10)

At the pinned target n-A=80869 and A-w+2=50206, (10) fails for
every E>=1. For the h-th power with n0=h,k=h-1, the strict condition
is hE(n-A)<A-w+2. This quantifies the second-source failure separately
from the primary-factor resource.

## 5. Precise remaining geometric bridge

Inequalities (5)--(7) give a primary-factor/contact budget, including
nonuniform profiles. They do not yet bound the normal divisor charge
of multiplicity-one first-tail components. Such a component is a
codimension-two intersection component, not automatically a separate
factor of Q0 with its own contact profile. A useful strengthening would
associate positive contact-excess charges to collections of active
simple components and show their total normal cost is bounded by those
charges. No such association or inequality is established here.

The explicit E=6 primary factor prevents replacing that missing bridge
by a blanket assertion that the primary source excludes simple
components. The resource inequality does exclude the expensive
binding-shaped locator model, while leaving genuinely new component
geometry to be proved.
