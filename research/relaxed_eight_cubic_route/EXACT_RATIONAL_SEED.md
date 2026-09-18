# Exact rational model of the eight-cubic seed

The eight-cubic seed has an explicit rational realization. Rational reconstruction was used only for discovery: `rational_seed.py` hardcodes the rational table below and verifies all incidences with Python Fraction arithmetic, without reading the p-adic lift. Its machine-readable output is `rational_seed.json`.

Normalize the projective parameter line by sending nodes 10,11,3 to infinity,0,1, respectively, using zero-based indices. Subtract the old polynomial P3 from all candidates and the received word, then scale so that P4=X(X−1). In an original affine coordinate x the parameter change is

    X=((x3−x10)/(x3−x11))*(x−x11)/(x−x10).

Transform sections of O(3) using the cubic denominator factor, not merely by substitution. The resulting nodes, in their original order, are

    11/9, 11/5, 77/65, 1, 66/65, 22/25, 6/5, 55/52,
    11/10, 77/95, infinity, 0, 33/5, 33/25, 99/95, 33/35.

The ascending coefficient rows are

| Candidate | constant | X | X² | X³ |
|---|---:|---:|---:|---:|
| P0 | 693/25 | −165/2 | 883/11 | −6175/242 |
| P1 | −99/14 | 90/7 | −81/14 | 0 |
| P2 | −198/25 | 69/5 | −65/11 | 0 |
| P3 | 0 | 0 | 0 | 0 |
| P4 | 0 | −1 | 1 | 0 |
| P5 | 0 | −12/5 | 38/11 | −130/121 |
| P6 | 0 | 6 | −54/11 | 0 |
| P7 | 0 | −6 | 116/11 | −50/11 |

At infinity evaluate a degree-three section by its X³ coefficient. The received word is specified uniquely by any candidate incident to each node; the verifier checks that all incident candidates give the same rational value and that every candidate has exactly its original seven-node support. All sixteen word values are serialized in `rational_seed.json`.

The fresh section is exactly

    Q=(14/9)P1=−11+20X−9X².

Its agreement support is exactly {0,1,3,8,10}. Thus the persistent fifth match is an exact rational identity, not a conclusion from finite p-adic precision. Q is distinct from every listed candidate.

For ordinary affine Reed–Solomon coordinates use U=1/(X−3), with transformed sections U³P(3+1/U). The node at infinity becomes U=0; every other node becomes 1/(X−3). Scale the received value at finite X by U³. The complete affine coefficient/node/word tables and Q are also in the JSON. Three is absent from the projective node set even modulo17, so this chart has integral, unit-separated coordinates at17. (An earlier exploratory X−2 chart was replaced before the final certificate.)

The normalized table reduces to the projective/gauge transform of the certified F17 seed: its parameter map there is X=3(x−12)/(x−11). Therefore the previous complete cubic census applies after reduction. Every rational or algebraic cubic with seven matches is determined integrally by four matching nodes and reduces to one of the eight known seven-match cubics. Seven-point support equality then forces it to equal that known rational lift. Hence this explicit rational source retains the complete eight-element nearest list and maximum agreement seven. Only finitely many prime specializations are exceptional; an algebraic number-field splitting argument is unnecessary for the rational source itself.

In particular, Q has exactly five old matches. The generic-padding lemma applies with two new rational coordinates, avoiding the finite set of equality roots between Q and every other four-point interpolant. It yields a rational length-eighteen cubic source with a complete nine-element nearest list of agreement seven. This note proves the input and existence of suitable padding; the actual chosen padding coordinates and their avoidance receipt should be recorded separately.

This is a fixed finite construction and an improvement in explicitness and computability, not an unbounded-list or asymptotic amplification result.

## Correct complete quadratic cover

The final affine chart has the exact residue coefficient identity

    q_i(U) = 10 (P_i(11−3U) − P_3(11−3U)) mod17,

where P_i are the original displayed F17 cubics and P_3=3+Y+15Y²+7Y³. Received values obey the same gauge. The correct rational cover reusing the existing completeness certificate is U=(11−T²)/3. Its radicands 11−3u_j reduce in order to 1,...,16, so its thirty-two points are unit-separated over the unramified quadratic17-adic extension. The pulled-back sextics reduce to 10(P_i(T²)−P_3(T²)). Every coefficient and all radicands are independently verified in `verify_rational_cover.py` and `rational_cover.verified.json`, which also records the exact rational sextics. The cover U=T² in this affine chart does not have this certificate and is not substituted for it.

The manuscript fragment `eight_cubic_smooth_seed.tex` now uses this explicit rational proof and retains its original theorem label. The previous Hensel derivation is archived in `eight_cubic_hensel_archived.tex`.
