# Why a zero-cost polynomial derivation is special to codeword-related lines

This is a classification of a precise operator class, not a claim that every conceivable kernel argument has this form.

Let n>w≥2, let the evaluation nodes be distinct, and let the received line be f_i+Zg_i. Consider polynomial derivations of k[X,Y,R,Z] preserving every cutoff for (i) the contact weight wt(X,Y,R,Z)=(1,w,w−1,0), (ii) joint(Y,R,Z)-degree, and (iii) R-degree. Require also preservation of every local first-jet contact filtration at the received line. No characteristic assumption is needed.

The ambient degree conditions force the derivation to have the form

    a(X)partial_X
    +(u(X)+Zv(X)+bY)partial_Y
    +(r(X)+Zs(X)+dR)partial_R
    +(alpha+beta Z)partial_Z,

where deg a≤1, deg u,deg v≤w, deg r,deg s≤w−1, and b,d,alpha,beta are constants. In particular an R term in the Y coefficient would violate preservation of the R-degree cutoff.

Preservation of the order-one local contact ideal forces a(x_i)=0 at every node. Since n≥3, a=0. Applying the operator to Y−f_i−Zg_i gives

    u(x_i)+b f_i−alpha g_i=0,
    v(x_i)+(b−beta)g_i=0.                    (1)

Applying it to the order-two generator

    Y−f_i−Zg_i−(X−x_i)R

forces d=b, r(x_i)=u'(x_i), and s(x_i)=v'(x_i). Their degree bounds and n>w give r=u',s=v'. Conversely these conditions suffice: the derivative of the order-two generator equals b times that generator plus a polynomial divisible by(X−x_i)². The derivation therefore preserves all weighted contact orders.

Consequently all operators in this class are exactly

    (u+Zv+bY)partial_Y +(u'+Zv'+bR)partial_R
      +(alpha+beta Z)partial_Z,

with(1) and the stated low-degree bounds.

Let C_w be the evaluation space of degree-at-most-w polynomials. In k^n/C_w, equations(1) say

    b[f]−alpha[g]=0, (b−beta)[g]=0.

If [f] and[g] are linearly independent, these force b=alpha=beta=0, then u=v=0 by injectivity of evaluation. Thus there is NO nonzero operator in this uniformly filtered class for such a received line.

The exceptions have the expected concrete forms. If g is a codeword direction, delta_h=partial_Z+h partial_Y+h' partial_R is available. If f−c g is a codeword h, the translated Euler operator

    (Y−h)partial_Y+(R−h')partial_R+(Z+c)partial_Z

is available. The classification does not preclude an operator tailored only to a particular finite-dimensional kernel, rather than to the full contact and ambient filtrations. It also does not preclude positive-cost Hermite--Padé operators; those are treated in LOW_COST_OPERATOR_REFINEMENT.md.
