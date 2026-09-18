# The proposed 20-mask pattern and the even-seed quotient

The incidence pattern in `relaxed_seed_design.json` is combinatorially
feasible for eight sextics on 32 nodes. It is NOT feasible for the
preserved EVEN four-quadratic seed, even if its blocks specify only
selected agreements and additional agreements are permitted.

Write the four old candidates as P_i(Y)=u_iY+u_i^{-1}, with Y=T^2.
Their six pair-intersection values are distinct. The preserved corrections
are cubic polynomials in Y:

    Q_i^epsilon(Y)=P_i(Y)+e_i^epsilon D_i(Y),
    D_i(Y)=product_{j!=i}(P_i(Y)-P_j(Y)).

The two coefficients for a given i must be distinct if the eight
candidates are distinct. Therefore their difference is a nonzero scalar
multiple of D_i and cannot vanish at a fresh Y value. At such a value,
any actual agreement mask contains at most one candidate from each
old pair. In particular it has size at most four.

## Pair-incidence count after passing to Y

Eight distinct cubics have total pair-intersection budget

    binom(8,2)*3=84.

At the six old Y values the four preserved candidates from two old
pairs agree. These already consume at least6*binom(4,2)=36, leaving at
most48 for all fresh Y values.

The proposed20 new T-node masks are all distinct. They consist of four
quads and sixteen triples, all transversal to the four candidate pairs.
Direct inspection shows that none of the sixteen triples is contained
in any of the four quads.

A new quad's Y value cannot coincide with another requested node's Y:
its actual mask would have to contain the union of the two requested
masks, which has size at least five or contains both variants of a pair.
Both alternatives are impossible at a fresh value. The four quads
therefore contribute at least4*binom(4,2)=24 fresh pair incidences.

The remaining sixteen triple nodes can occupy Y values singly or in
pairs, since a quadratic map has at most two distinct preimages. A
single triple costs at least3 pair incidences. Two distinct requested
triples at the same Y require an actual mask containing their union.
If compatible, that union has size four and costs6, again at least3 per
T node; an incompatible union is impossible. Thus the triples cost at
least48. The fresh cost is at least72, exceeding the available48.
This contradiction permits extra agreements and includes T=0.

Consequently amplitude elimination for this exact pattern and EVEN seed
is unnecessary. It would only reprove this quotient pair-budget failure.
This does not exclude the same sextic pattern based on a non-even
four-quadratic seed.

## The viable reformulation

For the even route, formulate the problem directly as eight cubics on
16 Y nodes with seven agreements each. Retaining six old Y values
requires ten fresh values, with four new agreements per candidate.
Two fourfold blocks and eight triple blocks give the needed32 new
incidences. After quadratic pullback, EACH mask is doubled: four quad
occurrences and sixteen triple occurrences, but only ten distinct masks,
not the twenty distinct masks in the original JSON.

This cubic16-node target is not covered by the saturated cubic14-node
max-seven theorem. Its total minimal pair count is72, below the cubic
budget84. A realization would pull back to the desired n32,k7,A14
parameters. It remains an open construction target.
