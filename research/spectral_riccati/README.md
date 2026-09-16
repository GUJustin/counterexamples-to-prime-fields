# A linear spectral bound for a nonlinear Riccati family

Let R be monic of degree D+1, let B have degree b<=D-2, and consider

```
R P' - R' P + P^2 - z B P = 0,       deg P <= D.
```

In characteristic zero or characteristic greater than D+1, if
`D>(b+1)(b+2)`, at most `D-b-1` nonzero challenge labels admit a nonzero
polynomial solution. This gives at most `n+D-b` bad full-support MCA
labels on any n-point received line, including the zero candidate.
The result covers every fixed b for sufficiently large D.

[PROOF.md](PROOF.md) gives the elementary division and multiplicity
argument. [CONSTANT_WEIGHT.md](CONSTANT_WEIGHT.md) proves the sharper
classification for B=1: at most three nonzero labels for D=2, two for
D=3, and one for D>=4. Neither requires R to be squarefree or split.

This excludes a particular nonlinear construction route. It does not
settle general first-order MCA, improve the better.codes score, or give
a quadratic lower bound. The proofs are self-reviewed; no independent
mathematical review or literature-priority claim is made.

## Reproduce

Both checks use only Python's standard library:

```sh
python3 research/spectral_riccati/verify_constant.py
python3 research/spectral_riccati/verify_weighted.py
```

The weighted checker tests 248,561 candidates in 1,780 fixtures. Its
7,191 solutions include nonsplit and repeated-root examples, and its
small-degree negative controls show why the theorem's degree threshold
cannot simply be omitted. Candidate counts and label groups match a
prior run using SymPy's independent factorization implementation; the
comparison hashes are recorded separately.

The constant-weight checker also tests 59,740 unrestricted small-field
polynomials and all 775 monic R over F_5 in degrees two through four.
Finite checks supplement the proofs. Resource reports record sequential
execution under a 384 MiB watchdog, with sampled RSS rather than a claim
about exact peak memory.
