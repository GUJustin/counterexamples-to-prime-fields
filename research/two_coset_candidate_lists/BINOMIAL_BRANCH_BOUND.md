# A uniform bound for subsets of higher binomial-section orbits

September17,2026. Locally derived and proof-audited research result.
No independent human/agent review or novelty claim. Restricted to this
explicit candidate family; not a general prime-field decoding bound.

## Statement

Let r>=3, k>=2, p=2rk+1 prime, 0<=j<r, and

    G(X)=sum_{i=0}^k binom(rk+j,ri+j) X^i in F_p[X].

Let S be ANY L-element subset of H=mu_k. Its candidates
P_h(X)=G(hX)-X^k are distinct and have degree<k. Let c>=1 and let
D be ANY n-point domain in F_p with n<=c*k, with any received word.
If every P_h has at least k+1 agreements, then

    L <= 2^20*r^3*4^r + 24*c*(r*2^r+1).                 (1)

Thus for each fixed r>=3 and fixed c, no growing subset of this orbit
gives even one agreement beyond capacity. The bound includes arbitrary
non-subgroup subsets and non-invariant domains/words. It does not apply
to r2,j1 (the Dickson case). For growing r it is exponential in r:
it does not exclude the main target when r is comparable to log k or
larger. No claim is made about other hypergeometric families.

More informatively, put

    B=r*2^r+1, Lambda=2^(r+1)*(sqrt(p)+3),
    b_r=binom(r,floor(r/2))/2^r,
    a_(r,j)=2*b_r + 1_{r even,j=1}*2^(1-r/2),

except use a_(4,1)=3/4. Then the minimum agreement of the L candidates
is at most

    a_(r,j)*k + 4*Lambda
      + (2*r+4)*Lambda*sqrt(k/L) + c*k*B/L + 1.        (2)

For all r>=3, a_(r,j)<=7/8. The exact constants are deliberately loose.

## 1. The root filter and its branches

Choose omega of order r. With e=(p-1)/2+j,

    G(t^r)=1/(r*t^j) sum_a omega^(-aj)*(1+omega^a*t)^e.

For one rth-power class of nonzero x choose tau with
tau^p=omega^b*tau, and write t=tau*T for T in F_p^*. All x in that
class are obtained, r times each. Set L_a=1+omega^a*t and introduce
u_a with u_a^2=L_a*L_(a+b). The actual finite-field values
u_a=L_a^((p+1)/2) satisfy these equations. The possible functions are

    F_sigma(T)=1/(r*t^j) sum_a omega^(-aj)*L_a^(j-1)*sigma_a*u_a.

Work for the moment over the rational function field over an algebraic
closure of F_p. Distinct nontrivial square classes give linearly
independent radicals over that field: they are distinct characters in
a multiquadratic extension. Here their classes are encoded by the
unordered pairs {a,a+b} of distinct linear factors.

If b is neither0 nor r/2, those pairs are distinct. Consequently none
of the functions F_sigma is constant: subtracting a constant still
leaves nonzero coefficients in distinct nontrivial character spaces.

If b=r/2, pairs repeat twice. Their coefficients are proportional to
(1+u)^(j-1) and (1-u)^(j-1), with fixed nonzero sign factors. For
2<=j<r these polynomials cannot be proportional, since their constant
and linear coefficients disagree and 0<j-1<p. For j0, clearing the
two denominators gives the same conclusion in characteristic not2.
For j1 cancellation is possible, and all pairs cancel precisely when
the chosen radicals in every opposite pair agree. The only constant
value is0. With tau^2=d a nonsquare in F_p, the actual pair equality
is equivalent to

    chi(1-omega^(2a)*d*T^2)=1  for a=0,...,r/2-1.       (3)

Indeed u_(a+r/2)=u_a^p=chi(L_a*L_(a+r/2))*u_a.
The quadratic polynomials in (3) are pairwise coprime, irreducible,
and have distinct roots in the algebraic closure.

If b0, u_a can be chosen equal to L_a. The signs are the actual
quadratic characters sigma_a=chi(1+omega^a*T), away from their zeros.
The branch is constant exactly when its coefficients of T^ell for
0<=ell<j vanish. Its constant value is (1/r)sum_a sigma_a. At most
binom(r,floor(r/2)) sign patterns give any one value, since p>2r.
For r4,j1 the sole lower coefficient condition says
sigma0=sigma2 and sigma1=sigma3. The largest value multiplicity is2
patterns out of16, yielding b_(4,1)=1/8 instead of the general6/16.

## 2. Every other fiber is bounded

Fix a class and a value v. Multiply F_sigma-v over all NONCONSTANT
branches. Excluding constant branches is essential when v equals a
constant value. This multiset is stable under the Galois group of the
radical extension, so its product belongs to the rational function field.
It is nonzero because none of its factors vanishes identically.

For j>=1 clear each factor's common denominator r*t^j. The resulting
factors are integral over the polynomial ring and have pole order at
infinity at most j. For j0, multiply each factor by r*prod_a L_a;
its pole order at infinity is at most r. The Galois-invariant product
is therefore a nonzero polynomial of degree at most r*2^r. Integrality
uses the fact that the polynomial ring is integrally closed.

Every occurrence of G(x)=v not explained by a constant branch gives
a root of this polynomial in T, except possibly x=(-1)^r where some
L_a vanishes. Choosing one T per such x is injective. Thus the number
of residual x-values in an rth-power class, and hence in any mu_k
coset, is at most B=r*2^r+1. This deliberately avoids needing a
factor-r improvement in the norm bound. The point x0 is handled
separately in (2).

## 3. Means and Fourier coefficients of constant-branch masks

Only two mu_k cosets occur in the rth-power class b0. On each, let
f_v be the indicator of a constant branch with value v, excluding base
points. There are at most r+1 such values. Its density has the form

    |sum f_v - k*pi_v| <= Lambda,
    pi_v <= b_r  (or1/8 for r4,j1).                    (4)

For every nontrivial multiplicative character psi of mu_k,

    |sum_{x in C} f_v(x)*psi(x/x_C)| <= Lambda.        (5)

Here x_C is any coset representative. To verify (4), parametrize
x=T^r and specify chi(T), which selects one of the two cosets.
Each sign pattern is counted by expanding r+1 quadratic-character
indicators. All nonempty products are squarefree with at most r+1
roots. The error for one pattern is at most r*sqrt(p)+r+1 before
division by r. There are at most2^r patterns; the trivial term after
division is k/2^r up to less than1. The displayed Lambda dominates
the resulting error and all excluded zeros.

For (5), extend psi to a multiplicative character Psi on F_p^*.
The weight in the T-sum is Psi^r(T), up to a unit scalar. It is
neither principal nor quadratic, because psi is nontrivial on mu_k.
After optionally multiplying by chi(T), it remains nonprincipal.
The character product in every expanded sum has a nontrivial exponent
at T0 and at most r+1 distinct roots, so it is not a power for the
primitive character used to express it. Its sum is at most
(r+1)*sqrt(p); excluding zeros and dividing by r gives (5), even
after summing over all2^r patterns.

For b=r/2,j1 there are two more mu_k cosets and only the value0.
Expand the r/2 indicators (3), with the additional sign of chi(T)
that selects a coset. The same arguments give (4),(5), now with
pi=2^(-r/2). Distinct quadratic factors and T guarantee the same
non-power condition. Lambda safely bounds these smaller errors too.

The analytic input is the standard multiplicative-character Weil bound
in the distinct-root formulation: Sárközy–Sárközy, Discrete Mathematics
305(2005), Lemma2, https://web.cs.wpi.edu/~gsarkozy/Cikkek/23.pdf .
This primary formulation was checked September17. Character products
above are expressed using one primitive character; their nontrivial
root exponents establish its required non-power hypothesis.

## 4. Arbitrary candidate subsets and arbitrary domains

For S subset mu_k, |S|=L, convolution with a mask gives the number
C_v(x) of selected candidates taking that constant-branch value at x.
By Parseval and (5), on an entire mu_k coset,

    sum_x |C_v(x)-L*(sum f_v)/k|^2 <= Lambda^2*L.

Thus on any subset of its coordinates the sum of absolute deviations
is at most Lambda*sqrt(k*L). For the two b0 cosets, sum this over
at most r+1 possible values; for the two possible b=r/2 cosets there
is just one. Their total mean contribution, divided by L, is at most
a_(r,j)*k+4*Lambda, and the deviation contribution is at most
(2r+4)*Lambda*sqrt(k/L).

At every coordinate, at most B candidates from the FULL orbit can take
any particular residual value, by Section2. All n<=c*k coordinates
therefore contribute at most c*k*B/L to the average agreement across S.
The possible coordinate0 contributes at most1. Minimum agreement is
at most average agreement, proving (2). The argument allows a different
received symbol at every coordinate, including outside the special cosets.

## 5. Extracting the uniform list bound

The central-binomial probabilities decrease separately along even and
odd r. For odd r>=3, 2*b_r<=3/4. For even r>=6,
2*b_r+2^(1-r/2)<=5/8+1/4=7/8. The refined r4,j1 coefficient is3/4;
all other r4 sections also have coefficient at most3/4.

Put epsilon=1/8 and C=2^(r+3)*sqrt(r). Since p=2rk+1 and r>=3,
Lambda<=C*sqrt(k). If k>=(192*C)^2 and

    L>=576*(2*r+4)^2*C^2,  L>=24*c*B,

then respectively the terms4*Lambda+1, (2*r+4)*Lambda*sqrt(k/L),
and c*k*B/L are each at most k/24. Formula(2) gives minimum
agreement at most k. Otherwise either k<(192*C)^2 and L<=k, or
one of the two displayed L bounds fails. Using C^2=64*r*4^r and
2r+4<=4r gives the deliberately rounded bound(1).

## Checks and limits

check_branches.py verifies26 parameter/section fixtures, including every
section for r3,4,6 over F12289. It independently checks sample coefficients
against integer binomial coefficients, the root-filter identity at every
nonzero prime-field t, constant-branch values and r-to-one masks, and
all residual fibers. The largest observed residual fiber is small, but
only the proved bound B is asserted universally. Fourier values in the
report are floating-point diagnostics, NOT exact certificates or the
basis of the theorem. The analytic proof establishes their bound.

This closes a particular extension of the Dickson mechanism when r is
fixed. It gives no upper bound for arbitrary RS lists, no new growing
fixed-gap list, and no protocol-security claim. The original research
target remains open.
