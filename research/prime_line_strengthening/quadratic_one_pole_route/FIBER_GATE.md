# Complete finite gate for a quadratic cover and one projective pole

For the polynomial cover X=U² (more generally U²+c), write N(U)=E(X)+U O(X), deg E,deg O<=3, and ell=d1 U+d0. The full-fiber conditions at X=x are

    E(x)=d0 w(x), O(x)=d1 w(x).

Hence every full fiber is a zero of L=d1 E-d0 O, of degree<=3. If L=0 and d1!=0 then N=ell O/d1 is improper. If d1=0, L=0 means O=0 and deg N<=6; this cannot be a proper pole-at-infinity witness of degree7. Thus every proper witness, including infinity, has at most3 full fibers.

Take any14 of its matched core points. Let F be the set of selected full fibers and E0 the set of empty fibers. Since there are14 fibers of size2, |F|=|E0|=f<=3. Every remaining fiber contributes exactly one chosen point. Let M_x be the set of old candidates matching the received word at the base point x. Each candidate matches7 of the14 base fibers. Since N-ell H_i is nonzero of degree<=7 (properness ensures nonzero), the selected matches satisfy, for every i,

    sum_{x in F}1[i in M_x] <= sum_{x in E0}1[i in M_x].

Conversely, the gate enumerates all disjoint F,E0 of equal size<=3 obeying these necessary inequalities, and every choice of one root on the remaining fibers. This is an exhaustive necessary support enumeration, not a sufficiency claim. For the Paley incidence matrix there are1,7,42,252 pairs at f=0,1,2,3 respectively, giving152576 sign assignments before symmetry.

For X=U², multiplication U->zeta^4 U rotates both base orbits by one step and rescales received values by zeta^5. It preserves the rational-witness class and properness. Choose one simultaneous cyclic representative of (F,E0). The involution U->-U preserves each fiber and its word, so fix the selected root of the first single fiber. This leaves44 full/empty representatives and17920 rank tests. No other symmetry quotient is used.

For each support the homogeneous14-by10 matrix has columns N_0,...,N_7,d1,d0 and rows

    (1,u,...,u^7,-u*w,-w).

A kernel vector is checked for ell!=0, properness, pole exclusion, and its actual matches against all28 points. If d1!=0 the pole b=-d0/d1 must be outside the core and N(b)!=0. If d1=0, the infinity pole requires N_7!=0. These conditions include both projective pole cases. A nullity-one kernel has one projective point; nullity two is exhaustively enumerated over F29². Higher nullity is explicitly reported unresolved rather than rejected.

The pilot field is F29[j]/(j²-2): 2 is nonsquare modulo29, and29=1 mod7, so the base word lies in F29 and every quadratic fiber splits in F29². The prepared bank has28 distinct nonzero nodes. A finite-field witness is only a lead for the desired characteristic-zero/large-prime construction; no lift follows merely from its existence.

## First pilot result

The sole authorized fixed-cover pilot, psi=U² over F29², completed in0.56 seconds under the384MiB/60sec watchdog. All17920 homogeneous matrices have rank10. There are no kernel vectors, no candidate guard ambiguities, and no unresolved higher-dimensional strata. This rules out the proper one-pole witness on this fixed finite-characteristic cover even after extending the coefficient field. It does not rule out shifted or general rational quadratic covers, other primes, or the two-branch-value family. No further cover scan was run.

Files: `fiber_patterns.py/json` (complete incidence enumeration), `prepare_pilot.py`, `pilot_bank.json`, `pilot.in`, `pilot.cpp`, `pilot.summary.json`, empty `pilot.hits.jsonl`, and `pilot.resources.json`. The C++ field implementation is exact lookup-table arithmetic in F29[j]/(j²-2). Full-rank claims currently have one implementation; an independent saved-minor replay has not yet been performed. A characteristic-zero specialization certificate would additionally make the correspondence of every lifted fiber labeling and nonzero minors explicit; it is not silently claimed here.
