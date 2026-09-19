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
