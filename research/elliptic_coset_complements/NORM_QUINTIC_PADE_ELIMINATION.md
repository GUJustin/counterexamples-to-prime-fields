# Norm-quintic Padé elimination and the torsion 3/7 specialization

2026-09-19. Exact algebraic reduction; no generic-rank assumption.
The explicit norm-label fixture is excluded by an exact finite certificate.
The particular torsion 3/7 support family also has a stronger, all-label
linear bound described below. The general moving norm-quintic system is
not solved.

Use the notation of FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md:
\[
 n=(\ell^2-1)/2,\quad k=n-4\ell+1,\quad R=4\ell-1,\quad
 T=n-2\ell-5,\qquad \ell\ge23.
\]
The elliptic curve is \(y^2=F(X)=X^3+aX+b\), in characteristic greater
than three and different from \(\ell\). For a subgroup \(H\), write
\(Y_H=N_H/B_H\), \(B_H=K_H^2\).
The syndrome of a word has coordinates
\[
 s_j=\sum_{x\in\mathcal D}\frac{w(x)x^j}{\Phi'(x)},\qquad 0\le j<R.
\]
The same two syndromes \(s_f,s_g\) must be used for every subgroup.

## 1. Four explicit parameters for a genuine extra-root family

The signed-divisor construction in AG_PARITY_AND_NORM_QUINTIC_REDUCTION.md
gives \(u=A_2(X)+yB_1(X)\) for five distinct signed torsion points whose
sum is zero. Its coefficient of \(X\) in \(B_1\) is nonzero: otherwise
the pole order at infinity is at most four, incompatible with five zeros.
Normalize \(B_1=X+c\) and write \(A_2=q_0+q_1X+q_2X^2\).
The monic extra locator is
\[
 J=F(X)(X+c)^2-(q_0+q_1X+q_2X^2)^2=\sum_{v=0}^5J_vX^v,
\]
with
\[
\begin{aligned}
 J_5&=1,&J_4&=2c-q_2^2,\\
 J_3&=c^2+a-2q_1q_2,&
 J_2&=2ac+b-q_1^2-2q_0q_2,\\
 J_1&=ac^2+2bc-2q_0q_1,&
 J_0&=bc^2-q_0^2.
\end{aligned}                                                    \tag{1}
\]
Thus the coefficients are explicit quadratics in four parameters.
Conversely, when \(J\mid\Phi\) is squarefree, this norm form recovers a
signed degree-five divisor of sum zero. The two representations differ
by \(A_2\mapsto-A_2\). Arbitrary parameters in (1) need not give domain
roots; the split-divisor requirement remains essential.

## 2. Eliminate the two omitted tags

Put \(s(\lambda)=s_f+\lambda s_g\), and for
\(P_0=N_H^2,P_1=N_HB_H,P_2=B_H^2\) define
\[
 C_{\nu,j}(\lambda,J)=
 \sum_{v=0}^5J_v\sum_{i=0}^{2\ell}[X^i]P_\nu\ s_{i+v+j}(\lambda),
 \quad \nu=0,1,2,\quad 0\le j<2\ell-6.                    \tag{2}
\]
The largest index is \(4\ell-2=R-1\). Each entry is affine in
\(\lambda\) and has degree at most two in the four norm parameters.
The exact recurrence condition is
\[
 C_{0,j}-\sigma C_{1,j}+\pi C_{2,j}=0
 \qquad(0\le j<2\ell-6),                                 \tag{3}
\]
where the two omitted tags are the roots of \(Z^2-\sigma Z+\pi\).

Choose two rows \(r,s\) on which
\[
\begin{aligned}
 \Delta&=C_{1,r}C_{2,s}-C_{1,s}C_{2,r}\ne0,\\
 S&=C_{0,r}C_{2,s}-C_{0,s}C_{2,r},\\
 V&=C_{0,r}C_{1,s}-C_{0,s}C_{1,r}.
\end{aligned}
\]
Then the tags are recovered without enumerating tag pairs:
\[
 \boxed{\ \sigma=S/\Delta,\qquad \pi=V/\Delta.\ }           \tag{4}
\]
Every remaining condition is exactly
\[
 \boxed{\ \Delta C_{0,j}-S C_{1,j}+V C_{2,j}
 =\det\!\begin{pmatrix}
 C_{0,r}&C_{1,r}&C_{2,r}\\
 C_{0,s}&C_{1,s}&C_{2,s}\\
 C_{0,j}&C_{1,j}&C_{2,j}
 \end{pmatrix}=0.\ }                                     \tag{5}
\]
These are cubics in \(\lambda\), of degree at most six in the norm
parameters, hence total degree at most nine. For fixed norm parameters,
the challenge test is a common-root test for univariate cubics, followed
by the filters below. There is no independent choice of five extra roots
after these equations are solved.

All rank-degenerate cases remain explicit. Solvability with leading tag
coefficient one is equivalent to
\[
 \operatorname{rank}[C_1,C_2]
 =\operatorname{rank}[C_0,C_1,C_2].
                                                               \tag{6}
\]
If the rank on the left is one or zero, retain the resulting affine
family of \((\sigma,\pi)\); a nonzero 3-by-3-minor test alone is not an
equivalence on those cases.

Let \(W_H(Z)=\prod_{\alpha\in\mathcal A_H}(Z-\alpha)\).
Tag admissibility is exactly
\[
 Z^2-\sigma Z+\pi\mid W_H(Z).                              \tag{7}
\]
Since \(W_H\) splits squarefree, this includes distinctness and membership
of both tags. It can be evaluated by the two-term remainder recurrence
\(Z^{j+2}\equiv\sigma Z^{j+1}-\pi Z^j\), without square-root choices.
Also require \(J\mid\Phi\) and
\(\gcd(J,N_H^2-\sigma N_HB_H+\pi B_H^2)=1\).

Equations (1)--(7) with these domain conditions are sufficient as well as
necessary within this norm-quintic family. Indeed they are precisely the
monic recurrence for the locator
\[
 U=(N_H^2-\sigma N_HB_H+\pi B_H^2)J,\qquad\deg U=2\ell+5.
                                                               \tag{8}
\]
Its recurrence space is the \(2\ell+5\)-dimensional span of the parity
columns on its roots. Thus it determines actual error values and a
degree-less-than-\(k\) witness, not merely a Hankel-rank condition.

For an explicit cofactor, solve for the unique error values \(e_x\) on
\(Z(U)\), and set
\[
 A_U(X)=\sum_{x\in Z(U)}
   \frac{e_x}{\Phi'(x)}\frac{U(X)}{X-x},\qquad
 E(X)=\frac{\Phi(X)}{U(X)}A_U(X).
                                                               \tag{9}
\]
Then \(E\) is the actual error interpolation polynomial and subtracting it
from a representative of \(s(\lambda)\) leaves degree below \(k\).
Require \(\gcd(A_U,J)=1\) if all five added positions must carry nonzero
errors; otherwise some extra factors merely pad a smaller support.

## 3. What generic and isolated solutions can supply

These statements concern the algebraic incidence before torsion filtering,
over an algebraic closure. They do not assume that any finite-field
solution is generic.

For every choice of the seven parameters
\((q_0,q_1,q_2,c,\lambda,\sigma,\pi)\), the \(2\ell-6\) equations (3)
are independent linear equations in \(s_f\). Their shifted rows have
different last nonzero entries, since \(U\) is monic. Consequently the
incidence with ordered global syndrome pairs has dimension
\[
 2R+7-(2\ell-6).
\]
Its projection to the \(2R\)-dimensional space of global pairs has
codimension at least \(2\ell-13\). In particular a Zariski-generic pair
has no solution even before the domain-root filter. This is a proved
rank calculation, not an assumption that a structured pencil is random.

For a fixed pair of global syndromes, (3) is a system of total degree at
most four in seven variables. If its full solution variety is
zero-dimensional, affine Bézout bounds its number of geometric points by
\(4^7\), independently of \(\ell\). This bound includes degenerate tag
charts. Alternatively, on the rank-two locus of (6), all charts are
contained in the one global determinantal variety (5) in five variables.
If that open locus is zero-dimensional, its points are isolated points
of this variety, so their total over all pivot charts is at most \(9^5\);
one must not multiply this bound by the number of row choices.

Thus isolated solutions for all \(H\) supply only \(O(\ell)\) labels.
A superlinear asymptotic construction within the norm family requires a
special positive-dimensional incidence for some subgroups; positive
dimension alone proves neither split torsion supports, varying labels,
nor far endpoints.

## 4. The concrete torsion 3/7 family and its norm label

Assume characteristic greater than seven. For
\(P\in E[\ell]\setminus H\), put
\[
 J_P(X)=\prod_{j\in\{1,2,4,5,6\}}(X-x([j]P)),\qquad
 a_3=x([3]\phi_H(P)),\quad a_7=x([7]\phi_H(P)).
                                                               \tag{10}
\]
All five extra positions are distinct and off the two selected fibers.
The signed list \(P,6P,-4P,2P,-5P\) has successive sums
\(7P,3P,5P\). Its Miller function is
\[
 u_P=
 \frac{\mathcal L_{P,6P}\mathcal L_{7P,-4P}
                   \mathcal L_{3P,2P}}
 {(X-x(7P))(X-x(3P))}
 =A_2+y(X+c)
                                                               \tag{11}
\]
after normalization. The same identity on the quotient curve has
denominator \((Y-a_7)(Y-a_3)\). The isogeny norm gives a genuine
distribution relation
\[
 \prod_{T\in H}u_P(Q+T)
   =\kappa_H(P)\,u_{\phi_H(P)}(\phi_H(Q)),\qquad
 \boxed{\ \kappa_H(P)=
       \prod_{j\in\{1,2,4,5,6\}}K_H(x([j]P)).\ }            \tag{12}
\]
For the constant, compare the common normalized pole term of order five
at \(Q=O\); normalized Vélu preserves the local parameter to first order.
This gives \(\kappa=\prod_{T\in H\setminus0}u_P(T)\).
Pairing \(T,-T\) gives
\((-1)^t\operatorname{Res}(K_H,J_P)\), where \(t=(\ell-1)/2\).
Swapping the monic resultant contributes \((-1)^{5t}\), cancelling the
sign and proving (12). The product is nonzero.

The denominators in (11) cancel in the resulting regular function.
Consequently (12) does not itself say that a fixed global received
pencil has errors on the two fibers plus \(J_P\). It provides the
specific label candidate \(\lambda=\kappa_H(P)\) for testing (3).

The root dependence is explicitly bounded. Write \(Z=x(P)\). Since
\(x([j]P)\) has rational degree \(j^2\), with numerator degree \(j^2\)
and denominator degree \(j^2-1\), the common denominator of the five
roots in (10) has degree 77, and all coefficient numerators of \(J_P\)
have degree at most 82. The two isogeny tags have a common denominator
of degree at most \(58\ell-2\); their sum and product numerators have
degrees at most \(58\ell-1\) and \(58\ell\). Therefore, after clearing
denominators, (3) becomes
\[
 A_j(Z)+\lambda B_j(Z)=0,\qquad
 \deg A_j,\deg B_j\le58\ell+82.                            \tag{13}
\]
Its pairwise minors have degree at most \(116\ell+164\).
If some minor is nonzero, at most this many \(Z\)-values qualify for
that \(H\). A rank-zero point would place the entire received pencil
inside one allowed support space and is excluded by a far endpoint.
If all minors vanish identically, the resulting rational challenge
function still requires nonconstancy, distinct labels, torsion values,
and source-distance bounds. These identities give a symbolic test, not
an existence result.

## 5. Exact finite test and stronger support-family closure

The saved \(\ell=23,\ p=1657\) fixture has
\((n,k,R,T)=(264,173,91,213)\). With the prescribed labels (12), every
support yields 40 linear equations in the 182 coefficients of
\((s_f,s_g)\). The exact test at
ell23_fixture/kappa_pencil/verify.py stopped at rank 182 after 25
supports, in 0.33 seconds and 44.4 MB. Its independent square certificate
uses 182 original recurrence rows from only six of those support records.
Thus this entire prescribed labelled bank has no nonzero common syndrome
pair in that fixture. It does not exclude arbitrary subbanks omitting
those constraints or different label maps. Inverting the labels or
applying one projective reparameterization cannot change this rank, so
no such reruns were made.

A stronger structural observation closes the whole support family (10),
with arbitrary labels and error values, under the far-endpoint condition.
Fix \(H\) and a nonzero quotient point modulo sign. Its \(\ell\) lifts
have the same two base fibers, and their extra five-point sets are
pairwise disjoint. Indeed
\(x(jP)=x(j'P')\) implies \(jQ=\pm j'Q\); the five multipliers are
distinct modulo sign, so \(j=j'\) and the lifts agree.

Under a far-endpoint hypothesis each individual support contributes at
most one projective point: otherwise the entire line lies in that support
space. Thus three distinct labels require three distinct lifts. If three
of these supports give three distinct projective points on a genuine
syndrome line, their three error representatives have a
dependence with all coefficients nonzero. Its support has size at most
\(2\ell+15<4\ell\), the code's minimum distance. Hence the dependence
holds as actual words. Disjointness forces all three extra parts to
vanish, putting the whole syndrome line inside the common two-fiber
error space. Every word then agrees on at least \(n-2\ell>T\) points,
contradicting a far endpoint. There are at most two labels per such
bank and exactly \((\ell+1)(\ell-1)/2=n\) banks:
\[
 \boxed{\text{At most }2n\text{ distinct labels for the family (10).}}
\]
This is an obstruction for this particular one-parameter support family,
not for the four-parameter norm-quintic system (1)--(9).
It supersedes further Plücker computation for the same family.
No Plücker benchmark or expanded label dictionary was run.
