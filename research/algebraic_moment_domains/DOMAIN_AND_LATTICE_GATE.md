# Noninterval moment domains: exact reductions and the remaining lattice gate

Status: bounded strategic assessment, not a new asymptotic construction.

## Product boxes do not save the logarithm by size alone

Fix a number field of degree d and an integral basis. Take the m-by-...-by-m coefficient box, of size n=m^d. Multiplication in this fixed basis gives coordinates of z^j bounded by (C_K m)^j. Thus the elementary range count for moments 1,...,s has logarithm at most

    d s log(2n+1) + d s(s+1)/2 log(C_K m)
      = (s²/2) log n + O_K(s²+s log n).

The shorter archimedean radius is exactly canceled by the d coordinate constraints. This is a limitation of this counting proof, not a lower bound on the actual number of signatures. In particular, replacing an interval with a Gaussian square does not by itself improve the asymptotic exponent.

For increasing distinct integer nodes x_i, the Vandermonde Gram determinant is also no smaller than on consecutive integers: Cauchy--Binet expresses it as a sum of squared products of pairwise differences, and x_j-x_i >= j-i term by term. This compares raw Gram determinants only. A larger image-lattice covolume can matter, so this is not a universal exclusion of nonconsecutive nodes.

## Full cyclotomic domains are a genuine obstruction

Let D=mu_M, and fix the cardinality and first s power sums of a subset. A difference of two indicator vectors defines Q(T) in Z[T], degree < M. For every j=0,...,s, Q(zeta_M^j)=0. Therefore Q is divisible by every Phi_d with d|M and M/d<=s, as well as Phi_1.

The rational dimension of the difference space is consequently at most

    sum_{d|M, d<M/s} phi(d) <= (M/s) tau(M).

An affine d-dimensional rational subspace meets the Boolean cube in at most 2^d: projection onto d appropriately chosen coordinates is injective. Hence every moment fiber has logarithmic size at most (M/s) tau(M). For s comparable to sqrt(M), this is M^{1/2+o(1)}, insufficient for the desired Theta(M) exponent. This applies to the complete roots-of-unity domain, not arbitrary cyclotomic subsets or unions of dilates.

## The concrete remaining test: normalized Gaussian moment lattice

For the square D_m={a+ib:0<=a,b<m}, build the integer matrix A whose columns are

    (1, Re z, Im z, ..., Re z^s, Im z^s).

Let B be an exact lattice basis of A Z^{m²}, in its rational span, and C=B^{-1}A. Thus C is integral and retains exactly the moment fibers. For any unimodular row transformation U, put

    W_j = sum_x |(UC)_{j,x}|.

There are at most product_j(1+W_j) distinct signatures (each row ranges over an integer interval of that length). Restricting to subsets of size floor(rho m²), one obtains the rigorous certificate

    log_2 L >= log_2 binom(m²,floor(rho m²))
                 - sum_j log_2(1+W_j).

This isolates the only benefit not captured by the radius/dimension cancellation: the exact image lattice and a short integral coordinate basis. HNF/SNF plus exact row reduction makes this a bounded, reproducible experiment; a numerical covariance determinant alone is not a certificate. Suggested first gate: m=8,12,16 and s=m, record both the best certified width product and the exact lattice-normalized Gram determinant. A positive finite case is not an asymptotic result and does not automatically amplify.

An actual log-removal theorem from this route would require, for infinitely many m and some fixed c,delta>0, a certified count at s=floor(cm) with sum log_2(1+W_j) <= (H_2(rho)-delta)m². That gives log L >= delta m²-O(log m), gap eta=s/m²=Theta(1/m), and hence log L=Omega(eta^{-2}). This is the precise sufficient target; no such basis has been exhibited here.

Prime descent adds no further obstacle for this particular domain. Choose a prime p=1 mod 4 with p>2(m-1)² and p>s, and map i to a square root of -1 in F_p. A collision would force p to divide (a-a')²+(b-b')², a positive integer smaller than p. Thus all m² nodes remain distinct, and all exact moment identities descend. Arbitrarily large such primes are available. There is no analogous automatic injectivity claim for arbitrary algebraic-integer boxes without checking norms of differences.

## Relation to existing PTE work

Caley, *The Prouhet--Tarry--Escott problem for Gaussian integers*, arXiv:1011.1262, develops the Gaussian setting and ideal solutions. Coppersmith--Mossinghoff--Scheinerman--VanderKam, arXiv:2304.11254, supplies further ideal solutions over quadratic integer rings. These are valuable exact trades, but one pair or disjoint copies supplies only one bit per trade. They do not establish a positive-rate common moment fiber. The proposed lattice gate asks for precisely that stronger object and makes no novelty claim about Gaussian PTE.

Primary sources: https://arxiv.org/abs/1011.1262 and https://arxiv.org/abs/2304.11254.
