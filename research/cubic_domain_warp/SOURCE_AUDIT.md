# Primary point-count input

Cafure and Matera, *Improved explicit estimates on the number of
solutions of equations over a finite field*, Finite Fields and Their
Applications 12 (2006), 155–185, DOI10.1016/j.ffa.2005.03.003.
Primary published PDF:
https://bibliotecadigital.exactas.uba.ar/download/paper/paper_10715797_v12_n2_p155_Cafure.pdf

Downloaded to tmp/source-audit/cafure-matera-2006.pdf; SHA256
b2d8ce47416111061c9d50079b60e4e39c45e1bc9a74cb4e1e16a3251ffc883a.
Theorem5.2, printedpage171, gives the unrestricted hypersurface bound.
For the proposed construction, Corollary5.6 on printedpage174 is simpler:
if characteristic p>2d² and an affine hypersurface in n variables is
absolutely irreducible of degree d>1, its point-count error from
q^(n-1) is at most

    (d-1)(d-2)q^(n-3/2)+3d^4 q^(n-2).

Specialize q=p,n=3,d<=t. Linear hypersurfaces have exactlyp² points.
The condition p>2t² suffices uniformly over all residual support pairs.
Using ceil(sqrtp) gives the exact rational collision multiplier

    B=[p+(t-1)(t-2)ceil(sqrtp)+3t^4]/[p-binom(m,2)].

No restriction on the number of support pairs occurs: sum the uniform
bound over pairs, then divide by the count of injective cubic maps.
The cited theorem is used as a published input, not independently proved.
