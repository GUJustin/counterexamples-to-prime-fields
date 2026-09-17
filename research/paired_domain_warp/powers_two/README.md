# Deterministic powers-of-two examples

The core evaluation coordinates are `±2^i`, with padding `±1`. Every nearby
parameter has a unique codeword, recovered by an elementary integer decoder.
The nearby count exceeds the proposed numerical bound exponentially, while
parameter zero is one coordinate short of maximum RS distance.

The proof in [deterministic.tex](deterministic.tex) uses the exact list
classification in [../unique.tex](../unique.tex). The internal audit is
[../UNIQUE_PROOF_AUDIT.md](../UNIQUE_PROOF_AUDIT.md).

- `check.py`: exhaustive small support recovery and finite parameter search.
- `verify.py`: independent rational decoder and exact finite arithmetic.
- `check_two_levels.py`: exhaustive interpolation-pencil distance profiles.
- `check_two_adic.py`: the signed-power valuation identity.
- `deterministic_instance.json`: length82, dimension41 over `2^1279-1`.
  It has exactly131,282,408,400 nearby parameters, all uniquely decodable.
  Their distance is38/82; every other parameter has distance40/82.

This instance's classification is deterministic, not a probability guarantee.
There is no claimed FFT-domain transfer or global list-size upper bound.
