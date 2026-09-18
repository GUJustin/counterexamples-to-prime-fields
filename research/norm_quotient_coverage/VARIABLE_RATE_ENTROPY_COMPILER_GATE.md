# Variable rates: current completion certificate versus a genuine count-only escape

2026-09-18. The current seed/pair sufficient certificate does not asymptotically enter the DKT first-order region. However a universal obstruction based only on all-product coverage counts would be false as a parameter argument: a narrow high-rate regime survives those necessary constraints. It needs a new restricted two-product basis, not the current completion certificate.

Write M=p−1, n=(s+1)m≤p, m≥2, v=w/m∈[0,1), and

    ρ=[r−2+v+1/m]/(s+1), a=[r+v]/(s+1).

The elementary necessary coverage condition is binom(s,r)≥M. Along any growing-p family it implies s→∞. Set k=s−r (number of omitted tags).

## All but the two-element endpoints are below first order

The independently proved bound a1(ρ)−ρ≥min(ρ,1−ρ)/4 immediately excludes a≥a1 whenever r≥10 and k≥7, for all padding choices and fiber sizes.

For3≤r≤9, use a≤(r+1)/(s+1), ρ≥(r−2)/(s+1). For sufficiently large s (s≥64 suffices), a²≤ρ/2 and ρ is in the low-rate branch, where a1(ρ)>sqrt(ρ/2). Thus these low-cardinality cases cannot cross.

For3≤k≤6, put d=k+3−v−1/m. Uniformly in these bounded parameters, the upper branch expands as a1(1−d/(s+1))=1−d/[2(s+1)]+O(s^−2). Hence

    a1(ρ)−a=[k−1−v+1/m]/[2(s+1)]+O(s^−2)>0

for sufficiently large s, because the numerator is at least k−2≥1. Cases k0 or1 violate binom(s,r)≥M: their counts are1 or s, whereas n≤p,m≥2 imply s≤(M−1)/2.

For r2, a²/ρ=(2m+w)²/[(s+1)m(w+1)]≤9m/[(s+1)J]. Counting and n≤p imply (s+1)m−1≤M≤binom(s,2), hence m≤s/2. Therefore a²/ρ<9/(2J). If J≥9 this is below1/2. Only bounded dimensions J≤8 survive this crude count-only low-rate test.

## A count-only HIGH-rate escape, with large J

Take k2, i.e. r=s−2, and maximal padding w=m−1. Then

    ρ=(s−3)/(s+1),
    a=(s−1−1/m)/(s+1).

For x=1/(s+1), direct expansion of DKT equation(31) gives

    a1(1−4x)=1−2x−(7/2)x²−x³/4+O(x⁴).

If m/s→c, then a=1−2x−x²/c+o(x²). Thus the compiler's threshold lies ABOVE first order when c>2/7. The necessary count/domain conditions only impose c≤1/2 when p∼n. They leave the nonempty window2/7<c≤1/2.

Covering every product by (s−2)-subsets is equivalent, by multiplying by the product of all generators, to covering every group element by products of TWO DISTINCT generators. The escape would require such a restricted two-product basis among the allowed shifted-subgroup factors, with s²/p asymptotically below7/2, and compatible m∼cp^(1/2). This is a concrete unresolved algebraic target, not a proved construction. Necessary counting alone does not close it, and J grows almost as fast as n here.

## Why the current finite seed/pair certificate does not prove that escape

In the finite completion lemma, total final size is s=s0+2t and final cardinality r=r0+t. For k2, the seed complement is s0−r0=2−t. Since the seed requires0<r0<s0, only t0 or1 is allowed.

If t0, its energy bound h0≥(M−1)/binom(s,2). The final condition M h0<1 would require binom(s,2)>M(M−1), impossible because s≤(M−1)/2.

If t1, the seed complement is1 and L0=s−2<M−1, so h0≥(M−1)/L0>1. The stated recurrence h1=(h0²+γ0²h0)/(1−1/P0) is then greater than1, so it cannot certify coverage. Complement0 is not an admissible seed. The identical argument applies to final r2: t0 has the same binomial bound, and t1 has seed cardinality1.

Therefore every growing-p parameter sequence certified by the CURRENT finite seed/pair inequality is eventually below a1: the middle regimes and cardinalities3 through9 / complements3 through6 are excluded above, and its criterion cannot certify the only remaining two-element endpoints. This conclusion does not forbid a better seed-energy analysis or a separate explicit two-product construction.

The fixed-rate entropy corollary is only a special case. The restriction here concerns the actual finite sufficient certificate, not an unjustified extension of fixed-ρ asymptotics to ρ→0 or1. No first-order tightness or practical benchmark improvement follows from the existing result.
