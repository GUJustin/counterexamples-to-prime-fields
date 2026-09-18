# Complete octic-cover / three-pole norm gate

For both archived seven-cubic banks, every eligible multiplicity pattern gives a full-column-rank norm matrix. There are 386 patterns for Paley and 410 for orbit2. All 796 maximal minors were independently replayed. This excludes the indicated proper degree-eight-cover/three-pole augmentation in characteristic zero; it does not construct an eight-word bank.

## Geometry and scope

Let psi=R/S be a degree-eight rational map and let v=N/(D S^3), in homogeneous coordinates, with numerator degree at most27 and denominator D of degree3. Assume gcd(N,D)=1, D avoids the selected core, and the fourteen selected base fibers consist of eight distinct points each. Numerator cancellations with S are permitted, as are overlaps of D and S. Select exactly56 matching core points from any proposed witness with at least56 matches.

The map (psi,v) is birational onto its image. Indeed the positive part of the signed pole-order function

    poleorder(v)-3*poleorder(psi)

is exactly the proper degree-three divisor of D. Both pole-order functions pull back under an intermediate normalization map, so this positive divisor pulls back as well. The intermediate degree divides both8 and3, hence is one. This argument includes poles of D lying over infinity.

The primitive norm relation has coefficient of V^(8-j) of X-degree at most3j+3, by the elementary-symmetric pole bound. Its irreducible closure on the third Hirzebruch surface has class `8 C0+(24+c)F` for the actual pole excess parameter c<=3, where C0^2=-3. Adjunction gives arithmetic genus at most

    (8-1)(3*8/2+3-1)=98.

Using the actual class avoids artificial boundary components. Since the normalization is rational, the total singularity delta is at most98, and in particular the selected finite coincidences have this budget. This is the same compactification and adjunction calculation used in the manuscript addendum; no separate cancellation-at-infinity estimate is needed.

If m_j selected points lie in fiber j, birationality implies delta at their common image is at least binomial(m_j,2). Consequently

    sum m_j=56, 0<=m_j<=8, sum binomial(m_j,2)<=98.

Each old candidate can share at most27 selected coordinates with a proper new witness: its difference numerator N-D*S^3*P_i(psi) is nonzero and has degree at most27. Let T be the sum on the seven triple buckets. Counting old-candidate incidences gives 224-T<=189, so T>=35. Convexity gives minimum delta91,94,97,100 at T=35,36,37,38, respectively; hence T<=37.

## Exact finite census

Write triple multiplicities as5+u_j, quadruple multiplicities as3+v_j, and s=T-35 in {0,1,2}. Then

    sum u=s, sum v=-s,
    sum(u_j^2+v_j^2)<=14-4s.

The uniform baseline supplies27 matches to each old candidate. Their deficits d_i are nonnegative integers with sum s. If A is the7-by7 quadruple-incidence matrix and B is the triple-incidence matrix, then

    A v = -B u-d.

Both archived A matrices are invertible over Q. Paley has the familiar Fano-complement inverse; orbit2 does not, so the implementation computes its exact rational inverse separately. Enumerate all seven-coordinate integer u vectors within the displayed norm bound and sum, all deficit compositions of s, and solve uniquely for v. Retain precisely integral v satisfying their bounds and the full norm inequality. This is exhaustive and uses no floating-point optimization.

| Bank | T=35 | T=36 | T=37 | Total |
|---|---:|---:|---:|---:|
|Paley|43|259|84|386|
|orbit2|43|253|114|410|

## Norm matrix and certificates

The primitive degree-eight relation F(X,V) has coefficient of V^(8-j) of X-degree at most3j+3: elementary symmetric pole bounds clear a divisor of degree at most3, including infinity. There are sum_{j=0}^8(3j+4)=144 coefficients.

At a fiber with m_j distinct preimages, the image point has multiplicity at least m_j. Therefore every Hasse derivative of total order less than m_j vanishes there. This gives sum binomial(m_j+1,2)=56+sum binomial(m_j,2) rows. The implementation includes all of them, in ascending total order.

`census.py/json` records every admissible pattern. `gate.cpp` constructs the matrices directly over F29 for Paley and F83 for orbit2 and saves pivot rows, columns, and nonzero products. Every rank is144. `verify.py` independently reconstructs all Hasse entries with Python integer binomial coefficients and replays all 796 selected144-by144 determinants using exact modular NumPy arithmetic. Every determinant agrees and is nonzero; `verification.json` records them. No solver boolean is used as the final certificate.

The entries are reductions of the characteristic-zero bank entries at the established good primes, and no new node-root choices or denominators occur. Each nonzero minor therefore proves full rank over the number field and its algebraic closure. Thus no nonzero norm relation exists for any of these patterns. This is a fixed-minor specialization argument, not a modular ideal-inconsistency inference.

The census took0.55 seconds; the C++ gate1.08 seconds; independent replay2.16 seconds and35440 KiB, all under60-second/384-MiB guards. The shell-wrapped C++ watchdog does not reliably measure child RSS. No kernel inspection is needed because all matrices have trivial kernel.
