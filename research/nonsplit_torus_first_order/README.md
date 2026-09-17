# Nonsplit projective-torus orbit search

September 17, 2026. A finite alternative-family search; no new lower bound.

Take a nonsquare nu in F_p and the anisotropic quadratic form
q(X,Y)=X^2-nu Y^2. For even D, a homogeneous polynomial P of degree D
defines the function P/q^(D/2) on P^1(F_p). A norm-one matrix
[[a,nu*b],[b,a]], with a^2-nu*b^2=1, preserves q. Choose one whose
projective order is (p+1)/2. Its action has two coordinate orbits,
distinguished by the quadratic character of q at projective representatives.

For each candidate polynomial, select a modal value on each coordinate
orbit as the received word. The sum M of the two mode frequencies is
the maximum possible minimum agreement of the FULL candidate orbit
with ANY received word on this projective domain. Coordinatewise modes
maximize average agreement, and the invariant modal word makes every
candidate's agreement equal, attaining the bound. This does not optimize
proper candidate suborbits or other domains.

The function space has dimension D+1. Subtracting a constant function
removes P's leading X^D coefficient, because q^(D/2) is monic. Nonzero
output scaling then normalizes the highest remaining coefficient to one.
The complete normalized search therefore has (p^D-1)/(p-1) cases.
The sparse searches permit at most three nonzero coefficients AFTER
this normalization, giving sum_{s=1}^3 binom(D,s)(p-1)^(s-1) cases.

The domain includes infinity, so these are projective, weighted RS
evaluations. Puncturing infinity and undoing the nonzero column weights
gives ordinary RS on F_p, dimension D+1, with minimum agreement M-1.
The verifier explicitly checks this loss for every extremal witness.
Projective regime crossings must not be reported as affine crossings.
Neither type of finite crossing alone proves asymptotic tightness.

| p | D | Search | Best agreement by orbit size |
|---|---|---|---|
|11|4|complete|3:8, 6:6|
|19|4|complete|5:8, 10:7|
|19|6|complete|5:8, 10:10|
|31|6|complete|8:8, 16:11|
|43|12|three terms|11:16, 22:14|
|67|16|three terms|17:22, 34:19|
|67|22|three terms|17:16, 34:26|
|83|20|three terms|21:20, 42:18|
|83|28|three terms|21:20, 42:18|

Only the three-element orbit over F11 crosses the projective first-order
curve in these searches. The other cases supply no growing-orbit lead.
For each row the C++ output records exact orbit counts, the maximum,
a witness, and the number of normalized cases above the continuum curve.
All rates are in the range of the quadratic first-order expression
(8-rho)a^2-6rho*a+rho(4rho-5). Its sign is evaluated in integer arithmetic.

All numerical jobs ran sequentially with a 384 MiB, 60 second watchdog.
`verify.py` independently checks the extremal orbits by homogeneous
matrix substitution, all mode agreements, affine puncturing, and case
counts. It repeats the entire F11 census using a separate enumeration.
This finite search does not exclude dense polynomials in the larger
fields, other torus representations, or arbitrary received-word lists.
