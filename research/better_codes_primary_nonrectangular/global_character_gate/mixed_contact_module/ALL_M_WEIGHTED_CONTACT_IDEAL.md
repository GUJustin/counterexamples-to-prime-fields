# Exact all-m weighted first-jet contact ideal

## Definition and distinction from ordinary line contact

Throughout, contact means the archived primary interpolation substitution

`X=a+t, Y=w_a+tR+t²E`, with R,E algebraically independent,

and vanishing modulo t^m. For a received affine line replace w_a by f_a+Zg_a, with Z another independent coefficient variable. The actual rows used in the archived global gates have indices `(a+u+2v,j+u,v)`, where v is the E exponent. Thus this is **weighted first-jet contact**, not substitution with E set to zero.

Locally put h=X−a and L=Y−w_a−hR. The weighted kernel is

`K_(a,m)=(h^u L^v : u+2v≥m)`.

Indeed substitution sends h^u L^v R^j to t^(u+2v) E^v R^j, so coefficients of distinct E/R monomials cannot cancel. In contrast, ordinary affine-line contact has ideal `(h^m,L)`. They coincide for m=1,2 but already differ at m=3:

`weighted: (h³,hL,L²)`, versus `ordinary line: (h³,L)`.

In particular L itself has weighted contact exactly2 and must not be admitted at m3. Ordinary fat-point powers `(h,Y−w_a)^m` are a third filtration, also different from the weighted one.

## Uniform global generators, using only order-two Hermite data

Let S(X)=∏(X−a) be the monic squarefree node locator, deg S=n. Choose Hermite polynomials A,B of degree below2n satisfying

`A(a)=w_a, A′(a)=0; B(a)=0, B′(a)=1`.

For a received line use A=A_f+Z A_g, with the same zero-derivative conditions for each intercept/direction Hermite polynomial. Put

`H=Y−A(X)−B(X)R`.

Then for EVERY positive m the global weighted contact ideal is exactly

`K_m = ( S^max(m−2j,0) H^j : 0≤j≤ceil(m/2) )`.           (1)

At each node S is h times a unit, while H=L+h²C(X,R,Z). The change from L to H preserves the weighted monomial filtration wt(h)=1,wt(L)=2: both it and its inverse add a term of weight at least2. Hence (1) localizes to K_(a,m). Outside S=0 both ideals are the unit ideal. Equivalently Chinese remaindering modulo S^m proves global equality. The same A,B work for all m; this would be false for the ordinary-line filtration.

For explicit construction, let f be the degree-below-n received interpolant, let b be the inverse of S′ modulo S, and let c be f′b modulo S. Then A=f−Sc and B=Sb satisfy the required Hermite conditions. For a received line apply this to f and g separately for A and keep the same B.

If I=(S,Y−f) is the ordinary ideal of the received plane points, extended by R, then

`I^m ⊆ K_m ⊆ I^ceil(m/2)`.

These inclusions do not equate the filtrations or their weighted source dimensions.

## Exact unfiltered Hilbert function and syzygies

Because H is monic of degree one in Y and S is monic of degree n in X, the full polynomial ring has a unique expansion over k[R] (or k[R,Z]) in

`X^d S^u H^v, 0≤d<n, u,v≥0`.

Modulo K_m, retain exactly u+2v<m. Therefore the quotient is free over k[R] (or k[R,Z]) of rank

`n * sum_(v=0)^floor((m−1)/2) (m−2v) = n*floor((m+1)²/4)`.

Its associated contact-graded Hilbert series is `n/((1−t)(1−t²))`. This counts contact order, not the original interpolation weights `(1,w,w−1)` or joint/challenge caps.

The generator syzygies are universal. For adjacent generators G_j with exponent drop two, `H G_j−S² G_(j+1)=0`. For odd m, the last exponent drops one and the last relation is `H G_h−S G_(h+1)=0`. These adjacent relations generate the syzygy module, as for the corresponding monomial ideal in the regular sequence (S,H). Thus a list of nearby polynomials cannot create extra *abstract* syzygies of this ideal. Any benefit must appear in its original-weight initial ideal or filtered regularity after replacing H by its received-word-dependent expression.

This identifies the concrete missing optimization: compute the degree/cap-filtered dimension of K_m, not only its contact-graded length. The Hermite change is not weight-preserving; high X terms in A,B can cancel across the universal generators. A valid positive certificate would exhibit such a cancellation inside all original weighted, Y/R, and challenge caps, or prove a list-size hypothesis forcing that filtered Hilbert-function excess.

## Cost-selected multiplicity-three test

The earlier three-quadratic example has six distinct pair-intersection nodes and four agreements per candidate. At m3, strict cap12 and weights(1,2,1), two shapes were selected before computation because their source columns are BELOW the sums of exact local ranks and no automatic product kernel was identified:

|Joint Y/R cap Q|R cap S|Columns|Sum of local ranks|Original rank|One-value perturbation rank|Independent word-control rank|
|---:|---:|---:|---:|---:|---:|---:|
|2|1|50|54|50|50|50|
|2|2|60|66|60|60|60|

The controls are explicit, not a claim that every generic word has maximal rank. One full-rank control suffices to establish generic maximal rank for that shape; the list-conditioned example is full rank as well. The matrices include free-E rows, so they test weighted first-jet contact and distinguish it from ordinary-line contact. Files `m3_three_graph_gate.py/json/resources.json` retain the exact rational computation, completed in under one second.

No list-conditioned rank defect is found here. The all-m ideal description is the concrete structural result; it does not itself improve the benchmark ledger or justify an unstructured higher-m scan.
