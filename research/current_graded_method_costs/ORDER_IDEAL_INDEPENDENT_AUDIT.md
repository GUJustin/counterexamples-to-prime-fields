# Independent audit: order-ideal fourth-power bound and the Eq64 extension

## Verdict and precise scope

**PASS** for `ORDER_IDEAL_FOURTH_POWER.md`, with its stated characteristic and full-coefficient-prefix hypotheses. Its Eq63 and Eq64 conclusions apply to coordinatewise monomial order ideals. The Eq64 conclusion additionally extends to every monomial support downward in Y0 alone, by the direct weighted sorting argument below. This does not extend Eq63 to that larger class and does not prove the fourth-power bound for choosing the better of Eq63 and Eq64 on arbitrary downward-Y0 supports.

All bounds concern the current declared-degree reconstruction ledger. They are not lower bounds on actual lists, exceptional challenges, actual component degrees, or arbitrary interpolation methods.

The hypotheses retained throughout are n>=12 divisible by4, D=n/4-1, integer D+1<A<=n, full prefixes x+Du+(D-1)v<mA, characteristic zero or greater than every retained total jet degree, and 0<epsilon*<=1/2000 with the a*,a0,c0 definitions in the audited note. H is a nonnegative integer and the received curve is affine (degree one).

## Imported statements checked

- The cached primary `tmp/eprint-2056/paper.txt`, Proposition5.10, Eq64, is exactly
  sum_u (H+1-u)_+ G_u > n(H+1)R.
  The scalar local rank is not multiplied by a u-dependent weight.
- `research/first_order_support_audit/note/finite_length.tex` gives the exact degree-q prefix count and rank, and the half-rank inequality. For Lq=mA-(D-1)q<m, it gives Gq<=2Rq, so these final diagonals have nonpositive surplus. For Lq>=m the local rank is saturated.
- `research/first_order_support_audit/note/main.tex`, lemmas `lem:sorting` and `lem:lex`, state the needed saturated-rank rearrangements. Diagonal compression preserves diagonal cardinalities and leading benefit; height sorting preserves column-height multiplicities and lowers saturated rank.
- The finite positive-surplus converse gives m>c0/epsilon*, maximum Y0 exponent>m/4, and maximum Y1 exponent>m/4-1. It applies after the exact finite reduction, not by assuming that all original prefixes are saturated.

This audit checks how these already proved imports are used; it does not claim a new proof of every imported theorem.

## Mandatory triangle: original support, not only its rearrangement

After deleting the final unsaturated diagonals, a positive-surplus coordinatewise ideal S0 has positive leading surplus at a*. Let d be its first incomplete diagonal. The complement's upward shadow has cardinality at least one larger on the next diagonal, so selected diagonal lengths are nonincreasing from d onward. Before d the diagonal of degree q has q+1<=d monomials; afterward each has at most d.

Compress each diagonal to v=0,...,kq-1. The result is still an order ideal, has the same leading benefit, has no larger saturated rank, and has maximum v at most d-1. The positive-surplus converse forces that maximum to exceed m/4-1. Hence d>m/4. Every diagonal of the ORIGINAL S0 of degree at most m/4 was therefore complete. This is the logical reason the original source contains the low-degree triangle; preservation of a graded moment under compression is neither assumed nor needed.

The m bound and epsilon*<=1/2000 imply m>=16. Thus J=floor(m/8)>=m/16, and J lies inside that mandatory triangle.

## Eq63 and Eq64 arithmetic

For Eq63, every positive prefix satisfies the same finite converse. For every prefix, positive or not, finite reduction and the critical-support bound give Pj<=3 epsilon* m^3. The complete triangle gives Pj<=-m(j+1)(j+2)/8 for j<=J, hence negative prefix area exceeding m^4/12288. Summing prefixes gives exactly the stated H+1 and H bounds. No rank contribution from a deleted diagonal is silently reused as a saturated rank.

For Eq64, put h=H+1 and Delta=G/n-R. Its exact rearrangement is

h Delta > sum_u min(u,h) G_u/n.

Thus Delta>0. The source truncated to u<=H has positive surplus: its dimension times h bounds the left side of Eq64 from above, and its local rank is at most R. This truncation preserves the coordinatewise ideal, full prefixes, and characteristic guard. The finite converse therefore gives H>m/4. In particular min(u,h)=u throughout q<=J.

Each monomial there has at least nm/8 coefficients, as follows directly from A>=D+2 and q<=m/8. Therefore the loss is at least

(m/8) sum_{q=0}^J sum_{u=0}^q u
= m J(J+1)(J+2)/48
>= m^4/196608.

Together with Delta<=3 epsilon* m^3 this gives

H+1>m/(589824 epsilon*),
H>m/(1179648 epsilon*).

The second inequality uses H>=1 and H>=(H+1)/2. The declared reconstruction caps dominate the triangle, so the imported list and regular-family ledger lower bounds apply unchanged.

## New extension: Eq64 for every downward-Y0 support

Let the initial jet support be any finite union of columns

S={(u,v):0<=u<hv}.

Discard empty coefficient prefixes, which preserves downward-Y0 closure. Write wu=(h-u)_+, where h=H+1. The exact Eq64 margin is

M(S)=sum_{(u,v) in S} wu [mA-Du-(D-1)v] - n h R(S).

Assume M(S)>0.

### 1. Remove unsaturated final diagonals before sorting

Rank is additive in total jet degree. A diagonal with Lq<m contributes at most

h Gq - n h Rq <=0,

because 0<=wu<=h and the half-rank lemma gives Gq<=2Rq<=nRq. Hence deleting every such diagonal weakly increases the Eq64 margin. The surviving support remains downward in Y0 and lies inside a total-degree cutoff q<=Qcut on which Lq>=m. Its exact local rank is now the saturated rank.

This step is necessary: one cannot simply apply the saturated sorting lemma to arbitrary finite prefixes.

### 2. Sort the heights using the entire Eq64 source count

For a retained column of height t at derivative exponent v, its exact weighted source count is

Phi(t,v)=sum_{u=0}^{t-1} wu [mA-Du-(D-1)v]
        =alpha(t)-(D-1)v beta(t),

where

alpha(t)=sum_{u<t} wu(mA-Du),
beta(t)=sum_{u<t} wu.

The multiset of heights preserves sum alpha(hv). Since beta is nondecreasing, arranging the heights in decreasing order minimizes sum v beta(hv), by the elementary rearrangement inequality (or adjacent inversion swaps). D-1>0, so the ENTIRE Eq64 weighted source count weakly increases. The existing height-sorting lemma weakly decreases saturated rank. Therefore the Eq64 margin cannot decrease.

### 3. Sorting preserves saturation and the declared caps

If the original retained support lies in u+v<=Q, then for every u the number of columns with height at least u+1 is at most Q-u+1. After decreasing rearrangement these columns occupy the first such positions, so u+v<=Q still holds. Apply this to Qcut to preserve saturation, and to the original declared total-degree cap B to show the sorted cap is no larger. The new largest derivative exponent is the number of nonempty columns minus one, at most the original derivative cap b.

The sorted support is an order ideal in both coordinates. It has positive Eq64 margin at the same H, its full coefficient prefixes are valid, and all characteristic hypotheses remain valid because total degrees have not increased. The audited coordinatewise Eq64 theorem applies. Its m,H bounds transfer directly; its reconstruction cap lower bounds transfer because the original B,b dominate the sorted caps.

**Conclusion:** the same Eq64 fourth-power regular-family ledger necessity and second-power list ledger necessity hold for all downward-Y0 full-prefix monomial supports. No comparison of the separate loss moment is used.

## Why preserving the loss moment would be wrong

Take column heights (1,2) at v=0,1 and sort them to (2,1). For H>=1, the only positive-u monomial moves from (u,v)=(1,1) to (1,0). Its coefficient-prefix length increases by D-1, so the weighted loss sum min(u,H+1)G_u increases by D-1. It is not preserved and need not decrease.

This does not obstruct the extension: the full Eq64 source count increases by H(D-1), while saturated rank does not increase. The direct Phi comparison is the correct quantity. No analogous argument for the Eq63 graded row cost is asserted here.
