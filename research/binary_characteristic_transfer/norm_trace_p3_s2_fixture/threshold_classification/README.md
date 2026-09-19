# Bounded finite check of the exact trace–norm threshold classification

The general theorem is proved in
../../ODD_TRACE_NORM_EXACT_THRESHOLD_CLASSIFICATION.md.
This folder supplies a separate exact verification of its exponent-orbit
step in three cases and of its equality-case polynomial identities in
the saved \(p=3,s=2\) fixture. The parent fixture is unchanged.

## Exponent and coefficient check

For \(Q=p^s,\ n=Q^2,\ d=(n+Q)/p\), the script enumerates multiplication
by \(p\) orbits of the nonzero exponents modulo \(n-1\). It retains
exactly the orbits whose every member is at most \(d\).

| \(p,s\) | \(n,d\) | Allowed nonconstant exponent orbits | Dimension over \(\mathbb F_p\), including constants |
|---|---|---|---:|
| \(3,2\) | \(81,30\) | \(\{1,3,9,27\}\), \(\{10,30\}\) | 7 |
| \(3,3\) | \(729,252\) | \(\{1,3,9,27,81,243\}\), \(\{28,84,252\}\) | 10 |
| \(5,2\) | \(625,130\) | \(\{1,5,25,125\}\), \(\{26,130\}\) | 7 |

The coefficient on each orbit determines the others by Frobenius.
Closing an orbit of length \(r\) forces that coefficient into
\(\mathbb F_{p^r}\), giving dimension \(r\); the constant is in
\(\mathbb F_p\). Thus the dimensions are the sums of the two displayed
orbit lengths plus one. This is the coefficient-field restriction, not
just a count of allowed monomials. The exponent \(n-1\) is excluded by
the degree cap.

## Full enumeration of the dimension-seven native-valued space

Only for the small \(p=3,s=2\) case, the script enumerates all
\[
 3^7=2187
\]
polynomials
\[
 G=\operatorname{Tr}_{\mathbb F_9/\mathbb F_3}(aX^{10})
   +\operatorname{Tr}_{\mathbb F_{81}/\mathbb F_3}(lX)+c,
 \quad a\in\mathbb F_9,\ l\in\mathbb F_{81},\ c\in\mathbb F_3.
\]
It verifies an explicit seven-element coefficient basis has rank seven
over \(\mathbb F_3\), then verifies that all 2187 resulting polynomials
are distinct. It checks every polynomial at all 81 native coordinates:
177147 exact finite-field evaluations.

| Number of distinct native roots | Number of polynomials |
|---:|---:|
| 0 | 2 |
| 21 | 648 |
| 27 | 240 |
| 30 | 1296 |
| 81 | 1 |

Exactly 1944 have degree 30. Completing the norm gives 648 at each
constant level \(0,1,2\). The 648 level-zero polynomials have a center
root of multiplicity ten and 21 distinct roots. The 1296 nonzero-level
polynomials are squarefree with 30 native roots.

Normalizing those squarefree polynomials to monic locators gives exactly
648 distinct locators, each twice. Taking the unique polynomial cube
root \(F\) of \(G'\) and reconstructing
\[
 P=\frac{\Lambda F}{G},\qquad \Lambda=X^{81}-X,
\]
gives precisely the existing 648 bank polynomials, each twice. Every
reconstructed polynomial is monic of degree 54, has correction degree
34, and has exactly 51 distinct native roots. Its normalized parameters
and exterior-pole label are checked against the saved parent bank.

## Literal equality-case identities

For all 2187 polynomials the script verifies
\[
 G^3-G=\Lambda G'.
\]
For every one of the 1296 full-degree squarefree cases, let
\(L=G/\operatorname{lc}(G)\), \(V=\Lambda/L\), and \(H=P/V\).
The script verifies that
\[
 H^3V-L^2=c\ne0
\]
is constant. Choosing a native root \(v\) of \(V\) and
\(\alpha=L(v)\), it then checks
\[
 c=-\alpha^2,\qquad
 L^3+cL=\Lambda H^3,\qquad
 (L/\alpha)^3-L/\alpha=\Lambda(H/\alpha)^3.
\]
It also completes the norm, divides by its nonzero prime-field level,
and recovers the original normalized \(G,F,P\) exactly. This checks the
scaling and descent equations used in the classification proof, rather
than only its numerical population.

## Reproduction and scope

Run from the repository root:

    /Users/jthaler/.local/share/research-toolchain/venv/bin/python research/binary_characteristic_transfer/norm_trace_p3_s2_fixture/threshold_classification/verify.py

The saved run uses about 1.2 seconds and 38 MB. The receipt records the
exact script and input-bank hashes.

This enumerates all elements of one dimension-seven space, not all
Reed–Solomon codewords or all monic received residuals with the prescribed
head. The general absence and singleton claims rely on the algebraic
classification theorem. No larger-parameter finite-field census or new
challenge-domain construction was attempted.
