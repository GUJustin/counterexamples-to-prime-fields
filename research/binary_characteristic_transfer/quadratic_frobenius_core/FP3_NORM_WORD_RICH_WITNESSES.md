# Fp³ norm-type word: exact rich-witness confinement

Independent audit: PASS, with an important population caveat. Let E=F_{p³} and f(X)=X^{p+1}. The degree argument works in every characteristic; the comparison with quadratic-code transformations below assumes p>2.

For Q=aX²+bX+c and a nonzero matching x,

    x^p=R(x),   R(X)=aX+b+c/X.

Twisting coefficients by Frobenius and iterating three times gives

    x=R^[p²] o R^[p] o R(x).

If a,c are both nonzero, R has degree two, so the composition has degree eight and cannot be the identity. Its fixed-point numerator has degree at most nine. Since c is nonzero, zero is not an original match. Thus Q has at most nine matches, including all zero cases correctly.

If R is a nonconstant Möbius map but the twisted composition is not the identity, its fixed-point numerator has degree at most two. This bounds nonzero matches by two; zero can add one only when c=0. A constant R (a=c=0) gives at most two original matches.

Consequently every quadratic with more than nine matches belongs to one of the coefficient planes a=0 or c=0. This does not say that the population is smaller than p³.

## Explicit reciprocal family: p³−1 rich witnesses

For a=0,c!=0, represent R by M=[[b,c],[1,0]]. Direct multiplication of M^[p²] M^[p] M shows that the composition is scalar identity exactly when

    b!=0,   c=−b^(1+p²).

Indeed the off-diagonal equations are c^p=−b^p b and c^{p²}=−b^{p²}b^p, and then both diagonal entries equal −b b^p b^{p²}.

For every b in E*, Q=bX−b^(1+p²) has exactly p+1 matches. Its residual X^{p+1}−bX+b^(1+p²) is squarefree: its derivative is X^p−b, and a common root would leave the nonzero constant term. Every root is nonzero and the twisted iteration proves x^{p³}=x, so all p+1 roots lie in E. Thus this is an actual p³−1 bank, albeit entirely inside span_E{X,1}. The proof must not be summarized as ruling out p³ rich banks.

## Affine family

For c=0,a!=0 the original residual is X(X^p−aX−b). The F_p-linear map X^p−aX has a p-element kernel exactly when Norm_{E/F_p}(a)=1; otherwise it is invertible. In the norm-one case b in its image gives p roots, with an additional zero root precisely when b!=0. Thus the rich affine family is Q=aX²+bX, Norm(a)=1, b in image(X^p−aX). It has agreement p for b=0 and p+1 for b!=0. There are p²+p+1 possible a, each with p² possible b. All remain inside span_E{X²,X}.

For small p, the generic degree-nine bound need not separate these families from other witnesses. The precise uniform statement is the bound and the explicit family counts above, not a complete classification at threshold p+1 when p+1<=9.

## What shifts and mixed words do

An affine input change X→uX+h, u!=0, preserves the quadratic code and transports the classification unchanged. Adding a common quadratic received-word term likewise only translates the two coefficient planes. Neither operation creates a full three-coefficient rich family.

The proposed mixed word X^{2p}+tX^{p+1}, t!=0, satisfies

    X^{2p}+tX^{p+1}=(X^p+(t/2)X)^2−(t²/4)X².

This is not an ordinary affine input conjugacy: X→X^p+(t/2)X is a linearized degree-p map, and transporting arbitrary quadratics through its inverse does not generally preserve the RS quadratic code. Moreover its degree 2p cannot become p+1 under an affine input change and addition of a quadratic when p>2. The identity therefore exposes a genuinely different remaining algebraic problem, but supplies no rich-bank construction or root-count theorem by itself. No nearby finite-field scan was run.

## Relation to the archived note

The earlier `../inversive_circle_gate/NORM_WORD_CLASSIFICATION.md` treats the full Fp² domain, including coefficients in extensions. Its four-root Bezout gate and smaller reciprocal family do not establish the present Fp³ statement. The new argument here is the threefold semilinear iteration and its explicit reciprocal identity. It confines rich witnesses to two coefficient planes; it is not a universal obstruction to a line construction from such a bank.
