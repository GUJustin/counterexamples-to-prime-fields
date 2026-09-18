# Independent audit: the p^5 low-rate comparison

September 18, 2026. **PASS**, with the scope below. This independently checks `EXPLICIT_LOW_RATE_LARGE_CHARACTERISTIC.md` and the codimension-two specialization in `GOLD_AND_NEAR_JOHNSON_LEDGER.md`. No binary-repository edits or new construction priority claims.

## Exact construction and fields

Let p≥53 be prime, B=F_(p^5), and D=B. Every codimension-two F_p-subspace W has locator

    L_W=X^(p³)+a X^(p²)+c X^p+vX,  v≠0.

Choose 1,theta,s linearly independent over B in F_(p^15). Set

    g=X^(p²-1),
    f=X^(p⁴-1)+theta X^(p³-1),
    z_W=c^p-a^(p+1)+theta a,
    H_W=-((theta-a^p)(cX^p+vX)+(vX)^p)/X.

All H_W have degree at most p-1, and direct expansion in characteristic p gives

    f+z_W g-H_W=L_W(L_W^(p-1)+theta-a^p)/X.

On B the second factor is nonzero because theta is outside B. At zero the cancelled expression has value v(theta-a^p)≠0. Thus the agreement set is exactly W minus zero, of size A=p³-1.

If two labels coincide, independence of 1,theta recovers a and then c (Frobenius is injective). Their locator difference has degree at most one and vanishes on W intersect W', which has dimension at least one and hence at least p points. It is zero. Consequently the number of distinct labels is exactly

    M=[5 choose 2]_p=p^6+p^5+2p^4+2p^3+2p²+p+1.

For any two-dimensional F_p-subspace U, reduction of each additive head modulo L_U leaves a polynomial of degree at most p with zero constant term. Dividing these remainders by X gives degree-at-most-p-1 simultaneous witnesses on U minus zero. Hence CA≥p²-1. The degree of g minus any strict witness gives the opposite inequality. Therefore CA=agr(g)=p²-1.

Replace f by f+s g and z_W by z_W-s. Every shifted label is nonzero. Projection onto the s-coordinate bounds agreement of the shifted f by the agreement of g, so **both individual agreements and CA are exactly p²-1**. These statements use degree-at-least-three extension over B; a quadratic extension only gives the unshifted construction and label injectivity without this exact two-far conclusion. The concrete ambient choice is F_(p^15), not F_p.

## Threshold comparison

The code dimension is K=p, message degree d=p-1, length N=p^5. Advertise A0=p³-p². Then

    CA=p²-1 < A0 < A,
    A0²=N d (1-1/p) < N d,
    A²-Nd=p^5-2p³+1>0.

Thus A0 is genuinely below the exact finite Johnson threshold, while the actual witnesses have above-Johnson agreement. Their agreement sets cannot have common source witnesses, since their size exceeds CA. They are bad for ordinary correlated agreement as well as for full-agreement-set recovery at A0.

The primary DKT low-rate formula gives

    a1(p^-4) ≤ p^-2/sqrt(2)+p^-3/(2^(3/4)sqrt(3)).

For p≥53 this is less than p^-2(1-1/p)=A0/N. For a simple rational comparison, bound the two constants by 3/4 and 1; then 3/4+1/p<1-1/p for p>8. The rate p^-4 and the absolute first-order margin both vanish. The limiting ratio (A0/N)/a1 is sqrt(2), not a fixed absolute gap.

## Direct primary-source interface check

Read the cached primary ePrint `tmp/eprint-2056/paper.txt`, Eqs. (60)--(64), Proposition 5.10, Lemma 5.6/Eqs. (54)--(56), and Eq. (38). Proposition 5.10 explicitly holds over every field. Lemma 5.6 requires p>max(d,M), where M is the derivative cap, **not the total jet cap**. The proposed d=p-1, M=2 satisfy this. There is no illicit p>4p² assumption.

With m=4, B=4p² and H=48B, source coefficients are exactly

    G=sum_(q=0)^B sum_(v=0)^min(q,2) ((p-1)(B-q)+v)
     =(p-1)(3B²-3B+2)/2+3B-2
     =24p^5-24p^4-6p³+18p²+p-3.

The local-rank layers s=0,1,2,3 are 3,6,8,6, hence R=23. Only q≤5 can contribute, and their specialization cutoff is satisfied. For all p≥53, G>(47/2)N. The graded source count is at least (H-B+1)G, while the row count is at most (H+1)23N. Their strict inequality follows from

    (47B+1)(47/2) > (48B+1)23.

This is an explicit finite interpolation certificate, uniformly in p along this sequence.

## Reconstruction ledger checked independently

Using the exact primary formulas and L=L0=floor(A0/2), the claimed bounds hold:

    lambda<2p²; tau≤2p; u≤8p³; v≤3p;
    Freg≤28p³; S<12p²; Hs=576p²; J1≤30776p^6;
    (N-L+1)/(A0-L+1)≤3p²; (N-d)/(L-d)≤4p².

The ordinary term from Eq. (38) is bounded by 82956p^7+15588p^4. The two regular terms are at most 184656p^10 and 112p^10. Their sum is below 300000p^10=300000N². The fixed-word list upper bound is at most 68N.

The adjacent independent script `verify_low_rate_independent.py` rebuilds source/rank sums and the graded row inequality, then evaluates the **exact rational** primary counting budget at p=53,59,101,211. All four pass. Its JSON stores exact budgets and margins. These samples corroborate the algebraic inequalities above; they are not the proof of uniformity.

## Precise consequence and limitations

This supplies M>N^(6/5) distinct bad challenges with both sources far, at a below-Johnson advertised threshold above the first-order curve, in characteristic p>d. The explicit uniform DKT upper budget is O(N²) on these same parameters. Therefore the example refutes a uniform constant-times-N exceptional-count assertion **along this varying-rate, shrinking-gap sequence**. It does not refute O_(rho,eta)(N), where its constant may depend on the varying parameters, and does not match quadratic dependence or resolve fixed-rate first-order tightness.

M counts bad labels on a received line, not the size of an ordinary list. The actual per-word Johnson cap is Theta(p³); its square being on the scale of M does not show that this cap is attained. A prime ambient field cannot contain this five-dimensional F_p-domain. The result is a useful explicit extraction from an existing compiler, not a new prime-field family.
