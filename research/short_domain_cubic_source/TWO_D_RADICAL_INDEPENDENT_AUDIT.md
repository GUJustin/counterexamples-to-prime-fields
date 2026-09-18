# Independent audit of the p>2D upgrade

**PASS.** The radical budget in `TWO_D_RADICAL_BUDGET.md` proves the
combined arbitrary-word theorem with characteristic zero or
p>max(3,2D), with no change to its list bound. The manuscript fragment
`general_cubic_list.tex` has been revised accordingly; no manuscript
input or build was performed.

After extending constants algebraically, a nonconstant rational p-th
power A/H admits a reduced expression (a/b)^p. Polynomial unique
factorization gives A=G a^p and H=G b^p after absorbing a nonzero
constant into G or a. Both a and b are nonzero and coprime. Writing
M=max(deg a,deg b)>=1 yields deg G+pM<=3D. Hence

    # distinct roots(H) <= deg G+deg b
                         <=3D-(p-1)M<=3D-p+1<=D.

The final inequality uses integrality: p>2D means p>=2D+1. The
argument includes polynomial p-th powers (b constant), all cancellation
in the original ratio, and repeated factors shared by G and b.
The zero numerator is constant and never invokes this lemma.

On an arbitrary domain, at most D coordinates are roots of H. At each
other coordinate a received value fixes c=F(x,w)/H(x), and a cubic has
at most three polynomial sections at that label. Thus La<=LD+3n,
giving L<=3/eta whenever a>=D+eta*n. No assumption about the received
word lying on a branch or satisfying the ODE is used.

For a rational critical root r, integrality and the weighted caps give
deg r<=D and deg F(r)<=3D. Its zero derivative makes F(r)/H a p-th
power. A nonconstant ratio triggers the root budget; a constant ratio
retains the repeated-fiber/cubic-cover argument unchanged.

For an irreducible quadratic critical component, depress F to
z^3-3gz+b. Both conjugate critical values have derivative zero, so
(b/H)'=0. If nonconstant, the same root budget applies. Otherwise
b=beta H and the relation 3g'H-2gH'=0 follows from the critical
equation. A section with c!=beta would satisfy

    (z^2-g)(2gz'-g'z)=0.

Nonsquareness of g rules out the first factor. Since z!=0, this forces
(g/z^2)'=0. Its height is at most max(deg g,2deg z)<=2D<p, so it is
constant, making g a square over algebraically closed constants: a
contradiction. Thus this case has at most three sections. The argument
does not assert that all critical values are constant at p>2D.

The zero-dimensional scheme and valuation parts only require p>3 and
are unaffected. The new 3/eta alternative is smaller than the stated
floor(9+(3+108D/n)/eta), so no adjustment of constants is required.

The illustrative Frobenius example also checks: for p/3<D<p/2,
h=X^D and s=X^(p-2D), the displayed cubic has critical value
beta+X^p at u=-h. Its nonzero constant-fiber sections would have to
be constant; their X^(2D) coefficient excludes them. In the beta fiber
the residual quadratic discriminant is
X^(2(p-2D))(1+4X^(3D-p)), whose nonzero roots are simple because
0<3D-p<p. Thus only P=0 survives. This confirms why a critical-value
constancy argument alone cannot justify the improved threshold.
