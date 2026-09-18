# Mapping the new curvature-one source to the restored second-jet route

The restored route is present in cached LowerGeometry.lean and research/better_codes_current_lower_2026_09_17/SecondJetRefinements.lean. It was formulated at agreement181353. Porting the numerical target to181275 is required; this note does not claim that the old fixed constants already prove the target result.

The restored variable order is (X,V,Y,R,Z). Its interpolant support requires

    2*deg_V+deg_R≤B, deg_V≤s,
    deg_V+deg_Y+deg_R≤U,
    deg_V+deg_Y+deg_R+deg_Z≤L,

and weighted cutoff

    wt + reserve(k,n0,deg_V)*(A−(w−2)) < mA,
    reserve(k,n0,h)=h if h<n0, and k otherwise.

The current rectangular curvature-one source with first-derivative cap S and total jet cap J fits

    s=1, B=S+2, U=J, k=0, n0=1.

Both curvature levels then have zero reserve; the required derivative identities are only the original d=0 source identity. All elementary shape inequalities in the restored interface are satisfied for the current shapes. The source need not fill the entire relaxed flag: membership of the actual source in that support is sufficient once its independent existence proof is supplied.

For the representative m128,S40,J177,L5515 source this gives

    (m,B,s,U,L,k,n0)=(128,42,1,177,5515,0,1).

However `helper_or_divisibility` / `count_of_interpolant_total` require L<wt_total(F) for the left factor. At the binding context the factor total degree is3261, so5515<3261 fails. The current source does not activate that total-avoidance route at the critical singleton.

The retained branch has budgetFlag(B,U,L,k+1,n0)=(5338,136,42), and k+1=1 gives no derivative-order division gain. These are real costs of the existing route, not a missing generic counting theorem.

Choosing k=1 requires n0≥2. Because s=1<n0, the retained high-curvature branch becomes impossible, but the curvature-one coefficients must reserve one derivative: the new target reserve is A−(w−2)=50206. This forces the leading curvature coefficient to vanish on relevant candidates, converting to a first-order helper. It is not the unreserved source already proved positive. Its dimension gate must be recomputed before use.

The older successful-looking profiles have larger curvature cap (for example s21) and derivative order k5, with joint challenge cap2255. Their activation and retained scaling differ materially from our curvature-one shape. Frontier is checking those old support formulas at the repaired target; one cannot transplant their old numerical certificate unchanged.
