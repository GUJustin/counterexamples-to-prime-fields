# Universal first-jet contact resource and zero-charge classification

## Theorem: a sharp resource for every received word

Let K be any field, w>=2, and n>=2w. Let x_1,...,x_n be distinct elements
of K and r_i arbitrary received symbols. For a nonzero polynomial
F in K[X,Y,R], use weights (1,w,w-1), and define its ACTUAL formal contacts

    a_i=ord_t F(x_i+t,r_i+tR+t^2E,R).

Put V=wt(F), r=deg_R F, A(X,Y)=[R^r]F, q=deg_Y A, and
B(X)=[Y^q]A!=0, d=deg B. Then, in EVERY characteristic,

    a_i <= q+2ord_(X-x_i) B,                     (1)
    e(F):=V-(w/n)sum_i a_i
       >= r(w-1)+(1-2w/n)d >= r(w-1).            (2)

In particular every factor has nonnegative charge, with no small-degree,
subset-count, coprimality, genericity, or characteristic assumption.
The coefficient field may be K=k(Z); the received symbols may be f_i+Zg_i.
Degree in R, not merely the nonvanishing of F_R, is controlled, so R^p
terms are included in small characteristic.

### Proof of the local bound

Translate r_i to zero and decompose F(x_i+t,r_i+Y,R) into pieces homogeneous
in (Y,R). The local substitution preserves degree in formal (R,E), so the
contact of the full polynomial is the minimum of the contacts of these pieces.
For a homogeneous piece of degree k+r containing B_k(t)Y^kR^r, no term
has R-degree greater than r. Thus it has a factor Y^k, and its remaining
factor G(t,Y,R) is homogeneous of degree r with G(t,0,1)=B_k(t).

Expand

    G(t,Y,1)=sum_j c_j(t)(Y-t)^j.

The coefficients c_j(t) are integral polynomials in t. After the zero-word
substitution, G becomes

    sum_j c_j(t)t^(2j)E^j R^(r-j).

Consequently its contact is a=min_j(ord c_j+2j). But
G(t,0,1)=sum_j c_j(t)(-t)^j has order at least ceil(a/2), because
ord c_j+j >= (ord c_j+2j)/2. Thus this homogeneous piece has contact
at most k+2ord B_k. The full contact is no larger.

Apply this to k=q: translation by r_i leaves the leading Y coefficient
of A unchanged, so B_q(t)=B(x_i+t). This proves (1). Notice that no
factorial division or root extraction occurs.

Summing (1) gives sum a_i<=nq+2d. The coefficient B Y^q R^r gives
V>=qw+r(w-1)+d. Subtracting proves (2).

### Sharpness and primary factorization

The zero-word polynomial Y^q R^r attains e=r(w-1). For any primary
Q0 of weight W0<mA and contact at least m at every node, factor
Q0=c product_j F_j^(h_j). Contacts and weights add, giving

    0 <= sum_j h_j e(F_j) < m(A-w),
    (w-1) sum_j h_j deg_R(F_j) < m(A-w).          (3)

These inequalities hold without the earlier enormous-binomial sufficient
conditions. At the pinned benchmark the resulting derivative-degree bound
is weaker than the separately known source R-degree cap36; no numerical
benchmark improvement follows.

## Theorem: complete zero-charge classification

In the setting above, suppose e(F)=0. Then F is independent of R.
Put q=deg_Y F. If q=0, F is a nonzero scalar. If q>=1, then in EVERY
characteristic

    F=c(Y-P(X))^q,
    c in K^*,  deg_X P<=w,  P(x_i)=r_i for all i. (4)

This removes the earlier assumptions gcd(n,w)=1, q<w-1, n>w+q, and
any restriction on the characteristic.

### Proof

Equation (2) forces r=0. Let B(X) be the leading Y coefficient of F,
and d=deg B. For an R-free polynomial, the coefficient of R^q E^0 in
the local substitution is exactly t^q B(x_i+t). Therefore the sharper
local inequality a_i<=q+ord_(X-x_i)B holds. It implies

    e(F)>=V-qw-(w/n)d >= (1-w/n)d.

Since n>w, zero charge forces d=0, V=qw, and all a_i=q. If q=0 this
already says F is scalar. Otherwise write B=c in K^*. First suppose
q is nonzero in K. The coefficient
of R^(q-1) E^0 is

    t^(q-1) [q*c*r_i+B_(q-1)(x_i+t)],

where B_(q-1)(X) is the coefficient of Y^(q-1). Contact q gives
q*c*r_i+B_(q-1)(x_i)=0. Thus P=-B_(q-1)/(q*c) matches every symbol,
and deg P<=w by the weighted cap V=qw.

The residual J=F-c(Y-P)^q has contact at least q, weight at most qw,
and Y-degree j<q if nonzero. Its leading coefficient C_j(X) then has
ord_(X-x_i) C_j>=q-j at every node, by the coefficient of R^j in its
local substitution. Hence the domain locator to power q-j divides C_j.
But deg C_j<=(q-j)w<(q-j)n, a contradiction. Therefore J=0.

### Frobenius descent when the characteristic divides q

Suppose char K=p>0 and p divides q. Differentiate the local contact identity
with respect to R. Since F is independent of R, this gives

    t*(F_Y after substitution)=0 mod t^q.

Thus F_Y has contact at least q-1 and weight at most (q-1)w. If nonzero,
the universal nonnegative resource forces its weight to be exactly (q-1)w
and its charge to be zero. The preliminary zero-charge argument above,
which used no division by q, then says its Y-degree equals q-1. But the
leading term cY^q differentiates to zero, so deg_Y F_Y<=q-2. Contradiction.
Hence F_Y=0.

Differentiating the contact identity with respect to t now gives contact
at least q-1 for F_X, since the chain-rule term (R+2tE)F_Y is zero.
Assume F_X nonzero and write j=deg_Y F_X. All Y exponents of F are
multiples of p, and its leading coefficient c is constant in X. Hence
j<=q-p. Its leading coefficient C_j(X) must satisfy

    Lambda^(q-1-j) divides C_j,
    deg C_j<=(q-j)w-1,

using the coefficient t^j C_j(x_i+t) of R^j in the local substitution
and the strict weight loss under X differentiation. Put d=q-j>=p>=2.
Then

    n(d-1)>=2w(d-1)>=dw>dw-1,

contradicting these two degree bounds. Thus F_X=0 as well.

Over the perfect closure of K, these two vanishing derivatives imply
F=G^p for a polynomial G. It has weight (q/p)w, Y-degree q/p, and actual
contact q/p at every node: polynomial substitution commutes with p-th
powers, and orders multiply by p. Induct on the positive Y-degree q.
The induction either repeats this step or reaches the already proved
case in which q is invertible. It gives

    F=c(Y-P)^q,  deg P<=w,  P(x_i)=r_i,

initially over the perfect closure. Since n>=2w>w, interpolation at any
w+1 original nodes expresses every coefficient of P in the original
field K. Thus P descends to K. The scalar c was already the original
leading coefficient. This proves the classification in every characteristic.

For affine symbols over k(Z), interpolation at w+1 nodes forces
P=P0(X)+ZP1(X), with P0,P1 over k and degrees at most w. Thus a
positive-weight irreducible zero-charge factor is exactly a received-line
graph factor. The degree endpoint is <=w, not the strict <w convention.

## What remains geometric

The universal inequality is a complete factor-level resource, including
nonuniform contacts and nonhomogeneous carriers. A first-tail component is
not a separate primary factor, so this theorem does not independently charge
its normal-divisor cost. The explicit binding simple-tail model satisfies
(2), since5898195>12*(w-1)=1572840. Universal-kernel divisibility and
retained-source hypotheses remain unaccounted for by this scalar resource.
