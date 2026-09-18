# Norm-one reciprocal bank: direct list audit

September 18, 2026. **PASS.** The reciprocal identity is already in `FP3_NORM_WORD_RICH_WITNESSES.md`. The norm-one restriction, doubled domain, and exact matched Johnson-list statement below were not found in the targeted local-note search. No literature-priority claim is made: the incidence design is the classical projective-plane/Singer type.

## Exact construction and splitting proof

Let p be odd, E=F_(p^3), L=p^2+p+1, G=ker Norm_(E/Fp), and D={x in E*: x^2 in G}. Since L is odd and divides (p^3-1)/2, every member of G is a square in E. Thus D is the cyclic subgroup of order N=2L.

Take the received word f(x)=x^(2p+2). For each a in E with Norm(a)=-1 define the degree-two polynomial

    Q_a(X)=a X^2-a^(p^2+1).

There are L such parameters and their leading coefficients distinguish the polynomials. Put y=a^(p^2)z. The matching equation y^(p+1)=ay-a^(p^2+1) becomes

    z^(p+1)-z+1=0, equivalently z^p=1-1/z.

No root is zero or one. The map R(z)=1-1/z has third iterate the identity, and its coefficients lie in Fp. Hence all roots satisfy z^(p^3)=z. The polynomial is squarefree: a common zero with its derivative z^p-1 would have z^p=1, leaving residual 1. It therefore has exactly p+1 distinct roots in E. Moreover z^(p^2)=1/(1-z), giving Norm(z)=-1. Consequently Norm(y)=Norm(a)Norm(z)=1. All p+1 y-roots lie in G and each lifts to two x-roots in D. Every Q_a has exactly A=2p+2 matches.

## Complete list and exact Johnson saturation

This is stronger than only an at-least-L list. For every quadratic Q, f-Q has degree A, so its agreement on D is at most A. Thus every member of the threshold-A list has exactly A matches. If its size is m, let r_x count its witnesses matching at x. Distinct quadratics agree at at most two coordinates. Hence

    sum_x r_x=mA,
    sum_x r_x^2 <= mA+2m(m-1).

Cauchy gives m^2 A^2/N <= mA+2m(m-1), and therefore

    m <= N(A-2)/(A^2-2N).

Here A^2-2N=4p, so the right side is exactly L=N/2. The displayed bank has that size; it is the complete nearest list, the maximum agreement is A, and the standard pairwise-intersection Johnson count is attained exactly. Equality also proves each coordinate belongs to p+1 supports and each pair of witnesses shares exactly two coordinates. On G before square pullback, this is the projective-plane incidence parameter set (L,p+1,1).

The actual threshold A lies ABOVE the exact Johnson agreement sqrt(2N), not below it. This exact Johnson saturation alone should not be advertised as new first-order DKT tightness.

## Below-Johnson advertised threshold and finite support

For p>=4099 set T=2p-ceil(4sqrt(p))-4. The same list of L witnesses persists at threshold T. The subsequent independent review proves completeness there as well: every outsider has at most p+1 matches; see `NORM_ONE_DIRECT_LIST_INDEPENDENT_REVIEW.md`. The actual nearest agreement remains A.

We have T<2p<sqrt(2N). Also the standard first-order curve estimate gives

    N a_1(3/N) <= sqrt(3N/2)+(3N/8)^(1/4)
                   < (7/4)p+sqrt(p) < T.

For the last inequality use T>=2p-5sqrt(p), valid at this onset, and sqrt(p)>24. The preceding bounds follow directly from N=2(p^2+p+1) at p>=4099.

The existing finite primary support m=6, derivative cap 3, B=3T, H=40B has G=4B^2-2B columns per leading challenge scale and local rank R=62. Here

    29p/5 <= B <= 6p,
    39G-40NR >= (7196/25)p^2-5428p-4960 > 0.

Since this also implies G>NR, the full surplus

    B(39G-40NR)+(G-NR)

is positive. These are the same finite-support formulas independently audited for the nearby Fp3 line construction, with the larger present N substituted explicitly. Characteristic p>3 satisfies the derivative guard; p need not exceed B or H.

## Honest scope and comparison

The code has K=3, rate 3/N tending to zero, characteristic p=Theta(sqrt(N)), ambient size p^3=Theta(N^(3/2)), and a complete actual nearest list of size N/2. At the lower advertised threshold T it gives a linear-in-N list above the first-order agreement curve and below Johnson. The ratio T/sqrt(3N/2) tends to 2/sqrt(3), but all normalized agreements and their absolute normalized separation tend to zero. This is not a fixed-rate/fixed-normalized-margin lower bound, and primary interpolation feasibility alone does not match a list upper bound. The explicit counting transfer below supplies the additional uniform bound and establishes a matched constant-factor comparison.

The projective/Frobenius line results concern many exceptional labels, mostly singleton lists; this construction concerns a single word with a genuinely large list. It supplies a useful contrasting list-size example but no far-source line statement. Its entire witness bank is two-dimensional, so the independently proved fixed-witness-span gate continues to block its preserved-span translation to the frozen high-rate benchmark. The audited statement is now integrated in `norm_one_direct_list.tex`; it has no protocol-level consequence established here.

## Follow-up: matched finite DKT list upper bound (independently verified)

The local primary text `tmp/eprint-2056/paper.txt`, Lemma 5.6 Eq. (56), and especially the explicit uniform fixed-word statement of Lemma 5.11, justify the additional counting step. It is not an assumption that a symbolic interpolant remains useful on an arbitrary special fiber: Proposition 5.10 supplies a nonzero fixed-word equation for each received word, and the fixed-word counting argument is applied separately. Alternatively one can use the already certified constant received curve; Proposition 5.10 guarantees nonzero specialization. The ordinary dimension surplus G>62N is already enough for each fixed word. No source/common-agreement hypothesis is needed.

Use D=2, B=3T, M=3. Equation (54) gives tau=1, u=B, v=4, F_reg=7B-12, and S=5B-9. With lambda=(N-2)/(T-2), Eq. (56) therefore bounds EVERY received word's quadratic list at threshold T by

    floor[lambda(21T-12)+15T-9]
      = floor[21N+30lambda+15T-51].

The hypotheses are precisely the support surplus already proved, K=3, and characteristic p>max(2,3). They hold for every evaluation domain of this size over E and every received word, not merely for the norm word or a particular received line.

For p>=4099, T-2>=p+1, so lambda<=2p. Also T<=2p. Thus the upper bound is at most

    21N+90p-51 <= 22N,

where the last inequality is N-90p+51=2p^2-88p+53>=0. Together with the explicit N/2-member list on the same code/domain and at the SAME advertised threshold T, this proves

    N/2 <= maximum list size at T <= 22N.

Consequently this is a genuine matched-parameter constant-factor (at most 44) comparison with the present finite DKT list certificate. It remains a varying-rate extension-field statement, not fixed-rate/fixed-normalized-gap tightness, not MCA-count tightness, and not a prime-alphabet result. The subsequent independent review sharpens this to exact completeness N/2 at every integer threshold p+1<T'<=2p+2, including T. The upper bound is codewide, which is stronger than an along-one-line list bound.
