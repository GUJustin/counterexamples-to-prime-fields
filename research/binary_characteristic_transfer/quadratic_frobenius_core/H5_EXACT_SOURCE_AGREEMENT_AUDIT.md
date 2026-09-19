# h=5: exact source agreements from a branch classification

2026-09-18. Independent verdict: **PASS for the p=97 fixture and the corrected general onset below**. No scan or manuscript edit. The proposed p+45 bound must be replaced by max(p,25)+45 when p<25; thus the argument proves the general exact-source conclusion for admissible primes p>=17, not p=13.

## One coefficientwise-B branch

Let B=F_(p²), p odd, with 5 dividing p²+1, and let P in B[Z] have degree at most five. Consider solutions z in B of

    z^(5p)=P(z).

Put u=z^p. Every solution gives a common zero of

    F(Z,U)=U^5-P(Z),
    G(Z,U)=Z^5-P^sigma(U),

where sigma is coefficientwise p-th power. Distinct z give distinct affine pairs (z,u).

Suppose P is nonconstant and not a fifth power over the algebraic closure. Since five is prime and the characteristic is not five, the Kummer polynomial U^5-P(Z) is irreducible over the rational function field, hence in the polynomial ring by Gauss's lemma. Here P is a fifth power in the rational function field exactly when it is a fifth power polynomial up to a scalar, and every scalar has a fifth root over the algebraic closure.

Both F and G have total degree exactly five. If they shared a component, irreducibility would force G=cF for a nonzero scalar c. Comparing the separated Z and U terms then forces

    P(Z)=a Z^5+b.

This is only a necessary condition for a shared component; the appropriate conjugate coefficient identities are also needed for sufficiency. In particular, if P has a nonzero intermediate coefficient, no shared component exists. Bezout then bounds the number of affine solutions by25.

If P is a nonconstant fifth power, its degree bound implies P=(aZ+b)^5 over the algebraic closure. This representation descends to B. The leading coefficient has a unique fifth root a in B because gcd(5,p²-1)=1; the coefficient of Z^4 determines b in B by division by5a^4. Consequently fifth-power injectivity on B gives the exact equivalence

    z^(5p)=P(z)  iff  z^p=a z+b.

The latter equation has at most p solutions: it is a nonzero degree-p polynomial, or equivalently an affine semilinear equation with kernel size at most p. Constant P has at most one solution by the same fifth-power permutation and is not a missing exception.

Thus for any P with a nonzero intermediate coefficient, its branch match count is at most max(p,25). The proof distinguishes the non-fifth-power and fifth-power cases; it does not claim that every P=aZ^5+b shares a component.

## From one branch to the whole h=5 domain

Use the primitive-scale higher-power construction with h=5. There are five B* branches per full block, at most ten total. Let Q be any degree-at-most-five polynomial outside the canonical family aX^5+b. It has some nonzero coefficient q_j with1<=j<=4.

Within either block, coefficientwise-B membership on two different branches would imply

    (M/5)*j*(t-u)=0 mod M,  M=p²+1.

Since gcd(j,5)=1, the branch indices must coincide modulo5. There is therefore at most one coefficientwise-B branch per block. The existing cross-block obstruction, valid when4<M/5, rules out good branches in both blocks. Hence there is at most ONE good branch in the entire domain.

On that branch the normalized polynomial P retains the same nonzero intermediate coefficient, so the preceding classification applies. Every other branch contributes at most five matches by the B-linear projection argument. If no branch is good, all ten contribute at most50. Therefore, uniformly in the challenge,

    noncanonical agreement <= max(p,25)+45.

Arbitrary puncturing, including the deterministic complete-branch-plus-prefix rule, preserves this bound. The ten-branch estimate is deliberately conservative and does not need the partial branch to be analyzed separately.

## Corrected consequences

For p>=25 the bound is p+45. For admissible primes17<=p<25 it is70, still less than5p. Therefore for every admissible prime p>=17, every noncanonical polynomial has fewer than5p matches. Canonical polynomials outside the doubly canonical label planes have at most5p matches, as in the existing theorem. At either explicit endpoint outside the planes, a nonzero core canonical fiber attains5p. Thus both individual source agreements, and the already proved ordinary common agreement, are EXACTLY5p.

For p=97, noncanonical agreement is at most142<485. The deterministic small fixture therefore has

    A(r0)=A(r1)=CA=485,  T=593,  k=6,  n=70560.

Its source-loss/capacity ratio sharpens to

    (593-485)/(593-6)=108/587,

while its exact threshold-list profile is unchanged. This is an exact algebraic improvement of the source agreement assertion, not an enumeration of all degree-five codewords.

For p=13 the available uniform bound is70>65, so this proof does not establish exact source agreement there. It neither disproves that equality nor supplies an obstruction; a further argument would be needed. No such additional scan or classification is asserted here.
