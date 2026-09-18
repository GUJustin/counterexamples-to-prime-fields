# Complete exclusion on the canonical tangent conic

The projective conic

    ac=(123201/8000)b²

in the exact Q(eta) Paley net contains no geometrically integral rational
member. This excludes this particular one-parameter family, not the whole
net and not arbitrary degree-ten constructions.

## Modular parameterization and coverage

At the chosen prime29, parameterize the conic by
`[a:b:c]=[5u²:u:1]`, with projective endpoint[1:0:0]. A saved residual
coefficient `sum d_ij s^i t^j` on the a=1 chart is homogeneous of parameter
degree18. Its substitution is therefore exactly

    sum d_ij * 5^(18-i-j) * u^(36-i-2j).

All exponents are nonnegative. This formula includes u=0 (the F2 member)
and has the F0 residual as its top homogeneous parameter coefficient, up
to a nonzero scalar. No chart division is used in this substitution.

Let f(u,X) be the resulting residual polynomial. Its X degree is48 and
the degree48 coefficient has precisely the following irreducible factors:

```
u,
u^7+4,
u^21+25u^14+5u^7+7.
```

Outside these roots there is no residual discriminant root at base
infinity. Rationality then requires gcd_X(f,f_X) to have degree at least15.
Every subresultant polynomial is an integral polynomial combination of f
and f_X. Consequently every coefficient of any subresultant with X degree
below15 must vanish at such a parameter. This necessary test does not
depend on the CAS's indexing convention for principal subresultants.

The Sage job computed these necessary coefficient gcds. A separate
implementation, `verify_conic.py`, reconstructed f and used a flint-backed
fraction-free subresultant PRS, with every division checked exact. It
stopped at X degree14: already the gcd of that polynomial's15 coefficients
has roots only among the three leading-degree-drop factors above. Hence
there are no candidates outside that finite algebraic set. This replay
does not call Sage or reuse its subresultant output.

At roots of the three factors, the independent verifier works respectively
over F29, F(29^7), and F(29^21). It computes the homogeneous residual
gradient gcd using

    f_X, 48f-Xf_X,

and adds their common vanishing order at base infinity. The results are:

| Parameter factor degree | Residual X degree | Homogeneous gradient gcd degree |
|---:|---:|---:|
|1|46|4|
|7|47|0|
|21|47|0|
|projective endpoint|44|4|

All are below15. None has identically zero residual discriminant. The
factorization exhausts all algebraic parameter values on the projective
conic, not just rational parameters of F29.

Receipts: `conic.json`, `conic.independent.json`, and their resource reports.
The independent implementation passed in0.54seconds using under8MiB. Its
candidate residue-field arithmetic is also independent of Sage's fields.

## Characteristic-zero transfer

Use the DVR at the prime eta=7 above29, extending it to split the seven
base coordinates if desired. The exact net coefficients are integral
there and reduce to the recorded modular net; this was checked in
`exact_kernel.verified.json`. Kappa=123201/8000 is a unit with reduction5.
The projective conic parameterization thus has good reduction and extends
to a morphism from P1 over this DVR. The fixed factor T is monic with
integral coefficients, and exact division of the discriminant by T
preserves integrality. Its residual homogeneous form has degree48.

The condition that the two binary partial derivatives have a common
factor of degree at least15 is a closed rank condition on fixed-degree
binary forms (equivalently, a Sylvester-matrix rank condition). Include
the zero form in this closed condition. Its inverse image on parameter
P1 is therefore closed and proper over the DVR. The preceding complete
modular calculation shows its geometric special fiber is empty. If its
geometric generic fiber were nonempty, an algebraic point would extend
after a finite extension of DVRs by properness, giving a point in that
empty special fiber. Thus the generic fiber is empty too.

The universal binary-discriminant lemma makes this closed condition
necessary for every geometrically integral rational member, including
members on all leading-coefficient and infinity boundary strata. This
proves the stated characteristic-zero conic exclusion. The transfer uses
the entire projective parameter line and a closed condition; it would
not follow from an empty modular open chart alone.

## Structural scope

The conic's parameter discriminant factors into the seven old graph
polynomials and an absolutely irreducible weighted-degree47 quotient,
as certified in `../EXACT_CONIC_STRUCTURE.md`. Thus the factorization
does not expose a smaller pencil or a rational parameterization of its
members. No additional exact syzygy reducing the global two-parameter
rationality locus has been established. The existing mu7 quotient and
finite-locus reduction remain valid tools, but this one-dimensional
exclusion alone does not replace the global elimination problem.
