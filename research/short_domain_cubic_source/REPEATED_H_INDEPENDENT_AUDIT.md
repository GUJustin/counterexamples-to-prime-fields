# Independent audit of the repeated-H multiplicity budget

**PASS.** The bound in `REPEATED_H_MULTIPLICITY_BUDGET.md` is valid with its original zero-dimensional critical-ideal hypothesis. The local valuation threshold, repeated-point accounting, rounding, and final constants all check. No numerical experiment is required.

## Local valuation and strict threshold

At a root x of H with multiplicity m, write A=F_u(X,P), d=ord_x A, and b for the quadratic coefficient in F(P+Z), with e=ord_x b. For a root delta of `A+2b delta+3 delta²=0`, choose the root of larger local order. Sum/product valuations give orders e and d−e when 2e<d, and orders at least d/2 when 2e>=d. In the former case the correction `−b delta²−2 delta³` has order greater than3d/2; in the latter it has order at least3d/2. These statements include b=0 and ramified fractional valuations.

Therefore d>2m/3 makes `(F(P+delta)−cH)/H` have positive valuation, so the fixed critical value F(P+delta)/H is regular and has residue c. In one fixed valued algebraic closure there are only two roots of F_u and thus at most two such residues. No counting of conjugates across different completions is being added. Since d is integral, `d>floor(2m/3)` is exactly the required strict inequality, not a weaker rounded condition.

## Scheme multiplicities and overlap

Restriction of the original critical ideal to the section graph gives exactly `(A)` because `HF_X−H'F=-HAP'` there. Hence each local order d is at most the critical-scheme length at (x,P(x)). At a root of H only two labels can have positive charged excess. Even if both graphs pass through the same critical point, charging each by that point's length costs at most twice the length. At points off H, labels are determined uniquely by F/H. Summing therefore costs at most twice the **whole** affine critical-scheme length. No implicit disjointness at basepoints is needed.

The infinity argument excludes at most two labels and gives degree A>=ceil(2N/3) for all others. Subtracting the uncharged root budget gives cost at least

`ceil(2N/3)−Σ_x floor(2m_x/3) >= n0−floor(N/3)`.

The inequality uses floor(2m/3)<=m−1 for each positive integer m and is valid even when individual multiplicities exceed the characteristic. A nonzero section forces N<=3D, so n0>D makes the denominator positive.

Using critical length at most2N+12D−2, then multiplying labels by at most three roots per cubic fiber, gives exactly

`9+3 floor((4N+24D−4)/(n0−floor(N/3)))`.

The displayed simpler bound `9+108D/(n0−D)` follows from N<=3D and is conservative. The additive9 covers two exceptional nonzero labels and the zero fiber. Characteristic different from2 and3 suffices; no p>D condition is used.

## A valid extension: splitting of F is unnecessary here

The repeated-H proof does not use F=∏(u−A_j). That factorization was needed in the earlier squarefree argument to prohibit all critical points above H. The new excess budget instead charges those points directly.

Consequently the same bounds hold for **any monic cubic**

`F(X,u)=u³+a2(X)u²+a1(X)u+a0(X)`

with polynomial coefficients satisfying `deg a2<=D`, `deg a1<=2D`, and `deg a0<=3D`, provided the original ideal `(F_u,HF_X−H'F)` is zero-dimensional, n0>D, and the characteristic is different from2 and3. All needed degree bounds remain unchanged: F_u has X-degree at most2D, the second critical generator at mostN+3D−1, and F(X,P) at most3D for deg P<=D. The zero fiber has at most three polynomial roots even without splitting over k[X]. The Taylor cubic, its two critical branches, and every valuation step are identical.

This broadens the conditional constant-first-integral theorem. It does not classify positive-dimensional critical loci, remove the coefficient-degree bounds, or bound arbitrary cubic first-order equations.
