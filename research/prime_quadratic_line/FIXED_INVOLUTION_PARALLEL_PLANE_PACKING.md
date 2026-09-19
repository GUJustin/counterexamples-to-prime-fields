# Fixed-involution packing across parallel coefficient planes

September 19, 2026. An exact necessary condition, not a new counterexample or global rigidity theorem.

Let F be a field of odd characteristic, D a set of n distinct elements, and f:D→F a received word. Let Q be M distinct polynomials of degree at most two, each with a selected T-element agreement set, where T≥3 and (T−1)²>n−1. Set

    R=(n−1)(T−2)/((T−1)²−(n−1)),  b=T²/n−1.

In particular b>0. The anchor argument in DENSE_DOUBLE_INTERSECTION_SIX_ROOT_TRIANGLES.md shows that at most R members of Q have any particular coordinate in their selected sets.

Fix one nonidentity projective involution

    iota(x)=−(beta x+gamma)/(alpha x+beta),
    beta²−alpha gamma ≠ 0.

Only its two-element orbits {x,y} contained in D will be used. There are at most floor(n/2) such orbits. Define the nonzero coefficient functional

    ell(A X²+B X+C)=gamma A−beta B+alpha C,

and the parallel affine coefficient planes P_tau={q:ell(q)=tau}.

## 1. Each native orbit is owned by exactly one plane

For each orbit {x,y}, there are unique nonzero scalars lambda,mu such that

    ell(q)=lambda q(x)+mu q(y)                 (all quadratic q).

Indeed ell annihilates (X−x)(X−y), because alpha xy+beta(x+y)+gamma=0, so it belongs to the span of the two evaluation functionals. Neither scalar can vanish: ell proportional to a single evaluation functional would force beta²=alpha gamma.

Consequently a quadratic agreeing with f at both x and y must lie in the unique plane

    tau=lambda f(x)+mu f(y).

Let h_tau count the native orbits assigned to P_tau in this way. Then

    sum_tau h_tau ≤ floor(n/2).                           (1)

Within its assigned plane, the two agreement equations at x and y define the same affine line. In all other parallel planes, they define distinct parallel lines. Different native orbits give different line directions: proportional restrictions of evaluations at x and z to ker ell would imply that {x,z} is the same involution orbit.

Thus this is an ordinary affine line arrangement inside each coefficient plane, with h_tau distinguished lines of pairwise distinct directions. It does not force those lines into a pencil.

## 2. Six-root triangles have a finite orbit budget

Let H_tau count the six-root triangles of Q whose coefficient points lie in P_tau and whose involution is the fixed iota. Then

    H_tau ≤ binom(h_tau,3),
    H_iota=sum_tau H_tau ≤ sum_tau binom(h_tau,3).         (2)

Proof: the three disjoint root pairs of such a triangle are three owned orbits. Their three agreement lines in P_tau have distinct directions, and their pairwise intersections uniquely determine the three polynomial vertices. If the lines are concurrent there is no six-root triangle. Hence any three orbits yield at most one unordered polynomial triangle. Selected support restrictions can only remove triangles.

Writing h_max=max_tau h_tau gives the additional bounds

    H_iota ≤ floor(n/2) (h_max−1)(h_max−2)/6
            ≤ n h_max²/12                               (3)

when h_max≥3 (otherwise H_iota=0). In particular, H_iota>0 implies that some parallel plane owns at least sqrt(12 H_iota/n) native orbits. This is conditional concentration for ONE involution; the earlier triangle-supply lemma does not show that any one involution has a large share.

## 3. Rich-polynomial populations also consume the orbit budget

Put r_tau=|Q∩P_tau|. Two selected supports in one plane intersect twice only on an owned orbit. Every such orbit belongs to the selected sets of at most R polynomials. Therefore the number m_tau of double-intersection edges inside P_tau satisfies

    m_tau ≤ h_tau R(R−1)/2.

Applying the elementary edge lower bound to this subfamily yields

    b r_tau²−(T−1)r_tau ≤ h_tau R(R−1).                 (4)

Thus

    r_tau ≤ ((T−1)+sqrt((T−1)²+4b h_tau R(R−1)))/(2b).  (5)

Also, since h_tau≥0 and the planes partition Q,

    sum_tau max(0, b r_tau²−(T−1)r_tau)
       ≤ floor(n/2) R(R−1).                             (6)

For T=(c+o(1))sqrt(n), c>1 fixed, this gives

    r_tau=O_c(sqrt(n)+sqrt(n h_tau)).

Planes containing substantially more than sqrt(n) rich polynomials must consume a quadratic amount, r_tau²/n, of the fixed involution's native-orbit budget.

## Scope and remaining obstacle

These statements use only degree two, distinct native coordinates, and one received value at each coordinate. They hold in extension fields as well as prime fields and do not exploit n<p. No global affine coefficient plane, common involution, or prime-field incidence improvement follows.

The fixed-involution maximum in (2) is still O(n³), while a hypothetical M=O(n) rich list needs only O(M³) six-root triangles. Thus this packing lemma alone does not exclude the target range. A useful next theorem would have to control triangle distribution BETWEEN involutions, or improve the incidence bounds inside these particular coefficient planes using additional structure. Treating all parallel planes as independently having n/2 available orbits would lose the genuine shared-budget constraint (1).
