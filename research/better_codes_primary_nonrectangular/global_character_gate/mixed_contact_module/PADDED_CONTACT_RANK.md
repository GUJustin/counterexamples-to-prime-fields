# Exact multiplicity-two contact ranks on the complete ten/eleven sources

The source is the entire weighted polynomial box

`V={F(X,Y,R): wt(F)<14}, wt(X,Y,R)=(1,3,2)`.

It has 123 monomials. No joint-degree or derivative-degree restriction is imposed beyond this weighted cap; in particular it contains every capped monomial support requested for this test and every non-prefix or cancellation-based linear subspace obeying the same cap.

At m=2 the local substitution is X=x+t,Y=w+tR+t²E. For `F=ΣR^j F_j(X,Y)`, the contact rows are the coefficients of

`Σ F_j(x,w)R^j`, and `Σ (∂X F_j(x,w)R^j+∂Y F_j(x,w)R^(j+1))`.

There are fourteen possible local rows for this full weighted box. The exact matrices are assembled over the actual quadratic coefficient fields, then restricted to rational matrices using the basis (1,theta). Rational rank is twice the field rank.

|Source|Word|Columns|Rows over source field|Exact rank|
|---|---|---:|---:|---:|
|Complete ten, n18, Q(sqrt17)|Original|123|252|123|
|Same nodes|First received value plus1|123|252|123|
|Complete eleven, n19, Q(sqrt39)|Original|123|266|123|
|Same nodes|First received value plus1|123|266|123|

The perturbations are controls, not claims about generic words. Since the original full boxes are injective, all smaller source spaces are injective as well. In particular:

* Riccati support `{1,Y,Y²,R}` with full allowed X prefixes:45 columns,72/76 local rows;
* joint degree≤2,R-degree≤1:54 columns,90/95 local rows;
* all weighted monomials with R-degree≤1:70 columns,90/95 local rows.

The source words are taken from the stable rational source and padding certificates. `padded_contact_rank.py/json/resources.json` records the coefficient-field construction, full column ordering, exact ranks, and bounded execution receipt. The four computations together completed in under one second.

No multiplicity-two non-prefix direction remains inside this strict weighted box on these fixed words: a linear change of source basis cannot change injectivity. A next meaningful mechanism must change the multiplicity, the actual received line (nonzero challenge direction), or prove a large-list-dependent structural theorem unavailable for these finite lists. This result does not assert maximal rank at the benchmark multiplicity115, and it does not justify another blind multiplicity/support scan.
