# One derivative-pencil screen on the verified order-23 fixture

September 18, 2026. **Complete bounded screen: no qualifying witnesses.**

The sole instance is the stored curve \(y^2=x^3+121\) over
\(\mathbb F_{1657}\), with its verified full order-23 torsion domain:
\[
n=264,\qquad k=173,\qquad T=213.
\]
The sole received pencil is \(w_\lambda=\Phi'+\lambda\Phi''\). The screen
tests all 1,320 two-fiber base pairs and extra degrees \(d=0,\ldots,5\),
using the error ansatz
\[
U=L_0J,\qquad
e_U=\frac{n}{2\ell+d}\frac{\Phi}{U}U'.
\]
These errors have the prescribed values \(\gamma\Phi'(x)\) on \(Z(U)\),
with the necessary normalization \(\gamma=n/(2\ell+d)\). Arbitrary error
values are not included.

For each pair and degree, FLINT finds the field roots of the nonzero
degree-\((d+1)\) Newton gate from
[the derivative discriminator](../DERIVATIVE_EXTRA_LOCATOR_DISCRIMINATOR.md).
The uniquely predicted \(J\) must then divide \(\Phi\) and be coprime to
\(L_0\). Every survivor is checked both by actual-root syndrome moments and
by the direct requirement
\[
\deg\left(\Phi'+\lambda\Phi''
 -\frac{n}{2\ell+d}\frac{\Phi}{L_0J}(L_0J)'\right)<173.
\]

| Extra degree \(d\) | Gate roots, counted by base pair | \(J\mid\Phi\) | Also coprime to \(L_0\) | Qualifying witnesses |
|---:|---:|---:|---:|---:|
| 0 | 1,320 | 1,320 | 1,320 | 0 |
| 1 | 1,317 | 204 | 162 | 0 |
| 2 | 1,335 | 30 | 24 | 0 |
| 3 | 1,332 | 0 | 0 | 0 |
| 4 | 1,392 | 0 | 0 | 0 |
| 5 | 1,257 | 0 | 0 | 0 |

All 7,920 gates were processed, yielding 7,953 candidate roots. Among the
1,506 admissible split/coprime locators, every moment test agreed with its
direct polynomial-degree test and rejected the candidate. The first failed
moments were order two or three for \(d=0\), order three for \(d=1\), and
order four for \(d=2\). The corresponding residual degrees were 261/260,
260, and 259, respectively, all above the strict code cap 172.

The original run took 0.268 seconds; a root replay took 0.296 seconds and
reproduced the same candidate-stream hash and all counts. Peak memory was
about 34.2 MiB, below the explicit
30-second cap. No field-wide label loop, extra-set enumeration, curve search,
or rental was used. All 91 derivative syndrome moments were independently
checked from the actual word values before the screen.

Reproduce using the existing environment:

    /Users/jthaler/.local/share/research-toolchain/venv/bin/python \
      research/elliptic_coset_complements/ell23_fixture/check_derivative_pencil.py

The code and [count receipt](derivative_pencil_screen.json) bind the run to
the fixture hash and record the gate-candidate stream hash.

This is not a counterexample and does not establish or need endpoint
farness. It excludes only the displayed scalar-\(\Phi'\) error ansatz for
this one pencil on this one fixture. Arbitrary within-support errors,
other pencils, other curves, and growing torsion order remain outside it.
