# Cubic domain deformation: candidate full punctured-line theorem

September 17, 2026. Written proof, finite arithmetic audits, and final adversarial read
completed. The main paper now inputs cubic_warp.tex. SOURCE_AUDIT.md verifies the published
point-count hypotheses; both finite certificates have independent replays.

## 1. Arrangement irreducibility

Over an algebraically closed field, take two disjoint families of u
hyperplanes A_i,B_j in P^3 such that any four defining linear forms are
independent. The same holds for any subcollection of at most four.
For u>=2, F=product A_i-product B_j is irreducible.

For each i,j the base line L_ij=A_i=B_j=0 lies in F=0 and is generically
smooth on F: no other hyperplane vanishes at a generic point, so the
local equation has nonzero linear terms in A_i,B_j. Thus that line
belongs to exactly one irreducible component.
For i!=i', L_ij and L_i'j meet at A_i=A_i'=B_j=0. General position
excludes every other hyperplane there. The derivative from product B
is nonzero, whereas product A has two zero factors, so this is a smooth
point of F. Hence those two base lines lie on the same component.
Likewise L_ij and L_ij' do. Connectivity of the complete bipartite grid
puts every base line on one component G.
Restrict G to A_i=0. This restriction is nonzero, because A_i does not
divide F. It vanishes on all u distinct lines B_j|_(A_i)=0. Their
product therefore divides the restriction, giving deg G>=u=deg F.
Thus F itself is irreducible, and smooth base points also exclude a
repeated irreducible factor. The u=1 case is linear.

For distinct field elements a, the forms

    l_a=X-a U-a^2 V-a^3 W

are in the required general position by Vandermonde determinants.
For disjoint equal-size sets S,T, the homogeneous difference
product_(a in S) l_a-product_(a in T) l_a is consequently absolutely
irreducible. Set W=1: the resulting polynomial in X,U,V remains
absolutely irreducible. It is nonconstant and not a factor W.
It is the collision equation for the monic cubic map

    phi_(U,V)(a)=a^3+V*a^2+U*a.

## 2. Average collision count

Let a seed domain have m distinct nodes in F_p and a family of L
anchored t-subsets with the first 3s integer power moments equal.
Use nodes0,...,m-1 and anchor0. The cubic map preserves equal power
moments1,...,s, since phi(a)^j has degree at most3s in a.
At least p^2-binom(m,2)p parameter pairs (U,V) give an injective map:
each node collision cuts out one affine line in the parameter plane.

For two distinct supports, remove their common nodes. Their residual
support sets are disjoint and have equal size u. At an outside domain
point, collision of the associated codewords is equivalent to the
absolutely irreducible equation from part1. An explicit Lang–Weil
hypersurface estimate should bound its total (X,U,V) points by

    p^2 + O(t^5 p^(3/2)),

uniformly in the pair. (Primary source now verified; see SOURCE_AUDIT.md.)
Thus summing over pairs and averaging over injective maps gives one
map with total outside pair collisions at most

    binom(L,2)*(1+O(m^5/sqrt(p))),

provided p>m^2. The error is deliberately loose; polynomial dependence
on m is all that the asymptotic argument needs.

The transformed anchored locators H_S all share their first s
coefficients. Choose one H_0 and set w=H_0/X, P_S=(H_0-H_S)/X.
Then deg w=t-1 and deg P_S<=t-s-2. Distinct supports give distinct
candidates. Each P_S agrees with w on exactly t-1 core coordinates,
and P_S-w has no roots outside the core.

## 3. Image size and complete nonzero coverage

Let N=m-1 be the core size and R=p-N. For the good map from part2,
the average outside evaluation image size is at least

    M = L^2 R / (L R + L(L-1)*(1+O(m^5/sqrt(p)))).

If m=O(log p) and L>=p^(1+epsilon), then M/p=1-o(1).
Choose q=Theta(log p) distinct outside points with largest image sizes.
With independent nonzero padding directions, expected uncovered
nonzero labels are at most

    (p-1)*(1-M/(p-1))^q.

This tends to zero, since q/log p stays positive and the base tends
to zero. Therefore some directions cover EVERY nonzero parameter.
At parameterzero the global word w has maximum agreement exactlyt-1;
threshold A=t makes it exactlyone coordinate too far and excludes CA.

## 4. Fixed rate, fixed relative separation, below Elias

Fix rational rho in(0,1), finitec1,c2>=1. Choose rationalrho<beta<1,
alpha=rho/beta, and C>1/(alpha H2(beta)). Choose fixedintegers>=1
with (s+1)/C>c2H2(rho). For b=log2p choose n=Cb+O(1) through
common denominator multiples, K=rho*n,m=alpha*n,t=K+s+1.
The anchored t-subsets of0,...,m-1 number2^(mH2(t/m)-O(logm)).
Their first3s INTEGER moments have onlym^O(s²) possible vectors.
Hence some anchored class has L>=p^(1+epsilon) for fixedepsilon>0.
Applyparts1–3 with q=n-m+1=Theta(logp).

Proposed conclusion: every sufficiently large prime supports an
exact-rho code of lengthTheta(logp) and a received line for which ALL
p-1 nonzero parameters are nearby, while parameterzero is
kappa*eta outside, kappa=1/(s+1)>0 fixed, eta=(s+1)/n.
StrictElias follows eta*log2p→(s+1)/C>H2(rho).
Numericalprescriptionc1*n*2^(c2Hrho/eta)=o(p).
This would close the previously stated fixed-positive-relative-buffer
frontier, but still has shrinkinggapeta, arbitrary(nonFFT)domains,
and enormousactualgloballists. Do not claimfixedgapsuperlinearcount.

## Audit details and exact certificates

The common anchor is removed from the core but may be selected again
as a padding coordinate. In a support-pair difference, cancel the full
common locator BEFORE forming the irreducible residual equation. After
dividing by the anchor, the remaining common factor has roots only in
the core. Thus the collision equivalence remains valid at the former
anchor too. No available point is silently omitted from R=p-(m-1).

Primary source Cor5.6 gives the exact multiplier
B=[p+(t-1)(t-2)*sqrt(p)+3t^4]/[p-binom(m,2)], under p>2m².
Finite certificate uses integer square-root ceiling. Independent replay
uses anchored elementary binomial-moment boxes (no Gram helper imports)
and the coarser Theorem5.2 remainder5t^5. Both prove M/(p-1)>3/4 and
2q>=log2(p+1), so expected uncovered labels<1 without giant powers.

M1279: n3834,K1917,m2556,A1921,originalmoments9,transformed3,
q1279, allp-1nonzeroznear, zeroeta/4outside, strictElias,
numericalprescription<2^-307 fraction. Primarylistbits1653;
independentanchored-boxlistbits1547.
M9689: n18162,K9081,m12108,A9083,originalmoments3,transformed1,
q6055, allp-1nonzeroznear, zeroeta/2outside, strictElias,
prescription<2^-591 fraction. Primarylistbits9724; independent9702.
Both primality checks replayed. Directions/domain are existence-certified,
not enumerated. Geometry checker exhausts arrangement points foru1..4,
Vandermonde minors/smooth triple points, and all5692injective cubic maps
of a17-node anchored Thue–Morse moment pair overF131. It checks moments,
candidate degrees, agreement8, and5095totaloutsidecollisions.

Theorem can be sharpened to prescribed integeru>c2 and kappa=1/u:
choosebeta justaboverho and C between1/(alpha Hbeta) andu/(c2Hrho),
then s=u-1. See cubic_warp.tex for the formal formulation/proof.
The actual global list is still >p asymptotically: on the core use
thresholdt supports and3(s+1) moments before deformation, preserving
s+1 moments after, which makes degree<t-(s+1)=K.

Integration completed as Theorem4.18, with the strongest line claim now
in abstract/intro/README and the former fixed-kappa density frontier
removed from open questions. The remaining fixed-gap and prescribed-
domain questions are unchanged. A smaller independently verified row
has M127,n214,K107,m202,A109,q13, allp-1nearby, farη/2, prescription
fraction<2^-12. Gramlist151bits, independentbox137bits. Its exact
rational missing expectation is below1. Larger-row prescription bounds
were tightened to2^-308(M1279) and2^-593(M9689).
