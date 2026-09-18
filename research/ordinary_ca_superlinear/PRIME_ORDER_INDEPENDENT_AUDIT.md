# Independent audit: prime-order characteristic-zero agreement bound

Status: PASS. This audits the theoretical deduction in `EXCEPTIONAL_PRIME_SUPPORT_IDEAL.md`; it does not replay the separate exceptional-prime enumerations.

Let r>5 be prime, W=(1+X^(2r))/2-X^r, and deg P<r. Suppose P agrees with W on a subset S of mu_(4r) of size M>=r+3. The polynomial F=2(W-P) is monic of degree 2r, so M<=2r. Put A=product_(z in S)(X-z) and write F=A Q, where Q is monic of degree k=2r-M<=r-3.

Although P initially may have coefficients in any characteristic-zero extension, descending monic division fixes every coefficient of Q from A and the coefficients of F in degrees 2r through M. All these degrees are greater than r, so these coefficients are integral (the leading coefficient is 1, the rest 0). Thus Q belongs to Z[zeta_(4r)][X], and P belongs to Z[zeta_(4r),1/2][X]. This proves descent and integrality without using a Vandermonde inverse at the ramified prime.

Reduce at any prime above r. The reduction of mu_r is 1, whereas the four elements of mu_4 remain distinct. Each reduction bucket has exactly r original roots; let n_c denote the selected multiplicities and t<=4 their number of occupied buckets. The identity F=AQ retains divisibility by product (X-c)^(n_c). Differentiating gives F'=-2P', which is divisible by product over occupied c of (X-c)^(n_c-1). This statement remains valid when n_c=r, even though the derivative of that particular factor is zero. If P' were nonzero, its degree at most r-2 would be at least M-t>=r-1. Hence P'=0. Because deg P<r, the reduced P is constant.

The reduced values W(c) at c in mu_4 are 0,2,i,-i, in some order. They are pairwise distinct in characteristic r>5: a collision between 2 and either sign of i would imply 4=-1 and therefore characteristic 5; the other possible collisions require characteristic 2. Consequently only one bucket can be occupied, giving M<=r, a contradiction.

Therefore the characteristic-zero maximum is at most r+2. The proof applies to arbitrary algebraic or transcendental coefficient extensions, because the initial monic division already forces cyclotomic coefficients. It does not give an upper bound in another split characteristic p, nor for composite r. No computation or numerical evidence is required.

## Prime-power and general source-reduction extension

Independent audit: PASS for `PRIME_POWER_FROBENIUS_SOURCE_REDUCTION.md`. Write r=ell^a s, gcd(ell,s)=1, ell odd. Monic division provides integrality whenever M>r. There are 4s reduction buckets with multiplicities at most ell^a. At stage j the Frobenius-root polynomial has root multiplicities at least ceil(n_c/ell^j); its derivative, if nonzero, has degree at most r/ell^j-2. The strict hypothesis M>r+(4s-2)ell^(a-1) makes the sum of derivative root multiplicities strictly exceed that bound at every j<a. Perfection permits each Frobenius root, without enlarging the finite residue field. At the last stage the degree is below s and every occupied bucket remains a matching coordinate, yielding at least ceil(M/ell^a) matches. The stated normalized-gap inequality follows directly from the ceiling inequality.

For s=1 and ell>5 this gives M<=r+2r/ell. The conclusion only excludes fixed positive gaps when the prime bases tend to infinity; it does not exclude fixed-prime powers or force general orders to be smooth. For general s the smaller source may exist and need not have a prime alphabet. These scope qualifications in the source note are necessary and correct.
