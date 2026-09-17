# The characteristic-41 seed has no mixed-characteristic DVR lift

September 17, 2026. A strengthening of the earlier obstruction modulo
41 squared. The argument handles every ramification index and every
residue-field extension. It concerns the exact selected incidence seed
from README.md, not arbitrary Dickson patterns or arbitrary codes.
A separate stdlib implementation checks the finite identities; the
valuation and coordinate-normalization arguments are given here.

## Precise conclusion

Let R be any mixed-characteristic discrete valuation ring with residue
characteristic 41. There do not exist 40 evaluation nodes and 20
polynomials of degree at most nine over R that reduce to the saved
characteristic-41 seed and satisfy all its selected agreement incidences.
Received values are unrestricted: they have already been eliminated by
equating incident polynomial values at each node.

In particular, this seed cannot be lifted to characteristic zero through
a finite ramified extension of the 41-adic field. This does not exclude
a characteristic-zero configuration with a different reduction or a
different incidence pattern. No uniform statement for all larger primes
is proved here.

## Normalizing the fourteen geometric freedoms

The original system has 260 equations in 240 variables: 40 nodes and
200 polynomial coefficients. Normalize three nodes to their canonical
integer values 1,2,3, all ten coefficients of the first polynomial to
their canonical values, and one coefficient of the second polynomial
to its canonical value. The last coefficient is chosen so that its
difference from the corresponding first-polynomial coefficient is
nonzero modulo 41. The certificate records the exact fourteen columns.

Every hypothetical lift can be put in this form without changing its
reduction or losing an incidence. There is a fractional linear map h,
reducing to the identity, that sends 1,2,3 to the lift's first three
nodes. Change node coordinates by h inverse and transform each message
polynomial by

    P(X) -> (cX+d)^9 P((aX+b)/(cX+d)).

The matrix of h has unit determinant and may be chosen to reduce to the
identity. All denominators at the nodes are units, and this operation
preserves degree at most nine and equality between candidates at nodes.
Next multiply all polynomials by a common unit to normalize the chosen
nonzero coefficient difference. Add one common degree-at-most-nine
polynomial to restore the entire first polynomial to its canonical
value. These operations also preserve all incidences and reductions.

Append the fourteen resulting linear coordinate equations to the
incidence equations. Call the integer polynomial system F and the
canonical integer seed z0. Every coordinate of F(z0) is divisible by p=41.

## Independently verified finite identities

Write J for the reduction modulo p of the Jacobian at z0, and write
Q(v) for the homogeneous quadratic part of F(z0+v), reduced modulo p.
There are now 274 equations and 240 variables.

The certificate and verifier establish:

1. J has rank 230. Ten saved independent vectors span ker J. Write
   v=Zt with t=(t0,...,t9).
2. Ten saved row vectors lambda_i annihilate J and satisfy

       lambda_i Q(Zt) = t_i^2+c_i*t_i*t9,  0<=i<9,
       lambda_9 Q(Zt) = t9^2,

   where (c0,...,c8)=(16,29,14,31,23,35,34,14,30) in F_41.
   Their common zero over any residue-field extension is t=0.
3. A further saved row vector lambda_* annihilates J and obeys

       lambda_* Q(Zt)=0 identically,
       lambda_* (-F(z0)/p)=8 mod41.

Thus lambda_* sees a nonzero constant obstruction but no quadratic
correction along the tangent space. The ten other combinations prevent
a nonzero tangent direction from having every quadratic correction zero.

The independent verifier reconstructs the nodes, binomial-formula
polynomials, incidences, Jacobian, and Taylor coefficients. It computes
rank 230 directly, checks the kernel basis and all eleven left-kernel
vectors, and checks all 605 quadratic coefficients. It also verifies
that the fourteen geometric infinitesimal motions preserve the original
equations and have rank fourteen on the chosen normalization coordinates. It does not import
the NumPy generator. The displayed forms and constant obstruction are
exact finite-field identities, not numerical approximations.

## Valuation proof excluding every ramification index

Suppose a normalized lift exists. Let pi be a uniformizer, let
e=v_pi(p)>=1, and write the lifted variables as z0+delta. If delta=0,
the constant obstruction already gives a contradiction. Otherwise let
r>=1 be the minimum valuation of its coordinates.

Lift the saved row vectors to integer representatives. Since they
annihilate J modulo p, each projected linear term has valuation at
least e+r. Taylor terms of degree at least three have valuation at
least 3r. The projected constant term for lambda_* has valuation
exactly e, because its residue after division by p is -8.

If 2r>e, that constant term is the unique lowest-valuation term in
lambda_* F(z0+delta), a contradiction.

In the remaining cases 2r<=e, one has r<e. Reducing the original
equations after dividing by pi^r shows that the nonzero leading vector
v=delta/pi^r modulo pi lies in ker J. Write v=Zt, with t nonzero.

If 2r<e, project onto each lambda_i and divide by pi^(2r). The
constant and linear terms vanish on reduction, as do all terms of
degree at least three. The ten displayed quadratic forms must all
vanish at t. First t9=0, then every t_i=0, a contradiction over any
residue-field extension.

If 2r=e, instead project onto lambda_*. The quadratic contribution
vanishes because v lies in ker J, but the constant contribution is
a nonzero residue times the unit p/pi^e. The linear and higher terms
have larger valuation. This is again a contradiction.

These three cases cover every positive pair of integers r,e. Thus no
normalized lift exists, and normalization excludes every original lift.

## Files and research consequence

* generate_ramified_obstruction.py: NumPy certificate generator.
* ramified_obstruction.json: kernel and row-vector certificates.
* verify_ramified_obstruction.py: independent stdlib reconstruction.
* ramified_obstruction_verification.json: exact verification report.

Both runs pass under the 384 MiB watchdog in about half a second each.
The new conclusion supersedes the earlier statement that ramified lifts
of this particular seed were still open. The characteristic-17 seed's
positive lifting result is unaffected. The desired growing fixed-gap
list remains unconstructed; a successful route must change this seed
or use a different construction.
