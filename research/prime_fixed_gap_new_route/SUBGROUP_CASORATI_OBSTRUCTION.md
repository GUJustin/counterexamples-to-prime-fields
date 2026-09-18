# A fixed-index obstruction from contiguous binomial determinants

**Theorem.** Let h>=1 and q>=h², and suppose p=4(4h+3)q+1 is prime. Put n=4q and k=(p−1)/4. For every nonzero t in F_p, the reduction modulo X^n−1 of

    P_t(X)=sum_(j=0)^(k−1) binom(2k+1,2j+1)t^(k−j)X^j

has degree at least q. In particular literal subgroup restriction of the native Dickson bank cannot produce a quarter-rate candidate in this range. The assertion is stronger than needed for the bank because t need not be a square.

This is an analytic obstruction, not a survey or a claim about arbitrary new polynomial sources. It uses neither differentiation of a reduced polynomial nor an ODE modulo X^n−1.

## 1. A rational Casorati determinant

Work first over a field of characteristic zero or p>2h, and take a nonzero scalar n. Set

    R(x)=(x+1/4)(x+3/4)/[(x+1)(x+3/2)],
    f_i(x)=product_(a=0)^(i−1) R(x+a),  0<=i<h,
    D_h(x)=product_(a=0)^(h−2) (x+a+1)(x+a+3/2).

Empty products are one. The determinant

    C_h(x)=det_(0<=i,j<h) f_i(x+jn)

has a common denominator product_j D_h(x+jn), monic of degree2h(h−1). Its numerator is a nonzero polynomial of degree exactly h(h−1), with leading coefficient

    n^[h(h−1)/2] product_(i=0)^(h−1) [(3/2)_i i!],        (1)

where (a)_i is the rising factorial. No assertion of a reduced denominator is needed.

Here is a complete infinity calculation proving the degree and nonvanishing. Write alpha=−3/2, the coefficient of x^−1 in R(x), and

    f_i(x)=sum_(a>=0) P_a(i)x^−a.

For 0<=a<h, P_a(i) is a polynomial in i of degree at most a, whose degree-a coefficient is binom(alpha,a). To verify this without a formal logarithm, use f_(i+1)=f_i R(x+i). The coefficient of x^−b in R(x+i) has degree at most b−1 in i and leading coefficient alpha*(−1)^(b−1). Induction shows that the finite difference of P_a has degree at most a−1, with zero initial value for a>0. If ell_a is its leading coefficient, then

    a ell_a=alpha sum_(c=0)^(a−1) (−1)^(a−1−c) ell_c,
    ell_0=1.

The binomial identity gives the unique solution ell_a=binom(alpha,a). Only denominators1,...,h−1 are needed.

Apply the unit lower-triangular row transformation

    g_i(x)=sum_(a=0)^i (−1)^(i−a) binom(i,a) f_a(x).

Finite differences annihilate P_a when a<i, so

    g_i(x)=c_i x^−i+O(x^−i−1),
    c_i=(−1)^i(3/2)_i.

Next replace column ell by its ell-th forward difference at step n, another triangular transformation of determinant one. For a Laurent term x^−i,

    Delta_n^ell x^−i
       =(−1)^ell(i)_ell n^ell x^−i−ell+O(x^−i−ell−1).

Consequently, after removing x^−i from row i and x^−ell from column ell, the leading determinant is

    det[c_i (−1)^ell(i)_ell n^ell].

The polynomials (i)_ell are monic of degree ell, so their evaluation determinant at i=0,...,h−1 is the Vandermonde product product_i i!. The two signs, from product c_i and the column factors, cancel. This proves

    C_h(x) = (coefficient in (1))*x^−h(h−1)
              +O(x^−h(h−1)−1).

All factors in (1) are nonzero under p>2h, and multiplying by the stated monic common denominator proves the exact numerator degree. Higher Laurent terms cannot change this leading determinant: each gains at least one inverse power after the same finite differences.

## 2. Apply the determinant to the subgroup coefficients

Put c_j=binom(2k+1,2j+1). For 0<=j<k,

    c_(j+1)/c_j
      =[(2k−2j)(2k−2j−1)]/[(2j+2)(2j+3)]
      =R(j) in F_p,

because 2k+1=(p+1)/2 is congruent to1/2. Every relevant c_j is nonzero: its binomial indices are between0 and2k+1<p.

For r=3q,...,4q−1, exactly h terms contribute to the reduced coefficient of X^r. After removing the nonzero factor t^(k−r), its vanishing says

    sum_(j=0)^(h−1) c_(r+jn) T^j=0,  T=t^−n.

A reduction of degree<q would make all these q consecutive equations hold. For each starting r=3q,...,4q−h, take h consecutive equations. The matrix of coefficients is

    [c_(r+i+jn)]_(0<=i,j<h)
      =[f_i(r+jn)] diag(c_r,c_(r+n),...,c_(r+(h−1)n)).

It annihilates the nonzero vector (1,T,...,T^(h−1)), so C_h(r)=0. All denominators are nonzero: every integer j occurring in the adjacent coefficient ratios is nonnegative and below k, and hence neither j+1 nor2j+3 vanishes modulo p. The window starting points are distinct modulo p, and n is nonzero modulo p.

There are q−h+1 such roots of the numerator polynomial. Its degree is h(h−1), whereas

    q−h+1 >= h²−h+1 > h(h−1).

This contradicts the determinant lemma and proves the theorem.

## 3. Index eleven is completely excluded

For h2 (index11), the theorem handles q>=4. The remaining possibilities q1 andq3 give composite p45 andp133. For q2, p89,n8, the two high-residue linear equations have a common root only if R(6+n)=R(6). Clearing denominators gives

    24n[16j²+(16n+28)j+14n+11]=0 at j6.

The bracket is1635, congruent to33 modulo89, so it is nonzero. Thus index11 is excluded for every admissible prime, not just the previously surveyed ones. The h1 case recovers the index-seven obstruction. Index three is separately excluded because no polynomial reduction occurs there.

## Remaining range and validation

For an index4h+3, any surviving candidate must have q<h². Thus no fixed-index family can work as subgroup size tends to infinity. Equivalently, a remaining index must exceed2*sqrt(n)+3. This does not exclude growing-index families, Reynolds projections, common-factor shortening, or other constructions.

The independent tiny check check_subgroup_casorati.py expands the cleared polynomial determinants for h2,3,4 over F_1000003 with n7, using permutation expansion. It verifies degrees2,6,12 and the exact leading coefficient (1). Its watchdog report is0.56seconds/3.2MiB. It is a consistency check of the analytic proof, not a larger subgroup or parameter scan.
