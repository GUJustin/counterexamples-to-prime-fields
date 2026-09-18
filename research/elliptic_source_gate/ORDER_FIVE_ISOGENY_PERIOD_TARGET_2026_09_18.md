# Order-five shared poles: exact isogeny-period reduction and remaining target

September 18, 2026. A proved reformulation, not a positive construction. No enumeration or manuscript change.

## Exact five-period formula

Let ell be an odd prime congruent to -1 modulo 5, H=E[ell], M=ell², and identify H additively with F_(ell²). Work in characteristic different from 2,3,5,ell, with the torsion and a primitive fifth root zeta available. Let chi have order five, extended by chi(0)=0. Its restriction to F_ell* is trivial. Thus chi is constant on each cyclic subgroup L of order ell, excluding zero. Each of its five values occurs on (ell+1)/5 such subgroups.

For the normalized Velu quotient phi_L:E→E/L, put c_L=sum_(T in L, T≠0) x(T). Directly from the defining Velu formula,

    sum_(T in L, T≠0) x(P+T) = x(phi_L(P)) - x(P) + c_L.

Consequently, for the EXACT previously defined convolution function,

    F_chi(P)=sum_(T in H) chi(T)x(P+T)
            =sum_(j=0..4) zeta^j R_j(P) + c,
    R_j(P)=sum_(L:chi(L)=zeta^j) x(phi_L(P)),
    c=sum_L chi(L)c_L.

The x(P) terms disappear because sum_L chi(L)=0. This is an identity of rational functions, including principal parts, not merely a special-value formula.

The bank G_S(P)=F_chi(P+S)+F_chi(P-S) therefore becomes

    G_S(P)=sum_j zeta^j R_(j,S)(P)+2c,
    R_(j,S)(P)=sum_(L:chi(L)=zeta^j)
       [x(phi_L(P)+phi_L(S))+x(phi_L(P)-phi_L(S))].

Each R_(j,S) is even in P, hence rational in X=x(P). Multiplication by the same shared denominator D0 gives exactly the existing polynomial bank Q_S. No degree, bank-size or agreement improvement follows merely from this rewrite.

## A precise common-remainder test

Let K contain the torsion data, and let G(X) be squarefree and coprime to D0. In K(zeta)[X]/(G), the necessary and sufficient equality test is

    sum_j zeta^j (R_(j,S)-R_(j,S0)) = 0.

All denominators are units. If additionally [K(zeta):K]=4 and G is defined over K, this is equivalent to the FOUR equations

    R_(j,S)-R_(j,S0) = R_(4,S)-R_(4,S0),  j=0,1,2,3.

Without these field and factor-descent hypotheses, coefficient splitting is invalid. In particular a split prime field containing zeta does not permit it.

This identifies the exact missing identity: five isogeny-period translates must acquire common remainders on a growing collection of offpole divisors. An identity for one isogeny, one CM special value, or the convolution inverse does not establish these four simultaneous congruences.

## Quantitative acceptance criterion before a job

For M=ell², L=(M+1)/2, N=4M, any proposed factors G_j and buckets B_j must satisfy:

* G_j are squarefree, mutually coprime and coprime to D0;
* each congruence above holds for all S in B_j;
* sum_j deg(G_j)≤4M;
* every retained S belongs to buckets of total degree greater than 4*a1(1/4)*M, asymptotically 1.8751 M.

The last condition must be checked per candidate, not just in total. In an offpole-only design the mean bucket density must exceed a1(1/4), approximately 0.4688. The h=5 pair budget allows at most 1.9267 M agreement, so the margin for such a design is narrow.

The earliest prime with the subgroup-period simplification is ell=19: 20 cyclic quotient maps grouped four per period, M=361 and L=181. A proposed symbolic factor family should therefore specify its buckets and predicted factor degrees before a specialization job. A generic triple gcd, a census of all evaluation values, or special values with buckets of density 1/5 or 2/5 would not test a sufficient positive mechanism. No such sufficient factor family has been found here, so no job is proposed for execution yet.

## Literature and descent scope

Moody–Rasmussen, Character sums determined by low degree isogenies of elliptic curves, https://arxiv.org/html/1210.2743, Section 2.1 supplies the Velu formula; their Theorem 1 transports a finite-field cokernel-character sum to a weighted kernel sum. That character and scalar identity do not assert equal remainders for the translated functions above.

Asai, Elliptic Gauss Sums and Hecke L-values at s=1, https://arxiv.org/abs/0707.3711, studies quartic CM Gauss-sum special values. Its stated theorem does not supply the required order-five shared-factor identity. Neither source is being cited as an exclusion of other elliptic identities.

For a characteristic-zero identity with all required nonvanishing guards, one can put its finitely many coefficients, torsion points and selected roots in a number field and reduce at sufficiently large completely split good primes. This gives prime-field realizations for each fixed ell, without a bound on the prime as ell grows. It cannot convert an unproved factor pattern into a construction. Exclude also the finite cyclotomic additive-collapse primes from HIGHER_CHARACTER_COLLISION_BUDGET_2026_09_18.md; the crude ambient guard p>256 suffices for that particular h=5 issue.

Conclusion: the five-period formula is an exact reduction of the surviving h=5 task. A growing balanced common-remainder identity remains missing. Current primary-source identities do not yet provide a positive construction or justify another fixture scan.
