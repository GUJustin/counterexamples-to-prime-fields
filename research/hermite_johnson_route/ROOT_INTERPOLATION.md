# Constant-challenge-degree Hermite interpolation

2026-09-17. Independent root derivation. This lemma is an interpolation statement, not by itself a line-agreement theorem.

Fix n distinct field elements x_i and affine received jets u_i(z)=f_i+z g_i, v_i(z)=h_i+z k_i. Fix positive integers D,M,T and let B=floor(T/D). Put

    V = sum_{j=0}^B (T-Dj+1),
    c_M = sum_{b=0}^{floor((M-1)/2)} (M-2b)
        = floor((M+1)^2/4).

If V>n*c_M, choose H>=0 with

    (H+1)(V-n*c_M)>n*c_M*B.

Then there is a nonzero Q(X,z,Y) of weighted (X,Y) degree at most T (weights 1,D), Y degree at most B, and z degree at most H, such that every polynomial P of degree at most D matching both received jets at A coordinates satisfies

    Q(X,z,P(X))=0

at its parameter z whenever M*A>T. The equation can be chosen with no parameter at which all its X,Y coefficients vanish.

Proof: use all V monomials X^a Y^b with a+Db<=T, each with an unknown z-polynomial coefficient of degree <=H. At coordinate x_i substitute

    X=x_i+t, Y=u_i(z)+v_i(z)*t+U.

Require coefficients t^a U^b to vanish for a+2b<M. There are c_M such coefficients, each of z degree at most H+B; these impose at most c_M(H+B+1) scalar homogeneous equations. There are V(H+1) unknowns. The displayed inequality guarantees a nonzero kernel vector.

For a matching P, P(x_i+t)-u_i(z)-v_i(z)t is divisible by t^2. Every surviving local monomial therefore has order at least M after substitution. Distinct matching coordinates give at least M*A zeros with multiplicity in Q(X,z,P(X)), whose degree is at most T. Thus this polynomial is zero. This argument uses formal polynomial expansion, without factorial denominators.

Divide all X,Y coefficient polynomials by their common divisor in F[z]. The local constraints remain polynomial identities, because their linear maps commute with the common scalar factor and F[z] has no zero divisors. The primitive result has no identically zero specialization, even over an algebraic closure.

For fixed positive degree rate D/n and fixed positive slack A/n-sqrt(D/(2n)), constants M,B,H suffice for all sufficiently large n. Choose T below M*A with T/(Mn)>sqrt(D/(2n)) by fixed slack. Since V>=T^2/(2D) whereas c_M=M^2/4+O(M), choosing sufficiently large constant M gives V>n*c_M by a fixed relative margin. The displayed inequality then permits constant H.

The pending additional theorem is a specialization-safe O(n) bound on bad full-support labels for polynomial roots of Q. No such conclusion follows from this interpolation count alone.
