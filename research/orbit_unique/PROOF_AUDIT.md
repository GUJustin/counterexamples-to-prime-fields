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


## Random representatives at logarithmic length

Theorem `ou:random` keeps prime-order padding and samples independent core representatives and extras. For p>d^(d-1), no proper nonempty subset of the d-th roots sums to zero: the nonzero cyclotomic norm is too small to be divisible by p. Each forbidden nonpadding zero-sum subset is therefore a nonzero linear equation in the random representatives, with probability exactly 1/p before domain conditioning. There are at most 2^(n-d) such subsets. Distinct D-support products differ by a nonzero polynomial of degree at most dD, giving at most dD*binom(binom(m,D),2)/p collision probability. Domain collisions cost at most binom(n,2)/p. Valid-domain rejection changes the bound by the explicitly recorded denominator p-binom(n,2).

For n=alpha log2(p)+O(1), alpha<1 fixed, the bad probability is at most p^(alpha-1+o(1)). All-codeword classification is deterministic on the good event, but the sampler need not test that event. This theorem deliberately does not claim efficient witness recovery. Its nearby set is sparse.

`verify_random.py` uses exact integers/rationals and fresh Lucas-Lehmer checks for three finite half-rate certificates. `check_random_geometry.py` exhausts all subset sums and all interpolation pencils for nine fixed small random domains, with separately checked primality. Both passed. These tests check the sufficient criterion; the probabilistic estimate is proved by the union bound, not inferred from experiment.


## Root-of-two finite refinement

Proposition `ou:kummer` requires both alpha^d=2 and an order-d root omega in F_p. Its zero-sum lift lies in Q(2^(1/d),zeta_d), of degree d(d-1). The coprime degrees of the two subfields prove the degree statement. The integral order with basis u^s*zeta^j maps to F_p using the supplied roots; multiplication by a nonzero element mapping to zero has determinant (norm) divisible by p. Every conjugate of a subset sum or point difference is bounded by A=n*2^ceil((m+c+1)/d), so p>A^[d(d-1)] rules out a nonzero modular vanishing. Independence of the u powers, followed by binary uniqueness within each exponent residue class, forces complete core orbits and no extras.

Indices begin at TWO. Then products of (2^i-1) have normalized value strictly between 1/2 and 1, and their bit length is exactly the sum of the indices. The base-two greedy threshold is valid because the finite tail product is strictly larger than 1-2^-i. The no-wrap exponent is D(2m-D+3)/2, a factor approximately d smaller than the earlier orbit exponent. This is a conditional-root finite refinement; it does not assert alpha exists at every p congruent to 1 modulo d.

`generate_kummer.py` certified five Mersenne fields and saved roots, including d=13 over M23209 and d=19 over M44497. `verify_kummer.py` independently checked primality, roots, every domain coordinate, exact entropy inequalities, 80 decoded supports and 10 fully evaluated witnesses. Largest domain: n=7068, K=2830, d=19, m=371, D=149, c=0, ratio >1, separation 19/20 eta. Replay took 36 seconds and less than 89 MiB.

`check_kummer_small.py` independently decoded all 32,766 subsets up to core size 14, exhausted 1,024 / 4,096 / 524,288 subset sums, and classified all nearby codewords via 56 / 1,287 / 12,870 / 2,380 interpolation pencils. All passed, including extra-coordinate cases. Saved `kummer_instances.json` contains compact domain recipes and exact witness polynomial coefficients. No sampling-success assumption remains after the roots are certified.
