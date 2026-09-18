# Independent audit: full shared-pole bank double-zero budget

Verdict: PASS. Reviewed `SHARED_POLE_DOUBLE_ZERO_BUDGET_2026_09_18.md` together with the defining rational formula and distinctness certificate in `SHARED_POLE_PALEY_TRANSLATION_TARGET.md`. No manuscript edits or finite-field scans.

## Exact pole buckets

Identify H with F_{ell²}, whose quadratic character is chi, and fix nonzero T. Scaling S=Tz reduces the coefficient sum to chi(T)(chi(1−z)+chi(1+z)). Since ell²=1 mod8, chi(−1)=1. Excluding z=±1, the standard elementary character sums give the ordered (++),(--),mixed counts (M−5)/4,(M−1)/4,(M−1)/2. Under z→−z, the ++ class contains the fixed point z=0 and the other classes do not. Quotienting by sign therefore gives h=(M−1)/8 for each nonzero ±2 bucket and r=(M−1)/4 for the zero bucket. The two excluded points form one sign orbit and have coefficient chi(T), a singleton. Multiplication by chi(T) merely swaps the ±2 buckets. These four coefficient values are distinct in characteristic zero or p>5. The counts sum to L=(M+1)/2.

At t_T, the numerator of R_t has value 4(t_T³+A t_T+B)=4y(T)², nonzero because nonzero odd-ell torsion is not 2-torsion. Thus the cleared value of Q_S is a nonzero common scalar times this coefficient sum. Equal values really do imply equality of the entire coefficient of R_t. Cancellation removes both pole orders, and multiplication by the double-zero denominator contributes at least order two to the difference. All other summands are regular there. This is stronger than pointwise root counting and remains valid whether the pole is selected as an evaluation coordinate.

The target's augmentation-zero convolution argument proves the polynomials distinct under p!=ell and p!=2. Consequently each nonzero pair difference has degree at most M; none invalidates the root budget by vanishing identically.

## Aggregate budget and optimization

The exact equal-pair count is

 E_pole=r(r−1)/2+h(h−1)=(M−1)(3M−19)/64.

Subtracting all forced double zeros at P=(M−1)/2 poles from M*binom(L,2) yields

 B=(5M³+25M²−49M+19)/64.

If q poles are selected, their incidence contribution is at most qr, and offpole incidences S satisfy S²<=(4M−q)(S+2B) by pair counting and Cauchy. The displayed function f(m) is the positive root of this inequality.

The monotonicity argument is correct: direct differentiation gives f'(m)<=1+sqrt(B/(2m)). For M>=25, B<M³/8, m>=(7M+1)/2, hence f'(m)<1+M/sqrt(56)<1+M/7<r. Therefore qr+f(4M−q) increases with q and is maximized at q=P. No assumption about which poles occur or about rational elliptic points in the domain is required.

The resulting leading minimum-agreement bound is (1+sqrt(35))M/4+O(1), i.e. fraction (1+sqrt(35))/16+o(1) on 4M points. Both constants are correct.

## Finite first-order exclusion

Independently checked all displayed polynomial identities with exact Fraction arithmetic. The degree-four identity was checked at five distinct rational M-values, and the translated coefficients were separately computed by binomial expansion. Results:

 256(S0²−mS0−2mB)=29M⁴−954M³+413M²−452M−56;
 coefficients after M=u+49, ascending:
 [55911492,6815644,277949,4730,29].

Thus the margin is positive for every M>=49. S0 is positive and beyond m/2 in this range, so positive quadratic residual indeed contradicts the necessary offpole-incidence inequality; there is no wrong-root issue.

For a=15/32, the high-branch polynomial is −1/4096 at rho=1/4. Its rho-derivative is 8rho−a²−6a−5, negative throughout [1/4,.26] (at .26 it is −152377/25600). Its a-derivative is positive at a=15/32 throughout that interval. Thus the relevant positive first-order root exceeds 15/32 for every stated rate.

At M=25 the claimed values B=1446 and residual 1632 check exactly. At rho=.26,a=.47 the polynomial is −26517/500000<0, so the integer first-order threshold is indeed at least 48. The remaining prime-square cases start at M=49.

## Scope

The conclusion excludes the FULL specified Paley coefficient bank from simultaneous first-order agreement at n=4M,k=M+1, over the stated characteristics and any affine evaluation domain/word. It does not exclude subbanks with different bucket statistics, other coefficient arrays, other lengths/rates, or elliptic constructions in general. The common-remainder consequence is justified within precisely this full-bank scope. No correction to the proof is needed.
