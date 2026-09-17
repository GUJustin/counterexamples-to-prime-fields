# Multi-pair blocks: candidate near-full-gap separation

NEW WORKING ARGUMENT, NOT YET INTEGRATED OR FULLY AUDITED.

For any fixed r>=1, use the same paired core, candidates w-H_I,
K=2D-1. Each padding block contains r distinct ±orbits. A candidate
matching its r-vector of directions at label z gets2r new agreements.
Threshold A=2D+2r, eta=(2r+1)/n, far2r/n, fraction2r/(2r+1).
Parity adjustments in paired.tex preserve every rational exact rate.

Joint-image collision argument. Fix r nonzero x_j with distinct squares,
and sample independent seed a in T=Fp minus {0,±x_1,...,±x_r}, size
N=p-2r-1. Vector v(a)=(x_j²-a²)_j lies in G=(Fp*)^r, |G|=V=(p-1)^r.
For each nontrivial multiplicative character tuple, combine characters
using a generator of the character group of Fp*. The resulting polynomial
has <=2r distinct roots, with some exponent not divisible by p-1.
Weil therefore bounds the full-field sum by 2r sqrtp. Removing the
2r+1 excluded arguments gives normalized Fourier bound
 lambda=[2r sqrtp+2r+1]/N.

For supports with symmetric difference u on each side, independent seeds
have vector collision probability
  (1/V) sum_chi |hat(mu)(chi)|^(2u) <= 1/V+lambda^(2u).
Conditioning the m seeds to have distinct squares costs at most1/a,
 a=1-m(m-1)/N, by union bound; nonzero is already built into T.
For u>=r+1, bound by (1/V+lambda^(2r+2))/a whenlambda<1.
For close supports u<=r, use probability<=1. Each support has at most
 S=sum_(u=0)^r binom(D,u)binom(m-D,u)
close supports, including itself.

Average over the joint distribution of a good seed and an outside r-block.
This is the same as choosing the r-block first and then good seeds outside
it: all good seeds have the same number of possible outside blocks, and
all blocks have the same number of good seeds. If E is the vector-image
collision energy and Delta=V E/L²-1>=0, then
 E[Delta] <= delta=V*S/L+(1+V*lambda^(2r+2))/a-1.
For fixed r,m=Theta(logp),L>=p^(r+epsilon), delta=p^-Omega(1).

Randomly select q disjoint outside blocks. Every block has the same marginal
law used above, so union+Markov gives P(any Delta>gamma)<=q delta/gamma.
When all Delta<=gamma, each image has size>=V/(1+gamma). Independent
uniform nonzero directions in each block leave expected missing labels
<=(p-1)(gamma/(1+gamma))^q. Thus generator failure is bounded by
 q delta/gamma+(p-1)(gamma/(1+gamma))^q.
No independence of the block-goodness events is needed. Uniform directions
are drawn AFTER seeds and blocks; conditioned on those, block hit events
for a fixed z are independent.

Asymptotics: choose rho<beta<1, alpha=rho/beta, and
 2r/(alpha H(beta)) < C < (2r+1)/H(rho).
Then n~C log2p, m~alpha n/2, D~rho n/2, L>p^(r+epsilon),
q~(1-alpha)n/(2r). Pick fixed gamma small enough that the second
failure term is p^-Omega(1); the first is too. Full p-1 coverage,
strict Elias, and n*2^(H(rho)/eta)=o(p), with separation
[2r/(2r+1)]eta, arbitrarily close to the entire capacity gap.
For general numerical constant c2 require c2<1+1/(2r).

Proof obligations before promoting:
- primary source and exact Weil hypothesis / zero-extension convention;
- Fourier orthogonality and conditional-good-seed normalization;
- exact finite r2/r3 collision histograms and Fourier identity;
- independently replay all parity variants at threshold2D+2r;
- exact finite arithmetic probability certificates;
- asymptotic error exponents, coefficient quantifiers, no FFT transfer.

## Sharpened audit: all short support differences are collision-free

The close-support term S is unnecessary. If 1<=u<=r, after canceling
common roots the difference of two distinct monic degree-u polynomials
in Y=X² has degree<=u-1<r. It cannot vanish at r distinct Y_j. Thus
under the good-seed condition these pairs have ZERO joint collisions.
Only the L diagonal pairs contribute directly, giving the sharper

 delta=V/L+(1+V*lambda^(2r+2))/a-1.

Primary character-sum input checked: Bourgain–Garaev–Konyagin–Shparlinski,
arXiv1110.0812v2, Lemma17, printedpage10 (PDFpage10). Product of2r
characters at distinct shifts±x_j, at leastone nonprincipal, constant
additive phase, bound2r sqrtp. Existing bibkeybgks-shifted. Use the
conservative correction2r+1 for deleted arguments regardless of zero
extension convention. No new geometric input needed for this route.

## Growing r: relative far separation tends to one

Let b=log2p, H=H2(rho), J=-log2(1-rho)>0, r=floor(b^(1/3)).
Choose n=(2r+1/2)b/H+O(1) respecting rate parity; m=(n-tb)/2+O(r),
t=1/(4J), with m adjusted so q=(n-a-2m)/(2r) is integral. Here
a in{0,1} is the extra-zero coordinate flag. D=(K+1-epsilon)/2.
Then q~t b/(2r), and entropy expansion gives
 log2 binom(m,D) = r b + b/8 + O_rho(b/r+r+log b).
Indeed m H2(D/m)=(n/2)H-(t b/2)(H-rho H')+O(b/r+r),
H-rho H'=J. Thus L>=p^(r+1/9) eventually. Also
 V lambda^(2r+2) <=p^-1*(2r+o(1))^(2r+2)=p^-1+o(1),
1-a=O(m²/p), delta=p^-Omega(1). Take gamma=p^-1/20.
The first failure term q delta/gamma tends to zero polynomially in p;
second term U gamma^q is negligible because q→infinity.

Result if all details survive final audit: n=Theta(b^(4/3)),
eta~H/b, full p-1 coverage, exact far distance1-rho-1/n,
relative separation1-1/(2r+1)→1, strict Elias sinceeta*b-H=Theta(1/r)
dominates the O(1/b) entropy-radius change, and
 n*2^(H/eta)/p=n*2^(-b/(4r+2)+O(1/r))→0.
The code/line sampler remains polynomial time in logp.
This defeats c2=1; it does not extend to c2>1 fixed asr→infinity.
