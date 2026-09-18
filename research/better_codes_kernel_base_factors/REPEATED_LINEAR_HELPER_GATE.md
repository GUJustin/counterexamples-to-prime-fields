# A highly repeated linear leading factor forces a received-word pencil

Status: exact nonuniform-profile theorem at the binding shape. It closes a subcase of the zero-discriminant branch, not that entire branch or the benchmark ledger.

Work over K=k(Z), with n=262144 distinct base-field nodes, w=131071, affine received symbols f_x+Zg_x. Let F be a universal factor with the exact own-system caps v=55w, y=55, r=12, t=3261. Assume its leading R coefficient A has Y-degree43. Its actual first-jet contacts a_x satisfy

    sum R(a_x) >= C-1, C=6802316684345,
    a_x <=43+2b_x, sum b_x<=12,

where b_x is the X-order of the leading Y coefficient of A. Thus a_x<=67. R is exactly the local rank formula in OWN_SYSTEM_RIGIDITY.md.

## Exact profile threshold

For every integer h in [0,30] and a in [0,67], the finite exact certificate checks

    R(a) <= R(h)+(R(43)-R(h))*1[a>h]+M*b(a),
    M=12474280/3, b(a)=max(0,ceil((a-43)/2)).

Consequently the number N_h of nodes with a_x>h satisfies

    N_h >= ceil((C-1-n R(h)-49897120)/(R(43)-R(h))).

This bound is the exact integer optimum for these abstract profile constraints: the displayed JSON supplies the profile with one contact67 (using the entire b-budget12), N_h-1 contacts43, and n-N_h contacts h. It meets the rank requirement, while one fewer high node cannot. It is not asserted to arise from an actual polynomial.

For h=16 the bound is212704; for h=0 it is218594.

## Repeated factor theorem

Suppose A=G^e H, where deg_Y G=1 and e>=27. Put h=deg_Y H=43-e. Weighted additivity gives

    e wt(G)+wt(H)<=43w+12, wt(H)>=h w.

Since e>12 and wt(G)>=w, integrality forces wt(G)=w. Normalize its Y-leading coefficient (which is independent of X) to write G=Y-P(X,Z), deg_X P<=w, initially with coefficients in K. The leading Y coefficient of H has X-degree at most12; discard its at most12 coordinate zeros.

At any remaining node, the Newton contact lemma at t=0 implies that A(x,Y,Z) has a root of multiplicity at least a_x at the received symbol. If a_x>h, this root must belong to G. This is an ordinary fixed-X root statement; it does not transfer Y-multiplicity to vanishing along an arbitrary candidate.

Thus G(x,f_x+Zg_x,Z)=0 on at least212692 coordinates. Interpolate on any w+1 of them: P=P_0(X)+ZP_1(X) with P_i in k[X], degrees<=w. This descends the graph to the original field and removes all possible rational-in-Z specialization exceptions. The monic graph identity now holds polynomially at every label.

Let a degree<=w polynomial candidate agree with the received word at any A0=181275 coordinates. Its agreement set meets the fixed good-coordinate set in at least

    181275+212692-262144=131823>w.

Hence the candidate equals P_0+zP_1. All such candidates at all labels are on the same affine codeword pencil. Any applicable no-large-selected-pencil hypothesis can now be applied directly; no stronger hypothesis is silently assumed here.

For the maximal power e=43, the clean overlap is137713, exceeding w by6642. The first multiplicity certified by this particular profile/overlap argument is e=27, with margin752. The e=26 profile does not clear this argument; that does not show an actual counterexample exists.

## Why the next quadratic power is not automatically excluded

The Newton support condition does imply the genuine along-candidate bound

    ord_x A(X,P(X),z) >= nu(a_x),
    nu(a)=max(ceil(a/2),a-12),

at agreement coordinates where the relevant specialization/contact identities hold. If A=G^e H and neither evaluated helper is zero, the local orders u,v obey e*u+v>=nu(a), and their sums are bounded by the evaluated helper degrees. This is the safe version of the discrete ceiling argument.

Even granting those constraints uniformly, the e=21, deg_Y G=2, deg_Y H=1 case survives. Inside an181275-coordinate agreement set take:

| contact a | order u of G(P) | order v of H(P) | count |
|---:|---:|---:|---:|
|33|1|0|87300|
|43|1|10|13108|
|43|2|0|80867|

Outside take80869 contacts43. Then sum u=262142=2w, sum v=131080<=w+12, every local inequality holds, and total rank6962641412584 exceeds the necessary6802316684344. The leading-coefficient b-budget is zero. This is an explicit feasible numerical profile, not an algebraic construction; it proves that these inequalities alone cannot force either quadratic/linear helper to vanish.

`repeated_helper_lp.py` additionally supplies exact rational dual certificates for the finite LPs e21/g2, e20/g2, and e14/g3. Floating-point optimization only finds the dual: its nonnegative slopes and every state inequality are checked with exact fractions. `repeated_linear_gate.py` uses no optimizer and verifies the high-node threshold, extremal abstract profiles, and the integer quadratic profile directly.
