# Independent small-q modular and composite-profile audit

PASS for all supplied receipts. `verify_small_batch.py` converts each independent input, checks unique and complete pair-by-twist coverage and source-class metadata, and invokes `verify_modular.cpp`. The latter recomputes monic source/target remainders, the exact subset-overlap factor, elimination polynomials, a degree-preserving witness, and extended-Euclidean gcd certificates. It verifies primality of the reduction prime and the full order of the chosen q-th root, checking every prime divisor of q. No primality assumption on q remains.

Counts are saved in `SMALL_Q_MODULAR_AUDIT.json`. All cases certify exclusion for q=9,13,15,17,19,21,23. Controls retain the expected unresolved cases: all four q=5 cases and two of twelve q=7 cases. A noncertificate is not by itself an existence claim.

Composite census completeness is independently checked by `composite_census_independent.cpp` and `verify_composite_census.py`: recursive subset enumeration, explicit position translation, and ordered-pair difference counting replace the generator's bit-rotation/popcount route. Literal profile sets and allowed first-support lists match for q=9,15,21. The counts (all rotation classes / retained / ordered compatible pairs) are 14/9/12, 429/82/172, and 16796/408/984. Results and all canonical raw profiles are saved. Prime-q census completeness was audited separately; this audit does not reassert that computation.

Together with the previously proved degree-preserving modular specialization lemma, these receipts exclude the corresponding two-orbit cyclic interpolation systems over characteristic zero, for all supplied compatible supports and twists. They do not exclude arbitrary noncyclic banks or four-orbit constructions.
