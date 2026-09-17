# Bounded novelty audit: the rational-Hermite actual-solution theorem

2026-09-17. This is a focused comparison, not an exhaustive priority certification. Main manuscript unchanged.

## What is classical

The threshold A>sqrt(D*s/2) for matching a prescribed value and first derivative at s coordinates is the order-two multiplicity-code Johnson threshold. A degree-D difference has at most floor(D/2) double roots. Multiplicity interpolation and weighted monomial counting recover this same threshold. Neither the factor 1/2 nor the Guruswami--Sudan dimension argument is a new decoding phenomenon.

Primary references:

* Venkatesan Guruswami and Madhu Sudan, *Improved Decoding of Reed-Solomon and Algebraic-Geometry Codes*, IEEE Transactions on Information Theory 45(6):1757--1767 (1999). Author-hosted conference/full argument source: https://people.csail.mit.edu/madhu/papers/1998/gs.pdf . The abstract and interpolation algorithm establish the familiar multiplicity-based improvement to the RS Johnson radius.
* Swastik Kopparty, *List-Decoding Multiplicity Codes*, Theory of Computing 11(5):149--182 (2015), DOI 10.4086/toc.2015.v011a005. Primary PDF: https://theoryofcomputing.org/articles/v011a005/v011a005.pdf . Its introduction, informal Theorem B and the following paragraph (printed pages 152--153), explicitly place univariate multiplicity-code Johnson decoding in prior work of Guruswami--Sudan and Guruswami--Sahai--Sudan. Its differential-equation framework and power-series lifting are also directly relevant classical ingredients.

These checked sources are enough to credit the method and threshold. The original Guruswami--Sahai--Sudan paper was encountered through Kopparty's attribution, not independently read in this bounded search. Do not claim it was audited firsthand.

Repeated-root formulas for cubics, squarefree factorization, discriminants, Hasse/implicit Taylor lifting, plane Bezout, and degree bounds for rational images are also standard tools. The cubic extension rests on the elementary fact that a cubic has at most one distinct repeated root, not a newly discovered algebraic mechanism.

## Closest checked modern framework

Fernando Granha Jeronimo, *Algorithmic List Decoding at Capacity and Optimal Proximity Gaps for Reed--Solomon Codes*, arXiv:2609.05870v1 (5 September 2026):
https://arxiv.org/html/2609.05870v1

Sections 5--7 already combine symbolic differential equations, specialization-safe solution covers, Taylor lifting with numerator/denominator bounds, and cuts taken from the original full agreement support. Theorem 5.5 gives bounded-dimensional covers with polynomial cumulative degree; Lemma 5.7 explicitly bounds Taylor denominators by exponent 2t-1. The manuscript already cites this preprint in related work. These general strategies must not be advertised as new here.

Its displayed theorem bounds cumulative degree by an unspecified fixed polynomial, with both challenge and X degrees bounded by one growing parameter. Its displayed Taylor numerator bound is quadratic in the truncation index. The inspected statements do not give our linear-in-n conclusion for the specific bounded-challenge rational-jet class. That is a comparison of the stated bounds, not proof that their arguments cannot be sharpened to imply ours.

## What the present theorem actually adds to this framework

The proposed contribution is the following specialized quantitative combination, with all of its scope retained:

1. Begin with one common bounded-complexity differential identity containing the ACTUAL nearby candidates; permit arbitrary X-degree.
2. For derivative degree at most three, classify singular value agreements into an ordinary core, one rational derivative prescription per persistent coordinate, and O(n) exceptional coordinate-label incidences. The derivative prescription has bounded challenge height, even with degree drops.
3. Use classical order-two interpolation symbolically in the challenge, keeping its Y-degree and challenge degree CONSTANT at fixed slack. This is the crucial parameter feature for the next step.
4. For that order-zero interpolant, retain linear complexity in deg_X Q+D when handling specialized polynomial roots. The explicit proof picks one obstructing Taylor coefficient per initial-plane component and bounds its zeros, rather than imposing a large residual system with a coarse polynomial-degree estimate.
5. Apply persistent-agreement incidence counting to original FULL supports, yielding O(n) bad labels, not merely a bounded list for each fixed challenge or a polynomial-in-n count of unspecified exponent.

The specialized outcome is stronger than the general polynomial upper bound in the checked modern theorem, but applies to a narrower actual-solution class and a quantified Hermite agreement margin. This is an application/refinement of established interpolation and algebraic geometry, not a new general decoding algorithm.

## Why fixed-challenge Johnson list bounds alone do not prove it

An O(1) list for every individual received first-jet word does not by itself bound how many challenges have a bad witness. The identities of those witnesses may change with the challenge. The symbolic bounded-height interpolation and specialization control address this missing cross-challenge step, and the full-support cuts distinguish correlated agreement from ordinary list size. This explains why citing the classical Johnson result does not by itself subsume the entire claimed theorem.

Conversely the main interpolation threshold remains exactly classical: no claim of an improved multiplicity-code Johnson radius is justified. The ordinary core and signed margin are essential hypotheses, not technicalities that can be omitted from the headline.

## Local research comparison and limits of this audit

Checked the current manuscript's related-work discussion and the local Hermite, rational-jet, cubic, root-specialization, generic-branch, and earlier fixed-singular-cover notes. The earlier local bounds either used a triple-intersection core-size restriction or treated narrower monic-Riccati forms. The current theorem removes that particular core-size restriction by applying Hermite interpolation, subject to its stated numerical margin; it also permits broader value dependence and cubic derivative degree.

I did not perform an exhaustive recursive search over the roughly 76,500 restored files, and did not audit every differential-equation or ideal-code paper. No exact matching published theorem was identified in this focused comparison. That absence does not certify novelty.

## Recommended attribution and wording

Credit Guruswami--Sudan/multiplicity-code interpolation for the threshold and Kopparty for differential power-series methods. Explicitly acknowledge the prior symbolic-specialization/full-support geometric framework in Jeronimo. Describe the result as a self-contained linear bound for a bounded-complexity class of actual first-order solutions, obtained by combining rational singular jets with Hermite interpolation and a quantitative specialization lemma. Avoid phrases such as “a new Hermite bound,” “a new Johnson threshold,” or “a new specialization framework.”

For assessing the paper's strength, the theorem is useful structural progress because it rules out a broad class of candidate counterexamples and identifies the remaining ordinary-core/multiple-jet obstructions. It is not itself the sought prime-field fixed-gap lower construction, an improvement to better.codes, or tightness of the unrestricted first-order proximity theorem.
