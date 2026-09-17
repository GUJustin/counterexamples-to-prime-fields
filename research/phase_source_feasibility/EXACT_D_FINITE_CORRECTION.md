# Exact-D routing: rigorous bound on the removed finite penalty

The source has actual contact bound D=mA and rounded bound
Dbar=w(Y+1)-s, where Y=floor((D+s-1)/w). Thus

    epsilon=Dbar-D lies in {0,...,w-1}.

Replacing the initial thin contact budget Dbar-dc by D-dc is a sound
sharpening once the primary theorem's actual-D premise is used. The
root and independent auditor checked that premise; this note analyzes
only its arithmetic effect.

## Every channel loses at most one Y layer

The thin contact budget is repeatedly decremented and clipped at zero.
The two runs therefore differ by a number in[0,epsilon] at every step.
Their integer Y cutoffs floor(max(0,Dh+ss-1)/w) differ by at most one.
Taking the other channel minima preserves this bound. It can improve
a threshold at an integer boundary, but cannot remove many layers at
one step.

The exact channel formula is

    Channel(T,U,S)=sum_{j=0}^U (min(S,j)+1)(T+1-j),

with U already the minimum of the total and jet caps. Removing its top
layer saves exactly

    (min(S,U)+1)(T+1-U).

For fixed(m,s,Y,r,v,z) in the affine-in-L regime L>=Y+F*z,
F=min(Y//(r+v),s//r), the affected-layer indicators do not depend on L.
Therefore the exact-D thin loss, like the old loss, is affine in L.
Its improvement in the normalized lambda=L/m coefficient is exactly

    delta/(w*m^3) * sum_affected_h (min(s-hr,U_h)+1),

where delta=A-w+1. In particular it is nonnegative and at most

    delta/(w*m^3) * [F(s+1)-r F(F+1)/2].          (1)

No asymptotic approximation or random-residue assumption is used in(1).

## The decisive existing finite sample

At m28000,s8529,Y38724,r12,y55,z3206, F704 and epsilon15946.
Bound(1) is

    5.282109246956777e-8.

The old EXACT normalized lambda-slope, determined by the frontier's
lambda130/260/520 samples, is approximately -1.79296714725e-6.
Consequently the exact-D slope remains at most

    -1.74014605478e-6 < 0.

Thus increasing L cannot repair this fixed(m,s) source even after the
proof-preserving exact-D sharpening. The lambda130 old margin is
-.00039499489537686696. Since T_h+1-U_h<=L+1, its total improvement is
at most (130+1/28000) times(1), less than .000006867. It remains negative.
Combined with the negative slope, this rules out every lambda>=130 in
the affine range for THIS fixed shape, without any further grid.

The old finite slope deficit from continuum was approximately
.0720/m. Bound(1) times m is only .00147899, so contact rounding can
explain at most about2.1 percent of that deficit here. Most of the
high-lambda finite penalty is intrinsic to the other discrete dimension
and thin-count terms, not to the rounded initial contact cap.

## Shape implications and observed thresholds

At m64000,s19840, the all-layers upper bound is .00153189/m; at
m120000,s37168 it is .00152967/m. This scale suggests small threshold
improvements, not a new large-lambda feasible regime. It can still
matter for a singleton exactly one step before activation, so applying
exact-D throughout is worthwhile.

The frontier independently reports source00 threshold3207 unchanged,
source06 threshold3376 reduced to3374, and the small new source threshold
5872 reduced to5860. The critical singleton peak is unchanged. These
are finite arithmetic diagnostics, not a complete soundness certificate.

Continue exact-D local low-lambda candidates near sigma.30975 with
large admissible multiplicity only if their total helper charge helps.
Do not reopen a broad high-lambda grid based solely on this sharpening:
the exact slope test gives a direct rejection criterion. Further gains
require a distinct discrete-count improvement or a different source,
not treating this small removed rounding term as the entire finite loss.
