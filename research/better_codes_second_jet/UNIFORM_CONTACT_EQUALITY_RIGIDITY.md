# Rigidity at the uniform first-jet contact budget

**Proved statement.** Let n distinct nodes over a field carry arbitrary
received symbols w_x (also allowed in the coefficient field k(Z)). Let
w>=2 and 1<=a<w-1, assume n>w+a, and assume characteristic zero or
characteristic p>a. If a nonzero polynomial F(X,Y,R) has weighted degree
at most aw for weights (1,w,w-1) and satisfies

    F(x+t,w_x+tR+t^2E,R)=0 mod t^a

formally at every node, then there are a nonzero scalar c and a polynomial
P(X) of degree at most w such that

    w_x=P(x) for every node,   F=c(Y-P(X))^a.

Scalars and P may belong to k(Z). Consequently an irreducible F under
these hypotheses has a=1 and is a codeword-graph factor. No genericity,
large-field point-density assumption, or characteristic bound p>w is used.

## 1. An independent proof excluding lower total jet degree

The total (Y,R) degree b is at most floor(aw/(w-1))=a. Write F_b for
its highest homogeneous jet piece. For a w-element subset T, let P_T
interpolate its received values with degree less than w, and let
H_T=product_(x in T)(X-x). Substitute the indeterminate pencil
P_T+cH_T and its derivative. Its degree in X is at most aw, and contact
forces divisibility by H_T^a. Therefore

    F(X,P_T+cH_T,P_T'+cH_T')=C(c) H_T^a.           (1)

Here C(c) is independent of T: it is the coefficient of X^(aw),
computed from the weighted-leading part of F with the leading terms
Y=cX^w and R=wcX^(w-1). This also holds when w=0 in the field;
then the R leading coefficient is zero. C may be zero.

Taking the coefficient of c^b gives

    F_b(X,H_T,H_T')=C_b H_T^a.                     (2)

Fix w-1 nodes B and put H_T=H_B(X-z), where z ranges over the remaining
n-w+1>a nodes. Both sides of (2) are polynomials in z of degree at most
a, so (2) holds for an indeterminate z. If b<a, the coefficient of
z^a forces C_b=0. Divide by H_T^b and use

    H_T'/H_T=H_B'/H_B+1/(X-z).

This ratio is transcendental over k(X), so the nonzero polynomial
F_b(X,1,U) cannot vanish at it. Contradiction. Thus b=a.

The same argument for b=a gives

    F_a(X,1,H_B'/H_B+1/(X-z))=C_a,

and consequently F_a=C_a Y^a. Its scalar coefficient c=C_a is nonzero.
This argument also independently verifies the entire top-jet reduction.

## 2. Recovering the received polynomial

Write the degree-(a-1) jet piece as

    sum_(j=0)^(a-1) B_j(X) Y^(a-1-j) R^j,

where deg B_j<=w+j. In the formal contact substitution, the coefficient
of E^0 R^(a-1) is

    a*c*w_x*t^(a-1) + sum_j B_j(x+t)t^(a-1-j).

Descending through j>=1, the coefficient of t^(a-1-j) forces B_j(x)=0
at every node after the higher B_j have vanished. Since deg B_j<=w+j<n,
this makes B_j the zero polynomial. The coefficient of t^(a-1) now gives

    a*c*w_x+B_0(x)=0.

Because characteristic does not divide a, P=-B_0/(a*c) is defined,
has degree at most w, and matches the entire received word.

## 3. Removing the residual polynomial

The polynomial (Y-P)^a has contact at least a at every node. Indeed
P(x)=w_x, so its inner factor is divisible by t under the formal
substitution. Thus F-c(Y-P)^a has contact at least a and weight at most
aw, but has total jet degree less than a. Section 1 shows that a nonzero
such polynomial is impossible. This proves the identity claimed above.

## Scope for component accounting

This proves equality rigidity for UNIFORM contact a in the stated
small-contact range. It does not classify zero average-excess factors
with nonuniform contact, nor factors with small positive excess.
It also does not yet turn the nonnegative primary-factor resource into
a bound on codimension-two first-tail components. The degree bound
here is degree <=w; any application using a code dimension convention
requiring degree <w must handle that endpoint explicitly.
