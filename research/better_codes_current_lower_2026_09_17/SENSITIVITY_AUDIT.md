# Exact source sensitivity audit for the current lower receipt

September 17, 2026. Target integer agreement181275; baseline181284.
This examines interpolation gates and their declared geometric inputs.
It is not a complete receipt, Lean proof, or better.codes improvement.
The cached primary source definitions, not the ePrint's generic ledger,
are the basis of this audit.

## What actually changes the downstream geometry

MovingFiberProfile6811 defines d=k+1 and the source flag

    (zOnly,yz,all)=(L-U, U-B+n0, B-2*(n0-k-1)).

The coefficient helper uses pair caps (R,Y,T)=(B,U,L). The differentiated
helper uses (B+s*(r-1), U+s*(y-1), L+s*(t-1)) at a geometric cell(r,y,t).
The regular mixed term uses this flag divided by d (through the common
integer scale). Source multiplicity m is ABSENT from all these caps and
from the regular mixed term. It affects existence of the interpolant,
not its subsequent declared geometry once all source hypotheses hold.

Thus changing m alone is the cleanest nonworsening repair. Lowering s
with all other entries fixed improves the helper caps, preserves the
coefficient caps and regular flag, provided the source hypotheses remain
valid. Lowering L improves the third cap and only the zOnly flag entry.
Changing B or U redistributes flag entries, so coordinatewise cap
improvement alone is not a proof that every displayed mixed bound gets
smaller. Changing k or n0 also changes d, the reserve cutoff, and multiple
flag entries; these cannot be optimized by interpolation surplus alone.

More explicitly, write n,w,a for the pair's parameters, g=a-w, e=n-a,
and left agreement vector

    lY=1+2wy, lR=w(2r-1), lZ=2wt+1.

For right caps(R,Y,T), mixed cost is
(rT+tR, yT+tY, yR+rY). The numerator before division by g is

    (n-w)[lY(rT+tR)+lR(yT+tY)+lZ(yR+rY)]
      +(e+1)g(yR+rY).

Its exact increments per unit of T,Y,R are respectively

    (n-w)(lY*r+lR*y),
    (n-w)(lR*t+lZ*r)+(e+1)g*r,
    (n-w)(lY*t+lZ*y)+(e+1)g*y.

The final count is the integer floor after division by g. In particular,
one unit of L can be quite costly even though the dimension surplus is
linear in L. These formulas explain the sensitivity without claiming
that old packed receipt thresholds remain valid after any change.

## Full multiplicity optimization with unchanged source shape

The new search exhausts every m allowed by the existing closed-count
regime B<=m<=U-s, retaining B,s,U,k,n0. It enforces all additional shape
and cutoff assertions used by the exact arithmetic, and does not assume
that this regime exhausts all possible interpolation constructions.
For each m it computes the exact affine surplus in L and the minimum
feasible integer L>=max(U,m+B+s). It checks the passing value and the
preceding failing value whenever the minimum is not forced by shape.

Only source1 admits a target-feasible replacement at no greater L:

    (m,B,s,U,L,k,n0)=(133,56,25,180,2796,6,8).

The original source is (134,56,25,180,2819,6,8). Thus m alone can repair
that source and additionally reduce L by23. For each of the other26
sources, no m in this entire stated regime passes at its original L.
A useful smaller repair is source17: m161 requires L2343, only5 above
its original L2338 (original m162). It still changes the geometry.

The exact per-source minima and every tested m are saved in
multiplicity_sensitivity.json. The complete run took20.12 seconds and
less than21MiB sampled RSS. This extends the earlier +/-2 multiplicity
search rather than repeating its full multi-cap grid.

## Primary A/B/TCap kernels are additional active gates

The primary kernels use a different coefficient model, so their L must
not be confused with the relaxed-source L above. Their baseline exact
coefficient and local-rank counts were independently reproduced from
MovingFiberKernels6811 and the primary closed formulas.

At target181275 the original dimension surpluses are:

| Kernel | Target surplus | Consequence in the tested regime |
|---|---:|---|
| A | -1455824819235 | No L repairs any m<=115,s<=35 in the tested regime |
| B | -155031989640 | Minimum L22192 at m134,s40, versus old18992 |
| TCap | -363409809704 | Minimum L9681 at m226,s70, versus old9281 |

The search covers all m<=oldm and s<=olds satisfying2s<=m and the
one-residue/closed-rank assumptions, with q=floor(mA/w) no greater than
the old q. Surplus is affine in L on the valid shape interval. The script
handles positive, zero and negative slopes, checking the lower endpoint
when a nonpositive slope cannot be repaired upward. Thus the A failure
is stronger than an unsuccessful search over a few larger L values.

A separate45-case neighborhood per primary kernel permits m to increase
by up to8 and s to vary by2. It records Pareto choices in(q,s,L), not
full geometric dominance. For A, m116 gives no repair in that neighborhood;
one example with lower L is m118,s36,q163,L176421, versus original
m115,s35,q159,L274277. This increases two degree caps while decreasing L,
so it is a tradeoff needing a new downstream audit, not a free gain.
For B, m137,s42,q189,L18812 slightly lowers L but increases q and s.
For TCap the neighborhood does not approach its original L9281.

The full scalar results are in primary_sensitivity.json and
primary_tradeoff.json, with guarded reproducible scripts and resource
reports. These checks address positive kernel dimension only. If a
subsequent theorem requires a larger nullity than one, that stronger
requirement must also be restored. Updating the target changes agreement,
phase and packing arithmetic elsewhere in the receipt; none of it is
silently inherited here.

## Practical prioritization

The clean source1 replacement is real but isolated. PrimaryA is a more
serious obstruction than the27-source catalog alone suggested: increasing
its challenge cap L cannot repair the target with the current/lower
multiplicity and derivative cap. A credible next attempt must trade its
shape parameters or improve its rank/constraint accounting, then rerun
the downstream geometry and receipt. This audit supplies exact local
sensitivities and bounded minima, not a claim that such a trade will win.
