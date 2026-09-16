# Independent referee review: balanced Galois rational maps

## Verdict

The theorem in `../structured_domains/GALOIS_BALANCED_FIBERS.md` is
correct as stated. Its hypotheses `n>=3`, `char(F)>n`, `mu_n subset F`,
full degree-sized fibers, and geometric Galoisness suffice. The
arithmetic and geometric Galois assumptions are equivalent under these
hypotheses. The projected twist condition is essential; replacing it
by a nonsquare condition on the raw reflection parameter is incorrect.

## Stabilizer audit

If `g(X)=(aX+b)/(cX+d)` permutes `mu_n`, its denominator has no zero
there, and

\[
(aX+b)^n-(cX+d)^n=\lambda(X^n-1),\qquad\lambda\ne0.
\]

The left side cannot be identically zero: that would make the
nonconstant rational function `g` satisfy `g^n=1`. Its degree is at
most `n`; its `n` distinct zeros prove the identity and, in particular,
rule out cancellation of its leading degree.

All intermediate binomial coefficients are nonzero because `p>n`.
If all four matrix entries are nonzero, the coefficients at exponents
one and two imply `a/b=c/d`, violating the nonzero determinant.
When one entry vanishes, an intermediate coefficient forces its
opposite entry to vanish. Thus `g=zeta X` or `g=zeta/X`, with
`zeta in mu_n`. For `n=3`, the two necessary intermediate coefficients
still exist; the resulting six maps comprise the full `S_3` action.
This argument is over the algebraic closure, so it excludes additional
geometric stabilizers, not merely additional `F`-rational ones.

## Deck transformations and descent

Every fiber over `R(mu_n)` already contains `B=deg(R)` distinct
points. A rational map's geometric fibers have total multiplicity
`B`, so these fibers contain neither further points nor ramification
nor the point at infinity. Every geometric deck transformation
therefore preserves the entire domain.

Consequently the geometric deck group lies in the above dihedral
stabilizer. Since `mu_n subset F`, all those stabilizer maps are
defined over `F`. An equivalent descent argument uses the images of
three distinct `F`-rational domain points. Geometric Galoisness gives
`B` deck maps, hence `B` distinct arithmetic automorphisms, proving
arithmetic Galoisness. The converse follows because the arithmetic
maps remain distinct and the rational-map degree is unchanged after
extending constants.

The assumption that the domain lies in `F` matters for that equivalence.
For example, take `F=F_7`, `n=B=4`, `R=X^4`, and take `mu_4` only in
the algebraic closure. The map is balanced on that geometric domain and
the geometric extension is Galois. Its arithmetic extension has only
two deck maps, `X` and `-X`, because `F_7` has only two fourth roots of
unity. It is not Galois of degree four. This example satisfies `p>n`.

## Quotient fields and the precise twist

Let the deck group's rotations have order `d`. If there are no
reflections, `B=d` and the invariant field is `F(X^d)`.
Otherwise choose one reflection `X -> alpha/X`; the group has order
`B=2d`, and with `c=alpha^d` its invariant field is

\[
F(X^d+c/X^d).
\]

The displayed invariant has exact rational degree `2d`, matching the
group order, so there is no hidden proper extension in this step.
The map `R` is a generator of the same rational function field and
therefore differs from that invariant by an output Möbius map over `F`.

Rotations act freely on the nonzero domain. Some reflection fixes `x`
if and only if

\[
(x^d)^2=c.
\]

Since `x^d` ranges over `mu_N`, `N=n/d`, every orbit has the full
size `2d` exactly when `c` is a nonsquare **in the cyclic group
`mu_N`**. In particular, `N` must be even. This is not a statement
about quadratic residuosity in the whole field.

Raw-parameter counterexample: in `F_7`, take `n=6`, `d=2`, and
`alpha=3`. The element `3` is nonsquare in `mu_6=F_7^*`, but the
deck subgroup also contains the reflection `4/X`, fixing `2` and `5`.
The projected twist is `c=3^2=2` in `mu_3`; all elements of `mu_3`
are squares there. Accordingly `X^2+2/X^2` fails full four-point
balance on `mu_6`. The theorem's condition rejects this example.

## Boundary and converse checks

- `B=1`: every admissible Möbius map is included as `h(X)`.
- `n=3`: the stabilizer proof is valid. Divisibility restricts balanced
  degrees to one and three; the nontrivial Galois case is cyclic.
- `M=n/B=1`: both cyclic and dihedral cases can occur. For example,
  `R=X^n` is constant with value one on the domain. If `n=2d`, the
  dihedral invariant `X^d-X^{-d}` is constant with value zero there;
  its rational degree is `2d=n`, and all `n` points in that fiber
  are simple. Thus the one-fiber case must not be excluded.
- Converse: cyclic quotient fibers have `d` points on the domain;
  the nonsquare projected twist pairs the `mu_N` values without fixed
  points and therefore produces `2d`-point fibers. An output Möbius
  map preserves these fiber sizes. Its pole must avoid the image if
  the theorem requires finite values on the domain.
- There is no classification of arbitrary rational maps here.
  The earlier balanced cubic over `F_13` has four simple critical
  points, whereas a Galois degree-three cover is cyclic and has two
  totally ramified points. It falls outside the Galois subclass.

## Related pullback statement

The note's output-Möbius Reed--Solomon equivalence is also valid.
If `h(U)=(aU+b)/(cU+d)` has no pole on the evaluation set, multiplying
each coordinate by `(cU+d)^(k-1)` converts evaluations of
degree-`<k` polynomials on `h(E)` into those of degree-`<k` polynomials
on `E`. The polynomial-space transformation is invertible by the
homogeneous action of the invertible matrix defining `h`. Every
coordinate multiplier is nonzero, so Hamming distances and lists are
preserved. This does not imply invariance of a particular combinatorial
coefficient-signature construction.

`verify_galois_boundaries.py` records exact small-field checks for the
three-point stabilizer, the projected-twist counterexample, one-fiber
dihedral behavior, and the arithmetic/geometric distinction. The
structured_domains agent independently checks larger collections of
stabilizers and free actions.
