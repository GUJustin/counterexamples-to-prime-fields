# Independent review: support-incidence envelope

**Verdict:** the claimed envelope is correct for linear MDS codes, including
all witness pairs simultaneously and the degree factor for polynomial
curves. The affine parameter-count version and the sharp local rejection
lemma are already Jo's Lemma 4.1 and Theorem 4.2. Present the witness/curve
form as a direct extension of that argument, not a new affine MCA bound.

## An especially short proof of rejection abundance

Let `C` be an `[n,k]` MDS code, `S` have size `s>=b>=k+1`, and
`w` be outside `C|S`. Let `R_b(w;S)` count `b`-subsets `T` of `S`
with `w|T` outside `C|T`. Then

\[
R_b(w;S)\ge\binom{s-1}{b-1}.
\]

Induct on `s`, with `b` fixed. For `s=b`, the whole support rejects.
If `s>b`, at most one of the `s` single-coordinate deletions can accept:
two accepting deletions would give codewords agreeing with one another
on `s-2>=k` positions, hence the same codeword, and together those
deletions cover `S`. That contradicts `w` being outside the code.

At least `s-1` deletions therefore remain outside their punctured MDS
codes. Induction and double counting give

\[
(s-b)R_b(w;S)
\ge(s-1)\binom{s-2}{b-1}
=(s-b)\binom{s-1}{b-1}.
\]

The lower bound is sharp: take a codeword and change exactly one
coordinate. Precisely the `b`-sets containing that coordinate reject.
This proof of abundance also works for nonlinear MDS codes with the
usual size/uniqueness property, although the curve argument below needs
linearity.

## All witness pairs on a curve

Let `C` now be linear over `F_q`, and let
`f(z)=sum_{j=0}^e z^j f_j` be a **formal** degree-at-most-`e` curve.
Count pairs `(z,c)` with `z in F_q`, `c in C`, whose entire agreement
support `S={i:f(z)_i=c_i}` has size at least `t>=k+1`, and for which
some coefficient `f_j|S` is outside `C|S`. Fix `k+1<=b<=t`.

For each pair, select one such coefficient. The rejection lemma yields
at least `binom(|S|-1,b-1)` incident subsets `T` contained in `S` on
which that coefficient rejects. A fixed incident `T` has a nonzero
vector polynomial

\[
\sum_{j=0}^e z^j[f_j|T]\quad\text{in }(F_q^T/C|T)[z].
\]

At least one scalar coordinate of this vector polynomial is nonzero and
has degree at most `e`, so it has at most `min(e,q)` field roots.
At each root there is **at most one global codeword** agreeing on `T`,
because `|T|>=k` and puncturing an MDS code to `k` coordinates is
injective. Thus a fixed `T` is incident to at most `min(e,q)` pairs,
even when many codewords are near one curve point. Consequently,

\[
\sum_{(z,c)\text{ unexplained}}
\binom{|S(z,c)|-1}{b-1}
\le\min(e,q)\binom nb,
\]

and the number of unexplained pairs is at most

\[
\left\lfloor\min(e,q)
\min_{k+1\le b\le t}\frac{\binom nb}{\binom{t-1}{b-1}}
\right\rfloor.
\]

The incident collection for a pair may instead include every rejecting
subset for every coefficient, counted only once. Choosing one bad
coefficient merely supplies the lower bound; it causes no ambiguity or
multiple counting in the upper bound.

## Edge cases and qualifications

- For `e=0`, there are no unexplained witnesses: any agreement support
  has `f_0|S=c|S`. The zero upper bound is correct.
- If `e>=q`, the formal quotient polynomial can vanish at every field
  point. The bound `min(e,q)` is still correct. A coefficient-based
  explanation then depends on the chosen formal representation of the
  curve; it need not be intrinsic to its function on `F_q`.
- At `t=k+1`, only `b=k+1` is available and the affine upper bound is
  `binom(n,k+1)`, agreeing with the endpoint construction.
- If the stated agreement threshold is below `k+1`, unexplained pairs
  necessarily have at least `k+1` agreements: puncturing to at most `k`
  coordinates is surjective. One may use `t_eff=max(t,k+1)`.
- For affine lines, if one coefficient fails membership on an agreement
  support then the direction fails there too: the equality
  `f_0+zf_1=c` implies `f_0` is in the punctured code whenever `f_1`
  is. This recovers Jo's bad-support criterion exactly.
- The bound counts codewords, not polynomial representatives. For RS,
  dimensions are defined by degree strictly less than `k`, so the two
  descriptions coincide.
- No square-root or unique-decoding hypothesis is used. The estimate
  can be exponentially large and does not resolve the fixed-gap linear
  MCA question.

For computation, successive ratios satisfy

\[
\frac{\binom n{b+1}/\binom{t-1}b}
     {\binom nb/\binom{t-1}{b-1}}
=\frac{b(n-b)}{(b+1)(t-b)}.
\]

The envelope decreases while `b(n-t+1)<=t` and increases afterwards;
an equality gives adjacent minimizers. Retaining the finite minimum in
the theorem avoids rounding conventions at such ties.

## Source verification

I checked the primary-source page and the locally downloaded PDF text
`research/puncturing_improvement/jo1432_source.txt`, lines 499--625.
[Sunghyeon Jo, *Reed–Solomon Mutual Correlated Agreement Beyond the
Johnson Radius*, ePrint 2026/1432](https://eprint.iacr.org/2026/1432)
states rejection abundance as Lemma 4.1, including sharpness, and the
affine envelope as Theorem 4.2. Its proof chooses one witness per bad
parameter and charges local tests. The uniqueness argument above permits
charging all witness pairs; quotient-polynomial root counting supplies
the curve-degree factor. These are direct extensions of that published
counting argument. The local source includes the August 19, 2026 revision.
