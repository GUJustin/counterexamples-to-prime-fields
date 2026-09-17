# Independent sharpness check against the actual lower proposition

2026-09-17. Checked research/fixed_singular_cover/appendix.tex, Proposition all-singular-linear-lower and its proof, rather than relying on the working-note summary.

The equation is

    U=v-zD X^(D-1),
    Q=R0(X)(X-z)U+U^2.

It is independent of the value variable, has total jet degree two, challenge degree at most two, and leading coefficient one in v^2. Therefore its ordinary core is empty. The discriminant in v is R0(x)^2(x-z)^2. Its persistent rational-Hermite core consists exactly of the original fixed subset, of size s. Outside that core, the only singular label at coordinate x is z=x.

With n=100m, D=25m-1, s=48m-1 and A=48m:

    dimension D+1=25m, hence exact rate 1/4;
    A-D=23m+1;
    A-sqrt(D*s/2) > (48-sqrt(600))*m > 23.5m.

These are fixed positive signed margins. Even the weaker uniform-core condition A>sqrt(D*n/2)+epsilon*n holds, for example with epsilon=0.12. The positive-rate lower bound D/n>=0.24 holds for every m>=1. Characteristics can be chosen above every fixed interpolation threshold as well as D.

The proposition supplies n-s=52m+1 distinct selected labels, each with exact full support S0 union {x_i}, and excludes a direction polynomial on ANY A coordinates under its displayed random-direction inequality. Its ordinary-CA failure is thus stronger than merely full-support failure. The inequality holds for sufficiently large primes, which suffices for the sharpness family.

Consequently the O(n) order of the new actual-solution theorem cannot be improved uniformly to o(n), already for quadratic derivative degree, challenge degree two, and empty ordinary core. This is sharpness in block length for this bounded-complexity class, not sharpness of gap-dependent constants or an unrestricted first-order quadratic lower bound.

## Why obvious products and unions do not improve the lower order

For polynomial equations Q1,Q2, the identity Q1(X,z,P,P')*Q2(X,z,P,P')=0 in the integral domain F[X] means that one factor vanishes identically. Thus a fixed product merely unions a fixed number of actual solution families. If each has O(n) bad labels under its applicable margin/core conditions, so does their union. In particular, multiplying two copies of the present quadratic equation does NOT produce a superlinear lower example, even though its derivative degree is four and it admits two repeated derivative branches.

Letting the number of factors grow would leave the bounded-complexity hypothesis. Concatenating a fixed number of examples likewise only adds O(n) labels and lengths; a growing concatenation does not automatically remain a Reed--Solomon code at the intended degree. A Cartesian product of label sets introduces multiple independent challenges and does not directly furnish a one-parameter line with product-many distinct labels.

Any superlinear first-order lower result therefore needs more than the syntactic change from derivative degree two to four: it needs a genuinely new interacting source, an ordinary core large enough to invalidate the signed margin, or an equation-complexity regime outside the theorem. No such intrinsic amplification is proved here.
