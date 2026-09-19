# Character-times-linear cyclic banks cannot cross sqrt(n) by a fixed factor

September 19, 2026. **Superseded in part:** `CHARACTER_ADJACENT_EXPONENT_GCD_GATE.md` subsequently closes the h and h+2 full-coefficient possibilities left open below; this note retains the earlier reasoning and exact fiber criterion. This is a constructor-specific ordinary-list statement, not a line-proximity theorem. No new large search was run.

Let D=mu_n be a multiplicative subgroup of F_p*, with n<p, write n=hr with h,r>=2, and receive f(x)=x^(h+1). Put chi(x)=x^h, whose image has order r and whose fibers have size h. For a quadratic P=aX^2+bX+c with ac nonzero, let T be its agreement count.

On a fiber chi(x)=zeta, agreement means

    a x^2+(b-zeta)x+c=0.

At most two distinct points match. If two do, their product is c/a, so applying chi yields zeta^2=(c/a)^h. At most gcd(2,r) members of mu_r satisfy this condition: the squaring map on mu_r has kernel of that size. Thus

    T <= r+gcd(2,r),    T <= h+1.

The second bound is the degree of X^(h+1)-P. In particular, writing g=gcd(2,r), for T>g,

    (T-1)(T-g) <= hr=n,
    T <= (g+1+sqrt((g-1)^2+4n))/2 <= sqrt(n)+2.

Hence no sequence in this family has T>=c0 sqrt(n) for any fixed c0>1 as n grows.

Degeneracies do not conceal a large rich list. If a=0,c!=0, each character fiber contributes at most one match; if c=0,a!=0, the same holds. Both obey T<=min(r,h+1). The only exceptions are P=bX, which can have h matches, and there are at most r such nonempty polynomials, one for each b in mu_r. Consequently, if T exceeds the displayed nonmonomial bound, the complete list has at most r=n/h<=n/T members. In particular T>sqrt(n) forces this exceptional monomial list to have fewer than sqrt(n) members. The zero polynomial has no matches.

The reciprocal map x->1/x, f->X^2 f(1/X), P->X^2 P(1/X), preserves the same assertions for exponent m=1-h modulo n. More generally m=1+kh with gcd(k,r)=1 retains the fiber bound r+g, but need not retain degree h+1; the stronger square-root conclusion is only claimed for k=+1 or -1. Multiplication of exponents by arbitrary units is not an allowed equivalence because it does not preserve the degree-two code.

## Nearest family escaping the proof

For f=X^h (and reciprocally f=X^(2-h)), a fiber instead gives

    a x^2+b x+c=zeta.

Its root product is (c-zeta)/a, which varies with zeta. The constant-product argument above no longer applies. The elementary bounds are only T<=min(h,2r). They permit T close to sqrt(2n) when h is close to 2r. Thus this is a mathematically admissible next exponent family, but no scalable candidate is supplied here.

There is a further exact-edge obstruction. Suppose h=2r, r>=2, and P has a!=0 and b!=0. It is impossible to have T=h=2r. Otherwise the monic polynomial F=X^(2r)-P has all its roots in D; on those roots P(x)^r=x^(hr)=1. Both F and P^r-1 have degree 2r, so

    P^r-1=a^r (X^(2r)-P).

Differentiate and evaluate at the unique zero x0=-b/(2a) of P'. Since 2r=h<p, the result is 0=a^r (2r) x0^(2r-1), forcing x0=0 and hence b=0, a contradiction. This rules out complete splitting at the exact balanced edge for full-coefficient quadratics; it does not exclude T=(1-o(1))sqrt(2n), unbalanced h,r, or a different exponent.

A positive construction would therefore require a sparse polynomial X^h-aX^2-bX-c having many, but not necessarily all, roots in mu_(hr), with h,r both of order sqrt(n), and preferably a multiplicative orbit of n distinct candidates. There is no proof here that such a family exists. For full nonzero coefficients the orbit is of size n when h is not 0,1,2 modulo n, because the three consecutive character exponents have trivial common stabilizer.

## Exact bounded evidence

`character_linear_gate_check.py` replays all applicable entries of the existing 698-profile census (p=17,97,193); it does not rerun or extend the scanner. Every full-coefficient maximum for m=h+1 obeys the new bound. The p=17,n=16,m=5 seed with T=5 is fully consistent with the additive constant and cannot imply a fixed factor above sqrt(n).

The same replay identifies all m=h proper-character profiles with full-coefficient T>sqrt(n). They are only n=8,h=4,r=2,T=3, repeated over the three primes. Thus the existing bounded evidence does not favor a scalable positive family; the escaped family remains an algebraic question, not a computational success. The saved receipt distinguishes a check of archived census data from an independent recomputation.

## Exact double-fiber criterion for m=h+2

The other adjacent family f=X^(h+2) has a useful explicit criterion (suggested by the root agent). Assume abc!=0 and n=hr. In a double fiber zeta=x^h, write the two roots as x and omega*x. Then omega belongs to mu_h, omega!=1,-1, and Vieta gives exactly

    x=-c(1+omega)/(b*omega),
    zeta=a-b^2*omega/[c(1+omega)^2].

Conversely these formulae give a double agreement fiber if and only if x^h=zeta and zeta^r=1. The signs follow from the fiber polynomial (zeta-a)X^2-bX-c. The omitted omega=-1 would force b=0; omega=1 would repeat a root. Two valid omega values related by inversion give the same double fiber, and no other duplication occurs.

This is an exact small algebraic test: put K=(-c/b)^h, B=b^2/c and form

    H0(W)=W^h-1,
    H1(W)=K(1+W)^(h+2)-a(1+W)^2+B W,
    H2(W)=[a(1+W)^2-B W]^r-(1+W)^(2r).

The number of double fibers is half the number of common roots of H0,H1,H2 other than W=+1,-1. Since h divides p-1, H0 splits simply over F_p, so this count is exactly half the degree of their gcd after removal of those roots. Each condition is necessary: H1 enforces x^h=zeta; H2 ensures zeta belongs to mu_r, equivalently x lies in D. The criterion is not an independence heuristic or an existence theorem. It could support a small parameterized gcd search if a structured coefficient family becomes available; absent such a family, it does not justify a large sweep.

The general bounds for this family remain T<=min(h+2,2r), and the product-of-roots condition is zeta^2(a-zeta)^h=c^h. Unlike the h+1 case this is not a constant-size restriction on double fibers. Therefore m=h+2 (as well as m=h) remains a genuine algebraic escape from the square-root obstruction, with no demonstrated scalable rich bank.

`check_double_fiber_identity.py` separately verifies the h+2 criterion by direct agreement enumeration for 625 nonzero coefficient triples: a,b,c in {1,2,3,4,5} for (p,n,h)=(17,16,2),(17,16,4),(17,16,8),(29,28,4),(29,28,7). It checks the exact number of double fibers against H0/H1/H2 roots and checks closure under inversion. `double_fiber_identity_receipt.json` records PASS. This finite replay checks the formula, not asymptotic existence or a search frontier.
