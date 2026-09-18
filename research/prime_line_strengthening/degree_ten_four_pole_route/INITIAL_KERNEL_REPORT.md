# Degree-ten cover / four-pole uniform norm net

This is a positive-dimensional candidate family, not a construction yet. Work over characteristic zero for the intended construction; the initial computations below are exact modular linear algebra and finite-field factorizations.

A degree-ten cover of a seven-cubic bank has140 core coordinates. Clearing a proper denominator of degree4 gives candidate polynomials of degree at most34, hence dimension35 and exact quarter rate. The target is70 agreements. The uniform support pattern has six matched preimages above each triple base node and four above each quadruple node.

Assuming the norm map is birational, its necessary relation is

    H(X,Y)=sum_{j=0}^{10} A_j(X)Y^(10-j), deg A_j<=3j+4.

This has220 coefficients. A multiplicity-six plane point imposes21 Hasse jet equations and a multiplicity-four point imposes10. Thus the fourteen fixed word points give217 equations. The closure on F3 has class10C0+34F, arithmetic genus162. The prescribed multiplicities consume at least147 delta units, leaving at most15. Producing rational normalization therefore remains a substantial geometric condition, beyond consistency of the linear equations.

## Verified linear result

Both the Paley and orbit2 matrices have full row rank217, kernel dimension3, and injective leading-Y^10 projection. Exact modular certificates:

| bank | prime | 217x217 minor | leading 3x3 minor | leading coefficient columns |
|---|---:|---:|---:|---|
| Paley |29|19|15|0,2,4|
| orbit2 |83|3|50|0,1,2|

Every input node/word is the reduction of the previously verified number-field bank and all input denominators are units. Normalize the three kernel vectors by their free columns. Cramer's rule lifts them to integral characteristic-zero vectors at the chosen prime. The unit217minor proves exact kernel dimension3; the unit leading minor proves that every nonzero characteristic-zero vector in this net has degree exactly10 in Y. This is a nonvanishing-minor conclusion, not a nonlinear modular lifting claim.

`gate.py` builds the full Hasse matrices using python-flint for row reduction. `verify.py` independently rebuilds them from the original bank arrays and uses plain-Python modular elimination on the selected square minor. It checks every kernel vector and the leading projection. Both banks PASS. The runs took0.55 and0.54seconds respectively, under6MiB.

## Modular factor observations (strictly scoped)

`factors.py/json` uses exact FLINT factorization over the displayed prime fields.

* Both three-dimensional nets have common polynomial gcd1 in their reductions.
* All three Paley basis members are irreducible over F29; their bidegrees (degX,degY) are (31,10),(31,10),(33,10).
* The first two orbit2 basis members each factor as Y times a cubic graph times a degree-eight-in-Y factor. The third is irreducible over F83, of bidegree(34,10). Thus these individual reducible members do not form a common fixed component of the modular net.
* The Paley leading-Y^10 coefficients are25,27X^2,20X^4. Each basis vector is a mu7 eigenvector under (X,Y)->(zeta X,zeta^5Y), with character exponents1,3,5 respectively.

These factor statements are not claims of absolute irreducibility, characteristic-zero factorization, or geometric genus. A factor can behave differently on reduction; only the unit-minor linear conclusions above are asserted in characteristic zero. No cover, pole divisor, or actual candidate bank has yet been constructed.

## Next bounded question

Determine the normalization genus and boundary/forced singularities of this explicit projective plane of norm curves. The required fourteen singularities may carry additional automatic delta, or special parameter members may acquire the remaining15 units. Irreducible genus-zero members with the correct projection, proper pole divisor and distinct selected fibers would give a construction; an arbitrary nonzero kernel member does not suffice. The parent assigned independent genus/boundary analysis to the upper-bound agent, using the saved basis rather than rerunning the linear gate.
