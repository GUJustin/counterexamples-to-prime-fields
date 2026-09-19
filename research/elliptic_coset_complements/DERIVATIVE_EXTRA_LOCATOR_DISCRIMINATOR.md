# Variable extra locators: a bounded derivative discriminator

September 18, 2026. No scan, rental, or manuscript edit.

**Outcome.** No split family or proximity-gap theorem was obtained. Variable
proper residues of degree at most five remain far and cannot supply freely
moving poles on a fixed received line. Domain-cancelled logarithmic derivatives
give sparse error markers, not codewords. For the concrete received pair
\(f=\Phi'\), \(g=\Phi''\), a scaled logarithmic-derivative ansatz nevertheless
has an exact, small algebraic acceptance test: for each pair of full fibers
and each \(0\le d\le5\), at most \(d+1\) labels survive its first \(d+2\)
moment equations. The remaining equations, split-domain roots, and endpoint
farness are unproved. No finite label scan is justified by this reduction alone.

## Setup

Use the elliptic domain \(\mathcal D\), monic locator \(\Phi\), and
\[
n=(\ell^2-1)/2,\qquad k=n-4\ell+1,\qquad
R=n-k=4\ell-1,\qquad T=n-2\ell-5,\qquad \ell\ge23.
\]
For a subgroup \(H\) and two distinct tags \(a,b\), put
\[
L_0=(N_H-aB_H)(N_H-bB_H),\qquad \deg L_0=2\ell.
\]
An admissible extra locator is monic \(J\mid\Phi\), of degree \(d\le5\),
coprime to \(L_0\). Thus \(U=L_0J\) is squarefree, splits on the actual
domain, and has degree \(u=2\ell+d\).

For the derivative/Newton test assume characteristic \(p>n\). This is
automatic for full rational \(\ell\)-torsion over the **prime field**:
\(\ell^2\le\#E(\mathbb F_p)\le2p+1\) gives \(p\ge n\), and
\(n=(\ell^2-1)/2\) is a composite multiple of four. For extension-field
domains, \(p>n\) must be imposed separately.

## 1. Varying a small proper-residue denominator does not repair farness

For any \(J\mid\Phi\) of degree \(d\le5\), a word equal to \(A/J\) away
from \(Z(J)\), with \(\deg A<d\) and \(A\ne0\), has agreement at most
\[
k+2d-1<T
\]
with the degree-\(<k\) code, regardless of the assigned values at its
poles. Indeed \(A-Jh\) is a nonzero polynomial of degree at most \(k+d-1\);
at most \(d\) omitted coordinates can be added. Adding a codeword changes
neither the argument nor the agreement maximum. This bound holds pointwise
even when the reduced \(J\) varies with the challenge.
The zero rational term is excluded: a word supported only at its assigned
exceptional coordinates can of course be close to the zero codeword.

There is also an exact moving-pole restriction. Suppose three distinct
parameters of a fixed received line have representations modulo code as
proper reduced residues \(A_i/J_i\), \(\deg J_i\le d\), away from their
domain poles. Take an affine relation among the three parameters and clear
the squarefree union denominator \(Q\), of degree \(m\le3d\). The resulting
polynomial has degree at most \(k+m-1\) and vanishes at \(n-m\) coordinates.
Since \(4\ell>2m\), it is identically zero. The proper rational terms then
have an exact affine relation, and the polynomial codeword part vanishes.

Consequently, after two parameters are fixed, every further reduced residue
lies on their **rational-function** affine line. All poles lie in the union
of those first two pole sets, of size at most \(2d\). A pole can cancel at
at most one parameter. If the union has more than \(d\) points, there are
at most \(2d\) admissible parameters; otherwise the denominator is fixed
apart from at most \(d\) cancellation parameters. This is a bounded-pole
statement, not a restriction on arbitrary high-degree rational sources.

## 2. Multiplying by the domain locator produces errors

For any squarefree divisor \(U\mid\Phi\),
\[
E_U(X):=\Phi(X)\frac{U'(X)}{U(X)}
       =\frac{\Phi(X)}{U(X)}U'(X)
\]
is a polynomial, with evaluation word
\[
E_U(x)=
\begin{cases}
\Phi'(x),&U(x)=0,\\
0,&U(x)\ne0.
\end{cases}
\]
The values on \(Z(U)\) are nonzero. Thus this operation converts logarithmic
residues into exact supported errors; it does not automatically give a
degree-\(<k\) explanation. Appending an extra factor gives the exact identity
\[
E_{L_0J}=E_{L_0}+E_J.
\]

In particular, suppose a received word already has a canonical witness
whose exact error support is \(Z(L_0)\). Any other codeword whose error
support is contained in \(Z(L_0)\cup Z(J)\) must be the same codeword:
their difference has weight at most \(2\ell+5<4\ell\), the code's minimum
distance. Hence the appended extra positions have zero actual error and
are padding. A nonzero \(E_J\) cannot be absorbed into a codeword in this way.
This closes only the same-pair append operation, not witnesses on a new
base pair or general coordinate-dependent error values.

## 3. A concrete fixed source pair and its exact polynomial test

Take the actual received polynomials
\[
f=\Phi',\qquad g=\Phi'',\qquad w_\lambda=f+\lambda g.
\]
Their syndrome span has dimension two: its first two coordinates are
\((n,P_1)\) for \(f\) and \((0,n(n-1))\) for \(g\), where
\(P_1=\sum_{x\in\mathcal D}x\). Both displayed nonzero scalars are invertible.
This does **not** prove either source is far at \(T\).

Test the explicitly restricted error ansatz
\[
e_U=\gamma E_U,\qquad U=L_0J.
\]
It supplies a valid witness exactly when
\[
\boxed{\quad
h=\Phi'+\lambda\Phi''-\gamma\frac{\Phi}{U}U'
\quad\hbox{has degree }<k.\quad} \tag{1}
\]
The leading coefficient forces
\[
\gamma=n/u.
\]
Thus the unscaled unit-residue choice \(\gamma=1\) fails immediately:
\(n-u\ne0\). If (1) holds with \(\gamma=n/u\), its exact agreement is
\(n-u=n-2\ell-d\ge T\), since every entry of the error on \(Z(U)\) is
nonzero. This is an exact witness check, including the absence of artificial
extra roots.

## 4. Newton identities predict \(J\) and give a degree-six gate

Let
\[
P_j=\sum_{x\in\mathcal D}x^j,\qquad
Q_j=\sum_{L_0(x)=0}x^j,\qquad P_0=n,\quad Q_0=2\ell.
\]
The syndrome-generating rational functions of \(f\) and \(g\) are
\(\Phi'/\Phi\) and \(\Phi''/\Phi\), respectively. The latter's moments are
\[
H_0=0,\qquad
H_j=\sum_{i=0}^{j-1}P_iP_{j-1-i}-jP_{j-1}
\quad(j\ge1),
\]
because \(\Phi''/\Phi=(\Phi'/\Phi)'+(\Phi'/\Phi)^2\).
In particular \(H_1=n(n-1)\).

The first \(R\) syndrome equations for (1) require the extra-root power sums
to equal
\[
m_j(\lambda)=\frac un(P_j+\lambda H_j)-Q_j,
\qquad 1\le j\le R-1. \tag{2}
\]
The zeroth equation has already fixed \(\gamma\), and gives the correct
extra-root count \(d\).

For fixed \(H,a,b,d\), the first \(d\) equations uniquely determine the monic
polynomial
\[
J_\lambda(X)=X^d+c_1(\lambda)X^{d-1}+\cdots+c_d(\lambda)
\]
by Newton identities; \(\deg c_i\le i\). Put \(A=u(n-1)\ne0\), the
coefficient of \(\lambda\) in \(m_1\). Then
\[
[\lambda^i]c_i=\frac{(-A)^i}{i!}.
\]
The next necessary Newton recurrence is the polynomial equation
\[
F_{d+1}(\lambda):=
m_{d+1}+c_1m_d+\cdots+c_dm_1=0. \tag{3}
\]
For \(d\ge1\), its leading coefficient is
\[
\boxed{\quad
[\lambda^{d+1}]F_{d+1}
=\frac{(-1)^d A^{d+1}}{d!}\ne0.\quad}
\]
Only \(c_dm_1\) reaches that degree; the prescribed \(m_j\)'s are affine
in \(\lambda\). For \(d=0\), (3) means \(m_1=0\), a nonzero linear
equation with coefficient \(A\).

Thus there are at most \(d+1\le6\) candidate labels for a fixed pair and
fixed \(d\), at most \(21\) across \(d=0,\ldots,5\). These are only
**candidates**. One must still require \(J_\lambda\mid\Phi\),
\(\gcd(J_\lambda,L_0)=1\), and every remaining moment in (2), or equivalently
the direct polynomial degree test (1). Those conditions imply split,
distinct domain roots; a formal Newton polynomial alone does not.

## Scope and decision

The degree-six discriminator is specific to the \(\Phi',\Phi''\) pencil and
the scalar-\(\Phi'\) error values. It leaves room for
\(O((\ell+1)\binom t2)=O(n^{3/2})\) distinct labels across all base pairs;
it is **not** a linear-count theorem or a closure of the variable-extra-set
target. No subgroup-compatible family making these Newton polynomials split
and satisfy the remaining moments was found. Endpoint/common-agreement
separation for this pencil was not proved either.

The arbitrary-error quintic recurrence in
[FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md](FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md)
therefore remains the general target. The KKH outsider divisor identity
supplies no missing identity here: its monomial high-band cancellation is
absent, and logarithmic differentiation alone does not replace it.
This bounded assessment stops at the exact discriminator, without a
parameter scan or a claim that dimension or formal locators give a
construction.
