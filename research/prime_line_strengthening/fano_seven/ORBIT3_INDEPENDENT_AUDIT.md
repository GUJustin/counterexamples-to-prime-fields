# Independent audit of the global orbit-3 obstruction

Verdict: PASS, in every characteristic different from two.

Independently reviewed ORBIT3_OBSTRUCTION.md, the complete row/minor output in nonfano_involution_3.json, and nonfano3_exact_minors.json against the geometric construction.

The three pair-root quadratics at triple156 are pairwise coprime and dependent. Their degree-two pencil is separable in odd characteristic, with an involution exchanging each prescribed root pair. Neither fixed point belongs to those six roots; at least one is different from the seventh quadruple node. Sending that fixed point to infinity and the other to zero therefore gives the stated finite coordinates (u,-u,d,v,z,-v,-z) without losing a chart.

Interpolation of the seven quadruple values, followed by subtraction of its degree-at-most-three part, gives exactly the three amplitudes of aX^4+bX^5+cX^6. The amplitudes cannot all vanish because then all seven candidate cubics coincide. For each remaining triple, dividing pair differences by the common triple factor gives the identity A V-B U=0 described in the note: evaluation at the single root q fixes the ratio of the other two quadratic factors. This also holds for a triple point at infinity, using homogeneous cubics. Every selected coefficient is X^5, and all six row contents in the saved output equal 1. No geometric factor is silently discarded in constructing the matrix.

The exact minor M012 has precisely the displayed guarded factors times F G. On D_F=0, N_F=-2z(v+z)^2 is nonzero. On D_G=0, solving for v is legitimate because u-z is nonzero, and N_G=-4uz(u+z)^2/(u-z) is nonzero. Hence the two rational branches are exhaustive even at their apparent denominator loci.

The saved exact branch minors have scalar factors 16, -2, and -2 as stated. Every remaining factor in the G-branch minor is a distinct-node guard. In the F branch, J=D_F(d+z) is also guarded; consequently the two remaining cubic factors E1,E2 must vanish. Their sum is 4(u-v)(uv-z^2). Substitution v=z^2/u into E1 gives -z(u+z)^2(u^2+z^2)/u^2. Thus v=-u, a forbidden collision. This final collision is v=-u (not v=u).

The proof is global over the algebraic closure, permits triple points at infinity, and excludes only characteristic two. It does not rely on a rational sample or a generic denominator assumption. No additional numerical job was needed for this audit.
