# Lattès Schwarzians: the two-tag ratio loses its tags

2026-09-19. One symbolic candidate test; no curve, label, or locator scan.

**Outcome.** The Schwarzian of the natural two-fiber ratio is independent
of both tags. Its domain-regularized high-degree word is an exact marker
of the subgroup's fixed kernel, with universal values proportional to
`Phi'(x)²`. The global multiplication-map Schwarzian gives the sum of
these markers. Thus this identity supplies a genuine high-degree global
word, but its isogeny factorizations do not supply a second common word
or a moving quintic locator. This is a scoped test of this Lattès
identity, not an exclusion of other division-polynomial or higher-jet
pencils.

## 1. The differential identity and its common part

Let the prime-field elliptic curve be `E:y²=F(X)=X³+AX+B`, with
characteristic `p>3`, and let odd prime `ell>=23` differ from `p`.
Use the rational full-torsion domain and coding parameters from
`FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md`:

\[
 \mathcal D=x(E[\ell]\setminus\{O\}),\quad
 n=(\ell^2-1)/2,\quad k=n-4\ell+1,\quad T=n-2\ell-5.
\]

Write `Phi` for the monic domain locator and, for an order-`ell`
subgroup `H`, write the normalized isogeny as

\[
 Y_H=N_H/K_H^2,\qquad \deg K_H=t=(\ell-1)/2.
\]

Its quotient curve has cubic `F_H`. The exact invariant-differential
identity already verified in `ISOGENY_WRONSKIAN_MOVING_EXTRA_TEST.md` is

\[
 F(X)Y_H'(X)^2=F_H(Y_H(X)).
\tag{1}
\]

For any separable rational function `Y`, define

\[
 \mathcal S(Y)=\frac{Y'''}{Y'}-
       \frac32\left(\frac{Y''}{Y'}\right)^2,
 \qquad
 C_F=\frac{3F'^2-4FF''}{8F^2}.
\]

Differentiating (1) gives
`2FY_H''+F'Y_H'=F_H'(Y_H)`. Differentiating once more, or directly
substituting the logarithmic derivative of (1), proves

\[
 \boxed{\quad
 \mathcal S(Y_H)=C_F-Y_H'^2 C_{F_H}(Y_H).
 \quad}
\tag{2}
\]

No analytic uniformization is needed in positive characteristic.
All divisions here are identities of rational functions; `Y_H'` is
nonzero because the isogeny is separable. Formula (2) has also been
checked by formal symbolic elimination in the accompanying verifier.

The subgroup-independent, renormalized expression
`S(Y_H)+Y_H'^2 C_FH(Y_H)` is therefore just the **single** rational
function `C_F`. Its numerator has degree at most four and its
denominator has degree six, with poles only at two-torsion x-values.
Those poles miss the odd-torsion domain. In particular this common
part is not a new high-degree received pencil. It has at most `k+5`
matches with any degree-`<k` polynomial: after multiplication by
`F²`, the residual is nonzero and has degree at most `k+5`.
Nonzeroness follows from its double poles at the simple roots of `F`.
Since `k+5<T` for `ell>=23`, this single common word is far at the
target threshold.

## 2. The two omitted fibers disappear from the Schwarzian

For distinct quotient tags `a,b`, the two-fiber ratio is

\[
 R_{H,a,b}=
 \frac{N_H-aK_H^2}{N_H-bK_H^2}
 =\frac{Y_H-a}{Y_H-b}.
\]

A fractional linear map has zero Schwarzian, and the differentiation
chain rule gives

\[
 \boxed{\quad
 \mathcal S(R_{H,a,b})=\mathcal S(Y_H).
 \quad}
\tag{3}
\]

This can also be checked directly from the three derivatives of
`(Y−a)/(Y−b)`. Thus (3) forgets `a` and `b` exactly, not just in its
highest coefficients. In particular the apparent poles on the
`b`-fiber are simple poles of the fractional linear map and cancel
from its Schwarzian. Neither omitted fiber creates a domain pole or
a moving extra-root condition through (3).

## 3. Keeping the high-degree residue gives fixed kernel markers

To retain high-degree torsion data rather than just the bounded-pole
common term in (2), consider the received word obtained by evaluating

\[
 W_H=\Phi^2\mathcal S(Y_H)
\]

at the domain, using removable values at kernel points. This rational
function may still have poles **off** the domain; it is not asserted
to be a code polynomial.

At a nonkernel domain coordinate, both the point and its isogeny image
are nonzero odd-order torsion points. The map `Y_H` is finite there
and its derivative is nonzero, so its Schwarzian is regular. Hence
`W_H` has value zero there. At a kernel coordinate `q`, the map has
a pole of order two. Writing `u=X−q` gives

\[
 Y_H=\alpha u^{-2}+\beta u^{-1}+O(1),\qquad \alpha\ne0,
\]
\[
 \mathcal S(Y_H)=-\frac{3}{2u^2}
                  +\frac{3\beta}{2\alpha u}+O(1).
\]

As `Phi=Phi'(q)u+O(u²)`, the exact evaluation word is

\[
 \boxed{\quad
 W_H(x)=-\frac32\Phi'(x)^2\,1_{\{K_H(x)=0\}}.
 \quad}
\tag{4}
\]

All these nonzero weights are independent of the tags. The full
marker has `t>=11` domain positions; selecting at most five of them
would require a separate choice, not a locator provided by the
Schwarzian identity. This statement does not classify arbitrary
errors supported on two tag fibers plus chosen kernel positions.

Let `R_ell(X)=x([ell]P)`, where `X=x(P)`, be the common multiplication
map. It has a pole of order two at every domain point. Therefore the
same calculation gives the genuinely global high-degree word

\[
 W_{\rm all}:=\Phi^2\mathcal S(R_\ell)|_{\mathcal D}
 =-\frac32\Phi'^2|_{\mathcal D}.
\tag{5}
\]

For any factorization `[ell]=dual(phi_H) o phi_H`, the Schwarzian
chain rule decomposes (5) into (4) and its complementary marker on
the nonkernel points. Indeed the first summand is (4), while their
sum is (5). Every nonzero torsion point belongs to a unique subgroup
of order `ell`, so the kernel x-sets partition the domain and

\[
 W_{\rm all}=\sum_H W_H.
\tag{6}
\]

Equations (3)--(6) supply one global word and subgroup-indexed
coordinate masks. They supply no tag-dependent recurrence for
`L0=(N_H−aK_H²)(N_H−bK_H²)` and no reduced moving divisor `J` of
degree at most five in the exact quintic target.

## 4. What the marker identities can and cannot compile

The marker words for distinct subgroups have disjoint supports, and
each has exactly `t` nonzero coordinates. Any nontrivial combination
of three of them has weight at most `3t<4ell`, below the minimum
distance of the dimension-`k` code. Their syndrome vectors are
therefore linearly independent. Consequently a two-dimensional
syndrome plane contains at most two of these distinct marker points.

A pencil generated modulo code by two marker words has all its words
supported modulo code on their union of size at most `2t=ell−1`.
Every parameter then has agreement at least `n−ell+1>T`, so that
marker-only pencil has no far endpoints. This is not a claim about
arbitrary pencils containing `W_all` or about other independently
chosen high-degree words.

The exact moving-quintic equations in
`FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md` remain the acceptance criterion.
This candidate fails to generate their pair-dependent information:
the ratio Schwarzian erases the two tags, the common connection term
has fixed low-degree poles, and the retained high-degree pieces are
fixed subgroup masks. Other Laurent coefficients, differential
combinations not reduced to (2)--(5), and arbitrary error values are
not excluded. No new scan is justified by the identities proved here.
