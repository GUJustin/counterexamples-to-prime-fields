# Nearly complete rational fibers at large Frobenius index

Theorem 2.8 and Appendix E of `paper.tex` show that a degree-B rational
map whose complete B-point fibers cover all but c points of mu_n is
geometrically Galois with torus deck maps when p = ell*n +/- 1,
ell >= 6, and n > 6*(B-1+c). If c<B/2, the action is free and the
preceding corollary gives the power and free twisted-inversion
classification. Full balance is the special case c=0.
The proof is self-reviewed; no independent coauthor review or novelty
claim is asserted.

At p=2130706433 and n=262144, this covers every possible balanced degree
through 32768. The remaining degrees give at most four fibers. This
restricts full-fiber constructions from a fixed map; it does not improve
the pinned better.codes display of 116.13.
The extension also excludes degrees 513, 514, and 516 with coverage
defects 1, 4, and 16, respectively. Their hypothetical counting ledgers
are saved for provenance; they are not achieved scores.

## Verification

Run from the repository root:

```sh
python3 research/structured_domains/frobenius_index/verify_rational_frobenius_index.py
python3 research/structured_domains/frobenius_index/verify_balanced_rational_pencils.py
python3 research/structured_domains/frobenius_index/check_near_balanced.py
```

The first script uses Python's standard library. It checks 87,379 exact
inequalities, sample Wronskians in both congruence classes, and enumerated
small finite-field deck groups. The second requires clang++ with C++17;
it exhausts 27,273,130 disjoint pairs of possible complete fibers on five
small domains. It includes non-Galois examples outside the hypotheses.
The pair enumeration tests pencils up to output Moebius transformation,
allowing the two selected fibers to map to zero and infinity. A finite
output relabeling can move the pole outside the domain image.

The third check tests 26,880 exact inequalities and exhausts 1,823,695
additional pencils, including 2,106 qualifying positive-defect pencils.
It also verifies ramified examples at and beyond the strict free-action
cutoff. See `NEAR_BALANCED_RATIONAL.md` for the proof extension.

All three checks are part of `make verify`. Saved JSON results record the
exact evidence. Resource reports record sequential runs with a 384 MiB
process-group RSS watchdog. Fast runs may finish between RSS samples;
reported peaks are sampled, not exact operating-system high-water marks.
These finite checks supplement the proof, not replace it.

## Provenance

The proof and checks originated in the September 16 staged research.
Integration added a direct Wronskian-independence calculation, clarified
that all deck graphs are removed in the collision-component argument,
and made the first checker's output independent of the working directory.
The sources for the classical method and tame group classification are
cited in the manuscript and the detailed proof note.
