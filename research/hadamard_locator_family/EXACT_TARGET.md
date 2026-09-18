# A scalable exact locator target, without a cyclic or cover hypothesis

This is a new explicit construction target, not an existence theorem. It arises from reviewing the current intrinsic-tightness gaps and does not reopen the Dickson, Riccati, full-torsion, or one-pole families. No large search is proposed.

## Parameter ledger and exact scope

For an even integer L, seek L distinct polynomials of degree at most D=L−2 on n=4(L−1) distinct nodes, each agreeing with one word on A=2(L−1) nodes. The RS dimension is k=L−1, so the rate is exactly1/4 and agreement is exactly1/2. The capacity gap is1/4. The margin above the classical rate-based Johnson curve is ZERO; degree-based A²/n−D is1. Relative specifically to the repository's audited current first-order curve a1(1/4)=(3+sqrt133)/31, the agreement margin would be the positive constant1/2−a1(1/4). These conventions must not be conflated.

Existence for unbounded L would give a linear-size true nearest list at fixed rate and agreement. It would not alone supply a quadratic MCA construction. A characteristic-zero realization for each L specializes to arbitrarily large split prime fields after finitely many bad primes are removed, preserving all distinctness and exact incidence guards.

## Saturation forces the design

Let m_x count agreeing candidates at node x. Total incidences are at least LA. Every pair agrees with the received word together at at most D nodes. Convexity gives

    sum_x binom(m_x,2) >= n binom(L/2,2) = binom(L,2) D.

Thus every inequality is equality: every candidate has exactly A agreements, every column has exactly L/2 agreements, and every pair shares exactly D columns. Consequently any realization induces a 2-(L,L/2,L−2) block multidesign with n blocks. Each pair difference has degree exactly D and its domain roots are exactly its D common blocks. In particular all leading coefficients are distinct.

This saturation is a useful constructive reduction, not an obstruction to the design itself.

## Explicit designs for every power of two

A normalized Hadamard matrix of order L gives 2(L−1) blocks: for each nonconstant column, take its positive and negative row sets. Each row lies in L−1 blocks and each pair in (L−2)/2 blocks. The union of two independently relabeled copies therefore has precisely the required parameters. Sylvester matrices supply these designs for every L=2^m.

For L=4 the resulting design has every pair twice and is realized by the existing four-quadratic construction. For L=8 the first copy is the14 affine hyperplanes of F2³. There are30 distinct labeled copies. Relative to the first copy their intersection sizes and counts are

    14:1, 6:7, 2:14, 0:8.

In particular disjoint copies exist. One disjoint copy is obtained by the permutation [0,1,2,4,3,6,7,5] of vertex labels0..7. The resulting28 blocks are all distinct. Thus this sextic target cannot be a full quadratic pullback of a14-node bank: such a pullback repeats every incidence mask twice. This is a combinatorial distinction from the already studied common-cover deformations.

## Exact polynomial compatibility matrix

Assign a distinct scalar x_B to each block occurrence. Define the monic pair locator

    H_ij(X) = product_{B containing i,j} (X−x_B),

of degree D. Subtract candidate P0 from every candidate and from the word. Any realization is then necessarily

    P0=0,  Pi=lambda_i H_0i (i=1,...,L−1).

Here lambda_0=0 and all lambda_i are pairwise distinct. At a block containing0 the required equalities are automatic. At each block B not containing0, choose one reference label j in B and impose

    lambda_i H_0i(x_B) − lambda_j H_0j(x_B)=0
        for i in B minus {j}.

These are a homogeneous linear matrix M(x) on L−1 leading coefficients, with (L−1)(L−2) rows. For L=8 it is a42×7 matrix. Existence is EXACTLY existence of distinct nodes and a kernel vector with pairwise distinct entries including0. No candidate-coefficient interpolation, word variables, or extra pair-difference identities remain to be checked.

Indeed these equations define the received value at every block. The pair differences have their D prescribed distinct roots and nonzero leading coefficient, so their degree/root count is exact. No additional candidate can agree at a block outside its mask: doing so would give D+1 roots in a pair difference. This proves both sufficiency and exact masks.

Moreover the displayed bank is the complete nearest list. Any other degree-D polynomial Q with a agreements meets L/2 bank members at each such node. Hence a L/2 <= L D and a<=2L−4=A−2. The received word therefore has maximum agreement exactly A, precisely L maximizers, and a two-coordinate drop to every other codeword.

## What a productive next identity must do

This is not a generic-dimension existence argument. Before gauges, the full incidence system has expected dimension (8−L)(L−1); at L=8 it is0 despite11 unavoidable gauge directions. Thus a sextic realization needs at least11 equation dependencies, and the deficit grows with L. A recursive Hadamard identity would have to provide these dependencies explicitly.

Nor can the sextic target be obtained simply by multiplying the known seven cubics by a common cubic A and adding a common polynomial. Each of their pair differences would have its three old roots plus all three roots of A. Saturation forces all six roots into the domain; the latter would create a column with at least seven agreements, contradicting the forced column size four. Repeated roots of A only worsen the required six-simple-root condition. This excludes that tempting shortcut, not the new locator system.

The concrete unexhausted algebraic problem is thus the guarded42×7 kernel for the disjoint-Hadamard28-block design, preferably through an identity which extends along the Sylvester recursion. Solving a single fixed L is only a seed; an unbounded realization or an actual recursive gluing lemma is required for intrinsic length-exponent progress. No positive sextic realization is asserted here.
