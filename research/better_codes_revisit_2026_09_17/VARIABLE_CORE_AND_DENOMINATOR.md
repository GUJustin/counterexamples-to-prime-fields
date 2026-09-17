# Variable cores and alternative denominators: degree-band obstruction

This follows the archived heterogeneous, partial-fiber, fixed-core, and
coefficient-lane reviews. No improved counting construction was found.
The following extension addresses moving the distinguished fiber or
its omitted point, while allowing arbitrary scalar normalization.

## Lemma

Let Fp be a subfield of E. Fix a polynomial T, integers B,h,k,c with
0<=c<B, and fixed polynomials F0,F1 over E. Suppose distinct parameters
gamma satisfy identities

    F0+gamma F1-T P_gamma = lambda_gamma R_gamma(X) V_gamma(X^B),

where lambda_gamma is nonzero, deg P_gamma<k, R_gamma is monic of
degree c with coefficients in Fp, and V_gamma is monic of degree h.
Assume

    deg T+k-1 < Bh.

If there are more than p parameters, every R_gamma is the same polynomial.

Proof. Let D=Bh+c. The coefficient at X^D gives
lambda_gamma=a+b gamma for fixed a,b. For each j=1,...,c, the
coefficient at X^(D-j) is precisely lambda_gamma times the coefficient
r_(c-j)(gamma) of R_gamma: the next monomial block from V_gamma
starts at degree D-B, strictly below Bh. The same coefficient receives
no contribution from T P_gamma by the degree hypothesis. Hence

    r_(c-j)(gamma)=(a_j+b_j gamma)/(a+b gamma).

The denominator is nonzero on the parameter set. A fractional linear
function is constant or injective. Since its values lie in Fp and there
are more than p parameters, it must be constant. This holds for every
coefficient of R_gamma, proving the claim.

## Exact parameters

For the closest failed certificate, B=1024,h=136,k=131072,c=1023.
The condition holds for every common denominator of degree at most8192:

    8192+131072-1=139263 < Bh=139264.

In particular it holds for the pinned degree2048 denominator. Therefore
moving the core among different base-field fibers, changing its omitted
point, or replacing it by any other monic degree1023 base-field root
polynomial cannot combine product classes on one such line with the
required roughly2^58 parameters. A core can vary only by leaving at
least one hypothesis: changing the error-factor shape, allowing its
coefficients outside Fp, increasing its degree past the separated block,
or changing the denominator/degree regime sufficiently.

## Extra-root and denominator possibilities left open

An extra factor whose roots are outside Fp need not have base-field
coefficients, so the lemma does not exclude it. However, appending a
fixed factor to a known identity adds its degree to the witness and
error polynomials together; it supplies no free degree reduction.
If the same factor is put in a common numerator and denominator, it
cancels algebraically and likewise changes no degree tradeoff.

To obtain a genuinely new construction, a varying factor must make
the whole residual numerator divisible by a larger common denominator
while retaining one affine parameter and enough choices of supports.
No such divisibility identity or family count has been established.
Treating the additional factor's choices as free would omit precisely
this missing condition.

A denominator with nonzero constant term escapes the earlier
root-product-at-zero lemma. It also loses the established automatic
divisibility at zero provided by a common product. A replacement must
prove another common remainder or interpolation relation. Counting
five product classes without supplying that relation does not define
a polynomial witness.

The exact obstruction above is restricted to the stated polynomial
identity. It does not exclude arbitrary received lines, identities
wrapping modulo X^n-1, support-dependent denominators, or extra factors
with extension-field coefficients. Those are unresolved alternatives,
not certified improvements.
