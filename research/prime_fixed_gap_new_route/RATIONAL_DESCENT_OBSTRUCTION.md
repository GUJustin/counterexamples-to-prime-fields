# A rational-descent obstruction for the explicit Dickson bank

This is a new bounded algebraic audit, not a prime-ambient fixed-gap construction. It identifies exactly why replacing multiplicative orbit descent by an arbitrary rational/split-torus quotient cannot compress the full explicit bank.

## General polynomial-bank lemma

Let F be any field, W⊂F[X] a vector space of dimension ell≥2, consisting of polynomials of degree ≤ D. Suppose

 W ⊂ R(X)·F(phi(X))

for a nonzero rational function R and nonconstant rational function phi of degree d. Then

 d(ell−1)≤D.

Proof: extend scalars to an algebraic closure. Choose ell−1 generic distinct values of phi whose fibers avoid the zeros/poles of R and infinity. Impose on f∈W one vanishing condition at one point in each fiber. There is a nonzero f satisfying theseell−1 conditions. Since f/R belongs to F(phi), its zero propagates to the entire corresponding fiber, with the fiber's ramification multiplicities. Each fiber contributes d zeros to the polynomial f, counted with multiplicity. Thus deg f≥d(ell−1). This also handles inseparable phi: generic fibers may have fewer distinct points, but their total multiplicity is d. Base extension causes no loss, since a basis of W remains independent and its ratios by R are still functions of phi.

Equivalently, a polynomial space of degree ≤ D lying in a single rational pullback module has dimension at most floor(D/d)+1. Arbitrary common rational multipliers are allowed.

## Application to the explicit prime-field Dickson family

Let p=4k+1 be prime, k≥2,e=2k+1. The explicit family is

 H_a(X)=Σ_{j=0}^{k−1} binom(e,2j+1) a^{2(k−j)} X^j,

obtained by subtracting X^k from G_a. Every displayed coefficient binom(e,2j+1) is nonzero inFp, because e<p. Put t=a². Different nonzero squared parameters give different candidates.

For any L distinct squared parameters, the vector space spanned by their pairwise differences has dimensionmin(k,L−1). This follows from the Vandermonde matrix of 1,t,...,t^k: for L≤k+1, the firstL columns already give independent affine evaluations; for L≥k+1, any k+1 parameters suffice to span allk coefficient directions.

Suppose a bank with L≥3 members admits a common rational compression

 H_a(X)=B(X)+R(X)·V_a(phi(X)),

where B,R are arbitrary common rational functions, R≠0, and V_a may be arbitrary rational functions. Applying the lemma to the difference space gives

 d(min(k,L−1)−1)≤k−1.

In particular:

- any bank with at least k+1 distinct squared parameters forces d=1;
- a bank of size proportional to k permits only bounded quotient degree;
- an unbounded quotient degree requires retaining o(k) members of this explicit bank.

The full bank has (p−1)/2=2k distinct squared parameters, so it cannot descend through any nontrivial rational map, even after a common offset and common rational multiplier. This includes ordinary polynomial substitution, split-torus quotients, nonsplit-torus quotients, and projective changes before descent. A projective coordinate change alone has degree 1 and provides no asymptotic domain compression.

For the full bank there is an especially short proof: differences span 1 and X. If both are in R·Fp(phi), theirratio implies X∈Fp(phi), and the intermediate function field must already equalFp(X).

## Consequences and limits

The known prime-field source is initially on p−1 coordinates with degree bound k−1. The extension-field compiler has enough labels because it passes to Fp². To keep prime ambient and obtain superlinear labels, one needs a source length o(p). A rational quotient of degree tending to infinity would provide such compression only if the bank actually descends. The theorem rules this out for the full explicit Dickson family and for any positive-density subbank.

This does not obstruct the existing descent of an UNKNOWN true-nearest candidate's cyclic orbit. That orbit may be a sparse subbank with a large stabilizer, and its members need not be the explicitH_a family. Nor does it rule out a newly designed sparse family with shared rational structure. It sharpens the missing condition: rational parametrization alone does not create the required stabilizer or compressible coefficient space.

## Ranked mechanisms after this audit

1. A prime-field source with an explicitly forced growing stabilizer, or another sparse bank in a rational pullback module. It must be constructed before applying the ordinary-CA compiler. The existing proof forces a growing orbit, not a growing stabilizer; these are different requirements.
2. A characteristic-zero source with unbounded nearest list and fixed surplus, followed by the already proved splitting-prime transfer. Prime-power torsion avoids the particular prime-order obstruction, but presently lacks an agreement identity.
3. Direct rational/projective compression of the full explicit Dickson bank. The theorem above excludes asymptotic compression; no numerical search on this mechanism is warranted.

No unconditional prime-ambient fixed-gap superlinear ordinary-CA result is claimed here.

## Independent root audit

The generic-fiber proof remains valid over an algebraic closure: extend the polynomial-space basis, avoid the finite zeros and poles of the multiplier, and impose one linear condition per generic fiber. Pullback of a zero has total multiplicity equal to the rational-map degree, including inseparable maps. The Vandermonde difference-space calculation also checks out. The general bound is sharp: take R=1, phi=X^d and W spanned by 1,X^d,...,X^{d(ell-1)}. This sharpness example does not construct a compressible Dickson subbank.
