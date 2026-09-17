# Finite high-L feasibility under localized characteristic caps

This note incorporates the frontier agent's exact finite evaluations in
better_codes_current_lower_2026_09_17/local_singleton_source_grid.json.
It does not prove a global impossibility theorem for all source shapes.

## Exact affine-in-L gate lemma

Fix m,s,Y and a context (r,v,z), put y=r+v,t=y+z, and

    F=min(floor(Y/y),floor(s/r)).

Assume r,y>0 and L>=Y+F*z, as well as the source's dimension/rank shape
hypotheses. Then the complete thin loss is affine in L.

Indeed L>=Y+F*z>=F*t makes the fuel equal to F, independently of L.
At every step h<=F,

    L-h*t >= Y-h*y,

so the channel's U=min(total_budget,jet_budget) is determined solely by
the jet budget, including its independently computed thin cutoff.
Writing B=total_budget-U, the channel formula is affine in B and hence
in L. The coefficient count is affine in L once L>=Y (its total-degree
cap does not truncate the weight region), and the exact local-rank
formula is affine in L. Thus the FULL signed gate surplus

    coefficient_count - n*local_rank - thin_loss

is exactly affine in L on this range. Two exact evaluations determine
its slope and intercept; no L grid is necessary. A passing source needs
strictly positive surplus. For positive slope one can solve for the
minimal passing integer L and compare it with the characteristic cap.
For nonpositive slope, increasing L cannot repair this fixed(m,s) gate.
This is an arithmetic statement, separate from the formal justification
for applying a source locally or charging its exact helper count.

## What the actual samples show

At m=28000,s=8529 and z3206, exact normalized surplus (divided by w*m^4)
is:

    L/m=130: -.00039499489537686696
    L/m=260: -.00062808062451938690
    L/m=520: -.0010942520828044267.

These points lie safely in the affine regime: F=704,Y=38724 and
Y+F*z=2295748, below even L=3640000. Their exact finite slope with
respect to lambda=L/m is approximately

    a_m = -1.79296714725e-6.

The corrected continuum slope at this sigma is about +7.7875e-7.
Consequently the leading finite slope correction is approximately

    a_m-a_infinity ~= -.0720/m.

The previously observed roughly18/m total penalty at lambda260 was
therefore NOT lambda-independent: 260*.0720=18.72. Multiplying L under
a looser local cap also multiplies this penalty. This resolves the
specific apparent high-lambda opportunity.

As a useful asymptotic guide, positive large-lambda slope would require
m around92500. The localized characteristic cap is approximately

    m*(55*lambda+9678*gamma)<2130706433.

At lambda260 it allows m only around77000; at lambda2700 it allows only
around13200. Thus the local cap still conflicts strongly with the
multiplicity needed for positive high-lambda slope. These rounded
comparisons are diagnostics, not uniform rigorous bounds over m,s;
the exact finite evaluations and affine lemma are the rigorous parts.

The frontier's bounded local-source tests corroborate this explanation:
the best reported local shape was m120000,L8400000,s37168,Y165963,
activating at z3191, just two earlier than its best globally admissible
shape. The singleton value improved to286812541719741796, while the
high-lambda candidates did not repair the deficit. Formal source
applicability and the exact local helper charge are audited separately.

## Decision

Do not pursue another blind high-lambda grid. At a fixed(m,s), first
compute the exact affine L-slope. If it is negative, the direction is
closed immediately, even with extra characteristic headroom. If positive,
solve the gate threshold algebraically and check the actual local cap
and full singleton charge. The remaining gain observed here is a small
low-lambda refinement, not the proposed large high-lambda bypass.
