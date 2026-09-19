# Omitting two roots does not produce a twist plane

September 19, 2026. Exact symbolic obstruction; no scan or manuscript edit.

Let D⊂Fp have n distinct elements, let Λ=∏_{x∈D}(X−x), and fix
a monic divisor H|Λ of degree h≥4. Put S=Z(H) and W=Λ/H.
For selected unordered pairs {a,b}⊂S, a≠b, write

    J_ab=(X−a)(X−b),       G_ab=H/J_ab.

The tempting reciprocal family is genuinely two-dimensional:

    1/G_ab=(X²−(a+b)X+ab)/H.

This note tests whether it can lift to a small affine space of twists
in the exact identities

    G_ab^p − A_ab G_ab = Λ F_ab^p.                          (1)

Coefficients of A and F may lie in any finite extension E of Fp.

## 1. Twists affine in the two pair coefficients

Assume fixed polynomials A0,A1,A2 satisfy

    A_ab=A0+(a+b)A1+ab A2                                  (2)

for every selected pair. Then the selected-pair graph on S has at
most 3h−6 edges. In particular the complete pair family is impossible
when h≥5. No bound on deg F or deg A is needed for this conclusion.

**Proof.** Introduce formal parameters a,b, constant under
differentiation in X, and set

    J=(X−a)(X−b),
    J^[p]=(X^p−a)(X^p−b),
    A=A0+(a+b)A1+ab A2,
    Y=H^(p−1)J−A J^[p].

For actual native pairs, J^[p]=J^p. Multiplying (1) by J^p,
dividing by H, and multiplying by J gives

    Y=WJ (J F_ab)^p.

Consequently the polynomial

    Z(a,b)=WJ Y′−(WJ)′Y                                   (3)

vanishes identically in X at every selected pair. Expanding it yields

    Z(a,b)=−H^(p−2)Λ′ J²
            +J^[p] [ A(WJ)′−WJ A′ ].                       (4)

Viewed over the coefficient field E(X), this is a polynomial in
a,b of degree at most three in each variable. It is not zero:
substituting a=X^p AFTER forming (3) and (4) gives

    Z(X^p,b)=−H^(p−2)Λ′(X−X^p)²(X−b)² ≠0.                 (5)

Here Λ′≠0 because Λ is squarefree.

If a graph vertex a has four distinct neighbors, then Z(a,b),
as a degree-at-most-three polynomial in b, has four roots and is
identically zero. Four such vertices would make every coefficient
in b vanish at four a-values, forcing Z=0, contrary to (5).
Thus at most three vertices have degree at least four.

Choose three vertices containing all such high-degree vertices.
The number of edges within them is at most three; every other
vertex has degree at most three. Counting the remaining edges
by these vertices, with harmless double counting of their mutual
edges, gives at most 3+3(h−3)=3h−6 edges. ∎

The specialization in (5) is an algebraic test of a polynomial
identity. One must not differentiate after substituting a=X^p;
the derivation first treats a,b as independent constants.

## 2. Any affine plane of twists reduces to the matched form

Assume additionally

    p−n≥3,       P_ab=(Λ/G_ab)F_ab,       deg P_ab<n.        (6)

Suppose all A_ab belong to one E-affine polynomial space of dimension
at most two, without prescribing their coordinates in that space.
The same bound of 3h−6 distinct selected pairs still holds.

Put e=h−2. Since deg F_ab≤e−1 for nonzero F_ab, rearranging (1)
gives

    A_ab=G_ab^(p−1)−(Λ/G_ab)F_ab^p.

Every A_ab is monic of degree (p−1)e, because the second term has
degree at most (p−1)e+n−p<(p−1)e. This also holds when F_ab=0.
Reverse at infinity, writing

    Hrev(Z)=Z^h H(1/Z)=1−S_H Z+E_H Z²+...,
    j_ab(Z)=1−sZ+tZ²,       s=a+b, t=ab,
    g_ab(Z)=Hrev(Z)/j_ab(Z),
    a_ab(Z)=Z^((p−1)e) A_ab(1/Z).

As in the affine-twist reversal argument,

    a_ab(Z)=1/g_ab(Z)+O(Z^(p−n)).

Thus (6) makes its first two nonconstant coefficients exactly

    c1=S_H−s,
    c2=S_H²−E_H−S_H s+t.

They recover the pair coefficients affinely:

    s=S_H−c1,       t=c2−S_H c1+E_H.                        (7)

If the head image of the twist plane has affine dimension two,
the map to (s,t) is invertible on that plane. Hence the entire
polynomial A_ab is necessarily affine in s,t, and Section 1 applies.

If the head image has dimension at most one, the selected pair
coefficients lie on a line α(a+b)+βab=γ. For β=0 they form a
matching. For β≠0, rewrite this as

    β(a+α/β)(b+α/β)=γ+α²/β.

A nonzero right side again gives degree at most one at every
vertex; a zero right side gives a star. In either case there
are at most h−1 unordered pairs, which is at most 3h−6.

This proves the arbitrary-plane assertion. The condition is only
p−n≥3, not the stronger p−n>2e used for the earlier affine-line gate.

## 3. Scope

The reciprocal two-plane itself exists and contains binom(h,2)
squarefree native locators. The obstruction is its lift to the exact
Frobenius identity with an affine two-plane of polynomial twists
and sub-n residual degree. It occurs before imposing a common
received line or endpoint farness.

The bound counts distinct pair locators. It does not bound parameters
obtained by varying F repeatedly at one locator, and it does not rule
out genuinely higher-dimensional twist families or residual degrees
at least n. Without (6), Section 1 still rules out twists whose
dependence is the specifically matched expression (2).

No inference of general Reed–Solomon optimality is intended.

