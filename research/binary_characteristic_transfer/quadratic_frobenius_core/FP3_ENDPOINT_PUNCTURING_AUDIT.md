# Endpoint-support puncturing: independent proof audit

September 18, 2026. **PASS.** The resulting theorem is in `fp3_far_endpoints.tex`; it is separate from the all-near unpunctured theorem.

Choose u1=eta u0, so eta Iu1=Lambda0 and Iu1 is a different F_p-line. For fixed nonzero b in Iu1 and distinct v1,v2 in Iu1, both labels b-eta*v_i are generic and have the SAME unique high witness a_u1 X²+b. This follows from the proved exact unpunctured classification, not from an assumption about generic received words.

Deleting its two FULL supports removes one core fiber and two disjoint fresh fibers, at most3p-2 coordinates by choosing the smallest nonzero core fiber and the two smallest trimmed fresh fibers. At either selected endpoint the sole high witness loses every match; all other quadratics retain at most their original p+2sqrt(p) matches. Hence both endpoints are far, and their ordinary common agreement is automatically no larger. Exact endpoint agreement is not claimed.

Every label outside the one excluded direction plane has a different quadratic leading coefficient. A common match with the deleted witness solves a nonzero quadratic on the core, and a nonzero quadratic with a constant shifted by the label on each fresh fiber. Thus at most2+2+2=6 matches are deleted. Its original unique witness retains at least A-6, and every competitor stays below that threshold. The excluded plane has p² labels and already contains the p-label multiple-list locus; therefore at least p³-p² labels are singleton-near. This is not an exact total count of all remaining nearby labels.

The integer threshold is T=2p-ceil(4sqrt(p))-8. At p>=4099 its gap above the source upper bound is at least p-6sqrt(p)-9. With the stated punctured length, the first-order and strict below-Johnson inequalities in the fragment hold. The same m6 derivative-cap3 explainer test is valid with B=3T,H=40B, since B>=29p/5 and n<=2p². No large numerical computation or new ambient field is needed.

This mechanism escapes the previous redundant-third-block obstruction by changing the domain in a witness-dependent way: it removes all matches of two selected endpoint witnesses, while quadratic intersection bounds limit collateral damage to other directions. It preserves the native F_(p³) alphabet and gives near-unit failure with two individually far endpoints. The rate and relative source gap still vanish; no prime-alphabet or fixed-rate theorem is asserted.

Averaging optimization independently rechecked: nonzero core fibers have total p²-p over p-1 choices, so one has size<=p. The p fresh fibers partition trimmed D1 of size p²-p, so the two smallest distinct fibers total<=2p-2. All choices remain generic because b+Lambda0 is disjoint from Lambda0 for every nonzero b in Iu1. This yields n>=2p²-4p+1 without changing the threshold A-6 or the six-root collateral-loss proof. The updated Johnson lower bound is 2n-T²>=16p sqrt(p)-24p+2>0.
