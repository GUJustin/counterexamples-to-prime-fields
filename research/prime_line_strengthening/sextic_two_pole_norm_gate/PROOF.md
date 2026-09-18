# Sextic covers with a proper quadratic denominator

Characteristic zero; fourteen selected base fibers are separable. Let psi=R/S have degree6. A proposed witness is N/D, where N is a binary form of degree20 and D is a binary quadratic whose degree-two zero divisor Delta is outside the84-point core. Require gcd(N,D)=1. Delta may be two simple poles or one double pole. The target is42 matches, yielding eight degree-at-most20 polynomials after clearing D, at exact rate21/84=1/4.

Put v=N/(D S^3). Its pole excess over3 psi^*(infinity) is precisely Delta, and is nonpositive elsewhere.

## Intermediate fields

Let phi:P1 -> C normalize the image of (psi,v), of degree t. Positive pole excess pulls back from C, so Delta=phi^*(Delta_bar), and t divides2. If t=2, psi descends to degree3 and Delta_bar has degree1. All selected psi-fibers are separable, so phi is unramified there and each matched intermediate point accounts for two of the original matches. The descended function has at least21 matches on the42-point cubic core and exactly one proper extra pole outside it. Choosing a projective coordinate on C (Luroth), clearing its degree-three cover denominator cubed, gives precisely a forbidden degree(10,1) witness. This is excluded by the established universal cubic one-pole theorem. Thus any possible witness is birational, t=1. This proof includes a double pole: a ramified pullback of the single downstairs pole is still covered.

## Genus and unique incidence pattern

The primitive norm relation has degree6 in V and coefficients

    H(X,V)=sum_{j=0}^6 A_j(X)V^(6-j), deg A_j<=3j+2.

The norm denominator bound follows from the total extra pole degree2, including coincident image values and ramification. On F3 its irreducible closure has class6C0+(18+c)F with c<=2. Adjunction gives arithmetic genus at most

    (6-1)(18/2+2-1)=50.

There are no artificial boundary components when c is the actual maximum of deg A_j-3j. Birationality gives normalization P1, so finite delta costs at most50.

Select42 matches and let T,Q be their totals over the seven triple and seven quadruple base nodes. The seven old degree20 difference polynomials give

    T+Q=42, 3T+4Q<=140, hence T>=28.

Convexity for the multiplicities in both groups gives cost at least49 at T=28: all seven triple multiplicities4 and all seven quadruple multiplicities2. At T=29 the minimum is52 (one triple5, six4; six quadruples2, one1). The convex minimum is increasing thereafter. Thus T=28, Q=14.

For integer multiplicities within either group, excess over its balanced cost is half the sum of squared deviations. The total cost at most50 permits either the balanced pattern or exactly one transfer (+1,-1) within one group. Summed pair bounds are now equal to140=7*20, so each old candidate must have exactly20 selected intersections. A single transfer changes this intersection vector by the difference of two incidence columns. The columns are distinct in both banks, so that vector is nonzero. Hence transfers are impossible. The sole admissible pattern is:

    every triple fiber: 4 matches;
    every quadruple fiber: 2 matches.

## Exact linear gate

At a point with k distinct matched normalization preimages, the irreducible plane curve has multiplicity at least k. Its local Taylor coefficients of total degree<k vanish. Thus impose all Hasse derivatives in X,V of total order<4 at the seven triple points (10 each), and total order<2 at the seven quadruple points (3 each):91 equations.

The degree flags supply sum_{j=0}^6(3j+3)=84 coefficients. `gate.py/json` constructs these91-by84 matrices directly from the independently archived Paley reduction modulo29 and orbit2 reduction modulo83. Both have rank84 and trivial kernel. The JSON saves every entry and84 pivot rows. These are necessary norm equations over the base coefficient field and remain so after any extension. Every input denominator is a unit at the chosen prime, so a nonzero maximal minor proves characteristic-zero full rank; Galois conjugates inherit the conclusion.

This excludes the sextic/two-pole augmentation for every characteristic-zero seven-cubic bank, using the complete orbit2/orbit7 realization classification. It is not a general eight-word nonexistence claim. Independent replay in `verify.py` reconstructs the Hasse coefficients by repeated polynomial multiplication and evaluates the selected minors by integer Bareiss elimination. Their residues are11 modulo29 and55 modulo83. Both pass. The generation run took0.54seconds and6.5MiB.
