# M31 degree-five challenges on a selected symmetric circle space

2026-09-18. **Proved finite existence statement for the code defined here.**
It extends the challenge-field degree covered by the circle construction;
it does **not** increase the capacity margin of the preceding finite
examples. The exact verifier is `verify.py`, with output `receipt.json`.

Let `p=2^31-1`, `E=F_(p^5)`, and

\[
 T=\{z\in\mathbb F_{p^2}^*:z^{p+1}=1\}.
\]

There is a selected 262144-point domain `D subset T` and a circle code
over `E` of dimension **131071**, defined below, with two words whose
individual and common agreements are exactly **132094**. Every nonzero
label in `E` has exact pencil agreement **133118**. The source-to-near
gap is1024 and the capacity margin is `2047/262144`.

No identification with the dimension-131072 code of a Circle-STARK
implementation is asserted. The tag set and domain are existential,
rather than an explicit prescribed FFT domain. This is a finite-field
coding statement, not a protocol or security claim.

## The circle code is defined over the degree-five field

Choose `i^2=-1` in `K=F_(p^2)`, and use the compositum `E(i)=F_(p^10)`
only to express Laurent polynomials. For `L=65535`, define `C_L(E)` as
the `E`-span on `D` of

\[
 1,\quad z^j+z^{-j},\quad (z^j-z^{-j})/i,
       \qquad 1\le j\le L. \tag{1}
\]

All displayed basis functions take values in `Fp` on `T`: Frobenius
sends `z` to `z^-1` and `i` to `-i`. Thus this is an `E`-valued code
without embedding `K` in `E`. Multiplication by `z^L` bounds the zeros
of a nonzero function in (1) by `2L`; since `|D|>2L`, its dimension is
exactly `2L+1=131071`. The source polynomials below use only the
inversion-symmetric coordinate `X=z+z^-1`, but witnesses are compared
against the **entire** code (1), including its sine modes.

## A uniform mixed character estimate

Let `b in E` have degree five over `Fp`. For every nontrivial character
`chi` of `E*` and every character `psi` of `T`,

\[
 \left|\sum_{a\in T}\chi\bigl(b-(a+a^{-1})\bigr)\psi(a)\right|
       \le10\sqrt p. \tag{2}
\]

Use the rational parametrization `a=(t-i)/(t+i)` of the circle by
`P1(Fp)`. The map `a -> a+a^-1` is defined over `Fp` and has degree two,
with branch values `+2,-2`. The five conjugates of `b` are distinct and
avoid these two values. Consequently the pulled-back Lang character
has ten distinct simple zero punctures, two over each conjugate of `b`.
Its only other possible punctures are the two geometric circle points
`a=0,infinity`; the circle character twist can also ramify only there.
The point `t=infinity`, corresponding to `a=1`, is regular with value
`chi(b-2)`.

The rank-one Lang-sheaf construction is the one used in
[Katz, *An Estimate for Character Sums*, proof of Theorem2,
pp.198--199](https://web.math.princeton.edu/~nmk/old/estcharsums.pdf),
pulled back along this rational map and tensored with the circle's Lang
character. It is tame. Each zero above a conjugate of `b` has nontrivial
local monodromy, since `chi` is nontrivial. Hence the sheaf is
geometrically nontrivial. On the projective line with at most12 actual
punctures, `H_c^0=H_c^2=0` and `dim H_c^1<=10`. The weight bound proves
(2) for every such `chi,psi`; there is no restriction on the order of
either character and no random-character assumption.

## Trace population and exact completion

Take `m=512` and `H=T^m`, so `|H|=2^22`. Averaging (2) over the512
characters annihilating `H` bounds the corresponding sum over `H` by
`10 sqrt(p)`. Its trace image

\[
 A=\{a+a^{-1}:a\in H\}\subset\mathbb F_p
\]

has size `2^21+1`. All traces have two inverse preimages except `+2,-2`,
which have one each. Thus, for the regular traces,

\[
 \left|\sum_{v\in A\setminus\{2,-2\}}\chi(b-v)\right|
       \le 5\sqrt p+1.
\]

Choose any one regular tag `a0` and reserve it. The population
`{b-v:v in A\{2,-2,a0}}` has

\[
 P=2^{21}-2,\qquad
 \varepsilon\le\frac{5\sqrt p+2}{P}<\frac{231707}{P}.
\]

The exact fixed-weight completion lemma in
`../fixed_weight_completion.tex` passes with final `s=255`, `r=129`,
and `t=22` pairs. The seed uses211 tags and107-element products. Using
the exact overlap sum gives `log2(h0)<-23.3093`; after22 steps,

\[
 (p^5-1)h_{22}<0.003713<1.
\]

The verifier uses rational arithmetic and upward rounding on a
`2^-320` grid; the decision is an integer inequality. It also certifies
M31 primality by Lucas--Lehmer. Thus there exists a255-element regular
tag set `G`, disjoint from `a0`, whose exact129-element products
`prod_(v in S)(b-v)` cover `E*`.

## Exact agreement and source bounds

Put

\[
 Y=z^{512}+z^{-512}=C_{512}(X),\qquad X=z+z^{-1},
\]

where `C512` is the monic degree512 trace polynomial. Each regular
tag fiber in `T` has1024 points. Let `D` be the union of the256 fibers
with tags in `G union {a0}`. Choose `z0` in the reserved fiber, put
`x0=z0+z0^-1 in Fp`, and set

\[
 R(X)=\frac{C_{512}(X)-a_0}{X-x_0}.
\]

This is a monic degree511 polynomial in `X`, hence of Laurent degree511.
Its1022 distinct roots on `T` are precisely the reserved fiber minus
`z0,z0^-1`. The excluded branch tags ensure all these fibers and roots
are simple.

Define the `E`-valued words

\[
 f=R\frac{Y^{129}-b^{129}}{Y-b},\qquad
 g=-\frac{R}{Y-b}.
\]

The denominator never vanishes on `T`, since `Y` is in `Fp`. For a
129-subset `S` of `G`, write `V_S(Y)=prod_(v in S)(Y-v)` and
`P_S(Y)=Y^129-V_S(Y)`. At label `lambda=-V_S(b)`, the witness

\[
 h_S=R\frac{P_S(Y)-P_S(b)}{Y-b}
\]

has Laurent degree at most `511+127*512=65535` and is in (1).
Its residual is `R V_S(Y)/(Y-b)`, with exactly
`1022+129*1024=133118` zeros on `D`. Coverage supplies all nonzero
labels in `E`.

For every witness in (1), clearing `Y-b` from the pencil residual leaves
a nonzero Laurent polynomial of degree exactly `129*512+511=66559`:
the extreme leading terms of `R Y^129` cannot cancel. Multiplying by
`z^66559` gives an ordinary polynomial of degree133118, proving the
matching upper bound for **all** witnesses.

The source/common lower bound uses any128-subset of `G` exactly as in
the quotient compiler: subtract its monic locator times `R` from `f`,
and use `R(V_A(Y)/V_A(b)-1)/(Y-b)` for `g`. Their common match set has
`1022+128*1024=132094` points. The source `f` has Laurent degree66047,
so no degree65535 witness can agree more often than132094. Clearing
the denominator for `g` gives a nonzero Laurent polynomial of degree
at most66047, proving the same bound. It is nonzero because `Y-b`
has Laurent width1024 whereas `R` has width1022, so it cannot divide
`R` in the Laurent polynomial ring. Both individual agreements and
common agreement are therefore exactly132094.

## Why increasing the fiber size cannot enlarge this margin

This compiler has regular fiber size `F=2m`, fixed core of size `2w`,
and code dimension `J=2((r-2)m+w)+1`. Its near agreement satisfies

\[
 T=J+2F-1.
\]

Since `|T_circle|=2^31`, the power-fiber choices are powers of two.
The current `F=1024` gives capacity margin `2047/n`. At the next
choice `F=2048`, the fixed length `n=262144` contains at most128 complete
fibers. Even allowing **all** subsets of those128 fibers and omitting
the reserved-fiber requirement produces at most `2^128` canonical
supports, fewer than `p^5-1>2^154` labels. Larger fibers only decrease
this upper bound. Thus increasing `m` cannot give all native labels
with a larger margin in this fixed-core, complete-fiber one-pole model.

This agrees with the independently developed base-fiber counting gate,
with effective fiber `F=2m`. It does not bound arbitrary circle-code
witnesses, partial-fiber constructions, varying cores, or a different
coefficient-cancellation mechanism. Such a change is necessary for this
route to produce the larger capacity margin sought by the user.
