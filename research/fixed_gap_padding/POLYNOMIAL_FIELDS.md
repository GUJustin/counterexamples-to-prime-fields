# Polynomial-size fields for the fixed-gap lower bounds

September 17, 2026. Self-audited strengthening; no novelty claim for the
character-sum or least-prime tools. This replaces the splitting-prime
existence step for selected lists and actual correlated-agreement
failure. It does NOT retain the whole-line uniqueness assertion.

## Simultaneous power-residue shifts

Let a_1,...,a_m be distinct in F_p and B divide p-1. Let N count shifts
c for which every c+a_i is a nonzero B-th power. Then

    N >= p/B^m - m*sqrt(p) - m.

Proof: use the indicator B^-1 sum_{j=0}^{B-1} chi^j(x), extending every
character, including the principal character, by zero at zero. Expand
the product of m indicators. The all-principal term is p-m. For every
other tuple the complete character sum has absolute value at most
m*sqrt(p)+m: the usual product-character Weil bound is m*sqrt(p), and
removing the at most m excluded shifts costs at most m, independently
of the convention for the principal character at zero. Dividing the
sum of the bounds by B^m gives the displayed conservative inequality.
The distinct shifts ensure that the nontrivial character tuple cannot
become a trivial multiplicative character of the rational function.
In particular p>16*m^2*B^(2m) suffices for N>0 (m,B>=1).

Source checked: Bourgain--Garaev--Konyagin--Shparlinski, arXiv:1110.0812v2,
Lemma 17, with constant additive phase. This gives the deliberately
nonsharp m*sqrt(p) bound. Only that mathematical estimate is used:
https://www.ias.edu/sites/default/files/math/csdm/11-12/jbourgain_on_the_hidden_shifted_power_problem.pdf

## Transporting the anchored construction

Fix any integer seed from PROOF.md, with common anchor a_*=1. For a
large enough p, its m nodes remain distinct. Choose the shift c above
and alpha with alpha^B=c+a_*. Put W_c(Y)=W(Y-c) and G_{i,c}(Y)=G_i(Y-c).
The degree bounds and distinct locator supports are unchanged. On the
union of the m full fibers X^B=c+a, remove alpha and use

    F_old(X) = (W_c(X^B)-W(a_*))/(X-alpha),
    P_i(X)   = (G_{i,c}(X^B)-W(a_*))/(X-alpha).

These are polynomials, of degrees Bt-1 and at most B(k-1)-1. Each
selected P_i agrees at exactly Bt-1 old coordinates. For flexible
parameters n,K,q=n-mB+1 satisfying q>=1, K>=B(k-1), K-1+q<Bt, choose
padding points separating ONLY the fixed L selected candidates.
It suffices that

    p > mB+(K-1)*binom(L,2)+q,
    p > (q-1)*L^2.

The offsets then make the Lq selected labels distinct. The exact same
degree argument bounds common agreement for all pairs of codewords by
max(Bt-1,K-1+q)<Bt. Thus every displayed nearby label is an actual
ordinary correlated-agreement failure. Extra candidates and extra
nearby labels are allowed; uniqueness is not claimed.

For the list-only version, restore alpha and use W_c(X^B),G_{i,c}(X^B)
on all fibers, with arbitrary extra coordinates to reach n. Every
selected candidate has exactly Bt agreements.

## Polynomial field-size bound

For each fixed seed, take B tending to infinity through the required
integer multiples. Apply Linnik's theorem to the residue class 1
modulo Q=B^(2m+2). There are absolute constants C,L_0 such that its
least prime satisfies

    B^(2m+2) < p <= C*B^((2m+2)*L_0).

The lower bound uses p=1+jQ with j>=1. It ensures B divides p-1 and,
for B>4m, the positive shift-count bound above. Since the seed, L,
and all ratios n/B,K/B,q/B are fixed, the two padding inequalities,
node distinctness, and strict Elias also hold for all large B.
Consequently n=o(p) and p=n^{O_seed(1)}. No assertion about the
optimal Linnik exponent is needed. Primary source checked for the
absolute power bound: Xylouris, On Linnik's constant,
https://arxiv.org/abs/0906.2749 (Acta Arith. 150 (2011), 65--91).

Applying PRESCRIBED_GAP.md gives, at every sufficiently small rational
eta and fixed rational rho, the SAME lower bound

    log_2 C_rho(eta) >= (H_2(rho)^2/2-o(1))/(eta^2 log_2(1/eta))

for genuine bad-label counts C_rho(eta)*n, now with polynomial-size
prime fields. The exponent may depend on rho and eta; from the displayed
seed parameters it is O_rho(eta^-2/log(1/eta)) as eta tends to zero.
The first eligible length and implicit constants are not uniform in eta.
The corresponding fixed finite list lower bound has the same property.

The entire-line uniqueness proof in UNIQUE_NEARBY_PADDING.md separates
an exponentially large interpolation pool. Its field bound is not
polynomial by this argument. Nor does the shifted-fiber construction
imply the exact-list rigidity proved by a different prime-selection
argument. No fixed prescribed subgroup or better.codes instance follows.
