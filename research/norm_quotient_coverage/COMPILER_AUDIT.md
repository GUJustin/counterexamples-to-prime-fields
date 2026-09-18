# Native norm quotient compiler and matched comparison

September 18, 2026. Exact symbolic audit; `norm_quotient.tex` is integrated
as Theorem N.31 of the 263-page manuscript. This is a specialization of known quotient and
character-sum ingredients, not a priority claim. The elementary character
argument is in `CAUCHY_SUBSET_PRODUCT_LEMMA.md`.

## Exact degree and agreement ledger

Let `q=p^5`, `E=F_q`, `m=(q-1)/(p-1)`, and `N(X)=X^m`. Choose `b` of
degree five over `F_p`, a tag `a0 in F_p*`, and a core `B` of `w<m` points
inside the norm fiber `N^-1(a0)`. Put `R=L_B`. Use `r`-subsets `S` of
`F_p* \ {a0}`, and define

```
J = (r-2)m+w+1
A = (r-1)m+w = J+m-1
T = rm+w       = J+2m-1
f = R (N^r-b^r)/(N-b)
g = -R/(N-b)
V_S(Y) = product_(a in S) (Y-a)
P_S(Y) = Y^r-V_S(Y)
lambda_S = -V_S(b)
h_S = R [P_S(N)-P_S(b)]/(N-b).
```

* `f` is monic of degree `A`; `g` is defined at every point of `E`.
* `deg h_S <= (r-2)m+w=J-1`, preserving the strict degree convention.
* The residual is exactly `R V_S(N)/(N-b)`. Its zeros are exactly `B`
  and the `r` selected norm fibers: **exactly `T` canonical agreements**.
  The zero coordinate is in neither set and does not agree.
* `agr_J(f)=agr_J(g)=CA_J(f,g)=A` exactly. Upper bounds follow from
  the nonzero residual polynomials of degree at most `A`. Lower bounds
  come from simultaneously interpolating the two quotient-variable
  functions on `r-1` allowed tags, substituting `N`, and multiplying by
  `R`: both witnesses match on those full fibers and on `B`.
* The label is necessarily nonzero. If the subset products cover `E*`,
  every nonzero affine label is nearby and zero is far. The projective
  direction `g` is also far. Distinct labels need not have distinct
  witnesses; no such injectivity is used or needed.

For exact prescribed dimension `J=floor(rho q)`, divide `J-1` by `m` to
get the displayed `r,w`. For any fixed `0<rho<1`, `r/(p-2)->rho`, and
`2<=r<p-2` eventually. The tag deletion costs only one character-sum term.
With `theta=r/(p-2)`, the sufficient positivity condition is

```
log((p^5-2)(p-1)) < theta(1-theta)(p-4-4sqrt(p)).
```

This follows from Katz's affine-line bound after deleting `0,a0` and the
fixed-cardinality Cauchy estimate. Thus the exact-rate result applies to
**every sufficiently large prime**, without a congruence subsequence.

The manuscript states the same theorem for every fixed
extension degree `d>=2`: use `q=p^d`, choose `b` of exact degree `d`,
and replace `4sqrt(p)` by `(d-1)sqrt(p)` in the character criterion.
All compiler and exact-agreement formulas remain unchanged.

Without padding or tag deletion, take `w=0`, all `p-1` nonzero tags, and
`J=(r-2)m+1`. The positivity condition improves to

```
log((p^5-2)p) < theta(1-theta)(p-2-4sqrt(p)), theta=r/(p-1).
```

## What this does and does not improve

At the same full domain `E=F_(p^5)`, exact dimension `J=floor(rho q)`,
and native challenge space:

| Guarantee | Earlier five-dimensional locator theorem | Norm quotient theorem |
|---|---:|---:|
| nearby affine labels | at least `q-3`; sometimes all `q` | exactly `q-1` at the stated threshold |
| certified agreement | `J+floor((1-rho)p^3/2)` | `J+2m-1` |
| margin above capacity | `Theta(p^-2)` | `Theta(p^-1)` |
| direction agreement | exactly `J` | exactly `J+m-1` |
| common agreement | exactly `J` | exactly `J+m-1` |
| first-source guarantee | first source nearby | both sources far |
| source-to-near gap | `Theta(p^3)` | `m=Theta(p^4)` |

The norm construction improves both the capacity margin and the separation
between sources and nearby combinations; it supplies almost every label
and keeps both sources far. It does **not** preserve the older theorem's
exact common/source agreement `J`, nor its all-label conclusion on the
special prime subsequence. A claim of literal componentwise domination
would therefore be false. Whether the older exact deep-hole common
agreement warrants retaining its longer proof is an editorial decision.

The margin `Theta(p^-1)=Theta(q^-1/5)` is still asymptotically smaller
than the inverse-logarithmic margin in Krachun--Kazanin--Haboeck. The
almost-complete coverage is now obtained by an elementary finite-field
subset-product argument applied to that quotient mechanism; it should
not be described as requiring the new Grassmannian label calculation.

## Relation to primary Appendix A

Primary text inspected: Krachun--Kazanin--Haboeck, *Failure of proximity gaps
close to capacity*, ePrint 2026/782, Appendix A, printed pages 13--16;
the locally cached extraction has Appendix A at lines 635--802.

Theorem 1 and Proposition 4 as stated use a prime alphabet of size
`P=Theta(n^beta)`, `beta>12/5`, and a multiplicative domain of size `n`.
Proposition 4 certifies at least `P/(2n)` labels, a fraction `1/(2n)`, at
inverse-logarithmic capacity and source margins. This is a **lower bound**,
not an upper bound on the image of their construction. Its hypotheses do
not literally include `E=F_(p^5), n=p^5`.

The immediate quotient-variable generalization removes the purported
full-domain pole obstruction: choose `b` outside the image of `X^m`
directly. It need not have the form `z^m` for an element `z` outside the
evaluation domain. In particular, `X^m-b` is root-free on all of `E` in
the norm specialization, including at zero.

For a small subgroup `G` of size `s|q-1`, put `m=(q-1)/s` and use
`r`-subsets of `G`. The same unpadded compiler gives near agreement `rm`
and exact source/common agreement `(r-1)m` at dimension `(r-2)m+1`.
Let `L=binom(s,r)` and take `b` from `E \ (G union {0})`, of size
`Q=q-s-1`. Distinct polynomials `P_S` have degree at most `r-1`; their
differences have at most `r-1` roots. Collision averaging and Cauchy--Schwarz
give one such `b` with at least

```
L Q / [Q + (r-1)(L-1)]
```

distinct labels. If `s=Theta(log q)` and `L>>q`, this proves an
`Omega(1/log q)` fraction of labels and an inverse-logarithmic margin.
It does not prove an upper bound preventing almost-all labels. A sequence
of suitable `s` can reuse the paper's primes `p=Theta(n0^beta)`,
`p=1 mod n0`, choosing a power-of-two `s=Theta(log n0)` dividing `n0`.
Choose its entropy exponent above `5 beta` to make `L>>p^5`; the paper's
prime-existence step needs only `beta>12/5`. Its separate condition
`beta>tau+1` must not be retained when replacing its original label
separation argument.

Thus the precise unresolved comparison is whether the logarithmic-size
subset-product bank can cover almost all native labels at the same
inverse-logarithmic margin. Neither Appendix A's stated lower bound nor
the collision argument settles that question. The full-norm result above
proves almost-all coverage at the weaker but improved `Theta(q^-1/5)`
margin.

## Bounded verification

`verify_exact_rate_compiler.py` independently checks the padded compiler
on every point of `F_(5^5)=F_5[X]/(X^5-X-1)`. Six fixtures use
`r in {2,3}` and padding sizes `0,1,7`, with full norm-fiber counts,
strict witness degrees, simultaneous source/common attainment, exact
residuals, canonical support sizes, and the zero coordinate checked.
All pass in 3.61 seconds with peak RSS 14.4 MB. This fixture verifies the
identity and padding, not large-characteristic product surjectivity.

For exact half dimension `J=floor(p^5/2)`, the Euclidean division gives
`r=(p+1)/2`, `w=m-1`, and `theta=(p+1)/(2(p-2))`. The independent
character audit proves the positivity criterion for every odd prime
`p>=191`; see
`../astra_practical_2026_09_18/FIXED_CARDINALITY_CHARACTER_AUDIT.md`
and its rational onset certificate `verify_character_half_onset.json`.
