# Exact secondary level and disjointness by an operator trace

This refines the p^5 specialization, for p>=5. Use B=F_(p^5), F=F_(p^15), theta outside B, and the shifted sources f,g of `large_characteristic_singleton_line.tex`. The strengthened coefficient-comparison argument gives the following preliminary fact: any witness with at least p² agreements has the form

    h=-((theta-a^p)c+v^p)X^(p-1)-(theta-a^p)v,
    z=c^p-a^(p+1)+theta a-theta²,

and its residual multiplied by X is

    L^p+(theta-a^p)L,
    L=X^(p³)+aX^(p²)+cX^p+vX.

For reference, the argument requires no finite-difference estimate. Write h=h_B+theta h_theta after projecting the agreement equations onto a basis extending 1,theta,theta². Set L=X^(p³)+aX^(p²)-Xh_theta and T=X^(p⁴)+z0X^(p²)-Xh_B. Then

    (T-L^p+a^pL)/X

has degree at most p²-1 and vanishes at all agreement coordinates, including a matched zero. It is identically zero. The exponents p-1+pj force h_theta to have only degrees 0,p-1, and coefficient comparison gives the displayed formulas.

## The two possible high levels

If v!=0, zero is not an agreement and the agreement number is |ker_B L|-1. Thus at least p² agreements forces dim ker L=3. This is the primary Gaussian family, with p³-1 agreements.

If v=0, write L=J^p, where

    J=X^(p²)+a^(1/p)X^p+c^(1/p)X.

Now zero is an agreement, and the agreement number is |ker_B J|. At least p² agreements forces J to be the locator of a two-dimensional subspace U. Each U therefore supplies a secondary label. Distinct U give distinct (a,c), and hence distinct labels. There are exactly [5 choose 2]_p secondary labels, each with a candidate agreeing on p² coordinates.

## Primary and secondary labels cannot overlap when p!=3

Suppose a secondary and primary label coincide. Their a,c coincide, so the corresponding locators satisfy

    L_W=J_U^p+vX,  v!=0,

where dim U=2 and dim W=3. Their kernels intersect trivially: at a common root the right-hand side is vX. Hence B=U direct-sum W as F_p-vector spaces.

The F_p-linear map

    T(x)=-J_U(x)^p/v

is zero on U and the identity on W. It is a projection of rank three, so its F_p-linear operator trace is 3.

However its linearized polynomial contains only X^p,X^(p²),X^(p³), and no X term. For a linearized map on F_(p^5),

    trace_Fp( sum_(i=0)^4 a_i Frobenius^i )
       = Tr_(B/Fp)(a_0).

One proof extends scalars to an algebraic closure: multiplication by a_i is diagonal in the five embedding coordinates, while Frobenius^i permutes those coordinates without a fixed point for 1<=i<=4. Such summands have matrix trace zero. Only i=0 contributes the field trace. Therefore trace(T)=0, contradicting 3!=0 in F_p.

This proves disjointness for every p>=5, in particular for all p>=53 in the large-characteristic first-order comparison. The trace argument alone does not handle p=3. A separate small p=3 RREF census (`secondary_spectrum/census.py/json`) finds the sets disjoint there too, but that computation is unnecessary for the main range.

## Exact nearest-agreement spectrum for p>=5

Put M=[5 choose 2]_p and C=p²-1. On the full affine challenge line:

* exactly M primary labels have nearest agreement p³-1, with a unique nearest polynomial;
* exactly M disjoint secondary labels have nearest agreement p², also with a unique nearest polynomial;
* every remaining label has nearest agreement exactly C.

The upper bound C for the remaining labels follows from the complete >=p² classification. Its lower bound holds uniformly because the simultaneous degree-<p witnesses on any two-dimensional subspace minus zero give C agreements for every challenge.

All primary and secondary labels have theta² coefficient -1 and so are nonzero. Thus the number of bad challenges is exactly 2M at threshold p², and exactly M at every integer threshold p²<T<=p³-1. In particular every primary nearest list remains a singleton at the advertised below-Johnson threshold A0=p³-p². No claim is made about the list cardinalities at the bottom threshold C.
