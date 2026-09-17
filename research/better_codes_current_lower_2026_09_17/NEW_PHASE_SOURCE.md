# A new source clears the frozen-base phase deficit

At target agreement 181275, a new first-jet interpolation source appended to
the 31-phase diagnostic makes all 4970 existing ledger contexts pass. This
is constructive progress inside the current proof architecture, **not a
complete 68.12 certificate**. The base and packing inputs, derivative-chain
charges, primary B/TCap sources, and original component box are still frozen.

The best of three fully propagated finalists is

\[
(m,L,s,Y)=(350,31116,107,484),\qquad D=181275m=63446250.
\]

Its coefficient count is 40881618929493603 and its local rank bound is
155599707384. Therefore its certified dimension lower bound is

\[
40881618929493603-262144(155599707384)=92089237022307>0.
\]

The associated linear phase potential has coefficients
`(23071889772,1413934061769,6458432636841)` in the coordinates
`(total,middle,slope)`. The worst resulting ledger charge is
274874442495903237, below the unchanged budget 274980720549750805 by
106278053847568 (about 0.03865%). The binding context remains
`(r,v,z)=(35,124,9090)`. Its new phase inherits its prefix from `(17,45)`,
whose raw prefix requirement is 267947979335334905.

The complete 4970-row ledger is saved in
`new_phase_refined_finalist_0_all_rows.json`; its summary is
`new_phase_refined_finalist_0.json`. The saved intermediate state is an
ignored cache artifact rebuilt by the scripts, not a new primary input.

## Applicability audit

`audit_new_phase_parameters.py` checks the numeric hypotheses appearing in
the pinned source adapter, not just positivity of the dimension count:

* `D+s <= 131071*(Y+1)`, with slack 123078;
* `s <= m < 2130706433`;
* the closed coefficient-count residue and rank-formula hypotheses;
* the three mixed characteristic gates throughout the original box
  `r<=35, middle<=159, total<=9275`, whose maxima are
  `(2081485,9436544,33953)`, all below 2130706433;
* the three inequalities in `leftRegularCountCap_le_linear`, with exact
  positive slacks `(32451,40423,31340)`.

The general constraint-kernel dimension bound and helper monotonicity apply
to these numeric parameters. However the pinned Lean `helperPair`,
`PhaseKernelRealization.weighted`, routing arithmetic, and coverage interfaces
contain the literal incumbent agreement 181284. They must be explicitly
ported to 181275. The longer phase schedule also requires new lookup
definitions and finite coverage proofs. No Lean compilation of that port is
claimed here.

## Bounded search and reproduction

The initial grid tested 504 shapes. A refinement tested 1144 shapes against
12 selected ancestor contexts. These are optimistic ranking filters; the
actual inherited prefix can originate at an untested ancestor, as happened
here. Exactly three distinct finalists received complete context propagation:

| Source `(m,L,s)` | Passing rows | Minimum ledger margin |
|---|---:|---:|
| `(250,16250,75)` | 4970 | 17519224691198 |
| `(350,31116,107)` | 4970 | 106278053847568 |
| `(350,33250,105)` | 4970 | 94922511412773 |

Run `fetch_primary_sources.py`, the baseline/target replay scripts described
in `PHASE_EXTENSION_AND_TARGET.md`, then `search_new_phase.py`,
`refine_phase_grid.py`, and `evaluate_new_phase.py 0 --refined`. The last
command recomputes the best finalist and exports every row. All numerical
jobs were run under the repository 384 MiB / 60 second watchdog.

The next dependency is primary source repair. In particular, the feasible
primary A candidate with `(q,s,L)=(163,36,176421)` changes the component box
to 5238 contexts. Its smaller total degree helps the complement charge, but
the 268 added contexts and enlarged phase potentials must be audited; the
4970-row result cannot be substituted into that larger box unchanged.
