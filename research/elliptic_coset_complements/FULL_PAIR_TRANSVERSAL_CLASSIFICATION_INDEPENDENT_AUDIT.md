# Full-pair transversals for one elliptic quotient: independent audit

September 18, 2026. **PASS, with exact full-support and full-pair hypotheses.**
This is a proof audit, with no scan or manuscript edit. It classifies a
two-dimensional syndrome plane meeting **every** two-fiber error space for one
fixed subgroup. It does not classify an arbitrary large subbank, witnesses with
additional omissions, or received planes with one-dimensional syndrome image.

**Current-status update:** [TWO_FIBER_LINEAR_RESOURCE_BOUND.md](TWO_FIBER_LINEAR_RESOURCE_BOUND.md) now gives an O(n) label bound even for arbitrary partial selections of pairs and partial coordinate support, assuming a far endpoint. The full-pair classification below remains valid with its original hypotheses; it is no longer the broadest route restriction. Extra omissions remain outside the linear bound.

## Statement and notation

Use the setup of [FIXED_SUBGROUP_QUOTIENT_PLANES.md](FIXED_SUBGROUP_QUOTIENT_PLANES.md).
Thus \(\ell\ge 11\) is an odd prime, all \(\ell\)-torsion is rational, and
\[
t=(\ell-1)/2,\qquad n=(\ell^2-1)/2,\qquad
k=n-4\ell+1,\qquad R=n-k=4\ell-1.
\]
The code is \(\operatorname{RS}_k(\mathcal D)\), meaning polynomial degree \(<k\).
For the fixed order-\(\ell\) subgroup suppress its subscript, and write
\[
B=K^2,\quad Y=N/B,\quad
F_i=N-a_iB,\quad \mathcal D_i=\{x:F_i(x)=0\},\quad
\Phi=K\prod_{i=1}^t F_i.
\]
The distinct tags are \(a_1,\ldots,a_t\). Each \(\mathcal D_i\) has \(\ell\)
distinct points, the fibers and kernel coordinates are disjoint, and \(N,B\)
are coprime. In particular \(B\) and \(K\) do not vanish on a full fiber.

Let \(\mathsf H\) be the parity-check map with columns
\[
\mathsf h_x=\frac{(1,x,\ldots,x^{R-1})^{\mathsf T}}{\Phi'(x)},
\qquad
S_i=\operatorname{span}\{\mathsf h_x:x\in\mathcal D_i\}.
\]
Every set of at most \(R\) columns is independent. Let \(L\) be a
two-dimensional subspace of syndrome space. Assume that for **each** \(i<j\)
there is a nonzero vector \(s_{ij}\in L\) represented by an error vector whose
support is **exactly** \(\mathcal D_i\cup\mathcal D_j\).

Define
\[
C=KB^{t-4}.
\]
For a tag function \(z:\{a_1,\ldots,a_t\}\longrightarrow\mathbb F_p\), let
\(w_z\) be the word which is zero on the kernel coordinates and equals
\(C(x)z(a_i)\) on \(\mathcal D_i\). Set
\[
V_H=\mathsf H\{w_z:z\text{ is any tag function}\}.
\]
Then
\[
\boxed{\dim V_H=3,\qquad L\subseteq V_H.}
\]
The linear-algebra proof below already works for \(t=4\), provided the displayed
squarefree fiber factorization, code parameters, and degree identities hold.
For the stated prime-order elliptic setup the first applicable case is
\(\ell=11,t=5\).

## 1. Pair intersections and coherent local directions

Any three spaces \(S_i,S_j,S_h\) have direct sum: their \(3\ell\) defining
columns are independent since \(3\ell\le R\). Therefore
\[
(S_i+S_j)\cap(S_i+S_h)=S_i.
\]
The plane \(L\) cannot be contained in \(S_i+S_j\). Otherwise an exact
two-fiber representative for the pair \(\{i,h\}\), with \(h\ne i,j\), would
have syndrome in \(S_i\), forcing its component on \(\mathcal D_h\) to vanish.
Representation on \(\mathcal D_i\cup\mathcal D_h\) is unique, so this
contradicts exact support. It follows that
\[
\dim\bigl(L\cap(S_i+S_j)\bigr)=1
\]
for every pair. No separate exclusion of a two-dimensional intersection is
needed under the hypotheses.

For a triangle \(i,j,h\), the three projective points
\([s_{ij}],[s_{ih}],[s_{jh}]\) are pairwise distinct. An equality, for example
between the first two, would again put the common syndrome in \(S_i\), contrary
to full support. Three distinct points of a projective line have a dependence
in which all three coefficients are nonzero. Decomposing this dependence in
the direct sum \(S_i\oplus S_j\oplus S_h\) shows that the two nonzero local
components at vertex \(i\) are proportional.

Applying this to every triangle gives fixed one-dimensional spaces
\(\langle v_i\rangle\subset S_i\) such that
\[
s_{ij}\in\operatorname{span}(v_i,v_j)
\]
with both coefficients nonzero. Each \(v_i\) has a unique error representative
on \(\mathcal D_i\), nonzero at every point of that fiber. Any three \(v_i\)'s
are independent.

For every triple, two of its edge syndromes span \(L\), so
\[
L\subseteq\operatorname{span}(v_i,v_j,v_h).
\]
Put \(W=\operatorname{span}(v_1,v_2,v_3)\). If some \(v_h\notin W\), then
\[
L\subseteq W\cap\operatorname{span}(v_1,v_2,v_h)
 =\operatorname{span}(v_1,v_2).
\]
This contradicts the nonzero \(v_3\)-component of \(s_{13}\in L\). Thus all
\(v_i\) lie in the same three-dimensional space \(W\).

## 2. The four-fiber MDS relation fixes the error weights

Choose any four distinct indices \(I\). Their \(v_i\)'s have one relation up
to scale, with every coefficient nonzero. The resulting error vector is a
nonzero vector in the kernel of \(\mathsf H\) supported on the \(4\ell=R+1\)
coordinates of those four fibers.

Let
\[
Q_I(X)=\prod_{i\in I}F_i(X).
\]
The parity-check matrix on those coordinates has one-dimensional kernel,
spanned by
\[
e_I(x)=\frac{\Phi'(x)}{Q_I'(x)}.
\]
Indeed, for \(0\le j\le 4\ell-2=R-1\), Lagrange interpolation gives
\[
\sum_{Q_I(x)=0}\frac{x^j}{Q_I'(x)}=0.
\]
All displayed values are nonzero, since the factors are squarefree and
disjoint. Thus the unique local error representative of \(v_i\), for
\(i\in I\), is proportional on its fiber to \(e_I\).

For \(x\in\mathcal D_i\), one has \(N(x)=a_iB(x)\), and hence
\[
Q_I'(x)=F_i'(x)B(x)^3
             \prod_{j\in I\setminus\{i\}}(a_i-a_j),
\]
whereas
\[
\Phi'(x)=K(x)F_i'(x)B(x)^{t-1}
             \prod_{j\ne i}(a_i-a_j).
\]
Consequently
\[
\frac{\Phi'(x)}{Q_I'(x)}
=C(x)\,
\frac{\prod_{j\ne i}(a_i-a_j)}
     {\prod_{j\in I\setminus\{i\}}(a_i-a_j)}.
\]
The second factor is a nonzero scalar depending on the tag and chosen four
fibers, not on the point within a fiber. Every \(i\) belongs to some such
four-set, so all local error directions are exactly \(C\) on their respective
fibers, up to nonzero scalar. Therefore \(W\subseteq V_H\) and \(L\subseteq V_H\).

## 3. Exact dimension and the advertised quotient basis

The space of words \(w_z\) has dimension \(t\), because \(C\) is nonzero on
each full fiber. If \(P\) is a polynomial with \(\deg P\le t-4\), the tag
function \(z(a)=P(a)\) gives the polynomial word
\[
w_z=KB^{t-4}P(N/B)
\]
on the entire domain, including its assigned zero values on the kernel.
Its degree is at most
\[
t+(t-4)\ell=n-4\ell=k-1.
\]
These \(t-3\) independent tag functions are therefore in the kernel of the
syndrome map. Hence \(\dim V_H\le3\). Conversely the \(C\)-weighted indicator
words of any three fibers have independent syndromes, by independence of
the \(3\ell\) parity-check columns. Thus \(\dim V_H=3\), with no further
kernel directions.

Interpolation on the \(t\) distinct tags identifies its quotient basis as
\[
e_j(x)=C(x)Y(x)^{\,t-3+j},\quad j=0,1,2,
\]
off the kernel, with all three words defined to be zero on the kernel. In
rational notation,
\[
e_j=\frac{N^{\,t-3+j}}{K^{\,2j+1}},
\]
and their degree at infinity is \(k+j\). These rational formulas have genuine
kernel poles; their values there are the specified zero extensions. The
syndromes of the three words, not the rational functions evaluated at poles,
are the basis of \(V_H\).

## Scope and degeneracies

- Full support is used to rule out pair-plane containment, coincident triangle
  labels, and zero local components. None is silently assumed away.
- The elliptic setup supplies simple fiber roots, distinct tags, and coprime
  \(N,B\). Kernel multiplicity two in \(B=K^2\) causes no division by zero on
  a full fiber; kernel word values are always assigned separately.
- The classification allows collisions between disjoint pairs. It does not
  assert \(\binom t2\) distinct challenges or any source/common-agreement
  bound.
- The hypothesis concerns every pair for this subgroup at redundancy
  \(4\ell-1\). It does not exclude a large partial collection, extra error
  coordinates, or a different code dimension.
- Combined with a **separate** proof that
  \(\dim(V_H\cap V_{H'})\le1\), it excludes one two-dimensional syndrome plane
  realizing both complete, exact-support pair banks. That cross-subgroup
  bound is not needed or reproved in this audit.
