# Pooled prime-field quadratic intersection certificates

The averaging theorem is in `pooled_prime_corollary.tex`; detailed proof and scope are in `PROOF_AND_JOB.md`. For arbitrarily large primes, it gives more than p/36 singleton bad challenges, length Θ(p^(2/3)), message dimension3, and a threshold above the first-order curve but below Johnson. The rate vanishes and the source gap is one coordinate.

## Exact optimized certificates

| Quantity | Small pilot | Large rental result |
|---|---:|---:|
| Bank size L |25|363|
| Prime p |20,011|47,700,761|
| Length n |1,201|262,813|
| Source/common agreement A |48|724|
| Threshold T |49|725|
| Fresh coordinates |601|131,407|
| Finite incidence-singleton labels |10,731|19,600,551|
| Exact finite singleton threshold lists |10,797|19,622,800|
| Exact finite bad labels |12,630|31,301,642|

The both-far line adds one further bad label, with a singleton list: the infinity word −g. Thus the large certificate has **19,622,801 exact singleton bad challenges (41.1373%)**, and **31,301,643 total bad challenges (65.6208%)**. The singleton optimization target40% was met;45% was not attained. These are finite constants, not an improved asymptotic exponent or a fixed-rate result.

## Algorithm and validation

`swap.cpp` starts with a random allowed fresh subset, maintains exact label occupancies, and accepts a one-coordinate replacement only when the number of occupancy-one labels does not decrease. It excludes core coordinates, zero, and labels0/1. All bank labels at a single allowed coordinate are distinct.

The local run used200,000 proposals. `swap.json` is independently replayed by `swap.independent_replay.json` (another agent's Python implementation) and `swap.checked.json` (direct polynomial evaluations).

The rental used eight seeds101–108, each5,000,000 proposals. All reached at least41.078% incidence-singletons. Best seed101 took96.2505 seconds for optimization after initialization, accepted200,721 proposals, and improved17,547,896 initial singleton incidences to19,600,551. `large/runs_summary.json` records every run. Each worker used about475MB RSS.

`check_large.cpp` independently recomputes labels by evaluating each quadratic and the quartic received word, verifies primality, all node guards, coordinate distinctness, total incidence count, occupancy counts, and distinct incumbent-owner counts. It does not reuse the optimizer's rearranged label formula. `large/best.checked.json` is the remote replay; `large/best.local_checked.json` repeats it after download. The proof that no other quadratic reaches T uses the structural bound L core plus4 fresh matches, rather than enumerating all p³ quadratics. A label's threshold list consists exactly of the distinct bank owners appearing at that label; repeated incidences of a single owner still give a singleton list.

The winning coordinate certificate is `large/best.json` (also flat integer input `large/best.flat`). The local archive `large/results.tgz` preserves all eight runs and sources; the repository includes the winning certificate and all-run summary; `large/manifest.json` records hashes.

## Resource receipt

Exactly one Vast instance was used, with16 effective CPU cores; its GPU was unused. The instance existed for279.2 seconds, about4.65 minutes, including installation, optimization, replay, and transfer. Estimated compute charge is $0.042 at about$0.536/hour, excluding small disk/transfer fees; this is not a final invoice. All outputs were downloaded before explicit destruction. `rental_destroyed.json` records successful CLI destruction and a post-destruction lookup with `instances:null`. No rental remains active from this task. The initial CLI destruction required adding `--yes`; the final destroy succeeded, and the saved watchdog has that correction.
