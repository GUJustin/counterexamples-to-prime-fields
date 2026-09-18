# Primary A: all multiplicities and all challenge caps

**Result: every one of the 194 exact maximum slopes is zero.** All 194
integer flow/cut certificates passed the independent replay. Consequently
no multiplicity m>=1 and no challenge cap L gives a positive local-rank
dimension certificate in the support class below. This is not a benchmark
improvement; it closes the proposed restoration of the old A jet caps by
optimizing downward monomial supports.

Parameters are n=262144, w=131071, A=181275. The jet support lies in
`i+j<=159, j<=35` and is downward closed in i. For multiplicity m>=1,
put D=mA. Each selected jet monomial has its full X prefix
`0<=x<D-wi-(w-1)j`, and, at challenge cap L, its full Z prefix
`0<=z<=L-i-j`. Omit monomials with empty prefixes. Characteristic greater
than 159 suffices for the Pascal minors used below.

The certificate family in `all_m_certificates` decides the coefficient-
dimension minus the sum of local ranks test for this entire class. It does
not assert that a nonpositive dimension test means the actual interpolation
kernel is zero. In particular it does not rule out dependencies between
different coordinate conditions, nor supports without these prefix and
closure conditions.

## Exact local rank, including unsaturated diagonals

Let S be an available jet support and write
`c(q,ell)=#{(i,j) in S:i+j=q, i<=ell}`. At zero received value, the homogeneous
jet block q and t degree ell is available exactly when
`ell+(w-1)q<D`. Indeed its source X exponent is ell-i, and its weighted
degree is ell+(w-1)q, independent of i. The substitution
`Y=tR+t^2E` gives a truncated Pascal matrix; distinct allowed i give rank
`min(m-ell,c(q,ell))`. This is the usual Vandermonde minor argument and does
not require the allowed i to be consecutive. Hence

```
R_m(S)=sum_q sum_{0<=ell<m, ell+(w-1)q<D}
                    min(m-ell,c(q,ell)).
G_m(S)=sum_(i,j in S)(D-wi-(w-1)j)-n R_m(S).
```

Translations by the affine received symbol preserve the source because it
is Y-downward, has full X prefixes, and has the joint Y,R,Z cap. They are
invertible and preserve the target contact filtration. Thus this is also
the exact local rank at every received symbol. The same argument gives a
factor L-q+1 on block q when challenge coefficients are included.

## One unweighted test settles every L

Write g_q for the contribution of diagonal q to G_m. The actual dimension
margin is

```
sum_{q<=L}(L-q+1)g_q(S)
   = sum_{t=0}^L G_m(S intersect {i+j<=t}).
```

Every prefix on the right is still an allowed downward support. Therefore
if max_S G_m(S)=0, no L admits a positive dimension margin. Conversely a
positive G_m(S) gives a positive margin at sufficiently large L. This is an
exact equivalence for existence of a positive dimension certificate.

## Only multiplicities 1 through 194 are needed

For m>=194 every one of the 5130 jet columns is available, and every
ell<m on every diagonal is available: `D-(w-1)*159>=m`. Fix a diagonal q
with k selected distinct indices i_1,...,i_k. If `m>=q+k-1`, direct summation
gives

```
sum_{ell=0}^{m-1} min(m-ell,#{i_s<=ell})
       = k*m - sum_s i_s - k*(k-1)/2.
```

To see this, without the minimum the sum is `km-sum i_s`; the only
truncation occurs in the final k-1 rows, after all selected indices have
entered, and subtracts 1+...+(k-1). Since q<=159 and k<=36,
`q+k-1<=194`. Thus for every fixed nonempty support, for all m>=194,

```
G_(m+1)(S)-G_m(S)=(A-n)|S|<0.
```

There are no new columns beyond this endpoint. Maximum slope zero at
m194 therefore rules out every larger m.

## Exact primal-dual certificates

The generator `all_m_slope.cpp` uses a source edge of capacity
`D-wi-(w-1)j` for each jet variable. Infinite-capacity closure edges enforce
Y-downward selection (capacity sum of benefits plus one suffices). For
each available (q,ell) block an auxiliary node receives capacity n from
each selected variable and has sink capacity `n(m-ell)`. Minimizing its
side of the cut contributes exactly `n min(m-ell,c(q,ell))`. Therefore
minimum cut equals total benefits minus maximum G_m.

`verify_all_m.py` independently reconstructs every edge, checks sparse
integer flow capacities and conservation, verifies flow=cut, and computes
the chosen support's rank directly. It invokes no flow optimizer. Binary
flow records are little-endian uint32 edge index followed by int64 amount.
They are stored as deterministic gzip files; the checker transparently
reads compressed or raw files. `flow_manifest.json` records raw and gzip
SHA-256 hashes. The parameterwise JSON receipts and the three
`verified_*` replay summaries contain the results. Optimization batches
took 1.07, 5.35, and 9.62 seconds; independent replay batches took 0.54,
2.67, and 5.87 seconds. All runs stayed below 384 MiB. Compressed flow
certificates total 72,276,108 bytes (420,618,516 bytes before compression).

## Interface scope

A positive supported-subspace certificate would imply positivity for the
full source kernel; one must keep that full kernel for the existing
universal-divisor and own-system arguments. At arbitrary m the jet cap159
must be explicit: a weighted degree cap alone can admit higher jet degrees.
The negative result here applies even with that explicit additive cap,
and is a statement about the exact local-rank dimension test, not all
possible primary-source constructions.
