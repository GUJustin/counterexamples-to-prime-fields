# Adversarial audit of the arbitrary-word cubic section bound

**Later strengthening:** the final list theorem uses `p>max(3,2D)`; see `TWO_D_RADICAL_BUDGET.md`, its independent audit, and `general_cubic_list.tex`. The stronger characteristic assumptions in this earlier argument remain valid sufficient conditions.

**PASS under the stated hypotheses.** Independently checked the three
notes `ARBITRARY_WORD_CUBIC_LIST.md`,
`REPEATED_H_MULTIPLICITY_BUDGET.md`, and
`CRITICAL_COMPONENT_CONSTANT_VALUE.md`, together with the proof of the
three-cubic-cover lemma. No counterexample or mathematical gap was found.
This is a proof audit, not a numerical or formal verification.

The conclusion is restricted to polynomial sections of a weighted monic
cubic first integral F/H. It is not a statement about arbitrary cubic
ODEs. The bound on coefficients and p>max(3,6D) are used essentially in
the positive-dimensional case.

## 1. Local valuations: no Puiseux theorem is required

Fix one extension of the local valuation to an algebraic closure of
k((X-x)), normalized by ord(X-x)=1. Put A=F_u(P), b=3P+a2,
d=ord(A), e=ord(b). The two roots of

    A+2b delta+3 delta^2=0

are the differences between P and the two fixed roots of F_u. For
2e<d their orders are e and d-e, so choosing the larger gives correction
-b delta^2-2 delta^3 of order at least 2d-e>3d/2. For 2e>=d both
orders are d/2 (the weaker claimed lower bound is sufficient), and
both terms of the correction have order at least 3d/2. Cancellation
can only improve this lower bound. The case b=0 is included.

These are quadratic sum/product or Newton-polygon statements in a
valued field. They require neither infinite Puiseux expansions nor
separability of a map defined by P. In characteristic p>3 the quadratic
extensions involved are tame; a repeated root simply lies in the base
field. Arbitrarily large multiplicities of H cause no issue.

If d>floor(2m/3), then 3d/2>m. Thus a fixed critical value F(r)/H
has residue c. In this ONE valued algebraic closure there are at most
two critical roots and therefore at most two possible residues. It
would be invalid to sum residues from newly chosen places for each
section, but the proof does not do this.

At infinity use degree=-valuation. If 2e>d choose the root of smaller
degree d-e, giving correction degree <=2d-e<3d/2. Otherwise each
root has degree <=d/2, giving correction degree <=3d/2. Hence
deg A<2N/3 identifies c with one of at most two fixed critical residues
at infinity. This justifies the global two-label exception.

## 2. Original critical scheme and multiplicity charging

Let I=(F_u,B), B=HF_X-H'F. Substituting the section gives

    B(X,P)=-H F_u(X,P) P'.

Consequently k[X,u]/(I,u-P) is exactly k[X]/(A). Localization at
(x,P(x)) is a quotient of the localized critical algebra, so ord_x A
is bounded by its local length. This remains true when P'=0, when H
has repeated roots, or when the section is tangent to the critical locus.
If A were identically zero, the entire section graph would lie in I,
contradicting zero dimensionality.

The bidegrees of F_u and B are at most (2D,2) and
(N+3D-1,3). Their isolated affine intersection length is at most

    (2D)*3+2*(N+3D-1)=2N+12D-2.

One may homogenize using actual bidegrees: neither polynomial then has
an entire boundary divisor as a component, and zero dimensionality
excludes common components meeting the affine chart. The projective
intersection number bounds the affine length. The same inequality is
automatic for the unit ideal. Dividing either original generator by
content and silently using a new ideal would not be justified here.

Choose only ONE section per label. Off H, a critical point fixes its
label by F/H, so there is no cross-label overlap. Above a root of H,
only two labels have positive excess over floor(2m/3). Even if both
selected sections pass through the same point, at most twice that
point's length is charged. Thus total charged cost <=2 length(k[X,u]/I).
This is the required protection against repeated basepoints; counting
distinct critical points instead would be incorrect.

For each nonexceptional label the cost is at least

    ceil(2N/3)-sum_x floor(2m_x/3)
    >= n0-floor(N/3) >= n0-D.

The inequalities and resulting bound
9+3 floor((4N+24D-4)/(n0-floor(N/3))) check exactly. The factor three
is applied only after counting labels; it bounds polynomial roots of a
fixed cubic over k(X). The additive nine safely covers two exceptional
labels and the zero label.

## 3. Positive-dimensional components and Frobenius

Since F_u is monic up to the invertible scalar three, no vertical
component can occur. A critical root r generates an extension of degree
d<=2, which is separable for p>3. Differentiating v=F(r)/H gives v'=0.
In positive characteristic this alone does NOT imply v is constant.

The recorded height argument supplies the missing step: r is integral
at finite places and has infinity pole order <=D times ramification.
Therefore h(v)<=dN+d(3D-N)=3dD<=6D<p. The derivation extends
nontrivially to k(X,r), its kernel is the p-th-power subfield, and a
nonconstant p-th power has pole-divisor degree at least p. Hence v is
constant. Algebraically closed constants ensure that residue degrees
are one and that the sum of ramification indices over infinity is d.

A repeated root of a cubic in characteristic different from two and
three belongs to k(X); monic integrality and the weighted degree caps
then put R,S in k[X] with degrees <=D. The reduction to
(P-R)^2(P-S)=(c-c0)H is valid, including the triple-root case.

The separate cover proof is sound in p>3: the unique third branch point
of each scaled cubic provides a transposition in only that S3 factor,
forcing product monodromy S3^3. Tame inertia indices are 13,18,9,9,9
on 27 sheets, giving genus three. Luroth excludes a rational
parametrization even if q(X) is inseparable. Thus nonconstant q allows
at most two nonzero labels and eight sections total. Constant q, or a
triple repeated root, gives an affine family. Distinct members of that
family can agree on at most D common coordinates, proving
L(a-D)<=n for arbitrary received words.

## 4. Arbitrary received words and final constant

At H(x)!=0 one received value fixes a label and thus matches at most
three candidates. At roots of H use the crude bound L. This yields
n0>=a-3n/L. Once L>max(9,3/eta), the denominator
eta*n-3n/L is strictly positive; applying the total-bank bound and
multiplying gives

    eta L <=9 eta+3+108D/n-27/L
           <9 eta+3+108D/n.

The claimed floor(9+(3+108D/n)/eta) is consequently safe. The small-L
cases, D=0, absence of nonzero labels, and the affine-family alternative
are all covered. Extending constants does not change coefficient
degrees, section equalities, or the agreement incidences.

No revision of the numerical constant or hypotheses is needed. For a
manuscript, retain the explicit valued-field wording above rather than
citing unrestricted Puiseux expansions in positive characteristic.
