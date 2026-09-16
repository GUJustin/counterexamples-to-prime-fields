# Completing the fixed rational cubic packet-map search

September 16, 2026. Exhaustive search completed and independently checked.
The exact maximum is three complete fibers. The previous
check covered polynomial cubics and rational cubics with equal values at
zero and infinity. This search covers the remaining maps.

## Why all coefficient fields are covered

A complete fiber on mu_n consists of three distinct finite nonzero roots.
Its monic locator is X^3-e1 X^2+e2 X-e3, with all coefficients in F_p and
e3 in mu_n. All full-fiber locators of a fixed rational cubic lie on one
affine line in (e1,e2,e3). Two distinct full fibers determine this line
over F_p, even if the original rational map has extension-field
coefficients. A common root of two fiber locators would be a common
factor of the pencil and would reduce its degree, so it must be excluded.

The case of constant e3 is exactly the earlier equal-zero/infinity case;
the saved exhaustive check gives at most three full fibers on the pinned
mu_256 domain. In the other case, e3 parametrizes the line injectively:

    e1=a1+s1*(e3-1), e2=a2+s2*(e3-1).

The associated normalized map is

    R(X)=[X^3+(s1-a1)X^2+(a2-s2)X] / [s1 X^2-s2 X+1].

It has R(0)=0 and R(infinity)=infinity. A common root occurs precisely
when the denominator vanishes at a root of the anchor locator
X^3-a1 X^2+a2 X-1. Testing its three known domain roots is exact.

## The product-bucket reduction

Let b be a power of two dividing n. Partition the possible products e3
into the n/b cosets of mu_b. If a nonconstant-product line has more than
2n/b full fibers, at least three products lie in one coset. Scale all
input roots so that the first of those products becomes one. Cubing is
a bijection of mu_n, so this normalization exists uniquely within mu_n.
It preserves the domain and the number of full fibers. The other two
products now belong to mu_b minus one.

There are exactly binom(n,3)/n=(n-1)(n-2)/6 product-one triples.
For each anchor, enumerate all triples at the other b-1 product levels
and hash their two slopes (s1,s2). A repeated slope supplies the required
three collinear locators. Reject common-factor pencils; for every other
candidate count its full fibers over all n possible products, using a
lookup among the normalized triples. Thus

    full-fiber count <= max(2n/b, largest candidate count).

For b=n this gives the exact maximum as soon as a two-fiber witness is
available: every line with at least three fibers is examined. The
implementation also finds and checks a two-fiber witness at startup.

## Implementation and verification

The C++ code uses precomputed product levels and a stamped flat hash
table, avoiding a stored table of all pairs. An independent Python
enumeration of all coefficient-point pairs checks the exact maxima
at mu_8/F_97 and mu_16/F_193. Python also evaluates every chunk's
recorded rational-map witness at every domain point and checks that
its full-fiber count matches the C++ result.

Chunks cover disjoint, explicit anchor-index intervals. Checkpoints are
atomic and record the C++ source hash. The first run hit a disk-space
failure after one saved chunk; its memory was within the 384 MiB limit.
Own temporary PDF renders were removed, the checkpoint writer was made
atomic, and the verified first chunk was retained for the resumed run.

## Relevance to better.codes

Composing such a map with X^1024 gives degree-3072 packets on the pinned
mu_262144 domain. A fixed map with f complete fibers supplies at most 2^f
unions of those packets; a fixed core does not increase that count.
The certified maximum is three, so there are at most eight unions.
This closes the fixed-map cubic packet route, whose required bank size
is 274980728111395088. Maps varying
with the candidate and constructions using partial fibers remain outside
the conclusion. No score improvement is inferred from an exclusion.

## Execution record

The bucket-256 run examined 29,715,666,375 anchor/triple pairs in 85
disjoint chunks covering all 10,795 anchors. It found 22,692 nondegenerate
candidate occurrences, none with more than three complete fibers, and
recorded explicit three-fiber witnesses. The elapsed time was 524.46
seconds, with sampled peak process-group RSS 176,192 KiB under the
384 MiB watchdog. This run completed without interruption.

The saved `verification.json` and `checkpoints.json` retain the source
SHA-256, exact ranges, counts, and witnesses. The separate default
checker validates these ranges and all 85 witnesses, independently
exhausts all pencils on the two small fields, and reruns the complete
constant-product search (58,260,615 pairs). That check also passed.
Default checking does not replay the 29.7-billion-pair enumeration;
`verify.py --full` does. Both C++ sources are included.
