# Independent audit of Frobenius-monomial elimination

September 18, 2026. **PASS** for `FROBENIUS_MONOMIAL_ELIMINATION.md`, with its explicit fixed-r / r²=o(p) scope. No new variants or numerical searches were undertaken.

At a nonzero match to X^(p+r) on B=F_(p²), one has X^p=Q/X^r and X^(p²)=X. Raising the original equation to the p-th power and substituting gives, for r>=2,

    X Q^r = a^p X^(r²-2r) Q² + b^p X^(r²-r) Q + c^p X^(r²).

The powers cleared are nonzero at every evaluation point, so no matched point is lost. The polynomial has degree at most max(2r+1,r²); this bound applies whether leading coefficients vanish or not. Coefficients outside B are handled separately by a nonzero B-linear projection killing B, yielding at most two matches. These steps require neither factorial division nor r<p for the algebraic identity itself.

- **r=1:** the printed quartic follows after multiplication by X². Its constant coefficient forces a=0 or c=0. If c=0 and Q!=0, the cleared identity factors as X²(aX+b)[a^p(aX+b)+b^p-X]. The last factor must vanish, giving norm(a)=1 and a^p b+b^p=0, with exactly p choices of b for each of p+1 choices of a. If a=0 and c!=0, the cubic coefficient forces b=0 and then c^p=c. Zero Q has no matches. Thus the stated O(p²) family and its missing coefficient are correct.
- **r=2:** the degree-five coefficient is a², forcing a=0 even in characteristics where other coefficients simplify. The remaining degree-four coefficient forces c=0. For b!=0, the identity becomes b²=b^(p+1), equivalently b in F_p*. Its original equation is X^(p+1)=b, with p+1 nonzero solutions. Q=0 is separately excluded from positive match counts.
- **r=3:** the degree-nine coefficient forces c=0. For Q!=0 the stated division by X⁴(aX+b) is legitimate in the polynomial integral domain. The resulting cubic term forces b=0, and then a²=a^(p+1), so a in F_p*. Again the original equation is X^(p+1)=a. This classification remains valid in characteristic three; it does not rely on a nonzero binomial coefficient 3.
- **r>=4:** the c^p X^(r²) term is uniquely highest, so c=0. With b!=0 the left valuation is r+1, while every nonzero right term has valuation at least r²-2r+2>r+1. Cancellation on the right can only raise that valuation, not fix the discrepancy. With b=0 and a!=0, the two exponents differ by (r-1)(r-3)!=0. Hence no nonzero identity branch exists. The zero polynomial is an identity branch but has no nonzero matches, exactly as the note states.

The nonidentity root bound is o(p) only when r is fixed or r²=o(p). Under that guard, witnesses with Theta(p) matches must lie in the listed small identity families. At r on the square-root-p scale or larger, the degree bound no longer excludes such matches, and no closure of that regime is justified. Likewise this is not a result for arbitrary rational or polynomial received words.

Conclusion: the note rigorously closes the specified norm/fixed-shift Frobenius monomial mechanism as a source of p³ full-quadratic witnesses with Theta(p) matches on a p²-scale core. It does not establish a general full-quadratic population bound.
