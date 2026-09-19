# Five extra errors: exact quintic recurrence and the remaining elliptic target

September 18, 2026. Bounded algebraic assessment; no scan, fixture search, or rental.

**Status.** The five extra errors produce a genuine new system, not a free multiplicity factor on the old bank. The exact system below accommodates arbitrary errors inside the two fibers and arbitrary additional domain positions. No common received line satisfying it for a growing collection of subgroups has been constructed. The common multiplication-map factorization does not, by itself, solve the new recurrence equations.

## 1. Parameters and normalization

Use the notation of [FIXED_SUBGROUP_QUOTIENT_PLANES.md](FIXED_SUBGROUP_QUOTIENT_PLANES.md), with \(\ell\ge23\),

\[
n=(\ell^2-1)/2,\qquad k=n-4\ell+1,\qquad R=n-k=4\ell-1,
\qquad T=n-2\ell-5.
\]

Let \(\Phi\) be the monic domain locator. A parity-check matrix for the degree-\(<k\) code has columns

\[
h_x=\frac{(1,x,\ldots,x^{R-1})^{\mathsf T}}{\Phi'(x)}.
\]

For a received word \(w\), write its syndrome as
\(s_j=\sum_x w(x)x^j/\Phi'(x)\), \(0\le j<R\). Two received words are equivalent modulo the code exactly when their syndrome vectors agree.

Fix \(H\) and two distinct tags \(a,a'\in\mathcal A_H\), and put

\[
L_0=(N_H-aB_H)(N_H-a'B_H)=\sum_{i=0}^{2\ell}u_iX^i.
\]

Its roots are the two full nonkernel fibers. We seek an enlarged omission locator

\[
U=L_0J,\qquad J\mid\Phi,\quad \gcd(J,L_0)=1,
\qquad J\text{ monic},\quad d=\deg J\le5.
\]

These conditions require distinct domain roots for \(J\). A polynomial with arbitrary coefficients, roots off the domain, or repeated roots is not an admissible extra-error locator.

## 2. Exact elimination of the two full fibers

Define the transformed moment sequence, of length \(M=2\ell-1\), by

\[
\boxed{\quad c_j=\sum_{i=0}^{2\ell}u_i s_{i+j},
\qquad 0\le j\le2\ell-2.\quad} \tag{1}
\]

All indices lie in the available syndrome range. The linear map \(s\mapsto c\) has rank \(M\): since \(u_{2\ell}=1\), its rows have distinct last nonzero columns. Its kernel has dimension \(2\ell\) and is exactly the error space supported on the two fibers. Indeed it kills those parity-check columns because \(L_0(x)=0\) there.

If \(e\) is any error representation of \(s\), then

\[
c_j=\sum_{x\in\mathcal D\setminus Z(L_0)}
\frac{e(x)L_0(x)}{\Phi'(x)}x^j.
\]

Consequently the following conditions are equivalent:

1. \(s\) has an error representation supported on \(Z(L_0)\cup Z(J)\).
2. There are scalars \(\eta_z\), \(z\in Z(J)\), such that
   \[
   c_j=\sum_{z\in Z(J)}\eta_z z^j\qquad(0\le j<M).
   \]
3. Writing \(J(X)=\sum_{i=0}^dJ_iX^i\), with \(J_d=1\), one has
   \[
   \boxed{\quad\sum_{i=0}^dJ_i c_{i+j}=0,
   \qquad0\le j\le2\ell-d-2.\quad} \tag{2}
   \]

For the second equivalence, a monic recurrence of order \(d\) has a \(d\)-dimensional solution space on these \(M\) positions; the \(d\) sequences \((z^j)_j\) are independent and satisfy it. This also handles a root \(z=0\), using \(z^0=1\). Conversely reconstruct the actual additional errors as

\[
e(z)=\eta_z\frac{\Phi'(z)}{L_0(z)}.
\]

After subtracting them, (1) is zero, so the remaining syndrome is represented on the two full fibers. Thus this is sufficient as well as necessary, with arbitrary values and partial support permitted inside those fibers.

For a genuine received pencil \(s(\lambda)=s_f+\lambda s_g\), equations (1)–(2) are an exact system in \(\lambda\) and the at most five coefficients of \(J\), together with its split-divisor condition. The same two global syndrome vectors must be used for every \(H,a,a'\). The unknown extra positions cannot be chosen independently of these equations.

## 3. The part supplied by the isogeny

The isogeny gives

\[
L_0=N_H^2-\sigma N_HB_H+\pi B_H^2,
\qquad \sigma=a+a',\quad\pi=aa'.
\]

Let \(\mathcal M_P(s)_j=\sum_iP_i s_{i+j}\), with all polynomials padded to degree \(2\ell\). Then the precise constructive target is

\[
\boxed{
\sum_{i=0}^dJ_i\left[
\mathcal M_{N_H^2}(s_f+\lambda s_g)_{i+j}
-\sigma\mathcal M_{N_HB_H}(s_f+\lambda s_g)_{i+j}
+\pi\mathcal M_{B_H^2}(s_f+\lambda s_g)_{i+j}
\right]=0
} \tag{3}
\]

for \(0\le j\le2\ell-d-2\). In addition, \(Z^2-\sigma Z+\pi\) must have two distinct roots in \(\mathcal A_H\), and \(J\) must satisfy the domain conditions above. There are \(2\ell-1-d\) recurrence constraints, already \(2\ell-6\) when \(d=5\).

The shared identity \(\Phi=K_H\prod_{a\in\mathcal A_H}(N_H-aB_H)\) certifies that the two-fiber factor divides the domain locator. It does not force (3) for a common pair \(s_f,s_g\). In particular it does not assert that these three transformed moment sequences have a common quintic recurrence across different subgroups.

The recurrence implies a rank-at-most-five Hankel condition. Its minors are useful necessary equations, but rank alone is not the acceptance criterion: finite-sequence boundary degeneracies and nonsplit or off-domain recurrence roots must still be excluded. Equations (2), with the explicit split squarefree locator, are the exact test.

## 4. Remove padding before counting new labels

For a fixed \(s\) and \(L_0\), a representation with at most five extra domain points is unique after zero coefficients are removed. Two such representations would give a dependence among at most ten Vandermonde columns, while \(M=2\ell-1\ge45\).

Thus every retained extra point must have \(\eta_z\ne0\). Equivalently, the rational generating function

\[
\sum_{z\in Z(J)}\frac{\eta_z}{X-z}=\frac{A_J(X)}{J(X)}
\]

must be reduced: \(\gcd(A_J,J)=1\). Extra factors at zero-error positions merely pad the same witness and label. When \(c=0\), the witness is already supported on the two fibers, regardless of which five-point locator is appended.

This is the analogue of removing \(\gcd(C,B)\) in the [KKH quintic outsider system](../prime_quadratic_line/kkh_noncanonical_high_rate/EXACT_OUTSIDER_SYSTEM.md). There, a fixed monomial source and its long coefficient gap yield the special divisor identity

\[
L_U=(Y^2-b^2+\kappa)C+(Y-b)B.
\]

Here no corresponding common received line has been found. Replacing \(Y\) by \(N_H/B_H\) separately for each \(H\) changes that line, precisely the compatibility issue proved in the earlier quotient-plane note. The five-atom moment system retains the general freedom without pretending that the KKH line is shared.

## 5. A precise small-correction test for the existing quotient planes

There is also a bounded rational-identity test for attempting to absorb the new freedom as a correction to the existing fixed-\(H\) compiler. Keep its notation \(t=(\ell-1)/2\), \(r=t-2\), external poles \(b_H\), and

\[
L_H=N_H-b_HB_H,\qquad
f_H=\frac{N_H^r}{K_HL_H},\quad
g_H=-\frac{B_H^r}{K_HL_H}
\]

away from the kernel, with zero word values on the kernel.

Suppose

\[
\alpha f_H+\beta g_H-\alpha'f_{H'}-\beta'g_{H'}-P
\]

is supported on at most five domain coordinates, where \(\deg P\le k-1\). Remove from that correction set the two kernel sets and let \(J\) be the locator of what remains, with \(d_0=\deg J\le5\). Write

\[
A_H=\alpha N_H^r-\beta B_H^r,\qquad
A_{H'}=\alpha'N_{H'}^r-\beta'B_{H'}^r.
\]

The same degree computation as before now gives the necessary exact polynomial identity

\[
\boxed{
A_HK_{H'}L_{H'}-A_{H'}K_HL_H
-P K_HK_{H'}L_HL_{H'}
=\frac{\Phi}{K_HK_{H'}J}\,Q,
\qquad \deg Q\le d_0-1.
} \tag{4}
\]

For \(d_0=0\), take \(Q=0\). For \(d_0>0\), comparison of the highest possible degree also gives
\([X^{d_0-1}]Q=\alpha-\alpha'\). In addition to (4), the original word equality must be checked at kernel coordinates outside the allowed correction set; their values were defined by zero extension. Thus (4) alone is not silently promoted to an equivalence on those coordinates.

Using \(\Phi/K_H\equiv N_H^t\pmod{K_H}\), identity (4) implies

\[
\boxed{
QN_H^2\equiv\alpha J B_{H'}L_{H'}\pmod{K_H},\qquad
QN_{H'}^2\equiv-\alpha'J B_HL_H\pmod{K_{H'}}.
} \tag{5}
\]

This is a concrete interpolation target: a rational function \(Q/J\), with numerator degree at most four and denominator degree at most five, must take the displayed isogeny-dependent values on both kernel sets. Full divisibility in (4), its degree condition, and the word-value checks remain required. No identity from the common multiplication map has been shown to satisfy these conditions.

One scoped conclusion follows immediately. If \(\alpha=0\), then \(Q\) vanishes modulo \(K_H\). Since \(\deg Q\le4<t\), it is zero. The other congruence forces \(\alpha'=0\). Equation (4) then becomes an exact rational identity between \(\beta g_H\), \(\beta'g_{H'}\), and a polynomial, which the distinct-pole-divisor proof already excludes unless both coefficients vanish. Therefore a nonzero \(g_H\) cannot be identified with any word in the other subgroup's canonical plane by a codeword and five coordinate corrections. In particular, adding a common five-coordinate correction space does not identify the two entire canonical received planes.

This does not exclude point-dependent solutions of (3), nor nonzero-\(\alpha\) solutions of (4)–(5). It only rejects treating the five errors as an automatic correction that merges the existing planes.

## 6. Acceptance gate and outcome

A positive construction must give one rank-two global syndrome pair and a growing family satisfying (3), with reduced extra locators, distinct projective syndrome points, and separately proved endpoint/common-agreement bounds. The target loss must be checked against those actual source bounds; satisfying the threshold parameter window alone does not give a proximity gap.

The present isogeny identities supply the two-fiber factors and the three-term expression in (3). They do not supply a shared recurrence or the interpolation in (5). The next meaningful algebraic input would be an explicit formula predicting those recurrences for growing \(\ell\). Without it, enumerating quintic domain locators would be a large unsupported search. No computation is proposed on the basis of this reduction alone.
