# Increasing the dimension: common gap versus endpoint gaps

September 18, 2026. The proposed common-agreement strengthening passes.
The separate candidate is `dimension_shift_common_gap.tex`; no main
manuscript edits were made. It does **not** improve the certified
two-thirds gap for both endpoints.

## Exact dimension-shift ledger

Start from the quotient compiler at dimension
`J0=w+(r-2)m+1`, with `0<=w<m`. Its words remain unchanged, but decode
at dimension `J=J0+t`, where `0<=t<=m-2`. Then

```
A = w+(r-1)m = J+m-1-t
T = w+rm     = J+2m-1-t
agr_J(f) = CA_J(f,g) = A
A <= agr_J(g) <= J+m-1 = A+t
agr_J(f+lambda*g) = T for every lambda != 0.
```

The old simultaneous witnesses have degree at most `J0-1<J`, so they
still attain `A`. The monic polynomial `f` has degree `A>=J+1`, which
proves the matching individual and common upper bounds. For `g`, only
the cleared-denominator bound `deg(-R-(Y-b)h)<=J+m-1` is available;
it must not be replaced by `A`. For nonzero pencil labels, the existing
witnesses still attain `T`, and the monic cleared numerator has degree
`T>J+m-1`, proving exact agreement.

At the tested radius the resulting fractions of the capacity margin are

```
common-agreement deficit / eta = m/(2m-1-t)
f endpoint separation / eta   = m/(2m-1-t)
g guaranteed separation / eta = (m-t)/(2m-1-t).
```

The last fraction decreases with `t`, since its derivative is
`-(m-1)/(2m-1-t)^2`. Its largest certified value over this compiler
with `m>=2,t>=0` remains `2/3`, attained at `m=2,t=0`.
This is a limit of these bounds, not a proof that the actual agreement
of `g` always reaches the upper bound.

## Near-full common gap strictly below Elias

Fix `m>=2` and take `t=m-2`. For every sufficiently large prime
`p=1 mod m`, the tag population has size `(p-1)/m-1` and character
mean at most `(sqrt(p)+1)/((p-1)/m-1)`. The audited entropy-threshold
lemma applies with `s=ceil(C log p)` whenever `C>1/h(rho)`.
Set `n=m(s+1)`, `J=floor(rho n)`, and choose `r,w` by
`J-m+1=(r-2)m+w`. The exact ledger becomes

```
agr_J(f) = CA_J(f,g) = J+1
J+1 <= agr_J(g) <= J+m-1
T = J+m+1
eta = (m+1)/n
common deficit = m/n = [m/(m+1)] eta
both endpoints are outside the tested radius by at least
2/n = [2/(m+1)] eta.
```

Choose `1/h(rho)<C<(1+1/m)/h(rho)`. Then
`eta log p -> (1+1/m)/C > h(rho)`, proving a strict below-Elias
radius. Every non-endpoint affine mixture is exactly at that radius.
For every desired constant common-gap fraction less than one, a
sufficiently large **fixed** `m` gives that fraction. This quantifier
does not assert a uniform theorem with `m` growing with `p`.

The alphabet is exponential in length:
`log p=n/(mC)+O(1)`. The growing-fiber polynomial-alphabet theorem
does not inherit this improvement with a fixed `C>1/h(rho)`: sending
`m` to infinity closes the constant-width below-Elias interval.
At the further dimension shift `t=m-1`, the same algebra would give
`CA=J` and the entire capacity margin as common deficit, but its
leading Elias condition becomes `C<1/h(rho)`, incompatible with this
coverage lemma. The proposed `m=1` full-loss case has the same
constant-threshold obstruction.

## What this changes relative to the old paired theorem

The old completed paired construction already has an underlying
one-far line with `CA=K+1`, near agreement `K+2k+1`, and common deficit
fraction `2k/(2k+1)`. Thus a near-full common-agreement deficit below
Elias is already present in the manuscript; it is not new here.

For `m=2k`, its common-gap ledger is identical to this dimension-shift
ledger. Choosing `C=(m+4/5)/(m h(rho))` also matches its leading length
`n=((m+4/5)/h(rho)) log p` and its leading capacity-margin constant.
This `C` is strictly inside the allowed interval. The alphabet and
length comparison is therefore stronger than comparing unmatched
families, but no common-gap improvement follows at those parameters.

The distinction from that underlying one-far line is that its direction
is supported on `2k=m` coordinates and hence close to the zero
codeword, whereas the new `g` is far, at distance at least the tested
radius plus `2/n`. The existing paired **two-far** corollary already
has both endpoints far by `k/n` (for even `k`). That exceeds the new
guaranteed `2/n` when `k>2`, equals it for `k=2`, and also comes with
the larger affine-space profile and disjoint-list guarantees.
Its ordinary common agreement after the two-endpoint reparameterization
is not determined by the cited corollary, so no extra exact value or
dominance is inferred. No priority claim is made for either the
two-far pattern or the common-agreement phenomenon.
