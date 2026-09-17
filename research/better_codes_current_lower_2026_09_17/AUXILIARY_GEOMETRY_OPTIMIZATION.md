# Bounded auxiliary geometry optimization at the binding singleton

Target agreement is 181275. The fully repaired receipt currently fails by about 2.1042e16. The binding ancestry reaches the zero-slope singleton at `(r,v,z)=(12,43,3206)`, where root group 11 gives 288191873412750740. This is immediately before phase source 00 activates at z=3207.

We varied each of group 11's three sources independently by dm,dB,dU in [-2,2], ds in [-1,1], keeping k,n0 fixed. For every shape the exact affine kernel surplus determines the minimum feasible L. Candidates must already activate at the actual contact. The objective is the actual rounded maximum of the three helper lines and retained-graph line, not L alone.

| Source | Best parameters (m,B,s,U,L,k,n0) | Contact reduction | Qualification |
|---|---|---:|---|
| 5 | (158,62,28,215,3230,7,10) | 189524100265891 | Later activation; no global improvement claim |
| 21 | (111,46,21,151,3169,5,7) | 16807212668 | Globally nonworsening replacement |
| 22 | (187,83,38,254,3240,9,10) | 76477182371741 | Later activation; no global improvement claim |

The source-21 replacement is exactly the already available source-25 shape. It lowers s and L while preserving all other geometry parameters. Thus every helper/coefficient bound weakly decreases, the graph weakly decreases (only z-only budget decreases), and activation weakly improves. Its improvement is numerically negligible. Its identity absorption was checked independently rather than inferred from monotonicity in the favorable direction.

For all three finalists, exact kernel surplus is positive; source shape gates pass; every affected group's three target identity absorption polynomials have nonnegative coefficients in r-3,v-2,z-3; and helper characteristic gates pass even at corner (36,163,9678). The independent script `audit_aux_geometry_candidates.py` records these checks. No Lean port or complete regenerated receipt is claimed.

An analytic sensitivity calculation explains the small tradeoff. For f=(z,v,r), t=r+v+z and a source budget flag (L-U,U-B+n0,B-2(n0-k-1)), the derivatives of mixed(f,direction,budget) with respect to (L,U,B) are:

- first slot: (0,r,v);
- middle slot: (r,0,t-r);
- third slot: (r+v,z,0).

This identifies zero-direct-graph-cost directions, but interpolation feasibility and activation counteract them. These bounded searches do not establish any global optimum. They do show that the immediate small-neighborhood geometry repairs recover far less than the present deficit; an earlier-phase activation or a substantially different source family remains necessary.

Reproduction: run `auxiliary_geometry_optimizer.py 11 SOURCE 12 43 3206` for SOURCE in 5,21,22 using the standard 384 MiB/60-second guard, then run `audit_aux_geometry_candidates.py` with the research-toolchain Python. Per-job JSON resource and result files are saved alongside this note.
