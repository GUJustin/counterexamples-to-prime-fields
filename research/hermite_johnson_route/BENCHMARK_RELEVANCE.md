# Does the degree-three theorem directly improve the benchmark?

**Not through the current raw ConstraintKernel interpolants.** There is a structural obstruction before numerical constants: their zeroth local block forces the specialized equation to vanish identically in the derivative and challenge at every domain coordinate. Their ordinary core therefore has size n, so the new signed Hermite–Johnson hypothesis fails. A successful transfer would require a justified extraction/normalization that removes these ordinary fibers, or a genuinely different source identity. Simply imposing derivative degree at most three is insufficient.

## 1. Full ordinary core is built into the current source

The pinned source is `proximity-prize/proximity-prize` at `cdb451f13fdc6c84f5fe363e77ee13a89bd30974`. In cached `LowerFoundation.lean`, the relevant first-jet map is `blockEntry` (around line16185), `constraintMap` (around line16270), and `all_blocks_divisible_of_equations` immediately afterwards.

Write the source polynomial as Q(X,Y,R,Z). At coordinate x with received affine value `u0(x)+u1(x)Z`, its r=0 extracted block is exactly

`Q(x,u0(x)+u1(x)Z,R,Z)`.

It is independent of the local transverse variable a. The ConstraintKernel condition says this block lies in the kernel of the order-m contact jet, equivalently is divisible by `(a−R)^m`, where m≥1. A nonzero polynomial independent of a cannot be divisible by a polynomial of positive a-degree. Therefore

`Q(x,u0(x)+u1(x)Z,R,Z)=0`

identically in R,Z, at **every** domain coordinate. If deg_R Q≤3, all four specialized derivative coefficients vanish identically. This is precisely the full ordinary core of the new theorem, u=n. The argument is characteristic independent and does not depend on numerical source parameters.

Dividing a source by a univariate domain factor is not automatically legitimate: ordinary-fiber vanishing does not assert divisibility by X−x as a polynomial in all variables, and an actual nearby polynomial may make such a division incompatible with the source construction. No such normalization is claimed here.

## 2. A separate derivative-cap dimension gate

Even ignoring that structural obstruction, small derivative caps do not reach the current target through the tested source dimensions. The pinned parameters are n=262144,w=131071 and target agreement A=181275, or **0.6915092468261719**.

`benchmark_source_gate.py` tests all 11,636 triples with multiplicity1≤m≤64, derivative cap0≤S≤3, and all integer YS caps from zero through the automatic cap `floor((mA+S−1)/w)`. It uses the independently audited restricted local-block rank, not a guessed rank reduction. In the exact affine-L regime

`L≥max(Y,m+S−1)`,

both the nullity lower bound at the left endpoint and its slope are nonpositive in every case. Thus no L in that regime supplies a positive dimension certificate for any tested triple. This is not a statement that no actual kernel exists, nor a global exclusion of other supports or smaller-L regimes.

For an automatic untrimmed source, the positive affine-L slope threshold can be determined globally over all multiplicities. The **sharp integer onset is A=183960**, or **0.701751708984375**, attained at m19,S3 and also m21,S3. The m19 witness has Y26 and minimal affine-regime L2213859, with a positive kernel lower bound of163. This is 2685 more required agreements than the target, not a benchmark improvement.

## 3. Exact all-multiplicity slope certificate

For m≥2S the local-rank slope is

`R_L=(S+1)/2 * [m²+(1−S)m+S(2S+1)/3]`.

Let `c=(w−1)/w` and `nu_j=mA/w−c*j`. The untrimmed coefficient-count slope satisfies

`C_L ≤ (w/2) Σ_(j=0)^S (nu_j²+nu_j+1/4)`.

This follows from the exact triangular arithmetic progression and the bound `fractionalPart(nu)*(1−fractionalPart(nu))≤1/4`. If nu is negative the true progression is empty and the squared upper bound remains nonnegative.

Consequently `2(C_L−nR_L)/(S+1)` is bounded above by the explicit concave quadratic

`(A²/w−n)m² + [A(1−cS)−n(1−S)]m`

`+ w[−cS/2+c²S(2S+1)/6+1/4] − nS(2S+1)/3`.

At A181275 this upper bound is strictly negative on m≥max(1,2S), for every S0..3. For sharp onset, exact arithmetic checks m1..64 at A183959; the same quadratic is negative and decreasing for all m≥64. The witness at183960 proves the stated globally sharp **positive-slope** threshold. It is deliberately not promoted to an all-support or all-L impossibility theorem.

With fixed S and growing m, the leading slope condition is `A²>nw`; thus this regime tends back to the ordinary Johnson threshold. The useful first-order source gain relies on derivative cap growing with multiplicity. The low derivative-degree theorem and the present optimized interpolation source therefore occupy different parameter/structural regimes.

## 4. Practical limits

The theorem's explicit constants are not a ready numerical certificate: the example small-S source already has challenge degree over two million, and the regular and specialization bounds grow with that degree. Positive source dimension, a controlled ordinary core, valid full-support geometry, and an acceptable final challenge-label budget are separate gates. None of the latter gates is established by the positive dimension example.

All numerical jobs took about one second or less and less than 24 MiB, under the repository watchdog. Exact outputs are `benchmark_source_gate.json`, `small_s_slope_bound.json`, and `small_s_global_threshold.json`, with corresponding scripts and resource reports. There is no better.codes score claim.
