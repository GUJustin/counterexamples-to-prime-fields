# Odd Gold, p=3 and s=2: cubic-pole finite certificate

This certificate verifies the displayed bank in
../ODD_GOLD_CUBIC_POLE_EXACT_CLASSIFICATION.md. It uses
\[
 (n,k,T,U,M)=(243,102,153,135,29403),\qquad E=\mathbb F_{3^{15}}.
\]
The strict code dimension is 102: witnesses have degree at most 101.
The complete classification, singleton lists and source bounds are
algebraic results; this program does not enumerate all codewords.

## Fixed field and native embedding

The verifier uses FLINT's polynomial-basis FQ_NMOD representation
\[
 E=\mathbb F_3[z]/(z^{15}+2z^8+z^5+2z^2+z+1),\qquad \beta=z.
\]
It checks irreducibility and that \(z\) is primitive, using the complete
factorization \(3^{15}-1=2\cdot11^2\cdot13\cdot4561\).
The native field \(B=\mathbb F_{243}\) is
\[
 B=\{0\}\cup\langle z^{59293}\rangle.
\]
Every listed native element is checked to satisfy \(x^{243}=x\);
\(\beta\) does not. Elements are encoded by their base-three
polynomial-basis coefficients. The native generator is encoded 6319081.
No table or scan of the 14,348,907 challenge-field elements is used.

## Complete coefficient and label checks

The native reduced Gold polynomial is
\[
 \Psi_a(X)=aX^{10}+a^3X^{30}+a^9X^{90}
                  +a^{27}X^{28}+a^{81}X^{84}.
\]
Among all 242 nonzero native coefficients, exactly 121 give 90 roots
of \(\Psi_a+1\), and 121 give 72. The good coefficients are exactly the
native nonsquares. This includes 58,806 native value checks.

For every good \(a\) and every \(b\in B\), put
\[
 G=\Psi_a(X+b)+1,\qquad F=a^{81}(X+b)^3+a^9(X+b)^9.
\]
The verifier evaluates
\[
 \lambda=P(\beta)=\frac{(\beta^{243}-\beta)F(\beta)}{G(\beta)}
\]
using only the five sparse Gold terms and two terms of \(F\).
All 29,403 labels are distinct and nonzero. The 58,806 values
\(uG(\beta)\), \(u\in\mathbb F_3^*\), are also all distinct.
The deterministic complete bank is saved in parameters_and_labels.json.

The endpoint constant is the unique cube root
\[
 c_\star=((\beta^{243}-\beta)^2)^{3^{14}},
\]
encoded 110317. The verifier checks its defining identity, verifies that
it is outside the bank, and checks all 29,403 affine parameters
\(t=1-c_\star/\lambda\) are distinct and avoid zero and one.

## Full polynomial sample

For twelve evenly spaced good coefficients and three centers
\(0,1,z^{59293}\), the script constructs all 36 full polynomials
\[
 P=F\Lambda/G,\qquad
 h=\frac{X^{162}-P+P(\beta)-\beta^{162}}{X-\beta}.
\]
It verifies exact polynomial division, \(G^3-G=\Lambda F^3\),
\[
 P^3=\Lambda^2-(\Lambda/G)^2,\qquad
 \deg(P-X^{162})=102,\qquad \deg h=101.
\]
Every sample has exactly 90 native roots of \(G\), 153 of \(P\), and
153 matches for the witness. The scaled witness for the actual affine
endpoint pair has the same 153 matches. All 8,748 sampled coordinate
identities are checked.

## Source bounds and placement

The endpoint pair is \(r_0=f+c_\star g,\ r_1=c_\star g\), with
\[
 f=\frac{X^{162}-\beta^{162}}{X-\beta},\qquad
 g=\frac1{X-\beta}.
\]
The audited multiplicity proof gives agreement at most 135 for \(r_0\);
the reciprocal proof gives exact agreement 102 for \(r_1\) and exact
common agreement 102. These are proof-based bounds, not results of a
codeword census. The smaller guaranteed loss is \(18/243\), or
\(18/51\) of the capacity margin.

The exact finite Johnson slack is
\(243\cdot101-153^2=1134\). The high-branch first-order polynomial
has value \(1496/59049>0\). These integer checks are included.

## Reproduction

Run from the repository root:

    /Users/jthaler/.local/share/research-toolchain/venv/bin/python research/binary_characteristic_transfer/odd_gold_p3_s2_fixture/verify.py

The saved run took 3.15 seconds and 90.6 MB. It has internal time and
memory guards and constructs full witnesses only for the stated sample.

Verifier SHA-256:
6655e860aa0919dbb43783c36074899c3dc0d5fc6efdcc21f11bd0bd6ab1ac7c.
Complete bank SHA-256:
c601bcc0a3bbbe29b55dfe5f9a74c06108be0acde60483fd059ebe187e6907f9.

This is a full native-field, fixed-characteristic fixture with an
extension alphabet. It does not assert a prime-alphabet construction or
a prescribed practical short domain.
