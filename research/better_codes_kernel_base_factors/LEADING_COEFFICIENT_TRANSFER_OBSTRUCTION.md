# Why the stronger contact-sum gate does not yet give a helper

A proposed shortcut from own-system rigidity to an R-free helper fails at multiplicity transfer. The numerical inequality itself is valid for the q43,d12 binding shape. With C=6802316684345, R43=31118386, exceptional-rank allowance49897120, n262144 and target agreement181275, the rank/contact inequalities imply for any target-size coordinate subset S:

    sum_{x in S} a_x >= 92143711640485/15559193
                          =5922139.512... .

Indeed R(a)/a<=R43/43 for integer1<=a<=43 (checked exactly), and the exceptional orders have the previously certified total rank allowance. The leading R coefficient has weight at most43w+12=5636065, so the displayed sum exceeds that weight.

HOWEVER the coefficient-extraction lemma only gives a Y-root of multiplicity a_x in A_r(x,Y,Z), at fixed X=x. It does not give an X-root of that multiplicity in A_r(X,P(X),Z). Therefore this numerical comparison is not a root-count proof.

An explicit counterexample is F=R(Y^2-X)+Y at node0 with received value0. Substituting X=t,Y=tR+t^2E gives first-jet contact exactly2. The leading R coefficient A=Y^2-X has a double Y-root at X0. The candidate P=0 even satisfies F(X,P,P')=0 identically, but A(X,P)=-X has X-order only1. Its leading Y coefficient is constant, so low leading-coefficient X degree does not remove the obstruction.

The stronger valid estimate ord_x A_r(X,P)>=a_x-r can be obtained by taking the r-th Hasse derivative in the physical R variable: each such derivative loses at most one unit of first-jet contact. This still falls short numerically here: subtracting12*181275 from the above bound leaves approximately3746839.5, below5636065. A detailed derivative proof is not used in the manuscript or ledger pending separate audit.

No proper helper, eliminated binding cell, or better.codes improvement follows from this attempted shortcut. The independent frontier agent identified the counterexample before any such claim was incorporated into the paper.
