# Restored high-agreement banks and the missing one-pole induction

## Outcome and scope

The restored archive contains explicit **prime-field** lists of six polynomials at agreement 0.49 and rate 1/4, well above the Dickson bank's 3/8 transition. Their size is bounded. The most concrete route found to an unbounded bank is a proved one-pole extension operation, but its required fresh rational witness is not supplied inductively. Moreover, the archived operation and list-to-line amplifier permit field extensions: neither alone proves a prime-ambient superlinear line example.

This is a provenance and algebra audit, not a new construction or a novelty claim. No search was run for new finite examples. PRETZEL is a lattice-signature project; the relevant restored material was instead `Documents/mca_exponent_one`.

## Exact prime-field seed

Source: `Documents/mca_exponent_one/rounds/R15_H_RAW.md`, section “A six-element list on a fixed-number coset union at agreement 0.49n”; summarized in `brief/RESULTS_INVENTORY_2026-09-10.md`, B16.

Fix m>=1 and a sufficiently large prime p with 196m dividing p−1. Let

    Omega = mu_(196m) union a mu_(4m),  n=200m,  D=50m−1,

where the two pieces are disjoint. On the first piece set w(x)=x^(98m), and set the remaining values arbitrarily. Put y=x^(49m). Each of the four values 1,−1,i,−i occurs 49m times and w=y². The six candidates are the constants ±1 and the four affine functions ell_(a,b)(y) with

    a in {1,−1}, b in {i,−i}, ell(a)=1, ell(b)=−1.

Each nonconstant affine function agrees at exactly these two y-values: its difference from y² is a quadratic with those two distinct roots. The constants also agree on exactly two fibers. Consequently every candidate has exactly 98m matches on the large component, and at least 98m on the whole domain. Their degrees are at most 49m<=D; the six candidates are distinct. Arbitrarily large primes in the indicated progression give n/p arbitrarily small. This is an actual prime-field bank, but L=6 does not grow.

The same source also gives four candidates at agreement 1/2 on mu_n, for 12|n: put m=n/6, take u in {1,eta,eta²,eta⁴} for primitive sixth root eta, and H_u=u X^m+u^(-1). The six unordered products uv exhaust mu_6. On each fiber X^m=(uv)^(-1), define the word to be H_u=H_v. Each candidate meets three fibers, hence n/2 coordinates, with degree n/6<=n/4−1.

## Audited one-pole operation

Source: `rounds/R13_E_RAW.md`, section “One-pole extension operation — proved”. Suppose n=4(D+1), and L distinct degree-at-most-D polynomials H_i each match w on at least A coordinates of Omega. Assume additionally a **proper** rational witness

    R=N/(X−a), deg N<=D+1, a notin Omega, N(a) != 0,

with at least A matches. Choose a quadratic phi whose critical value avoids Omega union {a}, then split all required fibers. Define

    G_i=(phi−a) H_i(phi),       G_(L+1)=N(phi).

Use the 2n preimages of Omega, the two preimages of a, and two further fresh points. On the first set use received values (phi−a)w(phi); on the pole fiber use 0; on the two fresh points use G_(L+1).

All candidates have degree at most 2D+2. Each old candidate matches at least 2A+2 coordinates; the new candidate gets 2A from its rational agreement and two from the fresh points. Properness guarantees the new polynomial differs from every old one. Thus

    n'=2n+4, D'=2D+2=n'/4−1, A'=2A+2, L'=L+1.

If this operation could be repeated t times, then exactly

    n_t=2^t(n_0+4)−4,
    D_t=2^t(D_0+2)−2=n_t/4−1,
    A_t=2^t(A_0+2)−2,
    L_t=L_0+t.

The code dimension D_t+1 is exactly n_t/4 at every step. The agreement ratio tends to (A_0+2)/(n_0+4); it increases when A_0<n_0/2 and remains exactly 1/2 when equality holds. From the six-coset seed its limit is (98m+2)/(200m+4)>.49. Thus the rate and agreement recurrence is favorable for the target around .46879. The missing issue is existence, not the recurrence.

## The exact missing identity

At every stage one needs a fresh a_t outside Omega_t and a numerator N_t of degree at most D_t+1 such that

    N_t(x)=(x−a_t) w_t(x)

on at least A_t distinct coordinates, with N_t(a_t) != 0. This is a genuinely non-descending rational witness. Pulling back another old one-pole function generally creates two poles and does not supply it.

For a fixed proposed agreement subset, the linear unknowns are the D_t+2 numerator coefficients and a_t, i.e. D_t+3 unknowns. At the six-coset seed the required A_t=98m equations exceed these unknowns by 48m−2. There is no interpolation dimension guarantee; the bank's special identities would have to enforce that many dependent conditions. Even nonzero solutions to a homogeneous reformulation must satisfy properness and pole avoidance. Merely having six nearby codewords does not establish these dependencies.

An actionable positive lemma would produce this identity from a preserved algebraic structure of the word, and show that the new word still has the same structure. No such invariant appears in the checked constructor. Repeating fixed-base rational searches is not an induction: the inventory already records fixed-base obstructions and failed one-pole companion shortcuts.

## Field and amplification audit

The constructor explicitly says to extend the field to split the quadratic fibers. The archived amplifier in `rounds/R10_F_RAW.md`, section 1.1, likewise concludes superlinear bad-label counts **after a finite field extension**, in its stated boundary window. Its proof must not be cited as a prime-ambient conclusion, nor imported without checking its parameter window after changing the length.

A characteristic-zero construction at each stage could be placed in a number field; finitely many distinctness and nonvanishing conditions, split coordinates, and any separately verified finite compiler data would then survive at sufficiently large completely split primes. This is a conditional route to prime fields, not a descent theorem for the current characteristic-109 example. An extension of a fixed finite field does not yield such a characteristic-zero lift.

In particular, `checks/eighth_word_n100_verify.py` and inventory D21 give an eight-word (n,D,A)=(100,24,49) object over F_(109^4), with agreement vector (49,49,49,50,49,50,49,49). It is not an F_109 example. `rounds/R17_E_RAW.md` treats its characteristic-zero lift as a prerequisite; the special sextic behind its eighth word has only nine old-base agreements and is not the ten-agreement input needed for the exact-half one-pole step.

The inventory's seven-word n=220,D=54,A>=108 construction has an asserted characteristic-zero family and archived lift checks (`checks/seven_word_n220_lift.txt`), but this audit did not reverify that lift. Its existence also does not supply the next rational witness.

## Recommended next mathematical test

Start from the explicit six-coset formula, not from extension-field census data. Derive whether its four-fiber structure can force a proper one-pole identity on 98m coordinates and whether the induced word admits a repeatable analogous identity. A proof of impossibility for this particular seed would end this attempt; a single additional numerical witness without a preserved structure would not establish scalability. Until such an identity is found, report only a bounded high-agreement seed and a conditional extension operation, with no prime-field superlinear or DKT-tightness claim.

## Follow-up: the proposed six-coset test is now closed

The exact rational Mason argument in `SIX_COSET_ONE_POLE_OBSTRUCTION.md` proves that no required one-pole witness exists for the six-coset seed, even over extensions and with arbitrary values on the added coset. Thus the recommendation above has been resolved negatively; do not run a search for that input. The general operation remains valid, but requires a genuinely different starting word and an inductively preserved source of rational witnesses.
