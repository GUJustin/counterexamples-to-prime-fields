# Fixed witness-span counting gate: independent audit

September 18, 2026. **PASS.** This is a finite-field-independent polynomial incidence bound, not a protocol or general benchmark impossibility claim.

## Hypotheses and bound

Let D consist of N distinct field elements, and let V be a polynomial code containing an r-dimensional linear subspace U whose elements have degree at most d. Assume U has no common zero on D, T>d, and r+1<=N. For arbitrary received words f,g define ordinary common agreement

C = max over F,G in V of |{x in D: f(x)=F(x) and g(x)=G(x)}|.

Assume C<T. Count qualifying pairs (lambda,h), with lambda in the field, h in U, and agreement(f+lambda g,h)>=T. Then

    # qualifying pairs <= (N)_(r+1) / [T (T-d)^(r-1) (T-C)].

In particular this bounds distinct qualifying labels. For a single fixed received word w, with no line or common-agreement hypothesis, the analogous list bound is

    # {h in U: agreement(w,h)>=T} <= (N)_r / [T (T-d)^(r-1)].

Here (N)_j=N(N-1)...(N-j+1). These bounds also hold for an affine translate H+U contained in V, by subtracting H from the received word f (or w); this preserves the full-code common-agreement maximum.

## Independent proof

Choose a basis of U and use its evaluation vectors as rows. For a qualifying pair, its first matching coordinate has a nonzero row, giving at least T choices. After j<r independent matching rows have been selected, choose a nonzero polynomial in U annihilated by those j evaluations. Any coordinate whose row belongs to their span is a zero of this polynomial. There are at most d such domain points. Thus there are at least T-d matching choices extending the rank, at each of the next r-1 steps. This includes the exclusion of all already selected coordinates.

For each ordered independent r-tuple, its interpolation constraints define a unique affine pencil h_lambda=F+lambda G with F,G in U. A further coordinate contains this entire pencil precisely if f(x)=F(x) and g(x)=G(x). At most C coordinates do so. Therefore every qualifying pair supplies at least T(T-d)^(r-1)(T-C) ordered (r+1)-tuples that determine that pair uniquely. The last coordinate cannot be one of the first r, since those are universal for the pencil. Counting all distinct-coordinate tuples proves the line bound. Stopping at r coordinates proves the fixed-word bound.

This also covers g=0 and constant-pencil degeneracies: if a qualifying pair existed with a pencil universal on all its matches, its common agreement would violate C<T. No assumption that the line has nonzero direction is needed. The proof uses root counts, not characteristic-dependent derivatives.

For r=2, the rank-extension polynomial is explicitly h0(x_i)h1(X)-h1(x_i)h0(X). It is nonzero because the evaluation row at x_i is nonzero and h0,h1 are linearly independent. Its degree is at most d. Thus the proposed denominator T(T-d)(T-C), including the T first choices, is correct.

## Exact frozen numerical comparison

The archived mathematical target has N=262144, d=131071, T=139782 and required count 274980728111395088. The weakest permitted common-agreement hypothesis is C=T-1. Independent integer arithmetic gives:

- r=2 line bound = 3002365391929344 / 202940167, hence at most **14,794,337** qualifying pairs/labels.
- r=2 fixed-word list: at most **56** witnesses.
- r=8 line bound: at most **10,986,827,589,352,011** pairs/labels, below the required count.
- r=9 line bound: at most **330,620,141,216,254,116**, above that count, so this test alone does not exclude dimension nine.

The formulas increase with r in this numerical range. Consequently a witness span of dimension at least nine is necessary for this particular ordinary-common-agreement line target. This is only a necessary span condition, not an existence assertion. Exact reproducible arithmetic is in verify.py and verify.json. Benchmark constants are taken from the frozen local UPPER_TRACK_TRANSLATION_2026_09_18.md; this audit does not assert a freshly checked live benchmark.

## Compiler scope

A fixed injective linear polynomial composition or rational/GRS transformation, using a common nonvanishing denominator-clearing multiplier on the retained domain, preserves witness-span dimension. In particular a two-coefficient bank mapped to span(P^2,Q^2) remains two-dimensional when the images are independent; coprime P,Q ensure no common basepoint. The relevant d is the degree bound of its actual admissible polynomial representatives, not an un-cleared rational degree. Puncturing is harmless if these hypotheses remain valid. A common polynomial offset gives the affine-translate case above.

Thus increasing the degree of such a preserved two-dimensional bank cannot reach the displayed target while remaining inside degree 131071 and satisfying C<T. The fixed-word obstruction requires no CA hypothesis at all. Neither conclusion covers nonlinear/label-dependent compilers that enlarge the span, newly introduced witnesses outside U, constructions failing the CA premise, or arbitrary multirow certificates. In particular the number r is a polynomial witness-span dimension, not the number of protocol rows. No statement about practical security follows from this counting lemma.
