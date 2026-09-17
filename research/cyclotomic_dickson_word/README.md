# The Dickson received word on a characteristic-zero cyclic domain

September 17, 2026. Exact finite exploration of a possible source for
large-prime fixed-gap lists. No growing-family conclusion is established.

## Word and exact support criterion

Let n=4k, choose a primitive nth root zeta in characteristic zero, and
use the domain mu_n with received word

    W(X)=(X^k-1)^2/2.

This is the characteristic-zero analogue of the full-length prime-field
Dickson word. Its degree2k is larger than the agreements sought, so the
existing boundary-locator theorem for degree(W)<=A does not apply.

For any k+1 distinct nodes S, a polynomial of degree<k agrees with W
on S if and only if

    h_k(S)=2,

where h_k is the complete homogeneous symmetric polynomial of degree k.
Indeed the kth divided difference of X^(2k) is h_k(S), that of X^k
is1, and that of the constant is0. The divided difference of W is
therefore h_k(S)/2-1; its vanishing is exactly the interpolation condition.

`search.py` enumerates all such supports for the small lengths below.
It first evaluates this identity at a primitive nth root in a split
prime near one million. Nonzero reductions cannot come from a zero
characteristic-zero value, so this is a safe exclusion filter. Every
survivor is then tested with integer coefficient arithmetic modulo Phi_n.
All surviving supports in these cases are genuine; the search does not
equate modular agreement with characteristic-zero agreement.

`verify.py` independently performs Lagrange interpolation in Q(zeta_n),
evaluates the resulting polynomials at every node, and checks that their
full supports reconstruct exactly all retained (k+1)-subsets.

| n | k | complete list with more than k agreements | agreement of every member |
|---|---|---|---|
|4|1|0|--|
|8|2|0|--|
|12|3|3|4|
|16|4|0|--|
|20|5|0|--|
|24|6|9|8|
|28|7|28|8|

The zero entries mean that this particular word is a deep hole for the
corresponding characteristic-zero code. For example, the cyclic n16 word
has no five-agreement degree-<4 candidate in characteristic zero, although
its reduction over F17 has22 candidates with six agreements. This does
not contradict the separately certified free-domain lift over F17: that
lift deforms the nodes and word rather than preserving this cyclic model.

## Testing the apparent 3-to-9 growth at a fixed gap

The n12 and n24 rows both have rate1/4 and gap1/12. We tested whether
their list-size increase continues, rather than extrapolating from two
small examples.

Put n=12r, k=3r, and target A=4r. The known candidates vanish on at
least2r of the3r zero-word coordinates mu_(3r). `structured_search.py`
enumerates all2r-subsets of these zero nodes, modulo the exact rotation
symmetry. Factoring out their locator leaves a polynomial of degree<r.
It then exhausts every r-subset of the9r nonzero-word nodes as a
determining support for that residual polynomial.

Every candidate in this shared-zero class over the chosen split prime
is covered: a target candidate has at most3r-1 zero-word agreements,
so it has at least r+1 nonzero-word agreements and supplies the needed
determining support. The search normalizes duplicates under rotation.
Characteristic-zero lifting is a separate exact verification, not an
assumption about the prime-field outputs.

| n | k | A | certified characteristic-zero list from this class |
|---|---|---|---|
|12|3|4|3|
|24|6|8|9|
|36|9|12|3|
|48|12|16|9|

The n36 and n48 entries are not unrestricted complete-list claims.
Every saved finite-field orbit lifts, and exact coefficient inspection
shows that all these witnesses descend to length12 or24 by composition
P(X)=R(X^h). In particular, the nine witnesses at length48 are composed
copies of the earlier families, not a newly larger bank. The fixed-gap
growing-list target remains open.

## Reproducibility and limitations

The outputs save split primes, chosen primitive roots, all surviving
support tests, exact cyclotomic remainders, and exact polynomial
coefficients in descending powers of the primitive root. The independent
verifier records full agreement sets and orbit sizes. At length48 the
structured search checks2,532,915 residual interpolations across43 zero
pattern orbits. All jobs ran sequentially under384MiB/60-second limits;
the largest peak RSS was about133MiB.

The support census is complete only at the printed small lengths. The
shared-zero search is restricted to its stated class, and its exact
cyclotomic lifts are positive certificates. There is no general theorem
that this word has bounded lists at fixed gap, and no assertion about
arbitrary received words or arbitrary domains.

These data stay in research notes. They do not change the159-page paper,
establish prime-field exponent tightness, or improve better.codes.
