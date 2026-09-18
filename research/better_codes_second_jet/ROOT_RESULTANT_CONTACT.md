# Curvature coefficient and two-source first-jet contact

Let m>=3. Write Q=A(t,Y,R)V+B(t,Y,R), allowing challenge coefficients. Suppose the polynomial identity

    Q(t,tR-t^2V+t^3E3,R,V)=0 modulo t^m

holds in the independent formal variables R,V,E3. Put E=E1, V=-E, E3=0. Then

    U=B(t,tR+t^2E,R)-E A(t,tR+t^2E,R)=0 modulo t^m.

Differentiate the original identity with respect to E3 and specialize as above. This gives t^3 Q_Y=0 modulo t^m, so the specialized Q_Y has t-order at least m-3. Differentiate U with respect to E (including V=-E). This gives

    t^2 Q_Y-A(t,tR+t^2E,R)=0 modulo t^m.

Consequently A has first-jet contact at least m-1. Formal differentiation here requires no division or characteristic bound.

For two such sources Q_i=A_iV+B_i, let

    R12=A_1 B_2-A_2 B_1.

Its first-jet specialization is A_1 U_2-A_2 U_1, so it has contact at least 2m-1. It can of course vanish identically; this lemma does not prove independence of the sources over the rational function field.

With weights wt(X)=1, wt(Y)=w, wt(R)=w-1, wt(V)=w-2, if wt(Q_i)<mA then

    wt(R12)<=2(mA-1)-(w-2)=2mA-w.

This exceeds the ordinary root-count budget (2m-1)A by A-w. Thus the contact gain almost compensates the doubled weight, but does not itself give an ordinary interpolation certificate at agreement A. Any actual candidate solving both Q_i also solves R12 exactly, irrespective of this root-count comparison.

The coefficient A itself has weight at most mA-w+1 and contact at least m-1; its weight can exceed (m-1)A by A-w+1. It is not automatically a first-order identity on every candidate.

Outstanding: prove that suitable sources have a nonzero useful resultant, handle common factors and specialization, and derive an applicable full counting bound. A dimension lower bound for the source kernel alone does not establish any of these.
