# Mixed Frobenius core: exact small-field replay

The adjacent `MIXED_LINEARIZED_SQUARE_CORE.md` proves that, on a two-dimensional F_p-plane in F_(p³), the word (x^p−s x)² has at most p²+2p−1 quadratic witnesses with more than four matches. The bound is attained for every p≥5 by the anisotropic-conic choice of s specified in that proof.

`check.py` enumerates all quadratic coefficient patterns for four specified words at p=3 and p=5. It loops over the leading and linear coefficients and counts the possible constant coefficients by evaluation histograms; omitted constants have zero matches. Thus each word's census covers all p^9 quadratics, rather than sampling a normalized family.

The fourth choice deliberately exercises the even nonsquare branch. At p=5 it gives thirty square witnesses and four even nonsquare witnesses, attaining 34=p²+2p−1. The other choices check zero, prime-field, and extension-field values of s. All eight censuses pass. The p=3 cases are checks of the upper bound, not claims that its sharpness construction applies below p=5.

This is a classification of a proposed core family. It supplies neither a new received-line counterexample nor a better.codes improvement, and does not bound the number of labels obtainable from a separate fresh-block construction.
