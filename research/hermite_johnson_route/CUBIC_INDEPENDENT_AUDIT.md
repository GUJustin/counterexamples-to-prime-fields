# Independent cubic-extension audit

Audited `CUBIC_EXTENSION.md` against the quadratic manuscript and specialization lemma. The extension passes.

- For generic cubic leading coefficienta≠0, the discriminant is the standard degree-four expression. At a specializeda=0 it becomesb²(c²−4bd), so every singular actual quadratic specialization is still included. Ifa=b=0, a singular linear/constant specialization also has discriminantzero. Thus degree drops require no extra uncounted labels in the nonzero-discriminant case.
- For a(v−r)²(v−s), direct expansion givesU=a²(r−s)² andV=2a²r(r−s)². ThereforeV/(2U) has the correct sign and is the unique repeated root whenU≠0.
- WhenU=Delta=0 and a≠0, characteristic different from2,3 givesc=b²/(3a),d=b³/(27a²), hence repeated root−b/(3a). These identities remain valid after any permitted specialization.
- DegreesDelta≤4h,U,V≤2h imply at most4h exceptional labels per nonordinary coordinate. In the persistent double-root case the explicitly excludedaU has degree≤3h; in the triple-root case the leading coefficient has degree≤h. Lower generic degrees are separately and exhaustively handled. The union count4hn is uniform across candidates.
- Prescribed rational first jets have numerator/denominator degree≤2h. Multiplying the Hermite expansion byE^B gives challenge degree≤H+B(2h+1), so the displayed floor choice ofH satisfies the same strict interpolation dimension gate.
- The regular-incidence bound uses the original equation'sB0,H0. Neither the rational jet height nor the cubic discriminant is substituted as a new original equation. The final incidence argument continues to use every original value agreement.

The sufficient combined characteristic assumption is characteristiczero orp>max(D,3,B), withB the bounded interpolationY-degree. The same positive-rate and signed-margin hypotheses are retained, including the ordinary-core loss. This is a bound on actual polynomial solutions of one bounded-complexity common equation; it does not assert that arbitrary first-order interpolants have derivative degree≤3.

The structural observation is correct: a nonzero cubic has at most one distinct repeated root, while a quartic can have two. It identifies the limit of this single-rational-jet proof, not a universal obstruction for quartic equations or all proximity gaps.

No additional numerical search or Lean compilation was performed for this independent symbolic audit.
