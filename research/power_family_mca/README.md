# Powers of bounded-degree bases have only linearly many bad MCA labels

For a fixed base degree r, consider candidates P=cH^e, with H monic of
degree r. At fixed positive rate and agreement above the degree bound,
the number of bad full-support mutual-correlated-agreement (MCA) labels
on any received line is O(n), in characteristic sufficiently large
relative to n. The constants depend on r and the agreement fraction.
The exponent e grows with n and is common to the candidate family.

[Proof and precise finite thresholds](PROOF.md). The proof combines an
elementary Wronskian gcd bound, a count of multiplicatively dependent
tuples, and a division into large and small coordinate-ratio groups.
It does not assume that the moving roots are independent parameters.

[Third-order quadratic-power equation](QUADRATIC_SURFACE.md) gives a
fixed-order, fixed-jet-degree nonlinear equation whose actual projective
solution variety has degree e^2. Its two-moving-root solutions are covered
by the linear MCA bound. Thus quadratic solution-variety degree alone
does not produce a quadratic proximity-gap lower bound.

## Replay

From the repository root, using Python's standard library:

```sh
python3 research/power_family_mca/verify_family.py
python3 research/power_family_mca/verify_wronskian.py
python3 research/power_family_mca/verify_mca.py
python3 research/power_family_mca/verify_parameters.py
```

The checks cover the classification and reduced degree sections, exact
Wronskian bookkeeping, finite received lines, dependent divisor tuples,
and explicit asymptotic parameter choices. The polynomial fixtures use
small auxiliary degree and do not attain useful asymptotic MCA constants.
Exact rational parameter checks establish feasibility of those constants;
they do not enumerate a received line at the enormous resulting length.

This is a self-reviewed supplementary proof, with no independent
mathematical review or novelty claim. The general nonlinear first-order
conjecture, variable root exponents, and the desired fixed-gap quadratic
lower bound remain open here. No better.codes score improvement is claimed.
