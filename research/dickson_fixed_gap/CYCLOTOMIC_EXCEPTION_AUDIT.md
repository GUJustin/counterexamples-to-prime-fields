# Exceptional-characteristic audit of fixed cyclotomic support patterns

September 17. This is a research obstruction, not a new list construction.

## Bounded scan, all primitive-root embeddings

`scan_cyclotomic_exceptions.cpp` uses the original Dickson supports and
maps their nodes g^j to zeta^j. It checks every prime q=1 mod n in the
specified range and every primitive nth root in F_q. A rank below n-K
is the criterion for a possible non-codeword received word.

| seed | n | q cutoff | primes | primitive-root embeddings |
|---:|---:|---:|---:|---:|
|17|16|100000|1188|9504|
|41|40|100000|582|9312|
|97|96|20000|71|2272|
|193|192|20000|36|2304|

Among all 23392 embeddings, the only exceptions are the original seed
prime, with the primitive root g or its inverse. Each has rank n-K-1.
The scan found no larger prime to which one of these full patterns lifts.
`verify_cyclotomic_exception_scan.py` independently checks the exact
prime and embedding counts, replays every exceptional rank, and checks
two full-rank new characteristics per seed, including the largest.
This bounded scan alone gives no conclusion beyond its cutoffs.

## Complete classification for n=16

For the seed17 pattern, `cyclotomic16_integral_audit.py` eliminates the
cutoff. Work in Z[zeta_16]=Z[X]/(X^8+1). Each interpolation relation is
cleared by its anchor Vandermonde product. Its coefficients are algebraic
integers, and it is equivalent to the original relation whenever the
nodes are distinct. The script checks that every degree-below4 monomial
satisfies each relation, independently validating the row construction.

Normalize the received word to vanish at four fixed domain nodes by
subtracting its degree-below4 interpolant. This loses no non-codeword
solutions. Restriction of scalars on the remaining12 coordinates gives
an integer matrix with128 rows and96 columns. A particular96-row square
minor has determinant of absolute value

    2^161 * 17^2.

Thus it is nonsingular in every odd characteristic other than17.
For an odd prime q, X^8+1 is squarefree. The restriction-of-scalars
matrix decomposes over its field factors, so nonsingularity excludes
a nontrivial normalized received word at every primitive-root embedding,
including embeddings over extension fields. The original characteristic17
is known to admit the seed. Characteristic2 cannot have16 distinct roots.
Therefore **17 is the only possible characteristic for a nontrivial
realization of this full support pattern on its natural cyclotomic lift**.

The integral row-lattice index is also computed by modular Hermite normal
form and is exactly 2^151*17^2, consistent with the minor certificate.
The minor alone suffices for the exclusion; no unproved factoring or
heuristic rank test enters it. The selected cyclotomic rows and exact
factorizations are recorded in the verification JSON.

An initial direct HNF computation hit the384MiB memory guard and stopped.
The final implementation first removes the four normalized coordinates
and uses the nonzero square-minor determinant as a valid modulus for HNF.
It completes in about one second at about59MiB. The failed resource report
is retained separately; do not restore the original unbounded approach.

## Scope

This complete result concerns n16 and the full fixed support pattern.
It does not classify the larger seeds outside the scan ranges, arbitrary
moving domains, or other selected sublists. None of the results here
provides a new fixed-gap short-domain counterexample.
