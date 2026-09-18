# A bounded gate for partial X and Z prefixes

**Computed result:** at m115,D20846625,Q159,S35 the exact optimum is zero.
An independent integer-flow/cut replay passed. Therefore no source in the
monomial translation-stable class below has a positive sum-of-local-ranks
dimension certificate, for any challenge support or cap. The completed
all-m theorem still assumes full X and Z prefixes at other multiplicities;
this new result does not prove full prefixes are without loss of generality.

Work in characteristic zero or characteristic large enough that the stated
monomial translation closure is literal (in the benchmark all relevant
degrees are below the characteristic). Fix m,D,Q,S. Consider a monomial
space inside `x+wi+(w-1)j<D, i+j<=Q, j<=S`, with arbitrary finite challenge
support, stable under X translations and `Y -> Y+c+dZ`. Equivalently, impose
the monomial implications obtained by lowering x, and by replacing one Y
with 1 or Z. These are the closure properties used here; no claim is made
about arbitrary nonmonomial translation-invariant spaces.

## Challenge layers

Partition the source by `k=i+j+z`. In a fixed layer k, replacement of Y by Z
requires `(x,i,j) -> (x,i-1,j)`, with the Z exponent adjusted to preserve k.
Thus every layer is X- and Y-downward, with the extra bound i+j<=k.
At received value zero, the contact substitution `Y=tR+t^2E` preserves
total R,E,Z degree k. The local rank and source dimension therefore add
over these layers. Received translations give isomorphic maps on the full
space. Dropping the implications between different layers only enlarges
the optimization class. Consequently a nonpositive optimum for every
single X/Y-downward layer rules out a positive dimension test for every
allowed partial challenge support, at every L.

## Exact X compression

Set `H_ij=D-wi-(w-1)j`. In one layer, X-downward support specifies an integer
height `0<=h_ij<=H_ij`; Y closure requires `h_(i-1,j)>=h_ij`.
At zero received value a column X^xY^iR^j contributes to local extraction
only at `ell=x+i<m`. In particular every column with x>=m is in the local
kernel, including after imposing all lower-Y implications.

Whenever h_ij>=m, replace its height by H_ij. Perform this simultaneously
for every such pair. This preserves closure: its lower-Y neighbor already
has height at least m, is also completed, and has available height at least
H_ij. It leaves local rank unchanged and increases dimension. Thus an
optimum exists with

```
h_ij in {0,1,...,m-1,H_ij}       if H_ij>=m,
h_ij in {0,1,...,H_ij}          otherwise.
```

This compression is safe. The tempting smaller threshold x>=m-i is NOT
safe under Y closure: adding those locally free columns can force
rank-bearing columns at lower Y degrees.

Represent the height with indicators for x=0,...,min(m,H_ij)-1. Each has
coefficient benefit one, except x=m-1 (when present), whose benefit is
H_ij-m+1. This last indicator means the entire remaining prefix is present.
Implication edges decrease x or i. If a lower-Y neighbor is completed,
its larger available X bound causes no difficulty. These indicators and
edges represent exactly the completed-prefix class above.

## Rank and mincut

For each q and ell<m, let the selected indices be the i with
`(x=ell-i,i,j=q-i)` selected. Its rank is
`min(m-ell,number of selected indices)`, by the same Pascal minors as in
the full-prefix proof. A bulk-tail indicator is never substituted for a
missing rank-bearing column: all such x satisfy x<m and are individually
represented. The exact objective is total indicator benefits minus n
times the sum of these ranks.

Use one source edge per indicator with its benefit, infinite closure
edges, and one auxiliary node per (q,ell). Every relevant indicator has
an edge of capacity n to its block auxiliary; the auxiliary has sink
capacity n(m-ell). The previous mincut proof applies verbatim.

At the frozen old A shape m115,D20846625,Q159,S35, all H_ij exceed m.
There are 5130*115=589950 variable nodes, 10695 rank auxiliaries,
584820 X-closure edges, 585810 Y-closure edges, and 240120 rank-incidence
edges. Including source and auxiliary-sink edges gives 2011395 original
directed edges and 600647 nodes including source and sink. The single
64-bit bounded maxflow in `partial_prefix.cpp` completed in 16.82 seconds,
using 221728 KiB peak RSS. Maximum slope was zero, with flow=cut=
47859086760 and the empty support optimal. `verify_partial_prefix.py`
independently reconstructed every edge, checked capacities, conservation,
flow=cut, prefix closure and the rank formula; it passed in 1.68 seconds,
using 48576 KiB. Both jobs had 60-second/384-MiB guards. Receipts are
`partial_prefix.json`, `partial_prefix.verified.json`, and their resource
reports. The raw flow is reproducible from the generator, so its compressed
payload remains local rather than being committed.

Since its optimum is zero, the result closes all stated partial X/Z-prefix
dimension tests at m115, including every challenge cap. If positive, the
selected layer must be extended to a genuinely translation-stable full
source before claiming a feasible improvement: ignored cross-layer
implications need to be restored and their margin checked. Thus this
relaxation is immediately decisive in the negative direction, while a
positive value is only a constructive lead.
