# Quadratic towers preserve the entire above-capacity profile

September 17. Strengthening of PROOF.md for B a power of two. This is
a locally audited argument, not an independent review or novelty claim.

For any characteristic-zero source word on N algebraic nodes, dimension
k<N, and every B=2^s, there are algebraic evaluation nodes of length BN
and a received word for dimension Bk such that the COMPLETE list of
polynomials with more than Bk agreements consists exactly of

    Q(H(X)), where deg Q<k and Q has more than k source agreements.

Here H is an iterated quadratic polynomial of degree B. Each such
candidate has exactly B times its source agreement count. Every other
polynomial has at most Bk agreements. The same full profile occurs over
arbitrarily large completely split prime fields after excluding finitely
many bad primes. No quantitative field bound is claimed.

## One quadratic step

Use X^2=t+a_i with t transcendental and the source value w_i on both
roots, as in PROOF.md. The splitting field has independent involutions
swapping the two roots of any one fiber. Suppose deg P<2k and P has
h>2k agreements. Its coefficients lie in that splitting field by
interpolation on 2k agreeing nodes.

For one fiber, if P agrees at both roots or neither root, swapping the
fiber preserves all h agreements. If it agrees at exactly one root,
P and its conjugate share at least h-1>=2k agreements. In every case,
the two degree<2k polynomials coincide. Thus P is fixed by all independent
involutions and lies over the ground function field. Any single agreement
then forces both roots to agree. Write

    P(X)=Q_0(X^2-t)+X Q_1(X^2-t), deg Q_j<k.

There are at least k+1 agreeing fibers. Therefore Q_1=0 and interpolation
shows Q_0 is an original source polynomial. This proves the exact
above-dimension threshold, stronger than the coarse h-2>deg P estimate.

## Iteration and arithmetic realization

Apply this step repeatedly, introducing a new transcendental parameter
at every stage. At each stage the preceding node configuration is held
in the constant field. Every above-dimension candidate descends to the
preceding stage, so induction gives the full statement for B=2^s.
For two stages one may take H(X)=(X^2-t_2)^2-t_1.

For each fixed s, enumerate all (Bk+1)-node supports. Generic inconsistent
supports have nonzero augmented Vandermonde minors; generic consistent
supports come from precisely the composed source candidates. Avoiding
these finitely many nonzero minors, node collisions, and nonagreement
zeros defines a nonempty open set in the finite splitting cover of the
parameter space. Norms give a nonempty open set downstairs. One can
choose rational parameter values there and retain all algebraic roots.
Reduction at sufficiently large completely split primes preserves these
same finite rank certificates and hence the complete above-dimension
profile, even against candidates over the algebraic closure of F_p.

This enlarges length and the spacing between distinct high-agreement
levels. It preserves the number of source candidates, so it does not
produce a growing fixed-gap list.

## Complete finite check

`verify_profile.py` uses F1000000007, t_1=63, t_2=1556, and source
(-2,-1,0,1,2) with word (2,1,0,1,2), dimension2. At the resulting20
nodes, dimension8, all125970 determining supports are exhausted.
There are124982 distinct interpolants:124980 have agreement8 and exactly
two have agreement12. Thus EVERY candidate with agreement above8 is
one of +/-H. This verifies a complete profile of one specialization;
the general theorem is the preceding algebraic proof.
