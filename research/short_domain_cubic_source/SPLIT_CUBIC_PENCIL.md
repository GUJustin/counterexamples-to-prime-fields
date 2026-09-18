# Split cubic first-integral pencils: an exact generator and a finite-section gate

## A characteristic-zero actual-equation generator

Let K be algebraically closed of characteristic zero or greater than three. Choose A_1,A_2,A_3 in K[X], each of degree at most D, and put

    F(X,u)=product_{j=1}^3(u−A_j(X)).

Choose nonzero H in K[X]. Every polynomial section

    F(X,P(X))=c H(X), c in K,

satisfies the common first-order equation

    Q(X,u,v)=H F_u v+H F_X−H′ F=0.               (1)

Its total jet degree is at most three and its derivative degree is one. At a root x of H, a received value chosen from {A_1(x),A_2(x),A_3(x)} makes (1) vanish identically in v. Thus this is an actual ordinary-core generator, not a collection of unrelated coordinate equations.

If H is squarefree and gcd(F_u,H F_X−H′F)=1 in K[X,u], Q is primitive and irreducible as a polynomial linear in v. No X-polynomial can divide both coefficients: the leading u coefficients include 3H and −H′, which are coprime. The additional gcd excludes common factors with positive u degree.

A source would require unboundedly many distinct sections, a root domain E of size Theta(D), and a branch word with at least D+eta|E| agreements per selected section. It would also need an actual specialization argument preserving these identities and agreements at arbitrarily large splitting primes. The scaled family P=b+alpha h does not provide this: its distinct values coincide only at zeros of h, and its apparent bank has the familiar common-factor agreement obstruction.

## The full-degree, primitive regime has at most 33 sections

**Proposition.** Suppose D≥1, deg H=3D, H is squarefree, and the critical ideal

    I=(F_u, H F_X−H′F) in K[X,u]

is zero-dimensional (the unit ideal is allowed). Then there are at most 33 polynomial sections P of degree at most D with F(X,P)=cH for some c in K. This includes the at most three sections in the c=0 fiber. In particular this regime cannot yield a growing bank.

The hypotheses include the split form of F. The assertion does not cover a general monic cubic with unrelated coefficients, a critical ideal with a curve component, or deg H<3D.

### 1. Critical-scheme length

Write B=H F_X−H′F. The bidegrees in (X,u) satisfy

    bideg F_u ≤(2D,2),
    bideg B ≤(6D−1,3).

The affine intersection length is bounded by the product-intersection number of their closures in P^1×P^1:

    length K[X,u]/I ≤(2D)*3+2*(6D−1)=18D−2.       (2)

Only isolated affine intersections are counted; points at infinity can only consume additional projective intersection multiplicity. One may use the actual bidegrees, which are no larger than the displayed caps.

### 2. A section uses the critical scheme with full multiplicities

On a section F(X,P)=cH, differentiation gives

    F_X(X,P)+F_u(X,P)P′=cH′,
    B(X,P)=−H F_u(X,P)P′.

Therefore substitution u=P induces a surjection

    K[X,u]/I -> K[X]/(F_u(X,P)).                 (3)

When F_u(X,P) is a nonzero polynomial, this quotient has length deg F_u(X,P), counting all repeated roots.

For c≠0, none of these roots lies on H=0. Indeed if H(x)=0 and F_u(x,P(x))=0, then F(x,P(x))=0 and the SPLIT factorization forces at least two factors P(x)−A_j(x) to vanish. Hence F_X(x,P(x))=0 as well. Differentiating the section would then give 0=cH′(x), contradicting squarefreeness of H.

Consequently sections with different nonzero c have disjoint critical supports: at any such point H≠0 and c=F/H is determined by that point. Taking one section for each distinct c, their quotient lengths from (3) can therefore be summed and remain bounded by (2). We do NOT sum over different sections in the same fiber, which may share a critical point. For example, two branches through a node would invalidate such a sum.

### 3. Only two leading critical values are exceptional

Let a_j=[X^D]A_j, h=[X^(3D)]H≠0, and

    f_infinity(T)=product_j(T−a_j).

For any degree≤D section write alpha=[X^D]P, permitting alpha=0. Comparing degree-3D coefficients gives

    f_infinity(alpha)=c h.

Moreover the coefficient of X^(2D) in F_u(X,P) is f_infinity′(alpha). The monic cubic f_infinity has nonzero derivative of degree two in the stated characteristic. Thus there are at most two exceptional values

    c=f_infinity(alpha)/h with f_infinity′(alpha)=0.

For every other c admitting a section, deg F_u(X,P)=2D. Picking one section for each nonzero nonexceptional c and applying (2),(3) gives

    (# such c)*2D≤18D−2,

so there are at most eight such c. Together with the at most two exceptional values, at most ten nonzero parameter fibers admit sections. Each cubic F(X,u)−cH has at most three roots in K(X), hence at most three polynomial sections. Finally F(X,P)=0 forces P to equal one of A_1,A_2,A_3, giving at most three more. This proves 33.

## General viable degree: at most 69 sections when deg H>D

The lower-degree-H escape can also be closed within the same primitive squarefree split-pencil class.

**Stronger proposition.** Under the same assumptions on K, D, the split cubic F, squarefree H, and zero-dimensional original critical ideal, replace deg H=3D by

    N=deg H>D.

Then there are at most 69 polynomial sections of degree at most D across all constant fibers. If any nonzero fiber has such a section, necessarily N≤3D. The previous bound 33 is sharper when N=3D.

The critical-scheme argument and exclusion of H-root critical points are unchanged. Its length now satisfies

    length K[X,u]/I≤(2D)*3+2*(N+3D−1)=2N+12D−2.  (4)

The following valuation lemma replaces the degree-3D leading-coefficient calculation.

### Critical values at infinity control every low-cost section

Fix an algebraic closure of the Laurent-series field K((1/X)), with the extended infinity valuation. Write deg_infinity R for the negative valuation, normalized by deg_infinity X=1. This can be rational for an algebraic function. Its residue field is K because K is algebraically closed. The two roots of the quadratic F_u in this field are fixed algebraic critical branches, independent of the section being considered.

For a section P with F(P)=cH, put

    A=F_u(X,P),  b=3P−A_1−A_2−A_3.

Here A is nonzero: otherwise differentiating the section would also make B(X,P)=0, putting its entire graph in the supposedly zero-dimensional critical locus. Write d=deg A≥0 and e=deg b, with e=−infinity if b=0. The exact Taylor expansion is

    F(X,P+Z)=cH+A Z+b Z²+Z³.

Choose a root delta of A+2b delta+3delta²=0 of smaller infinity degree. The coefficients 2 and 3 are nonzero in the stated characteristic. The root product is A/3 and their sum is −2b/3. Consequently:

* If 2e>d, the two root degrees are e and d−e, so choose deg_infinity delta=d−e.
* If 2e≤d, both roots have degree at most d/2.

These statements follow directly from sum and product valuations (or the quadratic Newton polygon) and do not assume an unramified extension. Using the critical equation,

    F(X,P+delta)−F(X,P)=−b delta²−2delta³.

In the first case its infinity degree is at most 2d−e<3d/2. In the second it is at most 3d/2. Hence in both cases

    deg_infinity [F(X,P+delta)−cH]≤3d/2.        (5)

If d<2N/3, then F(X,P+delta)/H−c has negative infinity degree. Thus the critical value F(X,P+delta)/H has residue c. But P+delta is one of the two fixed roots of F_u. Each corresponding critical value has at most one residue when regular at infinity. Therefore at most two constants c can admit a section with

    deg F_u(X,P)<2N/3.                          (6)

This is a statement about two algebraic branches in one fixed valued algebraic closure, not an assumption that the critical points themselves are rational or polynomial.

### Count the remaining fibers

For every nonzero c outside those at most two exceptional critical residues, any section has

    deg F_u(X,P)≥ceil(2N/3).

Choose one section for each such c. Their critical supports are disjoint, as established above, so (3),(4) give

    (# generic nonzero c) ceil(2N/3)≤2N+12D−2.

Since N>D,

    (2N+12D−2)/(2N/3)=3+18D/N−3/N<21.

There are therefore at most twenty generic nonzero c, and at most two exceptional nonzero c. Each fiber has at most three polynomial roots. Including the at most three zero-fiber seeds gives at most

    3*(20+2)+3=69

sections in total.

## Consequence for the proposed source mechanism

A source obtained by evaluating on a set E of roots of H with agreement above D necessarily has |E|>D and hence deg H>D. Thus the 69-section theorem closes the entire primitive, squarefree, split-cubic pencil route proposed here, including cancellations at infinity. It is stronger than the initial generic degree-3D check and requires no conclusion of isotriviality.

This does not bound arbitrary cubic first-order ODEs. It uses the constant-first-integral identity F(P)=cH, the split cubic form, squarefree H, and zero-dimensional ORIGINAL critical ideal. A positive-dimensional critical locus cannot be deleted silently: dividing global factors out of the ODE may alter the ordinary-core fibers, and the proof does not apply to a content-divided surrogate ideal. Repeated H or a genuinely nonintegrable cubic equation remains outside the theorem. No scalable new source or prime-field lower bound is established by this attempt.
