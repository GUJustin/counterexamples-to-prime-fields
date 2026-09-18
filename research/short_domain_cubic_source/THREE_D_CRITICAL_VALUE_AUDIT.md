# A section-assisted improvement from p>6D to p>3D

**Later strengthening:** the final list theorem uses `p>max(3,2D)`; see `TWO_D_RADICAL_BUDGET.md`, its independent audit, and `general_cubic_list.tex`. The stronger characteristic assumptions in this earlier argument remain valid sufficient conditions.

Verdict: independently checked algebraic strengthening. In the monic weighted-cubic list theorem, the positive-dimensional critical-component step works for p>max(3,3D). The same improved guard therefore suffices for the combined arbitrary-word list bound. No cover or zero-dimensional multiplicity argument changes.

Work over algebraically closed k, K=k(X), and depress the weighted cubic by z=u+a2/3:

    F=z³−3g(X)z+b(X),  deg g≤2D, deg b≤3D.

Assume some nonzero-label degree≤D section exists, so deg H≤3D. Suppose the original critical ideal has a positive-dimensional component. A critical branch r has r²=g, and its value is

    v=(b−2gr)/H,   v′=0.

## Rational critical branch

If r belongs to K, integrality gives r polynomial of degree≤D. The numerator b−2gr and denominator H both have degree≤3D, so h_K(v)≤3D<p. As v′=0 means v in K^p, v is constant. The repeated-fiber reduction and the existing cubic-cover lemma apply unchanged.

## Irreducible quadratic critical branch

Suppose r²−g is irreducible over K. Its nontrivial conjugation commutes with differentiation, so both critical values have zero derivative. Their trace gives

    (b/H)′=0.

The height h_K(b/H) is at most 3D<p, hence b/H=beta is constant. The difference of the two critical values then shows (gr/H)′=0. Using r²=g and p≠2,3 gives

    3g′H−2gH′=0.                               (1)

A polynomial section z of degree≤D at label c obeys

    z(z²−3g)=lambda H,   lambda=c−beta.

If lambda≠0, z is nonzero. Differentiate the section identity and combine with (1). After multiplication and simplification, using p≠3, the result is

    (z²−g)(g′z−2gz′)=0.

The first factor cannot vanish because g is nonsquare in K. Hence

    (g/z²)′=0.

The rational function g/z² has height at most 2D<p. It must be a constant. This constant is nonzero, and is a square in the algebraically closed field k. Thus g is a square in K, contradicting the assumed irreducibility. No lambda≠0 polynomial section exists.

All remaining sections lie in the single lambda=0 fiber and therefore number at most three (in fact only z=0 survives when g is nonsquare). This exceptional case already satisfies the list theorem without needing a constant critical value.

Characteristic zero follows by the same argument with derivative-zero implying constant immediately. The proof deliberately does not claim that every critical value is constant: in positive characteristic, the irreducible-branch case can have nonconstant Frobenius critical values, but then the polynomial section bank is too small.

## Why the p/6 boundary did not produce a lower construction

For p≡1 mod3, take a=(p+2)/3,

    F=u³−3X^a u,   H=X,   D=ceil(a/2).

The critical values ±2X^(p/2) are nonconstant pth powers in K(sqrt X), and 6D is approximately p. This realizes the potential height obstruction itself. But a nonzero-label section would satisfy

    P(P²−3X^a)=cX,

so P divides X. For a>2, neither a nonzero constant P nor P proportional to X satisfies the equation. The only polynomial section is the zero-label P=0. Thus this explicit Frobenius mechanism supplies no growing bank, and not enough agreement coordinates; the section-assisted argument explains the failure uniformly.

The exact remaining window for this mechanism is p≤3D, where the trace b/H can be a nonconstant pth power. Producing polynomial sections with a common fixed-surplus received word in that window remains an actual construction task, not a consequence of the critical-value example.
