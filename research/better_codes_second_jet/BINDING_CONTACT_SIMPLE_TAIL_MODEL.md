# A source-compatible binding carrier with a simple first tail

Independent audit of the root agent's strengthened model: PASS. This strengthens `BINDING_CONTACT_RESOURCE_GATE.md` by exhibiting an actual reduced first-tail component. It does not construct the required target second-jet source or a bad-line bank.

Work over an algebraically closed field of characteristic zero or p>n, with n=262144, w=131071, m=118, A=181275. Let Lambda be the monic squarefree domain locator, deg Lambda=n. Put W=Y-Z and

    F=W^55 + Lambda^10*(R^12+R+Z^3261) - Lambda^9*Lambda'*W.

## Irreducibility and exact support

Over k(X), divide by Lambda^10 and view the result as a polynomial in Z over k(X)[R,W]:

    Z^3261+f(R,W),
    f=R^12+R-(Lambda'/Lambda)*W+Lambda^-10*W^55.

Since f(0,0)=0 and f_R(0,0)=1, the factorization of f has an irreducible factor of multiplicity exactly one: at the origin precisely one vanishing factor can occur, to the first power. Eisenstein at that factor proves irreducibility of Z^3261+f. The W^55 coefficient of F is one, so F is primitive over k[X]; Gauss's lemma and the invertible substitution W=Y-Z prove irreducibility in all variables.

Its exact R, jet, and jet/challenge degrees are (12,55,3261). Its weighted degree for weights (X,Y,R,Z)=(1,w,w-1,0) is 55w=7208905. The potentially competing term Lambda^10 R^12 has weight4194280; the linear terms have weight2752510.

## Contact and primary-source compatibility

For the received affine word w_x(Z)=Z, substitute X=x+t and W=tR+t^2 E. The order-ten terms from Lambda^10 R and -Lambda^9 Lambda' W cancel. The order-ten coefficient left over is

    Lambda'(x)^10*(R^12+Z^3261),

which is nonzero. Thus contact is exactly ten at every node. The factor charge is

    e(F)=55w-10w=45w=5898195 <118(A-w)=5924072.

The polynomial Q0=F*W^108 has exact contact118, weight163w=21364573<118A=21390450, R-degree12, jet degree163, and total jet/challenge degree3369. It therefore fits the repaired primary-A support caps s36,Y163,L176421. The complete primary charge has25877 spare.

## Regular seed and a simple first-tail component

At challenge Z=0 the polynomial P=0 solves F(X,P,P',0)=0. It is a regular seed over k(X), since F_R(X,0,0,0)=Lambda^10 is nonzero. This regularity is generic in X; it does not assert nonvanishing at the domain nodes.

Let D be the rational ODE derivation on F=0, so DY=R and DR=-(F_X+R F_Y)/F_R, with DZ=0. At the generic-X point (W,R,Z)=(0,0,0), the linearized equation is

    R=(Lambda'/Lambda)*W,   DW=R.

Consequently the linear part of D^jY, for j>=1, along the tangent surface is

    (Lambda^(j)/Lambda)*W,

where Lambda^(j) denotes the ordinary j-th derivative. In particular the first degree-w tail D^(w+1)Y has nonzero W coefficient: its numerator has leading term n(n-1)...(n-w) X^(n-w-1), nonzero under p>n. The same statement holds for its Hasse-normalized tail, since (w+1)! is invertible.

At the point, the differential of F has nonzero R coefficient Lambda^10. After eliminating R, the differential of the first tail has nonzero W coefficient. Thus the intersection of F with the first tail is a smooth, reduced curve at this point (Z is the remaining local parameter). In particular an irreducible first-tail component through the point occurs with multiplicity one. Clearing the tail's separant denominator does not change this local conclusion because F_R is a unit there.

## What the model does and does not establish

This is an irreducible regular carrier at the exact binding flags, a genuine primary-source divisor with the target weight/contact budgets, and a carrier with a simple first-tail component. Thus the new scalar contact resource alone cannot rule out that combination.

It does not show universal divisibility by every primary-kernel source. It does not supply a target second-jet interpolant whose retained conditions select this component. It also does not produce a large bad-label set: the exhibited seed has label Z=0 and its singleton selection has no large-pencil obstruction, while the whole received line consists of codewords. Any proposed aggregate-cost improvement can still use these extra universal-source, retained-source, and selected-family hypotheses. No benchmark improvement or counterexample to such a stronger theorem is claimed.
