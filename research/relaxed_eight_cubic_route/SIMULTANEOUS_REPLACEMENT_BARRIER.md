# A weighted-incidence obstruction to simultaneous replacement

This is a structural obstruction for the fixed rational eight-cubic seed and all its full-fiber covers. It uses exact pair-difference identities, not a replacement-subset scan. It does not exclude moving retained coordinates or values, changing the incumbent polynomials, or a new coupled construction.

## Exact certificate

Index the original eight polynomials by 0,...,7 as in `rational_seed.json`. Assign positive weights

    lambda = (2,2,2,4,4,4,3,3).

Every original received column has total incident weight at least 6. At any genuinely fresh coordinate, for any choice of received value, the total incident weight is at most 5.

Here is a compact exact justification of the second assertion. Strip every old base root from every pair difference. The only nonconstant residual pair differences have label pairs

    01, 06, 07, 17,

with degrees 1,2,1,1, respectively. Every three-way equality is at an old coordinate: the pair-difference gcd for each triple becomes constant after stripping old roots. The eight leading cubic coefficients in the saved affine chart are distinct, so the projective point at infinity contributes at most one match. Thus a fresh bucket either is a singleton of weight at most 4, or is one of the four listed pairs, of weight at most 5.

The old column sizes are

    3,2,4,4,4,2,3,2,4,2,5,5,4,4,4,4.

Their four size-two masks are 67,04,15,03, each of weight 6; all other masks also have weight at least 6. `verify_simultaneous_exchange.py` verifies these assertions using exact rational polynomial arithmetic and saves the residual pair polynomials and separator in `simultaneous_exchange.verified.json`.

## Replacement theorem

Retain the eight incumbent polynomials and all undeleted old received coordinates and values. Delete d old coordinates and append a genuinely fresh coordinates with arbitrary values. If every incumbent still has at least its original seven agreements, then

    5a >= 6d.

Indeed the weighted agreement loss is at least 6d, whereas the gain is at most 5a. Every incumbent originally has exactly seven agreements, so maintaining each count forces total weighted gain to dominate total weighted loss. In particular no nontrivial equal-size simultaneous replacement is possible. This is stronger than the archived one-coordinate obstruction.

For a degree-e cover with all selected fibers simple and taken in full, the old masks repeat e times. A fresh covered coordinate maps to a fresh base coordinate: all preimages of selected base coordinates have already been taken. The same bucket bound holds for the natural pulled-back sections, since their fiberwise evaluations differ from base values by a common nonzero scalar in any local trivialization. This includes rational covers and points above base infinity. Therefore the same inequality holds while preserving seven-e agreements for each of the eight pulled-back incumbents. No bound on the cover degree is needed.

## What this does and does not say about a recurrence

This rules out replacing an arbitrary fraction of the fully covered original domain at zero length cost while merely carrying the same eight words. Replacing d original-fiber coordinates has net length cost at least d/5. Thus changing a positive fraction of those coordinates after each cover has a positive normalized cost, which cannot be repeatedly hidden by subsequent pullbacks.

The ten- and eleven-cubic seeds append coordinates on which the original eight have no matches. Those columns have zero weight for this separator. Consequently this argument does not automatically exclude exchanges spending the two or three padding columns: if d0 deleted coordinates belong to the original sixteen fibers, it only forces 5a>=6d0, while deleted padding coordinates incur no weighted loss. Under an equal-size exchange with dpad padding deletions, the necessary bound is d0<=5dpad. This is a precise limitation, not a claim that a viable exchange exists.

An actual repeatable positive mechanism must therefore either use and replenish padding slack with summable normalized cost, alter the incumbent sections/retained word, or provide a fresh nearly-nearest witness without replacing a positive fraction of original coordinates. The current complete ten/eleven censuses have no fresh six-match cubic, so a fixed-word one-node promotion cannot supply that witness. None of these facts proves a universal recurrence obstruction, and no unbounded construction is claimed.
