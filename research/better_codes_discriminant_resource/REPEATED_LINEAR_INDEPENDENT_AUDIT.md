# Independent audit: high repeated linear factors force one affine pencil

**PASS**, conditional on the stated universal-factor own-system inequality and binding caps. This covers a linear Y-factor of multiplicity at least27, including the maximal multiplicity43 branch. It does not cover every repeated leading coefficient.

## Exact arithmetic independently checked

Use n=262144, w=131071, Aagreement=181275, own ambient dimension C=6802316684345, and the previously independently checked local ranks R(a), 0<=a<=67. If b_x is the order of the leading Y coefficient, then sum b_x<=12 and a_x<=43+2b_x.

For h=0 and h=16, direct rational arithmetic verifies all68 inequalities

R(a)<=R(h)+(R(43)-R(h))*1[a>h]+(12474280/3)*max(0,ceil((a-43)/2)).

Replacing the final minimum order by the actual b_x preserves the inequality. Summing and using sum R(a_x)>=C-1 yields:

|h|R(h)|number of nodes a_x>h, at least|after 12 leading-coefficient exceptions|overlap with any 181275-set|
|---:|---:|---:|---:|---:|
|0|0|218594|218582|137713|
|16|3707136|212704|212692|131823|

R(43)=31118386. `REPEATED_BRANCH_INDEPENDENT_ARITHMETIC.json` contains the exact rational bounds and all68 slack values for each threshold. This independently checks the LP certificate arithmetic using the previously audited rank table; it is not a new optimization claim.

## Factor normalization and the weight argument

Write the leading physical R coefficient as

A_r(X,Y,Z)=G(X,Y,Z)^e H(X,Y,Z),

where deg_Y G=1 and e>=27. Work initially over k(Z), or an algebraic extension if the factorization requires it. By Gauss's lemma, choose G,H polynomial in X,Y; their coefficients may be rational or algebraic in Z. Let h=deg_Y H=43-e<=16.

Weighted degrees in X,Y are additive on nonzero products. The binding caps give wt(A_r)<=43w+12, while wt(H)>=h w and wt(G)>=w. Consequently

e(wt(G)-w)<=12.

Since weighted degrees are integers and e>12, wt(G)=w. Thus G=c(Z)Y+d(X,Z), with c nonzero and independent of X and deg_X d<=w. Also wt(H)<=h w+12, so the leading Y coefficient of H has X-degree at most12. This argument rules out an X-dependent denominator in the root of G; it does not assume the factor is already monic.

## Valid fixed-X multiplicity use

The audited local Newton lemma at X=x says that A_r(x,Y,Z) has a Y-root at the received affine value f_x+Zg_x of multiplicity at least a_x. This is the legitimate fixed-X statement, not the previously rejected claim about X-vanishing along a candidate.

Outside at most12 nodes where the leading Y coefficient of H vanishes identically over k(Z), H(x,Y,Z) is a nonzero polynomial of degree h. If a_x>h and G(x,f_x+Zg_x,Z) were nonzero, all root multiplicity would come from H and be at most h, a contradiction. Hence every such node lies on the rational graph

Pstar(X,Z)=-d(X,Z)/c(Z).

For e>=27, the h=16 row gives at least212692 such nodes. For e=43 the h=0 row gives at least218582.

## Specialization and descent: no exceptional challenge labels

Choose any w+1 of these persistent nodes and interpolate the two received coefficient vectors separately. This produces P0,P1 in k[X], both of degree at most w. The polynomial in X

Pstar(X,Z)-P0(X)-ZP1(X)

has degree at most w and vanishes at w+1 distinct base-field points. Therefore it is identically zero over the coefficient extension. In particular the monic graph descends to the original field and is affine in Z.

At every persistent node, the equality

P0(x)+ZP1(x)=f_x+Zg_x

is an identity of polynomials in Z. It therefore holds at EVERY specialization, including zeros of any denominator used in the original factor normalization. No challenge-label exceptions are introduced. The same reasoning works if the initial factor was defined only over an algebraic extension of k(Z).

Now fix any challenge lambda and any polynomial P of degree at most w agreeing with the received word in at least181275 coordinates. Its agreement set meets the persistent set in at least

212692-(262144-181275)=131823>w.

Thus P=P0+lambda P1. All nearby candidates at all challenges lie on this one affine codeword pencil. Indeed the persistent set itself has size212692>181275, so the received affine line has a common agreement support above the threshold with that pencil.

No division by e or q is used in this graph transfer. The characteristic assumptions are those needed for the imported source/rank facts and the existence of the distinct evaluation points, not an extra formal differentiation assumption.

## Consequence for routing

This is an actual simplification of this repeated-factor branch: its nearby-candidate set is a single persistent affine pencil, so treating it as a generic normal component is unnecessary once the appropriate line-level alternative is inserted. It is not yet a complete repaired benchmark ledger: factors with other multiplicity patterns, and the squarefree-leading branch, remain.
