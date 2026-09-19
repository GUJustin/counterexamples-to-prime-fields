# Explicit higher-power fixture over F_(97^4)

The initial fixture run passed in 19.59 seconds; a root replay passed
in 22.45 seconds with the identical raw-array hash, within the
60-second computation cap. No other parameters, received pencils, or
codewords were scanned.

The field is
\[
 E=\mathbb F_{97}[a]/(a^4+6a^2+80a+5).
\]
The verifier checks irreducibility through the finite-field constructor
and checks that \(s=a\) has multiplicative order \(97^4-1\). Let
\[
 h=5,\quad Q=9410,\quad L=9408,\quad z=s^Q,\quad
 \alpha_j=s^{1882j},\quad \eta=s^5.
\]
The domain consists of all five core branches \(\alpha_jB^*\), the two
fresh branches \(sB^*,s\alpha_1B^*\), and the 4704-point prefix
\(\{s\alpha_2z^t:0\le t<4704\}\). These are 70560 distinct coordinates.

The raw received words are \(f=x^{485},g=0\) on the core and
\(f=\eta^{1-97}x^{485},g=1\) on the fresh block. Take the two endpoints
\[
 f+(1+\eta z)g,\qquad f+(1+\eta(z+1))g.
\]
Since \(z\notin\mathbb F_{97}\), both raw parameters lie outside all
canonical label planes. This is a different valid endpoint choice from
the paper's displayed pair; both choices parametrize the same affine line
and satisfy the same agreement bounds.

| Quantity | Verified value |
|---|---:|
| Code length | 70560 |
| Message dimension | 6 |
| Rate | \(1/11760\) |
| Threshold | 593 |
| Ordinary common agreement | exactly 485 |
| Each endpoint's nearest agreement | in \([485,510]\) |
| First-order agreement upper bound | 483 |
| Singleton threshold-list parameters | 921984 |
| Additional parameter | one, with 98 witnesses |
| Every other parameter | empty threshold list |
| Actual nearest agreement at singleton parameters | between 712 and 738 |
| Actual agreement of the 98 zero-parameter witnesses | 720 each |

The threshold is strictly below Johnson:
\(593^2<5\cdot70560\), and 593 is the largest such integer.
The endpoint agreement loss is at least \(83\), or \(83/587\) of the
capacity margin. The common-agreement loss is \(108\).

The verifier explicitly counts every canonical support, verifies the
distinct image lines and the two endpoint exclusions, and instantiates
all coordinates and source values. Exclusion of every other
degree-\(\le5\) witness uses the proved universal agreement bound
\(hp+h^2=510\), not enumeration of codewords. Exact common agreement
uses the indicator-polynomial proof. Endpoint agreements are bounded,
not claimed to have been exactly enumerated.

Artifacts:

* [verify.py](verify.py): deterministic reconstruction and checks;
* [receipt.json](receipt.json): exact counts, histograms, field data,
  per-direction support summaries, and hashes;
* [domain_and_sources.npz](domain_and_sources.npz): the actual 70560-by-5
  array of coordinates and source values.

The archive has one array, named rows, whose columns are
\(x,f,g,f+(1+\eta z)g,f+(1+\eta(z+1))g\). Each field element
\(\sum_{i=0}^3c_i a^i\) is encoded as the integer
\(\sum_{i=0}^3c_i97^i\), in little-endian uint32. The ordered raw array has
SHA-256

    7257c227fe55be89a8e320d123452c8ae708095165068ed93c81c15c3c2cefd0

The full finite-field recipe and all-witness proof are in
[HIGHER_POWER_DETERMINISTIC_BRANCH_RETENTION.md](../HIGHER_POWER_DETERMINISTIC_BRANCH_RETENTION.md)
and [HIGHER_POWER_FULL_FIBER_LIFT.md](../HIGHER_POWER_FULL_FIBER_LIFT.md).
This is an explicitly instantiated moderate-length, very-low-rate
extension-field example. It is not a prescribed NTT-domain, prime-alphabet,
or half-rate practical benchmark.

## Independent arithmetic check

[independent_archive_check.py](independent_archive_check.py) uses NumPy
polynomial arithmetic modulo the displayed quartic, without FLINT
finite-field operations. It checks every saved coordinate, every raw source
value, and all 141,120 endpoint values, verifies the primitive order, and
counts an explicit 485-coordinate common-agreement witness.
[The receipt](independent_archive_check.json) records PASS in0.48 seconds
and the identical raw-array hash. This independently validates the saved
artifact; the upper bounds for arbitrary codewords remain mathematical
proofs, not exhaustive codeword enumeration.
