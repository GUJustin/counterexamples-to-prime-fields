# Bounded challenge degree, including a moving monic derivative coefficient

September17,2026. Extension of the triangular proof; awaiting independent
review of this extension. The root agent read the original PROOF.md in
full and found its recurrence, resultant split, component-incidence count,
and low-branch three-label argument sound in its initial audit. This is a
local mathematical review, not formal verification or a novelty claim.

## General statement

Let D>=1 and char(F)=0 or p>D. Consider

    T(X,z) P' -P²+R(X,z)P-S(X,z)=0, deg P<=D.

Assume T is MONIC in X of degree t>2D, with deg_z T<=a_T;
deg_X R<=t-2, deg_z R<=a_R; and deg_X S<=t+D-1,
deg_z S<=b. Here a_T,a_R,b are fixed nonnegative integers. Put

    a=max(a_T,a_R), K=b+(D-1)a,
    Bdeg=max(a_R,K), Adeg=max(2K,a_R+K,a_T+K,b),
    Cdeg=max(a_T+K,b).

Zero polynomials obey every displayed degree cap. The actual solution
locus is parameterized by z and c=P(0), and lies in a plane equation
monic quadratic in c with z-degree at most

    E=max(a_R,Cdeg).

The nonconstant message coefficient a_j(z) has degree at most
b+(D-j)a, hence at most K. The same triangular recurrence works because
the coefficient of a_j remains the nonzero constant j: monicity in X
makes the leading derivative coefficient independent of z. Challenge
variation in lower coefficients adds at most a to each recursive degree.

After substitution the constant-X equation is

    -c²+R_0(z)c+T_0(z)a_1(z)-S_0(z)=0,

and every nonconstant-X equation is B_i(z)c+A_i(z)=0, with the above
Bdeg,Adeg bounds. Terms TQ' cost at most a_T+K, RP costs at most a_R+K,
and Q² costs at most2K.

The isolated challenge-label count is at most

    I=max(Adeg,
          2Adeg, a_R+Adeg+Bdeg, Cdeg+2Bdeg,
          Adeg+Bdeg, Bdeg).

Redundant entries are retained to identify their source: a c-independent
residual, the three quadratic-resultant terms, a pair determinant, and
exceptional roots of B_i. Thus I=O_{a_T,a_R,b}(D).

There are at most two reduced horizontal curve components, with summed
bidegrees bounded by(E,2). For any received LINE on n distinct points,
agreement A>D, put L=max(K,1). The exact same incidence proof gives full
common witnesses outside at most

    I+n(E+2L)/(A-D)+2n

labels. This is O_{a_T,a_R,b,eta}(n) when A-D>=eta*n and D<=n.
The constants are independent of t and the actual X degrees below its
specified bounds. No regularity or separant assumption is used.

## What this adds, and what it does not

This includes moving derivative coefficients T(X,z), arbitrary bounded
challenge degree in R and S, and arbitrary evaluation domains unrelated
to the roots of T. It therefore describes a leading-X triangular class,
not only the two-branch construction. The proof still counts actual
nearby solutions; it does not infer proximity from formal solution counts.

It excludes terms of X-degree t-1 in R, which can introduce a z-dependent
pivot j+R_(t-1)(z). It also excludes a nonconstant leading-X coefficient
of T. Those cases produce denominators and require a separate degree
accounting argument. The condition t>2D prevents P² from entering the
coefficient equations used for triangular elimination. A generic
first-order interpolant need not satisfy any of these restrictions.

The fixed challenge-degree assumption matters: substituting bounds that
grow with inverse gap or n changes the constants and may erase a claimed
uniform linear bound. Likewise this result only applies to candidates
satisfying this one polynomial identity. It does not supply such an
identity for every received line.

## Subsequent extension

`SHARED_DENOMINATORS.md` now proves the following extension with explicit
bounds; the paragraph below records why shared accounting is essential.

If a leading pivot is a nonzero polynomial in z of bounded degree, one
may discard its roots and work over F(z). The recurrence denominators
then accumulate across D stages. Their product has degree O(D), but
naively clearing every coefficient separately can create O(D²) degree.
A shared-denominator recurrence may preserve O(D) total degree. That
would include deg_X R=t-1 and nonmonic moving T, substantially widening
the class. The shared-denominator proof is supplied in that separate note.
