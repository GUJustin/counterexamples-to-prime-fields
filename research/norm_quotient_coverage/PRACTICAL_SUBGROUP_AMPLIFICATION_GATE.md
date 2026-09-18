# Practical subgroup amplification: applicability audit and an exact moment gate

Date: 2026-09-18. Scope: pure finite-field mathematics, no protocol claim.

**Result.** The bounded primary-literature audit did not identify a theorem
giving a uniform bound below 262144 for

\[
 S_\chi=\sum_{a\in D}\chi(b-a),\qquad
 p=2130706433,\quad E=\mathbb F_{p^6},\quad
 D=\mu_{262144}\subset\mathbb F_p^*,\quad [\mathbb F_p(b):\mathbb F_p]=6.
\]

There is, however, a concrete additional analytic gate: a uniform normalized
tenth Mellin moment at most **130**, or a twelfth moment at most **4182**,
would imply both a nontrivial character bound and fixed-cardinality product
coverage at cardinality 139782. These moment bounds are **not proved here**.
The constants below distinguish this gate from an assumption of random
phases. General Mellin equidistribution does not certify it at this prime.

No computation over characters, subgroup enumeration, or resource rental
was performed. The accompanying small arithmetic verifier is
`verify_practical_subgroup_amplification.py`; its receipt is
`practical_subgroup_amplification.json`.

## What the primary results actually cover

| Primary source | Applicable statement and limitation here |
| --- | --- |
| [Ostafe--Shparlinski--Voloch, *Weil Sums over Small Subgroups*, Theorem 1.1](https://arxiv.org/html/2211.07739) | Bounds additive sums `sum_D e_p(f(a))` for a polynomial over the prime field. Its character type is different from `chi_E(b-a)`. The result cannot be substituted for a multiplicative-character bound. |
| [Chang--Shparlinski, *Double Character Sums over Subgroups and Intervals*, Theorems 1--3 and Section 4](https://math.ucr.edu/~mcc/paper/151%20CharSums-InterGroup.pdf) | Averages a base-field multiplicative character over both a subgroup and an interval. The interval must have a positive-power length in the stated ranges; setting its length to one does not recover a theorem for the present sum. The multiplicative variant in Section 4 still has this second averaging variable. |
| [Rojas-Leon, *Estimates for exponential sums with a large automorphism group*, Section 5](https://arxiv.org/html/1010.0120) | Sums over all elements of an extension field, with a character pulled back by the norm and a homothety-invariant polynomial. Our variable ranges over a subgroup of the base field and our character of `E*` is arbitrary. Neither the summation domain nor the character hypothesis matches. |
| [Xi, *Equidistributions of Jacobi sums*, Theorems 1.1, 1.4, 1.5](https://arxiv.org/html/1809.04286) | The single-character result averages over the full character group. Its restricted-family theorem averages two character variables and requires one family of size at least `sqrt(p)`. The present 8128 twists have size below `sqrt(p)=46159.5757...`, and the mixed degree-six sums are not ordinary Jacobi sums. |

These are failures of particular theorem hypotheses, not a claim that a
better estimate is impossible or absent from all literature. A norm-descending
subfamily of characters does not suffice: product orthogonality uses all
nontrivial characters of `E*`.

## Exact restricted second-moment identity

Write `N=262144`, `I=(p-1)/N=8128`, and let `H=D^perp` be the `I`
base-field characters trivial on `D`. Fix a nontrivial character `chi` of
`E*` and put

\[
 t(a)=\chi(b-a),\qquad
 M_\chi(\psi)=\sum_{a\in\mathbb F_p^*}t(a)\psi(a),\qquad
 C_\chi(u)=\sum_{a\in\mathbb F_p^*}t(ua)\overline{t(a)}.
\]

All `t(a)` have absolute value one. Orthogonality gives the exact identities

\[
 S_\chi=I^{-1}\sum_{\psi\in H}M_\chi(\psi),
\]
\[
 Q_\chi:=I^{-1}\sum_{\psi\in H}|M_\chi(\psi)|^2
 =\sum_{u\in D}C_\chi(u)
 =\sum_{cD\in\mathbb F_p^*/D}\left|\sum_{a\in cD}t(a)\right|^2.
\]

Consequently `|S_chi|^2 <= Q_chi`. The restricted second-moment route
would succeed if

\[
 Q_\chi/p < N^2/p = 32.25196848880025\ldots
\]

uniformly in `chi`. A typical-value assertion for the Mellin transforms
does not establish this inequality. Full-family Parseval gives only

\[
 \sum_\psi |M_\chi(\psi)|^2=(p-1)^2,
 \qquad |S_\chi|\le\sqrt{(p-1)N}=23633702.7761\ldots.
\]

For reference, if the six Frobenius conjugates of `b` and their `u`-dilate
are disjoint for each `u in D\{1}`, the tame rank-one correlation estimate
has the centered form

\[
 |C_\chi(u)+1+\chi(u)|\le 10\sqrt p.
\]

Here the boundary traces at zero and infinity are `1` and `chi(u)`.
Summing gives

\[
 Q_\chi\le p-N+1-\epsilon N+10(N-1)\sqrt p,
 \qquad \epsilon=\mathbf1_{\chi|D=1}.
\]

Even the `epsilon=0` bound has square root `350905.3162...`. Disregarding
the small boundary terms, replacing the coefficient 10 by a uniform
aggregate coefficient below `5.503017844...` would be necessary to beat
`N`. This is a quantitative requirement on the sum of correlations, not
an established improvement.

### A dilation exception that must be checked

The preceding correlation estimate needs its geometric nontriviality
hypothesis. The six conjugates of `b` form one Frobenius orbit. If a
base-field scalar carries one conjugate to another, it permutes this orbit;
its order divides both six and `p-1`. Since `gcd(6,p-1)=2`, the only
possible nonidentity scalar is `-1`, occurring when `b^(p^3)=-b`.

For such a `b`, take a nontrivial character of the form
`chi=eta o Norm_(E/F_(p^3))`. Then `chi^(p^3)=chi` and `chi(-1)=1`, so

\[
 t(-a)=\chi\bigl(-(b-a)^{p^3}\bigr)=t(a),\qquad C_\chi(-1)=p-1.
\]

Thus a claim of `10 sqrt(p)+O(1)` for every nonidentity correlation would
be false without excluding this case. Choosing `b^(p^3) != -b` removes
this particular obstruction for all scalars in `D`. It does not prove
additional cancellation.

## A higher-moment gate that would be sufficient

For an integer `k>=1`, define a moment over **all base-field twists**:

\[
 A_{2k}(\chi)=\frac1{p-1}\sum_{\psi\in\widehat{\mathbb F_p^*}}
       \left|\frac{M_\chi(\psi)}{\sqrt p}\right|^{2k}.
\]

Hölder on `H`, followed by positivity when enlarging `H` to the full
character group, proves

\[
 |S_\chi|\le\sqrt p\bigl(N A_{2k}(\chi)\bigr)^{1/(2k)}. \tag{1}
\]

There is no distribution assumption in (1). Therefore a uniform bound

\[
 A_{2k}(\chi)<N^{2k-1}/p^k \tag{2}
\]

would imply `|S_chi|<N`. The finite thresholds are:

| Moment | Threshold in (2) | Conditional `U(6)` Haar value | Bound from (1) if the moment equaled that value |
| --- | ---: | ---: | ---: |
| Tenth (`k=5`) | 133.1193572723 | 120 | 259438.2017 |
| Twelfth (`k=6`) | 4293.3613159943 | 720 | 225900.8387 |

The Haar column is only a comparison. For `k<=6`, the `U(6)` trace moment
is `k!`, by the dimension of the permutation commutant on the `k`th
tensor power. No `U(6)` or `SL(6)` monodromy assertion for every `chi,b`
is made here.

One can ask for enough deficit to imply product coverage, rather than
merely a strict bound. For `r=139782`, set `theta=r/N`. The
fixed-cardinality Cauchy lemma requires

\[
 (p^6-2)(N+1)\exp[-\theta(1-\theta)(N-B)]<1.
\]

The necessary deficit for this sufficient criterion is
`567.9277745969...`. Thus `B<=N-570` suffices. Exact rational inequalities
show that either of the following **unproved analytic hypotheses** would
give that bound through (1):

\[
 A_{10}(\chi)\le130\quad\text{for every nontrivial }\chi,
 \qquad\text{or}\qquad
 A_{12}(\chi)\le4182\quad\text{for every nontrivial }\chi.
\]

The verifier checks the two power inequalities using integers, and checks
the Cauchy positivity criterion using a rational Taylor lower bound for
the exponential. It verifies only this implication, not either moment
hypothesis.

## Why general Mellin equidistribution is not yet a finite certificate

[Katz, *Convolution and Equidistribution*, Theorem 7.2, Remark 7.5,
and Theorem 28.2](https://web.math.princeton.edu/~nmk/mellin398.pdf)
provides an actual framework for these moments, but requires identifying
the relevant monodromy and controlling the finite error. For a Mellin
object of dimension six and generic rank one, the general convolution
rank bound for a tensor space of total degree `2k` is
`R <= 2k*6^(2k-1)`, with dimension `D=6^(2k)`.
Even granting the favorable monodromy, the resulting general error bound
from Remark 7.5, bounded using `(1+1/sqrt(p))*(R+D)/sqrt(p)`, is about
3493 for the tenth moment and 141476 for the twelfth, before separately
including exceptional twists. These exceed the respective margins
`133.119-120` and `4293.361-720`. This does not lower-bound the actual
error; it shows that this general estimate fails to certify the desired
moment.

A useful next proof would have to establish the moment bound uniformly
in every extension-field character, handle the exceptional twists, and
sharpen the finite error substantially. Checking sampled characters
cannot replace these requirements. The tenth/twelfth thresholds provide
a definite pass/fail target for such a theorem.

## Separate coding limitation

Even successful product coverage at `r=139782` does not lower the degree
of its one-pole witnesses. On the practical code with strict degree bound
`J=131072`, the ordinary one-pole residual has degree `J+1=131073`, so
that compiler cannot attain 139782 agreements. See
`PRACTICAL_SUBGROUP_TWIST_AUDIT.md` and
`PRACTICAL_SEED_PAIR_COMPILER_GATE.md` for the already proved degree gates.
The present analytic gate would improve a future transfer ingredient;
it does not solve the practical coefficient-cancellation problem.
