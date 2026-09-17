# Paired domains and exact affine distance profiles

The integrated proof is [paired.tex](paired.tex), including
[completion.tex](completion.tex). See [COMPLETION_PROOF_AUDIT.md](COMPLETION_PROOF_AUDIT.md)
for the internal audit of the strongest result and [PROOF_AUDIT.md](PROOF_AUDIT.md)
for the original multiple-block argument.

At every fixed rational rate, every sufficiently large prime field admits a
line whose nonzero parameters all have exactly the tested distance, while zero
has distance 1-rho-1/n: one coordinate short of maximum possible RS distance.
The separation is 2r/(2r+1) of the capacity gap. The direction changes exactly
2r coordinates, the minimum needed for that improvement. The nonzero points'
decoding lists are pairwise disjoint. More generally an r-dimensional affine
space has distance 1-rho-(1+2 wt(z))/n at parameter z.

Taking r about log log p makes the separation approach the entire gap, at
length Theta(log p log log p), strictly below Elias. The numerical nearby
fraction tends to zero while the actual fraction tends to one. The gap shrinks;
no prescribed FFT-domain transfer or witness recovery algorithm is claimed.

The completion sampler is polynomial in log p, with probability 1-p^-Omega(1).
The sample `completed_samples/m521_r2_n2518.json` has 2518 coordinates over
p=2^521-1, dimension 1259, and a four-coordinate direction. Its generator
failure is below 2^-88 by the independent weaker-constant replay. The zero
codeword is a known nearest word at parameter one. The coordinates, direction
support, and distances at parameters zero and one are deterministically
verified. Full coverage is NOT individually deterministically certified.

Run the standard-library checkers from the repository root:

    python3 research/paired_domain_warp/verify_completion.py
    python3 research/paired_domain_warp/audit_completion_independent.py
    python3 research/paired_domain_warp/verify_translate_identity.py
    python3 research/paired_domain_warp/check_small_completion.py
    python3 research/paired_domain_warp/verify_completed_sample.py

`generate_completed_sample.py` draws a fresh completion sample; consult its
arguments for the output path. Its large image is implicit.

The older `samples/m521_r2_n2518.json` uses 24 padding blocks, a 96-coordinate
direction, and generator failure below 2^-128. `verify_sample.py` replays it.
It is a different construction and probability guarantee. The block argument
is retained and checked by `verify_joint_images.py`,
`verify_multiblock_finite.py`, and `audit_multiblock_independent.py`.
The one-pair curve route is retained in `single_pair.tex`.


The finite table also uses `optimized_completion.json`, replayed independently
by `audit_optimized_completion.py`. Fine upward rounding gives shorter
sufficient rows: M521/r2/n2142 with prescription below 2^-81 (existence),
and M1279/r3/n8014 with failure below 2^-64 and prescription below 2^-121.
The search is not a proof of optimality.

`m31_exact/` contains four fully deterministic finite banks over 2^31-1.
The n62/K31 instance has 140,916,078 nearby parameters; n68/K33 has
897,817,238 and beats twice the proposed prefactor. `m31_exact/verify.py`
compiles two independent C++17 enumerators, runs them sequentially, checks
all exact inequalities, and recovers explicit witnesses. It uses a 256 MiB
bitmap and takes about a minute on the restored laptop. Source and compact
instance files suffice; no bitmap artifact is required.
