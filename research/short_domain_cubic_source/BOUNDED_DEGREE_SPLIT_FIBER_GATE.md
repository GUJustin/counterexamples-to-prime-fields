# Beyond degree two: an explicit fully split fiber gate

Status: algebraic/Pasten–Wang gate derived; no assertion about arbitrary one-section fibers, and no unproved isotriviality step is included.

Let k be algebraically closed of characteristic p, K=k(X), and R=N/T a coprime rational function of degree b≥2 in u. Suppose selected constant labels c have fibers N−cT which have degree exactly b and split completely into degree-at-most-D polynomial sections, and suppose the generic discriminant F(C)=Disc_u(N−CT) has no repeated nonconstant irreducible factors in K[C]. A sufficient simpler hypothesis is that F is squarefree in K[C]. Define

    e=2b−2,    A_b=b(b−1)(2b+1).

Assume p>max(e,A_b D), p≠2. If at least 22b−23 such labels have nonzero discriminant, then

    F(C)=s(X)² q(C),   q in k[C],   s in K nonzero.

In particular every finite discriminant root is constant. This concerns the discriminant/branch locus, not yet the form of every section.

## Reconstruction and height

The 2b+1 selected distinct labels give distinct sections P_i. The rows

    (P_i^b,...,P_i,1, −c_i P_i^b,...,−c_i P_i,−c_i)

have rank 2b+1. Two kernel vectors yield a cross-difference of u-degree at most 2b with 2b+1 distinct roots; coprimality and exact rational-map degree b then force proportionality. Thus maximal minors reconstruct N,T with

    deg_X n_j, deg_X t_j ≤ [b(b+1)−j]D,   0≤j≤b.

The discriminant of a degree-b polynomial has total coefficient degree 2b−2 and weighted index degree b(b−1), where the coefficient of u^j has index weight j. These identities follow respectively from scaling the polynomial and scaling its variable. Hence

    deg_X [C^i] F ≤ [(2b−2)b(b+1)−b(b−1)]D=A_b D.

Also deg_C F≤e. Generic separability follows from p>b, which follows from the stated guard unless D=0; for D=0 the additional p>e gives it. More generally one may explicitly assume F nonzero.

## Fully split fibers and reciprocal normalization

At a degree-b, nonzero-discriminant completely split fiber,

    F(c)=a_b(c)^(2b−2) product_(i<j)(P_i−P_j)²

is a nonzero square in K. Choose one label c0 and write F(c0)=s². Form

    H(Z)=Z^e F(c0+1/Z)/F(c0).

Because e is even, each remaining split label produces a square value at Z=1/(c−c0). H is monic of degree e, even if F has lower degree; any extra zero at Z=0 is a constant polynomial factor. Its projective coefficient height is at most A_b D<p.

Every nonconstant irreducible factor of H is separable because its degree is below p; no such factor belongs to K^p[Z], since its monic factor height is below p. Reciprocal change preserves multiplicities of nonconstant factors. By hypothesis all these multiplicities are one.

Apply Pasten–Wang Theorem 3 with genus zero, n=e and mu=2. Its strict threshold is M>11e−3, met by M≥22b−24 remaining labels. It would force every nonconstant factor to have multiplicity two. Thus there are no nonconstant factors, and H has constant coefficients. Undoing the transformation proves F=s²q(C).

Primary theorem, directly verified in the preceding audits:
https://people.math.harvard.edu/~hpasten/preprints/PWposIMRN.pdf

## What this does and does not resolve

The degree-two theorem does not need the fully split hypothesis: one rational root already splits a quadratic. For b≥3, one polynomial root leaves a residual factor of degree b−1, whose discriminant need not be square. This is the exact point where the same argument stops; it is not a coefficient-height issue.

For simply branched rational covers, a constant branch locus suggests a tame-cover rigidity/descent step. Such a step needs a precise theorem and proof of descent of the parametrization. It has not been silently assumed here. A fully split unramified constant fiber would provide marked K-points that can remove a residual automorphism twist, but that observation alone is not a proof of cover rigidity.

Therefore the concrete construction window remaining beyond this gate is: fibers with only one polynomial component, residual degree at least two; or nonsimple moving branch points whose even discriminant multiplicities evade the square-value test. No positive construction or bound for that window is claimed.
