# Prime-alphabet fully split pencil barrier

Independent algebraic audit: PASS. This concerns fully split polynomial pencils, not arbitrary prime-alphabet counterexamples or received lines.

## Statement

Let A(X,Y), B(X,Y) be coprime homogeneous polynomials of the same positive degree d over F_p. Assume they are linearly independent and that every nonzero F_p-linear combination uA+vB factors completely into homogeneous linear factors over F_p, allowing repeated factors and the factor Y (the point at infinity).

Then the rational map [A:B] is a projective linear transformation composed with a power of Frobenius. More precisely, d=p^r for some r>=0 and, up to a common nonzero scalar,

`A=a X^(p^r)+b Y^(p^r), B=c X^(p^r)+e Y^(p^r)`

with `ae-bc!=0`. In particular a separable such map has d=1. If d<p, it necessarily has d=1.

## Separable proof, including infinity and wild ramification

The coprime homogeneous pair defines a morphism R:P^1->P^1 of degree d. For each of the p+1 rational target points, the hypothesis says its entire geometric fiber is supported on rational source points. Each fiber has total multiplicity d. Every rational source point maps to a rational target point, so the union of these supports is exactly P^1(F_p), with p+1 elements. Writing e_x for the local multiplicity therefore gives

`sum_{x in P^1(F_p)} e_x=d(p+1)`

and hence

`sum_{x in P^1(F_p)} (e_x-1)=(d-1)(p+1)`.

For a separable rational map this sum is at most 2d-2. One can verify the required inequality directly, without assuming tame ramification: write f(X)=A(X,1), g(X)=B(X,1). The nonzero derivative numerator `f'g-fg'`, homogenized to degree 2d-2, is a nonzero section of that degree. In a local source coordinate and a target coordinate that is finite at the image point, it vanishes to order at least e_x-1. This follows by differentiating a local expansion with leading exponent e_x; if p divides e_x the derivative vanishes to higher order, which only strengthens the inequality. The reciprocal charts give the same statement at source or target infinity. Thus its total zero multiplicity 2d-2 bounds the displayed sum.

Consequently `(d-1)(p+1)<=2d-2`. Since p+1>2, this forces d=1. Equivalently, Riemann–Hurwitz gives the same conclusion because the different exponent is at least e_x-1 even in the wild case; equality with e_x-1 is not being assumed.

## Inseparable reduction

Over the perfect field F_p, write the rational function as

`R(X)=S(X^(p^r))`

with S separable, extracting the maximal common p-power from the rational-function exponents. Frobenius is a bijection on geometric points, acts identically on P^1(F_p), and merely multiplies fiber multiplicities by p^r. Therefore every rational target fiber of S is also supported on P^1(F_p). The separable argument forces deg(S)=1. This gives the stated homogeneous form and d=p^r. Conversely these forms have the required splitting property, since every rational fiber is a single rational point with multiplicity p^r.

## Compiler scope

If a coefficient space contains a pencil whose every nonzero element splits over the prime field, first remove the homogeneous gcd of its two generators. If the remaining pair defines a positive-degree map, the lemma applies to that residual degree. Thus a nontrivial separable fully split pencil of residual degree greater than one cannot supply the norm–trace-style splitting argument over the prime alphabet itself.

This does not say that evaluation injectivity outside a field requires full splitting, that all prime-field compilers use such pencils, or that prime-alphabet counterexamples are impossible. The same theorem holds with F_p replaced everywhere by any finite field F_q. What the extension-field norm–trace construction escapes is the equality of the coefficient and splitting fields: its pencil is only F_p-linear, while its roots lie in a larger field B. Then only p+1 target fibers are constrained, their supports can use |B|+1 points, and the contradiction above no longer follows.

## Quantitative support form

More generally let R be a separable degree-d rational map defined over F_p, and suppose all geometric points in the p+1 rational target fibers belong to one finite set S in P^1(B), where B is any extension field. Put N_support=|S|; S may contain unused points. The union of the actual fiber supports has size at most N_support, so

`d(p+1)-N_support <= sum_{x over rational targets}(e_x-1) <= 2d-2`.

Therefore

`N_support >= (p-1)d+2`.

If S consists of a finite evaluation domain of size n together with at most the point at infinity, this gives `n >= (p-1)d+1`. In particular n<p is impossible for any positive separable degree. If infinity is not included, the stronger `n >= (p-1)d+2` holds.

This is a support requirement for preserving every complete rational target fiber of this pencil. It is not a restriction on preserving merely some roots of each member, some target parameters, or a different received-word construction. For an inseparable map the same bound applies to its separable degree, not automatically to its total degree.

## Partial splitting: exact fiber-defect ledger

Let R be one fixed separable degree-d map, S any set of N geometric source points, and Y a set of distinct target points. Write L=|Y|. For each y, define

- a_y = the number of distinct points of R^{-1}(y) in S;
- b_y = the number of distinct points of R^{-1}(y) outside S;
- delta_y = the sum of local multiplicities at the points outside S;
- rho_y = sum_{x in R^{-1}(y)}(e_x-1), the full fiber ramification defect;
- rho_{S,y} = the same sum restricted to S.

There are two exact identities:

`d=a_y+b_y+rho_y`,

`d=a_y+delta_y+rho_{S,y}`.

Distinct target fibers are disjoint, so sum a_y<=N. Separability gives sum rho_y<=2d-2, hence also sum rho_{S,y}<=2d-2. It follows that

`sum_{y in Y}(d-b_y) <= N+2d-2`,

and

`sum_{y in Y}(d-delta_y) <= N+2d-2`.

The first inequality is stronger when only distinct exceptional roots are controlled. In particular, if each fiber has at most b distinct geometric roots outside S and d>b, then

`L <= floor((N+2d-2)/(d-b))`.

Repeated exceptional roots do not invalidate this bound: their extra multiplicities consume the same global ramification budget. If the selected fibers are unramified, the +2d-2 term can be omitted. More precisely it can always be replaced by the actual total ramification defect of the selected fibers. A bound on the number of irreducible factors outside S is not sufficient unless it also bounds their total number of geometric roots.

For S=P^1(F_p), N=p+1, totally split fibers satisfy
`L <= floor((p+2d-1)/d)`.
With at most five nonnative geometric roots per fiber and d>5,
`L <= floor((p+2d-1)/(d-5))`.
For an n-coordinate domain with an allowed extra infinity point, replace p+1 by n+1. Thus one fixed map with large d and uniformly bounded fiber defects supports only O(n/d+1) different such target values. This statement needs an injective association between the challenge labels being counted and the target fibers; without that association it is not a label bound.

## Relation to the moving-extra elliptic target

The existing `FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md` and `MOVING_EXTRA_PATH_RATIONALITY.md` do not currently provide that association. Their five extra positions are native error coordinates appended to a union of TWO isogeny fibers. They are not five nonnative roots missing from a single fixed rational-map fiber. The isogeny also varies with H, and the path-derived rational leaf model can vary with the edge. Therefore the partial-splitting inequality does not close their open moving-extra problem.

Even for a fixed degree-ell isogeny map on n=Theta(ell^2) coordinates, this ledger permits O(ell) single fiber tags and O(ell^2) pairs of tags. Across Theta(ell) subgroup maps this elementary bound still permits O(ell^3)=O(n^(3/2)) descriptions before any syndrome compatibility or duplicate-label test. Thus it does not itself forbid a superlinear two-fiber bank. Its useful role is a precise gate for a proposed construction that really reduces all its distinct labels to almost-supported fibers of ONE map, or of a bounded collection of maps with a controlled label multiplicity.
