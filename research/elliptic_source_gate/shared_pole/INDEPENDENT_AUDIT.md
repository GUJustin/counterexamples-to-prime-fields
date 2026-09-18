# Independent shared-pole pilot audit

Status: PASS. `verify_pilot.py` reads only the saved data and independently checks the elliptic group labeling, all 625 label additions, curve point count 225, Paley autocorrelation, and thirteen distinct candidate polynomials. It verifies the cleared rational formula at all 199 nonpole field coordinates (more than the degree bound 25), and independently checks the original elliptic translation sum at every nonpole rational elliptic point. It does not import or run the generator.

The polynomial degrees are 24 for the zero label and 25 for each of the other twelve labels. Across all 211 affine coordinates, maximum equal-value bucket sizes have histogram {1:134, 2:63, 3:2, 6:12}. The sum of the 100 largest buckets is exactly 227. For any choice of 100 distinct affine coordinates and any received word, total agreements of the thirteen polynomials are therefore at most 227, so at least one candidate has at most floor(227/13)=17 agreements. This is an upper bound, not an assertion that a word attaining minimum agreement 17 exists.

The replay took under one second and saved `pilot.independent.json`. This is a complete decision bound for this fixed bank over F211. It does not establish a general shared-pole theorem, nor a result for changed curves, labels, normalizations, larger fields, or projective domains containing infinity.
