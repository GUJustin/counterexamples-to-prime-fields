# Direct comparison with a recovered coauthor draft

**Superseded for current theorem statements by EPRINT_2056_COMPARISON.md.**
The public ePrint has quadratic/fourth-power first-order gap bounds.

Recovered September17 from the continuing Dropbox sync. This supersedes
the older excerpt-only comparison for the statements below, but is NOT
a claim that the recovered file is the user's latest version.

Title: Quantitative Reed–Solomon List Decoding and Mutual Correlated
Agreement: From Johnson to Capacity.
Authors: Quang Dao, Scott Duke Kominers, Justin Thaler.
105 pages; PDF date September2026; local modification September10,13:11.
Source:
/Users/jthaler/Library/CloudStorage/Dropbox/Documents-full-2026-09-16/Downloads/rs-capacity-and-correlated-agreement (7).pdf
SHA256:15eb4c909fd65e4d6cb916360a984c4ee0797d75290d707f18cfb46864114991
Local read-only snapshot and extracted text:
tmp/recovered-coauthor-draft/ (not tracked or published).
The previously referenced version(9) has not been recovered.

## Exact current comparison points

* Theorem1.1, page7: first-order agreement a_1(rho)+eta_1, eta_1>0,
  gives list O_rho(n/eta_1^3) and full-agreement-set MCA exceptions
  O_rho(n^2/eta_1^5). Characteristic zero or p>max(k-1,B_partial).
  The finite formulas are displayed in that theorem. This corrects the
  older recovered eta_1^-4 excerpt for this particular version.
* Theorem1.3/page8 and the ordinary theorem give Johnson MCA error
  O_rho(n/(q eta_0^3)), with eta_0 measured above the Johnson agreement
  threshold, in every characteristic.
* Corollary5.6, pages33–34: at fixed rho and small capacity gap delta,
  sufficient order ceil(exp((c(rho)+epsilon)/delta)), where
  c(rho)=rho*log(40/(9rho)). List and MCA exponents are d and d+1.
* Corollary5.7, page34: for 0<delta<6/25 and sufficiently large n,
  order ceil(exp(1.5/delta)) works uniformly in the rate. Characteristic
  zero or greater than n. Constants and eventual length depend on delta.
* Theorems5.8–5.9, page35: field-size-independent n^{O_delta(1)} lists
  and full-support MCA, plus deterministic prime-field decoding in
  B_delta n^{O(exp(1.5/delta))} soft-O(log q) bit operations. These are
  statements of the recovered draft, not an independent proof audit.

## What our current lower bounds do and do not match

The ordinary Johnson theorem's linear dependence on n is already known
to be necessary; the draft itself says this in Section6.6, page45.
Our existing constructions do not match the eta_0^-3 factor.

For the first-order theorem, even matching the n versus n^2 powers is
open in our research. A growing fixed-gap source list in its agreement
regime would address list tightness. A suitable compiler can add a factor
n to exception counts, but the output parameters must also lie in the
first-order regime; the exact-halving compiler does not guarantee this. The subsequent
FIRST_ORDER_PRESERVING_AMPLIFICATION.md shows that a sufficiently small
positive padding fraction does preserve any strict first-order margin.
Do not identify its output with the same first-order threshold silently.

At rate1/4, the recovered curve is

    a_1(1/4)=(3+sqrt(133))/31,

about0.46879, with capacity gap about0.21879. Our new exact Dickson
profile has agreement3/8 and capacity gap1/8. It lies BELOW this
first-order sufficient curve, so it is not a lower bound on the
first-order theorem in its stated regime. Also eta_1 and the capacity
gap delta are different quantities. Blowup as delta tends to zero does
not establish blowup as eta_1 tends to zero at fixed rate.

For capacity, our almost-quadratic inverse-gap logarithmic list lower
bound and the large fixed-gap linear coefficient remain strong uniform
parameter obstructions. They do not force a superlinear n exponent at
one fixed positive delta, or an exponential derivative order. Section6.6,
page46 of the recovered draft makes the analogous quantifier distinction
for the earlier Krachun–Kazanin–Haboeck constructions.

Method sharpness remains a separate potential result: the restored
September13 first-order support-optimum draft claims the exact quarter-
rate curve above as an interpolation-method threshold. Its proof has
not yet been independently re-audited in this takeover. Auditing it is
more concrete than treating the currently open intrinsic exponent claim
as established.

## Older available source is not the same version

Dropbox also exposes ai-generated-papers/rs-correlated-agreement-capacity/
with September5 TeX sources. Its four-author title and exp(6.88/delta)
order are older. Its Proposition(eightlist) gives a different eight-member
boundary bank at rate1/4 and gap0.24, with received degree equal to the
agreement threshold. It is not our p17 deformation at gap1/8 with a
complete above-capacity profile. Do not confuse the two constructions
or describe the mere existence of an eight-member list as new.

Subsequent audit: ../first_order_support_audit/AUDIT.md now checks the
quarter-rate method converse and the two finite high-rate improvements.
The earlier 'not yet audited' sentence above records the state before
that audit; it no longer applies to those precisely scoped conclusions.
