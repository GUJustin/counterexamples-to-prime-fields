# Roots of X^(2p) minus an arbitrary quadratic over F_(p³)

Let K=F_(p³), p odd. For Q=aX²+cX+b in K[X], the equation X^(2p)=Q(X) has at most max(8,p+2sqrt(p)) roots in K, hence at most p+2sqrt(p) for p≥5. The same bound holds on K*. The exceptional even branch is essential; a blanket eight-root bound for nonsquares is false in general.

## Nonzero linear coefficient: exact degree-eight elimination

Assume c≠0 and write A(X)=Q(X). At a solution x put u=x^p, v=x^(p²). Then

    u²=A(x), v²=D(x)+c^p u,
    D=a^p A+b^p,
    C v=E(x)+F u,
    C=c^(p²), E=X²−a^(p²)D−b^(p²), F=−a^(p²)c^p.

Squaring the last relation and using u²=A yields L(x)u+M(x)=0, where

    L=2EF−C²c^p,
    M=E²+F²A−C²D.

L is not the zero polynomial. If a=0, it is the nonzero constant −C²c^p. If a≠0, E has nonzero X coefficient −a^(p²+p)c, so E is nonconstant; F≠0 and p odd then prevent L from vanishing identically.

Every root therefore satisfies M²−L²A=0, a polynomial of degree at most eight. If that polynomial is nonzero, there are at most eight roots. If it vanishes identically, A=(M/L)² in K(X), hence A is the square of a polynomial in K[X]: a rational function whose square is polynomial has no finite poles, and is polynomial itself. This is an actual K-square, not merely a square over an algebraic closure.

## Square and geometric-square cases

If Q=(sX+t)² with s,t∈K and s≠0, roots lie on the two affine-Frobenius equations X^p=sX+t and X^p=−sX−t. A nonempty fiber has p roots exactly when the slope has norm one, and otherwise at most one. Since Norm(−s)=−Norm(s) in the odd-degree extension, both slopes cannot have norm one. Thus their union has at most p+1 roots. For s=0 the bound is at most two.

A quadratic of discriminant zero with nonsquare leading coefficient is NOT a K-square. It is a nonsquare scalar times a linear square; equality to X^(2p), itself a square, forces that linear factor and X both to vanish. Thus there is at most one root. A nonsquare constant has no roots. These cases do not invalidate the rational-function-square step.

## Even branch: an elliptic character sum

Let c=0. Set y=x², so y^p=ay+b. If a=0 or Norm(a)≠1, this equation has at most one y and hence at most two x.

If Norm(a)=1, choose h≠0 with h^(p−1)=a. Solvability is equivalent to Tr_(K/Fp)(b/h^p)=0. An empty fiber has no roots. A nonempty fiber is y0+h F_p.

If b=0, this is h F_p. It has exactly p square preimages in K, including zero, and p−1 in K*: the quadratic character restricted to F_p* is its usual quadratic character because the extension degree is odd, so the nonzero character sum cancels.

If b≠0, the affine line avoids zero and alpha=y0/h lies outside F_p. Since [K:F_p]=3 is prime, alpha has degree three. The polynomial

    F(t)=Norm_(K/Fp)(y0+h t)

is a nonzero scalar times an irreducible cubic over F_p. It is squarefree because finite fields are perfect. Moreover the quadratic characters satisfy chi_K(y)=chi_p(Norm(y)). Consequently the exact number of roots is

    p + sum_(t∈F_p) chi_p(F(t)).

The smooth projective curve z²=F(t) is an elliptic curve with one rational point at infinity. Hasse's bound therefore makes the absolute character sum at most 2sqrt(p). This proves both upper and lower bounds p±2sqrt(p) for this branch. The standard bound is stated, for example, in [MIT 18.783, Hasse's theorem and point counting](https://ocw.mit.edu/courses/18-783-elliptic-curves-spring-2021/resources/mit18_783s21_notes7/).

## Small exact check

`check.py/json` tests every normalized quadratic Q(1)=1 over F27 and F125 (729 and 15625 polynomials). Multiplicative scaling x→t x preserves the equation family and square/even classification, and moves any nonzero matching point to one; zero contributes iff b=0. Thus this checks every nonempty root pattern up to that action, not only a sample. A polynomial with only the zero root already satisfies the bounds.

Observed maxima (including zero):

|p|K-square|non-even nonsquare|even nonsquare|
|--|--:|--:|--:|
|3|4|5|6|
|5|6|6|8|

The exact tuples, defining cubics, and normalization are in the receipt. Runtime was 0.35 seconds. No larger scan or manuscript edits.

The resulting p+O(sqrt(p)) estimate is uniform over all quadratic coefficients and therefore can control common-agreement explanations on any subset of K. Any application to a new affine received line must separately prove its support sizes and label counts; those do not follow from this root bound alone.
