# Why norm-circle descent does not transfer the quadratic example to a prime field

This is a scoped obstruction to descending the existing fixed-gap construction, not an impossibility theorem for prime-field superlinear nearby-label examples. No new protocol or first-order claim is made.

## 1. The scalar-label obstruction survives every reparameterization

The existing construction has output length n=Theta(r) over E=F_(p²), where the descended nearest source contains r candidates on 4r prime-field coordinates. It supplies J=Omega(r²) labels in E. An actual affine line over F_p has only p labels (p+1 after projectivization). Consequently any prime-field version with n=Theta(r) and J/n unbounded must satisfy p/r unbounded. Replacing E by norm-circle parameters gives at most p+1 labels and does not remove this necessary condition.

The existing CRT orbit argument proves r unbounded, but permits p/r asymptotic to 4 or 8. In those cases *no* reparameterization preserving length Theta(r) can yield superlinearly many distinct F_p labels. This conclusion does not depend on whether the intended compiler uses conjugation, trace, norms, or rational coordinates.

## 2. Rational coordinate descent is blocked by three old fibers

**Lemma.** Let E/F be a finite Galois extension and let phi:P1_E→P1_E be a degree-e rational map. If more than 2e distinct F-rational points u satisfy phi(u)∈P1(F), then phi is defined over F.

For each sigma in Gal(E/F), write phi=[R:S] with coprime homogeneous degree-e forms. The homogeneous form `R S^sigma −R^sigma S` has degree2e and vanishes at all the stated points, including infinity under homogeneous evaluation. Thus it is zero, so phi=phi^sigma. The fixed rational function belongs to F(U).

**Corollary.** If three distinct F-valued source coordinates each have an entirely F-rational separable fiber under phi, then phi is defined over F. In particular no non-F source coordinate can have even one F-rational preimage.

Indeed the three fibers provide 3e distinct F-points, more than2e. The existing quadratic-extension padding includes coordinates outside F_p, whereas the retained core contains many coordinates in F_p. Therefore no rational-cover pullback of *any degree* can simultaneously split three old core fibers over F_p and turn the external padding coordinates into F_p coordinates. This is stronger than the familiar Möbius obstruction: a fractional linear transformation mapping three F_p points into F_p already belongs to PGL2(F_p).

This lemma concerns ordinary full-fiber RS pullback. A punctured cover that retains only a few F_p preimages is not excluded, but has to rebuild the agreement, nearestness, and fixed-rate/gap calculations. If even one F_p preimage is retained for each of N distinct old coordinates, a map not defined over F_p must have degree at least N/2. A small-degree rational change of coordinates therefore cannot perform that weaker descent either.

## 3. A norm circle changes the descent condition, not the field of the old core

Choose tau∈E with tau^p=−tau. The parametrization

`x(u)=(u+tau)/(u−tau), u∈P1(F_p)`

maps to the norm-one circle x^p=1/x. Its intersection with the original F_p-valued coordinate line is only {1,−1}. Hence it cannot contain the old core in this construction.

For degree-D polynomials P with F_p coefficients, clearing the denominator gives

`Q(u)=(u−tau)^D P((u+tau)/(u−tau))`.

Conjugation replaces P(x) by the reciprocal form `x^D P(1/x)`. Thus Q has F_p coefficients only if the appropriate reciprocal invariance holds (up to an allowed common scalar). Arbitrary prime-field nearest candidates do not satisfy this condition. Pairing a candidate with its conjugate and taking trace or norm changes the polynomial and the match conditions; agreement at only one member of a conjugate pair is not enough for a norm equality. Such pairing is not an agreement-preserving descent of the archived nearest list.

A new construction on a nonsplit torus, with an explicitly conjugation-compatible nearest bank, could avoid this coordinate obstruction. However, if its orbit length remains Theta(p), the scalar-label obstruction still prevents superlinear prime-field labels at length Theta(p). A short orbit or another source-compression theorem remains necessary.

## 4. Descending the received affine line itself

Write E=F_p+tau F_p. At fixed F_p coordinates, the trace of an E-line f0+lambda f1, with lambda=a+tau b, is

`Tr(f0)+a Tr(f1)+b Tr(tau f1)`.

Generically the last two vectors are independent, producing an affine plane, not an F_p affine line. Making them dependent collapses the parameter map to one F_p scalar, with fibers of size p. It gives no automatic superlinear label count: the ambient label bound is still p, and an arbitrary known nearby-label set may collapse heavily.

Similarly

`Norm(f0+lambda f1)=Norm(f0)+Tr(lambda f1 conjugate(f0))+Norm(lambda)Norm(f1)`.

Restricting lambda to a norm circle fixes the last term but leaves two trace-coordinate directions generically. A rational parametrization of the circle traces a rational conic in that plane rather than an affine line. The rank-one exceptional case still has only p scalar labels and does not cure the missing p/r separation.

There is a useful exact criterion for a projectively reparameterized line, before adding parameter-dependent codewords: its two-dimensional E-vector span must be Frobenius stable to admit an F_p form. In the archived construction, the direction vanishes on the old core while the intercept has a nonzero F_p core value. Frobenius stability would force `conjugate(f1)=a f1` and `conjugate(f0)−f0=b f1` for scalars a,b∈E. Independent random padding directions and intercept translations need not satisfy these common-phase constraints. Imposing them is a different compiler and requires a fresh diversity and nearest-boundary proof. If one also permits parameter-dependent codeword corrections, the relevant Frobenius-stability criterion is instead in the quotient by the RS code; the displayed common-phase conclusion is not asserted in that quotient. This potential additional freedom does not affect either the scalar-label bound or the coordinate-descent lemma.

## Concrete remaining positive targets

There are two mathematically substantive exits already compatible with an actual prime-field affine line:

1. Prove that a nearest Dickson candidate can have stabilizer d>2 along the rough-prime family, forcing p/r=4d+1/r to grow. This is the missing short-orbit lemma isolated in PRIME_RANDOM_DIRECTION_TRANSFER.md.
2. Construct an unbounded characteristic-zero nearest bank with a fixed linear nearest margin, permitting arbitrarily large splitting primes to be selected *after* fixing the source. CYCLOTOMIC_PRIME_TRANSFER.md then applies.

The norm-circle substitution by itself establishes neither. The new rational-map lemma shows precisely why direct coordinate descent of the existing mixed F_p/F_(p²) domain cannot be substituted for either missing source theorem.
