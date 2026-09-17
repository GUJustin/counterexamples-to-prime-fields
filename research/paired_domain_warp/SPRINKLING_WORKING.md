# Product-image completion by adding pairs of alternatives

Development notes, September 17, 2026. The proof is now integrated in
`completion.tex`; see `COMPLETION_PROOF_AUDIT.md` and the independent
finite recurrence certificates. Provisional parameter suggestions below
are retained as development history, not as additional theorem claims.

Fix r padding sign-orbits ±x_j, e.g x_j=j. First choose a random base
core of m0 sign-orbits, and allD0-subsets. Let S0⊂G=(Fp*)^r be their
product-vector image H_I(x_j), with V=(p-1)^r. The existing energy proof
works for this FIXED block, and gives mean excessDelta<=
 delta0=p^r/binom(m0,D0)+((4r+2)^(2r+2)+2m0²)/(p-2m0²).
Hence some base core has missing density h0<=delta0, and Markov gives
high-probability small missing density when delta0 is small.

Now add t pairs of NEW core sign-orbits (a_l,b_l). A candidate selects
exactly one orbit from each pair, so total support size D=D0+t stays
fixed. Its product-vector image evolves by
 S_(l+1)=S_l*v(a_l) UNION S_l*v(b_l),
where v(a)=(x_j²-a²)_j. Missing set B evolves as the intersection of
two multiplicative translates.

At each stage choose a,b independently outside0,±padding and±allprior
core, then condition a≠±b. If p>(n+1)², where final
n=2(m0+2t+r) (plusoptionalzero), the deleted set has size<=n+1<sqrtp.
The same BGKS character sum gives Fourier coefficient bound
 lambda<=C/sqrtp, C=4r+2, uniformly over all previous choices.
For any fixed missing set of densityh, Fourier+Parseval gives
 E[h_new beforeconditioning] <= h²+(C²/p)*h.
This follows since the ratio distribution v(a)/v(b) has nonnegative
Fourier coefficients |hatmu|². Conditioning a≠±b costs at most
1/(1-4/p), because the available set has size>=p/2.
Therefore some new pair attains
 h_new <= (h²+(C²/p)*h)/(1-4/p).
Repeatedly apply this EXISTENCE recurrence. If V*h_t<1, the image is
ALL of G. Dyadic upper bounds avoid exponentially growing fractions:
if h<=2^-a, next <=[p+C²*2^a]/[(p-4)*2^(2a)].
Choose the largest integerk with numerator*2^k<=denominator.

All candidates have roots on exactly D core orbits. Put w=H_reference,
P=w-H_candidate, K=2D-1. With allG covered, for ANY padding value
vector z∈Fp^r, choose a candidate matching every nonzero z_j (extend
zero components arbitrarily to a nonzero target vector). It agrees on
K+1 core coordinates and2*wt(z) padding coordinates. Lipschitz distance
from w gives the matching lower bound, since w's distance is n-K-1.
Thus the exact distance profile on the r-dimensional affine space is
 dist(f+sum_j z_j e_j,C)=(n-K-1-2 wt(z))/n,
where e_j is1 on its padding pair and0 elsewhere. Parity/X-factor
adjustments preserve this formula, with e_j values x,-x in the odd case.
In particular g=sum e_j has support EXACTLY2r; all nonzero scalar line
points have EXACT distance theta=1-rho-(2r+1)/n, while zero has
exactdistance1-rho-1/n. No correlated agreement atthresholdK+2r+1.

Asymptotic high-probability sampler, conservative version:
Let b=log2p, H=Hrho, r>=1 withr logb=o(b), and n=(2r+4/5)b/H+O1.
Take t=16(r+1), m0=(n-a)/2-2t-r, D0=(K+1-epsilon)/2-t.
Then log2binom(m0,D0)=rb+(2/5)b-O_rho(r+logn)>=rb+b/3 eventually.
The base missing density is<=p^-1/8 exceptprobp^-Omega1, byMarkov.
At each stage, as long as h<=p^-1/8 and C²/p<=p^-1/8,
 E[h_new]<=4p^-1/8*h. Markov gives
 P(h_new>p^-1/16*h)<=4p^-1/16.
Aftert stages, h_t<=p^-1/8-t/16<p^-r<1/V, so the image is complete.
Union failure O(t p^-1/16)+basefailure=p^-Omega1. No image is computed
by the sampler. The t=O(r) overhead costs onlyO(r) entropy, so all
rate/Elias/prescription conclusions survive; growingr→infinity gives
farfraction→1 atlengthn~2rb/H. Code/line stillsampledpoly(logp).

Finite certificates should optimize t using the dyadic existence
recurrence, often t≈r+2 rather than16(r+1). These optimized EXISTENCE
certificates do not automatically inherit a chosen finite randomized
failure guarantee. Separate threshold schedules can prove such bounds.

Potential finite rows to test: M521 n2518 r2 with t3,
m0=1259-2-6=1251,D0=630-3=627. Initial missingbitsabout202;
dyadic recurrence should give~404,808,1322>r*b1042 ->fullG.
M1279 n26218r10 mayneedt12, m0=13075,D0=6543; initialbits~278,
then doubling and adding~1268 bits perstep shouldcross12790.

Proof obligations: exact Fourier-Parseval identity for translates,
conditioning/deletion bound, finite dyadic certificate replay, exact
full-affine-space distance fixture, high-probability threshold argument,
and all parity/rate/entropy details before promotion.
