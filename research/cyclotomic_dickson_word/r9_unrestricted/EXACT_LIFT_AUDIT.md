# Independent exact cyclotomic lifting audit

The sole modular representative has twelve matching indices. Independent interpolation on the reversed last nine, in Q[z]/(z^12-z^6+1), satisfies all twelve exactly. Its full mu9 rotation orbit has three distinct polynomials, all with exactly twelve matches. Coefficients reduce to the saved modular coefficients at z=41 mod1009. Together with the exhaustive modular search, this proves characteristic-zero maximum twelve and complete nearest-list size three.

The shared independent implementation is `../exact_unrestricted_replay.py`; it imports no generator code and saves every coefficient and support in `exact_replay.json`. Field coefficients are serialized in ascending powers of the indicated primitive root.

For completeness transfer, any characteristic-zero candidate with at least the searched threshold of matches is interpolated by k matching nodes. At the recorded split prime all nodes remain distinct, so interpolation makes its coefficients integral there, and its reduction belongs to the modular survivor list. Every survivor has exactly the threshold number of matches, so the characteristic-zero support must be that entire support. It is therefore enough to interpolate any k of those indices and check the remainder. The rotation symmetry covers every member of each canonical orbit. This exact-threshold fact is essential: a modular survivor with more matches would require checking multiple subsets.

This receipt audits the exact lifting and its completeness-transfer logic. The exhaustive finite search and its coverage are separate artifacts, not independently rerun here.
