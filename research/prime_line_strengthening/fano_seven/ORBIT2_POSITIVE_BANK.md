# A second seven-word characteristic-zero nearest bank

An exact positive construction was found in ordered incidence orbit2. It is
not isomorphic as an ordered incidence design to the earlier orbit7 bank.
The successful certificate is `orbit2_number_field.py/json`; its bounded
execution took1.62seconds with peakRSS below72MiB. Independent auditing and
the possible eighth-word test are delegated separately; this note records the
complete construction and the elementary nearest-distance certificate.

## Field, nodes, and cubic sections

Let K=Q(q), where

    q^3-10q^2+3q+1=0.

The cubic is irreducible overQ: the only possible rational roots ±1 are not
roots. Its polynomial discriminant is65^2. No identification of its maximal
order or conductor is needed here.

The quadruple-node coordinates, in C-block order, are

    infinity,0,1,u,v,q,d,
    u=(-q^2+13q+3)/20,
    v=(-4q^2+27q+7)/25,
    d=(-3q^2+29q+4)/20.

The ordered complementary triples are

    C=137,145,167,236,247,256,345.

Put

    B=(135854572q^2-1353831356q+428344204)/221646235,
    C0=(-143947248q^2+1457491984q-627685616)/221646235,
    W(X)=X^3+B X^4+C0 X^5.

For i=1,...,7 let L_i be the monic product of X-b_j over the FINITE
quadruple nodes whose C_j does not contain i. Define

    P_i(X)=W(X) mod L_i(X).

If i is in137, L_i has degree4 and P_i has degree at most3. For the other
four candidates L_i has degree3, so P_i has degree at most2 and matches the
quadruple value0 at infinity. This formula defines all seven sections without
listing their expanded coefficients.

The seven additional triple nodes, in the displayed T order, are

    T=123,124,156,257,346,357,467,

    (q^2-13q-3)/5,
    (-q^2+13q+8)/50,
    (q^2-8q-3)/10,
    (-q^2+8q-2)/10,
    (-11q^2+108q+23)/25,
    (-3q^2+34q+4)/25,
    (-7q^2+71q+1)/50.

At a quadruple node choose the common value of the four P_i outside C_j;
at a triple node choose the common value of the three indices in T_j.
The certificate reduces every operation exactly modulo q^3-10q^2+3q+1.
It checks all91 pairs of evaluation nodes are distinct, verifies all98
candidate/coordinate comparisons, and obtains EXACTLY the seven displayed
triple masks and complementary-quadruple masks. Each candidate has seven
matches; there are no extra incidences. The amplitude vector is also checked
against every necessary row, but the final direct evaluations, not those
necessary equations alone, certify the construction.

## Ordinary affine RS and true nearest distance

All finite listed nodes differ from2: each is0,1 or a nonconstant polynomial
in q of degree at most2, whereas q has degree3. Apply

    t=1/(X-2),     Ptilde_i(t)=t^3 P_i(2+1/t).

Infinity goes to0 and all14 points become finite and remain distinct. Scale
the finite received values by t^3; the received value at t=0 is the original
infinity value. Thus these are ordinary affine degree-at-most-three RS
codewords, with length14 and agreement7.

For any candidate distinct from the seven P_i, each matching received
coordinate contributes at least three pairwise intersections with this bank.
The seven nonzero cubic differences permit at most21 intersections. Hence
its agreement is at most7. Each displayed bank member already has exactly7,
so the maximum agreement is exactly7, even after extending the coefficient
field. This is a genuine nearest bank, not merely a list at an arbitrary
radius.

Any additional seven-match candidate must use exactly the seven triple nodes:
a quadruple match would exceed the21-intersection budget. It is therefore
unique if it exists, determined by any four triple nodes. The full nearest
list has size7 or8 until that separate interpolation check is completed.

## Prime-field specialization and scope

The construction specializes to every prime at which the defining cubic has
a root and all denominators and finitely many nonzero node/difference guards
remain nonzero. Clearing denominators and taking norms shows only finitely
many primes are forbidden. There are arbitrarily large primes with a root:
if only finitely many primes divided values of f(T)=T^3-10T^2+3T+1, their
product M would give f(Mk)=1 mod M, and a value of absolute size greater than1
would have a prime divisor outside that finite set. Thus this fixed bank has
realizations over arbitrarily large prime fields.

This result does not by itself provide growing list size, a better.codes
improvement, or a superlinear prime-field proximity-gap counterexample.
It supplies a new finite source geometry for subsequent exact amplification
and identity searches. The orbit7 same-pole failure cannot automatically be
transferred to this different bank.
