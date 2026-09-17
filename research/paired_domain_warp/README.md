# Paired-domain punctured lines

The integrated proof is [paired.tex](paired.tex); the detailed internal
review is [PROOF_AUDIT.md](PROOF_AUDIT.md).

At every fixed rational rate, every sufficiently large prime field admits
a line with all nonzero parameters nearby and a zero parameter at distance
1-rho-1/n, only one coordinate below the maximum possible RS distance.
With r paired coordinates per padding block, the far separation is
2r/(2r+1) of the gap. Taking r~log log p makes this fraction tend to1 at lengthTheta(log p log log p),
while the radius stays strictly below Elias and the c1=c2=1 numerical
nearby fraction tends to0. The gap still shrinks. No prescribed FFT-domain
transfer or nearby-witness recovery algorithm is claimed.

The sampler is polynomial in log p, with probability1-p^-Omega(1).
The fixed sample `samples/m521_r2_n2518.json` has2518coordinates over
p=2^521-1, dimension1259, and separation4/5 of the gap. Its generator
failure is below2^-128. `verify_sample.py` independently replays every
coordinate by root products and proves the far distance, prime, Elias
inequality, and probability terms using integers. The individual sample's
all-parameter coverage is NOT deterministically certified.

Run the standard-library checkers from the repo root:

    python3 research/paired_domain_warp/verify_joint_images.py
    python3 research/paired_domain_warp/verify_multiblock_finite.py
    python3 research/paired_domain_warp/audit_multiblock_independent.py
    python3 research/paired_domain_warp/verify_sample.py

`generate_sample.py --output /tmp/fresh-paired-sample.json` draws a fresh
sample and refuses to overwrite an existing file. The smaller one-pair
curve argument andM127certificate are retained as a supplementary route
in `single_pair.tex`, `verify_geometry.py`, and `verify_finite.py`.
