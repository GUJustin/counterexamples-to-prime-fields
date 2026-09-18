# The six-coset bank cannot start the proposed one-pole induction

This is the rational-function extension of the archived polynomial Mason argument in `Documents/mca_exponent_one/rounds/R15_H_RAW.md`. The idea and degree ledger were proposed independently by the root agent; the proof below checks the denominator, common factors, exceptional identity, and characteristic bound. It closes this particular seed, not the general one-pole operation.

## Statement

Let m>=1, let k be an algebraically closed field of characteristic zero or characteristic p>200m, and put M=98m. On mu_(2M), let the received word be x^M. Add any 4m distinct coordinates outside this group, with arbitrary received values. There is no proper rational function

    R=N/P,  P=X−a,  deg N<=50m,

whose pole is outside this 200m-point domain and which agrees with the word at 98m or more coordinates. The conclusion holds over every extension of a prime field satisfying these conditions.

Consequently the explicit six-word bank of length 200m and degree cap 50m−1 in the preceding report cannot supply the input to the one-pole extension operation, regardless of the word values on its added coset.

## Proof

Suppose such a function exists. It has at least t>=94m agreements on mu_(2M). Properness is N(a)!=0. Put d=deg N. Since agreement points are roots of N²−P², and that polynomial is nonzero, t<=max(2d,2). Thus d>=47m>=2 and deg(N²−P²)=2d.

Let

    G=gcd(N²−P², X^M P−N)

be monic. Every common root has P!=0, so substitution yields X^(2M)=1; conversely each agreement point is a common root. The gcd is squarefree. Indeed at a common root x, N(x)=x^M P(x), and if the derivative of N²−P² vanishes then

    N'(x)=x^M P'(x).

The derivative of X^M P−N there is therefore M x^(M−1)P(x)!=0. Hence deg G=t exactly. Define the coprime polynomials

    E=(N²−P²)/G,        Q=(X^M P−N)/G,
    e=deg E=2d−t,      r=deg Q=M+1−t.

The latter degree is exact because d<=50m<M+1. Completing the square in

    Q(N²−P²)=E(X^M P−N)

gives

    F²=4EQP X^M+C,
    F=E+2QN,           C=E²+4Q²P².                     (1)

Since d+r−e=M+1−d>0, deg F=d+r. If C is nonzero, put c=deg C. Then

    c<=max(2e,2r+2)<=max(12m,8m+4)<M.

Here d<=50m and t>=94m were used.

The three terms of (1) have no common root except possibly X=0. A root of Q cannot be a root of C, because E,Q are coprime. A root of E could be a root of C only if it were a root of P; but at the pole a, both numerators defining E and Q are nonzero, so E(a)Q(a)!=0. In particular C(a)=E(a)²!=0. These observations also cover the case a=0: then C(0)!=0 and no common factor occurs.

If C(0)=0, then E(0)Q(0)P(0)!=0. Since c<M, equation (1) gives

    ord_0 C=ord_0 F²=2h<M

for some integer h>=1. Otherwise set h=0. Dividing (1) by X^(2h) gives three pairwise coprime polynomials. Their maximum degree is 2(d+r)−2h; all degrees are at most

    2(d+r)<=112m+2<200m<p.

Thus the positive-characteristic p-th-power exception to polynomial Mason–Stothers is impossible. At least one term is nonconstant, and the ordinary radical-degree form of that theorem applies. Bounding the three radical degrees respectively by

    d+r−h,       e+r+2,       c−2h

(the middle bound includes the possible roots of P and X) yields

    2(d+r)−2h <= (d+r−h)+(e+r+2)+(c−2h)−1,

and therefore

    d <= e+c+1−h <= max(3e+1, e+2r+3).

Substitution gives

    3t <= max(5d+1, d+2M+5)
        <= max(250m+1,246m+5)
         = 250m+1.

But t>=94m implies 3t>=282m>250m+1. This is a contradiction.

It remains to handle C=0. Over the algebraically closed field, E=epsilon*2i QP for epsilon in {1,−1}. Since E,Q are coprime, Q is a nonzero constant. Equation (1) becomes F²=constant*P² X^M. The integer M=98m is even, so F=gamma P X^(M/2) for a nonzero constant gamma. But F=E+2QN then implies P divides N, contradicting N(a)!=0. This disposes of the exceptional identity and finishes the proof.

## Consequence for the search

The six-coset seed is an actual prime-field high-agreement bank, but it is not a viable starting point for the particular fresh-one-pole induction. Increasing p, passing to an extension, choosing the added 4m received values differently, or varying the pole cannot evade the proof.

This does not exclude one-pole growth from a different word with a richer value structure, a different rational denominator degree with a separately audited degree/agreement budget, or a different mechanism entirely. It supplies no stronger lower bound. The previously written recommendation to test this exact six-coset seed is now resolved negatively and should not trigger a numerical search.
