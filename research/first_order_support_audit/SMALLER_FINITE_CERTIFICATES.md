# Smaller finite high-rate certificates

September 17, 2026. The restored support construction admits smaller
certificates at the same two strict improvements over the recovered DKT
curve. These are new parameter optimizations of the restored construction,
not new agreement thresholds or a proof of globally minimal support.

| Rate | Agreement | Multiplicity: old -> new | Monomials: old -> new | Sufficient challenge degree: old -> new |
|---|---|---|---|---|
| 9/10 | 47389/50000 | 10000 -> 4096 | 9724108 -> 1632467 | 320257184 -> 241481265 |
| 3/4 | 43049/50000 | 100000 -> 65536 | 1830201539 -> 786044039 | 19137094352 -> 16569483999 |

The support uses the same endpoint formula and B=49/500 or173/1000,
respectively. Exact totals and positive surpluses are recorded in
smaller_certificates_verification.json. The verifier independently
recounts the column-formula rank by homogeneous diagonal lengths and
the original rank formula. Its diagonal summation identity passes21295
direct checks; both large recounts agree exactly. The bounded run takes
about1second and less than20MiB.

The 12-page technical note now displays these smaller certificates, with
provenance distinguishing the restored construction from this parameter
optimization. It builds without reference or layout warnings; the changed
pages were rendered and visually inspected.

These supports and conservative challenge degrees remain enormous. There
is no demonstrated better.codes improvement, deployed-system parameter
improvement, or intrinsic list/MCA lower bound. In particular, reducing
multiplicity can reduce the dimension surplus so much that the challenge
degree gets worse: at rate3/4, m32768 also has positive surplus at the
same agreement, but its sufficient challenge degree is121322117137.
The displayed m65536 choice improves both reported costs over the
restored certificate. No global cost optimization is claimed.
