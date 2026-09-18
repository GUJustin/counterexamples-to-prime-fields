# Restricted curvature routing for exact total derivatives

Let Q=A V+B=delta G, where delta=partial_X+R partial_Y+2V partial_R, and G lies in k[X,Y,R,Z]. Write w_x(Z)=f_x+Z g_x for the received line. Assume Q is nonzero, its second-jet source constraints hold to order m≥1 at every coordinate, and the characteristic is zero or sufficiently large for the explicit degree conditions below.

## Exactness test

Integrate A/2 with respect to R, with zero integration constant, obtaining G0. This requires deg_R A+1<p in positive characteristic. Then compute

    C=B−(G0)_X−R(G0)_Y.

A polynomial primitive with deg_R G<p (or unrestricted R-degree in characteristic zero) exists exactly when C=U+R W with U,W independent of R and a polynomial g(X,Y,Z) exists with g_X=U,g_Y=W. In characteristic zero this last condition is U_Y=W_X. The same criterion is sufficient in positive characteristic if all relevant X,Y exponents are below p−1, allowing ordinary polynomial integration and excluding closed nonexact Frobenius forms. Set G=G0+g.

Within this same p-safe primitive class, if Q has R-degree at most S, one can take deg_R G≤S+1. Writing the top coefficients as g_j(X,Y,Z)R^j, exact preservation of that R cap requires

    (g_(S+1))_Y=0,    (g_(S+1))_X+(g_S)_Y=0.

Thus a free G-box of cap S+1 is NOT automatically an admissible source primitive. Without the deg_R G<p restriction the test is not necessary: Q=R^p has primitive G=X R^p, but its R^p integration-kernel contribution is invisible to integration of A/2. In the benchmark weighted regime wt G≤T<p and w≥2, the required R-degree restriction is automatic.

For weights (1,w,w−1,w−2), delta lowers weight by one. If wt Q<T, discard any homogeneous components of a primitive of weight>T: their images must vanish separately. A primitive of weight≤T therefore exists. One may similarly discard derivative-kernel components of Z-degree above deg_Z Q. If T<p and deg P≤w, then deg_X G(X,P,P′,z)≤T<p. Every actual solution of Q consequently satisfies G(X,P,P′,z)=c for a constant c.

## Exact local contact equivalence

Assume p>m+1 and deg_R G<p. Put t=X−x and suppress Z. The condition

    Q(x+t,w+tR−t²V+t³E3,R,V)=0 mod t^m

is equivalent to the existence of g_x(Z), independent of R, such that

    G(x+t,w+tR+t²E,R)−g_x(Z)=0 mod t^(m+1).       (1)

Forward proof: the coefficient of V in the source identity at t=0 is 2G_R(x,w,R), so G(x,w,R)=g_x. Restrict to the genuine quadratic arcs P=w+a1 t+a2 t². The source identity holds there, hence differentiating G along the arc and integrating modulo t^(m+1) gives G−g_x=0. The polynomial change of variables R=a1+2a2t, E=−a2 is invertible over k[t]/(t^(m+1)), proving the full ambient first-jet identity (1).

Reverse proof: (1) holds along genuine cubic arcs P=w+a1t+a2t²+a3t³. Differentiate to get Q=0 modulo t^m. The transformation

    E3=a3,  V=a2+3a3t,  R=a1+2a2t+3a3t²

is invertible over k[t]/(t^m); its inverse is a3=E3, a2=V−3tE3, a1=R−2tV+3t²E3. This recovers the full ambient second-jet identity. No assumption that arbitrary formal jets are actual derivatives is needed: the displayed polynomial ring automorphisms supply the equivalence exactly.

In a full scalar ambient primitive box containing the constant monomial, allowing g_x removes exactly one local scalar condition from the ordinary first-jet zero-value condition. This does not assert that the globally weighted primitive support achieves every ambient rank. Frontier's INTEGRABLE_SOURCE_DOMINATION.md quantifies the source-gate loss: the hoped generic curvature saving does not survive this exactness restriction.

## Heavy coordinate groups route back to first order

Let H bound deg_Z g_x, let A be the required number of agreements, and choose 1≤t≤A. Partition coordinates by identical polynomials g_x(Z). Call a class heavy if it has at least t coordinates; there are at most floor(n/t) such classes, with distinct polynomials h_j(Z).

For an actual Q-solution P at challenge z, G(X,P,P′,z)=c. Every agreeing coordinate x satisfies c=g_x(z). If c=h_j(z) for a heavy class, P satisfies the first-order identity

    G(X,P,P′,z)−h_j(z)=0.

Otherwise, choose A agreement coordinates. Every identical-polynomial class represented there has size at most t−1. The number of ordered pairs from different classes is therefore at least A(A−t+1). Each such pair has g_x(z)=g_y(z), and a nonzero difference polynomial of degree≤H vanishes at at most H challenge values. Summing across all ordered coordinate pairs proves that the number of challenge labels having any A-agreement candidate outside all heavy first-order routes is at most

    H n(n−1)/[A(A−t+1)].                        (2)

At the pinned A=181275,n=262144, t=ceil(A/2)=90638 gives at most two first-order routes. Formula (2) remains an exact upper bound; no benchmark score is inferred from it.

If a downstream theorem needs each specialized G−h_j to be a nonzero polynomial, there is one additional common exceptional set of at most H_G labels, where H_G bounds deg_Z G. Choose any nonzero coefficient of a nonconstant (X,Y,R) monomial of G; such a coefficient exists because delta G is nonzero. Every zero specialization of any G−h_j must annihilate this same coefficient. Thus one does not pay separately for every heavy group.

## Scope

This is a genuine restricted routing theorem for exact total derivatives, not for an arbitrary curvature-linear factor. The simplest obstruction to general elimination is Q=V: all affine P=aX+b solve it, and their first jets fill the (Y,R) plane, so no nonzero first-order polynomial can contain all these solutions without an extra integration parameter or a proximity-based routing argument.
