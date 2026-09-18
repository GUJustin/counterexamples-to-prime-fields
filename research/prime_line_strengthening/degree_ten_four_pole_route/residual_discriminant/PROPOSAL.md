# An algebraic parameter-locus gate for the Paley net

This is a proposed exact computation, not a completed exclusion or a new
rational member. It targets parameters over the algebraic closure, rather
than enumerating the rational points of the parameter plane.

## Necessary condition on an explicit open chart

Write the three-dimensional norm kernel as
`F=a F0+b F1+c F2`. Its coefficient of `Y^j` has X-degree at most
`34-3j`. Consequently the Y-discriminant has X-degree at most342 and is
homogeneous of parameter degree18. The fourteen prescribed singularities
force the divisor

    T(X)=product_quad (X-x)^12 product_triple (X-x)^30,
    deg T=294.

One can establish this divisibility first on the dense open set of ordinary
prescribed points, where it follows by factoring the local smooth branches,
and then as a polynomial identity in the parameters. Define `D=Disc_Y(F)/T`;
its X-degree is at most48.

Consider irreducible members satisfying these open conditions:

1. The Y-leading coefficient B has degree4, is squarefree, is nonzero at
   all fourteen selected X values, and is coprime to the coefficient of Y9.
2. The weighted polynomial at X=infinity has degree10 and ten distinct
   roots.
3. At each selected point the Y-multiplicity is exactly the prescribed
   multiplicity m=4 or6. The desired realization moreover has m distinct
   smooth branches, each unramified over X. Their tangents may coincide.

The first two conditions ensure degree342 for the original discriminant,
degree48 for D, and no ramification over X=infinity. At a zero of B the
Y=infinity branch is also smooth and X-unramified: in the q=1/Y chart the
equation starts `B(X)+C(X)q`, with B' and C both nonzero. Its contribution
to the polynomial discriminant is zero. Thus all discriminant orders come
from ordinary finite Y charts, where

    ord Disc = different contribution + 2*local normalization index.

For a rational normalization, Riemann--Hurwitz gives total different18.
At each prescribed point the index is at least binomial(m,2); removing T
subtracts exactly twice these147 forced units of index. Therefore

    sum finite residual index = (48-18)/2 =15.

At a residual root with index k and different contribution r the residual
discriminant order is 2k+r. Its contribution to gcd(D,D') is at least k.
In characteristic zero this proves the necessary condition

    degree gcd_X(D,D') >=15.                         (*)

This also holds in characteristic29 for a separable irreducible rational
member on this chart: the degree10 cover is tame, and differentiation of
a polynomial can only increase the gcd contribution if a multiplicity is
divisible by29. No equality of discriminant index and geometric genus is
being assumed without the displayed boundary hypotheses.

The conditions excluded above are explicit parameter curves, not disposable
exceptions. A complete rational-locus calculation must analyze them as
separate strata. In particular, a negative result after saturation by the
open guards is not a global exclusion.

## Bounded first job

`reconstruct.sage.py` reconstructs D on the chart a=1 over F29 using190
triangular evaluations, sufficient for total parameter degree18. These
evaluations reconstruct every coefficient exactly; they are not a
finite-field candidate census. Each evaluation computes a univariate-in-Y
discriminant over F29[X], divides by T exactly, and saves its receipt.
Two-variable falling-factorial interpolation then outputs all49 coefficient
polynomials in the two parameters. Thus the resulting polynomial describes
the entire chart over the algebraic closure of F29.

Suggested first rental budget: one Sage process,600 seconds,2GiB actual
RSS; start with `--max-evaluations 5` for a pilot. The JSON checkpoint makes
the190-evaluation run resumable. Do not launch subresultant elimination
until the reconstruction size and time are measured.

Next algebraic target, if reconstruction is modest: compute the ideal of
the first15 principal subresultant coefficients of `(D,D_X)`, saturate by
the displayed open guards and by the degree48 coefficient, and determine
its dimension. Over a field, vanishing of these coefficients is equivalent
to (*). The exact subresultant indexing must be verified against the CAS
convention. A zero-dimensional result yields algebraic parameter candidates;
factor each specialized member and normalize its integral components.
Positive-dimensional output requires a geometric explanation before any
larger normalization job. A modular empty locus alone does not prove an
empty characteristic-zero locus: any claimed transfer needs an integral
ideal-membership certificate and control of the chosen chart/guards.

The bicanonical pencil provides no immediate smaller test: its restriction
to a target curve has degree24, so rationality does not contradict that
map. It is useful for subsequent normalization, but it does not presently
replace the concrete discriminant condition.
