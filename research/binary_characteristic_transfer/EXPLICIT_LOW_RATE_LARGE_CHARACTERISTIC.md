# Explicit low-rate large-characteristic comparison

This is a quantitative corollary of the binary manuscript's existing fixed-characteristic locator compiler, combined with the explicit finite support formulas of DKT ePrint 2026/2056, Eqs. (60)--(64) and Lemma 5.6. It is not a new baseline construction or a fixed-rate tightness result.

Let p>=53 be prime. Take the full additive domain D=F_(p^5), and set

    N=p^5, K=p, message degree d=K-1=p-1.

The codimension-two compiler in GOLD_AND_NEAR_JOHNSON_LEDGER.md gives

    actual agreement A=p^3-1,
    common agreement C=p^2-1,
    M=[5 choose 2]_p=p^6+p^5+2p^4+2p^3+2p^2+p+1

distinct bad challenge labels in a proper extension of F_(p^5). The characteristic satisfies p>d. For simultaneous exact individual-source agreement C, use the degree-at-least-three extension and source shift described in that note. That shift also makes every label nonzero. The construction alone already has distinct labels in a quadratic extension; dropping a possible zero label would cost at most one and does not affect the comparison below.

## Below-Johnson advertised threshold

The actual agreement A is **above** the exact finite Johnson threshold:

    A²-Nd = p^5-2p^3+1>0.

To make a below-Johnson comparison, retain the same witnesses but advertise

    A0=p^3-p².

Then A0²<Nd, since (1-1/p)²<1-1/p. All M challenges still violate common agreement at A0. Their full agreement sets have size A, and C<A0.

The rate is rho=p^-4. DKT's low-rate curve satisfies

    a1(rho)<=p^-2/sqrt(2)+p^-3/(2^(3/4)sqrt(3)).

Consequently A0/N=p^-2(1-1/p)>a1(rho) for p>=53, and the ratio tends to sqrt(2). This is a fixed *fractional* position relative to the low-rate curve. Its absolute agreement gap is Theta(p^-2), and its rate tends to zero.

## A uniform finite first-order support

Use multiplicity m=4, derivative cap B_partial=2, and total jet cap

    B=4p².

Retain exactly the DKT derivative-weighted monomials

    X^x Y0^u Y1^v,
    0<=v<=2, u+v<=B,
    x+(p-1)u+(p-2)v<4A0.

Since 4A0=(p-1)B, their exact number is

    G=(p-1)(3B²-3B+2)/2+3B-2
     =24p^5-24p^4-6p^3+18p²+p-3.

The local rank bound of DKT Eq. (62) is R=23: the Taylor layers s=0,1,2,3 contribute respectively 3,6,8,6. All relevant specialization cutoffs hold. Only q<=5 contributes to local rank. The high total jet cap B need not be less than p: the interpolation proposition holds over every field, and reconstruction requires p>max(d,B_partial), which holds here.

For p>=53,

    G>(47/2)N>23N.

For example 24-24/p-6/p²>47/2, and the remaining terms in G are positive. Choose challenge degree

    H=48B=192p².

The graded row test follows even from the crude lower bound

    sum_q (H-q+1)G_q >= (H-B+1)G
       > (47B+1)(47/2)N
       > (48B+1)23N
       >= sum_q (H-q+1)N R_q.

Thus this is an explicit uniform interpolation certificate for affine received lines, with fixed derivative cap 2. No hidden O_rho constant or characteristic assumption p>B is being used.

At the larger actual threshold A one can instead take B=4(p²+p+1), giving G=24p^5+24p^4+18p^3-12p²-11p-9>24N and H=24B. The below-Johnson version above is the stronger comparison of regimes.

## Explicit reconstruction/counting upper comparison

Use the below-Johnson support, and let lambda=(N-d)/(A0-d). DKT Lemma 5.6 applies because p>max(d,2). Its parameters satisfy

    lambda<2p²,
    tau<=2p,
    u<=8p³, v<=3p,
    F_reg<=28p³,
    S=3B-4<12p²,
    H_s=3H=576p²,
    J_1<=30776p^6.

Here J_1=H(2uv-v²)+2(1+tau H)F_reg. These inequalities are direct substitutions into Eq. (54). In particular the fixed-word list bound is at most

    lambda F_reg+S <=68p^5=68N.

For the MCA formula (55), choose both incidence thresholds L=L0=floor(A0/2). Then

    (N-L+1)/(A0-L+1)<=3p²,
    (N-d)/(L-d)<=4p².

Using Psi_d(S)<=1+4dS, the ordinary tail from Eq. (38) is at most

    82956p^7+15588p^4.

The two regular terms are at most 184656p^10 and 112p^10. Therefore the full-agreement-set MCA exceptional budget is, conservatively,

    E <=300000 p^10 =300000 N².

This is a uniform explicit bound along the vanishing-rate sequence. The construction supplies at least M>N^(6/5) bad challenges under the same characteristic guard. The gap between exponents 6/5 and 2 remains substantial. The result excludes a universal linear-in-N MCA bound along this varying-rate, shrinking-gap sequence with a uniform constant; it does not exclude a bound O_rho,eta(N), nor establish fixed-rate first-order tightness.

## Ordinary-list caution

M counts different words on a received line, not a single ordinary list. The separate proof `EXACT_SINGLETON_LIST_CLASSIFICATION.md` shows more: at the actual threshold A, these are exactly all qualifying labels, and each has a singleton nearest list. The stronger coefficient-elimination proof in `SINGLETON_BELOW_JOHNSON_INDEPENDENT_AUDIT.md` now extends exact classification and singleton lists to every threshold strictly above p², including A0.

At the actual threshold A, elementary Johnson counting gives the explicit per-word cap

    L_word <= N(A-d)/(A²-Nd)
           = p^5(p³-p)/(p^5-2p³+1)
           =Theta(p³).

Hence the bad-label count M=Theta(p^6) is on the scale of the *square of this upper cap*. The actual nearest lists at these words are singletons, so this upper-cap comparison does not identify an attained list-size mechanism. It also says nothing about the maximum list size over all words of the code, and the exact singleton lists at A0 do not bound lists of arbitrary received words.
