# Order-five periods: three named factor mechanisms checked

September 18, 2026. Exact identities and their supplied coverage only. This does not exclude accidental factors or the general order-five bank.

Use F(P)=sum_(T in H) chi(T)x(P+T), H=E[ell], M=ell², ell=-1 mod5, and G_S(P)=F(P+S)+F(P-S). The polynomial bank is Q_S=D0 G_S, with degree at most M and L=(M+1)/2 distinct labels modulo sign. Characteristic is different from 2,3,5,ell; retain the noncollapse guard of the earlier note.

## 1. Cyclic subgroup traces: exact formula, not equal remainders

For a cyclic subgroup J of order ell, chi is constant on J minus zero; denote that value chi(J). For U in H,

    sum_(S in J) chi(U-S)
      = (ell-1)chi(J), U in J;
      = -chi(J),       U outside J.

Proof: the first assertion is immediate. The sum is constant on cosets of J and invariant under multiplication by F_ell*, which acts transitively on the nonzero cosets. Summing over U gives zero, proving the second value.

Consequently

    sum_(S in J) F(P+S)
      = chi(J)[ell sum_(U in J)x(P+U)-sum_(U in H)x(P+U)]
      = chi(J)[ell x(phi_J(P))-ell² x([ell]P)+c_J'],

where phi_J is the normalized Velu quotient. The second equality uses sum_(U in J)x(P+U)=x(phi_J(P))+constant and sum_(U in H)x(P+U)=ell² x([ell]P)+constant. The ell² normalization is essential: at P=0, x([ell]P) has leading pole coefficient 1/ell².

Thus the five-period decomposition does give a compact exact trace formula for EVERY cyclic subgroup. It controls a sum of bank values, not their differences. Its zero divisor cannot be asserted to divide Q_S-Q_T for S,T in J.

Even granting equality for a bucket confined to one subgroup or one subgroup coset, its size is at most ell. If every selected agreement bucket has that size, on N=4M coordinates the average agreement is at most N*ell/L=O(ell), whereas the target is >1.8751 ell². Thus this particular grouping is too small, even under the optimistic equality assumption.

Grouping by five fixed character classes is different but also supplies no usable scheme by itself. If two fixed labels always belong to the same indivisible class, every coordinate at which either class is selected is a root of their nonzero polynomial difference. Hence that class can receive at most M agreements per member (or the sharper offpole pair budget). The required agreement exceeds M. This applies to schemes that only select or merge WHOLE fixed classes; it does not apply to coordinate-dependent partitions that split those classes.

## 2. CM fixed points: genuine factors, bounded degree and buckets

Let u be a nonidentity elliptic automorphism fixing the origin, in characteristic not 2 or 3. In short Weierstrass coordinates x(uP)=k_u x(P). Suppose the induced action on H is multiplication by a scalar in the chosen F_(ell²) model. Its order belongs to {2,3,4,6}, hence is coprime to 5, so chi(u)=1, and reindexing gives

    F(uP)=k_u F(P),       G_(uS)(uP)=k_u G_S(P).

At a point fixed by u, this gives G_(uS)(P)=k_u G_S(P), NOT equality unless k_u=1 or G_S(P)=0. The case u=-1 has k_u=1 but already identifies the same label S modulo sign. For the other CM automorphisms, a zero value can merge one automorphism orbit, whose size is at most 6. Fixed points lie in ker(u-1), of size at most 4 in these characteristics; their x-coordinates supply only O(1) factors. The same conclusion holds for uP=-P by replacing u with -u.

Therefore the actual fixed-point identities have bounded coordinate and bucket resources. No growing balanced coverage follows. More general CM endomorphisms are not automorphisms: F composed with an endomorphism of degree d>1 has pole divisor degree multiplied by d, so it cannot equal a nonzero scalar times F plus a constant. This degree statement assumes separability, as required for the proposed torsion-fiber use.

## 3. Division fibers: permutation is not equality

For an integer d prime to ell and the ambient characteristic, summing over E[d] gives the exact distribution relation

    sum_(V in E[d]) F(P+V) = d² chi(d)^(-1) F([d]P).

Here multiplication by d on H is a nonzero F_ell scalar, so chi(d)=1 in the present ell=-1 mod5 case; it is retained in the formula to show the reindexing. The constant in the usual x-coordinate distribution relation vanishes after weighting by chi.

A fiber of [d] therefore has a controlled SUM of values. Neither this identity nor its specialization to a zero of F says that the individual summands agree. Likewise the fiber [ell]P=R is permuted by H, but translation covariance of an argument does not identify the values of F at the permuted points. A claimed factor from a division-polynomial fiber still requires the separate remainder calculation for Q_S-Q_T from the previous note.

## Decision

The named identities yield one exact new cyclic trace formula, bounded CM fixed-point factors, and division-fiber sums. None supplies a scalable equal-remainder factor with the required degree and bucket size. In particular there is no positive gain prediction that would justify a finite fixture run from these identities alone.

The surviving concrete requirement is a coordinate-dependent partition of a growing bank, with large common remainders that are NOT merely traces, fixed character classes, or automorphism orbits. The earlier h=5 resource window remains open; this note makes no general exclusion or construction claim.

For the normalized isogeny identity used here see Moody–Rasmussen, Section 2.1, https://arxiv.org/html/1210.2743. All character-coset calculations and coverage counts above are derived explicitly.

Prime descent remains conditional: an actual characteristic-zero factor identity and its guards could be reduced at split good primes of its field of definition, with no controlled prime-size assertion. A finite modular coincidence would require an independent lifting or intrinsically modular growing construction.
