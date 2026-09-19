# Exact threshold classification for the odd trace–norm compiler

2026-09-19. A complete algebraic classification at the previously established threshold. This strengthens the exact finite output of the inherited construction; it does not claim a new fixed-rate or superlinear-population regime. No codeword enumeration is required.

## Statement

Let p>=3 be prime, s>=2, Q=p^s, B=F_(Q^2), and let K be any field containing B. Put

`n=Q^2, Lambda=X^n-X, d=(n+Q)/p, T=n-d,`

`D=n-n/p, k=(p-1)T/p`.

Every monic polynomial W in K[X] of the form

`W=X^D+C, deg C<=k`

has at most T distinct roots in B. Equality holds if and only if W is exactly one of the normalized trace–norm polynomials

`G_(a,b)=Tr_(F_Q/F_p)(a(X+b)^(Q+1))+1,`

`F_(a,b)=a^(Q/p)(X+b)^(Q/p),`

`P_(a,b)=F_(a,b) Lambda/G_(a,b),`

where a in F_Q* and b in B. In particular, equality forces W to have coefficients in B even when its coefficients were initially allowed in the larger field K.

For beta in K outside B, define on B

`f=(X^D-beta^D)/(X-beta), g=1/(X-beta)`.

At agreement threshold T for strict-degree-<k Reed–Solomon witnesses, the line f+lambda*g has precisely M=n(Q−1) exceptional finite labels, namely lambda=P_(a,b)(beta). Each has exactly one threshold witness, and its nearest agreement is exactly T. Every other finite label has agreement at most T−1. The reciprocal direction g has agreement exactly k<T.

The already proved every-exterior-pole injectivity of these M labels is used for the last assertions and recalled below.

## 1. The residual-degree bound

The leading terms cancel in

`Delta_W=W^p-Lambda^(p-1)`.

Since the first nonleading degree of Lambda^(p−1) is (p−2)n+1, while

`pk-[(p−2)n+1]=(Q−p)(Q+1)/p>0`,

we have `deg Delta_W<=pk=(p−1)T`.
The polynomial Delta_W is not zero: every root of Lambda has multiplicity p−1 in Lambda^(p−1), whereas every root of W^p has multiplicity divisible by p. Equivalently, the nonzero derivative of Lambda^(p−1) precludes it being a pth power.

## 2. Factoring the complete native root set

Let A be the number of distinct roots of W in B. Let V be the monic locator of all those roots, put L=Lambda/V in B[X], and write H=W/V in K[X]. Both V and L are squarefree and coprime. Then

`Delta_W=V^(p−1) [H^p V-L^(p−1)]`.

If A>T, the first factor has degree greater than the entire allowed degree of Delta_W, impossible since Delta_W is nonzero. Hence A<=T.

Suppose A=T. The bracket must be a constant c, and it is nonzero. Since T>0, choose v in B with V(v)=0. Then

`c=−L(v)^(p−1) in B*`.

Multiplying the constant-bracket identity by L gives

`L^p+cL=Lambda H^p`.                                      (1)

Thus H^p belongs to B[X]. Frobenius is an automorphism of the finite field B, and pth roots are unique in every field of characteristic p. Consequently H belongs to B[X], and W belongs to B[X]. This is the required descent for extension-alphabet witnesses; it does not assume that the original witness coefficients were native.

Set alpha=L(v) in B* and G=L/alpha. Since c=−alpha^(p−1), equation (1) becomes

`G^p-G=Lambda (H/alpha)^p`.                               (2)

In particular G(B) is contained in F_p. Also deg G=deg L=n−T=d, and G is squarefree with all its roots native.

## 3. Exact p-shadow classification at this degree cap

We now prove that every G in B[X] with degree at most

`d=p^(2s−1)+p^(s−1)`

and G(B) contained in F_p has the form

`Tr_(F_Q/F_p)(a X^(Q+1)) + Tr_(B/F_p)(l X) + c0`,          (3)

where a in F_Q, l in B, c0 in F_p.

The functional condition is exactly G^p=G modulo X^n−X. Polynomial representatives of degree<n are unique. On nonzero exponents less than n−1, multiplication by p modulo n−1 rotates the2s base-p digits cyclically. Hence the nonzero coefficient support of G must contain each complete cyclic orbit, and every exponent in that orbit must remain at most d. The exponent n−1 is absent because d<n−1.

Every digit is at most one: otherwise rotation puts a digit at least two in the leading position, producing an exponent at least2p^(2s−1)>d. If two positions contain ones, orient either one to the leading position. The other must then occur at position at most s−1, so the cyclic distance in either direction between the two ones is at least s. Their distance must therefore be exactly s. Three or more ones are impossible. Thus the only allowed nonzero orbits are:

- a single one, giving exponents1,p,...,p^(2s−1);
- two antipodal ones, giving exponents(Q+1),(Q+1)p,...,(Q+1)p^(s−1).

The coefficient Frobenius relations on the first orbit yield Tr_(B/F_p)(l X). Those on the second orbit have period s, forcing their initial coefficient into F_Q and yielding the norm trace in (3). The constant coefficient lies in F_p. Conversely all polynomials (3) have the required values and degree cap. This proves the classification, not merely a support containment.

## 4. Squarefreeness recovers the normalized bank

For the G in (2), its degree is exactly d, so the norm coefficient a in (3) is nonzero. There is a unique b in B with l=a b^Q. Completing the norm writes

`G=Tr_(F_Q/F_p)(a(X+b)^(Q+1))+c1`, c1 in F_p.

The level c1 is nonzero. Otherwise the center −b would be a root of multiplicity Q+1, contradicting squarefreeness of G. Normalize by c1:

`G0=G/c1=Tr_(F_Q/F_p)((a/c1)(X+b)^(Q+1))+1`.

Differentiating (2), using Lambda'=-1, gives

`G'=(H/alpha)^p`.

Therefore the unique pth root of G0' is `F0=H/(alpha*c1)`, since c1 belongs to F_p. It is precisely the polynomial F attached to the normalized parameters(a/c1,b). Hence

`F0 Lambda/G0 = H Lambda/L = H V = W`.

This proves that equality A=T recovers exactly an existing bank member. Conversely every such member has exactly T distinct native roots by its previously proved split trace–norm construction.

## 5. Exact lists and the final endpoint chart

For any degree-<k approximation h to f+lambda*g, its residual

`W=X^D-beta^D+lambda-(X-beta)h`

is monic of degree D, has correction degree at most k, and satisfies W(beta)=lambda. Agreements on B are exactly its native roots. By the classification, agreement at least T forces W=P_(a,b) and lambda=P_(a,b)(beta). Conversely the existing displayed witness realizes each such label with exactly T matches.

For completeness, the M normalized members have distinct exterior evaluations: equality of P-values forces G1(beta)/G2(beta) in F_p* by their pth-power identity. Every nonzero trace–Hermitian difference splits over B, so evaluation at beta outside B is injective on that difference space. Thus G1=uG2 as polynomials; their derivatives give the same center and proportional norm coefficients, and their normalized value1 at the center forces u=1. Each label therefore determines one W and then one h. This proves singleton threshold lists, not merely one exhibited witness per label.

For the original finite challenge field E=F_(Q^4) (or a field containing the required root), let c_*^p=Lambda(beta)^(p−1). Retain the established endpoints

`r0=f+c_*g, r1=c_*g`.

Their source bounds remain `agr(r0)<=U=floor(((p+1)k−1)/p)<T`, `agr(r1)=k`, and their ordinary common agreement is k. The known labels are nonzero, and c_* is not among them by the source bound. The invertible affine parameter formula

`t=1−c_*/lambda`

therefore gives exactly M interior exceptions for(r0,r1), with singleton threshold lists and nearest agreement exactly T. Every other affine parameter has agreement at most T−1; at t=1 the sharper exact agreement k holds. All previous first-order/Johnson placements and source bounds remain unchanged.

## Finite and prior-work scope

For p3,s2, this proves exact648 singleton threshold lists at T51 for RS34 on81 native coordinates, over F_(3^8), rather than only648 certified labels. The finite fixture verifies the displayed bank; the global absence and uniqueness claims above are algebraic and do not rely on codeword enumeration.

The fixed-rate, constant-margin, n^(3/2) population regime remains inherited. This result upgrades the exact classification of the already existing normalized family and the finite statement. It neither changes the alphabet to a prime field nor provides a prescribed short-domain construction or a better.codes improvement.
