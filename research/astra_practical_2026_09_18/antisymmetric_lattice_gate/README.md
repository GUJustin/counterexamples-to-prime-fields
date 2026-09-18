# Antisymmetric modular exchanges: verified, insufficient for the benchmark

This bounded September 18 pilot produces actual characteristic-specific subset exchanges on the KoalaBear 256th roots of unity. It does **not** improve the better.codes certificate or its guaranteed family size.

For p = 2130706433 and zeta = 392596362, use coefficients d_j in {-1,0,1}, with d_0 = 0 and d_(j+128) = -d_j. The three equations sum_j d_j zeta^(kj) = 0 for k = 1,3,5 imply all six required moment equations; the even equations vanish by antisymmetry. Even support ensures equal products. The positive and negative supports therefore give disjoint equal-cardinality exchanges preserving the six leading coefficients and root product.

The rank-127 integer kernel has determinant p^3. LLL and BKZ20 found no usable ternary relation. A BKZ40 checkpoint found an odd-support ternary relation; combining its signed rotations produced 14 even-support relations in seven rotation/swap orbits. The smallest exchanges have 54 roots on each side and change partial mu4-packet patterns. Their cyclotomic norm is nonzero, with p-adic valuation three, confirming these are modular rather than characteristic-zero identities.

`verify.py` independently checks the lattice determinant and kernel, every moment, disjointness, product equality, exclusions, and the exact rotation-orbit collision ledger. Run it with Python and python-flint installed. Inputs, intermediate bases, and exact results are included.

The seven orbits' total contribution to ordered collisions of 136-subsets is

    695965748775730753157757982387225324465954440.

This is only about 2^(-158.829) of the sufficient off-diagonal second-moment threshold for a fiber of size 274980728111395088. This calculation is a limitation of the found exchanges and this counting argument, not an upper bound on actual fibers. Counting more transformations as independent witnesses without proving distinctness and compatibility would be invalid.

The two bounded reduction runs used 59.49 seconds and at most 58992 KiB sampled resident memory. BKZ50 was stopped at the time limit; no BKZ50 result is claimed. No rental was used. Further reduction is paused pending a credible amplification argument.
