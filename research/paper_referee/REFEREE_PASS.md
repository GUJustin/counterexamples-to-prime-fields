# Mathematical referee pass on the canonical manuscript

Reviewed `paper.tex`, canonical repository manuscript, September 15, 2026.
Scope: headline general results, exact versus selected lists, field/domain
quantifiers, agreement counts, attribution as represented in the manuscript,
and the boundary between coding statements and protocol-security conclusions.
No protocol code was executed. This is an internal review, not external peer
review or an independent verification of every bibliography source.

## Conclusion

I found no mathematical counterexample to the headline statements during this
pass. The exact-profile proof, isolated-line construction, fixed-gap lift, and
puncturing argument retain their essential restrictions. Three small editorial
patches below make the claims more precise. None changes a numerical bound.

## Proposed exact patches

### 1. Keep the circle-list agreement count a certified lower bound

Theorem `thm:circle-finite-summary` correctly says **at least** `T` agreements
in both parts. Its proof subsequently says:

> Both choices give $K=n/2$ and the same agreement count $T=hB-2$.

Replace with:

```tex
Both choices give $K=n/2$ and the same certified agreement threshold
$T=hB-2$.
```

Reason: the real-list construction assigns the received word arbitrary values
at the two anchors, so individual list witnesses may have additional agreement
there. Its guaranteed off-anchor count is exactly `hB-2`; the total count is
at least that number. The headline theorem already gets this distinction right.

For further clarity, in `rl:list` replace:

```tex
Thus agreement holds exactly on the selected $h$ fibers, except for the two
discarded anchors. The map $u\mapsto u^B$ has fibers of size $B$ on $D$, so
there are $hB-2$ certified agreements.
```

with:

```tex
Among the nonanchor coordinates, agreement holds exactly on the selected
$h$ fibers. The map $u\mapsto u^B$ has fibers of size $B$ on $D$, so
there are exactly $hB-2$ nonanchor agreements, and at least this many
agreements on the full domain.
```

This makes the already intended qualification explicit. The separate reserve
pencil has removable anchor values; its common-core expression supports its
stronger exact count because the remaining factors are nonzero at the anchors.
The real-list caveat should not be propagated indiscriminately to every exact
count in the manuscript.

### 2. Narrow the root-bound sentence

In the security section, replace:

```tex
It does not bound how many codewords can lie
near an arbitrary received word beyond the unique-decoding radius.
```

with:

```tex
It does not by itself establish the proposed quantitative list bound
beyond the unique-decoding radius.
```

Reason: pairwise agreement bounds can be combined with incidence counting to
prove Johnson-type list bounds beyond unique decoding. The current sentence
can be read as denying such consequences of the root bound. The narrower
sentence says precisely what the surrounding argument needs.

### 3. Correct the finite-example forward reference

Immediately following the first length-64 finite example, replace:

```tex
Proposition~\ref{prop:conditional-moments} below strengthens this to
$L\ge5074503250115>2^{42}$ by Proposition~\ref{prop:polynomial-moment-weights}.
```

with:

```tex
The conditional-moment method below, sharpened by
Proposition~\ref{prop:polynomial-moment-weights}, strengthens this to
$L\ge5074503250115>2^{42}$.
```

The original syntax attributes the strongest number to two different
propositions. The number is the polynomial-weight certificate.

## Quantifiers checked

- The interval theorem fixes a rational rate, lets the gap decrease, and lets
  the prime grow. Its exact agreement count is justified by the root polynomial
  having precisely its chosen subset as roots on the domain.
- The fixed-gap lift preserves a selected finite list. It neither asserts a
  constant global maximum list nor excludes correlated agreement. The manuscript
  explicitly states both qualifications.
- The actual-list separation uses generic domains over very large primes,
  has gap `1/n`, and has exactly `binom(n,k+1)` nearby parameters. The distinct
  subset-sum requirement gives uniqueness of the nearby witness at each such
  parameter. The concurrency count is `n-k`, not `n-k-1`; the latter is the
  global maximum list size. These quantities are not conflated in the theorem.
- The profile extension uses column distance for interleaving. Full-rank
  minors persist over field extensions, and the proof uses them componentwise.
- The puncturing proof counts witness pairs, not merely parameters. Punctured
  unique decoding makes the per-puncture count a witness count, and the protected
  `(k+1)`-set proof treats entire unexplained agreement supports.
- The polynomial-curve extension keeps the degree factor `e`; its root-count
  argument does not require `e < |F|`. If `e` is large, the bound can simply
  become vacuous. The `e=0` case is correctly separated.
- Attribution now identifies the generic upper bound as published work and
  explains how Roth supplies the fixed-rate lower bound. The explicit finite
  lower construction makes no priority claim.
- The security section separates a coding event from verifier acceptance and
  names challenge order, fields, and Fiat--Shamir as additional requirements.
  It does not establish an improved better.codes certificate or a Stwo security
  level. These restrictions should survive any merge from the separate draft.

## Coordination warning

The reported 32-page draft is a separate manuscript. Its agreement-count fix
should be merged by formula and theorem, not by page count or a blanket change
from “exactly” to “at least.” Most interval and isolated-line exact counts in
the canonical manuscript have direct root-set proofs and should remain exact.
