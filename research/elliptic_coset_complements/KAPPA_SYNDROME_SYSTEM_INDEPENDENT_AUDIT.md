# Independent audit: the specified-kappa syndrome system

Algebraic equivalence: PASS. Finite implementation receipt: pending at the time this section was written; any replay result is recorded separately below.

## Exact dimension and threshold ledger

For ell23 the torsion x-domain has n=(23^2−1)/2=264 points. The strict message dimension is k=n−4ell+1=173; the parity-check length is r=n−k=91. A union of two full fibers and five disjoint extra points has e=2ell+5=51 coordinates. Its complementary agreement size is n−e=213, the proposed threshold T. These are strict degree<173 messages, not degree<=173.

Let Phi be the squarefree domain locator. The parity-check column at x is

`h_x=(1,x,...,x^90)^T/Phi'(x)`.

Its kernel is exactly RS173: for every polynomial h of degree<173, the largest numerator exponent h(X)X^90 has degree<=262=n−2, so its sum divided by Phi'(x) vanishes; the91 check rows are independent by Vandermonde rank.

## Support recurrence is sufficient as well as necessary

For a monic support locator U=sum_(i=0)^51 u_i X^i, define the40×91 matrix R_U by

`(R_U s)_j=sum_(i=0)^51 u_i s_(i+j), 0<=j<=39`.

For every x in its support, R_U h_x=0. The51 parity-check columns on that support are independent, since51<=91. The40 recurrence rows are independent because the monic coefficient supplies distinct last nonzero positions51 through90. Therefore ker R_U has dimension51 and is exactly the syndrome space of errors on the chosen support.

Consequently a received word has a degree<173 witness agreeing outside this support if and only if its syndrome is killed by R_U. No assumptions about error values, nonzero errors at all support points, or canonical witness formulas are required. Agreements can exceed213 if some errors vanish.

For chosen labels kappa_i and supports U_i, a global received line has the specified witnesses exactly when its two syndrome vectors satisfy

`[R_(U_i), kappa_i R_(U_i)] (S0,S1)^T=0`

for every i. These are40 rows per support in182 unknowns. Full column rank forces S0=S1=0: the only surviving received coefficients are codewords. This excludes a nonzero syndrome pair for the tested finite supports and prescribed labels, hence any far-source common pencil with that precise assignment.

## Reparameterization and scope

An invertible projective change kappa'=(a kappa+b)/(c kappa+d) does not require a new rank calculation. In homogeneous coordinates the new equations are

`R_U[(c kappa+d)S0+(a kappa+b)S1]=0`.

The unknown-pair transformation is invertible when ad−bc!=0. Therefore rank is unchanged. A sample sent to infinity must retain its homogeneous equation; dropping it is not justified by this invariance.

This excludes only the specified assignment and its projective reparameterizations. It does not exclude an arbitrary new labeling of these supports, a smaller support subbank after rows are removed, a different prime or ell, or the asymptotic moving-quintic construction. A rank-deficient system would not by itself prove far endpoints or challenge injectivity.

## Actual finite certificate: independently replayed PASS

Rebuilt all25 saved supports from the actual elliptic group law, independently recomputed both isogeny tags by Vélu sums, rebuilt locators using ordinary modular polynomial multiplication, and checked the selected182 original rows by pure-Python reverse-column elimination. The rank is182. No producer imports or FLINT rank routines were used. The independent replay took about0.18 seconds. Files: `ell23_fixture/kappa_pencil/independent_replay.py` and `.json`.

Matrix SHA256: `6b7618ea3e29a81f9f4f46724ba77b119367a154c520efc104304ebbc7e4f2fb`.

- `verify.py`: `9d55beefc60b5248e1591c943390e8cf144efdbb02cf3d94f0301995cbb4d315`
- `selected_supports.json`: `c87ca694f92d843a11ba62894f397d1872450032b7a04a3663e2a3a5376c0f1b`
- `receipt.json`: `084bdaf0e8ce272d0880d57cb46dfea10baef17065dd10ff637cb3749b26b787`
- `independent_replay.py`: `45c285b7de7d92449e560c000a6aa435b4f1d2033418cf16d9bcf7229757b4a0`

The later structural note `TORSION_LIFT_DISJOINT_EXTRAS_LINEAR_BOUND.md` gives a stronger arbitrary-label O(n) count for this particular support family under a far-endpoint premise. It does not change the finite certificate, which rules out the whole prescribed kappa assignment without needing such a farness premise.
