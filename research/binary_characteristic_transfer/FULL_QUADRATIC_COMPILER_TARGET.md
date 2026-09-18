# Toward a quadratic-line population of order N²

The target is a new compiler, not a reparameterization of the existing three-term remainder. On a projective six-space over F_p one would have N~p^6, projective three-space supports A~p^3, and a candidate subspace population ~p^12=N². The missing object is a shared affine received line with true quadratic witnesses and controlled label collisions.

## Complete ordinary code-equivalence test

The current remainder space after projectivization is span{1,Y,Y^(p+1)}. For p>2 it cannot be made into quadratic evaluation on more than 2p+2 distinct Y-values by any shared permutation, nonzero coordinate scalings, and invertible basis change. Indeed, quadratic evaluation points [1:T:T²] lie on a nonsingular projective conic. The original projective evaluation points [1:Y:Y^(p+1)] would therefore lie on a nonzero conic. Substitution gives a polynomial with exponents

    0,1,2,p+1,p+2,2p+2.

They are distinct, so a nonzero conic cannot vanish identically; it has at most 2p+2 roots. This includes rational parameterizations and Möbius changes that give a shared code equivalence. It does not exclude a new received line or nonlinear operations on the witness family.

## A compiler identity which would give true quadratics

Quadratic Frobenius remainders have the right weights:

    span{X², X^(p+1), X^(2p)} / X²
        = span{1,Y,Y²},  Y=X^(p-1).

Squaring an additive compiler gives such witnesses, but changes an affine received line f+zg into

    f²+2zfg+z²g².

In odd characteristic this is a parameter parabola, not an affine line. Dropping the mixed term is not legitimate.

An exact determinant replacement is available algebraically. For polynomial vectors u,v and a 2x2 polynomial matrix F,

    det(F+z*u*v^t)=det(F)+z*v^t*adj(F)*u.

Thus a rank-one direction matrix keeps the received determinant affine in the scalar label. If, for many labels, all four entries admit synchronized witnesses that are affine linear in Y on a common large support, their determinant is a quadratic witness on that support. A valid new construction must ensure that the quadratic coefficients genuinely span dimension three, that the determinant labels remain distinct, and that the received determinant is not already a codeword pencil.

Simply repackaging one known scalar compiler cannot supply this. If every matrix entry uses an affine combination a_ij(f+zg)+q_ij, its direction matrix is g*(a_ij). Rank one forces det(a_ij)=0, so the determinant of the corresponding witness matrix has zero coefficient of h_z². It reduces to a restricted linear-in-h_z family. Consequently the missing ingredient is at least two nontrivially synchronized scalar compiler identities, not four copies of one identity.

This is a concrete algebraic construction criterion, not an established N² example. No further finite parameter grid is justified until a synchronized family is supplied.

## Explicit check of the existing elliptic compiler

In the smallest unshifted full-rank case, m=4,t=2, the existing trace-form family is

    G_c(X)=c X^(p²+1)+c^p X^(p³+p),  c in F_(p²)*.

Its critical-level compiler has F=c^p X^p and hence

    P_c=G_c/F=X^(p³)+lambda X^(p²-p+1),
    lambda=c^(1-p), lambda^(p+1)=1.

Projectivize after dividing by X, with Y=X^(p-1). Then

    Pbar_c=Y^(p²+p+1)+lambda Y^p.

Moving the Y^p term into the received-line direction indeed restores the strict degree<p guard, but leaves the zero witness and only p+1 labels. On the projective domain of size (p+1)(p²+1), these are the ordinary multiplicative fibers Y^(p²+1)=-lambda, each of size p²+1. They give no large exceptional population.

The large translation factor in the elliptic theorem does not survive this fixed projectivization. For a nonzero translation a, the lower term (X-a)^d with d=p²-p+1 has nonzero coefficient -a at X^(d-1), because d=1 modulo p. The exponents d and d-1 have different residues modulo p-1. After division by X, it is not a polynomial in X^(p-1). A common low-degree correction cannot remove that high offending term. Using X-a instead changes the quotient map with the candidate, which is not a shared code or received line.

Thus the existing elliptic formula supplies no synchronized rank-one determinant pencil directly. This is a checked limitation of that substitution, not an exclusion of every quadratic-form compiler.

## Why the simplest determinant does not implement support union

Suppose a proposed matrix construction has only two entrywise discrepancies, on its diagonal:

    M=H+diag(e1,e2),

where all entries of H are affine linear in the common evaluation variable. Let S_i be the zero support of e_i. Then

    det(M)-det(H)=e1 H22+e2 H11+e1 e2.

To obtain agreement on S1 union S2, H11 must vanish on S1\S2 and H22 on S2\S1. If both differences contain at least two distinct points, both diagonal witness entries vanish identically. Furthermore, if the off-diagonal entries of M already equal low-degree witnesses for every label, their direction entries have degree at most one. The rank-one direction condition then equates the product of the two diagonal directions to a degree-at-most-two polynomial. It cannot accommodate two genuinely high-degree diagonal directions. Thus this direct two-pencil construction neither enlarges support by union nor supplies the desired rank-one affine parameterization.

A nondegenerate determinant route would need additional synchronized off-diagonal identities, with errors that are not of this simple diagonal form. No such identities are present in the checked elliptic compiler.
