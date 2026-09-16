# Linear full-support MCA for polynomials with boundedly many roots

At fixed positive rate and agreement above the degree cap, candidates
with at most r distinct algebraic roots have only O_r,a(n) bad
full-support mutual-correlated-agreement (MCA) labels, in sufficiently
large characteristic relative to n. The root positions, multiplicities,
and nonzero scalar coefficients can all vary.

[Proof and explicit thresholds](PROOF.md). Appendix G of the main
manuscript contains the proof and retains the third-order quadratic-power
surface as an example: its solution variety has degree Theta(n^2), but
its bad labels remain linear. The earlier
[fixed-power proof](../power_family_mca/README.md) is retained separately.

The key division is by root multiplicity. Quadruples with a large root
unique to each member admit a Wronskian gcd bound. Every other quadruple
has a member whose large-multiplicity roots lie in the other three root
sets; an exponent partition then reduces that cluster to small residual
degree. An affine polynomial pencil contributes at most n bad labels on
full supports, which controls the dependent cases.

## Replay

From the repository root, using Python's standard library:

```sh
python3 research/bounded_root_mca/verify_wronskian.py
python3 research/bounded_root_mca/verify_clusters.py
```

The checkers import the elementary arithmetic helpers in the sibling
`power_family_mca` package. All jobs were run sequentially under a 384 MiB
watchdog. They verify finite ingredients and explicit parameter choices;
they do not replace the proof or make its constants practically useful.

This is a self-reviewed result, with no independent mathematical review
or novelty claim. It excludes bounded root count as a construction route.
It does not settle general nonlinear first-order MCA, exclude families
with a growing number of roots, establish quadratic fixed-gap error, or
improve the better.codes score.
