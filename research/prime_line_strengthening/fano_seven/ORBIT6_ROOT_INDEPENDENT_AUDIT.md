# Independent root audit of the global orbit 6 exclusion

PASS in characteristic different from two. This is a global parameter proof, not a fixed-node test.

I checked the relabeled incidence pattern and the complete cubic parametrization in ORBIT6_OBSTRUCTION.md. Sending three quadruple-nodes to infinity, zero, and one leaves the other four finite and distinct. After subtracting P1, the prescribed nonzero word values at those three nodes justify j=1, K!=0, L!=0. Each Q_i gives exactly the two forced roots shared with P1; the remaining two scalar conditions specify its linear quotient. Thus no candidate family is lost.

For T123, equality of the two residual linear roots gives

    Q3(1)/Q3(0) = Q2(1)/Q2(0).

This is exactly the displayed formula v=wz(1-u)/(wz-u(w+z-1)); its denominator cannot vanish because u!=1. T147 and T156 have quotients with the same nonzero leading coefficient L, so their common root forces equality of those quotients, giving both equations (2).

The subsequent branch split is exhaustive. In the G=0 branch all divisions are by distinct-node guards. Substituting its K into the leading coefficient of P2 gives

    [(u-w)(z-1)-w(z-u)]/[w^2 z(z-u)]
      = [u(w+z-1)+w-2wz]/[w^2 z(z-u)] = L.

This is an inadmissible additional equality with the selected quadruple at infinity. Every pair already has its three distinct prescribed projective roots, so such an additional root is impossible, including when the pair's affine degree has dropped.

On the remaining branch u=w/s,v=z/s, s=w+z-1 is nonzero; s=1 would make u=w. I separately implemented all four pairwise polynomial divisions and their linear coefficient determinants, starting directly from the general P_i formulas rather than reusing the author's quotient expressions. Each of the four claimed rational identities has identically zero residual. See `orbit6_root_identity_audit.py/json/resources`; the bounded run took1.72seconds and about63MiB.

All denominators in those identities are guarded nonzero. D245 forces A+H=0, while H=(w-1)(z-1)(s-1) is nonzero. Hence A-H=-2H is nonzero in odd characteristic. The remaining identities force F3=F4=0; cancelling only nonzero w,z,w-1,z-1 gives w(w-1)=z(z-1), contradicting (w-z)s!=0.

This verifies the whole branch analysis and the exact determinant arithmetic. It excludes orbit6 only. It does not assert that unresolved orbits have been eliminated.
