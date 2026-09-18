# Equality classification at derivative degree one

Let n>2w, w>=2, and let F in K[X,Y,R] have R-degree one. Give (X,Y,R)
weights (1,w,w-1), and use actual first-jet contacts at arbitrary received
symbols r_i on n distinct nodes. Suppose

    charge(F)=wt(F)-(w/n)sum_i contact_i(F)=w-1.

Write F=A(X,Y)R+C(X,Y), q=deg_Y A.

**Classification.** If q=0, then F=cR+C_0(X), where c!=0 and
 deg C_0<=w-1. This puts no condition on the received word.
If q>=1 is nonzero in K, then

    F=c(Y-P(X))^q(R-T(X)),
    deg P<=w, deg T<=w-1, P(x_i)=r_i for every node.

Thus in characteristic zero every positive-contact equality example at
R-degree one is reducible. In positive characteristic the condition that q
is invertible is essential; a separate exact characteristic-two example
below shows why it cannot be dropped.

## 1. Consequences of universal equality

The universal resource theorem, with n>2w, forces the leading Y coefficient
of A to be a nonzero constant c. It also forces

    wt(F)=qw+w-1,   contact_i(F)=q at every node.

Indeed, its local upper bound is q+2ord B; equality in the global bound first
forces deg B=0, after which every contact is <=q. The weight is at least
qw+w-1, so equality in the charge forces both conclusions. The weight cap
gives deg_Y C<=q and total jet degree<=q+1. Its unique possible top-degree
term is cY^qR. If q=0, the same cap permits only C=C_0(X) of degree<=w-1,
which proves that case.

## 2. Recovering the word when q is invertible

For q>=1, write A=cY^q+B(X)Y^(q-1)+lower terms, with deg B<=w.
In the local substitution the coefficient of R^q at order t^(q-1) is

    q*c*r_i+B(x_i).

The R-free part C contributes to R^q only at order at least t^q.
Contact q therefore gives P=-B/(qc), deg P<=w, and P(x_i)=r_i.
Translate its jets so the received word becomes zero. This preserves the
weight, actual contacts, and R-degree. The translated polynomial still has
leading term cY^qR and R-free Y-degree at most q.

## 3. Removing all lower terms in the zero-word coordinates

Consider a homogeneous jet piece of degree b<=q containing an R term
B_b(X)Y^(b-1)R. Put k=q-b+1>=1. The weighted cap gives deg B_b<=kw.
Its zero-word contact is at least q, while the homogeneous local estimate
gives contact<=b-1+2ord_(X-x_i)B_b. Thus B_b is divisible by the locator
to power ceil(k/2), contradicting

    n*ceil(k/2)>kw>=deg B_b.

This removes every lower-degree R term. The remainder is cY^qR plus an
R-free polynomial sum_j C_j(X)Y^j. Different homogeneous degrees remain
separate under the zero-word substitution. For j<q, contact q forces
Lambda^(q-j)|C_j, but

    deg C_j<=(q-j+1)w-1 < n(q-j).

Hence all these coefficients vanish. Only C_q(X)Y^q can remain, with
 deg C_q<=w-1. Therefore the translated polynomial is
Y^q(cR+C_q(X)); undoing the jet translation proves the claimed formula.
Conversely every displayed factorization has exact charge w-1 at its
received word P, so the classification is sharp.

## 4. Exact limits: small characteristic and higher R-degree

The root/frontier characteristic-two example is independently verified:
over F8, on all eight coordinates, take w=3, received word x^4, and

    F=R(Y^2-X)+Y+X^4.

At X=x+t,Y=x^4+tR+t^2E, using x^8=x, the exact substitution is

    t^2(R^3+E)+t^4(E^2R+1).

Thus contact is exactly two at all nodes, weight is eight, and charge is
8-3*2=2=w-1. The polynomial is primitive irreducible as a polynomial linear
in R: Y^2-X is irreducible and does not divide Y+X^4. Its received word
cannot be interpolated with degree<=3. It is a genuine non-graph equality
factor, and q=2 is not invertible in the field.

The analogous graph-factor assertion for higher R-degree is false even in
characteristic zero. Take w=3,n=7, zero received word, squarefree locator
Lambda of degree seven, and

    F=Y R^2+Lambda.

It has exact contact one at every node, weight seven, and charge four,
which equals2(w-1). It is primitive irreducible as a polynomial linear in Y
and has no Y factor; F_R is nonzero outside characteristic two. More generally
Y R^r+Lambda works whenever2w<n<=w+r(w-1). Thus neither the R-degree-one
classification nor its graph factorization extends naively to general r.

These are structural equality statements and counterexamples. They do not
construct the missing benchmark retained source or charge individual first-tail
components beyond the established scalar resource.
