# Bounded search: one pole-fiber point and eleven old base fibers

This search uses a revised support after the all-twelve-base transversal was ruled out by the degree-seven difference from G5. No search was launched for that invalid completion: the initial compile failed before producing an executable. The saved C++ source searches only the valid revised support described below.

## Support and scope

For a generic reciprocal-quadratic seed and its first one-pole witness, split all thirteen fibers of T²+c over the twelve old base points and the first pole a0. Select one point from the pole fiber and one from eleven base fibers, omitting one of the six positive-edge fibers where the first rational witness matched the old word. This gives twelve core matches if interpolation succeeds.

The selected support intersects G5's agreement set in five nodes. Its intersections with the four old lifted candidates have sizes6,6,7,7. Thus the degree-seven difference bounds do not forbid it. The difference from G5 can leave two residual roots for the two fresh coordinates. Existence of admissible residual roots and characteristic-zero lifting require separate checks.

The pole b is required to lie outside the entire 26-point core, not merely the selected twelve nodes. Properness is checked algebraically by the interpolation identity below.

## Fast exact sign test

Choose signs for the first eight roots t_i, fixing the first sign by the symmetry T->−T. There are128 choices. Let L8=product(T−t_i), let P0 be the degree-at-most-seven interpolant through the corresponding W_i, and put

    ell=coefficient_(T^7)P0=sum_i W_i/L8'(t_i).

For a prescribed denominator T−b the numerator interpolant is

    N(T)=(T−b)P0(T)−ell L8(T).

If ell=0 this cancels to the polynomial P0, so it is rejected. At any remaining candidate root t with received value W(t), the required pole is uniquely

    b=t−ell / sum_i [(W_i−W(t))/(L8'(t_i)(t−t_i))].

A zero denominator gives no solution because ell and L8(t) are nonzero. Each remaining fiber provides at most two pole values, one per sign. Intersect the four two-element sets. This replaces4096 independent rational interpolations with128 small barycentric calculations.

When a surviving b lies outside the whole core,

    N(b)=−ell L8(b)!=0,

so the candidate is a genuine proper one-pole rational function. This source test does not by itself certify the fresh-coordinate or lifting conditions.

## Deterministic bounded run

The source is `search.cpp`. The random generator is std::mt19937 with fixed seed20260918. The primes are97 and113. Each prime has a cap of100000 sampled seeds and1000 fully split cores, and each core tests all six omitted positive edges and128 first-eight sign choices. The run was wrapped in the repository's `run_bounded.py` with384MiB and60second caps. Explicit compilation against the already-installed MacOSX15.4 SDK avoided the default SDK linker mismatch; no toolchain installation or environment changes were made.

Recorded counts:

| Prime | Sampled seeds | Admissible seeds | Split cores | Sign patterns | Proper hits |
|---|---:|---:|---:|---:|---:|
|97|30856|23331|1000|768000|4|
|113|27017|21512|1000|768000|1|

The executable completed in1.09seconds. `resources.json` records the watchdog result. `counts.jsonl` includes the two count records and the watchdog's final summary. `hits.jsonl` contains all five raw candidates with seed parameters, first pole, critical value, new pole, twelve selected nodes, corresponding base nodes, and received values.

These are sampled proper finite-field interpolation hits, not a complete parameter classification, not yet certified characteristic-zero constructions, and not growing-list results. Independent verification of the residual fresh-root guard and a full-rank deformation Jacobian is assigned separately.

For that lift one convenient system has27variables: four seed parameters, first pole, quadratic critical value, new pole, eight numerator coefficients, and twelve selected roots. Its25equations are the first-pole identity, twelve square-root equations, and twelve rational-agreement equations. Full rank25, together with all open guards, is a sufficient smooth-lifting certificate. No such rank is claimed by the search executable itself.

## Completed independent verification

All five raw hits subsequently passed the independent residual-root and rank13 norm-Jacobian checks. The first hit also passed the independent pointed25-equation Jacobian check, whose specified minor is21modulo97. `SIX_WORD_LIFT.md` and `six_word_lift.tex` now give the characteristic-zero and arbitrarily-large-prime-field existence theorem. The search executable itself still only claims the preliminary interpolation checks described above.
