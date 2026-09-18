# Independent audit: higher-character collision budget

Verdict: PASS under the stated fixed-order noncollapse guard and the underlying elliptic-bank hypotheses. Read the full note and checked the operator claim explicitly, including trivial Mellin characters. No manuscript edits or scans.

## Sum distribution and reduction guard

For unit complex numbers, a nonzero midpoint determines its unordered chord endpoints uniquely. The only extra unordered collisions are the diameters at zero. This gives exactly the stated odd/even multiplicities, kappa_h and beta_h, including h=2. The formulas count ordered pairs consistently in both the collision and largest-bucket quantities.

Each nonzero difference of two root-of-unity sums is an algebraic integer with all conjugates of modulus at most four. Its nonzero rational norm has absolute value at most 4^phi(h). Excluding primes dividing these norms prevents every unintended identification; excluding h preserves primitive order. Thus p>4^phi(h), together with p!=ell and the elliptic-bank assumptions, is a sufficient finite guard. This uses the bound on each factor, not a false bound on their entire product. The weaker exact exceptional-prime exclusion is also valid when the original elliptic model remains defined and nonsingular.

## Four-shift uniformity

Expand a specified character-value tuple into h^4 Fourier terms. Every nonconstant term has a nonzero exponent modulo h at one of four distinct linear factors. Therefore its polynomial is not a constant times an hth power, including when h is composite. The multiplicative Weil bound has constant controlled by four distinct roots, not by the degree obtained by writing exponents as integers. Exceptional roots cost a bounded amount. Summing the finitely many equal-sum tuples gives kappa_h M+O_h(sqrt(M)) equalities before the sign quotient. Passing to nonzero ±pole representatives divides their number by two, and forced double-zero multiplicity multiplies it by two. The note's pair-degree coefficient 1−kappa_h is correct.

## Mellin operator: no hidden large eigenvalue

For a nonconstant Fourier term (i,j), the matrix on U,S in F_M* is

 chi^(i+j)(S) K(U/S),   K(t)=chi^i(t−1)chi^j(t+1).

The first factor is a unitary diagonal column multiplier. Multiplicative convolution is diagonalized by the unitary Fourier transform of F_M*, with eigenvalues the UNNORMALIZED sums sum_t K(t)psi(t). No additional factor sqrt(M−1) is missing.

To bound every eigenvalue, express chi and any Mellin character psi as powers of a primitive multiplicative character rho of order M−1. The product becomes rho(t^e0(t−1)^e1(t+1)^e2), with exponents chosen modulo M−1. At least one of e1,e2 is nonzero modulo M−1, because (i,j)!=(0,0) modulo h. Hence this polynomial is not a constant times an (M−1)st power, irrespective of e0. This includes the trivial Mellin character and any cancellation of the total exponent at infinity. The distinct-root Weil estimate gives at most 2sqrt(M), up to a bounded correction for excluded zero arguments. There is therefore no degenerate Mellin mode of size M.

The cited primary mathematical statement was checked via the source's indexed text: [Theorem 3.7, explicit Weil bound](https://people.cs.uchicago.edu/~laci/papers/span1.pdf). It bounds a non-perfect-power character sum in terms of the number of distinct roots, uniformly in character order. Direct PDF opening returned a temporary 502, but the source's indexed theorem and surrounding application were available. No reliance on a numerical or secondary summary is needed for the exponent check above.

Finite Fourier expansion of each sum bucket therefore gives a centered operator of norm O_h(sqrt(M)). Restricting rows/columns to sign representatives cannot increase operator norm beyond fixed normalizations. Diagonal exceptions lie on U=±S; on representatives they are diagonal, with bounded entries, so their norm is O_h(1). For each of the finitely many bucket values, Cauchy gives O_h(sqrt(qML)); bounding the pointwise maximum by the sum of absolute centered errors preserves this order. The additional O_h(q) is conservative and covers exceptional buckets. This also handles small L; asymptotic use needs only L→infinity.

After dividing total incidences by LM, the spectral error is O_h(L^(−1/2)+L^(−1)); the pair-budget error contributes O_h(M^(−1/2)) away from a zero limiting radicand, which does not occur here. Thus even arbitrarily slow growing subbanks are covered for fixed h.

## Optimization and interpretation

The limiting objective beta_h z+sqrt((4−z)(1−kappa_h)) is concave on [0,1/2]. Its derivative is beta_h−sqrt(1−kappa_h)/(2sqrt(4−z)). For h=2 and 4 it stays positive and the maximum is z=1/2; for h=3 and 5 it is already negative at zero and the maximum is zero. These give the four exact constants in the table. Orders 2,3,4 lie strictly below 4(3+sqrt(133))/31; order 5 lies above it.

The convolution identity with the inverse character is also correct: at zero its value is M−1, while at every nonzero argument it is the Jacobi sum J(chi,chi^−1)=−chi(−1)=−1. Thus c_chi*c_chi^-1=M delta0−1, and the augmentation-zero inverse exists whenever ambient characteristic differs from ell. It ensures bank distinctness but supplies no offpole agreement factors.

Conclusion: five is the first order NOT EXCLUDED BY THIS PARTICULAR BUDGET, not the first order known to construct the desired word. Fixed h, preservation of root-of-unity additive relations, and the original unrenormalized bank remain essential scope restrictions. No correction to the proof is needed.
