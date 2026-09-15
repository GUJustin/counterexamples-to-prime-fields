# Stronger finite polynomial-weight certificate

For the same integer subset class used in the paper,

- `n = 64`, `t = 34`, and first moment `q = 1071`;
- second moment `Y = sum binom(a, 2)`;
- center `22138` and exact support interval `[17969, 26129]`;

the monic degree-40 polynomial in `factored40_certificates.json` proves

**maximum conditional class size at least 5,285,900,426,578.**

This strengthens the previous bound 5,074,503,250,115 for the same
length-64, dimension-32 interval Reed–Solomon instance, an increase of
4.1659%. The degree-24 checkpoint 5,141,180,908,468 remains preserved in
`factored_certificates.json`. The stronger bound uses precisely
the polynomial-weight inequality already proved in the manuscript.
There is no additional protocol or fixed-domain claim.

The certificate is the monic polynomial with roots

```
-4169, -3591, -3590, -3214, -3213, -2844, -2843, -2475,
-2474, -2107, -2106, -1742, -1735, -1391, -1358, -1065,
-968, -765, -565, -476, 482, 571, 769, 969,
1065, 1352, 1385, 1721, 1729, 2081, 2082, 2436,
2437, 2787, 2788, 3135, 3136, 3484, 3485, 4184.
```

The JSON record also gives its expanded coefficients.
Its numerator is the exact conditional expectation sum,
and its denominator is the exact sum of its positive parts over the stated
integer interval. Taking the ceiling of their ratio gives the stated bound.
The numerical search score is informational only.

## Reproduction

From the repository root:

```sh
python3 research/finite_weights/compute_moments40.py
python3 research/finite_weights/build_factored40.py
python3 research/finite_weights/verify_chebyshev.py
python3 research/finite_weights/verify_certificates.py
```

These commands use Python's standard library.
Optional numerical discovery (`search_chebyshev.py --degrees 40 --stride 20`)
needs NumPy and SciPy. Discovery uses a coarse lattice to find approximate
roots, then `optimize_integer_roots.py` and `optimize_root_pairs.py` improve
the integer-root candidate using exact ratios on the full lattice.
These optimizers do not certify global optimality. All computations are pure
integer subset counting; no field or protocol implementation is called.

The exact verifier passed:

- all moments through degree 40 via the complementary 30-subset identity;
- all existing degree-20 moments against the previously checked records;
- 35 small parameter pairs, 1,969 enumerated subsets, and 483 conditional
  classes against direct enumeration;
- support endpoints via a separate minimum/maximum dynamic program;
- the integer numerator, denominator, and ceiling bound.

The Chebyshev basis improves numerical conditioning during discovery.
The final verification evaluates the factored and expanded polynomial at
all 8,161 support integers. Numerical optimization and rounding do not enter
the validity of the resulting certificate.
