# Prescribed KoalaBear NTT domain: finite discriminator calculation

September 18, 2026. **PASS.** This uses the prior quotient/discriminator
mechanism from KKH Appendix A, with an elementary overlap-sensitive
root count. It is not a new asymptotic construction.

The prescribed domain does admit a lower-threshold example: at
n=262144, J=131072 over E=F_(2130706433^6), a one-pole construction
on D=mu_262144 has **860778005594247069** distinct nonzero good labels,
exact source/common agreement **135167**, and exact near agreement
**139263**. The label count exceeds ceil(|E|/2^128), even after losing
one label in affine reparametrization. The agreement is **519 below**
the required 139782. No upper bound at that required threshold follows.

Files:

- `fixed_ntt_discriminator.tex`: input-ready proof.
- `verify_fixed_ntt_discriminator.py`: exact integer/rational check.
- `fixed_ntt_discriminator_verified.json`: passing receipt.

## Fixed domain and random pole, not random tags

Set p=2130706433, q=p^6. The exact count of full-degree-six elements is

    Q=q-p^3-p^2+p.

The proper subfields are Fp^2 and Fp^3, intersecting in Fp. For a fiber
size m, let s=n/m-1, r=J/m+1, w=m-1, and
G=mu_(s+1)\{1}. Thus the entire set of nonreserved tags is fixed.
Choose a pole b only among the Q full-degree elements. None is in the
base field, so denominators are nonzero on all evaluation points.

For two distinct r-subsets S,T of G, put u=|S\T|=|T\S|. Factoring
their common roots from V_S-V_T leaves a nonzero polynomial of degree
at most u-1. A full-degree b is not a root of a common linear factor.
All full-degree roots occur in Frobenius orbits of six. Therefore at
most c_u=6*floor((u-1)/6) eligible poles cause this collision.

With L=binom(s,r) and

    W=sum_{u>=1} binom(r,u)binom(s-r,u)c_u,

the average ordered collision energy is at most L+L W/Q. Some pole
has no larger energy. Cauchy--Schwarz then guarantees at least

    ceil(L Q/(Q+W))

distinct products V_S(b). If L W<Q, its off-diagonal collision energy
can be zero, and every one of the L labels is distinct. This argument
does not assume independent subset products or use character sums.

Without the Frobenius refinement, c_u=u-1 gives the exact weighted sum

    sum_{u>=1} binom(r,u)binom(s-r,u)(u-1)
      = L[r(s-r)/s-1]+1.

At m=1024 this weighted mean is about 62.74118; the full-degree
refinement lowers it to about 60.24111. Thus the elementary energy
calculation gives a positive fraction of all q labels at that modest
agreement threshold, although it does not give near-total coverage.

## Exact compiler ledger

Let Y=X^m and R be the monic locator of w points in Y^-1(1). Define

    f=R Y^(r-1),  g=R/(Y-b),
    h_S=R[(Y-b)Y^(r-1)+V_S(b)-V_S(Y)]/(Y-b).

The witness has degree at most w+(r-2)m=J-1 and residual
R V_S(Y)/(Y-b), so it has exactly w+rm=J+2m-1 agreements.
Clearing the denominator against any other degree-below-J witness
gives a monic polynomial of that degree, proving the matching upper
bound. The polynomial source has degree J+m-1; the direction's
cleared numerator has degree at most J+m-1. Simultaneous interpolation
on r-1 tags, together with the w core zeros, proves both exact source
agreements and exact common agreement J+m-1.

| m | s | r | Guaranteed distinct nonzero labels | Exact source/common | Exact near |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1024 | 255 | 129 | 1553276470857367347050498710657094691569048149670139791 | 132095 | 133119 |
| 2048 | 127 | 65 | 11607093851088224732906772708434593182 | 133119 | 135167 |
| 4096 | 63 | 33 | 860778005594247069 (all subsets distinct) | 135167 | 139263 |
| 8192 | 31 | 17 | 265182525 (all subsets distinct) | 139263 | 147455 |

The required count is L*=274980728111395088. The m=8192 row clears
the agreement threshold but fails this label count badly. For every
m>=8192, even omitting the reserved fiber leaves at most 32 tags and
at most binom(32,16)=601080390 subsets of any fixed cardinality.
Because admissible fibers are powers of two, m=4096 is the largest
one-pole fiber that could supply L* labels in this fixed-cardinality
full-fiber model. Its degree ledger caps near agreement at 139263.
This is a scoped obstruction, not a universal Reed--Solomon bound.

## Primary-source comparison and correction of scope

The cached primary source is
`/Users/jthaler/Dropbox/Documents-full-2026-09-16/Documents/stwo_audit_2026-09-15/sources/actual_list_literature/kkh2026_782.txt`,
Appendix A, lines 635--802; Proposition 4 starts around line 785.
Its Lemma 3 is an evaluation-image discriminator obtained from second
moments. The subsequent construction divides a root-subset list by
X^m-z^m. Proposition 4 states at least p/(2n) close labels over a
polynomial-size prime alphabet at an inverse-logarithmic margin.

The present finite rows are not literal substitutions into the formal
asymptotic prime-alphabet Proposition 4. They are direct applications
of the same general discriminator lemma and quotient identity over
the extension alphabet E, with explicit n,p, core padding, pole
exclusions, and an overlap-sensitive collision bound. The full-degree
pole avoids the prescribed base-field domain automatically. This
does not establish a new mechanism or literature-priority claim.

Earlier statements that the *selected-domain theorems themselves*
do not establish a prescribed-domain result remain accurate. A broad
claim that no prescribed-domain result is available at any of those
lower agreement thresholds is too strong: the prior mechanism already
supplies the rows above. What remains unproved is the required pair
of agreement 139782 and label count L* on that prescribed domain.
