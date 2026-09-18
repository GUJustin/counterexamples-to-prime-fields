# Repeated H does not supply the weighted monic-cubic source on more than D roots

Status: independently audited in REPEATED_H_INDEPENDENT_AUDIT.md. The same proof works for a weighted monic cubic without a split-factor assumption. It addresses polynomial first-integral sections, not arbitrary cubic differential equations.

Let k be algebraically closed of characteristic different from 2 and 3. Let

    F(X,u)=u³+a2(X)u²+a1(X)u+a0(X),
    deg a2≤D, deg a1≤2D, deg a0≤3D, D≥1,

and let nonzero H have degree N. Let n0 be the number of distinct roots of H and assume n0>D. Suppose the ORIGINAL ideal

    I=(F_u, H F_X−H′F)

is zero-dimensional. No squarefreeness of H is assumed. Then the number of degree-at-most-D polynomial sections P with F(X,P)=cH for a constant c is at most

    9 + 3 floor((4N+24D−4)/(n0−floor(N/3))),       (1)

provided a nonzero-label section exists. Such a section forces N≤3D; hence a simpler bound is

    9 + 108D/(n0−D).                            (2)

If no nonzero-label section exists, only the at most three polynomial roots of the zero fiber occur.

For an evaluation domain contained in the distinct roots of H and having length n>D, replace n0 in (2) by n to obtain a weaker valid bound. Thus at fixed rate D/n≤rho<1 the entire proposed bank has bounded size, before considering the received word. Repeated-root multiplicity cannot provide a growing fixed-gap source under these hypotheses.

## 1. Fixed critical length and the infinity debit

The existing argument gives the critical-scheme length bound

    ell=length k[X,u]/I ≤2N+12D−2.               (3)

For any section write A=F_u(X,P). It is nonzero, because otherwise its entire graph lies in I. Substitution gives

    (H F_X−H′F)(X,P)=−H A P′.

The local quotient on the graph therefore has length ord_x A at every zero x of A; this length is at most the local critical-scheme length at (x,P(x)).

The previously proved infinity valuation lemma applies without squarefreeness of H: except for at most two constant labels,

    deg A≥ceil(2N/3).                           (4)

For completeness, Taylor expansion gives F(P+Z)=cH+A Z+bZ²+Z³, with b=3P+a2. A root delta of A+2b delta+3delta² can be chosen so that the infinity degree of F(P+delta)−cH is at most 3 deg(A)/2. If deg(A)<2N/3, the critical value F(P+delta)/H has residue c at infinity. There are only two fixed critical branches, so at most two such residues.

## 2. Local excess costs can overlap at only two labels

Fix a root x of H of multiplicity m. Put d=ord_x A, and e=ord_x b (infinity if b=0). In a fixed algebraic closure of the local Laurent-series field, choose a root delta of

    A+2b delta+3delta²=0

having larger order. If 2e<d, its order is d−e. If 2e≥d, its order is at least d/2. In both cases, since

    F(P+delta)−cH=−b delta²−2delta³,

this difference has order at least 3d/2. Thus if d>2m/3, the fixed critical value F(P+delta)/H is regular at x and has residue c. Each of the two critical branches contributes at most one such constant residue. Consequently

    ord_x F_u(X,P)>floor(2m/3)

can occur for at most two labels c, even though arbitrarily many labels can pass through the underlying basepoint.

This is exactly the distinction needed for repeated H: ordinary shared critical multiplicity is not charged repeatedly; only the excess above floor(2m/3) is charged.

## 3. Sum the excess and off-basepoint costs

For each nonzero, nonexceptional label choose one section. Define its cost as

    cost(P)=sum_(x not a root of H) ord_x A
            + sum_(x root of H) max(0,ord_x A−floor(2 ord_x H/3)).

At a point off H, the value F/H determines the label, so costs from different chosen labels have disjoint critical support. At a root of H, only two labels have positive excess. Each label's local contribution is at most the corresponding local critical-scheme length. Therefore, summing over all chosen labels,

    sum cost(P)≤2 ell.                          (5)

This bound counts scheme lengths, not merely distinct points; high intersection multiplicities cannot be hidden in it.

For each selected section, (4) gives

    cost(P)≥ceil(2N/3)−sum_(x root of H) floor(2m_x/3)=:r.

Since floor(2m/3)≤m−1 for every positive integer m,

    r≥ceil(2N/3)−(N−n0)=n0−floor(N/3)≥n0−D>0.   (6)

The bound N≤3D comes simply from F(P)=cH with c nonzero. Combining (3), (5), and (6) bounds the number of generic nonzero labels by the floor in (1). Add at most two exceptional labels and the zero label, with at most three sections per label, to obtain (1). Finally N≤3D gives (2).

## Interpretation and remaining exact escape

If nearly every root had multiplicity divisible by three, its degree cost would be at least three per coordinate. More than D such coordinates would force deg H>3D, incompatible with a degree-D section. The local rounding deficit formalizes this resource obstruction and also handles mixtures of larger multiplicities.

The result retains the original zero-dimensional critical-ideal assumption. Positive-dimensional critical components are not removed by division or ignored; they remain outside this proof. No claim is made that all polynomial first integrals satisfy this hypothesis. A new construction would have to exploit that remaining degeneracy or leave the split-cubic constant-first-integral template, rather than merely repeat roots of H. The split source F=product(u−A_j), deg A_j≤D, is a special case of the weighted coefficient hypotheses; no splitting is used in this proof.
