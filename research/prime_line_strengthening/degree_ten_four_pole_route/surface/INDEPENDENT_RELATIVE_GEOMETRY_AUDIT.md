# Independent relative-geometry audit: PASS

Reviewed `RELATIVE_DISCRIMINANT_AUDIT.md` and
`../paley_net_rational_exclusion.tex`, using the independently replayed
arithmetic certificates as inputs. No identity computation was repeated.
The proposition's precise scope—no integral rational member of this
uniform Paley net in characteristic zero—is supported. No further
mathematical correction is required in the reviewed argument.

## Expected codimension really gives relative flatness

The special ambient S_k times P²_k is regular of dimension4. Three local
components of the universal jet section generate the incidence ideal.
Basepoint-freeness excludes rank0. Rank2 occurs on a divisor and gives
one parameter, while rank1 occurs at finitely many surface points and
gives a parameter line. Thus the zero set has dimension at most1.
Krull's height theorem prevents a minimal prime of an ideal with three
generators from having height greater than3. Hence all minimal primes
have height exactly3. In the Cohen--Macaulay regular ambient the three
generators form a regular sequence, and there are no embedded components
of a different dimension.

The total relative ambient has dimension5. Adding the uniformizer to
the three equations gives height4. These four elements form a regular
sequence; permuting a complete-intersection system shows that the
uniformizer is a nonzerodivisor after imposing the three jet equations.
The incidence is therefore flat over the DVR. This is more than a
dimension-count heuristic, and justifies specializing its fundamental
cycle. Proper pushforward then commutes with specialization.

The global rank1 guard is essential. The affine gcd alone would not
suffice. The separate nonconstant, degree-below29 restrictions on every
boundary and exceptional divisor supply exactly the missing argument:
their tangential differential is generically nonzero, so the full jet
rank there is at least2.

## The residual degree62 divisor specializes correctly

The jet Chern calculation is90 using L²14, KL14 and c2=20. The seven
old-graph components each have simple determinant order and a separable
degree4 normal Gauss map, so they contribute exactly28 in both fibers.
The resolved incidence is flat, and these seven horizontal parameter
lines are individually identified over the DVR. Subtracting their fourfold
contributions leaves an effective horizontal divisor of degree62.

On P² over a DVR an effective codimension-one horizontal cycle is Cartier
and has a primitive homogeneous equation. Equivalently the degree90
equation divides by the product of the seven primitive linear equations
to the fourth power; the quotient is integral and primitive. The special
residual cycle is exhausted by the absolutely irreducible degree62 image,
with multiplicity1, so its equation reduces to the reconstructed H up to
a nonzero scalar. There is no unaccounted vertical factor or hidden
positive-degree rank1 image component in this conclusion.

## Integral original members and F1

At the fourteen prescribed points the rank3 leading-jet map prevents
any nonzero combination from increasing the fixed multiplicity. At the
two simple basepoints its kernel is exactly the parameter of F1, and
the exact support plus nonzero quadratic coefficient gives order exactly2.
Thus the only possible exceptional contribution of an original integral
member is the sum of those two exceptional curves, each with coefficient1.

In that case the strict transform is still integral with rational
normalization, and each exceptional component is rational. The resolved
divisor is reduced; double tangency to an exceptional curve does not
make that component nonreduced. Each exceptional curve meets the strict
transform, so connectedness is also retained. The normalization formula
gives sum(delta)=15+k-1 for k components. This step correctly avoids
silently treating the resolved F1 divisor as integral.

## Discriminant multiplicity and specialization

For a reduced divisor on a smooth characteristic-zero surface, singular
points are isolated. A generic second member of a basepoint-free net
is nonzero at all of them. The resulting pencil has locally smooth total
space, with parameter function equal to a defining equation divided by
a unit. The local critical-scheme length is the Milnor number. Its
contribution to the pushed jet-incidence divisor along the pencil is
therefore mu, including for reducible local singularities.

The identities mu=2delta-r+1 and delta>=r-1 give mu>=delta. A generic
line through the member also computes the ordinary multiplicity of the
parameter discriminant divisor. Consequently an original integral
rational member has full discriminant multiplicity at least15. It lies
off every old-factor line, so the residual equation has the same local
multiplicity there.

Finally, all Hasse jets of orders below15 define a closed relative
multiplicity locus, regardless of whether their characteristic-zero
parameter specializes onto an old-factor line. The locus is projective
over the DVR. If it had a geometric generic point, properness (after a
finite extension) would produce a geometric special point. The explicit
affine and boundary identities exclude the entire geometric special
fiber. This is the valid transfer argument; it does not infer a
characteristic-zero statement merely from testing rational F29 points.

## Scope retained

The conclusion concerns integral rational members of this specific net.
Reducible members exist, and no assertion is made about other incidence
patterns, other banks, or arbitrary degree-ten/four-pole constructions.
