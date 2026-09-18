# Targeted products and the norm-denominator tradeoff

September 18, 2026. The algebraic compiler and exact finite checks pass.
The natural code alphabet is the subfield K; E is an auxiliary field.
These are existence results for a selected union of base-field fibers,
not an explicit tag list or a prescribed NTT evaluation domain.

The input-ready proof is `target_subset_norm_compiler.tex`. The separate
pointwise-moment audit is `TARGET_SUBSET_SECOND_MOMENT_INDEPENDENT_AUDIT.md`.
The exact verifier `verify_target_subset_norm_compiler.py` passes and
saves `target_subset_norm_compiler_verified.json`.

## The identity and what it changes

Let E=Fp^d, K=Fp^(d/e), e|d, and let b have degree d over Fp. Put

    T(Z)=Norm_E/K(Z-b),  Y=X^m,
    n=(s+1)m,  J=w+(r-e-1)m+1,
    f=R Y^(r-e),  g=R/T(Y).

Here R is the monic locator of w<m points in a reserved fiber, and
the other s tags form G. For V_S(Z)=product_{a in S}(Z-a), |S|=r,
the condition V_S(b)=lambda in K implies T | (V_S-lambda). Hence

    h_S = R [T(Y)Y^(r-e)+lambda-V_S(Y)] / T(Y)

is a K-polynomial of degree at most J-1, and the residual is
R V_S(Y)/T(Y). No additional leading Fp coefficient is fixed.
All words and witnesses are K-valued, although products were analyzed
in E*. The exact profile is

    agr(f) = CA(f,g) = J+m-1,
    J+m-1 <= agr(g) <= J+em-1,
    agr(f+lambda*g) = J+(e+1)m-1  for represented lambda in K*.

The common-agreement gap is em/n; the guaranteed gap for both
individual sources is m/n. The latter is only a lower bound because
the rational direction's agreement need not attain its root-count
upper bound. All these statements concern the dimension-J code over K.
After an affine-mixture reparametrization at most one represented label
is lost (lambda=-1); the two endpoints themselves are farther.

Arbitrary affine K-coset averaging does **not** prove this profile:
the center R V_0(Y)/T(Y) is generally rational and already close.
The pointwise-missing lemma below targets the distinguished set K*
directly, which is what permits the polynomial center above.

## Pointwise moment and exact finite checks

For a P-element population in a group of order M with nontrivial
character bias at most epsilon, draw s iid elements temporarily.
Write L=binom(s,r), b_u=binom(r,u)binom(s-r,u), and

    V=(M-1)/L * sum_u b_u epsilon^(2u)
      +(M-1)(M-2)/L * sum_u b_u epsilon^(r+u),
    a=1-binom(s,2)/P.

For each specified target z, let Z_z count its subset representations.
Expanding E[(M Z_z/L-1)^2] gives the uniform bound V: the inverse
character pairs give the first sum and the remaining nontrivial pairs
give the second. Both single-trivial terms cancel exactly. This is not
an independence assertion about subset products. If a>0, conditioning
on distinct draws divides the nonnegative missing-target expectation
by at most a. Thus one distinct seed represents at least

    |B| - floor(|B| V/a)

elements of any fixed target set B. Taking B=K* is legitimate.

For KoalaBear p=2130706433 and auxiliary degree six, use
P=(p-1)/m-1 and epsilon=(6*46160+1)/P, with sqrt(p)<46160.
At n=262144, J=131072, m=1024, s=255, w=1023, r=128+e,
all four e=1,2,3,6 satisfy the exact rational inequality V/a<2^-22.

| Native degree [K:Fp] | Norm degree e | Near agreement | Common gap numerator | Guaranteed both-source gap numerator | Missing native-label fraction, approximately |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 6 | 1 | 133119 | 1024 | 1024 | 1.79149e-7 |
| 3 | 2 | 134143 | 2048 | 1024 | 1.84080e-7 |
| 2 | 3 | 135167 | 3072 | 1024 | 1.91733e-7 |
| 1 | 6 | 138239 | 6144 | 1024 | 2.35060e-7 |

Gap numerators are divided by n. The common and polynomial-source
agreement is 132095 in every row. In the prime row the exact rational
test guarantees at least **2130705932** nonzero good labels out of
2130706432; it does not establish all labels. At m=512 the same test
does prove all native labels for all four e, with the smaller margins
given by the compiler. The verifier also checks the Proth certificate
127*2^24+1 with witness 3, and uses only integer/rational inequalities.

For auxiliary degree six, m=2048 leaves at most 127 nonreserved tags.
Already the u=0 term implies

    V/a >= (p^6-2)/binom(s,r) > 1

for every r, since binom(127,63)<p^6-2. Larger admissible fibers make
this test only worse. Thus m=1024 maximizes the norm compiler's margin
**under this sufficient pointwise-moment certificate**, at these n,J
and this fixed auxiliary degree. This does not exclude a tag set whose
products concentrate much more strongly on K*, nor another proof.

## Matched one-pole comparison

Changing the alphabet changes the appropriate comparison. A one-pole
compiler analyzed directly in K has a smaller group order and better
character bound. At the same n,J it passes the identical pointwise
moment test at the following fibers.

| Native degree | One-pole m | Capacity numerator | Common gap numerator | Guaranteed both-source gap numerator | Missing fraction, approximately |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 4096 | 8191 | 4096 | 4096 | 9.78068e-8 |
| 2 | 2048 | 4095 | 2048 | 2048 | 2.50523e-15 |
| 3 | 2048 | 4095 | 2048 | 2048 | 7.20098e-4 |
| 6 | 1024 | 2047 | 1024 | 1024 | 1.79149e-7 |

Each is the largest fiber passing this particular positive-coverage
test: at its next doubled fiber, even the central binomial is below
the group's order minus one, forcing V/a>1. This comparison is exact
in the verifier; the decimals are explanatory only.

Accordingly, the prime norm row has a smaller capacity margin but
larger common-agreement gap and smaller guaranteed endpoint gap than
the one-pole row. The square norm row preserves the capacity margin
and increases the common gap, at the cost of endpoint separation and
the certified label fraction. The cubic norm row has a smaller
capacity margin, the same absolute common gap, and a better certified
label fraction. There is no blanket domination. The largest displayed
agreement is the prime one-pole value 139263, still 519 short of
139782, on a selected rather than prescribed domain.

## Asymptotic comparison: valid but already obtainable by dimension shift

For fixed e>=2, one can instead use all-product completion in auxiliary
E=Fp^e. On the existing prime-progressions with p=Theta(m^beta),
beta>12/5, the population size is a positive power of p and its bias
is O(p^(-(1/2-1/beta))). For s=C log p and fixed code rate rho, the
leading-entropy completion theorem applies when C>e/h(rho). It covers
all of E*, hence all native prime labels. The norm compiler is below
the prime-alphabet Elias threshold when C<(e+1)/h(rho). It therefore
has the valid nonempty window

    e/h(rho) < C < (e+1)/h(rho),

with polynomial prime alphabet, common-gap fraction tending to
e/(e+1) of the capacity margin, and guaranteed endpoint-gap fraction
tending to 1/(e+1).

This is **not a new asymptotic tradeoff** relative to the general
dimension-shift version of the one-pole compiler. If a one-pole fiber
m'=e*m is available, increase its code dimension by t=(e-1)*m.
Writing the final dimension as J, its profile becomes exactly

    source f/common: J+m-1,
    direction upper: J+em-1,
    near: J+(e+1)m-1.

The rescaling C'=C/e changes the displayed norm window into the
dimension-shift window 1/h(rho)<C'<(1+1/e)/h(rho). More generally,
t/m' approaching 1-1/e gives the same asymptotic comparison without
requiring exact finite divisibility. Comparing only with the extreme
shift t=m'-2 would obscure this equivalence. Finite divisibility and
the distinct label-count certificates can still differ; no literature
priority or stronger asymptotic Pareto claim follows here.
