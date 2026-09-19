# Growing witness degree: Frobenius match bound (candidate)

This addresses the all-new-witness issue under code enlargement on the
quarter-density domain D0 union D1', with NO neutral padding coordinates. It does not
preserve the first-order placement when the message dimension grows unboundedly.

Let B=F_(p²), and let P in B[X] have actual degree d>2. Any t in B satisfying
t^(2p)=P(t) also satisfies, with z=t^p,

    z²=P(t),   P^sigma(z)=t²,

where sigma raises coefficients to p. Write P^sigma(Z)=E(Z²)+Z O(Z²).
Every match is a root of

    R(X)=[X²−E(P(X))]²−P(X) O(P(X))².

This polynomial has exactly degree d² and nonzero leading coefficient.
For even d, E has degree d/2, and E(P)² uniquely contributes degree d²;
the other product has degree at most d(d−1). For odd d, O has degree
(d−1)/2, and P O(P)² uniquely contributes degree d². Terms involving
X² have lower degree because d>2. Thus there are at most d² matches.

For coefficients over the ambient E=F_(p⁴), restrict a degree-d explanation
to either of the two B-lines composing D0={x!=0:x² in B*}. After rescaling,
the same equation holds. If every coefficient is in B, use the bound above.
Otherwise apply a B-linear functional E->B annihilating B and nonzero on
some coefficient. The resulting nonzero polynomial has degree at most d,
and every match is its root. Hence each B-line has at most d² matches.
The same argument works on the scaled second block, including arbitrary
line parameter and arbitrary puncturing. A genuinely degree-d explanation
therefore has at most 4d² matches on the two active blocks.

Consequently, for any integer D>=3 with 4D²<=2p, enlarging the code to
dimension D+1 introduces no additional explanation above A=2p. All the
quadratic-bank threshold lists and exact source/common agreements in the
quarter-density construction remain unchanged. Its existing simultaneous
quadratic explanations still attain A. This allows message dimension of
order sqrt(p), with rate of order p^(−3/2), but the source and tested
agreements remain of order p and the length of order p².

Critical limitation: for D+1>=4 the old tested threshold below sqrt(2n)
lies below the new first-order curve, since
n*a1((D+1)/n)>sqrt((D+1)n/2)>=sqrt(2n).
This is a growing-dimension tradeoff only. It is not an improvement in the
same first-order regime, not constant rate, and not a practical-domain result.
Independent review of the two-active-block statement passed; the proof is
scoped to the quarter-density domain, not the older neutral-padded domain.


The older length-9p² construction with neutral values f=X³,g=0 is explicitly
excluded: after dimension reaches four, the codeword X³ agrees with every
finite pencil word on all its 5p²+4 neutral coordinates. The active-block
bound cannot be used to preserve that older construction's source distances.


For BabyBear p=2013265921 one may take D=31727, hence message dimension31728:
4D²=4026410116<=4026531842=2p. The same n=10133099171649945602,
T=4501799456 and full exceptional-list profile remain. The rate is only
about3.13e−15. This illustrates a real dimension increase, not a practical
rate, and the threshold is no longer above the first-order curve of that code.
