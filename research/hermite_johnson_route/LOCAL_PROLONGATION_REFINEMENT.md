# Recovering a prescribed derivative inside the ordinary core

2026-09-17. Conditional local refinement of Appendix R; not a normalization of the benchmark source.

Let Q(X,z,u,v) be a common actual-solution equation. At an ordinary-core coordinate x, the received-line specialization Q(x,z,w_x(z),v) is identically zero in z,v. In particular Q_v vanishes there. Differentiating the actual identity Q(X,z,P,P')=0 in X therefore proves, at every agreement at x,

    J_x(z,P'(x))=0,
    J_x(z,v)=Q_X(x,z,w_x(z),v)+v Q_u(x,z,w_x(z),v).

No assertion that J(X,z,P,P') vanishes globally is needed or justified. The displayed local condition follows because its missing chain-rule term is P'' Q_v, zero at this coordinate.

Suppose J_x is nonzero over F(z) and has exactly one distinct root over an algebraic closure. If its v-degree is q and the characteristic is zero or greater than q, write its two leading coefficients as c_q(z),c_{q-1}(z). Then

    J_x(z,v)=c_q(z)(v-r_x(z))^q,
    r_x(z)=-c_{q-1}(z)/(q*c_q(z)).

Thus it prescribes one rational derivative outside the zeros of c_q. With bounded original value/challenge degrees, the numerator and denominator degrees of r_x and the number of excluded labels are uniformly bounded. X differentiation does not increase challenge degree. For derivative degree at most t, J_x has derivative degree at most t+1.

Such a coordinate can be removed from the ordinary core and added to the prescribed-jet core in the Appendix R proof. The exceptional coordinate-label budget increases only by a bounded multiple of n; the same rational Hermite interpolation and full-support incidence argument then applies with the updated sizes u and s and the same signed threshold.

One repeated root is NOT enough: a cubic J_x may have both a repeated root and a distinct simple root, and an actual solution is only known to satisfy J_x=0. The required hypothesis here is one distinct root in total, or an independently justified selection of one root.

This refinement is not automatically available for the present ConstraintKernel source. For multiplicity at least two, its contact constraints force J_x to vanish identically at every received fiber. Higher prolongations can introduce P'' and higher derivatives; they cannot be dropped. The note supplies a valid local refinement, not an extraction theorem or a better.codes certificate.
