# Exact affine-in-L source routing gate

Fix source multiplicitym and slope caps, and factor weights(r,y,t), with1≤r≤y≤t. Let D=mA, δ=A−w+1, Y=floor((D+s−1)/w), and f=min(floor(Y/y),floor(s/r)). Assume2s≤m, s≤floor(D/w), and f≥1. All other source and field hypotheses remain as in LOCAL_SINGLETON_SOURCE_AUDIT.md.

Define dc=wy−r. The initial thin contact cap can be either H1=max(0,w(Y+1)−s−dc), as in the incumbent SourceNumbers adapter, or the stronger H1=max(0,D−dc). Put

Hh=max(0,H1−(h−1)(δ+dc)), sh=s−hr,
Eh=min(Y−hy, floor(max(0,Hh+sh−1)/w)).

These values are independent ofL. A sufficient saturated lower endpoint is

L0=max(Y,m+s−1,t,ft,max_{1≤h≤f}(ht+Eh)).

For every integerL≥L0, the exact coefficient count C(D,L,s), the retained local rank R(m,L,s), and the thin budget B(L)=δΣh channel(L−ht,Eh,sh) are affine inL. Consequently F(L)=C(D,L,s)−nR(m,L,s)−B(L) is affine inL with integer coefficients. Two exact probes atL0 andL0+1 determine it throughout this interval.

## Why each quantity is affine

The source coefficient count is

C=Σ_{j=0}^s Σ_{a≥0:wa+(w−1)j<D} (D−wa−(w−1)j)(L+1−j−a).

The maximum possiblej+a is floor((D+s−1)/w)=Y, so L≥Y removes all total-degree truncation of this summation. Its index set is then independent ofL and every summand is affine. The weaker conditionL≥floor(D/w) alone is insufficient across a residue crossing. Current high-L searches automatically satisfy the stronger condition.

The existing closed local-rank expression is affine under2s≤m andL≥m+s−1. It is the same exact expression already used for the source certificates.

The fuel is min(floor(L/t),floor(Y/y),floor(s/r))=f onceL≥ft. In channel(T,E,S), onceT≥E, the indices i,j with0≤i≤S andi+j≤E are independent ofT; channel=Σ(T+1−i−j). Its slope is

β(E,S)=(k+1)(k+2)/2+(S+1)(E−k), k=min(S,E).

The conditionsL≥ht+Eh give precisely this saturation for every postdivision channel. Thus all floor/residue changes are fixed before taking the two probes.

## Characteristic endpoint and exact strict feasibility

For use up to totalTmax≥t with the same fixedr,y, the mixed-characteristic upper endpoint is

U=min(floor((p−1−Tmax·s)/r),floor((p−1−Tmax·Y)/y)).

Also require r,y,Tmax<p andys+rY<p. IfU<L0 the certified interval is empty. Writeb=F(L0), a=F(L0+1)−F(L0).

- Ifa>0, the minimum strict feasible integer is max(L0,L0+floor(−b/a)+1); feasibility is exactly whether this is≤U.
- Ifa=0, the whole interval passes iff b>0.
- Ifa<0, feasibility is exactlyb>0, and the passing interval ends at min(U,L0+floor((b−1)/(−a))).

A positiveF implies both positive kernel nullity and strict thin routing because the band budget is nonnegative. For fixedm,s,r,y,t, stage-zero helper cost is nondecreasing inL; therefore the smallest feasibleL is the cheapest source under this saturated-interval restriction. No claim is made about smaller unsaturatedL, where a piecewise analysis would be needed.

## Exact source-D sharpening is valid

The generic theorem `exists_strict_helper_split_of_batch_source_thin` uses D−actualContact, not the rounded shape upper bound. The existing adapter establishesdc≤actualContact and invokes `powerBandBudgetThin_mono`. Hence replacing its rounded initial cap w(Y+1)−s−dc by D−dc is valid: D−actualContact≤D−dc. This changes neither coefficient/rank counts nor characteristic gates. The improved route predicate must retainD (or equivalentlym); the incumbent SourceNumbers structure omitsD and therefore uses a shape-derived upper bound.

## Implementation and verification

`affine_local_source_gate.solve(m,s,r,y,t,gate_t=Tmax,exact_degree=True)` implements the stronger cap; the defaultFalse reproduces the rounded cap. It returns exact endpoints and slope, plus the minimum passingL if any. It is lightweight and has no import-time receipt replay. `verify_affine_local_source_gate.py` checks small coefficient/channel counts against direct sums and checks nonadjacentL values against the affine prediction;1245 exact checks passed for the rounded-cap version. ExactD changes only the fixed channel caps; the same proof establishes affinity. Target theorem port and final receipt validation remain separate obligations.
