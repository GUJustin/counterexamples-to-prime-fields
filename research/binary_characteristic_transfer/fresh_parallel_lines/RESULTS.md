# Fresh witnesses on a few additive lines

This tests new degree-at-most-p-1 witnesses, not merely the inherited locator witnesses. The received sources are the p^5 seed f=X^(p^4-1)+theta X^(p^3-1), g=X^(p^2-1), with theta outside F_(p^5). Domain points are nonzero.

## Exact parallel-line reduction

For parallel affine F_p-lines with direction v, let T=X^p-v^(p-1)X. It takes a distinct constant c_j on each line. Repeated Frobenius substitution expresses every X^(p^r) as alpha_r X+R_r(T), where alpha_r is independent of the line and R_r is additive. Interpolate R_r on the m constants c_j using a polynomial of degree at most m-1. After division by X, both sources lie, modulo degree-at-most-p-1 polynomials, in the span of

    1/X, T²/X, ..., T^(m-1)/X,

because T/X=X^(p-1)-v^(p-1) is already a codeword.

For two parallel lines, the quotient has dimension at most one. A non-code word is a nonzero scalar multiple of 1/X modulo the code; it has at most p agreements, since Xh-c has degree at most p and is nonzero. At most one label on a nonconstant quotient line can itself be a codeword. Consequently two parallel lines cannot generate a growing above-capacity exceptional population using fresh witnesses.

For three parallel lines, the first genuinely two-dimensional quotient is span{1/X,T²/X}. Special offsets can collapse it further: if all line constants lie on an affine F_p-line, every additive R_r restricts affinely and the quotient again has dimension at most one.

## Bounded exact gates

For each (p+1)-subset of domain coordinates, solve the interpolation system for p witness coefficients and the label. Matrix entries lie in F_(p^5); the two independent source components are solved simultaneously. Full coefficient rank makes the unique solution valid over every extension. Consistent deficient systems are retained explicitly; none occurred in the cases below. Thus these are exhaustive gates for witnesses with more than p matches on these particular domains, not finite-label scans.

* p3 affine-plane domain, nine points: all126 systems give the same label, which is a codeword on all nine points. This confirms the quotient-collapse case.
* p3, three noncollinear parallel cosets eta+F3, eta²+F3, eta³+F3: all126 systems have full rank. Three canonical witnesses match six points; 81 fresh witnesses match exactly four. No fresh witness reaches the first-order five-match target.
* p5, three noncollinear parallel cosets eta+F5, eta²+F5, eta³+F5: all5005 systems checked. One is inconsistent, none is a consistent deficient family. Three canonical witnesses match ten points; 4374 fresh witnesses match exactly six. No fresh witness reaches the first-order nine-match target. Runtime1.21sec.
* p5, two nonparallel lines eta²+F5 and eta³+eta F5: all210 systems have full rank and yield distinct witnesses with exactly six matches. None reaches the first-order seven-match target. Runtime0.05sec.

The p3 field modulus is X5+2X+1; the p5 modulus is X5+4X+3. Exact nodes and solutions attaining the larger thresholds are in the adjacent JSON receipts. The code uses explicit zero comparisons for FLINT field elements.

These instances provide no positive fresh-witness signal. They do not exclude special coset geometries. The remaining concrete possibility is to choose offsets/directions so additional interpolation minors vanish while preserving distinct coordinates and more than a bounded collection of labels. No further parameter scan was run.
