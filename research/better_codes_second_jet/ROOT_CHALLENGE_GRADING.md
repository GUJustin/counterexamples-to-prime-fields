# Preserve total jet degree when counting challenge constraints

The restricted substitution Y=tR-t^2V+t^3E is homogeneous in total jet degree ell=deg(Y,R,V)=deg(E,R,V). Let R_ell denote the rank of its truncated local map on the ell-homogeneous source component, with the stated slope and curvature caps.

For a source with total degree deg(Y,R,V,Z)<=L and jet degree <=J, translating Y by f_x+Z g_x preserves total degree in Y,R,V,Z and never increases jet degree or either derivative cap. Thus, after translation, the coefficient of Z^z in jet degree ell belongs to the same allowed local ell-component and z<=L-ell. The image therefore lies in a direct sum of spaces of dimension

    sum_{ell=0}^{min(J,L)} (L+1-ell) R_ell.

This is a uniform sufficient local constraint bound, independent of f_x,g_x. It improves the conservative (L+1) sum R_ell bound. It does not require independence of the translated source coefficients, because enlarging their image to the full direct sum is an upper bound.

If C_ell is the weighted scalar source coefficient count in degree ell, a sufficient line-source dimension surplus is

    sum_ell (L+1-ell) (C_ell-n R_ell).

For L>=J this equals (L+1)(C-nR)-sum ell*C_ell+n*sum ell*R_ell. A bound on R alone is insufficient to recover the last term: use exact homogeneous ranks or a per-degree upper bound directly in the weighted sum. Any new kernel argument must preserve its degree indexing.

This establishes a source-existence counting refinement, not a second-derivative routing/factor theorem or a better.codes improvement. Numerical use awaits the independent audit and homogeneous rank accounting.

## Independent integer check at the representative finite gate

Root independently enumerated source monomials and the first-jet quotient rectangles (without invoking the certificate script) at m=128,S=40,J=177,L=5515. The totals are C=133261059668, M=9482670227536, upper-profile R=507092 and T=29231284. Therefore the certified line-source dimension is 53746080. This checks arithmetic for the proved sufficient source gate only.

In the full finite ambient source box, received-value translation is invertible: its inverse subtracts the same f_x+Zg_x and preserves all the same caps. Thus the graded ambient rank is actually unchanged by translation. Only restriction from that ambient box to the weighted global coefficient space requires an upper bound.
