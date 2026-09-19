# The binary two-head hash, and what it does not transfer

September 18, 2026. Read-only source audit of
`/Users/jthaler/Documents/binary_field_counterexamples/sections/constructions/quadratic-near-johnson.tex`
and `research/frontier/native-near-johnson.tex`, after reading that
repository's `AGENTS.md` and research strategy. The existing uniform
characteristic transfer in `LOCATORS_TREES_NORMS_TRANSFER.md` is not a new
result here. No binary-repository file was modified.

## 1. The exact binary encoding

On a binary additive domain of size `N=16K`, a codimension-two subspace
has locator

```
L_W = X^(4K) + a_W X^(2K) + b_W X^K + V_W,
deg V_W <= K/2.
```

The identity in the source is

```
L_W² + (a_W²+theta)L_W
 = X^(8K) + theta X^(4K)
   + (a_W³+b_W²+theta a_W)X^(2K)
   + (a_W²+theta)(b_W X^K+V_W) + V_W².
```

Dividing the last two terms by `X` supplies a strict degree-`<K`
witness. If `theta` lies outside the domain field, the affine hash
`a³+b²+theta a` determines `a` and then `b`, since squaring is injective
in characteristic two. Equal `a,b` force equal locators: their difference
has degree at most `K/2`, whereas two codimension-two subspaces intersect
in at least `K` points. The number of labels is
`(N−1)(N−2)/6`.

These are separate ingredients: sparse locator existence, an algebraic
compiler identity, coefficient-pair injection, and label encoding. The
last ingredient alone is easy over a sufficiently large prime alphabet.

## 2. Exact odd-characteristic hash lemma

**Lemma.** Let `S` be a set of `M` distinct pairs `(a,b)` in `Fp²`, with
`p` odd, and define

```
h_theta(a,b) = a³+b²+theta a,  theta in Fp.
```

Let `R` be the number of distinct pairs `(a,b²)` represented by `S`.
Then `ceil(M/2) <= R <= M`, and some `theta in Fp` satisfies

```
|h_theta(S)| >= ceil( p R / (p+R−1) ).               (1)
```

In particular, if `p>=M`, the image has at least `M/3` elements (and
hence certainly at least `M/4`). Thus this encoding loses only a
constant factor when the prime alphabet is at least the proposed bank
size. It does not require an external field element.

**Proof.** Two pairs define the same affine function of `theta` exactly
when their first coordinates agree and their second coordinates differ
by sign. Each such class has size at most two. Choose one representative
of each of the `R` distinct functions. For fixed `theta`, let `n_z(theta)`
be its output multiplicities and let `E_theta=sum_z n_z(theta)^2`.
Distinct affine functions agree at at most one `theta`. Counting ordered
pairs gives

```
sum_theta E_theta <= pR + R(R−1).
```

For some `theta`, therefore,
`E_theta <= R+R(R−1)/p`. Cauchy--Schwarz yields
`|h_theta(S)| >= R²/E_theta`, which proves (1), including its integer
rounding. Since (1) is increasing in `R`, using `R>=M/2` gives
`|h_theta(S)| >= pM/(2p+M−2) >= M/3` when `p>=M`.

**Scope.** This counts distinct labels. Selecting one sign representative
does not delete the other sign's polynomial from the code, so it does
not prove singleton lists. Nor does this argument supply the source
distance bound previously obtained by projecting onto an exterior
`theta` coefficient. Finally, a separate argument is still needed to
show that distinct supports give sufficiently many distinct coefficient
pairs. The lemma assumes that pair count; it does not manufacture it.

## 3. The literal sparse binary compiler has no odd-characteristic bank

Here is a precise obstruction for the unchanged identity, rather than
for every possible replacement. Work in any field of odd characteristic.
Let `K>=2`, and suppose the squarefree locator

```
L=X^(4K)+aX^(2K)+bX^K+V,
V(0)=0,  1<=deg V<=floor(K/2),
```

splits into `4K` distinct roots. For fixed `theta`, suppose

```
X^(8K−1)+theta X^(4K−1)+zX^(2K−1)
```

agrees with a polynomial `h` of degree `<K` on every nonzero root of
`L`. Then necessarily `a=b=z=0`. In particular, unchanged binary
sources cannot obtain even two distinct labels from these locators.

Indeed, `L` divides
`X^(8K)+theta X^(4K)+zX^(2K)−Xh`. Reducing modulo `L` gives

```
2ab X^(3K) + (b²−a³−theta a+z) X^(2K)
−(a²+theta)b X^K
+2a X^(2K)V + 2b X^K V + V²−(a²+theta)V−Xh.    (2)
```

Write `j=deg V>=1` and let `v_j!=0` be its leading coefficient. The
coefficient of `X^(2K+j)` in (2) is exactly `2a v_j`, so `a=0`.
The coefficient of `X^(K+j)` is then exactly `2b v_j`, so `b=0`.
The remaining coefficient of `X^(2K)` is `z`, so `z=0`. All coefficient
positions used are distinct from the remaining terms because
`j<=K/2` and `deg(Xh)<=K`.

The squarefree assumption ensures that divisibility follows from the
agreement set, including its root at zero. This proof does not assert
that locators with `a=b=0` are absent, only that the label population
collapses for this literal compiler. It does not cover modified sources,
larger witness spaces, coupled locator identities, or a different
denominator.

## 4. Current constructive checkpoint

The separately saved `quadratic_frobenius_core/density_quarter_puncturing.tex`
gives a positive strengthening of the existing extension-field route:
for every prime `p>=257`, length `(5p²−1)/2`, message dimension three,
source/common agreement `2p`, threshold `floor(11p/5)`, and exactly
`(p+1)(p²−1)` singleton affine-line labels, with one further list of
size `p+1`. Its loss/capacity ratio tends to `1/11` and its label count
is superlinear in length. The alphabet remains `Fp4` and the domain
uses the original `Fp2`-derived blocks.

No new prime-alphabet sparse locator family or coupled odd-characteristic
compiler is supplied by this audit. The unresolved task is the actual
locator/support identity, together with source farness and complete
witness control. Replacing `2` by `p` in the known additive compiler,
or citing (1) alone, does not resolve those tasks.
