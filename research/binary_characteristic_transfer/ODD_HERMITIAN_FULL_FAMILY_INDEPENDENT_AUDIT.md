# Full monic Hermitian family: independent algebra and compiler audit

2026-09-19. **PASS with an explicit source shift for the nonzero-label claim.** No manuscript edits or family enumeration.

Let p be odd, B=Fp², E=Fp4, beta∈E\B, Λ=X^(p²)−X, K=p²−2p, R=X^(p²−p). For s∈B and c∈Fp with c−s^(p+1)≠0, set

    G=X^(p+1)+s X^p+s^p X+c, F=X+s,
    J=Λ/G, P=FJ, C=P−R.

## Family, degrees and exact native matches

G=(X+s)^(p+1)+c−Norm(s). Its nonzero norm radius gives exactly p+1 distinct roots in B. Its derivative is X^p+s^p=F^p. The monic family has exactly p²(p−1) distinct members.

The identity G^p−G=F^p Λ gives

    P^p=Λ^(p−1)(1−G^(1−p)).

Also deg P=p²−p and its leading coefficient is one. To verify the full coefficient gap directly, subtract R G from ΛF: the remaining terms have degree at most p²−p+1. Dividing by monic G of degree p+1 proves deg C≤p²−2p=K. Finally G(−s)=c−Norm(s)≠0, so −s is already a root of J. Consequently P has exactly

    T0=p²−p−1

distinct native roots; multiplying by F adds multiplicity, not another distinct root.

## Pole evaluation is injective

Neither G(beta) nor P(beta) nor Λ(beta) vanishes, since their roots lie in B. If two P-values at beta coincide, the displayed pth-power identity gives G1(beta)/G2(beta)=a∈Fp*. For a≠1, (G1−aG2)/(1−a) is another monic Hermitian polynomial with its constant in Fp, so all its roots are in B, including the possible zero-radius repeated-root case. For a=1 and unequal s, the difference is a nonzero affine trace polynomial, with all p roots in B. For equal s and unequal c it is a nonzero constant. Thus a root at beta is impossible unless a=1 and G1=G2. Hence the p²(p−1) values P(beta) are distinct and nonzero.

## Exact compiler convention and common agreement

To use those nonzero values literally as labels, take

    f=(R−R(beta))/(X−beta),  g=1/(X−beta),
    lambda_G=P(beta),
    h_G=−(C−C(beta))/(X−beta).

The witness has degree<K and f+lambda_G*g−h_G=P/(X−beta). Thus each certified label has exactly T0 matches with its displayed witness. This does not classify the full nearest-codeword agreement or list. If instead f=R/(X−beta) is used, the corresponding labels are C(beta); they remain distinct, but their nonzeroness does not follow from P(beta)≠0. The shift above removes that ambiguity.

Every degree<K approximation h to g has at most K matches because (X−beta)h−1 is a nonzero polynomial of degree≤K. Interpolation on any K domain points attains K, so agreement(g)=K. Ordinary common agreement(f,g)=K: g gives the upper bound, and simultaneous independent interpolation on K selected coordinates gives the lower bound.

For two individually far endpoints, pass to E'=Fp8=E⊕theta E and take r0=f+theta*g and r1=f+(theta+1)*g. Projecting polynomial coefficients onto the theta coordinate bounds each endpoint's agreement by agreement(g)=K; interpolation attains K. Their common agreement is also K by the invertible source transformation. Their affine pencil has the same certified p²(p−1) distinct labels after lambda=theta+z. These labels are not endpoints. This is an alphabet-extension argument, not a claim of two far endpoints in E from the same projection.

## Placement and scope

For the strict integer threshold T=T0−1=p²−p−2,

    (K−1)p²−T²=2p²−4p−4>0  (p≥3),

so it lies below the finite Johnson threshold. With rho=K/p² and a=T/p², the first-order polynomial is exactly

    (8−rho)a²−6rho*a−rho(5−4rho)
       =−(p−2)(p+2)(9p+2)/p⁵<0.

For p≥3 these rates lie on the high-rate branch, so this is below first order. For p≥5, K>p; p=3 is the equality case K=p. Thus no large-characteristic DKT claim is supported. This family supplies N^(3/2) certified labels and exact source/common values after the stated extension, but not above-first-order placement or singleton/full-list classification.


## Appendix: fixed-rate common-agreement shortening loses the superlinear bank

For the complete monic Hermitian circle family, there are C0=p²(p−1) circles, each of size p+1. A point lies on exactly p²−1 circles: every center other than the point supplies its unique nonzero radius. Two distinct points lie on exactly p circles. Indeed the equal-distance equation is a nonzero affine trace equation in the center, with p solutions; neither endpoint can be an equal-distance center, so none of these radii is zero.

For a fixed native subset S of size m>0, let r_G=|S∩Z(G)|. Exact double counting gives

    sum r_G=(p²−1)m,
    sum r_G²=p m²+(p²−p−1)m,
    mu=m(p+1)/p²,
    sum (r_G−mu)²=(p²−p−1)m(1−m/p²).

Consequently the number Z of circles disjoint from S satisfies

    Z≤p²(p²−p−1)(p²−m)/(m(p+1)²).

For m≥alpha*p² with fixed alpha>0, this is O_alpha(p²), instead of the full family's Theta(p³). The displayed witnesses match precisely outside their omitted circle, so a common set of agreement coordinates S requires exactly this disjointness condition. Thus removing a fixed positive fraction of common agreement positions and reducing the code dimension accordingly cannot retain a superlinear number of these canonical witnesses. This is a limitation of common-agreement shortening of this bank; it does not constrain arbitrary puncturing, new witnesses, or other received pencils.
