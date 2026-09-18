# Exact octahedral half-agreement gate

The proposed eight-section octahedral construction does not attain18 agreements on the36-point domain, under either the untwisted or sign-twisted equivariant-word action described in STRUCTURE.md.

The untwisted obstruction is the elementary two-level root count in that note. For the sign twist, six special-orbit zero patterns exhaust the possible candidate sections up to scale. `pilot.py` constructs the full group of24 projective matrices over Q(i,sqrt(2)), verifies its sign homomorphism, verifies invariance of F8, constructs the four C3-orbits on the special12 points, and checks every candidate's C3 invariance with the exact determinant linearization.

For each candidate it checks all18 possible choices of one additional even coset and two odd cosets. A gcd of the corresponding exact polynomial differences gives every possible generic-orbit parameter. Repeatedly removing factors supported on F6*F8*F12*P removes precisely the forbidden smaller orbits and zero word amplitude. Infinity belongs to the forbidden size-six orbit. The calculation is over the number field itself, so admissible roots in arbitrary algebraic extensions are included.

Five candidates have stabilizer order3 and hence eight distinct actual sections. All their tests have no admissible parameter. The remaining candidate has stabilizer order6 and has three degree-four surviving gcds; it yields only four actual sections and cannot meet the eight-section target. Counting projective candidate lines instead of actual linearized sections would incorrectly retain it.

`pilot.json` records the six explicit polynomials, their stabilizer sizes, and all surviving gcds. The bounded run took1.08 seconds and72112 KiB under60 seconds/384 MiB. There is no modular-to-characteristic-zero inference.

This excludes the stated36-point octahedral construction at half agreement, not every eight-word construction or every nonequivariant word on those nodes. The follow-up below also settles the15-agreement variant.

## Follow-up: fifteen matches is also excluded

The lower-gap target15/36 was checked completely within the same sign-equivariant setup. Nonconstant candidates have at most6 matches in each of the three classes, and each count is a multiple of3. Thus15 matches requires either six special zeros and at least nine generic matches, or three special zeros and twelve generic matches.

`pilot15.py` treats the first case with pairwise gcds for the six already determined candidate sections. It again leaves only a section with stabilizer6, hence an orbit of four.

For the second case, choosing the matched special C3-orbit leaves a two-dimensional candidate space. `pilot15_pencil.py` constructs a basis from two independent special-zero products. Four matched generic cosets (two even, two odd) give three homogeneous linear equations in its two coefficients after choosing a positive identity match. The three2-by2 minors are univariate polynomials; their common gcd is computed for all4*18=72 choices.

Only six quartic parameter sets survive the forbidden-orbit guards. In every one, the coefficient kernel is the same constant candidate line, with stabilizer6. The code verifies that the coefficient matrix has no rank-zero point on the surviving gcd and that the displayed constant kernel vector annihilates all three equations modulo that gcd. Hence no exceptional algebraic parameter can escape the stabilizer check. All true orbit-eight candidates fail this target as well.

The final pencil run used about1.16 seconds and72368 KiB. Its explicit gcds, unique candidate sections, and stabilizers are in `pilot15_pencil.json`. Together these finite exact gates give an agreement ceiling of12 for actual orbit-eight sections in this prescribed sign-equivariant construction. This is a structural dead end for the requested half-agreement or15-agreement target, not a general obstruction to octahedral ideas with other domains or nonequivariant words.
