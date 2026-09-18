# Independent audit of the restored target second-jet profile

**Source gate PASS; routing is conditional on the listed target ports
and context gates.** The arithmetic for
(m,B,s,U,k,n0,L)=(108,41,19,146,4,7,2557) at agreement181275 is correct.
This is an independent mathematical/source-code audit, not a Lean build
or a complete benchmark certificate.

Primary cached definitions inspected:

* `LowerGeometry.lean`: SecondJetRelaxedRank, RelaxedCounts,
  RelaxedDifferentiation, RelaxedInterpolation, SecondJetRegularData,
  SecondJetFixedStage, SecondJetIdentity and HybridGatesC2;
* `LowerFoundation.lean`: UnequalParameters and flagMixed;
* `SecondJetRefinements.lean`: helper_or_divisibility,
  count_of_interpolant_total, bound_eq_numeric and avoidance_total.

## Exact source and reserve accounting

The source monomial flags are 2h+j<=B, h<=s, h+i+j<=U,
h+i+j+z<=L. Its weighted cutoff is

    m*A-reserve(k,n0,h)*(A-(w-2)),
    reserve(k,n0,h)=h if h<n0, and k otherwise.

At the target A=181275,w=131071, the reserve decrement is50206,
not the old50284. The exceptional low coefficients h=5,6 must retain
their own reserve; replacing every reserve by k=4 would invalidate the
leading-coefficient branch. For requested derivatives d<=k, every
surviving original h has h>=d and reserve>=d. Differentiation in the
second-jet variable lowers weighted degree by d*(w-2), and the reserve
therefore gives weighted degree strictly below (m-d)*A. The local
derivative contact is at least m-d. This exactly preserves the primary
`derivative_weight` and `derivative_vanish` argument at the new A.

The rank-profile script matches the primary source rectangle and kernel
rectangle definitions, including q=max(ceil((m-r)/2),m-r-(s-h)),
the extra condition m-r+2h<=B, and the degree shift h+q. Python's
possibly negative second argument to max is harmless because the
first argument is positive; the independent audit uses explicit natural
subtraction. The source X-exponent count is the strict weighted-budget
count, with no missing endpoint.

Direct integer monomial enumeration, independent of the closed-form
script, gives:

    C=496877347482, M=30748718496757,
    R=1887186, T=96199851,
    source dimension=(L+1)C-M=1240263536362199,
    local rank upper bound=(L+1)R-T=4731221937,
    source dimension-262144*rank=2092909271>0.

These are stored in `audit_restored_general_gate.json`. Every closed-rank
hypothesis passes: 2s<=B<=m, m+s<=U, m+B+s<=L, and all cutoff-derived
caps are at least147>U146. Also k<m, k<=s, s<m, B<=U<=L,
k+1<=n0, and 2(n0-k-1)<=B. Factorials through s=19 and k=4 are
nonzero at the pinned prime2130706433. The source weighted budget
mA=19577700 is also below that prime.

## Activation and both geometric alternatives

The routing theorem requires L<wt(residualTotalWeights,F), not merely
L below an arbitrarily chosen upper bound for that weight. In the
existing own-shape interface, `Own S` proves the actual weight equals
S.t. Thus L2557<t3261 legitimately activates the critical context
only after that own-shape witness is supplied.

The final count is the MAXIMUM of the proper-helper and retained
alternatives, including the exceptional leading-coefficient proper
count in the retained branch. The positive source nullity alone does
not imply that this maximum improves the incumbent singleton bound.
The exact costs are being audited separately; this note does not
replace them by the smaller alternative.

At the binding context (r,y,t)=(12,55,3261), proper-helper caps are
(R,Y,T)=(250,1172,64497). Their three mixed characteristic costs are
(1589214,7369227,27814); the coefficient pair costs are
(164385,616741,4007). All are below the prime.

There are ADDITIONAL retained C2 characteristic gates, independent of
these small helper pair costs. Conservative context-specific versions
are

    reduced=(1+(w+1)(2y-2))*r+y*(2r-2)*(w+1),
    identity=(1+w*(2y-2))*r+y*(2r-1)*w.

At (12,55) these are328466444 and335672843 and pass. At the old
uniform box (30,136) they are2095579166 and2113388834 and still pass.
At the expanded box (36,163) they are3024355364 and3045696863 and
FAIL against2130706433. Therefore this profile cannot simply be
enabled uniformly on every expanded-box context. A per-context gate
or a separately improved geometric characteristic argument is needed.
The cached Data interface additionally retains t<=6917,y<=136,r<=30;
using it outside these bounds requires an explicit port, even if a
particular sharper numerical gate passes.

## Target constants requiring coordinated updates

The source and geometric target adaptation must change all of:

    agreement181353 ->181275,
    errors80791 ->80869,
    reserve gap50284 ->50206,
    agreement-minus-degree gap50282 ->50204,
    ceiling numerator offset50281 ->50203,
    errors-plus-one80792 ->80870.

This affects the cutoff and Interpolant definition, derivative and
low-leading-coefficient vanishing, Data.agreement and Data.noPencil,
all UnequalParameters constructions, regular/proper count denominators,
identity-tail incidence bounds, and the cached affine ceilings.
The constants262144,131071,131073,131074,131076 and2130706433 retain
their meanings; in particular131076=w+5 is not agreement-dependent.
The hybrid rational-coordinate gate still passes since80870<=131076.

The retained identity-tail branch requires an additional target
inequality, not a blind reuse of its old numerical theorem:

    131073*80870*identityCurveDegree
       <=50204*flagMixed(flag,reducedABS,rationalABS).

The independent script expands the difference after a=a'+2,b=b'+1,
s=s'+1. It is linear in the three flag coordinates and quadratic in
a',b',s'. Every coefficient is nonnegative. The three constant terms
are3403566806837518,6806995426311568,6713708058693544. All coefficients
are recorded in JSON, giving an exact algebraic proof of this updated
inequality. This port therefore survives; it is not an unresolved gate.

## Status

The repaired profile is a valid positive dimension construction under
the parameterized target version of the primary interpolation theorem.
At the binding context its explicit source, activation, factorial,
helper and retained characteristic gates pass, and the target
identity-tail domination is verified. Applying it in the complete
receipt still requires the actual own-shape and regular-seed data,
the MAX of both geometric costs, target versions of the hardcoded
theorems, and per-context characteristic applicability. No compiled
formal target theorem or improved better.codes score is claimed.
