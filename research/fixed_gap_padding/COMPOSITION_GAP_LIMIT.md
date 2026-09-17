# Independent inner composition cannot preserve a fixed gap indefinitely

September 17. Elementary degree obstruction for a proposed amplification
route; not a theorem about all prime-field list constructions.

Let F be monic of degree A, and let G,H be distinct monic polynomials of
the same degree B. Put a=deg(G-H)<B. If the characteristic does not divide
A, then

    deg(F(G)-F(H)) = (A-1)B+a.

Indeed G^A-H^A=(G-H) sum_{j=0}^{A-1} G^{A-1-j}H^j. The sum has leading
coefficient A and degree (A-1)B. Every lower-degree term of F contributes
a difference of strictly smaller degree. This is exact, not merely a
root-count upper bound.

Suppose a Cartesian family of proposed locator polynomials includes both
F(G) and F(H), each monic of degree AB, and all locators have the same
coefficients in degrees K through AB. Their differences have degree <K,
so K >= (A-1)B+a+1. If the locators each split on AB distinct positions of
a domain of size n, then AB<=n and the corresponding capacity gap satisfies

    eta=(AB-K)/n <= (B-a-1)/n < 1/A.

Thus independent variation of the inner polynomial is incompatible with
outer degree A>=1/eta. On short prime-field domains n<p the hypothesis
on characteristic is automatic, because A<=AB<=n<p.

For a nested composition, apply this to the product of all degrees above
any independently varying inner layer. That product must stay below
1/eta. Repeated composition therefore does not supply an unrestricted
way to multiply list sizes at one fixed positive gap. This complements
the independent-product obstruction in INDEPENDENT_PRODUCT_LIMIT.md.

Scope: this does not exclude coupled choices of outer and inner
polynomials, non-Cartesian subfamilies, different degrees, or a received
word not obtained by common leading coefficients of these locators.
When the characteristic divides A, the degree identity can fail:
F=X^p has F(G)-F(H)=(G-H)^p. That exception cannot occur with AB<=n<p.
