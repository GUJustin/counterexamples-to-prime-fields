# Common anchors for a complete subgroup coset of the nearest orbit

September 19, 2026. Exact elementary obstruction to one shortening
mechanism. It does NOT exclude arbitrary non-subgroup retained subsets
of the nearest orbit. No search, positive construction, or manuscript
edit was performed.

The current shortening target is to retain a growing, ideally linear,
subbank of the true-nearest orbit while imposing about `4r/5` common
agreement anchors. This note rules out retaining a complete subgroup
coset of linear size along the actual prime-selection sequence. It
also gives the exact residue decomposition for subgroup-stable anchors.

## 1. General orbit lemma

Let a field contain `4r` distinct roots of unity. On `D=mu_(4r)` let

    W_r(X)=(1+X^(2r))/2-X^r.

Let `deg V<r`, and assume its orbit `{V(zeta X):zeta in mu_r}` has
exactly `r` distinct polynomials. Let `S<=mu_r` have order `h>1`, and
retain every rotation in one coset `aS`, with `a in mu_r`.

Then the number of coordinates at which ALL retained polynomials
agree with `W_r` is at most

    r-h.                                                   (1)

This bound does not require nearestness or any information about the
other agreement coordinates.

Proof. Replace `V` by `U(X)=V(aX)`. The maximal common agreement set is

    C={x in D: U(sx)=W_r(x) for every s in S}.

Since `W_r(tx)=W_r(x)` for `t in S`, multiplication by `S` preserves
`C`. Its orbits on `D` all have size `h`, so `|C|` is a multiple of `h`.
For any `s in S` other than one, `U(sX)-U(X)` is nonzero: otherwise
the original full orbit would have a nontrivial stabilizer. This
difference has degree at most `r-1` and vanishes on `C`. Hence
`|C|<=r-1`. The largest multiple of `h` below `r` is `r-h`, proving (1).

Any prescribed common anchor set is a subset of `C`, so the same bound
applies whether or not that prescribed set was initially `S`-stable.
It also applies if a larger retained family merely CONTAINS the
complete coset `aS`.

## 2. Exact residue decomposition

Write `q=r/h` and decompose

    U(X)=sum_(j=0)^(h-1) X^j U_j(X^h), deg U_j<q.

Let `A` be an `S`-stable common anchor set, let
`B={x^h:x in A} subset mu_(4q)`, and put

    ell=|B|=|A|/h, Lambda_B(Y)=product_(b in B)(Y-b).

For any fixed `y in B`, evaluating on its full `h`-point fiber gives
`U(sx)=W_r(x)` for every `s in S`. Independence of the `h` characters
of `S` yields

    U_0(y)=W_q(y),
    U_j(y)=0 for every 1<=j<h.

Consequently

    Lambda_B divides U_j for all 1<=j<h.                   (2)

At least one such `U_j` is nonzero, since otherwise `U` would be
`S`-invariant. Since `deg U_j<q`, (2) forces `ell<=q-1`, recovering
`|A|<=r-h`. When equality holds, every nonzero component has the form
`U_j=c_j Lambda_B`, while `U_0` interpolates the `q-1` required word
values. Thus this argument does not secretly prohibit the lower-index
normal forms that remain algebraically possible.

For example, the hypothetical choice `h=r/5` and four complete anchor
fibers is not excluded by (1): it gives exactly `4r/5` anchors and the
displayed extremal residue form. Existence of a true-nearest polynomial
with the required additional matches would still need a separate proof.

## 3. Consequence for the actual rough-r sequence

The source construction in `appendix.tex` chooses primes with

    p=9 mod 16, p=-1 mod B_R,

where `B_R` is the product of odd primes at most `R`, and takes a
descended orbit length `r>R` dividing `(p-1)/4`. Hence

    v_2(r)<=1,
    every odd prime factor of r exceeds R.

Fix `c>0`. If `h>=c r`, then the index `q=r/h` is at most `1/c`.
For `R>1/c`, it cannot have any odd prime factor, and its 2-adic
valuation is at most one. Therefore `q` is either one or two.

For `q=1`, (1) gives no common anchors. For `q=2`, it gives at most
`r/2` common anchors. Thus along this sequence a retained complete
subgroup coset of any fixed positive relative size cannot supply the
approximately `4r/5` anchors needed by the proposed shortening.

In particular the tempting index-five residue construction is not
available in this prime-selection sequence once `R>=5`.

## 4. Precise remaining gap

An arbitrary set of `Theta(r)` rotations need not contain a complete
coset of a subgroup of order `Theta(r)`. Merely having many pairwise
ratios in `S`, or generating `S`, does not make its common agreement
set `S`-invariant. Neither the closure argument nor (2) has been proved
for such an arbitrary retained set.

This note therefore does not close the unknown-nearest-orbit shortening
target. It imports no Fourier estimate for the explicit Dickson bank,
and does not identify the unknown nearest polynomial with that bank.

## 5. Exact coset caps for arbitrary retained rotation sets

The following necessary conditions do not assume that the retained
rotations form a subgroup or coset. Write the four `mu_r`-cosets as
`D_j={x:x^r=alpha_j}` and let `w_j` be the value of `W_r` there. For
the fixed nonconstant polynomial `V`, put

    b_j=|{x in D_j:V(x)=w_j}|, m=sum_j b_j.

For every two distinct cosets,

    b_j+b_k<=r.                                           (3)

Indeed, interpolate their two word values by a polynomial
`L_jk(Y)` of degree at most one, with
`L_jk(alpha_j)=w_j`, `L_jk(alpha_k)=w_k`. The polynomial
`V(X)-L_jk(X^r)` is nonzero and has degree at most `r`. If `L_jk`
is nonconstant, the degree mismatch proves nonvanishing; if it is
constant, nonconstancy of `V` does. Its roots include every agreement
in these two cosets, proving (3). Thus this proof also works if two
word values coincide, provided `V` is nonconstant.

Summing (3) over the three other cosets gives

    m+2b_j<=3r,  hence b_j<=(3r-m)/2.                     (4)

For the true-nearest source `m>=3r/2`, every `b_j<=3r/4`.
Consequently `4r/5` common anchors cannot all lie in one quartic coset.
The pair inequality is stronger information than this last consequence.
It is characteristic-independent once the specified domain has distinct
roots and the word is defined. It uses neither the explicit Dickson bank
nor a bound on its Fourier coefficients.

## 6. Exact shortened-subbank inequality

Let `S subset mu_r` be ANY set of `L>=2` retained rotations. Let `A_j`
be their common anchors in `D_j`, put `a_j=|A_j|`, and set

    t=sum_j a_j.

Common anchors of two distinct degree-`<r` polynomials give `t<=r-1`.
Shorten all retained polynomials on these anchors: subtract their common
interpolant and divide by the anchor locator. The resulting `L` distinct
polynomials have degree at most

    D'=r-1-t.

Rotation preserves every `D_j` and its word value, so every retained
polynomial has exactly `b_j` agreements in that coset before shortening,
and exactly `b_j-a_j` afterwards. For any nonempty subset `J` of the
four cosets, define

    N_J=|J|r-sum_(j in J) a_j,
    M_J=sum_(j in J)(b_j-a_j).

Then

    L [M_J^2-N_J D'] <= N_J [M_J-D'].                     (5)

Proof. On these `N_J` retained coordinates let `c_x` be the number of
shortened candidates matching the shortened word. Then
`sum_x c_x=L M_J`. Distinct candidate differences have at most `D'`
roots, so `sum_x binom(c_x,2)<=binom(L,2)D'`. Combining this with
`sum_x c_x^2 >= L^2 M_J^2/N_J` gives (5). No sign assumption on either
bracket in (5) is needed.

This is the ordinary pair-count/Johnson inequality applied to each
coset union AFTER shortening, not a new list-decoding theorem. It is
valid in arbitrary characteristic and for arbitrary `S`; full orbit
size supplies distinctness, while nearestness is needed only for the
known lower bound on `m`.

For growing `L`, write `t/r -> tau` and `m/r -> mu` along any convergent
subsequence. The full four-coset choice in (5) gives

    (mu-tau)^2 <= (4-tau)(1-tau).                         (6)

At the proposed `tau=4/5`, this requires `mu<=8/5`. Thus a growing
subbank surviving this shortening can only come from the narrower
nearest-agreement window

    3/2 <= m/r <= 8/5+o(1),

not the whole currently allowed interval through `5/3`. More generally,
`m/r>=3/2` forces `tau<=7/8+o(1)` for a growing shortened subbank.

## 7. These conditions still leave the required small positive density open

There is no contradiction in the following normalized resource ledger:

    a_j/r=1/5, b_j/r=3/8 for each of the four cosets,
    t/r=4/5, m/r=3/2, L/r=1/9.

This is a numerical feasibility check, NOT an incidence realization.
For a union of `q` cosets, `1<=q<=4`, the limiting left comparison in
(5) is

    (M_J/r)^2=(7q/40)^2,
    (N_J/r)(D'/r)=(4q/5)(1/5).

The required inequality is strict because `49q<256` for all these `q`.
Every pair also satisfies (3) strictly, since its normalized agreement
sum is `3/4<1`. Integer rounding does not remove these fixed slacks.

The elementary span bound is likewise compatible with this ledger:
the span of the `L-1` rotation differences has dimension at most
`r-t`, since all are divisible by the anchor locator; here
`L-1~r/9<r/5~r-t`. No assertion that arbitrary rotations are linearly
independent is used or justified.

Product-set expansion can impose further conditions, but its even-`r`
case has a possible index-two stabilizer and must not be replaced by
a uniform prime-cyclic Fourier or sumset estimate. No Kneser-based
quantitative exclusion is claimed here. In particular, (3)--(6) do
not rule out the linear-size `r/9` subbank at the target shortening,
and do not construct one. Arbitrary dense non-subgroup retention remains
the substantive unresolved step.
