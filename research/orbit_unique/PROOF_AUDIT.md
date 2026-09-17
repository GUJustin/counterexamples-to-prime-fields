# Prime-order orbit proof audit (17 September 2026)

This is a mathematical and executable audit, not a formal proof or external review.

## Claims and dependencies

For prime d and p congruent to 1 modulo d, the core consists of the d-th-root orbits of 2,4,...,2^m; the padding is the d-th roots of unity; up to d-1 additional powers of two permit exact rational rates. The field-size bounds in `orbit.tex` are part of every assertion.

1. **Distinctness and zero-sum rigidity.** A subset sum lifts to an integer polynomial of degree at most d-1. Its coefficient norm is strictly below A=2^(m+1)(d+2^c). A nonzero resultant with Phi_d is an integer divisible by p if the reduction vanishes, but its absolute value is at most A^(d-1)<p. Hence the lifted polynomial is a rational multiple of Phi_d. Equality of its coefficients, together with unique binary expansion, forces whole core orbits and excludes extra coordinates. Differences of distinct formal points give domain distinctness by the same argument. Primality of d is essential here.
2. **Every nearby codeword is classified.** A degree-(K+1) monic received polynomial is at distance (n-K-1)/n. Improving its agreement by d after changing only d padding coordinates forces all padding and K+1 nonpadding matches. The locator has zero penultimate coefficient, so its roots sum to zero. The preceding lemma forces exactly D core orbits. This is not merely a list of selected witnesses.
3. **Labels are distinct and decodable.** The signed label lifts to a positive product of factors 2^(di)-1 below p. The normalized product is greater than 2/3. Its bit length recovers d times the sum of the indices, and the greedy membership threshold separates each next factor from every possible tail. The paired powers-of-two decoder proof applies to base 2^d. No integer factorization or unproved primitive-divisor assertion is needed.
4. **Exact rate.** Write rho=a/b in lowest terms and choose prime d not dividing a. The congruence at=-1 modulo d has solutions, n=bt, c=n modulo d, and D=(rho*n+1)/d are integers with K=rho*n. Choosing n a sufficiently small constant times sqrt(log p) satisfies both field bounds. The product bound is quadratic in n; the resultant bound is linear in n for fixed d.
5. **Numerical violation.** log2 binom(m,D)=n H2(rho)/d+O(log n), while the proposed exponent is c2*n H2(rho)/(d+1). Thus c2<1+1/d is required. In particular c2=1 works for arbitrarily large fixed prime d. This does not give a constant c2>1 uniform as d tends to infinity.
6. **Algorithmic qualification.** Given an order-d root, construction and decoding are deterministic in polynomial time in log p. Finding the root by uniform sampling is zero-error Las Vegas, with expected d/(d-1) trials; no unconditional deterministic root-finding claim is made.
7. **Scope.** Gap tends to zero. Nearby set is sparse, not all nonzero parameters. No global list-size upper bound, prescribed FFT-domain transfer, or better.codes improvement follows.

## Executable checks

- `verify_parameters.py`: exact field bounds, entropy-prescription comparisons at half rate, strict Elias, and Lucas-Lehmer primality certificates for M9689, M19937, M44497.
- `check_small.py`: exhaustive subset sums for d=3,5,7; exhaustive interpolation pencils for three small lines, including an extra-coordinate exact-half-rate case. It separately checks the primality of the fixture fields.
- `verify.py`: independent Lucas-Lehmer implementation, saved root orders, every domain coordinate, integer comparisons, 16 recovered supports per row, and two fully evaluated witness polynomials per row. Uses an independent rational-arithmetic greedy decoder.
- `roots.json`: fixed hexadecimal roots, generated once by `generate_roots.py`. Root generation is not part of routine verification and no claimed property depends on random success after the root order is checked.
- `instances.json`: compact reproducible domains and witness coefficients in powers of X^d. No enormous field enumeration is claimed.

Finite separation fractions are 3/4, 5/6, and 7/8 of eta. The corresponding ratios exceed 2^9, 2^2, and 1 (the final ratio is not claimed to exceed 2). Independent replay passed within 31 MiB and 30 seconds on the restored laptop.
