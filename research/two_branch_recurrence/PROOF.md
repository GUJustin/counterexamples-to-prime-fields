# Triangular Riccati families: actual agreement gives a linear exceptional bound

September17,2026. Working proof for independent audit. No novelty claim.
This concerns solutions of the displayed equation; an application to all
nearby RS candidates requires an interpolant of this form covering them.
It does not prove a general first-order MCA bound.

## 1. A general triangular equation

Let D>=1 and char(F)=0 or p>D. Let T(X) be monic of degree t>2D,
R(X,z) have z-degree<=1 and X-degree<=t-2, and S(X,z) have z-degree<=2
and X-degree<=t+D-1. Consider all polynomial solutions deg(P)<=D of

    T P' -P²+R P-S=0.                              (1)

There are at most4D+4 challenge labels belonging to isolated points of the
actual solution locus. Its positive-dimensional components are covered
by at most two plane curves in coordinates(z,c), where c=P(0); their
summed bidegrees are at most(D+1,2).

More concretely, write P=c+sum_(j=1)^D a_j(z)X^j. Coefficients of
X^(t+j-1), in decreasing j, give

    j a_j = S_(t+j-1)
            -sum_(i>j) i T_(t+j-i) a_i
            -sum_(i>j) R_(t+j-1-i) a_i.             (2)

There is no P² contribution because t+j-1>2D. No constant c occurs
because deg_X R<=t-2. Thus each a_j belongs to F[z] and

    deg_z a_j<=D-j+2.

This uses only division by1,...,D; there are no challenge denominators.
Let Q(X,z)=sum a_j(z)X^j. All residual coefficients after substitution
P=c+Q are equations in(z,c). The constant-X coefficient is

    E0=-c²+R_0(z)c+T_0 a_1(z)-S_0(z),              (3)

of bidegree at most(D+1,2). Each other coefficient is

    L_i=B_i(z)c+A_i(z),
    deg B_i<=D+1, deg A_i<=2D+2.                   (4)

Equations(2)--(4) describe exactly the actual degree-<=D solutions.

### Isolated-label count, including singular solutions

If all L_i vanish identically, the locus is E0=0 and has no isolated
components: E0 is monic in c up to sign. If some L_i has B_i=0,A_i!=0,
all solution labels are roots of A_i, at most2D+2.
Otherwise choose L=Bc+A with B!=0. If Res_c(E0,L) is nonzero, every
solution label is a root, including B=0. Its degree is at most4D+4,
by the explicit substitution formula (terms A²,R_0AB,and (T_0a_1-S_0)B²).
If that resultant vanishes identically but some determinant

    A_i B-A B_i

is nonzero, it vanishes at every solution and has degree<=3D+3.
If all these determinants also vanish identically, then over B!=0 the
whole locus is the persistent rational graph c=-A/B. Thus isolated points
can occur only over roots of B, at mostD+1 labels. This proves the count.

Every curve component divides E0. Since E0 has c-degree2 and no vertical
factor, there are at most two such reduced components, each dominant over
z; their z-degrees sum to at mostD+1 and c-degrees to at most2. Statements
are geometric over an algebraic closure, hence bound base-field solutions.
No regularity/separant condition is needed.

## 2. Actual agreement on an arbitrary received line

Take any n distinct evaluation points in F, any received line w_z=f+zg,
and integer A>D. Outside at most

    4D+4 + 3n(D+1)/(A-D) + 2n                       (5)

labels, every solution of(1) having at least A agreements has the full
common-witness property with degree-<=D polynomials. In particular,
for fixed D/n<1 and fixed (A-D)/n>0, this is O(n).

Proof: for an irreducible curve component C of the plane locus, a match
at coordinate x is the equation

    c+Q(x,z)-f(x)-zg(x)=0.                         (6)

If(6) is not identically zero on C, substitution into its defining
polynomial gives a nonzero polynomial in z of degree at most
s+r(D+1), where(s,r) are C's bidegrees. Each root gives at most one
point satisfying(6), since(6) is monic linear in c. Summing over all
components gives at most3(D+1) nonpersistent incidences per coordinate.

Let I_C consist of coordinates for which(6) holds identically. If
|I_C|<=D, every A-near point on C contributes at least A-D nonpersistent
incidences. Across all such components there are at most
3n(D+1)/(A-D) nearby points, hence no more labels.

If |I_C|>D, interpolation at D+1 coordinates forces the ENTIRE polynomial
P on C to equal F0+zG0 with F0,G0 in F[X], degrees<=D. This is a genuine
base-field affine codeword graph, not merely a formal branch over an
extension. On coordinates outside I_C its agreement equation is a
nonzero affine polynomial in z, so at most n exceptional labels have
any extra agreement. Outside those labels its full agreement set is
exactly I_C, with the required common witnesses. There are at most two
components. Add the isolated-label count from Section1. This proves(5).

This argument counts actual agreeing candidates, including singular
solutions and persistent components. It does not replace the missing
agreement argument by a count of formal ODE solutions.

## 3. The entire unnormalized two-branch domain-locator family

Let T be the monic squarefree locator of the n evaluation points, assume
n>4D and char(F)=0 or p>D. Let F_z,G_z be polynomial received branches,
affine in z and of X-degree at most n-1. Consider

    T P'=(P-F_z)(P-G_z), deg P<=D.                 (7)

The same bound(5) applies to nearby solutions on ANY chosen received
line (in particular either branch). Thus this entire two-branch ansatz
cannot furnish fixed-gap superlinear exceptional counts at quarter rate.

If some coefficient of F_zG_z above X-degree n+D-1 is nonzero, it is a
nonzero polynomial in z of degree at most2. Every solution label is its
root, so there are at most two labels. Otherwise the generic product
X-degree is at most n+D-1.

If both generic branch degrees exceed D, each is at most n-2. Set
R=F_z+G_z,S=F_zG_z in(1). The hypotheses of Section1 hold, giving(5).
Degree drops at special labels do not invalidate this global polynomial
identity or the recurrence.

If a branch, say F_z, has generic degree<=D, it is an affine codeword
pencil. A solution P not equal to F_z agrees with it at at most D domain
points. At every other point equation(7) forces P=G_z, so P agrees with
G_z on at least n-D points. Such a P is unique at each label, because two
would agree on at least n-2D>D points.

If there are at least three such labels, take any triple and the affine
linear relation among their labels. On their common G-agreement set,
with at least n-3D>D points, their candidate polynomials satisfy the
same affine relation. Hence every such candidate lies on one affine
codeword pencil determined by the first two. If there are at most two
labels, simply discard them. All solutions are therefore contained in
at most two affine codeword pencils, outside at most two labels.
For any received line, each pencil has the full-witness property outside
at most n extra-agreement labels. The resulting bound2n+2 is smaller
than(5), proving the assertion.

## What this changes

The earlier zero-branch normalization is no longer the only closed case:
the degree conditions close the fully unnormalized polynomial two-branch
family at n>4D. The key is that forcing branch agreement at every domain
point also imposes a strong leading-X recurrence.

This is still a family theorem. A generic first-order interpolation
equation need not have this Riccati form, need not have a locator as its
leading derivative coefficient, and need not satisfy the triangular degree
conditions. A next extension should identify which wider leading-coefficient
conditions retain bounded bidegree after eliminating nonconstant message
coefficients. No general first-order linear bound is asserted here.
