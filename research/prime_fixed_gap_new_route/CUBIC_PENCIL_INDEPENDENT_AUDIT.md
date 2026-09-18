# Independent cubic-pencil count audit

The proposed bound of **33 polynomial sections** is valid under the following explicit hypotheses. Let K have characteristic zero or characteristic greater than 3, D>=1, A_1,A_2,A_3 in K[X] have degree at most D, and

`F(X,u)=∏_(i=1)^3 (u−A_i(X))`.

Let H in K[X] be squarefree of degree exactly 3D. Assume the **original** affine ideal

`(F_u, H F_X−H' F)`

defines a zero-dimensional scheme over the algebraic closure. Then there are at most 33 polynomials P of degree at most D for which F(X,P)=cH for some constant c. The bound includes c=0.

## Scheme count

The two generators have bidegrees bounded by (2D,2) and (6D−1,3). Their proper intersection in P¹×P¹ has length at most

`(2D)*3 + 2*(6D−1) = 18D−2`.

Use actual bidegrees when homogenizing; neither homogenization then contains an entire boundary divisor. Zero-dimensionality in the affine chart rules out any other common component. Consequently the affine scheme length is at most this number.

Fix a section P with c!=0. If F_u(x,P(x))=0 and H(x)=0, then F(x,P(x))=0. The split factorization forces at least two factors u−A_i to vanish at this point, whence F_X also vanishes there. Differentiating the section identity would give 0=cH'(x), contradicting squarefreeness. Thus all roots of F_u(X,P(X)) avoid H.

Modulo u−P(X), differentiation gives

`H F_X−H' F = −H F_u(X,P) P'`.

The intersection of the critical scheme with the section graph therefore has coordinate ring exactly Kbar[X]/(F_u(X,P)). Its length is deg F_u(X,P), counting repeated roots with their multiplicity. Distinct constants c give disjoint such schemes: at a common support point one would have (c−c')H=0, impossible away from H.

## Leading exceptions

Let a_i be the X^D coefficient of A_i (possibly zero), h the nonzero X^(3D) coefficient of H, and q(T)=∏(T−a_i). For a section P, write lambda for its X^D coefficient. Comparing leading coefficients gives c=q(lambda)/h. The X^(2D) coefficient of F_u(X,P) is q'(lambda).

Since characteristic is not 3, q' is a nonzero quadratic. At most two constants c can occur with q'(lambda)=0. Outside those constants every section contributes length 2D to the critical scheme. Choosing one section for each distinct generic constant gives at most floor((18D−2)/(2D))=8 such constants. Adding at most two exceptional nonzero constants leaves at most ten nonzero constants.

For each fixed c, the monic cubic F(X,u)−cH has at most three distinct polynomial roots over Kbar(X). Thus there are at most 30 nonzero-c sections. At c=0 the only sections are the distinct seed polynomials A_i, giving at most three more.

## Required qualifications

- Splitting into the three polynomial seeds is essential to the H-root exclusion above. A general monic cubic does not imply F_X=0 from F=F_u=0.
- Do not divide content or remove components from the critical generators and then apply the same length argument without proving that all section-graph multiplicities survive. The hypothesis here is on the original ideal.
- Squarefree H and its exact degree 3D are used separately: the former at finite roots, the latter in the leading-coefficient relation.
- No p>D assumption is needed. Characteristic zero or p>3 suffices for this argument.
- The zero-dimensionality assumption is substantive. This is a conditional count, not a classification or exclusion of positive-dimensional critical loci.

No numerical experiment is needed for the proof, and no benchmark or affine-line consequence is asserted here.

## Independent audit of the general N>D extension: PASS

The extension in `research/short_domain_cubic_source/SPLIT_CUBIC_PENCIL.md` is valid, with the same original-critical-ideal, split-seed, squarefreeness, and characteristic assumptions. It gives at most **69 sections** when N=deg H>D. No correction to the valuation argument is required.

Here is an independent check of its delicate step. Work in one fixed valued algebraic closure of Kbar((1/X)), so all sections use the same two algebraic roots of F_u and the same residue map. For a section P put A=F_u(X,P), d=deg A, and b=3P−ΣA_i. The polynomial A cannot vanish identically: differentiation would then put the whole section graph inside the critical scheme. Thus d>=0. Let e=deg b, allowing e=−infinity. The two roots delta_1,delta_2 of `3 delta²+2b delta+A=0` have product A/3 and sum −2b/3.

If 2e>d, their infinity degrees must be e and d−e: unequal root degrees make the larger equal the degree of the sum, whereas equal degrees would contradict the product degree. If 2e<=d, neither root can have degree greater than d/2: unequal degrees would give a sum of degree greater than e, while equal larger degrees would contradict the product. These arguments work for ramified rational valuations as well as integral degrees.

Choose the smaller root in the first case and either root in the second. The exact cubic identity gives

`F(P+delta)−cH=−b delta²−2 delta³`.

Its infinity degree is at most 3d/2 (strictly less in the first case). Therefore d<2N/3 implies that `F(P+delta)/H` is regular at infinity with residue c. Since P+delta is one of the two **fixed** critical roots of F_u, there are at most two possible exceptional residues. Conjugacy causes no extra choices: both roots are already included in the fixed valued algebraic closure. A repeated critical root reduces, rather than increases, this number.

All remaining nonzero constants consume at least ceil(2N/3) critical-scheme length each. The bidegree bound is now 2N+12D−2. Because D<N,

`(2N+12D−2)/(2N/3) < 21`,

so at most twenty generic constants, plus at most two exceptional constants, occur. At most three sections per constant and at most three zero-fiber seeds yield `3*(20+2)+3=69`. If N>3D, no nonzero section exists already by degree comparison, so the conclusion remains valid.

The section-graph multiplicity and H-root exclusion from the earlier audit apply unchanged. This closes the proposed lower-degree-H escape only for this split, squarefree, zero-dimensional-critical-locus class; it is not a theorem about arbitrary cubic differential equations.
