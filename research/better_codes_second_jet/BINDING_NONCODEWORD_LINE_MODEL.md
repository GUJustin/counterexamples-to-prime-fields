# A binding primary/simple-tail model on a non-codeword line

**Independent audit: PASS.** The earlier binding simple-tail model remains
valid after an explicit polynomial jet shift that removes the line-of-codewords
limitation. It still has only a singleton selected seed, and it does not provide
universal primary-kernel divisibility or the missing target retained source.

Take n=262144,w=131071,m=118,A=181275, a squarefree monic domain locator
Lambda of degree n, and characteristic zero or p>n. Put

    S=X^(w+1),  W=Y-ZS,  U=R-ZS',
    F=W^55+Lambda^10*(U^12+U+Z^3261)-Lambda^9*Lambda'*W,
    Q0=F*W^108.

Use the received word r_x(Z)=Z*S(x) at all domain nodes.

## Irreducibility, exact caps, and primary slack

The change from independent variables (W,U,Z) to (Y,R,Z) is an invertible
polynomial translation over k[X,Z]. It therefore preserves the irreducibility
already proved for the earlier binding carrier. Alternatively the same
Eisenstein proof applies in the translated coordinates. The Y^55 coefficient
is still one, so the source has no hidden X-content factor.

The exact caps of F remain

    deg_R F=12,  deg_(Y,R) F=55,  deg_(Y,R,Z) F=3261.

Here S and S' are X-coefficients, so multiplying them by Z introduces only
one degree in the joint jet/challenge grading. Its exact weighted degree is

    55(w+1)=7208960.

The competing Lambda^10 U^12 term has weight4194292, and the linear terms
have weight2752511, so they cannot cancel the highest-weight contribution.
For Q0 the corresponding exact data are contact118 (proved below),
R-degree12, joint jet degree163, joint jet/challenge degree3369, and weight

    163(w+1)=21364736 < m*A=21390450.

Thus it fits the repaired primary caps (36,163,176421), with strict weight
slack25714. The factor charge is

    e(F)=55(w+1)-10w=5898250,

and the full source charge is163(w+1)-118w=5898358, below5924072 by25714.
The shift costs163 weight units compared with the previous primary source.

## Actual formal contact

At X=x+t and Y=ZS(x)+tR+t^2E, let

    U0=R-ZS'(x).

Then W=tU0+O(t^2), U=U0+O(t), and Lambda=t*Lambda'(x)+O(t^2).
The order-ten contributions from Lambda^10 U and -Lambda^9 Lambda'W
cancel. The remaining order-ten coefficient is exactly

    Lambda'(x)^10*(U0^12+Z^3261),

which is a nonzero polynomial in the independent formal variables R,Z.
Hence F has actual contact ten at every node. W has actual contact one,
so Q0 has actual contact118. Equivalently, W=tU+t^2 E_new with E_new a
regular affine translation of E; the formal jet-coordinate change is invertible.

## Regular seed and the actual first-tail multiplicity

At Z=0, the polynomial P=0 solves F(X,P,P',0)=0, and the separant there
is F_R=Lambda^10, a unit over the generic-X field k(X). The linearized
surface equation is

    Y'=Z*S'+(Lambda'/Lambda)*(Y-ZS).

With DZ=0, its solutions are Y=ZS+C*Lambda. Consequently the linear part
of the j-th ODE derivative of Y is

    Z*S^(j)+(Y-ZS)*Lambda^(j)/Lambda.

For j=w+1, the coefficient of Y is Lambda^(w+1)/Lambda, which is nonzero
in characteristic zero or p>n. Since F_R is a unit and this first-tail
linear form has nonzero Y coefficient after eliminating R, their intersection
is a smooth reduced curve at the selected point. A first-tail component
through the point therefore has multiplicity one.

This is also true for the actual cleared tail used in the cached primary
proof. The identities iterate_Y_eq_numerator and globalTailCut_eq multiply
this ODE derivative by a power of F_R and by (-X)^(w+1), respectively.
Both are units at the generic-X selected point. Hasse normalization adds
only the invertible factorial (w+1)!, so none of these conventions changes
the simple-component conclusion.

## The received line is genuinely non-codeword

For every nonzero label z, the word zX^(w+1) on n>w+1 nodes is not the
evaluation of a polynomial of degree at most w. Otherwise their nonzero
difference, of degree w+1, would vanish at n distinct points. The label-zero
word is the zero codeword and supplies the selected seed above.

More strongly, at any common-support correlated-agreement threshold greater
than w+1 there is no ordinary correlated-agreement witness for this line:
the slope polynomial of a codeword pencil would have degree at most w and
would have to agree with S=X^(w+1) on more than w+1 nodes. This is impossible
by the same root count. In particular this applies to A=181275. The example
still exhibits only one selected exceptional label, not a growing bad-label set.

At the pinned prime p=2130706433, p>n and p>mA; the shifted source therefore
introduces no small-characteristic or coefficient-degree issue. The unchanged
(r,y,t)=(12,55,3261) carrier flags preserve the previously checked numerical
mixed-degree guards. This does not assert the unconstructed retained
second-jet source, universal kernel-factor requirement, or a full benchmark
certificate. It shows that primary-source and simple-tail compatibility alone
cannot dismiss the binding cell even after requiring a non-codeword line.
