# A torsion-quintic norm identity with a concrete candidate label

September 19, 2026. Constructive algebraic target, without a field scan.

**Status: the specific family is closed as a superlinear-label route.** The true identities below supplied a concrete candidate challenge. The prescribed challenge fails the existing order-23 fixture: 25 selected supports give rank 182 in 182 global syndrome unknowns. More decisively, [TORSION_QUINTIC_SUNFLOWER_BOUND.md](TORSION_QUINTIC_SUNFLOWER_BOUND.md) proves at most \(2n\) distinct qualifying labels for this support family under a far-endpoint premise, with arbitrary labeling. The addition, norm, trace, and degree identities remain useful algebraic records; no further Plücker test or scan of this family is proposed.

Keep the curve, domain, and code notation of [AG_PARITY_AND_NORM_QUINTIC_REDUCTION.md](AG_PARITY_AND_NORM_QUINTIC_REDUCTION.md). Let \(\ell\ge23\), \(t=(\ell-1)/2\), and let \(\phi_H:\mathcal E\to\mathcal E_H\) be the normalized Vélu isogeny. Write
\[
K_H(X)=\prod_{R\in(H\setminus\{O\})/\{\pm1\}}(X-x(R)),
\qquad B_H=K_H^2,\qquad Y_H=N_H/B_H.
\]
The two curves use short Weierstrass coordinates and the isogeny preserves the invariant differential.

## 1. The five extras and the two omitted fibers

For \(P\in\mathcal E[\ell]\setminus H\), set \(Q=\phi_H(P)\) and
\[
J_P(X)=\prod_{j\in\{1,2,4,5,6\}}(X-x([j]P)).
\]
Use the two full fibers with tags
\[
a_3=x([3]Q),\qquad a_7=x([7]Q),\qquad
L_{0,H,P}=(N_H-a_3B_H)(N_H-a_7B_H).
\]
All these factors are squarefree, have the asserted sizes, and are pairwise disjoint. Indeed the image \(Q\) has order \(\ell\), and for \(\ell\ge23\) the five integers \(1,2,4,5,6\) are distinct modulo sign and avoid \(\pm3,\pm7\); also \(3\ne\pm7\). Thus
\[
U_{H,P}=L_{0,H,P}J_P\mid\Phi,\qquad \deg U_{H,P}=2\ell+5.
\]
This checks actual supports, without making a statement about their common received line.

The signed extras \(P,6P,-4P,2P,-5P\) have successive partial sums \(7P,3P,5P,O\). Consequently the line-function identity
\[
u_P=
c_P\,
\frac{\ell_{P,6P}\,\ell_{7P,-4P}\,\ell_{3P,2P}}
{(x-x([7]P))(x-x([3]P))}
\tag{1}
\]
has divisor
\[
[P]+[6P]+[-4P]+[2P]+[-5P]-5[O].
\]
Here \(c_P\ne0\) normalizes the coefficient of \(xy\) to one. All displayed additions are nondegenerate for \(\ell\ge23\). In particular
\[
u_P=A_P(x)+y(x+b_P),\qquad \deg A_P\le2,
\qquad u_P\,u_P^\iota=-J_P(x),
\tag{2}
\]
where \(\iota(x,y)=(x,-y)\). The same normalized construction on \(\mathcal E_H\), at \(Q\), gives \(u_Q^H\). Its two vertical denominators are exactly the two chosen tags \(a_7,a_3\).

## 2. Exact isogeny norm and its scalar

Taking the norm through the degree-\(\ell\) isogeny pushes forward the divisor in (1). Hence
\[
\boxed{\quad
\prod_{R\in H}u_P(S+R)
=\kappa_H(P)\,u_Q^H(\phi_H(S)).
\quad}
\tag{3}
\]
Both sides have the same divisor; the ratio is a nonzero field constant. At \(S\to O\), normalized local parameters agree to first order and both normalized functions have the same leading coefficient at their order-five pole. Therefore
\[
\kappa_H(P)=\prod_{R\in H\setminus\{O\}}u_P(R).
\]
Pairing \(R,-R\) in (2) and then reversing the resultant gives
\[
\begin{aligned}
\kappa_H(P)
&=(-1)^t\operatorname{Res}(K_H,J_P)\\
&=(-1)^{t+5t}\operatorname{Res}(J_P,K_H)\\
&=\boxed{\ \prod_{j\in\{1,2,4,5,6\}}K_H(x([j]P))\ }.
\end{aligned}
\tag{4}
\]
There is no remaining sign. The scalar is native, nonzero, and invariant under \(P\mapsto-P\). Formula (4) is a candidate label, not a proof of challenge injectivity or of an affine relation between the received heads.

For comparison, trace is linear but gives a different identity. Write
\(\mathcal E_H:Z^2=Y^3+A_HY+B_H^{\rm curve}\), and put
\(c_H=\sum_{R\in H\setminus O}x(R)\). Normalized Vélu and differentiation with respect to the invariant differential give
\[
\begin{split}
\operatorname{Tr}_{\phi_H}(x)&=Y+c_H,&
\operatorname{Tr}_{\phi_H}(y)&=Z,\\
\operatorname{Tr}_{\phi_H}(x^2)&=Y^2+(A_H-\ell A_{\rm c})/3,&
\operatorname{Tr}_{\phi_H}(xy)&=YZ.
\end{split}
\]
For \(A_P=a_2x^2+a_1x+a_0\), it follows that
\[
\operatorname{Tr}_{\phi_H}(u_P)
=a_2Y^2+Z(Y+b_P)+a_1Y+
\left(\ell a_0+a_1c_H+a_2(A_H-\ell A_{\rm c})/3\right).
\tag{5}
\]
For example, the \(x^2\) identity follows by differentiating the y identity: \(D y=3x^2+A_{\rm c}\) and \(D Z=3Y^2+A_H\). The trace in (5) is not asserted to equal \(u_Q^H\). Replacing the norm in (3) by this linear trace would require a new identity.

## 3. The precise additive common-pencil test

Let \(R=n-k=4\ell-1\). A global source pair has syndrome vectors
\(s_f,s_g\in\mathbb F_p^R\), with the usual weights \(1/\Phi'(x)\). For a polynomial \(U\) of degree \(2\ell+5\), the exact support condition at projective label \([a:b]\) is
\[
\sum_{i=0}^{2\ell+5}U_i\bigl(a\,s_{f,i+j}+b\,s_{g,i+j}\bigr)=0,
\qquad 0\le j\le2\ell-7.
\tag{6}
\]
When \(U\mid\Phi\) is squarefree, these equations are necessary and sufficient for an error representation supported on its roots. The particular extra-error coefficients must still be nonzero if all five extras are to count as genuine rather than padded errors.

There is a useful low-degree identity test for this explicit parameterization. Write \(z=x(P)\). On the appropriate curve, the x-coordinate multiplication map has a coprime representation
\[
x([j]P)=A_j(z)/D_j(z),\qquad
\deg A_j=j^2,\quad \deg D_j=j^2-1
\]
for the fixed integers used here. These degree statements apply because the characteristic exceeds seven; full rational \(\ell\)-torsion over a prime field with \(\ell\ge23\) already implies \(p>n>7\).

Multiplying the five factors of \(J_P\) by their denominators gives coefficient polynomials of degree at most
\[
1^2+2^2+4^2+5^2+6^2=82,
\]
with common denominator of degree \(82-5=77\). The maps \(x([3]\phi_H(P))\) and \(x([7]\phi_H(P))\) have numerator degrees \(9\ell,49\ell\) and denominator degrees \(9\ell-1,49\ell-1\). Thus a common denominator clears every coefficient of \(U_{H,P}\) to degree at most
\[
58\ell+82.
\tag{7}
\]
Let \(\widehat U_{H,i}(z)\) be these cleared coefficients and define
\[
F_{H,j}(z)=\sum_i\widehat U_{H,i}(z)s_{f,i+j},
\qquad
G_{H,j}(z)=\sum_i\widehat U_{H,i}(z)s_{g,i+j}.
\]
The exact general-label test is that the two columns \(F_H(z),G_H(z)\) have rank at most one. Each two-by-two minor has degree at most \(116\ell+164\). If this succeeds for every \(P\notin H\), it has \(\ell(\ell-1)/2\) distinct z-values, so for primes \(\ell\ge239\) all those minors must vanish identically as rational identities. This conclusion is a test, not an impossibility assertion.

For the explicit proposed label (4), the test is stronger and linear in the unknown source syndromes. Let
\[
C_{\kappa,H}(z)=\prod_{j\in\{1,2,4,5,6\}}D_j(z)^t,
\]
\[
N_{\kappa,H}(z)=
\prod_{j\in\{1,2,4,5,6\}}
\left[D_j(z)^t K_H\!\left(A_j(z)/D_j(z)\right)\right].
\]
Then \(\kappa_H=N_{\kappa,H}/C_{\kappa,H}\), with respective degree bounds \(82t\) and \(77t\). Formula (6), at \([a:b]=[1:\kappa_H]\), is precisely
\[
\boxed{\quad
C_{\kappa,H}F_{H,j}
+N_{\kappa,H}G_{H,j}=0,
\qquad 0\le j\le2\ell-7.
\quad}
\tag{8}
\]
Every left side has degree at most \(99\ell+41\). All denominators are nonzero at the allowed torsion parameters. Hence a complete bank at this label, for every \(P\notin H\), forces the polynomial identities (8) for all primes \(\ell\ge211\). A fixed projective reparametrization of \(\kappa_H\) can be absorbed into the global source pair.

Equations (8) were the exact common-pencil target supplied by the norm route. Equation (3) does not imply them: the former is a multiplicative degree-\(\ell\) norm identity, while (8) is additive in two fixed received words.

## 4. Failed candidate scope and final disposition

The exact receipt [ell23_fixture/kappa_pencil/receipt.json](ell23_fixture/kappa_pencil/receipt.json) uses \(p=1657,\ell=23,n=264,k=173,T=213\). Its 25 selected supports and prescribed values (4) yield full rank 182 for the 182 coordinates of \((s_f,s_g)\), and nullity zero. The accompanying verifier stops as soon as full rank is reached; the parent independently replayed it. Thus even a nonzero source syndrome pair is impossible for those constraints. A single invertible projective reparameterization preserves this rank conclusion. This finite calculation by itself does not exclude other curves, smaller subbanks, or arbitrary new assignments.

The separate sunflower proof supplies the label-independent conclusion for the whole 3/7 support family. For fixed \(H\) and fixed quotient point modulo sign, the two full fibers are fixed while the five-point petals from the \(\ell\) lifts are disjoint. Three distinct qualifying projective labels would force all three extra-error vectors to vanish, then make every line point close using only the two base fibers, contradicting the far endpoint. There are \(n\) such base banks, hence at most \(2n\) labels overall.

Consequently neither (3) nor a different labeling can turn this specific one-quotient-parameter support family into the desired superlinear bank. A future construction would need a materially different support family, including more than order-\(n\) base fiber pairs in the same bounded-extra-error window.
