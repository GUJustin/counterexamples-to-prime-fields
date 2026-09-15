# Independent review of the unconditional radial certificate

**Verdict:** the theorem and exact certificate are valid as stated. The
bound is **5,133,798,314,667** members in a joint two-moment class, hence
the corresponding length-64, dimension-32 Reed–Solomon list for every
prime p>64. The certificate works without conditioning on one chosen
first-moment value. It is not stronger than the current conditional
degree-24 certificate **5,141,180,908,468**, which exceeds it by
**7,382,593,801**.

Reviewed source directory:
`/Users/jthaler/Documents/frontier_attacks_2026-09-15/stwo_port_review/radial_moment_experiment/publication/`.
No files in that directory or the shared manuscript were modified.

## Lattice and coordinate ownership

Write M1=Σa and M2=Σbinom(a,2) for a 30-subset. The displayed coordinates
simplify exactly to

    x = M1 − 945,
    y = M2 − 31 M1 + 9765.

Indeed, Y_a=((2a−63)²−1365)/4=a²−63a+651, and dividing its 30-term
sum by two gives the stated y. Thus (x,y) is an **integer affine
transformation with determinant one** of (M1,M2). No half-lattice,
rational Gram-coordinate, or shear correction is missing. Enumerating
all Z² is legitimate; unattainable signatures have zero multiplicity
and only enlarge the nonnegative denominator.

The total X_a and Y_a sums on the full 64-point population are zero.
Taking complements sends (x,y) to (−x,−y), preserves the radial
quadratic, and bijects the 30- and 34-subset moment fibers. Equal
integer moments then yield the asserted codeword list through the
paper's existing equal-moment lemma. The affine-coordinate changes are
used for integer counting, not as field operations.

The Z² enumeration is specific to this integral centered transform.
A general rational Gram/shear transform requires summing over its
actual affine triangular lattice. The present proof makes no incorrect
claim that an arbitrary such transform has image Z².

## Signed weight and exact compact support

Let Q=(341x²+5y²)/1884025 and A=851547/580691. For any rational
polynomial h, w(Q)=(A−Q)h(Q/A)² is nonpositive when Q≥A and
nonnegative when Q<A. If a_z counts the subsets at a lattice point z,

    Σ_z a_z w(Q(z))
      ≤ Σ_z a_z max(w(Q(z)),0)
      ≤ L Σ_(z∈Z²) max(w(Q(z)),0).

The verifier establishes a strictly positive numerator and denominator,
so taking the ceiling of their ratio is justified. Zeros of h inside
the ellipse cause no problem: their contributions are simply zero.
The strict region T<A D for integer T is precisely
T≤floor((851547·1884025−1)/580691)=2762804. The 210135 points
counted by the code are points in this region, not an assumption about
which signatures are attained by subsets.

The conversion to integer coefficients is exact. If A=a/b, D=1884025,
and H(T)=s h(T/(D A)) after clearing coefficient denominators, then

    W(T) = (aD−bT) H(T)² = b D s² w(T/D).

Both numerator and denominator are multiplied by the same positive
integer. The code explicitly constructs this polynomial, so sign
claims do not depend on approximate roots or sampled evaluations.
Degree 12 refers to h; W and w have degree 25.

## Moment recurrence

Pair the population into (u,v), (−u,v), with u=1,3,...,63 and
v=(u²−1365)/4. At every stage the partial population is invariant under
X→−X, so all moments with an odd X exponent vanish. It therefore
suffices to store X^i Y^j with even i and i+j≤50, giving 676 indices.

The four choices from one pair are: neither, either singleton, or both.
The singleton sum cancels odd powers of u and yields the recurrence

    2 Σ_(p even,q) binom(i,p)binom(j,q) u^(i−p)v^(j−q) M_(p,q).

The both-elements choice adds (0,2v), yielding
Σ_q binom(j,q)(2v)^(j−q) M_(i,q). The copied state handles choosing
neither. Subset sizes advance by 0,1,2 respectively, so the recurrence
counts subsets without replacement exactly.

The stored raw X,Y coordinates are twice x,y. Expanding
T^k=4^(−k)(341X²+5Y²)^k therefore uses total raw degree 2k≤50.
The divisibility checks by 4^k and the exact variance normalizations
agree with this conversion. All operations use Python integers or
exact rational numbers.

## Checks performed independently for this review

1. Ran `PYTHONDONTWRITEBYTECODE=1 python3 verify_publication.py`.
   It passed: 676 recomputed mixed moments, 26 radial moments, 400
   exhaustive small-fixture moment checks, exact rational/integer
   coefficient conversion, and the independent signed-lattice
   denominator computation on 210135 points.
2. Independently implemented a **single-element** subset dynamic
   program, adding each a=0,...,63 separately and updating subset sizes
   downwards. It computed all 28 mixed moments of total degree at most
   six, including odd X powers. Every even-X moment matched the saved
   degree-50 table; every odd-X moment was zero. This uses a different
   recurrence from the symmetric-pair implementation.
3. Audited the affine coordinate identities, complement map, support
   rounding, sign argument, and positive scaling symbolically above.

The full publication verifier is read-only; disabling bytecode output
also avoids creating ancillary files in the source bundle.

## Integration recommendations

- Present this as **an unconditional radial certificate**, explaining
  that it does not first fix one first-moment sum. Both this and the
  conditional certificate are rigorous unconditional existence results;
  the distinction describes their calculation methods.
- Keep the conditional degree-24 number as the paper's strongest
  finite length-64 result. The source's comparison with degree 20 is
  historically true but no longer identifies the strongest certificate.
- Preserve the exact ancillary files and deterministic verifier. Do
  not describe the discovery search as establishing optimality.
- The signed-weight principle is already present in the paper; the
  contribution here is its joint radial specialization and certificate.

## Reviewed file hashes (SHA256)

| File | SHA256 |
| --- | --- |
| moments_degree50.json | `3b625dd854e129e2b608cdda7eb380ec7481a137f8c3333e188e984bc8bb31d4` |
| certificate_degree12.json | `4fafcadb84e2c25e8070398bf5df436da21dea4ecfdfccc34aae4d91ae727b3f` |
| moments.py | `de3c4f9007a0db1e5169d85fc8375197f0bd6dad730d73414f67688a09a72718` |
| verify.py | `0af785228fbfeaaba6cb60dcb28e79c957eadcd706b85e18d39b7841c03fe42d` |
| verify_publication.py | `5ca8ded6580ac46a6948a7ae454f0e681ca0072a6e38f1c977645a6f3199a78f` |
| crosscheck_saved_certificate.py | `c19421536212409de1dd21ba111eec37bbd6a5e6a68d8206b44b9a664ed2db15` |
| radial_certificate_fragment.tex | `dbb73b392dba4cb21072aa3933226d6db0a51d66eaeafe92e201494cfd849c13` |
