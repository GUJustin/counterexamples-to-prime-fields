# Large fibers do not force an invariant nearest Dickson polynomial

September 19, 2026. A consequence of existing local proofs, with no new
scan, manuscript edit, or claimed prime-field construction.

**Conclusion.** The identity W_k(X)=W_r(X^d), k=dr, does not imply that
a true nearest degree-below-k polynomial can be chosen invariant under
mu_d. This fails for the exact archived word, and fails along sequences
with r→infinity, d→infinity, and r/p→0 that also satisfy the rough CRT
conditions in [PROOF.md](PROOF.md). Here r denotes the **prescribed quotient
order**, not the unknown orbit size of an actual nearest polynomial.
The result excludes an automatic symmetrization argument, not every
possible source of short true-nearest orbits.

## 1. The exact condition that would be needed

Let p≡1 modulo 4, k=(p−1)/4, choose d dividing k, and set r=k/d. Write

    W_k(X)=(1+X^(2k))/2−X^k,
    M_k(p)=max_(deg P<k) agr_(F_p*) (P,W_k),
    M_r(p)=max_(deg V<r) agr_(mu_(4r)) (V,W_r).

Since p does not divide d, a polynomial of degree below k is mu_d-invariant
exactly when it has the form P(X)=V(X^d), deg V<r. The map X↦X^d
from F_p* onto mu_(4r) has d elements in every fiber, and
W_k(X)=W_r(X^d). Therefore

    max_(mu_d-invariant P, deg P<k) agr(P,W_k)=d M_r(p).       (1)

In particular an invariant true nearest polynomial exists **if and only if**

    M_k(p)=d M_r(p).                                         (2)

Composition proves only M_k(p)≥d M_r(p). It does not prove the reverse
inequality needed in (2). In the orbit language of PROOF.md, a candidate
with actual mu_k-orbit size rho is mu_d-invariant exactly when rho divides r.
The proof there selects an actual nearest polynomial first and then
uses its actual stabilizer; reversing those choices requires (2).

The Reynolds projection is well defined:

    R_d P(X)=(1/d) sum_(zeta∈mu_d) P(zeta X)
            =sum_(d divides j) c_j X^j.

It preserves agreement on every fiber where P already matches at all
d points. On a partially matched fiber it averages residual values;
the number of zero residuals gives no corresponding zero-average claim.
The counterfamily below forces this projection to lose agreement for
**every** true nearest polynomial, regardless of the choice of nearest.

## 2. An explicit large-characteristic quotient bound

For any prime r>5 define the integer

    B(r)=(binom(3r−1,r)+2)^(2(r−1)).

For every prime p≡1 modulo 4r with p>B(r),

    M_r(p)≤r+2.                                             (3)

This follows from the already proved
[prime-order characteristic-zero obstruction](../cyclotomic_dickson_word/PRIME_ORDER_COSET_WORD_OBSTRUCTION.md)
and [support-ideal criterion and norm bound](EXCEPTIONAL_PRIME_SUPPORT_IDEAL.md).
Here are the steps to make the quantifiers and cutoff explicit.

If a finite-field polynomial has at least r+3 agreements, select exactly
M=r+3 of them and lift the selected primitive-root exponents to a subset
S of mu_(4r) in Q(zeta_(4r)). Let h_j(S) be the complete homogeneous
symmetric coefficients, and put a=2r−M=r−3. The denominator-free
support criterion says that the selected finite-field support is possible
only if, at the same prime ideal over p,

    h_(a+1)(S)=...=h_(r−1)(S)=0,   h_r(S)−2=0.              (4)

In characteristic zero these equations cannot all vanish: for prime
r>5, every degree-below-r polynomial has at most r+2 agreements with
W_r. Hence one generator alpha in (4) is a nonzero cyclotomic integer.
For every complex embedding sigma,

    |sigma(alpha)|≤binom(3r−1,r)+2.

Indeed |h_j(S)|≤binom(M+j−1,j), with M≤2r and j≤r. The cyclotomic
field has degree phi(4r)=2(r−1), so

    0<|Norm(alpha)|≤B(r).

If (4) held after reduction, p would divide this nonzero integer norm,
forcing p≤B(r). This proves (3). Because p≡1 modulo 4r, the domain
splits in F_p and no root-collision qualification is hidden in the argument.
The proof applies simultaneously to all supports; no enumeration of them
is needed.

## 3. An asymptotic counterfamily, including the original CRT conditions

Fix R≥40 and choose any prime r>R. Let B_R be the product of the odd
primes at most R, as in PROOF.md. The congruences

    p≡9 mod 16,   p≡1 mod r,   p≡−1 mod B_R               (5)

are compatible and define a reduced residue class modulo 16rB_R.
Dirichlet supplies arbitrarily large primes p in this class. Choose one
with p>B(r), and let k=(p−1)/4=dr.

The full Dickson lower bound in the archived construction gives

    M_k(p)≥3k/2.

But (1) and (3) give, for every mu_d-invariant candidate,

    agr(P,W_k)≤d(r+2)<3dr/2=3k/2,                         (6)

because r>5. Consequently **no true nearest polynomial is mu_d-invariant**.
The gap between the known attainable agreement and the invariant maximum
is at least d(r−4)/2>0. Since (1) bounds every invariant polynomial,
it also bounds the Reynolds projection of every true nearest polynomial.

The arithmetic assumptions in the original rough-prime argument are all
retained: v_2(k)=1, k≡1 modulo 3, and no odd prime at most R divides k.
For any sequence R→infinity, choose r>R and then p in (5) as large as
desired. One may enforce p/r→infinity and d→infinity, as well as p>B(r).
Thus the proposed desired scale separation for the **chosen quotient**
can coexist with a strict failure of the nearestness-preserving lift.

This does not show that all true-nearest orbit sizes are comparable to p.
There might be another nearest polynomial with another large stabilizer.
What (6) excludes is the prescribed stabilizer mu_d, or equivalently any
actual orbit size dividing the chosen prime r. Nor does (3) exclude
exceptional split primes p≤B(r) with p/r large. Those remain part of the
simultaneous support-ideal problem already isolated in the archive.

## 4. Small corroboration already in the repository

The complete [p=41 nearest census](../dickson_nearest_threshold/README.md)
has k=10, true maximum 15, and 210 nearest polynomials, all with full
mu_10-orbit size 10. Thus no nontrivial prescribed fiber subgroup works
even in that exact finite example.

The failure at d=2, r=5 does not require the full nearest census:
the existing all-split-prime r=5 certificate proves M_5(41)≤7, so
every even degree-below-10 polynomial has at most 14 agreements, while
the explicit Dickson bank supplies 15. At d=5, r=2, the archived
eight-point determinant certificate gives quotient maximum 2, hence
invariant maximum 10. These are existing certificates, not new scans.

The missing positive target is therefore still a special prime-field
source with a genuinely short **actual nearest orbit**, or a different
nearestness theorem. The composition identity and averaging operation
alone cannot supply it. This note makes no upper-bound improvement and
does not change the unconditional extension-field ordinary-CA theorem.
