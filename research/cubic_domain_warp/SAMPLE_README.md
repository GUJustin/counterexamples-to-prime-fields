# Direct randomized sample

`samples/m521_n990.json` contains a length990, dimension495 Reed–Solomon
domain and received line over p=2^521-1. The JSON records the original
anchored support, cubic-map parameters, and complete coordinate arrays.
`domain[i]` is the evaluation point; the line has value
`f[i]+z*g[i] mod p` there.

Run from the repository root:

    python3 research/cubic_domain_warp/verify_sample.py
    python3 research/cubic_domain_warp/verify_randomized_bound.py
    python3 research/cubic_domain_warp/verify_sampling_identity.py

All use the Python standard library. The sample verifier evaluates the
root product directly, independently of the generator's coefficient
multiplication and Horner evaluation. It checks domain distinctness,
line values, exact zero-parameter maximum agreement496, strict Elias,
and the numerical prescription fraction below2^-16.

The sampling theorem bounds the generator's probability of failing to
cover all nonzero parameters by less than2^-137. The independent sample
verifier proves the weaker bound2^-128 by integer comparisons. This is
a guarantee OVER GENERATOR RANDOMNESS, not a deterministic certificate
that the stored sample covers all2^521-2nonzero parameters. The exact
far point and absence of correlated agreement hold for every output.

To draw a fresh sample without replacing the frozen artifact:

    python3 research/cubic_domain_warp/generate_sample.py --output /tmp/new-cubic-sample.json

The generator uses uniform system-random sampling and refuses to overwrite
an existing output. Its proof never requires enumerating or locating the
large moment class or computing outside images. It does not recover a
nearby codeword for a supplied parameter.

The frozen artifact's SHA256 and structural replay are recorded in
`sample_verification.json`. `randomized_bound_verification.json` records
the exact rational failure bound. Finite identity checks are in
`sampling_identity_verification.json`; the general proof is in
`randomized.tex` and `RANDOMIZED_CONSTRUCTION.md`.
