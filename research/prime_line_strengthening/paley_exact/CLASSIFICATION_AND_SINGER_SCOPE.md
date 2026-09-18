# Exact Paley scaling classification and the distinct Singer route

## Outcome

Over characteristic zero, the two-orbit construction with first support
`{0} union QR` has no continuation at q=11,19,23 when its second support is
QR or NQR, for **any** scalar twist h=(q+1)/2,...,q−1 and any algebraic
nonzero orbit ratio alpha with alpha^q != 1. This is an exact elimination
of alpha over an algebraic closure, not a finite-field sample. At q=7 the
same calculation recovers precisely the established h=5, QR construction.
It does not exclude arbitrary second supports, noncyclic constructions,
or the Singer supports at q=31,127.

## General exact criterion

Let q be odd, r=(q−1)/2, zeta a primitive qth root, and choose supports
S,T subset Z/q with |S|=r+1, |T|=r. Write

    B_S(X)=product_(s in S) (X−zeta^s),
    A_T(X)=product_(t in T) (X−zeta^t).

After scaling the first received value to one, a cyclic candidate bank
with coefficient twist h has its base polynomial uniquely forced:

    P(X)=X^h mod B_S(X),  degree P <= r.

For h<=r this is the monomial X^h and the whole cyclic bank coincides, so
only r<h<q is relevant. The second orbit alpha mu_q with received scalar
c has the prescribed matches exactly when

    P(alpha X)−c X^h = 0 mod A_T(X).                    (1)

Write the two remainder vectors as R_j(alpha) and v_j, 0<=j<r. Since
A_T has no zero root, X^h mod A_T is nonzero; choose any v_k!=0.
Eliminating c from (1) gives the univariate equations

    f_j(alpha)=v_k R_j(alpha)−v_j R_k(alpha)=0.

Their gcd G is a complete criterion: every root alpha of G gives a unique
c=R_k(alpha)/v_k, and conversely. Delete roots alpha=0 and alpha^q=1 to
impose nonzero, disjoint orbits; additionally test c!=0 and distinctness
of candidates for any surviving positive instance. A translated second
support T+t is absorbed by replacing alpha with alpha*zeta^t (and
rescaling c), so translates of the tested supports are covered.

This criterion holds over the full algebraic closure of the coefficient
field. No restriction that alpha itself belong to the period field is
made. It is therefore stronger than searching alpha in one prime field.

## Paley specialization and exact results

For prime q=3 mod4, let eta=sum_(j in QR) zeta^j. Then
eta^2+eta+(q+1)/4=0. The polynomial A_QR has coefficients in Q(eta),
A_NQR is its conjugate, and B_S=(X−1)A_QR.
The script first constructs A_QR by multiplication in
Z[Z]/(1+Z+...+Z^(q−1)). It verifies that every coefficient is a constant
plus a multiple of eta and that A_QR*A_NQR=Phi_q exactly. It then forms
all remainder equations and computes their exact univariate gcd over
Q(sqrt(−q)).

The *raw* gcds, before deleting any inadmissible roots, are:

| q | twists tested | target QR | target NQR |
|---|---|---|---|
| 7 | 4,5,6 | alpha−1 except h=5 below | 1 |
| 11 | 6,...,10 | alpha−1 in every case | 1 |
| 19 | 10,...,18 | alpha−1 in every case | 1 |
| 23 | 12,...,22 | alpha−1 in every case | 1 |

At q=7,h=5 the raw gcd is

    (alpha−1)(alpha+(3−sqrt(−7))/4).

The unique disjoint-orbit root is alpha=(−3+sqrt(−7))/4=(eta−1)/2,
which agrees with the independently proved compact identity. The
ubiquitous QR root alpha=1 is the overlapping-orbit solution and is
inadmissible. Thus the negative conclusions do not rely on a subtle
saturation or a factor with unknown geometric meaning.

Reproduce each row with `classify.py q --output q.json`, under the
repository's 384 MiB/60 s watchdog. Saved q7/q11/q19/q23 JSON files contain
the period coefficients, every forced P, and every raw and reduced gcd.
Elapsed arithmetic times were 0.36,1.09,4.58,7.33 seconds respectively;
all jobs completed within the guard. These are computer-assisted exact
identities, not a proposed general theorem for every q>7.

## Why the Singer search is genuinely different

Let q=2^d−1 be prime, d odd, and identify nonzero elements of F_(2^d)
with powers of a primitive element gamma. Set

    D={j : Tr(gamma^j)=0},   S=(Z/q) \ (−D).

Then |D|=r, |S|=r+1. The standard trace calculation, also verified by
`singer/generate.py`, gives |D intersect(D+t)|=(q−3)/4 for t!=0.
The complementary small support C=−D has the same intersection counts.
Consequently these two cyclic incidence blocks satisfy precisely the
pairwise cubic-style saturation requirements for degree r. This verifies
the incidence budget; it does not construct polynomial evaluations.

For q=7, D=QR and S={0} union QR. For q=31 and127 that simplification is
not available: **S must be taken as complement(−D), not silently replaced
by {0} union D**. Multiplication by2 preserves D and S. Their cyclotomic
root polynomials therefore have coefficients in the fixed field of
<2>, of degree (q−1)/d: degree6 for31 and degree18 for127. The q=7 fixed
field is quadratic; this explains why its compact identity has quadratic
coefficients. The Paley exclusions above concern a different quadratic
period field and do not rule out these higher-degree fields.

A precise positive target is now available without guessing a polynomial:
for each Singer multiplier class, construct B_S, take
P=X^h mod B_S, and apply criterion (1) with T=D (or its multiplier
classes). The natural twist inherited from the projective action on
binary forms of degree r is h=(3q−1)/4; all r<h<q twists can also be
examined. A nontrivial common gcd root, followed by c!=0 and bank
nondegeneracy checks, is a complete algebraic witness for that family.

The fact that the trace set is defined using F_(2^d) supplies the
combinatorial supports only. The identities required here are in
characteristic zero or odd characteristic. Frobenius linearization of
the trace polynomial in characteristic2 cannot be imported as an
odd-characteristic polynomial identity. No unbounded construction or
universal Singer obstruction follows from the present calculations.

### Composite Singer sizes avoid a number-theoretic infinitude assumption

The preceding incidence construction does not actually require q to be
prime, nor d odd. For every d>=2, put q=2^d−1 and use the same trace-zero
Singer difference set. Its parameters remain
(q,(q−1)/2,(q−3)/4), so the same two-support pair budget and polynomial
remainder criterion apply over any field containing a primitive qth
root with characteristic not dividing q. The natural h=(3q−1)/4 is
integral and gcd(h,q)=1, since 4h=3q−1. In particular q=15,d=4 is a
legitimate smaller new test. When d is even, 0 belongs to D and therefore
not to S; nothing in the interpolation criterion requires 0 in S.
For composite q the cyclotomic fixed-field degree is phi(q)/d because
ord_q(2)=d, rather than (q−1)/d. Thus q=15 has a quadratic period field,
although its support is not a Paley residue set. A hypothetical identity
valid for all d would yield unbounded sizes without assuming infinitely
many Mersenne primes. No such identity is proved here.

## Exact q=15 Singer outcome

`singer15.py` verifies the primitive F16 basis X^4+X+1 and obtains

    D={0,1,2,4,5,8,10}, S={1,2,3,4,6,8,9,12}.

Every nonzero difference has multiplicity3. For a primitive fifteenth
root, set eta=zeta+zeta^2+zeta^4+zeta^8. Then

    eta^2−eta+4=0,  bar_eta=1−eta,
    C(X)=X^4−eta X^3−2X^2−bar_eta X+1,
    A_D(X)=(X^3−1)C(X),  B_S(X)=Phi_5(X)C(X).

The script checks C*bar_C=Phi_15 and B_S*A_(-D)=X^15−1 exactly.
There are precisely two unit-multiplier classes, represented by D and
−D. For every h=8,...,14, and each target class, the raw elimination gcd
is **1**. Thus no alpha at all realizes these prescribed second-support
matches, even before checking disjointness, c!=0, or candidate orbit
size. Conjugation covers the other first-support multiplier class;
translations of supports are absorbed by the usual orbit/candidate
relabeling. This is a negative classification of the Singer two-support
ansatz at q15, not a theorem excluding arbitrary half-agreement banks at
length30.

The job completed in2.51 seconds of arithmetic, below the 384MiB/60s
guard. `q15.json` records all fourteen exact gcds and forced polynomials;
`q15.resources.json` records the successful watchdog run.

## Exact q=31 Singer classification

The q31 extension is now complete for all Singer multiplier classes and
all nondegenerate twists, over characteristic zero, with arbitrary
algebraic alpha. Fix the trace-zero set D from the primitive F32 basis
X^5+X^2+1 and source S=complement(−D). The six target multiplier classes
have representatives 1,3,5,7,11,15. For **every** h=16,...,30 and each
of these targets, the raw alpha elimination gcd is1. In fact the first
two nontrivial scalar-elimination equations are already coprime in all
ninety cases. Thus no source/target Singer-class pair admits a scaling
parameter, even before disjointness or bank-distinctness guards.
All six first-support classes follow by Galois conjugation: conjugating
zeta relabels both multiplier classes, and the target list is exhaustive.
Translations of either support are absorbed by rotations as before.

This closes the exact Singer-support cyclic construction at q31; it is
not an exclusion of all cyclic supports at q31 or of arbitrary n62,
degree15 half-agreement banks.

### Exact coefficient-field construction and verification

`singer31.py` starts in Q[Z]/Phi_31. Its six Gaussian period orbits are

    {1,2,4,8,16}, {3,6,12,17,24}, {5,9,10,18,20},
    {7,14,19,25,28}, {11,13,21,22,26}, {15,23,27,29,30}.

For eta equal to the first period, exact multiplication gives

    eta^6+eta^5+3eta^4+11eta^3+44eta^2+36eta+32=0.

The script checks irreducibility and that powers 1,...,eta^5 are a basis
of the fixed field. It recovers this basis by a six-by-six rational
matrix, then checks multiplication compatibility on every pair of the
six spanning period vectors. Each source and target polynomial is first
constructed as a product of its cyclotomic linear factors, then converted
through this verified field embedding. Additional assertions check:

* all31 powers in the claimed F32 representation are distinct;
* every nonzero difference in D occurs seven times;
* all six target polynomials are distinct;
* B_S times A_(-D) equals X^31−1 exactly.

The final regression run contains all ninety exact gcds, completed in
0.78 seconds, below the 384MiB/60s watchdog. `q31_all.json` includes the
minimal polynomial, supports, source coefficients, equations used, every
raw/reduced gcd, and completion flag. `q31_all.resources.json` and
`q31_all.log` contain the successful run record. `q31_h23.json` preserves
the initial natural-twist pilot separately.

These are finite exact eliminations. They imply exclusion over all but
finitely many characteristics for the same fixed support family (clear
denominators in the finitely many polynomial Bezout identities), but no
explicit exceptional-prime set is asserted here. The q127 family remains
unresolved by these calculations.

## Mixed q31 classification and multiplier completeness

The mixed calculation is also complete. `q31_mixed_singer.json` has120
raw gcds equal1. `q31_mixed_paley.json` has105 raw gcds1 and15 gcds
alpha−1 (the same-QR target), all inadmissible. Together these cover both
source families, all eight Singer/Paley target classes, and all twists
16,...,30. Their other source multiplier classes follow by conjugation.

There is a self-contained reason these eight targets exhaust cyclic
(31,15,7) difference sets up to translation. More generally let q be an
odd prime and D a cyclic difference set with k−lambda a power of2. In
Q(zeta_q), put a=sum_(j in D) zeta_q^j. The difference-set identity gives

    a * conjugate(a)=k−lambda.

Every prime ideal dividing(a) lies above2. The automorphism sigma_2,
zeta_q -> zeta_q^2, fixes each such prime ideal (it is the Frobenius in
its decomposition group). Hence sigma_2(a)/a is an algebraic unit. All
its complex conjugates have modulus1, so Kronecker's theorem makes it
a root of unity, necessarily ±zeta_q^t. Comparing coefficient vectors
of degree at most q−1 rules out the minus sign: their sum would be an
integer multiple of Phi_q with augmentation2k, impossible for a nontrivial
set of size0<k<q because q is odd. For the plus sign
the augmentation difference is0, so the coefficient vectors are equal.
Thus 2D=D+t, and E=D−t obeys2E=E.

For q31 the nonzero doubling orbits have size5. Since |E|=15, E cannot
contain0 and must be a union of three of the six nonzero orbits. The
independent `cyclic_half_agreement/multiplier_census.json` exhausts these
20 choices and finds exactly eight difference sets, in the Singer and
Paley unit classes. Consequently the mixed q31 result excludes **all
cyclic difference-set source/target support pairs** in this two-orbit
normal form, not merely the initially named families. It does not
exclude complementary nonconstant autocorrelation profiles.

## q127 status and remote handoff

The same multiplier argument at q127 gives unions of nine of eighteen
doubling orbits. The independent census of48620 choices finds80
normalized difference sets in six unit-equivalence classes of sizes
18,18,6,18,18,2. The native Singer class is index4 and Paley QR is index5
in the saved census; the four other classes must not be omitted.

The local natural-twist h95 Singer pilot completed targets1,3,5 with raw
gcd1, then reached its60second watchdog. Its `complete:false` checkpoint
is explicitly partial. A separate all-family adapter regression checked
census sourceclass4,targetindex4 against the native Singer result,
including equality of source coefficients and gcd; it passed in22.3sec
with76MiB peakRSS. No other q127 outcome is asserted in this note.

`remote127_allfamilies.tar.gz` contains the self-contained adapter,
verified census, watchdog, exact source/target mapping, priority36 jobs,
and remaining444 relative orientations. The first36 use six source
representatives against six target representatives at h95; these are a
priority sample, not a complete classification. All480 support-pair
jobs, and further twists if desired, are separate outstanding work.
The parent owns deployment, timing, and interpretation of remote results.
