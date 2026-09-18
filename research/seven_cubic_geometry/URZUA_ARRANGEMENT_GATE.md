# The section-arrangement inequalities allow the seven-cubic pattern

## Result

The checked characteristic-zero log Miyaoka--Yau inequalities do NOT rule out the proposed seven-cubic, fourteen-node, seven-agreement bank. Every allowed partial extension passes with a substantial strict margin. This is a negative result for this particular obstruction route, not a proof of geometric realizability.

## Exact translation of the candidate

Assume the saturated incidence pattern: seven cubic graphs, seven ordinary triple intersections, seven ordinary quadruple intersections, and no other pair intersections. Pair counting gives

    7*binom(3,2)+7*binom(4,2)=63=3*binom(7,2).

Thus each pair meets at exactly three distinct finite points, with transverse intersection there. Their cubic differences have distinct leading coefficients, so no additional intersection occurs at infinity. The graphs compactify to sections of O(3), class C0+3F on the Hirzebruch surface F3; C0^2=-3 and each section is disjoint from C0. There is no common seven-fold point. All14 singular fibers are distinct, and each has exactly one singular point. Thus the arrangement hypotheses, not just a formal intersection count, match the indicated section-arrangement framework.

## Primary theorem used

Giancarlo Urzúa, *Arrangements of rational sections over curves and the varieties they define*, arXiv:0910.4928v2, especially Definition6.1, Propositions6.1/6.3 and Corollaries6.2/6.4:

https://arxiv.org/pdf/0910.4928
https://arxiv.org/html/0910.4928

These results define extended arrangements by adding the negative section and all singular fibers; partial extensions may delete up to delta-2 suitably transverse fibers. They give log Chern formulas and strict c1bar^2<3c2bar over C. The sharper8/3 bound in Remark6.3 is explicitly for O(1), and must not be transferred to O(3).

## Our substitution and all partial choices

The parameters are d=7 sections, e=3, g=0, delta=14, and tau=7*(3-1)+7*(4-1)=35. Substitution into the extended formulas gives

    c1bar^2=6*(28-4-3)+35=161,
    c2bar=6*(14-2)=72.

The ratio161/72 is about2.236, well below3.

Now remove a triple fibers and b quadruple fibers, with0<=a,b<=7 and a+b<=12. At a triple fiber the seven sections occupy five distinct points, hence k=6 after including C0, and k^o=1. At a quadruple fiber these numbers are k=5,k^o=1. Therefore the exact partial-extension invariants are

    c1bar^2=161-9a-7b,
    c2bar=72-4a-3b,
    3c2bar-c1bar^2=55-3a-2b.

The minimum gap over every allowed choice is24, attained at(a,b)=(7,5). Even the stronger8/3 test would pass: its numerator8c2bar-3c1bar^2 is93-5a-3b, whose allowed minimum is43. This latter computation is only a diagnostic, not an invocation of the O(1) theorem.

For comparison, the bare seven-section arrangement has logarithmic invariants(50,25), computed directly on its ordinary-point resolution: (K+sum S_i)^2=85 before resolution, then subtract7*(3-2)^2+7*(4-2)^2=35; Euler characteristic is4-14+7*2+7*3=25. Adding C0 alone gives(49,23). Neither numerical pair approaches a Miyaoka--Yau violation. No unverified nefness theorem for these unextended variants is needed for the conclusion about the already-covered extended arrangements.

## A nearby theorem with different hypotheses

Piotr Pokora, *Hirzebruch--Kummer covers of algebraic surfaces*, Turkish Journal of Mathematics43(1),412--421(2019), DOI10.3906/mat-1808-22, arXiv:1805.01215v2:

https://arxiv.org/pdf/1805.01215
https://journals.tubitak.gov.tr/math/vol43/iss1/33/

Definition2.1 uses sections in class Gamma+(e+1)F, of self-intersection e+2, rather than our Gamma+eF. The later Kodaira-dimension argument also imposes an additional four-section condition. Consequently its stated rational-section inequalities cannot simply be inserted with e=3 for the present pattern. The ordinary cover-Chern calculation, if used for our class, produces a positive defect25m^2-56m+91 for every covering exponent m anyway; it offers no numerical contradiction.

## Limits of the literature check

The requested Michigan thesis URL was attempted both through the browser and directly; it returned an error page rather than the thesis PDF. I have not represented that thesis as read:

https://deepblue.lib.umich.edu/bitstream/handle/2027.42/60657/gian_1.pdf?sequence=1

The accessible primary section-arrangement paper and the directly relevant later cover paper were checked at their actual hypotheses. This bounded check does not establish that no stronger arrangement inequality exists anywhere in the literature.

The cited strict log inequalities are characteristic-zero results; the same paper exhibits positive-characteristic failures of broad Miyaoka--Yau behavior. No prime-field exclusion follows from our calculations. Conversely, if another argument eventually excludes this fixed incidence system in characteristic zero, an algebraic elimination certificate with the distinctness guards could exclude all but finitely many characteristics. That separate transfer argument is not supplied by a numerical Chern-ratio test that the configuration already passes.
