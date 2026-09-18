# Rational parameterizations of modular guard curves

These formulas use the recorded F29 basis and parameters [a:b:c]. They
are derived directly from its coefficient rows, independently of any
parameter-plane factorization. They are not characteristic-zero formulas.
The universal binary-discriminant audit now includes these strata, so
separate analysis is optional rather than required for completeness.

The relevant coefficients are

```
B(X)  =25a+27b X^2+20c X^4,
C9(X) =12a X^5+b(25+15X^7)+17c X^2.
I(Z)  =a(23Z^8+10Z)+b(15Z^9+7Z^2)+c(20Z^10+2Z^3).
```

## Leading binary quartic

The repeated-root locus of the binary homogenization of B is the union
of a=0, c=0, and the conic `ac+4b^2=0`. The first two correspond to roots
at zero and infinity. Away from these, set r=X^2 and use the discriminant
of `20c r^2+27b r+25a`, which is `4b^2+ac` modulo29.
The conic has parameterization `[-4u^2:uv:v^2]`.

## Common B,C9 root

For a finite common root z, the two linear equations on [a:b:c] have
coefficient rows

```
(25,27z^2,20z^4),
(12z^5,25+15z^7,17z^2).
```

Their cross product gives the rational parameterization

```
[z^4(17+19z^7) : z^2(10+8z^7) : 16+22z^7].
```

The rows never become dependent at finite z: at z=0 the last coordinate
is16, and setting the last coordinate to zero at nonzero z forces
z^7=23, where the other two parenthetical expressions are19 and20.
The projective parameter z=infinity maps to [1:0:0], precisely the common
root at base infinity for the fixed-degree binary homogenizations.
Thus this gives a complete rational cover of the resultant guard curve.
No claim about the degree or birationality of this parameter map is needed.

## Repeated weighted-infinity root

I has a fixed root Z=0, repeated exactly when a=0. For a nonzero repeated
root z, write I=ZJ and impose J(z)=J'(z)=0. Put v=z^7. The cross product
of the two parameter coefficient rows gives

```
[z^2(14+12v+10v^2) : z(18+25v+8v^2) : 12+2v+26v^2].
```

This parameterizes the nonzero repeated-root incidence. The three
parenthetical expressions have no common zero: eliminating the quadratic
term between the first and third forces v=23, at which the second is11.
The parameter z=infinity maps to [1:0:0]. Separately, the degree-ten
binary I has a multiple root at infinity only when c=b=0; this is the same
axis point. Hence the repeated-root guard consists of the a=0 line and
the image of the displayed rational parameter map (including its limits).

These are potential rational parameter families, not excluded members.
Coincident pole images and nonordinary unselected fibers are allowed by
the construction. Substituting these maps into the homogeneous residual
discriminant gives univariate algebraic candidate conditions without a
ground-field parameter scan.
