# Independent audit: character-times-linear exponents

Audit date: 2026-09-19. This is a scoped obstruction, not a new counterexample.

Final outcome: for h>=4,r>=2,n=hr dividing p−1 and ac!=0, all three
words X^h, X^(h+1), X^(h+2) have at most sqrt(n)+2 agreements with
aX²+bX+c. The h+1 argument is elementary; h and h+2 require the
reciprocal-cofactor logarithmic-derivative proofs audited below.
The exact double-fiber criterion is correct but is not an escape from
these stronger bounds.

Let n=rh divide p−1, let D=mu_n in Fp*, and write P=aX²+bX+c.
The map x -> x^h maps D onto mu_r, with fibers of size h.

## Exponent h+1: audited bound

Assume ac != 0. On the fiber x^h=zeta, agreement with X^(h+1)
means aX²+(b−zeta)X+c=0. There are at most two roots. If two distinct
roots x,y occur, their product is c/a, so zeta²=(c/a)^h.
There are at most gcd(2,r) such zeta in mu_r. Consequently

    T <= r+gcd(2,r).

The polynomial X^(h+1)−P is nonzero: for h>=2 its leading degree
exceeds two, and for h=1 the nonzero c prevents identity. Thus also

    T <= h+1,
    T <= min(r+gcd(2,r), h+1) <= sqrt(n)+2.

The last inequality follows by splitting r<=sqrt(n) and h<sqrt(n).
No assumption b != 0 is needed. The bound may be improved by the
trivial cap T<=n, but this is immaterial asymptotically.

Degeneracies must be stated separately. If exactly one of a,c vanishes,
each fiber has at most one nonzero root, hence T<=r. For h>=2 the
polynomial degree bound still gives T<=h+1. For h=1 the quadratic
P=X² is the received word itself and has T=n, so the degree argument
must not be applied to this identity. If a=c=0, the word bX has either
h matches (b in mu_r) or none; this branch can exceed sqrt(n)+2.
It has only r possible nonzero matching monomials and is not the
full-three-coefficient bank under investigation.

Thus the proposed ac != 0 lemma is correct without extra assumptions.
Its extension to all quadratics is false without the listed exclusions.
At large n it rules out this full-coefficient exponent family achieving
agreement near sqrt(2n).

## Exponent h+2: why the elementary fiber argument alone is insufficient

On a fiber x^h=zeta, the agreement equation becomes

    (a−zeta)X²+bX+c=0.

For full coefficients abc != 0 every fiber has at most two roots, and
the exceptional fiber zeta=a has at most one. If a fiber has two roots,

    zeta²(a−zeta)^h=c^h.

Unlike the previous square equation, this has degree h+2 in zeta.
It does not cap the number of double fibers by a constant. The elementary
bounds are T<=min(2r,h+2), hence T<=sqrt(2n)+2. They allow the desired
scale only when h is approximately sqrt(2n) and r approximately sqrt(n/2),
with almost all fibers supplying two roots. These bounds do not show
that such simultaneous splitting is possible.

For odd p and b != 0, a double fiber with roots x,y has ratio
omega=x/y in mu_h excluding 1 and −1, and

    b²/[c(a−zeta)] = 2+omega+omega^(-1).

This assigns at most one zeta to each unordered reciprocal pair of
ratios, hence at most floor((h−1)/2) double fibers. This restriction is
compatible with, and does not establish, the desired balanced regime.
Inverting the evaluation coordinate and dividing values by X² maps
exponent h+2 to exponent −h and swaps a and c; it does not reduce this
case to the h+1 obstruction.

The existing normalized census contains 114 (profile,h) cases with
h|n and m=(h+2) mod n. Among them the maximum full-coefficient
A/sqrt(2n) is 0.75, attained only at n=8; no observed case reaches the
Johnson scale. This is a bounded computational observation, not an
asymptotic impossibility theorem. No further large search is justified
by the escape from the h+1 proof alone.

## Addendum: exact gcd criterion and balanced-edge obstruction

Independently checked the additions to CHARACTER_LINEAR_SQRT_GATE.md.
Both statements pass the algebraic audit.

For exponent h+2, put omega=y/x for the two distinct roots. Vieta yields
x=−c(1+omega)/(b omega), and zeta=a−(b²/c)omega/(1+omega)².
For abc nonzero, omega cannot be −1; it also cannot be 1 because the
roots are distinct. As omega^h=1, x^h=(-c/b)^h(1+omega)^h.
Multiplying x^h=zeta by (1+omega)² gives exactly H1 as displayed in
the companion note. Multiplying zeta^r=1 by (1+omega)^(2r) gives H2.
All cleared denominators are nonzero. Conversely these conditions make
x and omega*x distinct elements of D satisfying the same fiber quadratic.
Every fiber supplies precisely the two reciprocal ratios, and these are
distinct because ±1 were excluded. Therefore the degree of the common
gcd of H0,H1,H2, after removing roots ±1, is exactly twice the number
of double fibers. H0 is split and squarefree since h divides p−1.
There are no missing field-extension roots or multiplicity corrections.

Reviewed and independently reran check_double_fiber_identity.py: PASS,
625 triples across the five declared (p,n,h) cases. The verifier directly
enumerates agreement fibers and separately evaluates H1,H2 on roots of
H0; it does not implement a polynomial gcd, but this root enumeration
is exactly equivalent because H0 is split and squarefree. It checks
reciprocal closure too. This finite replay supplements the proof rather
than proving its generality.

For exponent h=2r and r>=2, T=h implies F=X^h−P has h distinct roots
in D. Each is a root of P^r−1; both polynomials have degree h, hence
P^r−1=a^r F. Differentiation at x0=−b/(2a), where P'=0, gives
0=a^r h x0^(h−1). Here a and h are nonzero in Fp because a!=0 and
h<n<p. Thus x0=0, contradicting b!=0. The exact-edge obstruction is
correct even if c=0. It does not bound the deficit below the edge beyond
at least one agreement, and does not rule out asymptotic saturation.

## Addendum: stronger reciprocal-cofactor gate

The stronger gate and its extension beyond h=2r pass independent
algebraic audit. A separate reciprocal version below closes h+2 too.

Assume h>=4,r>=2,n=hr<p, and ac!=0; b may vanish. Put
F=X^h−P, G=P^r−1, H=monic gcd(F,G), S=deg H,
A=G/H and B=F/H. All matching points in D are distinct common roots,
so their number T is at most S. This inequality, rather than equality,
correctly handles any other common roots and repeated roots of F,G.
Write A*,B* for reversals at their actual degrees. Then

    deg A=2r−S, deg B=h−S,
    A*(0)=a^r, B*(0)=1,
    Q=1+(b/a)z+(c/a)z²,
    A*=a^r B*Q^r + O(z^K), K=min(h−2,2r).

The last congruence follows by reversing AF=BG, using
F*=1−a z^(h−2)−b z^(h−1)−c z^h and
G*=a^r Q^r−z^(2r). No degree cancellation is assumed, and the reverse
cofactors are units at zero. For R=a^r B*Q^r/A*, one has R=1+O(z^K).
Its logarithmic derivative has numerator

    N=Q((B*)'A*−B*(A*)')+r Q'B*A*.

This polynomial has degree at most h+2r−2S+1 and vanishes to order
at least K−1 at zero. Hence N is identically zero if

    2S > h+2r+2−K.

The characteristic guard is sufficient: numerator and denominator of R
have degrees at most h+2r−S<=h+2r<=hr<p (h>=4,r>=2).
A rational function with derivative zero is in Fp(z^p); a nonconstant
one has reduced numerator or denominator degree at least p. Thus R is
constant, and R(0)=1 forces a^r B*Q^r=A*. But ac!=0 makes deg Q=2,
so its left side has degree at least 2r while the right side has degree
at most 2r−S. The contradictory regime has S>0. This establishes

    S <= r+2                    if h<=2r+2,
    S <= floor(h/2)+1           if h>=2r+2.

At h=2r this yields the announced S<=r+2; for r>=3 it materially
strengthens the exact-edge exclusion. The proof never requires b!=0.
Together with T<=min(h,2r), the general bound implies T<=sqrt(hr)+2.
In the first case use min(h,r+2); in the second use
min(2r,h/2+1), splitting h<=4r versus h>=4r. The h=3 case satisfies
the same square-root conclusion by T<=3 directly. Cases where the
received word itself has degree at most two must be excluded separately.

This is a constructor-specific obstruction. It gives no positive
counterexample or unrestricted ordinary-list upper bound. Reciprocity
takes h to 2−h, so closing h+2 requires the separate argument below.

## Addendum: reciprocal h+2 closure

The following separate reciprocal-cofactor proof closes h+2 as well.
Its logarithmic-derivative argument supplies the restriction missing
from the elementary double-fiber count.

Invert x and divide values by x². The h+2 agreement problem becomes
x^(-h)=P(x), where the new quadratic swaps the original a,c, so ac!=0
is preserved. Put F=X^hP−1, G=P^r−1, H=monic gcd(F,G), S=deg H,
A=G/H and B=F/H. Then deg A=2r−S, deg B=h+2−S. With the same
Q=1+(b/a)z+(c/a)z²,

    F*=aQ−z^(h+2), G*=a^r Q^r−z^(2r),
    A*=a^(r−1)B*Q^(r−1)+O(z^K), K=min(h+2,2r).

The congruence follows from A*F*=B*G* by dividing by the unit aQ.
The ratio R=a^(r−1)B*Q^(r−1)/A* has constant term one. Its logarithmic
derivative numerator has degree at most h+2r+3−2S and order at least
K−1. Thus it vanishes identically if 2S>h+2r+4−K. The numerator and
denominator degrees of R are at most h+2r−S<=hr<p, for h>=4,r>=2,
so derivative zero again implies that R is constant.

Here B* has its full degree h+2−S because B(0)=F(0)/H(0) is nonzero:
F(0)=−1 guarantees H(0)!=0. Consequently B*Q^(r−1) has degree
h+2r−S, strictly larger than the bound 2r−S on deg A*. This excludes
the constant identity and proves

    S <= r+1                    if h+2<=2r,
    S <= floor(h/2)+2           if h+2>=2r.

Combining T<=S with T<=min(h+2,2r) gives T<=sqrt(hr)+2.
For the first branch split h<=r versus h>=r; for the second split
h<=4r versus h>=4r. Again this is a scoped agreement obstruction for
these character exponents, not an unrestricted list-size theorem.
