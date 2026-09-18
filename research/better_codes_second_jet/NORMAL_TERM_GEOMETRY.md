# Exact origin and a conditional refinement of the retained normal term

Status: primary-source proof tracing and exact arithmetic; no new unconditional benchmark certificate. IMPORTANT: the conditional singleton cost below cannot consume the full MCA allowance. It has not been propagated through the full ledger and does not establish even a conditional benchmark improvement.

At the binding factor `(r,y,t)=(12,55,3261)`, put `w=131071`,
`a=t-y=3206`, `b=y-r-1=42`, `s=r-2=10`. The carrier flag is
`f=(3206,43,12)`, the reduced first-tail flag is
`q=(840433664,11272193,2883584)`, and the rational coordinate is
`R=(420223244,5505110,1310743)`. The exact normal term is
`flagMixed(f,q,R)=352613725068219795`.

## Provenance

Cached `LowerGeometry.lean`, `SecondJetRetainedStage.stage_card_le_scaled`
(around line 21284), obtains component moving budgets and invokes
`SecondJetHybridProvider.exists_provider_on_active_components` (around 17126).
The latter follows the C1 piecewise component argument (around 13540):

* local first-tail intersection multiplicity `mu>=6`: charge `mu*weightedCost(R)`;
* `1<=mu<=5`: charge `weightedCost(R_mu)+(w+mu)*movingCost`, where
  `R_mu=((w+mu+2)a,(w+mu+2)b+2,(w+mu+2)s+3)`.

It then uses `R_mu <= mu R` and sums intersection multiplicities. The resulting
normal term is the mixed flag intersection of the carrier, the reduced first-tail
cut, and the rational-coordinate pole budget. This already uses cumulative flag
support, not an independent-degree rectangular box. The former C1 coordinate
padding was already removed in the restored proof. It cannot be removed again.

The identity-tail branch separately bounds an identity curve and absorbs that
bound into the same normal term (`SecondJetIdentity.identity_le_normal`). Keeping
the smaller identity-branch value does not eliminate the proper-tail branch.

## A sufficient multiplicity certificate

Suppose, additionally, every active proper-first-tail component has local
intersection multiplicity at least 3. This is an EXTRA hypothesis, not a
consequence established for the restored source profiles.

Set `Rnew=ceil(R_3/3)` coordinatewise, so
`Rnew=(140076552,1835065,436921)`.
Use the moving engine for multiplicities 3 through 6. The three coordinates of
`R_mu/mu` decrease with mu, hence `R_mu <= mu Rnew` in this range.
Use the flag engine for multiplicities at least 7. The sharp later-tail flag is
`(2a,2b+1,2s+3)*(w+1+delay)+(0,1,0)`, with `delay<=mu`.
For mu>=7 its coordinatewise ratio to mu is maximized at mu=7; direct integer
comparison gives containment in `mu Rnew`. (Coordinatewise containment suffices
for the cumulative flag inequalities.) The tangent-curve debit is also absorbed,
since `Rnew.yz=1835065 > errors+1=80870` at target agreement 181275.
Consequently the existing component proof yields the conditional proper-tail bound

`normal_new + (w+6)*ceil(moving/(k+1)) + coefficient_helper`.

For the repaired profile `(m,B,s,U,k,n0,L)=(114,47,21,155,5,7,2777)`,

* normal_new = 117539708354527649;
* moving = 7184614079877;
* coefficient_helper = 22124923602288;
* conditional proper-tail retained total = 274518109902868397.

The full MCA allowance is 274980720453263170, but comparing this SINGLETON
cost directly to that full allowance is invalid: other ledger charges remain.
For scale only, subtracting the incumbent critical singleton from the current
worst total gives 7831042001878735. That subtraction is NOT a verified local
residual, since the worst full context is (36,127,9489), different from this
singleton context. Even adding this illustrative residual would produce
282349151904747132, above the allowance. The actual context-specific residual
and propagation need reconstruction. The identity-tail branch, all other
factors, and characteristic gates also require separate verification.
With minimum multiplicity only 2, analogous optimization gives
333285457932572185, insufficient.

## What is missing

Retained second-jet divisibility supplies repeated roots of a component polynomial
and a moving-pole budget. First-tail intersection multiplicity is the valuation of
a different cut in a local DVR. No implication between these quantities has been
proved here. Source parameters `n0>=7` or `k=5` cannot simply be substituted for
first-tail multiplicity. An independent agent is examining concrete simple-component
examples. Conversely, this note does not prove the current normal term necessary:
it only identifies where the existing proof spends it and one exact sufficient
additional certificate that would substantially reduce it.

Expanded-box characteristic failure is separate: the restored C2 mixed gate fails
near `(r,y,t)=(36,163,9678)`. Binding-factor arithmetic does not repair that gate.

## Correct context-specific arithmetic

The existing `repaired_primary_chain.ledger_overhead` evaluated at the SAME
context `(r,y,t)=(12,55,3261)` with repaired B=(189,42,18812) is
7610057517161789. Thus the local singleton has room only
267370662936101381; the conditional multiplicity-3 total plus this local
overhead is 282128167420030186, which FAILS the allowance.

Among these uniform minimum-multiplicity refinements, multiplicity at least 4
is the first sufficient one for this local arithmetic comparison. Moving
components of multiplicities 4 through 9 and using the sharp flag for multiplicity
at least 10 gives Rnew=(105058216, 1376309, 327694), normal=88155518342688946, and retained
cost=245137512198069634. Including the same local overhead gives
252747569715231423. This remains CONDITIONAL on an unproved
multiplicity exclusion and is not full propagation or a benchmark improvement.
The priority is proving or refuting that exclusion, not optimizing hypothetical
minimum multiplicities.
