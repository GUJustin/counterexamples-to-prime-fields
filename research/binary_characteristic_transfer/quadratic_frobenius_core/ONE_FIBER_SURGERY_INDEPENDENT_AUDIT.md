# One-core-fiber surgery: independent exact-profile audit

PASS. This supersedes deletion of two full endpoint supports: delete only one carefully selected nonzero core fiber. Use the original Fp3 construction and notation in `fp3_common_agreement.tex`, with p≥4099,

    N=2p²−p−1, A=2p−ceil(4sqrt(p))−2,
    Lambda0=(delta/u0)F_p, u1=eta*u0,
    I_u1=(delta/u1)F_p, eta I_u1=Lambda0.

The lines I_u1 and Lambda0 are distinct. Pick nonzero bstar∈I_u1 whose core fiber Sstar has at most p physical coordinates. Such a choice exists: its p−1 nonzero fibers partition p²−p coordinates, so their average size is p. Set Qstar=a_u1 X²+bstar and delete Sstar only.

The new length and threshold are

    N'=N−|Sstar| >=2p²−2p−1,
    T=A−2=2p−ceil(4sqrt(p))−4.

Let C=p+2sqrt(p). The exact list spectrum at threshold T is:

* p empty lists, at the affine coset bstar+Lambda0;
* p³−2p singleton lists;
* p lists of size p, at Lambda0.

Thus the raw affine line has exactly p far parameters, exactly p³−p qualifying parameters, near fraction 1−p^(−2), and singleton fraction 1−2p^(−2). Each of the p far words has agreement at most C. Ordinary common agreement remains at most C.

## Proof of the three cases

Every label in bstar+Lambda0 is generic (outside Lambda0), because bstar lies on a distinct line. As v ranges over I_u1 these p labels are precisely bstar−eta*v. Their unique original high witness is the SAME Qstar. Deleting Sstar removes its full core support. Its remaining fresh support has size at most C. Every other quadratic at these generic labels was already below max(16,C)=C by the original all-witness classification. All p lists are therefore empty at T>C.

For any other generic label, let Qlambda be its unique original high witness. If its slope differs from a_u1, a point of Sstar matching Qlambda must satisfy Qlambda=Qstar: both raw words equal f on D0 because g=0 there. This is a nonconstant quadratic equation with nonzero leading coefficient, so at most two matches are deleted. If its slope equals a_u1, its core intercept is different from bstar, and the two core fibers are disjoint. Thus in either case at least A−2=T matches remain. Every competing quadratic stays below C. There are p³−p generic labels originally and exactly p in the erased coset, leaving p³−2p singletons.

At a label of Lambda0, the original list has exactly p members. Any member of slope different from a_u1 loses at most two core matches by the same difference argument. The member of slope a_u1 has core intercept b=0: decomposition lambda=b−eta*v in I_u1+eta I_u1 forces b=0 since lambda∈eta I_u1 and these lines are distinct. Its core fiber is disjoint from Sstar. Hence all p old list members retain at least T matches. The originally excluded u0 candidate still has at most C matches, and all other competitors still have at most C or sixteen; puncturing cannot increase these counts. Therefore each of these p lists still has exactly p members.

This exhausts all p³ labels and proves the exact spectrum. Notice that the earlier caveat about unknown survivors inside a discarded plane no longer applies: the one-fiber operation has been checked for every generic and every exceptional parameter.

## Far endpoints and interpretation

Any two distinct labels alpha,beta in bstar+Lambda0 give two far endpoint words f+alpha*g and f+beta*g, both with agreement at most C. Their affine-mixture parameterization is a bijective affine transformation of the raw parameter, preserving the entire exact spectrum and ordinary common agreement. Thus there are p available far points on this affine line, not merely two.

If instead using the non-affine pencil F+tG of the two far endpoint words, its projective-infinity parameter is the step direction and must be handled separately; the raw/affine-mixture exact profile above should not be copied unchanged to that parameterization. The both-far conclusion itself is unaffected.

## Finite thresholds

This deletion is smaller and the threshold is larger than in the independently audited two-support version. Directly, T≥2p−5sqrt(p), N'≤N, so the original first-order upper estimate remains below T for p≥4099. Since N'≥2p²−2p−1 and T≤2p−sqrt(p), the Johnson inequality T²<2N' also follows at this onset.

For a finite certificate take m=6, derivative cap3, B=3T and H=40B. The counts remain G=4B²−2B and R=62. We have 29p/5≤B≤6p, and N'≤N; therefore

    39G−40*62N' >=(7196/25)p²−468p>0,

implying the strict graded row test (H−B+1)G>(H+1)62N'. Reconstruction requires only p>3. No manuscript edits or numerical scans were needed for this audit.
