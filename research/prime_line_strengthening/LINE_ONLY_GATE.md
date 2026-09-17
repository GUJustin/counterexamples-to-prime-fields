# Prime-field line strengthening: exact bottlenecks and a narrower target

2026-09-17. Research note, not a novelty claim or new fixed-gap construction.

## What cannot be amplified mechanically

Every length-n, dimension-k RS code has covering radius at most 1-k/n: interpolate any k coordinates of any word. Thus a word outside radius 1-rho-eta can have excess at most eta. Constant two-input separation requires constant eta, regardless of the construction. The existing paired affine profile also has the sharper two-input total-excess budget already proved in profile_lines.tex. Adding directions or batching does not remove either fact.

For m core sign-orbits and r padding sign-orbits, full product completion requires

    (p-1)^r <= binom(m,D).

The asymptotic entropy budget forces eta log p on the constant scale when eta is approximately r/(m+r). Increasing r cannot turn the current all-image construction into a fixed-gap result. Replacing pairs by larger equal-sized multiplicative fibers rescales both agreements and length by the same factor, leaving this budget intact. It does not provide a prescribed full subgroup: a union of selected fibers is still a selected domain.

## Exact maximum-distance modification and why it does not solve the problem

For an existing completed fixture with dimension K and monic reference locator w of degree K+1, enlarge the code to dimension K+1. Every old witness still belongs to the code. Any new codeword P has degree <=K, so w-P has degree K+1 and at most K+1 evaluation roots. The zero word attains that number. Sparse perturbation and the old matching witnesses consequently prove, without enumerating the enlarged code,

    dist(f+sum z_j e_j, RS_{K+1}) = 1-(K+1)/n-2 wt(z)/n.

The far point is now at exactly the covering radius. All actual distances, including the two far endpoints and their interior mixtures, are unchanged. The new gap relative to rate (K+1)/n is eta'=2r/n, so the two endpoint excesses are eta'/2 for even r. The one-coordinate gain in the old definition of eta has vanished.

At the current length n=((2r+4/5)/H) log_2 p+O(1), eta' log_2 p is below H, rather than above it. More precisely the independent ROOT_ENTROPY_GATE.md proves the full-image cardinality requirement is incompatible with strict Elias whenever

    eta' ln(1/(rho+eta')) >= (1-rho) ln(p/(p-1)).

I checked its identities for the exact even setup n=2(m+r), k=2D. They are correct. The completion's extra alternative pairs are part of m, so there is no missing resource term. At fixed rho, eta' tending to zero, and n=o(p), this gate applies eventually.

To target exact rational rho, one could start with old K=rho n-1 (choosing n through even denominator multiples gives even new k=2D). Candidate cancellation and degree accounting remain valid, but the same entropy obstruction remains. This is therefore an exact geometric variant OUTSIDE the claimed below-Elias strengthening, not a manuscript improvement that retains all current guarantees.

## A line-only sufficient condition that avoids full-image counting

Let E and B be disjoint subsets of F_p, with |E|=N, |B|=q, n=N+q. Let k<=N. For each k-subset A of E write F_A(X)=prod_{a in A}(X-a). Fix A_0 and w=F_{A_0}. Suppose a function g:B->F_p^* has the following property:

    for every z in F_p^*, there is A_z subset E, |A_z|=k,
    with F_{A_z}(x)=-z g(x) for every x in B.             (LC)

Extend g by zero on E and put f=w on the entire domain. Then for the dimension-k RS code:

    dist(f,C)=1-k/n,
    dist(f+z g,C)=1-(k+q)/n for every z!=0.

Proof: P_z=w-F_{A_z} has degree <k and agrees with f+zg on A_z union B. Conversely f has distance n-k by the degree-k root bound, and changing q coordinates can improve agreement by at most q. This proves exact distances. Every nearby witness must match all B, so different nonzero labels have disjoint lists. The far point excludes an ordinary common-agreement witness at k+q coordinates: such a pencil would also agree at z=0, contradicting the far distance. Here (LC) only asks for one multiplicative diagonal, not all (p-1)^q vectors.

Necessary counting is merely p-1<=binom(N,k), not (p-1)^q<=binom(N,k). Thus fixed rho and fixed eta=q/n leave a substantial nonempty entropy window, with p exponential in n if desired. Strict Elias then imposes no counting contradiction, since eta log p grows with n. This is a precise constructive target, not an existence theorem for (LC).

Equivalently, with R_B=prod_{x in B}(X-x), find completely split degree-k monic polynomials on the fixed core whose residues modulo R_B run through all nonzero multiples of a single invertible residue class. The missing input is a globally coordinated splitting family, not further completion of a random joint image.

## Two concrete easy approaches to (LC) are obstructed

**Polynomial pencils.** If the locators are F_z=U+zV, with U,V fixed and z distinct, their root sets outside the common roots of U,V are disjoint. After canceling gcd(U,V), if each locator has d>0 residual core roots, a bank with L labels needs at least Ld core points. Since E avoids the q nonempty padding points, |E|<p. It cannot cover all p-1 labels when d>=1 and q>=2 (and a near-complete bank at fixed d/n is only O(1)). Nonlinear witness switching is essential. The stronger existing polynomial-witness incidence lemma already quantifies how high the parameter degree must be.

**Independent binary packet switches.** Suppose the locator bank is produced by independent binary choices of equal-sized root packets U_j,V_j, disjoint between slots, and EVERY choice satisfies a scalar residue condition modulo R_B. Compare two choices differing only at slot j and cancel their common factors (these are invertible on B). Then

    F_{U_j}(x)=c_j F_{V_j}(x), x in B.

Remove U_j intersection V_j; the remaining monic locators have equal degree d_j. If the switch is nontrivial, root counting on their difference gives d_j>=q (and d_j>=q+1 when c_j=1). Each slot consumes at least 2q distinct core coordinates. Therefore J independent binary slots have N>=2qJ and at most 2^J scalar outputs. Covering p-1 labels forces

    q/n <= 1/(2 log_2(p-1)+1).

Hence independent packet-switch constructions also cannot achieve fixed gap. This includes a natural attempt to use independent cyclotomic distribution identities; it does NOT exclude globally overlapping, dependent cyclotomic identities.

## Most promising remaining escape and stop criterion

The clean target is a globally coupled, large splitting family with rank-one residues on q=Theta(n) prescribed padding coordinates, ideally within a full multiplicative subgroup. It must escape independent switch factorization and low-degree witness parametrization. Cyclotomic-unit identities with overlapping supports are a genuinely different possible source, but I have no verified family meeting these requirements. Claiming a candidate construction from such identities without simultaneous splitness and residue checks would be speculative.

Stop further random full-image optimization and independent packet amplification for the fixed-gap objective: the exact gates above already defeat them. A new search should proceed only after producing a coupled identity with (i) degree-k squarefree split locators on one common domain, (ii) q linear in n, (iii) many distinct scalar residues, and (iv) characteristic/field size compatible with the promised fraction of all labels. This note supplies no new fixed-gap or prescribed-domain counterexample.
