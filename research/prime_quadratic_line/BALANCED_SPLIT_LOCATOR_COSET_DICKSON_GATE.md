# Balanced split locators: coset and Dickson gates

September 18, 2026. Purely algebraic bounded follow-up to the saved modular
cyclic-bank census. No field scan, parameter search, or paper edit.

The target is a squarefree split polynomial

```
F(X) = product_(x in S)(X-x) = X^e-Q(X),
deg Q <= 2,  |S|=e,  e=Theta(sqrt(p)),
```

over a growing sequence of prime fields. A nonconstant Q with all three
coefficients nonzero would generate a full coefficient-span multiplicative
orbit of quadratics agreeing with X^e at e points. No such growing family
is constructed here.

Two proposed sources are excluded in precisely stated models:

1. Multiplicative-coset root sets cannot produce the required full-coefficient
   Q. In fact, even one root coset of size at least three forces Q to be a
   monomial.
2. For `e>=7` and `p>2e+2`, **no nondegenerate Dickson fiber of either kind,
   even after an arbitrary Möbius change of roots and clearing its
   denominator**, has the form `X^e-Q(X)` with `deg Q<=2`.

The second statement covers every sufficiently large member of a balanced
sequence. It is an obstruction to this explicit source of split polynomials,
not to general sparse split locators.

## 1. A local coset obstruction

Let d>=3 divide p-1, and suppose the entire nonzero coset t*mu_d lies in S.
Write `u=t^d`, `e=hd+r`, `0<=r<d`. Then `X^d-u` divides F, so

```
Q(X) = u^h X^r  modulo (X^d-u).
```

The left side already has degree below d. The right side is the ordinary
remainder of X^e. Therefore r<=2 and the identity is an equality of
polynomials:

```
Q(X)=u^h X^r.
```

This rules out all-three-coefficient Q even when the other roots have
arbitrary structure. Unions of cosets of different subgroup orders do not
evade the statement if even one of their constituent cosets has size >=3.

For two-element cosets, write `Q=aX^2+bX+c` with a,b,c all nonzero.
If e is even, a pair x,-x of nonzero roots implies `2bx=0`, impossible.
If e is odd, such a pair implies `a*x^2+c=0`; hence there can be at most
one opposite pair. Consequently a root set consisting entirely of
two-element cosets cannot give a full-coefficient locator of degree e>=3.
Zero itself cannot be a root when c!=0.

There is also a shared-center affine version. If S is invariant under
`x -> h+zeta*(x-h)` for some zeta of order d>=2, its root sum is e*h.
For e>=4, the X^(e-1) coefficient of F vanishes. If p>e this forces h=0,
reducing to the multiplicative case. This includes an optional fixed root
at the center. It does not cover unions of cosets with different centers.

### Monomial residuals have only sqrt(p)-scale banks

If `Q=cX^j`, c!=0 and j in {0,1,2}, then

```
F=X^j*(X^(e-j)-c).
```

For j=2 this is not squarefree. For j=0, complete splitting requires
`e | p-1` and there are exactly `(p-1)/e` possible c. For j=1 it requires
`e-1 | p-1` and there are exactly `(p-1)/(e-1)` possible c. In the balanced
regime these banks have only O(sqrt(p)) members. Thus the coset mechanism
does not supply the requested super-sqrt(p) bank through its surviving
monomial cases.

## 2. A Möbius-transformed single coset is still insufficient

This closes a possible change-of-coordinates loophole for one complete
multiplicative coset. Assume e>=5 and p>e. Suppose an invertible Möbius
transformation of the roots of `T^e-beta`, beta!=0, gives a monic polynomial
of degree e having the form X^e-Q, deg Q<=2. Before normalization it is

```
(rX+s)^e - beta*(uX+v)^e,  rv-su != 0.
```

If r,u are both nonzero, put `h=s/r`, `k=v/u`, and
`R=beta*(u/r)^e`. Vanishing of the X^(e-1) and X^(e-2) coefficients gives

```
h=R*k,  h^2=R*k^2.
```

If one of h,k is zero, both are zero, contradicting invertibility.
Otherwise R=1 and h=k, again contradicting invertibility (and also
cancelling the leading coefficient). Hence one of r,u is zero.
In those cases the first missing coefficient forces the corresponding
other translation term to vanish, leaving only `X^e-constant` after
normalization.

This lemma concerns one coset. General Möbius images of arbitrary unions
of cosets are not classified here.

## 3. Dickson definitions and identities

Define the monic first- and second-kind polynomials by

```
D_0=2, D_1=T, D_e=T*D_(e-1)-alpha*D_(e-2),
E_0=1, E_1=T, E_e=T*E_(e-1)-alpha*E_(e-2).
```

The first-kind trace identity

```
D_e(u+alpha/u,alpha)=u^e+(alpha/u)^e
```

follows from the recurrence. This is the standard Dickson normalization;
first-kind Chebyshev polynomials are obtained by an affine scaling.
See [Bluher, Section 1](https://arxiv.org/html/1707.06877v2#S1) for this
normalization and the Chebyshev relation. The obstruction below is derived
here; it is not quoted from that paper.

For the second kind, the same recurrence gives

```
E_e(u+alpha/u,alpha)
 = [u^(e+1)-(alpha/u)^(e+1)]/[u-alpha/u].
```

With kappa=0 for D_e and kappa=1 for E_e, write y for the chosen polynomial.
It satisfies

```
L_kappa[y] := (T^2-4alpha)*y''+(2kappa+1)*T*y'
               -e(e+2kappa)*y = 0.                 (1)
```

For completeness, this follows directly from coefficients. The coefficient
of T^(e-2j) is

```
D: (-alpha)^j * e/(e-j) * binom(e-j,j),
E: (-alpha)^j * binom(e-j,j).
```

The ratio of successive coefficients c_j/c_(j-1) is

```
-alpha*(e-2j+2)*(e-2j+1) / [j*(e+kappa-j)].
```

Substitution in (1) cancels every coefficient. Under p>2e+2, all displayed
denominators used for this calculation are nonzero.

### Squarefreeness when alpha!=0

Both y=D_e and y=E_e have simple roots over the algebraic closure under
p>2e+2. For D_e, a root T=u+alpha/u gives
`u^(2e)=-alpha^e`. Thus `u^2!=alpha`, and differentiation of the trace
identity gives a nonzero derivative `2e*u^(e-1)` with respect to u.
The change T=u+alpha/u also has nonzero derivative, so y'(T)!=0.

For E_e, the branch points u^2=alpha are not roots: its value there is
`(e+1)*u^e`, which is nonzero. At any other root,
`u^(2(e+1))=alpha^(e+1)`, and the numerator derivative is
`2(e+1)*u^e`, again nonzero. This proves squarefreeness without assuming
that the roots lie in the base field.

## 4. Full Möbius obstruction for both Dickson kinds

**Proposition.** Let e>=7, p>2e+2, alpha!=0, and y be either polynomial in
Section 3. There are no constants beta, C!=0 and invertible matrix
`[[r,s],[u,v]]` such that the polynomial

```
F(X)=C*(uX+v)^e * [y((rX+s)/(uX+v))-beta]
```

is monic of degree e and has the form X^e-Q with deg Q<=2.

No splitting or squarefreeness assumption on the fiber y-beta is needed
for this proposition. It therefore excludes split fibers in particular.

### Affine case: u=0

After monic normalization, the coefficient of X^(e-1) is e*s/r, forcing
s=0. The next coefficient is `-e*alpha*(v/r)^2` for D_e and
`-(e-1)*alpha*(v/r)^2` for E_e. Its degree is e-2>2, so it too must vanish.
This forces alpha=0, a contradiction. This part already holds for e>=5
and p>e.

### Non-affine case: u!=0, v!=0

Put `Delta=rv-su`, `t0=r/u`, `h=s/v`. Then t0!=h. Inverse substitution

```
X=(vT-s)/(r-uT)
```

in the asserted sparse identity gives, for a nonzero scalar c,

```
y(T) = beta+c*(T-h)^e + (T-t0)^(e-2)*R_2(T),       (2)
deg R_2 <= 2.
```

Indeed, after multiplying the inverse substitution by `(r-uT)^e`, the
quadratic Q contributes a factor `(r-uT)^(e-2)` times a quadratic.

Let `y0=beta+c*(T-h)^e`. Since the differential operator in (1) has order
two, (2) implies that `L_kappa[y0]` vanishes to order at least e-4 at t0.
A direct calculation gives

```
L_kappa[y0]
 = c*e*(T-h)^(e-2)*(A*T+B)-e(e+2kappa)*beta,

A=(2e+2kappa-1)*h,
B=-(e+2kappa)*h^2-4(e-1)*alpha.
```

Differentiating gives

```
(L_kappa[y0])'
 = c*e*(T-h)^(e-3)
     *[(e-1)*A*T+(e-2)*B-A*h].                    (3)
```

This derivative vanishes to order at least e-5>=2 at t0. Since t0!=h,
the bracketed **linear polynomial** in (3) must have a double root, and
therefore must be identically zero. Its leading coefficient gives A=0.
The scalar `2e+2kappa-1` is nonzero because p>2e+2, so h=0. The constant
coefficient then gives B=0 and hence alpha=0, a contradiction.

### Non-affine inversion case: u!=0, v=0

Now invertibility gives s!=0. The inverse numerator `vT-s` is constant,
so the analogue of (2) says

```
y(T) = K + (T-t0)^(e-2)*R_2(T).
```

Applying (1) shows that the constant `-e(e+2kappa)*K` vanishes to order at
least e-4>=3. Thus K=0. This would give y a root of multiplicity at least
e-2, contradicting the squarefreeness proved above. All Möbius cases are
now covered.

## 5. Interpretation and exact scope

The familiar trace parametrization of a multiplicative or norm-one torus
produces first-kind fibers `D_e(T,alpha)=beta`. The proposition excludes
using any whole degree-e fiber of that form to produce the requested
high-coefficient cancellation, even after a projective change of the
evaluation coordinate. Compatible first-kind compositions give no escape:

```
D_r(D_s(T,alpha),alpha^s)=D_(rs)(T,alpha),
```

as follows at once from the trace identity. They are still included in
the same degree-e obstruction. The second-kind statement covers its whole
degree-e fibers as well.

If alpha=0, both kinds become T^e. Section 2 then reduces a transformed
fiber to a binomial, whose split constant bank has only `(p-1)/e` members.
Thus the degenerate case does not restore the intended growing-richness
mechanism.

The characteristic guard is essential. In the balanced regime e=Theta(sqrt(p))
it holds eventually; it does not cover Frobenius constructions whose
degree is comparable to p. In particular this note is not an obstruction
to the distinct Dickson/binomial high-degree construction recorded in
`../quartic_singular_route/DICKSON_CUBIC_ORDINARY_CORE.md`.

The proof deliberately does **not** classify:

- arbitrary subsets of roots or proper factors of higher-degree Dickson
  fibers;
- unions of multiplicative cosets with different affine centers, or
  general Möbius images of unions of several cosets;
- compositions with incompatible Dickson parameters;
- sparse split locators that are not obtained from these sources.

The e=5 and e=6 positive finite examples from the census are also outside
the e>=7 Möbius proposition, so no contradiction with them is implied.

The next gate is an explicit split-locator family outside the closed
coset/whole-Dickson-fiber models. No general impossibility statement for
nonconstant Q, no new sqrt(p)-agreement orbit, and no scalable computation
are supplied by these scoped obstructions.
