# Non-divisor monomial orbits: exact discriminant and shape-energy gates

September 18, 2026. Symbolic assessment with independent audit PASS; see `NONDIVISOR_DISCRIMINANT_INDEPENDENT_AUDIT.md`. No construction search or rental. The pure-character divisor-exponent case is independently closed in PURE_CHARACTER_WRONSKIAN_CLOSURE.md. This note does not reopen it.

Let p be odd, n|p-1, D=mu_n, 3<=e<=n-1, and P=aX^2+bX+c with abc!=0. Write S={x in D:P(x)=x^e}, A=|S|. The orbit P_t=t^e P(X/t), t in D, has n distinct members because its three coefficient exponents are consecutive. Every member has A matches.

## 1. Exact overlap and discriminant identities

For t!=1 put m_t=|S intersect tS|. These are common matching coordinates of P and P_t, and

    sum_(t!=1) m_t=A(A-1).

The difference quadratic has discriminant

    Delta(t)=(b^2-4ac)(t^(e-1)-1)^2
                +4ac t^(e-2)(t-1)^2.

The formula is exact, including vanishing leading coefficients. Write chi for the quadratic character of Fp, extended by chi(0)=0.

### Degenerate actual overlaps cost only O(A)

Tangency at a common match x=t y implies P'(x)=t^(e-1)P'(y), hence

    xP'(x)/P(x)=yP'(y)/P(y).

The displayed rational function is nonconstant and has degree at most two. Indeed a constant logarithmic derivative would make the three nonzero coefficients have the same exponent in the field, impossible for odd p. Each x in S therefore has at most one distinct partner y in its fiber. A zero discriminant can contribute at most one actual common coordinate, and the total of these tangency contributions over all t is at most A.

If the leading coefficient of P_t-P vanishes, t^(e-2)=1, and a common match gives

    P(x)/x^2=P(y)/y^2.

This too is a nonconstant degree-at-most-two rational function, so the total actual contribution of linear differences is at most A. The difference cannot be constant with a root: leading and linear coefficients vanish simultaneously only for t=1.

Consequently at least A(A-3)/2 distinct ratios t give difference polynomials with TWO DISTINCT roots in Fp (not necessarily both in D). Thus if A~c sqrt(n), c^2>3/2, more than three quarters of ratios have two field roots, up to a vanishing error. This conclusion needs the preceding actual-overlap argument; merely bounding the number of roots of Delta would not justify discarding degeneracies.

For character sums the linear cases cause no problem: their formal discriminant is the square of their nonzero linear coefficient. A nonsquare discriminant has no common root, and zero discriminants contribute at most A in total. Therefore the stronger necessary character inequality is

    sum_(t in D\{1}) chi(Delta(t))
          >= A(A-2)-(n-1).                              (1)

To see this, the number D_+ of nonzero-square discriminants satisfies 2D_+>=A(A-1)-A. If Z is the number of zero discriminants, the left side is 2D_++Z-(n-1), proving (1). A target with c^2>3/2 requires positive character bias exceeding n/2 asymptotically.

## 2. The zero-discriminant bank is independently excluded

If b^2=4ac, every orbit member is a scalar times a square of a linear polynomial. Over Fp there are two possible scalar square classes. Partition the n candidates accordingly and choose a part of size at least n/2. For its fixed scalar nu, lift each received coordinate to the at most two points (x,y) with y^2=w(x)/nu. A selected linear square root of each candidate defines a distinct line and carries all its A matches to incidences with those at most 2n points.

The balanced Stevens–de Zeeuw line-incidence estimate gives O(n^(22/15)) incidences. If needed pad the point set to Theta(n) distinct points; this only increases incidences, and n<=p makes the characteristic condition n^11<<p^15 automatic. Hence A=O(n^(7/15))=o(sqrt(n)). This handles nonsquare leading coefficients too; calling every candidate literally a square over Fp without the two-class partition would be incorrect.

Primary source: https://arxiv.org/abs/1609.06284. This is a span-three family for which an additional square structure still gives a point-line reduction.

## 3. Why ordinary degree-Weil does not decide the surviving case

Assume delta=b^2-4ac!=0. For t!=1, remove the square factor (t-1)^2 and write

    H_e(t)=delta(1+t+...+t^(e-2))^2+4ac t^(e-2).

For e>=4 this polynomial is not a square even over an algebraic closure. Otherwise factor H_e-V^2=0 to get

    (sqrt(delta)S-V)(sqrt(delta)S+V)=-4ac t^(e-2),
    S=1+t+...+t^(e-2).

Both factors would be monomials, forcing S to have at most two terms, contrary to its e-1>=3 nonzero coefficients. The bounded e=3 case cannot produce growing agreement.

A usual multiplicative-character Weil estimate, after expressing the subgroup indicator by characters, only gives a bound of order e sqrt(p). One may also reverse the quadratic and replace e by n+2-e, choosing the smaller exponent. At the target A~sqrt(n), polynomial degree already requires that smaller exponent to be at least A. Since p>=n, a bound with this degree dependence is too large to contradict the required order-n bias in (1). Sparse ADDITIVE exponential-sum estimates must not be substituted for the needed multiplicative quadratic-character estimate. No degree-free sparse multiplicative estimate has been established in this note.

## 4. Remove the artificial zero-fiber bias

The leading and constant coefficients of P_t-P vanish respectively at

    L0=gcd(e-2,n)-1,   C0=gcd(e,n)-1

nonidentity ratios. At each such ratio the formal discriminant is a NONZERO square: its linear coefficient cannot vanish too unless t=1. Leading vanishing gives at most one root; constant vanishing gives at most one NONZERO root. When both vanish, the difference is a nonzero multiple of X and has no roots on D, so the two reductions add. Thus, using the at-most-A actual tangency contributions established above,

    2 D_+ >= A(A-2)+L0+C0,
    sum chi(Delta(t)) >= A(A-2)-(n-1)+L0+C0.           (2)

There is also the independent, slightly sharper total root-budget test

    A(A-1) <= 2(n-1)-L0-C0.                           (3)

It simply sums the available nonzero roots of every difference, before using any character information. This can already exclude exponents with large leading/constant degeneracy.

Now take the coprime chart gcd(e-1,n)=1 and put m=n-1. For t in D\{1}, define

    beta=b^2/(ac) in Fp\{0,4},
    v_t=4-4t^(e-2)(t-1)^2/(t^(e-1)-1)^2
       =4(t^(e-2)-1)(t^e-1)/(t^(e-1)-1)^2.

The exceptional zero fiber has EXACT size

    M0=L0+C0-B0,   B0=gcd(e,e-2,n)-1 in {0,1}.

This follows from the factored numerator and inclusion-exclusion; it is not a generic-fiber estimate. Write m'=m-M0 and retain only nonzero values:

    M_v=#{t:v_t=v}, v!=0,
    H_*(beta)=sum_(v!=0) M_v chi(beta-v),
    J(beta)=chi(beta) H_*(beta),
    K=A(A-2)-m+B0.

Because chi(ac)=chi(beta), each zero-fiber term contributes exactly +1 to the original signed discriminant sum. Subtracting those M0 terms from (2) yields the corrected necessary condition

    J(beta) >= K.                                    (4)

Thus a large v=0 fiber cannot create a spurious favorable character bias. In fact the exact identity sum chi(Delta)=2D_++Z-m yields the stronger necessary condition J(beta)>=K+M_beta, since zero discriminants in this coprime chart occur precisely at v_t=beta. The weaker (4) is sufficient for the energy bounds below.

## 5. Exact nonzero-fiber moments and a one-sided shape bound

Let E_*=sum_(v!=0) M_v^2 and C_*=H_*(0)=sum_(v!=0) M_v chi(-v). The elementary character-correlation identity gives

    sum_(beta in Fp) H_*(beta)^2 = p E_*-m'^2,
    sum_(beta in Fp) J(beta) = -m',
    S2 := sum_(beta in Fp) J(beta)^2
        = p E_*-m'^2-C_*^2.                           (5)

For the first identity, equal shifts contribute p-1 and distinct shifts contribute -1. For the signed first moment, every nonzero v contributes sum_beta chi(beta)chi(beta-v)=-1. Finally J(0)=0 removes H_*(0)^2 from the second moment. These statements hold exactly, including all multiplicities.

If K>0, the number of admissible coefficient shapes beta is at most S2/K^2. The negative first moment gives the stronger one-sided bound

    # admissible beta <= ((p-1) S2-m'^2)/(S2+(p-1) K^2+2K m'). (6)

To prove (6), sum over beta!=0, since J(0)=0 and K>0. Bound the count using sum_(beta!=0)(J(beta)+c)^2/(K+c)^2 for c>=0, and choose c=(S2+K m')/((p-1)K+m'). Equivalently this is the elementary one-sided variance inequality with mean -m'/(p-1). The excluded shape 4 remains in the sum, which can only make the bound less sharp. If the variance is zero, all J equal their nonpositive mean and no positive-threshold shape qualifies.

For n a positive fraction of p and E_*=O(n), (5)--(6) leave only O(1) possible shapes at A~c sqrt(n), c^2>3/2. No uniform E_*=O(n) theorem is assumed here. Removing the zero fiber is essential: its squared multiplicity could otherwise make the energy estimate vacuous even though it only creates automatic discriminant squares from degenerate differences. The remaining unavoidable symmetry v_t=v_(1/t) explains multiplicity two but does not exclude additional collisions.

For a specified exponent/domain, the nonzero multiset, E_*, and C_* are computable in O(n) field operations. Their exact moments require no scan of coefficient triples. The bounded checker `verify_discriminant_moments.py` replays the identities over p=11,17,31,47 and two subgroup sizes each, including coefficient degeneracies and the one-sided threshold bounds. It is proof validation, not evidence for a growing construction. Establishing a low-energy regime for this explicit rational map, or finding structured exponents with exceptional NONZERO fibers, is the remaining arithmetic lemma. Passing the moment or character screen is necessary only; it does not establish agreement roots in D.

## Scope and decision

The >75% two-root heuristic is valid after controlling actual tangencies and linear degenerations. The sharper signed-character requirement (1) is the useful invariant. The all-square bank is closed. Ordinary Weil bounds at the raw exponent degree do not settle the remaining range. The corrected one-parameter screen and nonzero-fiber moment identities (4)--(6) isolate what new arithmetic information is needed without repeating the closed pure-character or small-monomial scans. No positive prime-alphabet asymptotic family is claimed.
