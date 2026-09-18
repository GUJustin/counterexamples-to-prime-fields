# Translated-grid quadratic bank: independent constructive audit

2026-09-18. **PASS with two repairs:** isolate the exceptional zero-polynomial label, and add neutral coordinates if the conclusion is to lie below Johnson. This is an asymptotic existence proof in a vanishing-rate, prime-field quadratic code. No finite onset or concrete grid is certified here.

## 1. A rational-square multiplicative Sidon bank

Let H grow. Choose a prime p≡1 mod4 with 2H^4<p<4H^4; existence for all sufficiently large H follows from the prime number theorem in the fixed progression 1 mod4. Among the primes in [H/2,H], a largest quartic-character class has Ω(H/log H) elements. Split it into two disjoint sets of comparable size.

Use these as the vertex sets of a C4-free bipartite graph with L=Θ((H/log H)^(3/2)) edges. A concrete existence construction uses incidence between the q² points and q² nonvertical lines in Fq², for a prime q comparable to the square root of the available vertex count: it has q³ edges and no C4. Vertices can be assigned distinct primes arbitrarily. Each edge (a,b), with a in the first set and b in the second, gives θ with θ²=a/b and θ itself square in Fp: the ratio is a fourth power. Choose one such θ for each edge.

The θ are multiplicatively Sidon, including repeated pairs. Indeed equality of two pair-products, after squaring and clearing denominators, is a congruence between integers at most H^4. Since p>H^4 it is equality over the integers. Unique factorization and disjoint numerator/denominator prime sets imply either the same edge multiset or a C4; the latter is excluded. Thus there are no distinct unordered pairs with the same product.

Set Pθ(X)=θ+X²/θ. Every pair θ≠φ meets at exactly the two distinct Fp points x²=θφ. These pair intersections are disjoint by Sidonicity. At such a point the common value is θ+φ; a third bank polynomial cannot attain it, since (η−θ)(η−φ)=0 would be necessary.

The core consequently has N0=L(L−1) coordinates, each bank polynomial has A=2(L−1) matches, and any quadratic outside the bank has at most L core matches: count at most two intersections with each bank member and two incidences per matched core node.

## 2. Randomly translated grid

Put M=floor(L/4). Choose u0,v0 independently uniformly in Fp. For 1≤u,v≤M let U=u0+u,V=v0+v. Keep only pairs with U,V nonzero and V/U a nonzero square. Select one square root x of each ratio, using a fixed rule; discard repeated ratios and all ratios belonging to core points. Each retained coordinate retains one associated (U,V).

Before deletions, the expected number of eligible pairs is

    M² (p−1)²/(2p²).

For two different grid pairs, equality of their ratios is a nontrivial affine linear equation in u0,v0, so its probability is at most 1/p. Similarly hitting any specified nonzero core squared-coordinate has probability at most 1/p. Removing repetitions loses at most the number of colliding unordered pairs. Thus the retained count X satisfies

    EX ≥ M²(p−1)²/(2p²)
          − binom(M²,2)/p − M² binom(L,2)/p
       = (1/2−o(1))M².

Since 0≤X≤M², the event X≥M²/4 has probability bounded below by a positive constant (indeed at least 1/3−o(1)). No concentration theorem is needed.

## 3. Many rich fibers in every bank, deterministically

For the retained grid put g(x)=1/U and f(x)=c0/U. A bank match at pencil label λ obeys

    λ+c0 = θu0+v0/θ + (a u+b v)/(bθ).

For each bank, all possible raw labels are in an affine image of an integer interval of size K≤3HM. For large H this interval has length <p, so it does not wrap. Since gcd(a,b)=1 and a,b≥H/2, any fixed value of a u+b v is attained by at most

    Dmax≤1+2M/H≤3M/H

grid pairs. This bound survives every deletion.

Let d=floor(M/(64H)), which tends to infinity. On X≥M²/4, labels with fewer than d retained points account for at most K(d−1)≤3M²/64 points. Thus every bank has at least

    (M²/4−3M²/64)/(3M/H) ≥ HM/16

labels with at least d retained grid agreements. This conclusion uses the same global retained-point count for every bank; no simultaneous per-bank probabilistic estimate is missing.

## 4. Removing cross-bank collisions

Use, for each θ, the entire fixed integer interval above as a raw-label superset, of size at most K. Raw labels from different banks coincide with probability exactly 1/p: their difference has coefficients θ−φ and θ^−1−φ^−1 in u0,v0, and these are nonzero. The expected number Ccross of unordered cross-bank raw-label collisions is at most

    binom(L,2) K²/p = o(LHM),

because LHM/p=O((log H)^−3). Markov implies Ccross≤LHM/64 with probability 1−o(1). Intersecting this with the positive-probability retained-count event proves simultaneous existence.

There are initially at least LHM/16 rich bank-label pairs. Removing every pair involved in a cross-bank collision removes at most 2Ccross of them. At least LHM/32 remain; each resulting label has exactly one possible bank owner, even among the non-rich raw labels. This is a union count, not merely a witness-incidence count.

Choose c0 nonzero outside the union of raw bank labels. Such a choice exists since that union has size ≤LK=o(p). This makes λ=0 a far source. Translating by c0 does not affect collision counts.

## 5. Nonbank exception and source/common agreement

A nonconstant quadratic matches f+λg on at most two coordinates for each fixed U, hence at most 2M grid coordinates. A nonzero constant matches only one row, hence at most M. The **zero polynomial at λ=−c0** matches the entire grid. This is the necessary exception to the proposed generic nonbank bound. Discard this one label from the rich-label count.

On the core set f equal to the pair-intersection word and g=0. A nonbank quadratic, except at that exceptional label, then has at most L+2M core-plus-grid agreements. Every bank retains its A core agreements and at least d additional agreements at each retained rich label.

For ordinary CA, an explaining direction G≠0 has at most two zeros on all zero-direction coordinates and at most 2M grid matches to g. An explaining direction G=0 restricts joint matches to the zero-direction coordinates; there the intercept's maximum is A, as maintained by the neutral construction below. Therefore CA=A. At least one bank attains this lower bound on the core.

Every λ outside all translated raw bank labels and outside {−c0} has exact maximum agreement A: all bank words attain A, and all nonbank words have strictly fewer for large L. There are many such λ because LK=o(p). Choose any two as endpoints. Their affine mixtures enumerate the same received affine line, and ordinary CA is invariant under the invertible change of the two source coordinates. Thus both endpoints are exactly far, and the counted nonexceptional rich labels have singleton threshold lists.

## 6. Neutral padding to strictly below Johnson

The unpadded domain has size only about L²; its agreement threshold A+d is above the degree-two Johnson threshold there. To claim below-Johnson behavior, put

    T=A+d,        n=floor(T²/2)+1.

Append n−N0−X neutral coordinates with g=0,f=x³. Exclude all old coordinates, zero, and every root of x³−Pθ(x), at most 3L additional forbidden points. Since p≫n=Θ(L²), there are enough coordinates. Banks gain no neutral agreements. A nonbank quadratic gains at most three, so its nonexceptional total is ≤L+2M+3<A for sufficiently large L. On the zero-direction core plus neutral block its total is ≤L+3<A, preserving the CA argument.

There are therefore at least LHM/32−1 distinct labels with singleton lists at threshold T, exact endpoint/common agreement A, and gap d. One has T²<2n exactly, so the threshold is strictly below the usual degree-two Johnson agreement. Also T/sqrt(n)→sqrt(2), whereas the first-order agreement curve for dimension three has asymptotic n*a1(3/n)/sqrt(n)→sqrt(3/2). Hence the construction is strictly above first order for all sufficiently large members. The coefficient field and evaluation domain are prime-field, and characteristic is much larger than the message degree.

## 7. Scale and honest scope

With L=Θ((H/log H)^(3/2)), M=Θ(L), the resulting scales are

    n=Θ(L²)=Θ(H³/(log H)³),
    d=Θ(L/H)=Θ(n^(1/6)/log n),
    number of singleton nearby labels = Ω(HL²)=Ω(n^(4/3) log n),
    p=Θ(H^4)=Θ(n^(4/3)(log n)^4).

The constants in these statements are fixed. Thus the label count has the optimal order L times the number of grid coordinates divided by d within this particular fixed-bank incidence budget. This last observation is not a universal RS upper bound.

The result has fixed message dimension three and rate tending to zero. It is not a fixed-rate counterexample or a benchmark construction. It is an asymptotic existence proof; a concrete implementation, finite onset, and a separate adversarial audit of this proof would still be valuable before manuscript inclusion. No large computation was used.
