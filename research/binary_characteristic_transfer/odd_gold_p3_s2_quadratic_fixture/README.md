# Odd Gold, p=3 and s=2: one quadratic-pole label census

This is a separate finite evaluation of the 29,403 native odd-Gold bank
polynomials at one quadratic exterior pole. It preserves
\[
 (n,k,T,U)=(243,102,153,135)
\]
and uses the smaller coefficient field \(E=\mathbb F_{3^{10}}\).
The cubic-pole certificate is unchanged in the sibling folder
odd_gold_p3_s2_fixture.

## Field and coefficient-space checks

The exact polynomial-basis representation is
\[
 E=\mathbb F_3[z]/(z^{10}+2z^6+2z^5+2z^4+z+2),\qquad\beta=z.
\]
The verifier checks irreducibility and primitivity using
\(3^{10}-1=2^3\cdot11^2\cdot61\). The native subfield is
\[
 B=\mathbb F_{243}=\{0\}\cup\langle z^{244}\rangle.
\]
Its generator is encoded 37028; all 243 native elements and
\(\beta\notin B\) are checked. Element encodings are base-three
polynomial-basis coefficients. FLINT FQ_NMOD is used; no challenge-field
table or scan is built.

An explicit basis of
\[
 \mathcal H=\{\Psi_a+\operatorname{Tr}_{B/\mathbb F_3}(lX)+c:
               a,l\in B,\ c\in\mathbb F_3\}
\]
has coefficient rank 11 over \(\mathbb F_3\). Its evaluation at \(\beta\)
has rank ten, hence kernel dimension one. These ranks are checked
directly in the displayed field representation.

## Complete bank histogram at the chosen pole

The verifier uses every one of the 121 native nonsquares \(a\) and every
center \(b\in B\), with
\[
 G=\Psi_a(X+b)+1,\qquad
 F=a^{81}(X+b)^3+a^9(X+b)^9,\qquad
 \lambda=\frac{(\beta^{243}-\beta)F(\beta)}{G(\beta)}.
\]
All 29,403 evaluations are defined. Exactly one bank polynomial has
\(\lambda=0\). The nonzero labels have the following exact fibers:

| Bank members at a nonzero label | Number of labels |
|---:|---:|
| 1 | 14,210 |
| 2 | 6,246 |
| 3 | 900 |

Thus there are exactly **21,356 nonzero labels**, accounting for 29,402
bank members. This is larger than the general lower bound 9,801 obtained
from the maximum fiber size three. The complete deterministic bank
evaluation is saved in parameters_and_labels.json.

These are exact bank-fiber counts. Combined with the separately proved
classification of every threshold residual, they give the complete
threshold-list profile at this pole. No enumeration of all codewords
was used to establish completeness.

## Endpoints and representative witnesses

The constant
\[
 c_\star=((\beta^{243}-\beta)^2)^{3^9}
\]
is encoded 51092 and satisfies \(c_\star^3=(\beta^{243}-\beta)^2\).
The verifier checks \(c_\star\ne0\) and that it is outside the entire
label bank. Hence all 21,356 nonzero labels give distinct interior
affine parameters
\[
 t=1-c_\star/\lambda
\]
for \(r_0=f+c_\star g,\ r_1=c_\star g\).
The single zero label belongs to the omitted projective direction and
has no finite parameter in this chart.

The program constructs all witnesses in one deterministic fiber of
each observed size, together with the zero-label witness: seven full
polynomial samples. Each has degree 101 and exactly 153 native
agreements. Witnesses in the same selected collision fiber are
verified to be distinct. The six nonzero-label samples also satisfy
the scaled affine residual identity on all 243 coordinates.

The audited multiplicity and reciprocal arguments give
\[
 A(r_0)\le135,\qquad A(r_1)=\operatorname{CA}(r_0,r_1)=102.
\]
These bounds are proof-based, not outputs of the label census.
In particular, no exact agreement is asserted for \(r_0\).

## Reproduction and scope

Run from the repository root:

    /Users/jthaler/.local/share/research-toolchain/venv/bin/python research/binary_characteristic_transfer/odd_gold_p3_s2_quadratic_fixture/verify.py

The saved run took 0.86 seconds and 63.5 MB. The script has 110-second
and 512-MiB internal guards.

Verifier SHA-256:
9a73b17e6f79b61842544dd474a8cded1913d246ed3c6145b28ac0dfdbbd62dc.
Complete bank SHA-256:
4a25f33f1b28443ca50245b1430e2b1fb6b86c832aef5a65e51271a6e10214dc.

This receipt concerns the displayed pole and field representation.
Transport of its histogram to other quadratic poles requires a separate
affine-change proof. It is not inferred by scanning those poles.
The construction still uses a full native subfield and an extension
alphabet, and makes no prime-alphabet or practical-domain claim.
