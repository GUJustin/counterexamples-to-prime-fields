# An actual cubic first-order equation for the Dickson bank

This is a positive construction: a primitive first-order equation of total jet degree three has a growing bank of degree-D polynomial solutions, and the entire familiar Dickson received word is ordinary core. It does **not** by itself give superlinearly many prime-field labels, since its current domain has length p−1.

## Equation and bank

Let p=4k+1 be prime, k≥2, work over F_p, and put e=2k+1=(p+1)/2. Define

    q=X^(2k), S=1+q,
    G_a(X)=sum_{j=0}^k binom(e,2j+1) a^(2k−2j) X^j,
    P_a(X)=G_a(X)−X^k.

For a≠0, P_a has degree exactly k−1: its leading coefficient is binom(e,2k−1)a², which is nonzero modulo p. Distinct a² give distinct P_a, so there are exactly 2k distinct nonzero bank members. Include a=0 if desired, giving P_0=0.

Every G_a satisfies the SAME equation

    4X(2G²−1−X^(2k))G′ + G(4G²−1−3X^(2k)) = 0.       (1)

Equivalently every P_a solves Q(X,P_a,P_a′)=0, where

    Q(X,u,v)=4X[2(u+X^k)²−1−X^(2k)](v+kX^(k−1))
             +(u+X^k)[4(u+X^k)²−1−3X^(2k)].          (2)

This has derivative degree one and total degree three in (u,v). Its X-coefficient degrees grow with k. It is independent of the challenge z. The characteristic guard p>D=k−1 holds.

## Exact derivation

Work temporarily with t²=X and set

    J=((a+t)^e+(a−t)^e)/2,
    G=((a+t)^e−(a−t)^e)/(2t).

Because a^p=a and 2e=p+1, Frobenius gives the polynomial identities

    J²+XG²=a²+X^(2k+1),
    2JG=a(1+X^(2k)).                              (3)

Differentiating the two binomial powers gives

    2(a²−X)(2XG′+G)=aJ−XG,                      (4)

since e=1/2 in F_p. Multiply (4) by 2G and use (3):

    a²[4G(2XG′+G)−S]=2XG(4XG′+G).              (5)

Eliminating J from (3) also gives

    a²(S²−4G²)=4XG²(q−G²).                      (6)

For the nonzero polynomial G, eliminating a² from (5),(6) and cancelling 2XG yields

    (4XG′+G)(S²−4G²)
      −2G(q−G²)[4G(2XG′+G)−S]=0.

The left side factors exactly as

    (2G²−S){4X(2G²−S)G′+G(4G²−1−3q)}.

The factor 2G²−S is not identically zero: G is monic of degree k, so its leading coefficient is 2−1=1. Cancellation proves (1). This argument also covers a=0 because G=X^k is nonzero.

No integration, divisions by factorials, or unproved residue-moment cancellation is used.

## The complete received domain is ordinary core

On E=F_p^*, take

    w(x)=(1+x^(2k))/2−x^k.

At a received value u=w(x), the shifted value is G=(1+q)/2, with q=x^(2k) in {1,−1}.

* If q=1, then G=1 and both 2G²−1−q and 4G²−1−3q vanish.
* If q=−1, then G=0 and 2G²−1−q vanishes.

Consequently

    Q(x,w(x),v)=0 for EVERY v and EVERY x in E.      (7)

There is also an exact global fiber identity. With W(X)=S/2−X^k,

    Q(X,W(X),v)=(X^(p−1)−1)[2X(v+kX^(k−1))+X^(2k)/2].

Thus the ordinary-fiber vanishing has precisely the domain-locator factor, while Q itself has no such global content.

Thus the full ordinary core is real here, rather than an artifact of a coordinatewise residue alphabet. In particular, any bound discarding or normalizing this core must account for genuine actual solutions supported there. For the agreement claim additionally assume p=1 modulo 8. The existing exact character-sum calculation in `../dickson_fixed_gap/AUDIT.md` gives every nonzero bank member exactly k/2 square-coordinate and k nonsquare-coordinate agreements, hence 3k/2 agreements. Thus n=4k, dimension k, list size 2k, rate 1/4, agreement 3/8, and capacity gap 1/8. Equation (2) adds a global differential identity to that existing construction; it does not claim a new agreement estimate. For p=5 modulo 8 the equation and ordinary-core statements still hold, but this agreement count is not asserted.

The equation has no spurious global polynomial content. In coordinates G and V=G′ it is linear in V. Its two coefficients 4X(2G²−S) and G(4G²−1−3q) are coprime in F_p[X,G]: X does not divide the second; G does not divide 2G²−S; and subtracting twice 2G²−S from 4G²−1−3q gives 1−q, which cannot share a polynomial factor with 2G²−S since the latter has constant nonzero leading G coefficient. Hence (1) is primitive and irreducible as a polynomial linear in V. The affine change from (G,V) to (u,v) preserves this property.

## What this does and does not establish

This explicitly realizes Θ(D) distinct polynomial solutions at derivative degree one and total jet degree three, with a full ordinary core and the existing fixed-surplus Dickson agreement. The standard inverse-Bernoulli root bound does not apply to this equation.

It is not a prime-field superlinear ordinary-CA counterexample: the domain length is p−1, so there are only p scalar labels available. Passing to a larger characteristic does not preserve the Frobenius identities (3) at the same k. Averaging the bank onto a smaller domain is also not known to preserve the nonlinear equation (2). Neither step is asserted here.

A concrete next constructive target is to find an invariant subbank of actual solutions of (2), or a descended equation with analogous Frobenius identities, on a domain o(p) while retaining a fixed agreement surplus and growing bank. Unlike arbitrary sign masks, this starting bank already meets the global first-order differential equation requirement.

## Reproducible finite checks

`check_dickson_cubic.py` verifies the full polynomial coefficient identity for every a in F_p, the nonzero cancellation factor, distinct-bank count, and ordinary-core coefficient vanishing at every domain coordinate for p=13,17,29,41,73,97 (270 parameter identities). For the four primes congruent to one modulo eight it also verifies every nonzero parameter agreement count. Results are in `check_dickson_cubic.json`. These supplement the symbolic proof.
