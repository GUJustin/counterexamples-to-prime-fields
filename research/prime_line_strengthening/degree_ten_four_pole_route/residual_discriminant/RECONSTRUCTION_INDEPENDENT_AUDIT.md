# Independent exact reconstruction audit: PASS

`verify_reconstruction.py` verifies the downloaded residual polynomial independently of the generator's interpolation and discriminant calls.

* The input SHA-256, schema, field, chart, degree metadata and190 distinct triangular parameter points match.
* A dense190-by190 **monomial Vandermonde** matrix is inverted overF29 and applied to all49 X-coefficient evaluation vectors. Every reconstructed coefficient agrees with the saved polynomial. This is a different interpolation algorithm from falling-factorial Newton reconstruction.
* All1278 nonzero parameter monomials obey the derived mu7 character relation k-2a-4b=2 modulo7 for X^k s^a t^b. Parameter degrees are at most18.
* At five parameter points outside the reconstruction grid, the verifier forms F directly from the original kernel, computes the independent multivariate resultant Res_Y(F,F_Y), divides by the Y-leading coefficient with the degree-ten sign -1, then divides by the fixed degree294 polynomial. All five residuals agree coefficient by coefficient with the reconstructed D.

| New point (s,t) | Degree D | Degree gcd(D,D_X) |
|---|---:|---:|
| (19,1) |48|4|
| (20,2) |48|0|
| (21,3) |48|0|
| (22,4) |48|4|
| (28,28) |48|0|

The entire bounded replay took0.56seconds. The new resultant evaluations took approximately0.006seconds each using python-flint, so no rental was required for this audit. `verify_reconstruction.json` and the resource receipt preserve the results. A wrapper's sparse RSS sample should not be interpreted as a precise peak for a subsecond task.

## Generic geometric consequence

A degree48 specialization with derivative gcd1 proves that the universal residual polynomial is generically squarefree over the algebraic closure of F29. There is therefore no forced extra normalization index hidden in the residual48 degrees.

Intersect this nonempty open set with the nonempty ordinary-prescribed-point and simple-boundary open sets already checked in the genus analysis. On that intersection the discriminant has exactly the forced294 orders at the selected points and48 simple residual branch values. The degree-ten normalization map has total different48, hence

    2g-2 = -20+48,   g=15.

Equivalently the arithmetic genus162 loses precisely the147 prescribed delta units. The previous lower bound9 was conservative; the generic genus is exactly15 on this chart.

The same generic statement lifts to characteristic zero for the integral net supplied by the unit interpolation minor: a nonzero discriminant/resultant specialization modulo29 cannot be identically zero before reduction. This does not constrain the special subresultant locus where genus may drop. It supplies no rational member and no characteristic-zero emptiness certificate for that locus.
