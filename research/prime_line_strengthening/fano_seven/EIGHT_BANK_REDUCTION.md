# Every surviving eight-cubic bank contains orbit 7

Assume eight distinct degree-at-most-three polynomials each agree at least
seven times with a word on fourteen distinct points. The standard pair-count
bound forces exactly seven matches each, exactly four matching candidates
at every node, and exactly three common matches for every pair. (For nine
candidates, the minimum pair-incidence count is112, exceeding108, so eight
is already the general elementary upper bound.)

Delete candidate8. Its seven agreement nodes become the triple blocks T;
the other seven nodes remain quadruple blocks, whose complements form C.
Conversely, any seven-bank ordered design (T,C) has a UNIQUE possible
incidence extension to eight: adjoin candidate8 to each T block and retain
the quadruples [7] minus C. Thus no additional eight-design enumeration or
assumption of Hadamard-design uniqueness is required.

`eight_bank_removal_types.py` expands the eight published seven-bank
representatives under every S7 permutation into the independently certified
6150 labelled pairs. For each representative it builds this unique extension
and deletes each of the eight candidates, then classifies the resulting
ordered pair by literal lookup. The complete labelled deletion supports are
saved in `eight_bank_removal_types.json`.

Removal types, in candidate order1,...,8:

| Starting orbit | Eight removal types |
|---|---|
|0|3,3,0,6,0,3,3,0|
|1|1,1,5,5,1,1,1,1|
|2|2,2,7,2,2,2,2,2|
|3|3,0,6,0,3,3,0,3|
|4|4,4,4,4,4,4,4,4|
|5|5,1,1,1,1,1,1,5|
|6|0,0,0,3,3,3,3,6|
|7|2,2,2,2,2,2,2,7|

The proved odd-characteristic exclusions of orbits0,1,3,4,5,6 leave only
orbits2 and7. An extension of orbit2 has an orbit7 deletion. Consequently
EVERY surviving eight-bank contains a seven-bank of orbit7. The incidence
combinatorics alone does not exclude eight: orbits2 and7 close under the
relevant deletions.

Therefore a complete classification of admissible orbit7 realizations,
combined with failure of the eighth cubic for every classified realization,
would prove the universal bound seven. The existing exact positive
number-field orbit7 realization has no eighth cubic, but that fact alone is
not a classification. Any use of rational Groebner arithmetic must state its
characteristic scope and justify saturation and all omitted denominator
loci. No universal max-seven theorem is claimed by this note alone.
