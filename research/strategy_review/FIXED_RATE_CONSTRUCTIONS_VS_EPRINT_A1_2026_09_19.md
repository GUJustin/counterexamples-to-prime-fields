# Exact comparison of the fixed-rate constructions with the ePrint curve

2026-09-19. No existing fixed-rate family in the paper has been shown to
cross the agreement threshold of ePrint 2026/2056. Parameter optimization
within the proved nearest-orbit padding compiler cannot do so. This note
also identifies an exact shortening target that would cross, and explains
why that shortening has not been constructed. Arbitrary operations on an
unspecified nearest orbit must not be declared impossible by borrowing a
theorem about the different, explicit Dickson candidate bank.

## 1. The curve actually stated in the paper

Read Eq. (31), printed page 35, of the September 17 archived public PDF
`tmp/eprint-2056/paper.pdf`, SHA256
`b67c188ec477b6063caf9c1c06b214c71e358ff09b9517adcdb1db212ea2700a`.
The source is https://eprint.iacr.org/2026/2056.pdf?download=1.
This comparison uses that archived statement, not a claim about a later
uninspected revision or a separately optimized interpolation curve.

Let rho be message dimension divided by length, and put
rho_c=11−3sqrt(13). The theorem requires agreement a>a1(rho), where

    a1(rho)=sqrt(rho/2)*(1+u),  u²(u+3)=sqrt(rho/2), u>0,
        if rho<rho_c;
    a1(rho)=[3rho+2sqrt(rho(5−rho)(2−rho))]/(8−rho),
        if rho>=rho_c.

For the second branch a1 is the unique positive root of

    F_rho(a)=(8−rho)a²−6rho*a+rho(4rho−5).

The first branch cannot simply be replaced by this quadratic. A useful
exact lower bound on the first branch is a1(rho)>2rho. To see this, put
t=sqrt(rho/2). Then t<t_c=(sqrt(13)−3)/2<1/3. Since
t²(t+3)<=t, the positive solution u satisfies u>=t. Thus
a1=t(1+u)>=t(1+t)>4t²=2rho.

## 2. Current fixed parameter points

Here a is the agreement threshold, not the excess above capacity.
Decimals are explanatory; the inequalities below are algebraic.

| Construction | rho | a | a1(rho) | a−a1(rho) |
|---|---:|---:|---:|---:|
| Prime-field explicit n/2 list | 1/4 | 3/8 | 0.468792342 | −0.093792342 |
| Quadratic-extension exact-gap ordinary CA | 1/8 | 3/16 | 0.319059326 | −0.131559326 |
| Parameter family b=2,d=9 | 2/9 | 1/3 | 0.438994990 | −0.105661657 |
| Parameter family b=3,d=10 | 3/10 | 2/5 | 0.519019426 | −0.119019426 |
| Parameter family b=4,d=11 | 4/11 | 5/11 | 0.577873616 | −0.123328162 |
| Parameter family b=5,d=12 | 5/12 | 1/2 | 0.623442638 | −0.123442638 |
| Older rate-3/13 ordinary-CA family | 3/13 | at most 5/13+o(1) | 0.448326287 | at most −0.063710902+o(1) |

The last upper bound uses m<=5r/3 for the descended true-nearest source;
it is stronger than merely observing that this family's agreement is
not guaranteed to cross the curve. Its at-most-two anchors contribute
the indicated vanishing error.

These constructions prove that length-independent capacity list bounds,
and subquadratic ordinary-CA bounds at some fixed capacity parameters,
are impossible in their respective field classes. They do not witness
necessity of the first-order list/MCA length exponents at the agreements
where the first-order theorem applies.

## 3. All published b,d choices fail, analytically

The exact normalized parameter family has

    rho=b/d, a=(b+1)/d=(1+1/b)rho,
    b in {2,3,4,5}, d>=b+7.

In fact the following comparison holds for every real b>=2 and d>=b+7,
independently of whether the construction and characteristic guard extend
that far. On the low branch, a<=3rho/2<2rho<a1(rho).
On the upper branch write q=1+1/b. Then

    F_rho(q*rho)/rho = −q²rho²+(8q²−6q+4)rho−5.

This is strictly increasing for 0<=rho<=1: its derivative is at least
6q²−6q+4>0. Since rho<=b/(b+7), its maximum is

    −4(5b²+42b−14)/(b(b+7)²)<0.

Therefore a<a1(rho) for every permitted parameter choice. There is no
hidden successful d or b in the current normalization. Letting d grow
only sends the rate and absolute capacity gap toward zero; it does not
create a positive first-order margin.

## 4. Optimize the entire proved padding compiler, not just b,d

The true-nearest source used by ordinary CA has

    length 4r, dimension r, maximum m<=5r/3.

The upper bound follows by lifting to the original Dickson word and using
`quadratic_indicator_nearest/NEAR_RIGIDITY.md`; it is not an assumption
that the unspecified nearest polynomials belong to the explicit binomial
bank. Add s common-zero coordinates, any number t of coordinates without
inherited matches, and the existing bounded number of anchors. The final
nearby label gains one fresh match in the compiler. Up to O(1) changes,

    n=4r+s+t, K=r+s, T<=5r/3+s.

Optimizing over all s,t>=0 gives the limiting envelope

    a <= E(rho):=min(5rho/3,(2+7rho)/9).

Both linear inequalities are exact for the displayed continuous resource
model: no-match padding maximizes the first branch at rho<=1/4, while
common-zero padding maximizes the second at rho>=1/4. Arbitrary ordering
of these operations cannot help. A bounded number of anchors and the
compiler's one new agreement change the normalized bounds by o(1).
Inherited-match polynomial pullbacks likewise cannot improve the limiting
envelope when degree rather than dimension is tracked first.

This envelope lies strictly below the actual Eq. (31) curve at every
0<rho<1. Below rho_c use E<=5rho/3<2rho<a1. For
rho_c<=rho<=1/4,

    F_rho(5rho/3)=−rho(25rho²−146rho+45)/9<0.

The parenthesis decreases on this interval and is still positive at 1/4.
For 1/4<=rho<1,

    F_rho((2+7rho)/9)
       =−(rho−1)(49rho²−261rho+32)/81<0.

The quadratic parenthesis is already negative at 1/4 and keeps decreasing.
Thus no choice of the existing zero/no-match padding parameters reaches
a1(rho)+eta with eta a fixed positive constant. This includes choices
beyond the displayed exact-rate family. New simultaneous coincidences,
or a qualitatively different shortening/puncturing theorem, are required.

## 5. What puncturing and shortening are actually ruled out

For the EXPLICIT prime-field Dickson bank, the existing Fourier estimates
in `binomial_first_order_search/PUNCTURING_LIMIT.md` apply to arbitrary
retained original coordinates, received values, and growing candidate
subsets. The independently audited ancestry argument in
`dickson_fixed_gap/TRANSFORMATION_ENVELOPE_INDEPENDENT_AUDIT.md` extends
its stronger envelope min(3rho/2,(1+5rho)/6)+o(1) to inherited-match
pullback/common-zero/no-match transformations with later puncturing.
That envelope is below a1 too.

Ordinary shortening of a growing subbank on common agreement anchors
cannot make a macroscopic improvement to this explicit bank either.
Choose an orbit containing at least half the retained candidates. Its
uniform average bound on any t-coordinate subset is

    average agreement <= min(t/2,t/4+k/2)+epsilon_L*k,
    epsilon_L -> 0 as retained orbit size L -> infinity.

If every candidate agrees at all t anchor coordinates, then
`t<=t/2+epsilon_L*k`, hence t<=2epsilon_L*k=o(k). The estimate applies
also to t<=k, as explained in the ancestry audit. Dividing the common
anchor locator therefore changes degree and agreement by only o(k),
not the fixed fractions needed to bridge the threshold. Removing common
zeros that were artificially inserted merely undoes those insertions.

The unspecified TRUE nearest orbit used by the ordinary-CA construction
is different. Its full-domain maximum is controlled by m<=5r/3, but no
inspected theorem gives the explicit bank's uniform Fourier estimate for
arbitrary puncturings or common-anchor subbanks of this orbit. Therefore
an assertion that *all* arbitrary shortening or puncturing of that orbit
has been excluded would overstate the present results.

## 6. An exact shortening target, and why it is not a result

Suppose, hypothetically, a growing subbank of the true-nearest source
could be retained after shortening on 4r/5 COMMON agreement coordinates.
From m>=3r/2 it would have asymptotic parameters

    rho=1/16, a>=7/32.

These do cross the actual first-order curve. At rho=1/16, put
t=sqrt(2)/8 and u0=(7sqrt(2)/8)−1. Then

    u0²(u0+3)−t = 2−361sqrt(2)/256 > 0,

because 512²>2*361². Hence 7/32>a1(1/16), with numerical margin
approximately 0.000641864. This is a precise conditional parameter match,
not a constructed list or line.

The published anchor argument cannot supply it. Its guaranteed surviving
list is obtained by averaging one anchor at a time. Starting with r
candidates and agreement fraction at most 5/12, the resulting numerical
guarantee is at most r*(5/12)^t after t original-source anchors; this
falls below one long before t is proportional to r. That upper bound is
on the averaging GUARANTEE, not on the actual size of a specially chosen
common-anchor subbank. Only one or two anchors are currently used.
For the explicit Dickson bank the preceding Fourier argument actually
rules out such a common-anchor subbank. For the unspecified nearest orbit,
its existence remains an additional mathematical problem.
A subsequent exact orbit lemma rules out retaining a complete subgroup
coset of linear size along the actual prime-selection sequence: such a
subbank has at most r/2 common anchors. Arbitrary dense non-subgroup
retention remains open. See
`../ordinary_ca_superlinear/SUBGROUP_COSET_COMMON_ANCHOR_OBSTRUCTION_2026_09_19.md`.

Preserving only a bounded candidate set would not establish length-exponent
tightness. For the ordinary-CA compiler to retain its quadratic label count
at a fixed rate, it needs a linear-size retained bank and linearly many
usable padding coordinates, with the true-nearest boundary preserved.
None of these missing shortening properties is established by the
conditional pair (rho,a) above.

## Conclusion for the user's tightness question

The existing fixed-rate results give genuine capacity lower bounds, but
are quantitatively below the first-order theorem's agreement threshold.
All proved parameter choices and the explicit bank's inherited-match
transformations fail to cross it. The exact unresolved escape is a new
large-subbank shortening/puncturing structure (or new coincidences), not
another choice of constants in the published compiler. No better.codes
improvement or fixed-rate first-order tightness claim follows here.

Verification: independently recomputed the archived PDF SHA256; it matches
the value above. Symbolic expansion verifies both envelope factorizations,
the general b,d endpoint identity, and the exact square-root shortening
comparison. The sign and optimization arguments are given explicitly;
the decimal table is not used as proof. No paper source was edited.
