# The p/3 candidate, and the sharper p>2D list threshold

## An explicit Frobenius critical value with one actual section

Let p>3 be prime, p/3<D<p/2, h=X^D and s=X^(p−2D). For a constant beta put

    F=u³+(2h−s)u²+(h²−2hs)u+beta,   H=1.

The weighted coefficient bounds hold. The point u=−h is critical and

    F(X,−h)=beta+h²s=beta+X^p.

The sign is plus. Thus the critical value is genuinely nonconstant with zero derivative. Nevertheless the only polynomial constant-fiber section is P=0, at label beta.

Indeed F(P)−beta=P[P²+(2h−s)P+h²−2hs]. If the label differs from beta, P divides a nonzero constant, so P is constant. For nonzero constant P the coefficient of X^(2D) is P and cannot cancel with another term, so no such section exists. At label beta the other possible sections would be roots of the quadratic factor. Its discriminant is

    s²+4hs=X^(2(p−2D)) [1+4X^(3D−p)].

The integer r=3D−p lies strictly between zero and p, so 1+4X^r has simple roots and is not a rational-function square. Hence the quadratic has no polynomial root. This verifies the candidate fully rather than just its critical value.

## Rational Frobenius ratios consume the root-domain budget

Let A,H be nonzero polynomials of degrees at most 3D over an algebraically closed field of characteristic p. Suppose A/H is a nonconstant pth power. Write a,b coprime with

    A/H=(a/b)^p,   A=G a^p,   H=G b^p.

Let M=max(deg a,deg b)≥1. Then

    deg G+pM≤3D,
    deg rad(H)≤deg G+deg b
               ≤3D−(p−1)M≤3D−p+1.             (1)

Consequently p>2D implies deg rad(H)≤D. This bounds distinct roots, not merely multiplicities; it is valid with arbitrary cancellations before reducing the ratio.

For any cubic constant-fiber bank F(P)=cH, at a coordinate where H is nonzero a received value determines c, and hence matches at most three bank members. If rad(H) has at most D roots, then on any n-coordinate domain

    L a≤L D+3n,
    L(a−D)≤3n.

At surplus a−D≥eta*n this gives L≤3/eta. Thus a nonconstant Frobenius ratio of the displayed size prevents a large fixed-surplus list, even though it need not prevent individual sections.

## Applying the budget to every positive-dimensional critical case

Use the weighted monic cubic in depressed form

    F=z³−3g z+b,  deg g≤2D, deg b≤3D,

and assume characteristic p>max(3,2D). As before, if a nonzero-label section exists, deg H≤3D. A common critical branch r satisfies r²=g and

    v=(b−2gr)/H,   v′=0.

If r is rational, it is polynomial of degree at most D. Its critical numerator b−2gr has degree at most 3D. If v is nonconstant, it is a pth power and (1) applies, yielding the direct L≤3/eta bound. If v is constant, the repeated-fiber reduction and audited cubic-cover lemma give at most eight sections or an affine family, whose list size is at most1/eta.

If r²−g is irreducible, its conjugate critical value also has zero derivative. Thus (b/H)′=0. If this ratio is nonconstant, (1) again gives the direct3/eta bound. Otherwise b/H=beta is constant, and the critical relation gives 3g′H−2gH′=0. A section z at label c with lambda=c−beta nonzero would satisfy

    z(z²−3g)=lambda H,
    (z²−g)(g′z−2gz′)=0.

Irreducibility excludes z²=g. Therefore (g/z²)′=0. Its height is at most 2D<p, so it is constant, which would make g a square over algebraically closed constants. This contradiction excludes every lambda≠0 section. The single remaining fiber contributes at most three sections.

The zero-dimensional critical-ideal argument never required a p-versus-D bound; characteristic different from two and three suffices for its valuation estimates. Therefore the complete arbitrary-word list theorem in ARBITRARY_WORD_CUBIC_LIST.md holds with the improved guard

    characteristic zero, or p>max(3,2D),

and the same bound

    L≤floor(9+(3+108D/n)/eta).

The new direct3/eta alternative is smaller than this bound. The proof does not assert that every critical value is constant at the improved threshold.

## Construction implication

On a prime-field domain of length n≤p, every rate D/n<1/2 meets p>2D. This closes the entire below-half-rate regime for the specified monic weighted-cubic polynomial first-integral mechanism. It does not apply to arbitrary first-order equations or rational first integrals with value-dependent denominators.

The explicit candidate above proves that nonconstant Frobenius critical values can coexist with an actual polynomial section before p reaches3D. What is missing for a positive construction is a growing section bank with enough distinct agreement coordinates. In this model the radical budget, rather than derivative nonvanishing alone, prevents that mechanism below half rate.
