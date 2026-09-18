# Complete ordered incidence-design enumeration for seven cubics

## Input reduction and output

The independent proof in `GLOBAL_SEVEN_CUBIC_INCIDENCE_REDUCTION.md` reduces any seven-cubic, fourteen-node, seven-agreement configuration to seven triple columns T and seven quadruple columns. Write C for the seven complementary triples of the latter. Both T and C are three-regular triple multisets on seven candidates, and their combined pair multiplicities are exactly two.

`designs.cpp` enumerates these ordered pairs exactly. Repeated blocks are allowed in the enumeration; their combined multiplicity is automatically at most two. It does not identify (T,C) with (C,T), since that swap has not been justified as an equivalence of the polynomial problem.

Results:

- 12,780 labelled seven-triple multisets with each vertex degree3 and each pair multiplicity at most2;
- ten orbits of such halves under S7;
- three half-orbits admitting a compatible other half;
- 6,150 ordered labelled compatible pairs;
- eight ordered simultaneous-S7 orbits of compatible pairs.

All eight representatives appear in `design_orbits.jsonl`. The compatible representatives happen to have no repeated blocks; this was an output, not a restriction. The aligned Fano-plus-complement design is orbit4, already excluded in odd characteristic. Orbits5–7 also have a Fano T but a differently labelled Fano C. Orbits0–3 have one of two non-Fano half-types. No polynomial realizability conclusion is claimed for the other seven representatives.

## Exhaustive algorithm

List the35 triples of a seven-element set. Recursively choose a nondecreasing list of seven triple indices, rejecting a partial list whenever a vertex degree exceeds3, a pair degree exceeds2, or a vertex cannot reach3 in the remaining number of blocks. At a leaf retain exactly the lists with all vertex degrees3. These tests reject no possible half and allow repeated triples.

For each retained half encode its21 pair multiplicities in base3. Since each digit lies in{0,1,2}, the compatible half has exactly the complementary key

    (3^21−1)−key.

A hash lookup therefore enumerates precisely all labelled compatible ordered pairs.

To quotient without redundant large searches, compute all5040 permutations of the candidates and their action on the35 triples. For each not-yet-covered half, generate its full orbit and retain the lexicographically smallest representative. For each such T, find its exact stabilizer. Retrieve every compatible labelled C using the key lookup, and quotient those C only by the stabilizer of T. This is exactly simultaneous S7-equivalence of ordered pairs: every orbit has a representative with canonical T, and any map between two such representatives must stabilize T.

`design_counts.jsonl` records the counts and watchdog summary. The C++ program was compiled against an already installed SDK and completed in0.59seconds under384-MiB/60-second limits. No unbounded search or heuristic rejection was used. `designs.resources.json` records completion.

## Next proof target

For every pair i,j, the polynomial difference P_i−P_j must be a nonzero scalar multiple of the cubic locator of its three prescribed common nodes. The remaining realizability problem is therefore the compatibility of these21 cubic locators under the triangle identities

    (P_i−P_j)+(P_j−P_k)=P_i−P_k.

The aligned Fano case admits the particularly short determinant proof in `OBSTRUCTION.md`, and the independent matroid proof in `DIFFERENCE_FACTOR_OBSTRUCTION.md`. The other seven designs should be treated using their actual locator supports; the Fano obstruction must not be applied to them without another argument. A realization in any surviving orbit would be a genuinely different positive candidate.
