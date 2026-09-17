# Audit: a precise method-tightness result, plus two strict improvements

September 17, 2026. This is a new local audit of a RESTORED September13
research note, not a new discovery of its statements. No independent
human referee or formal proof checker was used for this audit.

Source files and SHA256 hashes are in source_provenance.json. The note
compares with coauthor draft version(9); the directly recovered105-page
version(7) has the same first-order curve at the rates used here.

## Conclusions supported by this audit

1. At rate1/4, the exact infimum agreement threshold for the stated
   leading dimension-versus-saturated-local-rank comparison is

       a_0=(3+sqrt(133))/31=0.4687923417635740609... .

   For every fixed finite multiplicity m, positive surplus below agreement
   1/2 requires

       a > a_0+(1-2a_0)/(8m)
         = a_0+0.00780191455910648.../m.

   This covers arbitrary monomial jet supports closed under decreasing
   the Y_0 exponent, and the specified translation-stable nonmonomial
   jet spaces with their total-degree filtered benefit.

2. The exact finite supports at rates9/10 and3/4 have positive surplus
   at agreements47389/50000 and43049/50000, respectively. Each agreement
   is strictly below the sufficient curve in recovered coauthor version7.
   This conclusion uses exact finite arithmetic and does not depend on
   accepting the note's complete high-rate continuum optimization.

This is meaningful optimality of a PARTICULAR CERTIFICATE METHOD.
It is not optimality of the n versus n^2 list/MCA exponents, and it does
not prove the existence of bad codes at agreement a_0. In particular,
a global interpolation kernel can exist despite failure of the count
'dimension > n times local rank.' Exploiting global dependencies, using
a different local ideal or source class, remains outside this restored converse. The subsequent
UNIFORM_FINITE_LENGTH_CONVERSE.md handles growing multiplicity in the
full-coefficient monomial model, with its exact stated scope.

## Checked proof chain for the quarter-rate converse

**Exact local rank.** Expand T^x Y_0^u Y_1^b after Y_0=E+TY_1 in the
quotient by monomials T^i E^j with i+2j>=m. At fixed total jet degree
q=u+b and grade x-b, the surviving column matrix is a truncated
binomial-Vandermonde matrix. Its initial-row minors are nonzero when
the characteristic exceeds every retained jet degree. This gives the
stated sum of minima, counting actual local rank rather than reachable
rows. No genericity of the received word is used.

**Height sorting.** The grouped selection-sort move has an unchanged
baseline/excess overlap profile C(q) nonincreasing on the support of the
moving excess X(q). Moving that excess left compares increments of
f(C+X)-f(C), with f(t)=min(t,m-ell). Concavity proves the correct rank
inequality. Sorting decreases sum_b b H_b while preserving sum H_b and
sum H_b^2, so benefit increases. The positive-benefit triangle survives.

**Diagonal compression.** In a two-variable order ideal, diagonal
lengths are nonincreasing after the first incomplete diagonal. Moving
occupied positions toward smaller Y_1 exponent preserves feasibility
and decreases each active count in the exact rank formula. The resulting
column marginal is

    max(0,m-u-b,ceil((m-u)/2)).

**Quarter-rate continuum optimum.** On the compressed support, put
L=4a. Columns s>=L-1 have nonpositive density. For s<L-1, the density
has one crossing from negative to positive and stays nonnegative to L.
If an unsaturated endpoint has positive density, raising its preceding
prefix to L increases surplus, since earlier columns have at least as
large a density on the added interval. Every remaining partial column
has nonpositive surplus and belongs to a removable suffix. Thus a
full-prefix cap is optimal. At a=a_0 its surplus for width B<=1/2 is

    -(7/24)*B*(B-6*(1-a_0)/7)^2.

The cap surplus decreases after B=1/2. Hence every continuum support
has nonpositive surplus. Increasing a above a_0 gives a cap with positive
surplus. This argument audits the quarter-rate conclusion without
requiring the full high-rate cubic formula.

**One-sided finite comparison.** For each integer column b<=q<=Q<2m,
the continuum column integral exceeds its discrete surplus by at least
m(1-2a)/4. The exceptional square corrections5/12 and-1/12, the parity
sequence, and the removed bottom-triangle estimate have the stated
signs. At a_0 this gives a deficit of at least C*m*(1-2a_0)/4 for C
nonempty columns. Since there are at most2mC monomials, raising agreement
by a-a_0 can add at most2m^2C(a-a_0), proving the strict finite bound.
An unsigned asymptotic error would not establish this conclusion.

**Nonmonomial extension.** The first flat degeneration takes highest
homogeneous parts and preserves the total-degree filtration. The second
uses Y_1->tY_1 together with T->t^-1 T, fixing E and preserving the local
ideal. Saturation in T ensures generic rank invariance. Rank can only
decrease in the limiting monomial space. Y_0-derivative stability is
closed and implies downward closure in characteristic zero or above
the degree guard. Both degenerations are independent of m. This does
not cover arbitrary global spaces mixing X and jet degrees.

## Independent arithmetic replay

The new stdlib verifier does not import the restored note's checkers.
It checks:

* 320 ranks by direct modular elimination of expanded local columns.
* 3750 height-sort, diagonal-compression, and cell-marginal comparisons.
* 3128 one-sided finite column inequalities by exact rational polygon
  clipping and integration of the maximum of three affine functions.
* Both large finite certificates using closed integer column sums.

The finite enumeration is a check on the derivations, not a proof for
all multiplicities. The all-m proof is the chain above. Runtime was
about1.14seconds under the384MiB watchdog.

| Quantity | Rate9/10 | Rate3/4 |
|---|---:|---:|
| Multiplicity | 10000 | 100000 |
| Agreement | 47389/50000 | 43049/50000 |
| Jet monomials | 9724108 | 1830201539 |
| Exact local rank | 44523829596 | 73254792027652 |
| Positive surplus | 14639357/10 | 1757723551/4 |
| Maximum jet degree | 10530 | 114797 |
| Sufficient challenge degree | 320257184 | 19137094352 |

The last row independently verifies the conservative sufficient inequality
(ell+1)*benefit > rank*(ell+q_max+1). It is not a claim that this large
challenge degree is necessary. The agreements lie below the positive
root of (8-rho)a^2-6rho*a+rho(4rho-5), checked by exact rational signs.
These are strict mathematical improvements of the sufficient curve;
the enormous supports and conservative budgets establish no practical
better.codes improvement.

## How this answers the tightness question

At the quarter-rate first-order threshold, the specified support-counting
method really is optimal, even after allowing its stated nonmonomial
extension. That is the cleanest currently audited 'tight-ish' statement
about the coauthor paper's first-order result. It leaves the more important
intrinsic question open: could the actual code lists be constant and
line exceptions linear at fixed positive gap, despite the method's
linear-list and quadratic-line upper bounds?

The restored all-rate continuum theorem, including optimality of its
new high-rate cubic curve, is not included in this audit verdict.
The finite strict improvements above stand independently of that claim.

## Subsequent finite-length extension

UNIFORM_FINITE_LENGTH_CONVERSE.md removes the growing-multiplicity caveat
for the explicitly weighted, full-coefficient MONOMIAL model. Its exact
cutoff rank and half-rank lemma reduce any positive finite-length count
to the audited saturated comparison. The resulting necessary agreement
is (1-8/N)*(a_0+(1-2*a_0)/(8m))+8/N^2, uniformly in m. This does not
extend the finite-length result to all nonmonomial global spaces or to
certificates exploiting dependencies between coordinates.

## September 17: high-rate support shape audited over an interval

The restored high-rate shape theorem is now independently audited and
included in Section 8 of the 17-page technical note. For rho>1/2, the
optimal decreasing endpoint is min(a/rho,(2a-1-s)/(2rho-1)), with prefix
width optimized in [0,(a-rho)/(1-rho)]. The exact surplus adds
rho*(B-(a/rho-1))_+^3/(6*(2rho-1)) to the old cubic cap polynomial.
The proof completes/deletes columns according to the signs of three
affine densities; it does not rely on numerical optimization.

A simpler untrimmed-cap argument already proves a strict improvement
over the recovered DKT curve at every rate 8-3sqrt(6)<rho<1: its rank
truncation adds (B0-(a/rho-1))^3/12>0 at the old threshold. Continuity
and lattice approximation give finite certificates at a smaller agreement.
This is recovered mathematics newly audited, not a new discovery claim.
The explicit optimized-threshold cubic and its asymptotics have not yet
been included in this audit verdict.

Independent verifier passed 220 exact rational polygon integrals and
4851 endpoint comparisons, plus positive examples at both certified
rates. The note builds without warnings; new theorem/proof pages were
rendered and inspected. No practical parameter or better.codes gain is
claimed.

## September 17: explicit high-rate curve and renewed intrinsic priority

The restored explicit high-rate continuum threshold is now audited in
Theorem 8.3 of the 18-page technical note. Existence of an interior
optimizer forces a definite square-root sign and the largest cubic
root; the proof does not merely select a numerical branch. Three exact
symbolic identities and six rational branch isolations pass, with
agreement intervals narrower than 10^-28 and admissible support widths.
The note builds without warnings; new pages were visually checked.
This remains continuum method tightness, not intrinsic code tightness.

The user specifically asked about intrinsic or spiritually meaningful
tightness of https://eprint.iacr.org/2026/2056.pdf. Direct web retrieval
failed and HTTPS download returned403; no copy was recovered by the
filename lookup. Do not claim this current ePrint has been read. The
comparison remains the recovered September10 version7. Our large
gap-dependent coefficient in a linear-n lower bound rules out easy
uniform gap dependence, but neither forces the first-order quadratic
exception count nor an n exponent growing toward capacity. Method
optimality must not be presented as a substitute. Prioritize a growing
fixed-gap list or superlinear fixed-gap exception construction next.

## September 17: CURRENT EPRINT RETRIEVED; quantitative comparison corrected

The public145-page ePrint2026/2056 was successfully retrieved using the
normal download query after plain URL403. SHA256
b67c188ec477b6063caf9c1c06b214c71e358ff09b9517adcdb1db212ea2700a.
Read-only snapshot stays ignored under tmp/eprint-2056. Current source
comparison is EPRINT_2056_COMPARISON.md, superseding version7 for theorem
statements. Theorem1.1 has eta1^-2 lists and eta1^-4 MCA, not the older
eta1^-3/eta1^-5. Proposition5.10 has graded challenge counts, and the
capacity characteristic guard is p>k-1. Page47 already acknowledges the
high-rate curve refinement. Do not present our old-budget converse as
current-theorem tightness or the high-rate refinement as absent from
the current paper.

The note abstract and first-page notice, legacy cost statements, README,
and comparison documents now make this distinction explicit. Main paper
related work now cites the public ePrint and states the missing intrinsic
lower bounds against its correct powers. Whole145-page proof and Lean
formalization have not been independently audited here. The user's
intrinsic tightness target remains unresolved.
