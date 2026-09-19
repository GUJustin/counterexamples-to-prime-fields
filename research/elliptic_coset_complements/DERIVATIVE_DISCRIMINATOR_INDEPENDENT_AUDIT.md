# Independent check of the derivative discriminator

PASS for the stated restricted ansatz. The root agent read the complete
DERIVATIVE_EXTRA_LOCATOR_DISCRIMINATOR.md proof and recomputed its identities.

For U|Phi, the polynomial (Phi/U)U' has exactly the error values Phi'(x) on
the roots of U and zero elsewhere. Hence its proposed witness test is an
equality of actual degree-<n interpolation polynomials. Cancelling the leading
coefficient gives gamma=n/deg U; the prime-field hypotheses ensure this is
nonzero and defined. Syndrome membership in RS_k is equivalent to all n-k
listed moment equations, not just to the early Newton conditions.

Expansion of (Phi'/Phi)' +(Phi'/Phi)^2 gives exactly

    H_j=sum_(i=0)^(j-1) P_i P_(j-1-i)-j P_(j-1),

including H_0=0 and H_1=n(n-1). Newton's recurrence gives c_i leading term
(-A)^i/i!, A=u(n-1). For the displayed F_(d+1), only c_d m_1 has degree
d+1, with coefficient (-1)^d A^(d+1)/d!. The d=0 case is separately the
nonzero linear equation m_1=0. Thus the candidate bound is correct, but it
does not assert that a candidate locator splits or passes later moments.

The small-residue argument also checks: clearing a union of m<=3d poles
gives degree at most k+m-1, versus n-m zeros, with positive difference
4ell-2m. The identity is therefore rational, and its proper rational part
cannot hide a nonzero code polynomial. The moving-pole restriction concerns
only those reduced proper-residue representations, all of which are already
far at the target. The padding argument compares two witnesses of the SAME
received word on the SAME enlarged support; minimum distance then proves
they coincide. It does not rule out a changed source pair or a different base
pair. These scopes are retained in the source note.

No positive line, split family, or far-endpoint separation follows from this
audit. A bounded finite screen of the explicit pencil, if performed, must
report its actual accepted witnesses separately from Newton candidates.
