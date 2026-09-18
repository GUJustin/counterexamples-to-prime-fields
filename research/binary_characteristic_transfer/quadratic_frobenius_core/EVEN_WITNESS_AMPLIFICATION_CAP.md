# Even-witness cap: scaled-block exponent amplification is closed

Independent audit, September 18, 2026. **PASS.** This decides the proposed amplification through additional scaled Frobenius blocks when the counted witnesses remain of the form aX²+b. It is not a general bound for all quadratic witnesses.

## Exact theorem

Let a received line f+lambda g be evaluated at N distinct field elements. Let C be its ordinary common agreement with degree-at-most-two polynomial explanations. Suppose T>max(C,2). The number M of distinct parameters possessing an EVEN quadratic witness aX²+b with at least T matches satisfies

    M <= N(N-1)(N-2) / [T(T-2)(T-C)].

If common agreement is defined only for even quadratic explanations, that smaller C works as well. The proof holds over any field with the usual distinct-point domain; no Frobenius or extension-field assumption is needed.

## Independent ordered-triple proof

Choose one qualifying even witness per counted parameter and let S be its full match set, of size t>=T. An ordered pair (x_i,x_j) from S with distinct squares has at least t(t-2) choices: each square has at most two distinct field preimages, so each first point excludes at most two choices, including itself.

The two equations

    a x_i²+b=f_i+lambda g_i,
    a x_j²+b=f_j+lambda g_j

uniquely express a and b as affine functions of lambda, because x_i²-x_j² is nonzero. Thus their entire solution set is a pencil P_lambda=F_ij+lambda G_ij of even quadratics. In particular the kernel direction necessarily has nonzero lambda coordinate; no separate constant-label kernel case is possible for these selected pairs.

A coordinate agrees throughout this pencil exactly when F_ij(x)=f(x) and G_ij(x)=g(x). These universally matching coordinates number at most C. Among the t selected matches, at least t-C are outside this universal set. Each gives an independent third equation and hence determines a unique triple (a,b,lambda). These third coordinates automatically differ from the first two.

Therefore the chosen parameter/witness contributes at least t(t-2)(t-C)>=T(T-2)(T-C) ordered triples. The same ordered coordinate triple cannot be counted for two distinct parameter/witness pairs, since its three independent linear equations have a unique solution. There are at most N(N-1)(N-2) ordered triples in all. Division proves the theorem. Choosing only one witness per parameter avoids any unneeded singleton assumption.

## Consequence for the amplification target

If N=Theta(p²), T=Theta(p), and the actual common-agreement gap T-C=Theta(p), then M=O(p³)=O(N^(3/2)). This applies to ANY number or arrangement of scaled blocks, provided the exceptional labels are witnessed by even quadratics. It does not matter whether several block pairs give distinct label families or whether the ambient field grows.

The completed two-block construction already attains this order with T=4p and C<=2p+3. Its M~p³ is therefore exponent-optimal within this two-coefficient witness model at these matched scales. Additional scaled blocks could alter constants or exact spectrum, but cannot improve the exponent while retaining both scales. This is a route-selection conclusion, not a new universal first-order upper bound.

The elementary block accounting is consistent with the cap. With J fixed disjoint scales and distinct constant block directions, a pair of canonical blocks fixes, for each norm-one leading coefficient a, two image values in p-point sets and therefore at most p² witness/label pairs. Summing over a and block pairs gives at most binomial(J,2)(p+1)p² candidates. This counting observation is not needed for the theorem and should not be extended blindly to repeated directions: repeated-direction pencils require common-agreement control, which the ordered-triple proof already supplies.

## What would constitute a real escape

To improve the exponent at the same length, threshold, and common gap, an amplification must obtain a substantial new population from witnesses with a nonzero linear term (or otherwise increase the effective witness dimension). Merely pooling more even Frobenius banks cannot do it. Alternatively one can change the threshold/gap scales, but that is a different parameter contract and must be compared explicitly. This note does not show that a non-even amplification exists, and does not rule out a larger bad probability obtained by reducing field size while retaining the same count.
