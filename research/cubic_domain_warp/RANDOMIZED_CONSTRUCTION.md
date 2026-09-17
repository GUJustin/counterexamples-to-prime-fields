# Efficient randomized output of the code and received line

September17,2026. Proof and finite checks completed; integrated as a randomized-construction proposition; no witness-enumeration
claim and no deterministic certification of an individual random sample.

Use the cubic theorem's fixed parameters m,t,s,K=t-s-1,N=m-1,R=p-N,
U=p-1 and its collision multiplier B. Let Q=binom(m-1,t-1), the number
of anchored supports, and let V bound the number of their first3s
integer moment vectors. Elementary binomial-moment ranges give an exact
integer V. Write mu=Q/V.

Algorithm: sample an anchored t-subset uniformly. Sample cubic parameters
uniformly until their map is injective on all m seed nodes. Sample q
outside coordinates uniformly without replacement and q independent
uniform nonzero directions. Set w to the monic locator of the sampled
transformed support with its anchor removed. Output the domain, RS
code dimensionK, and line w+zg (g=0 on the core).
No moment class is found or enumerated, and no evaluation image is computed.

For any threshold H>0 and tolerance gamma>0, the probability that some
nonzero parameter is not nearby is at most

    H/mu + delta/gamma + U*(gamma/(1+gamma))^q,
    delta=U/H + U*B/R - 1.

Derivation:
1. The sampled support lies in a class of size<H with probability at
   most V*H/Q: sum the sizes of at mostV such classes.
2. Condition on a class of sizeL>=H and a uniformly sampled injective
   cubic map. Let E=sum_outside_x sum_(v!=0) r_(x,v)^2 for the L
   nonzero locator difference values. Deterministically E>=R*L²/U.
   Define D=U*E/(R*L²)-1>=0. The collision theorem gives
   E_map[E]<=LR+L(L-1)B, hence E_map[D]<=delta.
3. Markov gives P(D>gamma)<=delta/gamma. If D<=gamma, the average
   outside image size is at least L²R/E>=U/(1+gamma).
4. For q uniform DISTINCT outside positions, the expected product of
   their nonnegative missing fractions is at most the qth power of the
   population mean. This is the elementary-symmetric-mean inequality:
   replacing two entries by their mean increases the elementary
   symmetric polynomial, since only their product changes and its
   coefficient is nonnegative. Iterate and use continuity.
5. Independent nonzero directions therefore leave expected uncovered
   labels <=U*(gamma/(1+gamma))^q. Probability of any uncovered label
   is at most this expectation. Union with the first two bad events.

In the all-prime theorem, mu>=p^(1+epsilon) for fixedepsilon>0.
Take H=p^(1+epsilon/2) in the analysis; delta=p^-Omega(1).
Since q=Theta(logp), choose a fixed sufficiently small gamma so the
last term is <=p^-Omega(1). Thus success probability is1-p^-Omega(1).
The algorithm does not need to know H,gamma or its class size.

Sampling an injective map takes expectedO(1) trials, since bad-map
fraction<=binom(m,2)/p. Outside-coordinate rejection sampling also has
expectedO(1) cost per coordinate. For fixed theorem constants, n=O(logp),
and forming/evaluating w takes O(n²) field operations. The procedure
therefore outputs a valid counterexample in expected polynomial time
in logp, with success probability1-p^-Omega(1).

Far distance and absence of correlated agreement hold for EVERY output:
w is monic degreeD=t-1, and zero is a codeword agreeing exactly on the
D selected support points. The probabilistic part is complete nonzero
coverage. Finding a nearby witness for a supplied nonzero parameter is
not supplied by this algorithm.

Finite implementation: M521,n990,K495,m900,t497,s1,H=p*2^150,
gamma=2^-8 gives exact failure<2^-137. Independent sample verifier
checks each of the three terms<2^-130 using integer products, hence
sum<2^-128. StrictElias and prescriptionfraction<2^-16 also checked.
The stored sample's990coordinates are replayed by direct root products,
independently of the generator's polynomial-coefficient/Horner route.
Finite averaging checker enumerates16,806coordinate/direction choices
and a separate grid of elementary symmetric inequalities. No individual
sample's all-parameter coverage is claimed to be exhaustively checked.
