# Exact primary-source support objective and min-cut audit

Fix n,w,A,m,L and weighted cutoff D=mA. Let S be a subset of monomials Y^i R^j, with i+j≤Q and j≤Smax, downward under i→i-1. Attach the full coefficient prefixes

    X^a Y^i R^j Z^z,
    0≤a<D-wi-(w-1)j, 0≤z≤L-i-j.

Terms with nonpositive prefix are omitted. Its scalar dimension is exactly

    C(S)=sum_(i,j in S) (L-i-j+1)*(D-wi-(w-1)j).

## Exact local rank

For extraction grade ell<m and homogeneous jet degree q, let

    N_(ell,q)=#{i≤ell : (i,q-i) in S}.

Modulo contact order h=m-ell, substitution Y=R+E has matrix binomial(i,k), 0≤k<h, on the selected exponents i. If characteristic exceeds Q, distinct i have distinct residues and the initial Pascal rows form a Vandermonde system. Its rank is min(h,N_(ell,q)). The Z coefficients are independent, so the full one-point rank is

    R(S)=sum_(ell=0)^(m-1) sum_q (L-q+1)*min(m-ell,N_(ell,q)).

This formula does not assume that a divisible polynomial has monomial quotient support. Such an assumption can fail for nonconvex monomial supports: Y²-R² is divisible by Y-R even when the support omits YR.

If D>(m-1)+(w-1)Q, global extraction onto all these blocks is surjective at the zero local point: the source monomial X^(ell-i)Y^iR^j Z^z realizes the desired local monomial in precisely grade ell. The support is preserved by X translations and Y→Y+u0+u1 Z because it is Y-downward and has full prefixes. Thus this exact rank holds at every received coordinate. Without saturation, the formula remains an upper bound but surjectivity must not be asserted.

## Graph representation

Write x_(i,j) for the selected-support indicator. Each variable has source-edge capacity

    benefit_(i,j)=(L-i-j+1)*(D-wi-(w-1)j).

For every nonempty (ell,q) block add auxiliary node z and edges

    x_(i,q-i) -> z       capacity K=n*(L-q+1), i≤ell,
    z -> sink           capacity (m-ell)*K.

A source-side variable means x=1; a source-side auxiliary means z=1. The block cut cost is exactly

    K*((m-ell)*z + sum_i x_i*(1-z)).

Minimizing over z gives K*min(m-ell,sum_i x_i), the rank penalty. Finally add infinite-capacity implication edges x_(i,j)→x_(i-1,j). A finite capacity greater than the sum of all benefits is sufficient. With B the sum of benefits, every finite admissible cut has cost

    B-C(S)+nR(S).

Hence maximum interpolation surplus C(S)-nR(S) equals B minus minimum cut. This is a global finite optimization over all stated downward supports, not a restricted wedge or rectangle scan. Since the empty support is admissible, the optimum is always nonnegative; zero optimum means no positive interpolation certificate in this class.

## Frozen primary A instance

At n=262144,w=131071,A=181275,m=115,D=20846625,L=274277,Q=159,Smax=35 there are5130 candidate monomials. Saturation holds because

    D-(w-1)Q=6495>m-1.

A nonrectangular support with positive surplus and these frozen caps would restore primary-A existence without enlarging its declared factor or helper caps. Primary A requires positive nullity; the stronger quotient-nullity condition for TCap is a separate requirement and does not follow automatically. The normal-ledger cost at the binding factor is also a separate downstream calculation: source positivity is not a7.65-percent ledger improvement by itself.

An independent optimum audit should verify an actual flow and cut certificate (capacity inequalities, flow conservation, equal flow and cut values), then independently recompute the selected-support dimension and Pascal-rank sum. A selected support alone proves feasibility, not global optimality.

## Retaining the full primary kernel

A positive restricted-support kernel can be used solely as a witness that the original full-box primary kernel is nonzero. One need not replace the primary kernel in universality or own-system definitions: inclusion preserves the old full kernel and all statements quantified over it. Equivalently, rank of the full map is at most rank of the restriction plus the number of omitted columns. This observation preserves the old interface, but does not create positivity when the optimized restricted surplus is zero.
