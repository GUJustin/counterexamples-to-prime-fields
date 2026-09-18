# Prime-alphabet direct-list target: span obstruction and a surviving exact gate
**Superseded later September 18, 2026:** the proposed full-coefficient pure-character high-gcd gate is closed by `PURE_CHARACTER_WRONSKIAN_CLOSURE.md`. Its explicit bound is gcd degree <=4h/7+26 for h>=367, and it excludes the desired agreement throughout the feasible divisor-exponent range. The independent two-dimensional-span obstruction and literature scope check below remain valid. The former next-step recommendation is retained only as research history.


September 18, 2026. Bounded mathematical assessment; no scan, rental, or manuscript edit.

## Matched target and literature boundary

For dimension three and n tending to infinity, the desired agreement is A=c sqrt(n)+o(sqrt(n)), with sqrt(3/2)<c<sqrt(2), and a single word should have M>=c_0 n quadratic witnesses. The first inequality puts the agreement above the low-rate first-order curve; the second puts it below exact Johnson agreement sqrt(2n). Here n<=p and the alphabet itself is Fp.

The archived `PRIME_TRANSFER_OPEN_LEMMA.md` correctly excludes characteristic-zero rich-core inputs. The prime-field parabola theorem does not exclude the target: Mohammadi–Pham–Warren, Theorem 1.3, gives

    I << n^(15/19) M^(15/19) + n^(23/19) M^(4/19) + M,

under n<<p^(15/13). At M~n its first term is n^(30/19), larger than the required n^(3/2). The size hypothesis holds for every growing n<=p. This remains true for n=p^alpha with any fixed 0<alpha<=1. It leaves a precise incidence range, not evidence that a construction exists.

Primary source rechecked: https://www.ricam.oeaw.ac.at/files/reports/22/rep22-18.pdf (Theorem 1.3). This assessment concerns the cited bound, not a claim of an exhaustive survey of all later incidence literature.

## New useful scope extension: every fixed two-dimensional quadratic bank fails

The direct norm-one list lies in span{1,X^2}. Its prime analogue cannot keep ANY fixed two-dimensional quadratic witness span, even if the received word and evaluation domain are changed arbitrarily.

Indeed let U=span(h0,h1) over Fp, with independent polynomials of degree at most two, and let n distinct evaluation points carry an arbitrary word w. Remove the at most two zeros of h0. Map each remaining coordinate to

    (h1(x)/h0(x), w(x)/h0(x)).

Every fiber of this map has size at most two, since h1-t h0 is a nonzero polynomial of degree at most two. A witness alpha h1+beta h0 corresponds to the distinct line Y=alpha X+beta. Therefore a bank of M~n witnesses, each with A matches, gives at least M(A-2)/2 incidences between Theta(n) distinct points and Theta(n) distinct lines.

Stevens–de Zeeuw's balanced point-line theorem gives O(n^(22/15)) incidences here: its characteristic condition is n^11<<p^15, automatic for n<=p. Consequently

    A=O(n^(7/15))=o(sqrt(n)).

The argument also applies to affine translates of U, by subtracting a common quadratic from w. It strengthens the archived two-term cyclic gate to arbitrary words and domains. In particular a fixed injective linear/GRS compiler preserving the two-dimensional span of the norm-one bank cannot produce the prime-alphabet target. A full three-dimensional span is necessary. This is not an obstruction to all quadratic banks.

Primary source: https://arxiv.org/abs/1609.06284, Stevens–de Zeeuw, An Improved Point-Line Incidence Bound Over Arbitrary Fields. Bounded multiplicity is explicitly removed before applying the theorem.

## A concrete surviving family: full-coefficient pure-character orbit

The archived character-times-linear exponent m=1±n/r is closed, and the even pure-character case is closed by the two-dimensional argument. A different still-admissible gate uses ALL three coefficients and the pure-character word. Choose n=hr dividing p-1, D=mu_n, and

    w(x)=x^h,
    P(x)=a x^2+b x+c,  abc!=0.

For t in D the scaled quadratics

    P_t(X)=t^h P(X/t)

are all distinct: their three coefficient exponents h-2,h-1,h are consecutive. Every candidate has the same agreement A, so one successful polynomial produces exactly n bank members (without asserting list completeness).

A character branch zeta in mu_r contributes at most two roots. The polynomial degree bound and pairwise packing give

    A<=min(h,2r),       A(A-1)<=2(n-1).

Thus set r/h=sigma strictly between 1/2 and 2/3. The required agreement fraction on the degree scale is

    sqrt(3sigma/2)<A/h<sqrt(2sigma),    A/h<=1.

For example sigma=3/5 permits any A/h in (sqrt(0.9),1], and A/h=0.97 lies strictly between the first-order and Johnson constants. This is a parameter ledger conditional on suitable divisors n=hr of p-1; no unproved infinitude of primes of a prescribed quadratic form is assumed.

Here is a new exact necessary algebraic gate, which avoids any large coefficient scan. Put K=-b/a, so K!=0. Two roots in the same character branch must be x and K-x. If both match, then x^h=(K-x)^h; writing z=x/(K-x) gives z in mu_h, z!=-1, and x=Kz/(1+z). The remaining matching equation is exactly

    R(z)=[c(1+z)^2-a K^2 z](1+z)^(h-2)-K^h=0.

Let d_2 be the number of branches contributing two distinct matches. Since there are at most r branches, d_2>=A-r. Each double branch contributes two distinct roots to gcd(R(Z),Z^h-1). Therefore

    deg gcd(R(Z), Z^h-1) >= 2(A-r).

At sigma=3/5 and A/h=0.97 this requires gcd degree at least 0.74h. These are not unrestricted cyclotomic moment equations: only the two shape parameters c/K^h and a K^(2-h) occur in the polynomial after division by K^h. All roots are tested in Fp since h divides p-1. The condition is necessary, not sufficient: additionally x=Kz/(1+z) must lie in mu_n, and single-match branches contribute to the final count. The original abc and orbit-distinctness guards remain essential.

This high-degree gcd in a two-parameter pencil is an inexpensive symbolic discriminating target relative to enumerating p^3 quadratics. A successful identity valid along growing (p,h,r), with the original domain guards and agreement count checked, would supply the requested linear list. Conversely a uniform bound deg gcd(R,Z^h-1)<2(A-r) in this parameter range would decisively close this precise full-coefficient pure-character subclass. The previous character-times-linear and even-candidate results do not establish that bound. The substantial required gcd makes a new splitting identity essential; a random finite-field hit or a bounded-order scan would not establish the asymptotic construction.

## Decision

Do not attempt to transfer the two-dimensional norm-one bank directly to prime alphabets: the point-line theorem excludes that target. Do not enlarge the prior coefficient-bank or small-cyclic scans. The distinct surviving calculation is the displayed two-parameter shifted-power/cyclotomic gcd, with the explicit 0.74h requirement in the example ledger. No positive family has been proved here; this identifies a concrete missing algebraic identity rather than a generic open-ended prime search.
