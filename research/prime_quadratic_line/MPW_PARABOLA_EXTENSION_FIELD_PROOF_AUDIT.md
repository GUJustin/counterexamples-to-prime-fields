# MPW parabola bound: extension-field proof audit

September 18, 2026. **PASS.** The parabola part of MPW Theorem 1.3
extends to F_(p^e), uniformly in e, under the same characteristic-size
condition n << p^(15/13). The bound involves the characteristic p,
not the alphabet size p^e. This conclusion follows from the proof,
and MPW also explicitly notes the arbitrary-field extension in its
introduction. No manuscript changes or priority claim accompany this
audit.

## Primary inputs checked

- Mohammadi–Pham–Warren, *A Point-Conic Incidence Bound and Applications
  over F_p*, [arXiv:2111.04072v2](https://arxiv.org/html/2111.04072v2),
  introduction just before Section 1.1, Theorem 1.3, and Section 4.
  The parabola argument anchors one point, converts the remaining
  matches to lines in coefficient space, and invokes Corollary 4.1.
- Stevens–de Zeeuw, *An Improved Point-Line Incidence Bound Over
  Arbitrary Fields*, [arXiv:1609.06284v4, Theorem 3](https://arxiv.org/pdf/1609.06284),
  printed page 2. Its field F is arbitrary. For m points and N lines,
  its assumptions are m^(7/8)<N<m^(8/7) and, in characteristic p,
  m^(-2)N^13 << p^15. The bound is I << m^(11/15)N^(11/15).
  Lemma 1 on the same page supplies the elementary bounds outside
  that size range.

The following derivation checks the characteristic guard and all
unbalanced cases directly, without relying on a prime-field statement
of the intermediate rich-point corollary.

## 1. The rich-point input over an arbitrary field

Let N distinct lines lie over a field of characteristic p, with
N << p^(15/13), and let m be the number of points incident to at
least k>=2 lines. Then

    m << N^(11/4)/k^(15/4) + N/k.                     (1)

For N^(7/8)<m<N^(8/7), SDZ applies in its original orientation:
the characteristic expression is

    m^(-2) N^13 <= N^13 << p^15.

Since k*m<=I, its incidence bound gives the first term of (1).
No condition on the extension degree occurs.

If m<=N^(7/8), use I<=m*sqrt(N)+N. For k>2sqrt(N) this gives
m<=2N/k. For k<=2sqrt(N), the first term on the right of (1) is
at least a constant times N^(7/8), and so already bounds m.

If m>=N^(8/7), use I<=N*sqrt(m)+m. It follows that

    m <= N²/(k-1)² <=4N²/k²,
    k <=1+N/sqrt(m) <=2N^(3/7).

This upper bound on k makes N²/k² at most a constant times
N^(11/4)/k^(15/4). The boundary cases are covered by these elementary
arguments. Thus (1) is valid over the extension field with precisely
the advertised sufficient characteristic guard. This is the
intermediate estimate used as MPW Corollary 4.1.

## 2. The anchored parabola map has no extension-field degeneracy

Let P be any n-point set over F_(p^e), and fix an anchor q in P.
Translate q to (0,0). A polynomial graph through q now has equation

    y = a*x²+b*x.

For every other contributing point (alpha,beta), alpha is nonzero:
an anchored graph has no other point with x=0. Points with alpha=0
and beta!=0 may therefore be discarded. A remaining point gives the
coefficient-space line

    beta = alpha²*A + alpha*B,
    equivalently B = -alpha*A + beta/alpha.           (2)

The slope of (2) determines alpha, and its intercept then determines
beta. Distinct contributing points give distinct lines over any field.
Distinct anchored graph polynomials give distinct coefficient points
(a,b). This step needs only division by nonzero alpha; it uses no
prime-field order, integer lift, character sum, square-root selection,
or subfield-avoidance hypothesis.

A graph containing at least k>=3 points, including q, corresponds
to a coefficient point incident to at least k-1 of these lines.
Applying (1), summing over anchors, and dividing by at least k
anchor choices per rich graph gives

    |C_k| << n^(15/4)/k^(19/4) + n²/k².              (3)

Only sets of at most n lines enter (1), so n << p^(15/13) suffices
uniformly at every anchor. The construction also permits a=0; thus
the same proof controls all distinct degree-at-most-two graph
polynomials, including the linear and constant members needed for
RS dimension three.

The circle proof's nonsquare condition on -1 is not used in (2).
In particular, the parabola conclusion does not require p=3 mod4
or odd extension degree. The argument does not by itself license
discarding the circle hypotheses when extending that different case.

## 3. Recovering the exact incidence bound

Let L=|C|. A dyadic decomposition using (3), for any cutoff Delta>=3,
gives

    I(P,C) << Delta*L
              + n^(15/4)/Delta^(15/4) + n²/Delta.

Set Delta=max(3,n^(15/19)*L^(-4/19)). This yields

    I(P,C) << n^(15/19)*L^(15/19)
              + n^(23/19)*L^(4/19) + L.              (4)

This is the same formula and the same characteristic-size guard as
the parabola case of MPW Theorem 1.3. The post-reduction steps are
finite counting and optimization of real-valued cardinalities; no
additional prime-field input is introduced.

All << constants here are implicit absolute constants inherited from
the primary incidence theorem. The audit does not supply numerical
constants or a finite-parameter nonexistence certificate.

## 4. Scope of the resulting high-characteristic obstruction

For one common graph on n coordinates, if every member of a degree-two
bank has A>=c*sqrt(n) matches for a fixed c>0, (3) gives

    L <<_c n^(11/8)+n = O_c(n^(11/8)).                (5)

This remains valid over every F_(p^e) when n << p^(15/13), including
base-field evaluation domains with extension-field values. Hence
enlarging the alphabet alone cannot transfer a common-core bank with
L growing faster than n^(11/8) into this characteristic range while
preserving those incidences.

If, in addition, every successful pencil label is witnessed by this
bank and requires at least d informative matches, each bank-coordinate
pair supplies at most one label. Thus B*d<=L*n. For d>=c'*sqrt(n),
equation (5) implies

    B=O_(c,c')(n^(15/8)).                             (6)

This requires a bank rich on one common graph. It is not a bound on
all witnesses of an arbitrary affine line, and it does not make the
common-rich-core hypothesis necessary for every construction. The
two-ray block bank has only Theta(sqrt(n)) core-rich words and is
consistent with (5)–(6).

For n<=p and growing p, the guard has asymptotic slack: n^13/p^15
is at most p^(-2). By contrast, a full domain of size p^e with e>=2
does not satisfy it. Fixed characteristic likewise cannot support
growing n under this guard. These distinctions, rather than the
alphabet being prime versus an extension, delimit the transfer
obstruction established by this proof.
