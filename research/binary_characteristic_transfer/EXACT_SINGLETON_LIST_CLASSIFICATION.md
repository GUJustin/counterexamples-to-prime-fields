# Exact bad-label and nearest-list classification for the p^5 specialization

Let p>=3 be prime, B=F_(p^5), and let F contain B properly. Choose theta in F outside B. On the full domain B consider

    f(X)=X^(p^4-1)+theta X^(p^3-1),
    g(X)=X^(p²-1),

with message degree less than p. At the actual threshold A=p³-1, the following stronger conclusion holds:

* The labels z having any degree-<p candidate with at least A agreements are exactly the Gaussian locator labels.
* There are exactly [5 choose 2]_p such labels.
* For each such label the degree-<p list at threshold A consists of exactly one polynomial. It agrees on exactly A points, so is the unique nearest polynomial.

This is a classification at the **actual**, above-exact-Johnson threshold A. It does not classify lists at the smaller advertised threshold A0=p³-p².

## 1. Any close polynomial has only two possible coefficients

Suppose h has degree less than p and agrees with f+zg at at least p³-1 points. Put

    R(X)=X^(p^4)+theta X^(p³)+z X^(p²)-Xh(X).

Its root set S in B has size at least p³-1, since multiplication by X cannot remove a matched root. Count ordered pairs of distinct elements of S by their nonzero difference t in B. Since

    (p³-1)(p³-2)>(p-1)(p^5-1)

(the difference is p^5-3p³+p+1>0), some t!=0 satisfies |S intersect (S-t)|>=p. The polynomial R(X+t)-R(X) has degree at most p-1: all three high powers are Frobenius powers, and the degree-p term of Xh also has constant finite difference. It has at least p roots, and hence is identically zero.

Therefore (Xh)(X+t)-Xh(X) is constant. If Xh contained a nonzero term of largest degree j with 2<=j<=p-1, its finite difference would have nonzero leading coefficient j*t in degree j-1; the possible degree-p term only contributes a constant. This is impossible. As Xh has zero constant term,

    h(X)=alpha X^(p-1)+beta.

Consequently R is p-linearized, and its root set in B is an F_p-subspace. Having at least p³-1 elements, it has at least p³ elements.

## 2. Every close label is a locator label

Apply any B-linear functional on F vanishing on B+B theta to the coefficients of R. The resulting polynomial has degree at most p² and vanishes on at least p³ distinct elements of B. It is zero. Hence z,alpha,beta all belong to B+B theta.

Write z=z0+theta a, alpha=alpha0+theta alpha1, and beta=beta0+theta beta1. The theta component of R is the monic polynomial

    L=X^(p³)+a X^(p²)+c X^p+vX,
    c=-alpha1, v=-beta1.

It vanishes on all the roots of R in B, so there are exactly p³ such roots. They form a three-dimensional subspace W, and L is its monic locator. In particular v!=0 because a subspace locator is squarefree.

The B component of R has leading term X^(p^4), no X^(p³) term, and vanishes on W. Subtract L^p-a^p L. The difference has degree at most p², so it vanishes identically. Coefficient comparison yields

    z0=c^p-a^(p+1),
    alpha0=a^p c-v^p,
    beta0=a^p v.

Thus z=c^p-a^(p+1)+theta a, precisely the compiler label, and h is precisely its compiler witness.

## 3. Uniqueness and exact agreement

Fix z. Its theta and B components determine a and c uniquely. If two three-dimensional subspaces W,W' gave the same a,c, their locators would differ by (v-v')X. Their intersection has dimension at least one, and so contains a nonzero element. Evaluating there gives v=v', hence W=W'.

Conversely every three-dimensional W gives a valid label and witness by the compiler identity. Their number is [5 choose 3]_p=[5 choose 2]_p. The witness's constant term is beta=-(theta-a^p)v, which is nonzero. Its agreement set is therefore W minus {0}, of size exactly p³-1.

No candidate can agree more often: it would satisfy the same classification and have exactly this agreement count. The nearest list at every qualifying label is consequently a singleton.

Replacing f by f+s g simply translates the classified label set by -s. In the degree-at-least-three extension used for exact individual-source comparisons, s outside B+B theta makes every exceptional label nonzero without changing these list conclusions.

## Interpretation

The exact Gaussian count is not explained by a large list at any one exceptional word: each of those words has a singleton nearest list at the actual threshold. Comparing the count to the square of a Johnson *upper bound* for ordinary lists would therefore conceal the actual behavior. This does not by itself disprove a theorem involving list sizes at a lower agreement threshold, or a supremum over all received words of the code.
