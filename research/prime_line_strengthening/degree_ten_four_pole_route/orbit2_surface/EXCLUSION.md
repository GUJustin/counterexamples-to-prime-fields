# Complete orbit2 uniform degree-ten exclusion

The characteristic-zero orbit2 seven-cubic bank is defined over
K=Q(q), q^3-10q^2+3q+1=0. Use the archived affine chart whose reduction
at q=4 above 83 is `quadratic_one_pole_route/orbit2_bank83.json`.
The chosen prime is good: the fourteen base points remain distinct and
the defining cubic has simple root 4 modulo 83. For its seven
four-agreement points Q and seven three-agreement points T, consider
weighted polynomials of degree at most 34 and Y degree at most 10,
with prescribed plane multiplicities 4 at Q and 6 at T.

**Theorem.** This net has no integral member with rational normalization
in characteristic zero. It also contains no nonzero pure power G^t for
any t dividing 10 with t>1. Consequently a proper uniform degree-ten
four-pole augmentation whose primitive norm has these caps and contacts
cannot arise from this bank. This does not exclude arbitrary eight-word
constructions or other degree-ten incidence patterns.

## 1. Exact net and good reduction

There are exactly 217 Hasse equations and 220 columns. The saved
217-by-217 unit minor, independently computed as an exact integer
determinant and equal to 3 modulo 83 (`kernel_unit_minor.json`), proves
exact rank 217 over K, not merely a modular
rank lower bound. Over the DVR at q=4 above 83, solve the pivot variables
by this unit square matrix. Taking the three free variables as the
standard basis gives an integral kernel basis reducing to the saved
modular basis. There are no additional rows whose vanishing would need
a lifting assertion. This gives the exact relative net without needing
to print its large characteristic-zero coefficients.

## 2. Complete base and rank-one-locus audit

`profile.py/json` and `finish_profile.py` prove that the fourteen
prescribed points are the entire base locus and are resolved by one
blowup each. The two resultants, divided by the forced degree-364 base
coordinate factor, have gcd one. All fourteen specialized ordinate
gcds are exactly the prescribed power of the one known linear factor;
thus removing the forced factor hides no other point in the same fiber.
The leading-Y and infinity restrictions have gcd one, including the
projective corner. Each tangent-cone triple has rank three and no common
projective direction. The boundary restriction coefficient matrices also
have rank three.

On the resolved surface S, L is basepoint-free, with

    L^2=16, K.L=12, c2(S)=18, p_a(L)=15.

These statements extend over the DVR by the properness of the closed
relative base locus. The rank-three tangent checks show that NO member
can jump its base multiplicity at any of the fourteen points. In
particular, an integral original member stays an integral member of L;
there is no exceptional-component endpoint to handle.

The affine jet-minor gcd is one. On each exceptional curve the map is a
nonconstant basepoint-free map of degree 4 or 6. The two original boundary
maps are nonconstant of degree at most 4 and 10. These degrees are below
83, so every restriction is generically separable. Jet rank is therefore
at least two at the generic point of every boundary divisor. The global
rank-one jet locus is finite; rank zero is impossible.

## 3. Residual discriminant and its integral model

The universal jet incidence has expected codimension three. Its
pushforward is an effective discriminant cycle of degree

    c2(J1 L)=18+2*12+3*16=90.

This is a cycle computation, without assuming nodality. The determinant
is the product of the seven old graphs and one remaining irreducible
factor Gamma. Each old graph has multiplicity one in the determinant.
`old_graph_degrees.py/json` gives its two normal quartics after removing
27 forced intersection orders. Every pair is coprime of maximum degree
four, so its separable map to the old-factor parameter line has degree
four. The seven old lines contribute 28 in total, leaving an effective
cycle of degree 62.

Gamma has bidegree (76,21), 986 terms, and smooth rational point (1,75)
with gradient (64,11). Its irreducibility over F83 plus that smooth point
proves geometric irreducibility. Sampling over F83[r]/(r^3-r-3) supplies
4,102 distinct certified images. A standard-library tuple verifier checks
every source equation, all 12,306 jet-kernel equations, and rank two at
every source point. Full degree-62 interpolation, without assumed
symmetry, has rank 2,015 on its 2,016 homogeneous columns. Its unique
relation H has 1,990 terms, and is checked at all 4,102 images.

The image has degree at most 62 from the effective cycle. Since
4,102>62^2, Bezout forces every degree-62 relation through the points to
contain the image. If the image degree were smaller, all degree-62
multiples of its equation would form a vector space of dimension greater
than one, contrary to the computed kernel. Thus H is exactly the reduced
image equation of degree 62 and consumes the entire residual cycle.
There are no additional components or multiplicities.

On the smooth relative surface times the parameter plane, the three jet
equations together with the uniformizer form a regular sequence, because
the special fiber has expected dimension. The incidence is flat over
the DVR. Proper pushforward of fundamental cycles commutes with
specialization. Subtract the seven horizontal old-line contributions.
The primitive equation of the residual degree-62 divisor therefore
reduces to H up to a nonzero scalar. This is the required characteristic-
zero identification; no claim is based on merely lifting sampled points.

## 4. The necessary multiplicity is absent everywhere

If an original member were integral rational, its resolved member would
also be integral rational, and its total delta would be p_a(L)=15.
A generic pencil through it, with the other section avoiding its finitely
many singularities, has smooth local total spaces. The local discriminant
intersection multiplicities are the characteristic-zero Milnor numbers,
whose sum is at least 15. This proves discriminant multiplicity at least
15 at the parameter. The parameter is off every old-factor line, since
those represent reducible original members; the residual divisor also
has multiplicity at least 15 there.

`hasse_basis.json` records a full-rank 2,016-row basis extracted from the
first 2,560 degree-bounded multiples of Hasse derivatives of orders below
15. `hasse_multiplicity_gate.json` records an explicit affine identity

    1 = sum constants * b^i c^j * Hasse_(db,dc) H(1,b,c).

On a=0,c=1 there is a separate univariate Bezout identity equal to 1,
using restrictions of all relevant Hasse derivatives, including a
derivatives. The final point [0:1:0] has multiplicity zero. The standalone
`verify_hasse_gate.py` replays the two identities by coefficient summation
only, with no elimination or row reduction, in 1.36 seconds.

Therefore the entire geometric projective multiplicity-15 locus is
empty over F83. This locus is closed in the proper relative parameter
plane; its geometric generic fiber is also empty. A characteristic-zero
parameter specializing onto an old-factor line would still satisfy the
closed residual multiplicity condition, so there is no lost boundary.
This contradicts the necessary condition and proves the theorem's
integral-member assertion.

## 5. All nonprimitive norm-power branches

For t=2,5,10, a hypothetical G^t in this net would have

    degY G <=10/t, wt_(1,3) G <= floor(34/t),
    contacts >=ceil(4/t) on Q and >=ceil(6/t) on T.

The Hasse matrices have respectively shapes 63x63, 28x12, and 14x5.
They have full column rank modulo 83, with selected maximal minors
67,49,31. `nonprimitive_norm_gate.json` records original selected rows;
`verify_nonprimitive_norm_gate.py` independently rebuilds the Hasse
entries and computes exact integer Bareiss determinants before reducing
modulo 83. Its receipt is `nonprimitive_norm_gate.verified.json`.
The unit minors exclude the corresponding exact kernels over K.

This covers every nonbirational intermediate degree dividing ten, without
assuming the declared four-pole allowance is attained. To apply this to
an augmentation, use its primitive norm equation: properness and
regularity on the separable selected fibers preserve the required
contacts under primitive clearing, and norm transitivity gives a pure
power of the irreducible image equation. The weighted cap must hold as
in the stated uniform construction. No assertion about an arbitrary
nonproper resultant with extraneous factors is used.

## Computational bounds and reproducibility

Profile: 0.56s, a few MiB. Sample: 9.17s,41MiB. Independent source replay:
3.28s,27MiB. Full interpolation:5.91s,198MiB. The first repeated-batch Hasse
implementation retained excessive allocator memory and was stopped by
the384MiB guard; it was not used as a final certificate. Splitting basis
selection and one linear solve into fresh processes completed in1.61s/
171MiB and2.18s/148MiB. The saved unit identities, not any failed pilot,
are the final exclusion certificates. No rental was used.
