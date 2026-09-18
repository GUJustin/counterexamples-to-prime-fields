# A smooth sixteen-node cubic seed and a complete eight-word quadratic pullback

This is a fixed-size construction. It supplies no growing-list family, first-order exponent lower bound, or better.codes improvement. Finite eight-word examples in the first-order regime were already known in the coauthor material; the useful feature here is a new explicit smooth cubic incidence seed, with a complete nearest list after a quadratic pullback.

## Exact seed over F17

The sixteen nodes are 1,...,16, with received values

    9,3,12,15,0,14,8,13,11,13,11,8,10,14,10,13.

The eight cubics have ascending coefficient vectors

    (1,10,7,2), (16,11,12,4), (13,4,7,5), (3,1,15,7),
    (0,10,2,10), (15,12,5,12), (14,15,0,14), (16,1,13,15).

Each has exactly seven agreements. Their zero-based supports are

    2,4,5,9,13,14,15
    0,3,7,10,12,14,15
    4,6,8,10,12,13,14
    0,3,4,9,10,11,13
    2,3,5,8,10,11,14
    2,4,7,8,11,12,15
    0,1,2,6,10,11,12
    1,3,6,8,11,13,15.

The column multiplicities are 3,2,4,4,4,2,3,2,4,2,5,5,4,4,4,4. Thus this seed does not satisfy the saturated three/four-column pattern of the fourteen-node cubic problem.

For completeness, any cubic agreeing at least seven times is determined by four of those agreements. Independently interpolating all binomial(16,4)=1820 four-subsets gives maximum agreement seven, attained by precisely these eight polynomials. This reasoning also proves completeness over the algebraic closure of F17: interpolation at four distinct F17 nodes with F17 values forces the polynomial coefficients into F17.

The received-word search and its receipts are local_search.cpp/json/resources.json. The search found the seed after seventeen coordinate-ascent steps of its first restart. independent_verify.py/json reconstructs every incidence, the Jacobian, and the complete finite list independently with standard-library arithmetic.

## Smooth characteristic-zero lift

Treat the 32 cubic coefficients, sixteen nodes, and sixteen received values as 64 variables. Impose the 56 selected agreement equations

    P_i(x_j)-w_j=0, j in support_i.

The Jacobian row has the four coefficient entries (1,x_j,x_j²,x_j³), node entry P_i'(x_j), and word entry -1. Its columns are ordered as 32 coefficients, sixteen nodes, then sixteen words.

The 56-column minor with columns

    0,...,45,48,...,57

has determinant 14 modulo17, independently verified. Fix the eight remaining variables at integer lifts of their displayed values: nodes x_14=15,x_15=16 and word values w_10,...,w_15. Hensel's lemma gives a solution over Z17. Its coordinates are algebraic over Q: after fixing the eight free coordinates, the nonzero square Jacobian makes this a zero-dimensional local solution of a polynomial system over Q. Hence all coordinates lie in a number field embedded in Q17.

Every node, node difference, nonmatching incidence, and distinguishing candidate-coefficient difference that was a unit modulo17 remains a unit. The lifted seed therefore has sixteen distinct nonzero nodes, eight distinct cubics, and exactly the displayed seven matches per cubic.

Its nearest list remains complete over the algebraic closure of the number field. Indeed any cubic matching at least seven nodes has integral coefficients at a place over17, by interpolation on any four of its matches using unit Vandermonde denominators. Its reduction is one of the eight finite cubics. That reduction has exactly seven matching coordinates, so the characteristic-zero polynomial's matching support is forced to be that same seven-set. Four-point uniqueness identifies it with the known lifted cubic.

The incidence scheme has local dimension 64-56=8. These dimensions are exhausted by adding a common cubic (four parameters), common scaling (one), and projective changes of the base with the degree-three section action (three). The infinitesimal actions are independent: a quadratic projective vector field vanishing at sixteen distinct nodes is zero; then distinct candidate polynomials force both the common scale and common additive cubic to vanish. Thus the configuration is locally rigid modulo these gauges. The full-rank certificate does not provide a new positive-dimensional family of inequivalent seeds.

## Complete quadratic pullback

Adjoin square roots of the sixteen nonzero nodes and pull back by Y=T². This gives 32 distinct nodes, eight degree-six polynomials P_i(T²), and received values w_j at both square roots of x_j. Each candidate has exactly fourteen agreements. The Reed--Solomon dimension is seven.

It remains to rule out additional degree-six polynomials. This is done over the algebraic closure of F17 before lifting, with no restriction on their coefficient field. Write a candidate as

    Q(T)=E(Y)+T O(Y), deg E<=3, deg O<=2.

If O=0, the complete cubic seed shows that Q is one of the eight known candidates whenever it has at least fourteen agreements. If O is nonzero, at most two fibers can be fully matched, since every full fiber is a root of O. Fourteen agreements must therefore meet at least twelve of the sixteen fibers. At every met fiber,

    H(Y,w)=(w-E(Y))²-Y O(Y)²=0.

Write H=w²+B(Y)w+C(Y), with deg B<=3 and deg C<=6. There are eleven unknown coefficients after normalizing the coefficient of w² to one.

The exact gate quadratic_pullback_gate.py/json enumerates all 1820 twelve-subsets and row-reduces their twelve linear equations over F17. Its exhaustive ranks are:

* 1686 subsets: coefficient rank11, inconsistent;
* 132 subsets: coefficient rank11, consistent;
* 2 subsets: coefficient rank10, inconsistent.

Thus there are no consistent positive-dimensional solution spaces. The 132 consistent subsets give 84 distinct pairs B,C, all defined over F17. For each, recover E=-B/2 and require E²-C to be divisible by Y with quotient of degree at most four. This quotient must be O² over the algebraic closure. The test divides its leading coefficient out, reconstructs a possible monic polynomial square, and checks that square exactly. A nonzero leading scalar is always a square over the algebraic closure, so nonsquare ground-field leading coefficients are not discarded.

For every valid square, the actual number of agreements is the number of norm-hit fibers plus the number of full fibers. No candidate reaches fourteen. All consistent norm cases and rejections are retained in the JSON certificate; lower-rank consistent cases would have been reported as unresolved rather than discarded.

Consequently the 32-node pullback has maximum agreement fourteen and precisely eight nearest polynomials over the algebraic closure of F17. This completeness transfers to the number-field pullback exactly as for the cubic seed: seven matched nodes make any degree-six competitor integral by unit interpolation; reduction has one of the eight exact fourteen-element supports; interpolation identifies the lift uniquely. A fixed algebraic closure place above17 suffices for every proposed competitor.

## Parameters and prime-field transfer

The construction has

    n=32, k=7, A=14, L=8,
    rho=7/32, a=7/16.

On the applicable first-order branch,

    F_rho(a)=(8-rho)a²-6rho a+rho(4rho-5),
    F_(7/32)(7/16)=105/8192>0,
    (11-7/32)²-117=-783/1024<0.

Thus a exceeds the first-order curve by approximately0.0023398407. The rate is 7/32, not one quarter, and agreement is 7/16, not one half. This is below the rate-based Johnson curve.

After removing finitely many bad primes, splitting primes of the number field preserve the nodes, coefficients, incidences, and their guards. Completeness can also be preserved: any degree-six threshold candidate is determined by seven domain points, so there are finitely many support interpolants; all unwanted match differences that are nonzero in characteristic zero stay nonzero outside finitely many primes. Hence the complete nearest list8 occurs over arbitrarily large prime fields.

No polynomial pullback in this argument increases the number of known candidates. It therefore does not establish unbounded list size at fixed rate or agreement margin. The new seed is useful as a concrete target for operations that genuinely increase the list.
