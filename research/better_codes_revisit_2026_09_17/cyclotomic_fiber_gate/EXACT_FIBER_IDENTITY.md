# Exact cyclotomic fibers are eight-packet fibers

This is a pure counting identity and a scoped obstruction to lifting the pinned coefficient-fiber problem to exact characteristic-zero moment equalities. It is not a finite-field upper bound, an improved benchmark certificate, or a protocol claim.

## Exact theorem

Let zeta be a primitive complex 256th root of unity. On the 136-subsets U of mu_256 minus {1}, use the signature consisting of the first six root power sums and the root product. The LARGEST signature fiber has exactly

    8,287,155

members. Newton identities give the same assertion for six leading nonmonic coefficients plus root product.

Proof of packet structure. For two subsets U,V, let d_j=1_U(zeta^j)−1_V(zeta^j). Equality of the first moments says sum_j d_j zeta^j=0. Since Phi_256(T)=T^128+1, the rational coefficients satisfy d_j=d_(j+128). Equality of the second moments then reduces to the analogous primitive-128th-root equation and gives period64. Equality of the fourth moments similarly gives period32. Thus the signed difference is constant on every coset of mu_8. Conversely, such a difference has vanishing moments1,...,7, since those exponents are not divisible by8. So moments1,2,4 already determine EXACTLY the same fibers as moments1,...,6.

Within one fiber, a packet containing both occupied and unoccupied positions cannot change: adding the same signed difference to every position would leave {0,1}. Only entirely full/empty packets may toggle. The packet containing1 cannot be full. Label the other31 packets by j=1,...,31, where their representative eighth powers are the nonidentity roots xi^j in mu_32. A full packet has root product −xi^j.

For any fiber, let r be its available full/empty packets and let c be the fixed number of occupied points in the other packets. Then c+8k=136, so c=8q and k+q=17. There are at most32−r fixed mixed packets, each with at most7 occupants, hence q<32−r and q<=31−r. Add any fixed q nonidentity packets outside the available r packets to each chosen k-packet set. This injects the fiber into 17-subsets of the31 nonidentity tags. It multiplies products by one fixed constant, so its image lies in a single product class.

Conversely, taking unions of17 whole packets among these31 makes all first six moments zero. Any product class then IS a signature fiber. Thus the exact maximum equals the largest product class of17-subsets of mu_32 minus {1}.

`check.py/json` computes all32 class sizes in two independent ways: cardinality/exponent-sum dynamic programming, and the integer Ramanujan filter. Their sum is C(31,17)=265182525 and their maximum is8287155. This tiny test verifies only the final integer enumeration; the structural proof above is symbolic.

## What it does and does not decide

The frozen finite field has p=2130706433 and the exact same combinatorial roots embedded in F_p. Its guaranteed largest signature fiber is already68579341025511059, while the proposed target is274980728111395088. These are far larger than8287155. Thus even the BASELINE finite-field guarantee necessarily merges billions of distinct characteristic-zero signatures. No proof based solely on exact cyclotomic equality, roots-of-unity symmetry, or archimedean central concentration of an exact common signature can give the requested improvement.

The rational irreducibility step above fails after reduction: T^128+1 splits into linear factors over F_p. Vanishing at the selected finite-field root does not force its cyclotomic conjugates to vanish. This is precisely where the large modular fibers arise. It would be incorrect to transfer the number8287155 as an upper bound on a modular fiber.

## Remaining decisive lemma

A positive next result must concern the REDUCED six-moment-plus-product distribution itself: either exhibit a fiber of size274980728111395088, or prove an excess-collision estimate of the strength already stated in SECOND_MOMENT_TARGET.md. A negative result would need a uniform modular fiber upper bound below that threshold. The packet identity supplies neither.

The inexpensive discriminating check is now exact: any proposed concentration construction whose equality proof lives over Q(zeta_256) is capped by8287155 and should be stopped before a larger computation. A proposed genuinely modular mechanism must identify which finite-field relations defeat this packet structure; rerunning product-class counts, coarser packets, or rotational quotienting does not do so. No inexpensive complete test of the six-dimensional modular distribution has been identified, and no large search is recommended on this evidence.
