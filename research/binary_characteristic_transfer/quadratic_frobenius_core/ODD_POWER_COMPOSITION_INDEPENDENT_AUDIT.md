# Independent audit of the odd-power composition refinement

2026-09-18. **PASS**, including the strict p≥3h−1 conclusion, for the source hash below. No manuscript edits or finite scan.

For a noncanonical q of degree≤h, its intermediate exponent set is nonempty. Let δ be its gcd together with h, and H=h/δ. All exponents of q, including a possible h term and its constant, are multiples of δ. Since h is odd and divides p²+1, δ and H are coprime to both p and p²−1; H is an odd integer at least three.

Within either physical block, two good branch indices differ by an element annihilated by every intermediate exponent modulo h. The common kernel has exactly δ elements. Requiring the leading or constant coefficients to be in B can only reduce this set. The previously proved primitive-scale congruence excludes good branches in both blocks, so the total number is at most δ, not 2δ.

After branch normalization, the received monomial is z^(hp) with coefficient one. The polynomial on its other side is a polynomial in z^δ. Substitution y=z^δ is bijective on B and changes the equation to y^(Hp)=Ptilde(y), where Ptilde has degree≤H and a nonzero intermediate term. Thus the local Kummer lemma applies and bounds a good branch by max(p,H²). The corrected standalone local hypothesis gcd(t,p(p²−1))=1 is exactly what is needed for separability, and is automatic here.

On a bad branch, projection kills the received monomial and leaves a NONZERO polynomial in z^δ. In the y coordinate it has degree≤H. This justifies H roots per bad branch; it is not an application of the ordinary degree-δH root bound. Constants and the label shift only affect the constant term and do not invalidate either assertion. Puncturing only reduces these bounds.

Consequently the global upper bound is

    δ max(p,H²)+(2h−δ)H
      =δ[max(p,H²)+(2H−1)H].

If p<H², the bracket is 3H²−H, strictly below Hp because p≥3h−1≥3H−1 and equality p=3H−1 is impossible for odd prime p and odd H. If p≥H², subtracting the bracket from Hp gives at least H(H²−3H+1)>0 for H≥3. Hence every noncanonical witness has strictly fewer than hp matches under p≥3h−1. There is no hidden need for p≥h².

For the proposed p=307,h=65 instance, H is one of 5,13,65. The corresponding exact upper bounds are 4576,3160,12610, respectively, all below hp=19955. The branch-separation guard also holds: (p²+1)/h=1450>64. This verifies only the refinement's finite inequalities; the independent deterministic-retention certificate remains responsible for the selected domain length and threshold.

With a full first block, a canonical nonzero core fiber gives hp matches at every label. Outside the canonical label planes, all canonical witnesses have at most hp matches. Thus the refined bound proves exact hp agreement throughout the empty-list class, and preserves the earlier common-agreement and complete-list conclusions whenever their separate retention/threshold guards hold.

Source SHA256: `b52d597171206a9d054c21a7ef422e98a90d15fe1fd3cde37b654fea4574134e`.
