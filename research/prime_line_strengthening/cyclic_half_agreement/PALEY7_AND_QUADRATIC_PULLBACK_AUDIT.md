# Independent Paley-seven identity and all-congruence-prime pullback audit

Verdict: PASS. Let zeta have order7 and set
eta=zeta+zeta^2+zeta^4, eta_bar=-1-eta. Then eta^2+eta+2=0 and

    A(X)=(X-zeta)(X-zeta^2)(X-zeta^4)
        =X^3-eta X^2+eta_bar X-1.

For P(X)=eta X^3+X^2+X+eta_bar, direct multiplication gives the exact identity

    P(X)-X^5=(eta_bar-X)(X-1)A(X).

Thus P agrees with X^5 at the four first-coset positions0,1,2,4.
Modulo A, one has X^4=-X^2-X+eta and X^5=eta_bar X^2-X-1.
Put

    alpha=eta_bar/eta=(eta-1)/2,
    c=3(eta+3)/4.

The relations alpha^2=(-3eta-1)/4 and alpha^3=(5eta+7)/8 show directly that
P(alpha X) has remainder c*(eta_bar X^2-X-1) modulo A. Hence it agrees
with cX^5 at positions1,2,4 of the second coset.

All guard claims can be made uniform. Eta and eta_bar are nonzero outside
characteristic2. The quadratic norm of alpha^7-1 is343/128; this follows
from alpha+alpha_bar=-3/2, alpha*alpha_bar=1 and the power-sum recurrence.
Thus alpha^7!=1 outside characteristics2,7. Finally c!=0 outside2,3,
since eta=-3 would make eta^2+eta+2=8 vanish. The cyclic bank and its exact
complete-list proof therefore work over every field of characteristic not
in{2,3,7} containing a primitive seventh root. In particular they work over
EVERY prime field with p=1 mod7. No unspecified finite bad-prime exclusion
is needed for this compact construction.

In characteristic3, the same identities instead have c=0 and produce a
complete list of eight cubics over a field containing mu7. This is a real
exception to an all-odd-characteristic universal max-seven statement.

## All sufficiently large primes in the congruence class: exact quarter rate

Let A be the fourteen distinct affine coordinates of this compact bank over
F_p. We seek c0 such that all a-c0, a in A, are nonzero squares. With the
quadratic character chi, expand

    2^-14 sum_c product_(a in A)(1+chi(a-c)).

Every nonempty subset of size k contributes a character sum bounded in
absolute value by(k-1)sqrt(p), because its polynomial has k distinct roots.
The sum of these coefficients is

    sum_(k=1)^14 binom(14,k)(k-1)=98305.

Deleting the fourteen possible zero positions costs at most14 (in fact7
suffices). Therefore the number N of good shifts satisfies

    N >= (p-98305 sqrt(p))/16384 -14.

This is positive for p>10^10: at sqrt(p)=100000 the numerator is169500000,
and the expression increases thereafter. Each good shift makes all fourteen
fibers of U^2+c0 split into two distinct F_p-points. Pulling back the bank
gives fourteen agreements on28nodes by seven degree-at-most-six polynomials.
The complete list remains exactly seven by the previously audited pullback
argument. Hence dimension7 is exactly quarter rate over every prime
p=1 mod7 with p>10^10.

Primary-source verification: Kim, Yip and Yoo, *Explicit constructions of
Diophantine tuples over finite fields*, Ramanujan Journal65 (2024),163–172,
Lemma2.1 states the distinct-root Weil bound used above. Their Lemma2.2
already gives the stronger bound N>=p/16384-(6+1/16384)sqrt(p)-7 for this
fourteen-sign instance. DOI:10.1007/s11139-024-00888-5.
https://link.springer.com/article/10.1007/s11139-024-00888-5

This audit concerns a fixed list of seven, not a growing family or a
better.codes improvement.
