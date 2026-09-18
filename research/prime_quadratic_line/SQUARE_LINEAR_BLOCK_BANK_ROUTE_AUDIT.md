# Square-linear bank: finite-field core and the planar multiplicity escape

September 18, 2026. The proposed signed-line bank has a concrete
finite-field realization with a dense regular core. It also admits
disjoint fresh blocks giving a constant relative gap. The construction
uses only the multiplicative group and polynomial root bounds, and
works over every odd finite field satisfying the size conditions.
No literature-priority or prime-specific separation claim is made.

The full finite lemma and integration-ready theorem are in
`square_linear_block_bank.tex`. This note records why the previous
planar obstruction does not apply, and independently checks the exact
profile used in that file.

## 1. A dense core from two signed-line directions

Let gamma generate Fp*, z=gamma², and let t²<(p-1)/2. Set

    a_i=z^i,  b_j=z^(tj),  0<=i,j<t.

The bank consists of Q_i=a_i X² and P_j=b_j. Every bank member is
the square of a linear polynomial, including the constant ones.
At x=±gamma^(tj-i), give the received word the value b_j and set
the direction to zero. The t² exponents tj-i are consecutive as a
set, and span fewer than (p-1)/2 residues. Thus all 2t² coordinates
are distinct. Exactly Q_i and P_j match at the corresponding pair.
Each bank member has 2t core matches, and an outside quadratic has
at most 2t core matches by the two-owner root count.

This is a complete bipartite intersection pattern between two
projective directions of signed lines, obtained entirely inside the
finite-field multiplicative group. It requires p=Theta(t²), rather
than an embedding of a small integer arrangement. For a pure quadratic
aX² whose coefficient is not one of the a_i, the core agreement is
exactly zero; this stronger fact is important below.

## 2. Why the earlier planar theorem loses its bounded multiplicity

Consider an arbitrary square-linear bank Q_(a,b)=(aX+b)² and suppose
f=c0*g on the informative coordinates E={x:g(x)!=0}. Let k=lambda+c0.
For k!=0, a match requires g(x) and k to have the same quadratic
character. On a character class write g(x)=epsilon*h_x², with epsilon
equal to 1 or to a fixed nonsquare. Choose tau²=k*epsilon. The match
condition becomes

    a*x+b = ±tau*h_x.

Thus the injective plane points (x,h_x) lie on one of two lines

    Y = ±(a/tau)X ± b/tau.

The reduction is planar, but its multiplicity is not bounded. Replacing
(a,b,tau) by (c*a,c*b,c*tau) leaves the two geometric lines unchanged,
while replacing the bank polynomial and k by c² times their values.
One line can therefore encode many distinct bank-label pairs. The
fixed conic bank had multiplicity at most two; the full rank-one cone
does not.

More precisely, a bounded number of bank polynomials on each scalar
ray would recover a bounded-multiplicity planar reduction. Distinct
bank-label pairs yielding one geometric line necessarily have
proportional linear polynomials, and hence scalar-multiple square
polynomials. The new bank deliberately has t members on each of two
such rays. The missing bounded-multiplicity hypothesis is therefore
an explicit mathematical failure, not simply an unavailable citation.

## 3. Block amplification and exact profiles

Use t disjoint fresh blocks E_j of D nonzero coordinates each, outside
the core. Put f=0 and g=x²/b_j on E_j. The remaining coordinates have
f=x³ and g=0. Exclude all nonzero intersections of X³ with the bank,
and with the 2t pure-quadratic witnesses at two chosen nonsquare
endpoint labels. Together with zero this excludes at most 6t+1 field
elements, so the sufficient domain-size conditions are

    D>4t+3,  t>=2,
    n>=2t²+tD,  p>n+6t+1.

At a nonzero label lambda, exactly the t pure quadratics

    (lambda/b_j) X²,  0<=j<t,

match an entire fresh block. A pure quadratic outside this list has
no fresh matches. Among the listed quadratics, a selected bank word
gains its 2t core matches and zero padding matches; any other member
has zero core matches and at most one padding match. Non-pure
quadratics have at most 2t core matches, 2t fresh matches, and three
padding matches. Hence they stay strictly below D.

The products a_i*b_j=z^(i+tj) are all distinct. Consequently, at
T=D+2t the exact successful set is

    {0} union {z^k:0<=k<t²}.

Every successful list is a singleton. The nonzero successful labels
have maximum agreement exactly T. At zero, the zero polynomial has
exactly tD matches, and all other polynomials have fewer than D.
Every other label has maximum agreement D or D+1, strictly below T.
The relaxed threshold-D list has exactly t members at every nonzero
label and exactly one at zero.

For either chosen nonsquare endpoint, all t pure witnesses have
coefficient outside {a_i}; the extra padding exclusions make their
agreement exactly D. Both endpoints therefore have exact maximum D.

Common agreement is also exactly D. A nonzero pure quadratic direction
explains at most one fresh block and has no zeros elsewhere. A non-pure
nonzero direction has at most 2t fresh matches and two zeros elsewhere.
A zero direction restricts the intercept to the core and neutral
block, where it has at most 2t+3 matches. The pair (0,X²/b_j) attains
D on E_j. These bounds prove the exact common-agreement claim.

In the planar reduction above, choose h_x=x/gamma^(tj) on block j.
All its points lie on Y=gamma^(-tj)X. For the t labels a_i*b_j, all
t selected bank words produce that same geometric line. Thus t²
successful nonzero labels need only t geometric lines, each containing
D points. There is no conflict with a point-line incidence bound.

## 4. Quantitative scope

The integration-ready choice D=14t and n=128t²+1 permits any prime
in (256t²,512t²), and gives

    source agreement = common agreement = 14t,
    successful threshold = 16t,
    successful labels = t²+1 > p/512,
    source loss / capacity margin = 2t/(16t-3) -> 1/8.

For t>=400 the established first-order upper bound is below 14t:

    sqrt(3n/2) <=13.857t,
    (3n/8)^(1/4) <=(8/3)sqrt(t) <=(2/15)t,
    13.857+2/15 <14.

Also (16t)²<2n exactly. More generally, D~c*t gives loss ratio
2/(c+2), with the same first-order comparison whenever
c>6+4sqrt(3). The achievable ratio can approach 1-sqrt(3)/2 from
below. The exceptional count remains Theta(n), the relaxed line-local
list size is Theta(sqrt(n)), and the rate is 3/n.

This answers the scoped construction question positively and shows
why the old fixed-conic planar gate does not transfer to scalar-rich
square-linear banks. It does not provide a superlinear exceptional
count, a fixed-rate example, a prescribed-domain result, or a
characteristic-specific separation.
