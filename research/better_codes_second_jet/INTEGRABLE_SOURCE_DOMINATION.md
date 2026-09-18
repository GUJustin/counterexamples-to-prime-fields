# Integrable curvature sources: exact contact correspondence and dimension domination

Let D_tot=partial_X+R partial_Y+2V partial_R. Suppose Q=D_tot G, with G independent of V. Work in characteristic zero or characteristic p larger than m+1 and all integration degrees used below. At coordinate x let t=X−x and w=f_x+Zg_x.

The curvature contact condition

    Q(x+t,w+tR−t²V+t³E,R,V,Z)=0 mod t^m

is equivalent to existence of a polynomial g_x(Z) such that

    G(x+t,w+tR+t²E,R,Z)−g_x(Z)=0 mod t^(m+1).

For the forward implication restrict to quadratic arcs P=w+a1 t+a2 t². The t^0 coefficient of the original Q condition gives G_R(x,w,R,Z)=0, so G(x,w,R,Z)=g_x(Z) is independent of R (degree below p is needed). Along the arc, Q is dG/dt. Integration through order m+1 is valid under the characteristic assumption. Inverting R=a1+2a2t, E=−a2 recovers the first-jet identity as a formal polynomial identity.

Conversely substitute a cubic arc P=w+a1t+a2t²+a3t³ into the first-jet identity and differentiate. This gives Q=0 mod t^m. The invertible substitutions E=a3, V=a2+3a3t, R=a1+2a2t+3a3t² recover the full second-jet identity. These arguments concern formal polynomial identities, not merely a finite set of actual candidate arcs. The proof was independently derived by the upper-bound-route agent.

Thus integrability replaces the order-m curvature condition by an order-(m+1) first-jet condition with a free coordinate constant. In a local source box containing the constant monomial, this removes exactly one scalar condition, or L+1 challenge coefficients, compared with requiring zero.

## The apparent free-constant saving is dominated at the pinned target

Use weights wt(X)=1, wt(Y)=w, wt(R)=w−1, wt(V)=w−2. Total differentiation lowers weighted degree by one. Consider the standard p-safe construction taking G of weight <mA+1, so Q has weight <mA. Compare it with an ordinary first-jet source of multiplicity M=m+1, the same slope/jet/challenge caps, and weight <MA.

Assume the common source caps contain both jet monomials 1 and Y, L>=1, and mA+1>w. The first assumption requires jet cap at least one; the last ensures that both smaller-budget X-coefficient intervals are positive. Put d=A−1. Increasing the budget from mA+1 to (m+1)A adds d independent X coefficients for each of these two monomials. Under jet degree plus challenge degree <=L they contribute at least

    d[(L+1)+L]=d(2L+1)

additional source coefficients. Meanwhile allowing free coordinate constants saves at most n(L+1) constraints.

For n=262144 and A=181275 the difference is

    (A−1)(2L+1)−n(L+1)
      =100404 L−80870 >0   for every L>=1.

Therefore the ordinary first-jet dimension lower bound strictly exceeds the free-constant integrable bound under these identical caps. This comparison is independent of the detailed graded rank formula, because the same first-jet contact map appears on both sides. Any extra cap constraints necessary to keep Q's slope degree small can only reduce the integrable source further.

This is a domination of the standard coefficient-count minus local-rank existence certificate. It does not assert that all integrable sources are absent, that global dependencies are absent, or that the separately proved heavy-coordinate-constant routing lemma is useless. It does show that the n freed scalar constraints do not convert the new curvature rank saving into a better source-existence gate by this direct integration construction. High-weight elements annihilated by total differentiation are outside this particular budgeted-source comparison and require separate treatment.
