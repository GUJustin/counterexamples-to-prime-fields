# Conditional classification of Galois balanced rational fibers

September 15, 2026. Elementary proof, independently discussed with the
`moment_literature` and `gram_norm` reviewers. No novelty claim.

## Precise theorem

Let F have characteristic p>n, let n>=3, and suppose mu_n is contained
in F. Put D=mu_n. Let R in F(X) have rational degree B>=1, have no
poles on D, and have exactly B distinct points in every fiber of its
restriction to D. Necessarily B divides n. Assume that the geometric
extension

    Fbar(X) / Fbar(R(X))

is Galois. Then the arithmetic extension F(X)/F(R(X)) is Galois too,
and, for some h in PGL_2(F), R has exactly one of the following forms
(with the possible overlap of representations immaterial):

1. **Cyclic:** R(X)=h(X^B), where B divides n.
2. **Dihedral:** B=2d divides n and

       R(X)=h(X^d+c/X^d),

   where c is a nonsquare in the cyclic group mu_(n/d).

In each case h must have no pole on the corresponding image of D.
Conversely, these forms satisfy the full balanced-fiber hypothesis
and are Galois, when that no-pole condition holds.

Here "nonsquare in mu_N" means not in {u^2:u in mu_N}; it does
not mean nonsquare in the ambient field. The dihedral case forces
N=n/d to be even. B=1 is included in the cyclic case.

## 1. The stabilizer of mu_n is dihedral

Work first over Fbar. If a Möbius map
g(X)=(aX+b)/(cX+d) permutes D, its denominator does not vanish
there. The degree-at-most-n polynomial

    (aX+b)^n-(cX+d)^n

vanishes on D and is not identically zero. The latter would make
g^n=1 in Fbar(X), forcing g to be constant. Therefore

    (aX+b)^n-(cX+d)^n = lambda(X^n-1),   lambda != 0.

For 1<=i<=n-1, comparison of intermediate coefficients gives

    a^i b^(n-i) = c^i d^(n-i),

because the binomial coefficients are nonzero when p>n. If all
four entries are nonzero, comparing i=1 and i=2 gives a/b=c/d,
contradicting ad-bc!=0. If one entry is zero, the intermediate
identities and nonzero determinant force either b=c=0 or a=d=0.
Consequently

    g(X)=zeta X  or  zeta/X,             zeta in mu_n.

Both types do permute D. Thus its geometric Möbius stabilizer is
exactly the dihedral group of order 2n, and every such map is
already defined over F. The argument also handles n=3; p>n
excludes small-characteristic exceptional configurations.

## 2. The geometric deck group preserves the full domain and descends

Let G be the geometric deck group. A rational map of degree B has
exactly B points in each geometric fiber when multiplicities are
counted. Each fiber over R(D) already contains B distinct points of
D. Thus these are complete geometric fibers, are unramified, and
contain neither extra points nor infinity.

A deck map preserves each fiber, hence permutes D. Therefore
G is a subgroup of the stabilizer just computed. In particular
every deck map is defined over F. Equivalently, one can use that
the images of three distinct F-rational points determine a Möbius
map over F. Since |G|=B=[F(X):F(R)], these B descended automorphisms
show that F(X)/F(R) is Galois. They act freely on D, because the
fibers under consideration are unramified.

Conversely, if the arithmetic extension is assumed Galois, its B
automorphisms remain distinct over Fbar, and the geometric rational
map still has degree B. Thus the geometric extension is Galois.
Under the theorem's hypotheses, either Galois assumption suffices.

## 3. Subgroups and quotient generators

The rotation subgroup consists of X -> zeta X. Let its intersection
with G have order d; it is the subgroup mu_d of rotations.

If G consists only of rotations, |G|=d=B and

    F(X)^G = F(X^B).

If G contains a reflection X -> alpha/X, then alpha is in mu_n,
G consists of d rotations and d reflections, and |G|=2d=B.
The rotation-invariant coordinate U=X^d is transformed by reflection
to alpha^d/U. Put c=alpha^d in mu_(n/d). Then

    V=X^d+c/X^d

is invariant under G and has rational degree 2d=|G|. Therefore
F(X)^G=F(V).

To check freeness, let N=n/d. A point x in D is fixed by some
reflection X -> alpha*zeta/X, zeta in mu_d, exactly when

    (x^d)^2=c.

Indeed, the reverse implication gives x^2/alpha in mu_d. Since
x^d runs over mu_N, freeness is equivalent to c being nonsquare
in mu_N. This implies N is even. Conversely, that condition
makes every orbit have 2d elements, so all fibers are full.

Since R and the displayed invariant generate the same rational
function field, they differ by an element h of PGL_2(F). This
gives the two asserted forms, including their field of definition.

**Parameter caution.** It is not sufficient to say that the raw
reflection parameter alpha is nonsquare in mu_n without also
checking all reflections. For example, n=6 and d=2 allow the
rotation by -1: a nonsquare alpha can become a square after that
rotation. The projected condition c=alpha^d nonsquare in mu_N
is the precise criterion. Under full balance, N is already even.

## 4. What the reduction does and does not establish

This theorem reduces the full balanced **Galois** rational-map
subclass to power and twisted-inversion quotient domains, up to
target Möbius relabeling. It supplies the structural reduction;
any numerical certificate on those image domains remains a
separate counting problem.

Target Möbius relabeling does not create a new Reed--Solomon
Hamming geometry. If h(U)=(aU+b)/(cU+d) has no pole on a finite
image set E, then for 1<=k<=|E| the map

    f(h(U)) -> (cU+d)^(k-1) f(h(U))

identifies the evaluations of degree-<k polynomials on h(E) with
those of degree-<k polynomials on E, using the corresponding
coordinate permutation and nonzero coordinate multipliers.
The polynomial-space map is invertible: it is the degree-(k-1)
homogeneous action of an invertible two-by-two matrix. Scaling
received words in the same way preserves every Hamming distance,
list size, and affine dependence among words. This equivalence
does not by itself identify arbitrary *coefficient-signature*
counting formulas under the relabeling.

The Galois assumption is substantive. The full balanced cubic
example over F_13 on mu_6 in
[`../gram_norm/BALANCED_FIBER_REVIEW.md`](../gram_norm/BALANCED_FIBER_REVIEW.md)
has four simple critical points, so cannot be a Möbius conjugate
of a cyclic degree-three quotient. It is therefore a concrete
non-Galois escape from this classification. General two-block
rational partitions likewise need not define Galois covers.

No assertion of optimality for arbitrary rational maps, arbitrary
lists, or a fixed coding-theory submission follows from this note.
For the polynomial case, no Galois hypothesis is needed: see
[`BALANCED_FIBER_CLASSIFICATION.md`](BALANCED_FIBER_CLASSIFICATION.md).

## Hypotheses that cannot silently be removed

* The n points must all belong to F to obtain the stated arithmetic
  descent argument. With only a geometric subgroup domain, descent
  requires additional analysis. For example, over F_7 the map X^4
  is geometrically Galois but has only two arithmetic deck maps;
  the four geometric fourth roots of unity are not all in F_7.
* The fibers must use the entire B-point geometric fiber. Partial
  or punctured fibers need not make deck maps preserve the domain.
* n>=3 is used to constrain Möbius transformations. One- and
  two-point domain stabilizers are larger.
* p>n is used in the elementary stabilizer proof. This note makes
  no classification claim in smaller characteristic, even though
  the polynomial-only theorem needs merely p not dividing n.

The one-image boundary M=1 is allowed in both forms. In particular,
if n=2d and c=-1, the dihedral quotient X^d-X^(-d) vanishes on
all of mu_n and has rational degree n. There is no exception to
the full-fiber statement at that boundary.

## Exact finite checks

`verify_galois_fibers.py` enumerates projective Möbius representatives
over primes 5 through 31. All 354,504 domain checks agree with the
dihedral stabilizer formula, recovering 544 stabilizer maps in total.
It also checks 498 rotation/reflection subgroups and their quotient
fibers; exactly 155 act freely, matching the nonsquare projected-twist
criterion. Results are in `galois_fiber_verification.json`. These are
independent finite checks of the algebraic proof, not tests of any
cryptographic protocol.

An independent review approved the theorem and checked the one-image,
descent, and projected-twist boundaries; see
[`../gram_norm/RATIONAL_GALOIS_REVIEW.md`](../gram_norm/RATIONAL_GALOIS_REVIEW.md).
