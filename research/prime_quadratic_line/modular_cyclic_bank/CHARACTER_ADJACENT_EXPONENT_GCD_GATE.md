# Adjacent character exponents: a square-root ceiling from rational approximation

September 19, 2026. Collaborative derivation by the root agent and modular-bank probe, independently checked by the cyclic-lemma auditor. This note supersedes the unresolved h and h+2 possibilities in `CHARACTER_LINEAR_SQRT_GATE.md`. It is an ordinary-list constructor constraint, not a general proximity-gap impossibility or a new positive construction.

## Statement

Let n=hr divide p-1, h,r>=2, and let D=mu_n be the subgroup of order n in F_p*. In particular n<p. For any quadratic P=aX^2+bX+c with ac!=0, its agreement T with each of the words

    X^h, X^(h+1), X^(h+2)

on D satisfies T<=sqrt(n)+2. Their reciprocal transforms X^(2-h), X^(1-h), and X^(-h) obey the same bound. In particular these full-coefficient cyclic-bank families cannot achieve T>=c0 sqrt(n) for a fixed c0>1 along an unbounded sequence. No statement here excludes arbitrary exponents 1+kh with k not ±1, or classifies all quadratics with ac=0.

For X^(h+1), use the character-fiber proof in the preceding note. The following gcd bounds prove the adjacent two cases. They hold for h>=4,r>=2. All gcd degrees count algebraic multiplicity, making them upper bounds for the distinct native agreement count.

## Exponent h

Put F=X^h-P, G=P^r-1, S=deg gcd(F,G), and K=min(h-2,2r). A matching x in D obeys P(x)=x^h and P(x)^r=1, so T<=S. We prove

    2S <= h+2r+2-K.

Equivalently S<=r+2 when h<=2r+2, and S<=floor(h/2)+1 when h>=2r+2. Also T<=min(h,2r).

Let H be the monic gcd and write F=A H, G=a^r B H, with A,B monic, degrees h-S and 2r-S. For a polynomial V of specified degree d, write V*(z)=z^d V(1/z). Define Q(z)=1+(b/a)z+(c/a)z^2. Reversing the identity A G=a^r B F gives

    A* [Q^r-a^(-r) z^(2r)]
      = B* [1-a z^(h-2)-b z^(h-1)-c z^h].

Thus A* Q^r-B* vanishes to order at least K at zero. The reverse polynomials A*,B* have constant term one, as does Q. The rational function R=A*Q^r/B* therefore satisfies R=1+O(z^K). Its logarithmic derivative has numerator

    N=r Q' A*B*+Q((A*)' B*-A*(B*)'),

of degree at most h+2r-2S+1, while it vanishes to order at least K-1. If 2S>h+2r+2-K, the order exceeds the degree, forcing N=0.

This cannot be explained by an inseparable rational function. The numerator degree of R is at most h+2r-S<=hr<p (the inequality h+2r<=hr holds for h>=4,r>=2), and its denominator degree is also less than p. A rational function of these degrees with zero derivative is constant: after canceling common factors, the coprime numerator and denominator each divide their own derivatives, forcing both derivatives zero and then both polynomials constant. Hence R=1. But deg(A*Q^r)>=2r whereas deg B*<=2r-S<2r in the alleged violation regime, a contradiction. Here deg Q=2 uses ac!=0.

To obtain T<=sqrt(n)+2: if h<=r, use T<=h; if r<h<=2r+2, use T<=r+2; if 2r+2<h<=4r, use T<=h/2+1<=sqrt(hr)+1; and if h>4r use T<=2r<=sqrt(hr).

## Exponent h+2 via reciprocal coordinates

The transformation x->1/x, f->X^2f(1/X), P->X^2P(1/X), preserves D and quadratic agreement, and exchanges X^(h+2) with X^(-h). It preserves ac!=0. For the latter word put

    F=X^h P-1, G=P^r-1, S=deg gcd(F,G), K=min(h+2,2r).

Again T<=S. We prove

    2S <= h+2r+4-K,

or S<=r+1 when h+2<=2r, and S<=floor(h/2)+2 otherwise. Also T<=min(h+2,2r).

Write F=a A H, G=a^r B H, with A,B monic of degrees h+2-S and 2r-S. Reversing A G=a^(r-1)B F gives

    A* [Q^r-a^(-r)z^(2r)] = B* [Q-a^(-1)z^(h+2)].

Consequently A*Q^(r-1)-B*=O(z^K). Use R=A*Q^(r-1)/B*. Its logarithmic-derivative numerator has degree at most h+2r+3-2S and vanishes to order K-1. A violation of the claimed bound again forces zero derivative. The numerator degree is at most h+2r-S<=hr<p, so R is constant and equals one.

This time deg A*=h+2-S exactly, because F has nonzero constant term -1 and therefore A does too. Thus

    deg(A*Q^(r-1))=h+2r-S > 2r-S >= deg B*,

contradicting R=1. This proves the bound.

For the square-root consequence, if h+2<=2r then use T<=h+2<=sqrt(hr)+2 when h<=r, and T<=r+1<=sqrt(hr)+1 when h>r. In the other case, use T<=h/2+2<=sqrt(hr)+2 for h<=4r, and T<=2r<=sqrt(hr) for h>4r.

## Small h and balanced near-complete splitting

For h=2,3, exponent h has degree at most three and immediately meets the square-root ceiling. For exponent h+2 and r>=3, degree h+2<=sqrt(hr)+2 suffices. When r=2, h=2 gives the constant word X^4=1 on mu_4 and at most two matches with ac!=0; h=3 gives X^5=X^(-1) on mu_6 and at most three matches, by multiplying the agreement equation by X. Thus the stated theorem covers all h,r>=2.

In particular, in the balanced case h=2r the stronger bound is T<=r+2. A proposed near-complete splitting T=2r-d with fixed d must have r<=d+2. For d=1, only r<=3 can survive this necessary condition; it cannot yield an infinite family. This substantially strengthens the earlier exact-complete-splitting obstruction. No Dickson or translated family can evade the bound while retaining the stated monomial/domain/quadratic hypotheses.

## Relation to prior local research and verification

The inspected `research/projective_dickson_search/README.md` and `AFFINE_TRANSLATION_BARRIER.md` concern a different received word, dimensions growing proportionally to p, and projective/translated Dickson candidates. They do not contain this adjacent-exponent gcd argument. This is a new local derivation, not a claim of novelty in the mathematical literature. No broad literature-priority claim is made.

`check_adjacent_exponent_gcd_gate.py` uses FLINT to compute the actual polynomial gcd degree and independently counts native agreements for both F models, with a,c in {1,...,5}, b in {0,...,5}, across eight (p,h,r) triples. All 2400 checks pass, including the exact integer square-root ceiling. `adjacent_exponent_gcd_gate_receipt.json` retains maxima and thresholds. The finite replay checks formulas and implementation; the symbolic proof supplies the asymptotic statement. No larger search or rental was needed.
