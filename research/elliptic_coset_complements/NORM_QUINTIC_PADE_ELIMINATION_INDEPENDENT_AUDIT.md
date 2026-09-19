# Independent audit of norm-quintic Padé elimination

Verdict: PASS on the actual saved file. This audit does not assert a solution of the general norm-quintic system.

- The norm coefficients are correct quadratics in four parameters. Squarefree divisibility by Phi preserves the necessary native-root condition; sign reversal is the only duplicate for distinct odd-torsion x-roots.
- All moment indices fit0..4ell−2. There are2ell−6 independent monic recurrence rows. The Cramer formulas, including the sign of pi=V/Delta, and the3×3 determinant expansion are correct. The rank-deficient charts are retained rather than silently discarded.
- The determinantal entries have challenge degree at most3, norm-parameter degree at most6, and total degree at most9. The tag quadratic dividing the squarefree tag locator is the exact admissibility condition. Recurrence plus the split/copime support filters is sufficient by equality of kernel and support-syndrome dimensions.
- The explicit error interpolant (9) has the correct Phi'(x) normalization. Its gcd condition with J is exactly the condition that all five extra error values are nonzero.
- The incidence dimension/codimension calculation follows from the monic Toeplitz pivots for every local parameter tuple. The4^7 zero-dimensional bound concerns the seven-variable original equations; the9^5 bound concerns isolated rank-two points of the global five-variable determinantal variety. Neither bound is multiplied by pivot-chart count, and neither controls positive-dimensional special incidences.
- The3/7 chord chain has successive sums7P,3P,5P and the correct two vertical denominators. The norm distribution has equal divisors and equal normalized pole terms except for product over nonzero kernel evaluations. Pairing signs and swapping resultants yields the stated positive product of K_H values; both signs cancel.
- Multiplication-map degrees give sum j^2=82 and sum(j^2−1)=77 for the five extra roots. The two tags have numerator-degree sum58ell and denominator-degree sum58ell−2. The resulting common recurrence bound58ell+82 and minor bound116ell+164 are valid upper bounds, including possible cancellations. They apply only where the rational formulas are defined.
- The finite kappa certificate and its scope agree with the independent group-law and modular-rank replay. The final2n support-family argument is valid with its genuine-syndrome-line and far-endpoint premises. It does not exclude the general four-parameter norm family.

The subsequent arbitrary-extra fixed-base argument may strengthen the per-base bookkeeping, but no such extension is needed for validity of this note.

Reviewed source SHA256: `55c153a78af281f1cfb1c95e407777f34f06c6321081c8261de612746ee47354`.
