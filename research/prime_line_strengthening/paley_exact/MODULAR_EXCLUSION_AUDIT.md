# Degree-preserving modular gcd certificates: independent proof audit

**PASS.** This gives a characteristic-zero exclusion from a finite-field
polynomial gcd, not merely from an unsuccessful finite-field root search.
No numerical assertion is made by this proof note.

## Integral univariate lemma

Let O be a discrete valuation ring with fraction field K and residue
field k. Let E_1,...,E_m in O[A] have degrees at most d. Assume:

1. at least one reduced polynomial has degree exactly d;
2. the gcd of all reduced polynomials in k[A] is1.

Then the E_i have gcd1 in K[A], and hence have no common root over any
algebraic extension of K.

Proof. The first condition gives an E_i whose leading coefficient is a
unit and whose degree is d. Divide by that unit to obtain a monic
polynomial in O[A]. If a monic nonconstant F in K[A] divided every E_j,
then every root of F would be integral over O. Its coefficients, being
symmetric functions of these roots and lying in K, are integral over O
and therefore lie in O, since O is integrally closed. Monic polynomial
division then shows every E_j is divisible by F already in O[A]. The
reduction of F is still monic of positive degree, contradicting condition2.

Only **one** E_i must attain the known characteristic-zero upper degree
d after reduction. The other polynomials may lose degree or vanish.
No claim follows when the degree-preservation condition fails. For
example p*A−1 has no reduced root and reduces to a nonzero constant,
although it has a characteristic-zero root; its degree falls on reduction.

## Application to cyclic support elimination

Fix a primitive qth root zeta and work over K=Q(zeta). Let S have size
r+1 and T size r. The two support polynomials are monic products of
(X−zeta^i), hence belong to Z[zeta][X]. Consequently

    P=X^h mod B_S,
    v=X^h mod A_T,
    R(A,X)=P(A X) mod A_T

all have integral cyclotomic coefficients, because monic remainder
computation introduces no denominators. The coefficients R_j(A) have
degree at most r. For any index k with v_k!=0, form

    E_j(A)=v_k R_j(A)−v_j R_k(A).

These belong to Z[zeta][A] and have degree at most r. A common root A
is exactly a scaling parameter for some c=R_k(A)/v_k.

Choose a prime p=1 mod q and an element zeta_p of exact order q. Evaluation
zeta -> zeta_p gives a prime of the ring of integers above p; localizing
there gives the DVR in the lemma. All polynomials reduce to the result
of computing the same monic remainders directly in F_p. Select the pivot
k with v_k nonzero **modulo p**, which in particular guarantees v_k!=0
in characteristic zero. If gcd_j(E_j mod p)=1 and one E_j mod p has
exact degree r, the characteristic-zero support pair is excluded for
all algebraic scaling parameters, even those not belonging to F_p or K.

The resulting certificate needs: p, an exact-order q root zeta_p, S,T,h,
the pivot, a polynomial-gcd certificate (or reproducible Euclidean
calculation), and an equation whose leading coefficient at degree r is
nonzero. Merely testing all A in F_p does not certify this conclusion.

## Removing known forbidden roots safely

If T+t is a subset of S, then interpolation gives

    P(zeta^t X) = zeta^(ht) X^h mod A_T(X).

Thus every E_j vanishes exactly at the specified parameter A=zeta^t
(with no claim that its multiplicity is exactly one). The monic product

    H(A)=product_{t: T+t subset S}(A−zeta^t)

therefore divides every E_j over Z[zeta]: the roots are distinct and
monic division preserves integrality. These are overlapping-orbit
parameters. Divide out H, use the new degree bound r−deg H, and apply
the modular lemma to the quotients. If it passes, the only possible
characteristic-zero scaling parameters are these known forbidden roots.
Repeated removal requires an additional exact multiplicity proof; a
repeated modular factor alone does not justify it. Similarly, removing
A=0 needs an exact characteristic-zero vanishing assertion.

## Scope and sign of the conclusion

A passing modular certificate proves a negative characteristic-zero
statement for the specific supports and twist. An inconclusive prime
can be replaced by another, or investigated by exact arithmetic; it is
not evidence for a positive construction by itself. The method works
for non-difference-set compatible profiles as well as Singer/Paley sets.
It does not prove that the enumerated supports themselves are exhaustive;
that remains the separate incidence/profile classification theorem.
