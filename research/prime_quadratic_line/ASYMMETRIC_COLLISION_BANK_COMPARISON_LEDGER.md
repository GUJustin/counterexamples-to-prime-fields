# Asymmetric collision bank: what improves and what does not

September 18, 2026. Proof: asymmetric_collision_bank.tex; independent audits accompany it. These are comparisons among the proved constructions, not a historical-priority claim.

## Parameters

Rate is 3/n. Let A be the exact maximum agreement of either endpoint and the exact ordinary common agreement, and T=A+d the threshold. The construction gives:

- capacity margin eta=(T-3)/n=Theta(n^(-1/2));
- loss epsilon=d/n=Theta(n^(-2/3)/(log n)^2);
- loss/capacity-margin ratio d/(T-3)=Theta(n^(-1/6)/(log n)^2), still tending to zero;
- prime p=Theta(n*(log n)^4);
- at least 2^(-19)*p singleton exceptional labels;
- relaxed threshold-A list bound R+1 with R=Theta(n^(1/3)*(log n)^2), local to the received line.

A successful witness may agree on more than T coordinates. The normalized exceptional fraction is constant, but its absolute count is only n times a polylogarithmic factor. The earlier symmetric bank has a smaller loss and larger absolute count n^(5/4)log n; the earlier Sidon grid has still smaller loss and still larger absolute count n^(4/3)log n.

## Mechanism

The rich component uses small rational slopes. The filler component makes each rich bank polynomial agree on many core coordinates without making its own bank polynomials equally close. Fillers stay uniformly below A even after the grid is added. Therefore only the rich component must be screened for label collisions. This changes the field-size budget from L*H*M to R*H*M, where R is much smaller than the total bank size L.

The exact identity A-Aprime=(s-t)*(s+t-2) is essential: the filler agreement deficit is of order s^2, much larger than its possible fresh fiber. This is not a heuristic typical-case exclusion.

## Scoped ceiling and remaining obstacle

For one translated M-by-M grid with p>2(M-1)^2, every d-rich slope has rational height at most floor((M-1)/(d-1)). The existing height-and-incidence argument gives B<=16*M^4/d^3 for d>=2, up to any separately counted exceptional outsider. Thus M=O(sqrt(n)) and B=Omega(p), with p>=n, force d=O(n^(1/3)). The asymmetric construction attains that exponent up to logarithmic factors.

This is an optimal exponent within this grid mechanism only. It is not an upper bound on arbitrary Reed--Solomon counterexamples. The broader proportional-fresh-word plane-incidence gate leaves nonconstant f/g and general quadratic banks outside its scope.

The gap remains much smaller than inverse logarithmic normalized gaps at fixed rate. The construction does not establish fixed-rate progress, prescribed-domain behavior, better.codes improvement, or nonvacuous n^2 exceptional-count tightness. Since p=o(n^2), an O(n^2) count bound is still vacuous on this family.

At the matched prime size, the elementary uniform-word bound is
Pr[agr_3(U)>=T] <= p^3*(e*n/(T*p))^T
= exp(-(1/2+o(1))*T*log n).
The Crites--Stewart all-label entropy hypothesis would require dimension at least (1/2+o(1))*T, rather than three. These checks exclude those immediate certificates at these parameters, not all adaptations of the prior papers.
