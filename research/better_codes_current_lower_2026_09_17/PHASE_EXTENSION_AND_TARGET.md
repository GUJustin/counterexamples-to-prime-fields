# Finite phase extensions and the next centibit

These experiments use the pinned proximity-prize repository revision
`cdb451f13fdc6c84f5fe363e77ee13a89bd30974`, with the input paths and SHA256
digests recorded in `source_inputs.json`. They do not establish a new score.

The incumbent has integer agreement threshold 181284. The next 68.12 target
uses threshold 181275. The incumbent ledger budget is 274980720549750805.
Its worst row is `(r,v,z)=(35,124,9090)`, with charge 274693043573515013 and
margin 287676976235792.

## A constructive finite extension

`repeat_phases.py 3` appends three explicit cycles of the seven available
sources to the ten incumbent phases. Each new prefix is computed from
strictly earlier phases and already computed parent rows; the computation
does not invoke a circular fixed point. The first repeated source reduces
2109 prefixes, and the next two reduce 23 each. The remaining appended
phases produce no further reductions. The binding ledger charge is unchanged.

This is an arithmetic extension, not an already ported Lean theorem. The
primary `phasePotential` and source-soundness lookup definitions default to
source 05 after index 9. Both must be replaced with the explicit new schedule,
and the finite coverage bounds must be reproved, before using a longer
certificate. The underlying induction is compatible with finite repetition.

## Target diagnostic

The five `target_thresholds_*.json` files recompute all 4970 context rows at
agreement 181275 with the seven original source shapes. The exact first-jet
kernel gaps, power-band thresholds, phase potentials, and minimal monotone
prefixes are recomputed. The incumbent base, complement, chain, packing, and
component box are deliberately frozen. Consequently these numbers diagnose
one part of the target calculation and are **not a soundness certificate**.
The primary sources A/B and total-cap gates also need separate repairs.

With ten phases, 78 context rows exceed the budget. The worst charge is
275819746156863944, an excess of 839025607113139. Its dominant parent prefix
increases from 266528645520722343 to 267655007102152307.

`repeat_phases.py 3 --target` propagates 31 explicit phases in this target
diagnostic. Its worst charge is 275547357531479674: repeated cuts recover
272388625384270 of the charge, leaving excess 566636981728869 (about 0.206%
of the incumbent budget). No new reductions occur after phase 17. This is a
real improvement of the conditional arithmetic, but it neither pays the
remaining target deficit nor addresses the independent source/base repairs.

The scripts maximize each piecewise-affine ledger over interval endpoints
and the two nearest integers to pairwise line intersections. They recompute
prefixes in increasing `(r,v)` order and enforce parent/previous-v
monotonicity. Resource reports show all jobs within 384MiB and 60 seconds;
the 31-phase target diagnostic took 13.65 seconds and approximately 113 MiB.

The useful next construction target is a new source or stronger charge
bound at the high-rank/high-middle-rank bottleneck, together with primary
source repairs. Repeating the same seven sources alone does not close the
remaining gap in the tested finite schedule. This is not a general
optimality or impossibility statement.
