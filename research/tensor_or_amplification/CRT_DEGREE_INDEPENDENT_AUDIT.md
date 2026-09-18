# Independent CRT product and wrapped-rectangle audit

Status: PASS for `CORRELATED_CRT_DEGREE_BARRIER.md` and `WRAPPED_CRT_RECTANGLE_BARRIER.md`, with their explicit factorization and zero-chart hypotheses. Neither is a theorem about arbitrary realizations of abstract OR incidences.

## Unreduced correlated products

For a changed coordinate i, telescoping the two discrepancy products gives a term of exact degree sum_j h_j*N/n_j-(h_i-d_i)*N/n_i. Any two such degrees are different: equality would force n_i to divide h_i-d_i by coprimality, whereas this is an integer strictly between zero and n_i. Therefore the largest-degree term is unique and cannot cancel, independently of outer-code correlations or leading-moment constraints. Common H disappears in the pair difference. A pair with distinct factor vectors produces distinct polynomials by the same argument.

The agreement formula is exact for received word H: a product over a field vanishes if and only if a factor vanishes. The CRT map is bijective on the root domains. The degree lower bound sigma-epsilon and gap at most epsilon follow as stated. The caveat about reduction modulo X^N-1 is necessary; the supplied wrapped example indeed shows that exact unreduced pair degree is not preserved by reduction.

Precision on dilution: bounded candidate degrees alone do not guarantee small h_i/n_i. The received polynomial degrees h_i must also remain bounded or sublinear in n_i. Arbitrary padding values can increase these degrees. The inequalities themselves state h_i explicitly and remain correct.

## Wrapped coefficient lines

CRT injectivity is valid for every multiindex in the full box 0<=e_i<=h_i<n_i, including multiindices whose ordinary exponents exceed N. Reducing a residue equality modulo each n_i recovers every e_i. Thus no two coefficients from distinct box indices combine on reduction. This injectivity is a coefficient-location statement, not preservation of numerical degree ordering.

Under rho<sigma-epsilon and rho<1-2epsilon, fix i. The remaining weights sum to more than rho. Greedy accumulation gives rho<u<=rho+epsilon, so every exponent on the i-coordinate coefficient line has normalized value in (rho,1), since u+w_i<1. This is a genuinely unwrapped high-degree line. The common H need not itself have small degree: the assumption that both reduced H-products have degree at most D implies equality of their product coefficients at each high position after subtracting the two outputs.

For nonzero constant coefficients, the other-coordinate multiplier K_s is nonzero for both tuples. At the i-leading coefficient, the fixed nonzero leading coefficient forces K_s=K_t; all the other high coefficients then identify the entire i-th factor. Repeating for every i contradicts distinct factor vectors. This proves rho>=min(sigma-epsilon,1-2epsilon). It does not rely on the tuple family containing neighbors, on polynomial values being generic, or on a tensor cardinality assumption.

Combining a<=min(sigma,1) gives a-rho<=2epsilon. If root counts vary by label, this remains an upper bound for each tuple's agreement fraction and hence for any common threshold. The stronger negative asymptotic bound for total density tending to lambda>0 follows from sigma>=sum a_i and the standard complement-product limit.

## Zero constants

For a pair, let Z contain every coordinate whose constant coefficient vanishes in either tuple. Initializing the greedy set with Z excluding i ensures that every outside coordinate chosen at exponent zero has nonzero coefficient in both tuples. If that initial sum already exceeds rho, the resulting coefficient line still lies below 1 because its upper endpoint is at most tau+w_i<=tau+epsilon<1. Otherwise the final greedy sum is at most rho+epsilon and the previous bound applies. Thus the stated strict assumption tau+epsilon<1 is sufficient.

Its contrapositive is exactly the documented alternative: a pair violating the degree lower bound must have tau>=1-epsilon. Equality belongs to the unresolved chart; it must not be discarded. No conclusion here excludes a bank in which every exceptional pair has a large zero-constant union, nor justifies stripping candidate-dependent powers and retaining the same common H/degree cap without a separate argument.

## Scope

These are explicit CRT product realization barriers, including arbitrary correlated tuple selections and common subtraction. They do not exclude a different received word, candidate-dependent transformations that alter the factorization, or an unrelated univariate realization of the sparse correlated incidence target. The abstract low-density correlated window in `OR_TENSOR_INDEPENDENT_AUDIT.md` therefore remains logically open even though this specific product implementation is ruled out on the stated charts.
