# A displaced spherical boundary improves both moment certificates

September16, 2026. Self-reviewed proof with separate exact raw-moment and
Cartesian-integration checks. No novelty or global optimality claim.

The strongest selected certificates now give:

- Prime-alphabet LIST, n157/k63/t68: **28169451256663519418** words,
  excess greater than **34.09967 bits**.
- Quartic-extension LINE, same interval parameters: source class
  **508108952862977950462384886**, giving
  **508108952659354448051620618** distinct labels and excess greater than
  **50.90955 bits**. Common agreement is63 and concurrency is at most18.
- The quadratic-extension label bank is137466243406665308.

The prime is p=2^31-1. These remain ordinary RS examples on{0,...,156},
using the stated alphabets. The pinned better.codes score is unchanged.

## Tilt the first factor of the radial weight

Use the already verified smoothed normalized coordinates X in dimension
d=4 for the list, or d=3 for the extension line. Put s=|x|^2. The baseline
radial weight is

    w0(s)=-product_(j=1)^7(s-r_j),   0<r1<...<r7.

Let l(s)=product_(j=2)^7(s-r_j), r=r1, and choose a rational vector v. Use

    w(x)=l(|x|^2)*(r-|x|^2+v.x).

This has coordinate degree14. Its first zero surface is the sphere

    |x-v/2|^2 = r+|v|^2/4.

The selected vectors are

    d4: (-644265078293/20000000000000, 0,
         -654309208103/20000000000000, 0),
    d3: (-2398622154541/100000000000000, 0,
         -2563556360181/100000000000000).

The exact inequality |v|^2*r2<(r2-r)^2 puts the displaced ball strictly
inside the sphere of squared radius r2. Consequently the positive set is
the displaced first ball together with the unchanged outer radial annuli.
The odd term(v.x)*l(s) integrates to zero on each origin-centered annulus.
Only the first ball's integral changes.

## The expectation uses existing directional moments

The degree14 data already verify identities

    |x|^(2j+2)=sum_a w_(a,j)*(a.x)^(2j+2),   0<=j<=6.

Differentiate with respect to x_i and cancel2j+2:

    x_i*|x|^(2j)=sum_a w_(a,j)*a_i*(a.x)^(2j+1).

Thus every required E[X_i*s^j] follows from the already counted odd scalar
moments. No further subset counting is needed. If l(s)=sum l_j*s^j, then

    E[w]=E[w0]+sum_i v_i sum_j l_j E[X_i*s^j].

Reflection of the interval makes the unused odd-degree Gram coordinates
vanish in this expression. Numerical optimization only proposes v; the
selected expectation is computed with exact fractions.

## Exact displaced-ball integral

Write a=v/2, A=|a|^2, R=r+A and x=y+a. On the displaced ball,

    w(y+a)=(R-|y|^2)*l(|y+a|^2),    |y|^2<R.

For z=|y|^2, the angular average of a monomial in the shifted norm is

    average_theta |y+a|^(2j)
      =sum_(h=0)^floor(j/2) binomial(j,2h)
         *(2h)!/[h!*(d/2)_h] * A^h*z^h*(z+A)^(j-2h).

Here(u)_h=u(u+1)...(u+h-1), with(u)_0=1. This follows by expanding
(z+A+2a.y)^j and using the sphere's even coordinate moments; odd terms
integrate to zero.

The remaining radial integral is elementary:

    integral_0^R (R-z)*z^(k+d/2-1) dz
      =R^(k+d/2+1)/[(k+d/2)(k+d/2+1)].

The sphere factor is pi^2 in dimension4 and2*pi in dimension3. Dimension4
therefore gives a rational integral before the pi bound. Dimension3 needs
only sqrt(R), bounded by rational intervals. Replace the baseline first
ball's integral by this new value, keeping the other annuli unchanged.

The usual smoothed-lattice density bound then gives the stated integer
source class. The 4D gain over the radial baseline is about0.0140150%;
the 3D source gain is about0.00825172%. These exceed the earlier quartic
angular perturbations, which remain valid historical certificates.

## Separate checks and scope

The independent verifier reconstructs the expectation directly from the
raw subset moments and a separate cube-noise expansion. It expands
l(|y+a|^2) in Cartesian monomials and integrates each even monomial over
the ball, without using the producer's angular-average polynomial.
Different Machin pi bounds, exact sphere nesting, entropy/Elias comparisons,
and the extension-line collision partition all pass. The independently
guaranteed integers equal both claimed source classes.

Producer: certify_tilted_radial_boundary.py.
Separate verifier: verify_tilted_radial_boundary.py.
Certificates: tilted_radial4d_boundary_verification.json and
tilted_radial3d_boundary_verification.json, with corresponding
independent_verification.json files.

The search also tested rational translations of the entire radial weight
and a conservative angular-variance bound for one tilted boundary. Those
candidates are weaker and were superseded before promotion. Their files
remain marked pending separate verification. Only the displaced-boundary
certificates above are the final verified refinements.
