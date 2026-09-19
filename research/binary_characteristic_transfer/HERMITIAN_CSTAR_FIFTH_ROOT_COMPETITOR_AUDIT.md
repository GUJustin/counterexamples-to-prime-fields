# A fifth-root competitor for the second explicit Hermitian endpoint

2026-09-19. Independent exact construction: **PASS**. No scan or manuscript edits. This supplies the previously unresolved c* endpoint and an unconditional simultaneous limitation for the two explicit quartic endpoints.

## Algebraic construction

Let p≥5 be prime and let e be even with 2≤e<p. Assume

    m=p+e divides p²−1,  p≡2 (mod 5),  e≡2 (mod 5).

Put B=Fp²⊂E=Fp4, Λ=X^(p²)−X, D=p²−p, k=D−p. Fix ANY beta∈E\B and a primitive fifth root t∈E. Such t exists and is outside B since p has order four modulo five. The two elements 1,t^(−1) are a B-basis of E, so there are unique b∈B and gamma∈B* with

    beta=b+gamma/t.

Define

    G=(X−b)^m−gamma^m, F=(X−b)^e,
    A0=−b^p F−gamma^m.

Then G=X^p F+A0, with deg A0≤e. Its m distinct roots are b+gamma*mu_m⊂B, since m divides p²−1. The only root b of F is not a root of G, hence gcd(F,G)=gcd(F,A0)=1. The associated degree-e rational map is

    R=−A0/F=b^p+gamma^m/(X−b)^e.

At beta,

    R(beta)=b^p+gamma^p*t^e
            =b^p+gamma^p*t^(−p³)=beta^(p³),

because p³+e≡8+2≡0 modulo five and gamma,b belong to B.

Set P=ΛF/G. It is monic of degree D and polynomial because G divides Λ. All its native roots are the complement of G: the extra root b of F already lies in that complement. Thus its number of distinct native roots is EXACTLY D−e. From

    (P−X^D)G=−XF−X^D A0

we obtain deg(P−X^D)≤D−p=k.

## Its pole value is exactly c*

Recall c* is the unique pth root of Λ(beta)^(p−1). Write L=Λ(beta)≠0. Since beta^(p⁴)=beta, one has L^(p²)=−L and therefore

    c*=−L/L^p.

Indeed (−L/L^p)^p=−L^p/L^(p²)=L^(p−1). On the other hand R(beta)=beta^(p³) gives

    G(beta)/F(beta)=beta^p−beta^(p³)=−L^p.

Here F(beta)≠0 and G(beta)≠0. Consequently

    P(beta)=L*F(beta)/G(beta)=−L/L^p=c*.

For the shifted source f=(X^D−beta^D)/(X−beta) and g=1/(X−beta), the polynomial

    q=(X^D−beta^D+c*−P)/(X−beta)

has degree<k, and f+c*g−q=P/(X−beta). This is an actual competitor at the second explicit endpoint, with exact agreement D−e, for EVERY exterior beta.

## Unconditional simultaneous prime progression

Choose any odd r≥3 with r≡3 modulo five (equivalently r≡3 modulo ten). Set

    j=10u+7, e=1+rj, p=(r−1)e+r,

where u is a nonnegative integer. Then e is even and e≡2 modulo five; p≡2 modulo five. The prime values of p lie in the progression

    p=10r(r−1)u+(7r²−5r−1).

Its residue is odd, is 2 modulo five, −1 modulo r and 1 modulo r−1, hence is coprime to 10r(r−1). Dirichlet gives infinitely many prime values for each fixed r. They satisfy e<p and

    p−1=(r−1)(e+1), r divides p+1,
    m=p+e=r(e+1) divides p²−1,
    (p²−1)/m=(r−1)(p+1)/r>e.

Thus the SAME prime progression also satisfies every hypothesis of HERMITIAN_SOURCE_MOBIUS_COMPETITOR.md, supplying a zero-endpoint competitor of exact agreement D−e for every beta. The two competitors need not be the same polynomial.

For both explicit endpoints r0=f and r1=f+c*g, at the theorem's threshold T=D−2,

    T−agreement(r_i)≤e−2,  i=0,1.

The theorem still guarantees that these losses are positive; the present construction supplies their upper bounds. For each fixed r the ratio to the capacity margin p−2 has limsup at most 1/(r−1). Taking r→infinity through r≡3 modulo ten and choosing a sufficiently large prime from each progression gives e/p→0. Therefore neither explicit quartic endpoint has a uniform positive fractional capacity loss across all primes and poles. This does not exclude a different pair of endpoints or the degree-eight projection construction.

## Compatibility with the saturation-orbit obstruction

There is no contradiction with the earlier observation at p=e²−e−1. In the Möbius orbit of R0=X^(−e), the c* condition is t^(p³+e)=1. At those quadratic parameters, gcd(p³+e,p⁴−1)=p+e, so all such roots are native and that orbit cannot supply an exterior pole. The present Dirichlet family instead deliberately supplies an exterior fifth root and does not assert exact square-root saturation. Whether c* attains the lower source-gap bound on the prime-quadratic parameters remains open beyond this orbit.


## Audited generalization and quantifier order

The fifth-root argument also works for p≡3 modulo five, provided e≡p modulo five. More precisely its sufficient hypotheses are p modulo five in {2,3}, 2≤e<p, e≡p modulo five, and p+e dividing p²−1. Evenness of e is not needed for the c* constructor itself. Since p²≡−1 and p³≡−p modulo five, the same exterior fifth root gives t^(p³+e)=1 and all displayed identities remain unchanged. In particular p=13,e=8 has m=21 dividing 168 and is covered, even though L=8=e does not meet the separate zero-endpoint lemma's L>e hypothesis. No simultaneous zero-source conclusion is inferred for this isolated case.

For simultaneous endpoint limitations, retain the even-e Dirichlet family already proved above. Given ANY epsilon>0, first choose a fixed odd r≡3 modulo five with 1/(r−1)<epsilon. Its single arithmetic progression contains infinitely many primes, independent of beta. For every such prime and EVERY beta outside B, both constructors apply and

    (T−agreement(r_i))/(p−2) ≤ (e−2)/(p−2) < 1/(r−1) < epsilon.

The strict middle inequality follows from e=(p−r)/(r−1), not from an unproved uniform prime estimate. This proves the order of quantifiers: for every epsilon, infinitely many primes, for every exterior pole, both explicit endpoint gaps are below epsilon times the margin. It does not assert one common finite prime works for all epsilon or that all sufficiently large primes do so.
