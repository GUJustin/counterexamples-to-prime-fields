# Exact amplitude curve for the C2 complement constraints

Use edge values x=e01,y=e02,z=e03,u=e12,v=e13,w=e23, all distinct,
and amplitudes a0,...,a3 with all eight signed values distinct. Define
H_ij as in the complementary-residual-quadratic construction. Clearing
only the guarded denominators a_i-a_j gives the three quadrics

    E1=y(z-u)a0a2+z(v-y)a0a3+u(y-v)a1a2+v(u-z)a1a3,
    E2=x(z-u)a0a1+z(w-x)a0a3+u(x-w)a1a2+w(u-z)a2a3,
    E3=x(y-v)a0a1+y(w-x)a0a2+v(x-w)a1a3+w(v-y)a2a3.

Their exact identity is

    (w-x)E1+(y-v)E2-(z-u)E3=0.                       (1)

Thus there are only TWO independent constant-complement equations,
without imposing the Ceva condition. Since z!=u, E1=E2=0 is equivalent
to all three. They cut out an intersection of two quadrics in amplitude
P3; the signed-amplitude guards must still be retained.

## Complete guarded fixture description

For (x,y,z,u,v,w)=(1,2,3,4,5,6), normalize a0=1, write A=a1,B=a2.
Every guarded solution is exactly

    a3=A(20B+1)/(6B+15),
    (72A+12)B²+(-100A²+30)B-5A²-9A=0,              (2)

with nonzero pairwise distinct signed amplitudes. The denominator cannot
vanish in a guarded solution: B=-5/2 forces A=0 in E2. Conversely (2)
with the guards satisfies all three original H equations.

The discriminant of the quadratic in B is

    4(2500A^4+360A^3-792A²+108A+225),

and is squarefree. Hence this amplitude curve has normalization genus1.
It is not a finite list of trial amplitudes.

The reciprocal-incident-product point gives (A,B)=(3/10,1/8), a3=1/15.
The tangent there has slope5/8. Its intersection with the cubic factors
exactly as

    -(10A-3)²(22A+13)/64.

The third point therefore gives the viable exact amplitudes

    (a0,a1,a2,a3)=(1,-13/22,-19/44,4/11),
    H01=56/5.

All signed-amplitude guards hold. This independently agrees with the
amplitudes obtained by imposing the complementary linear-coefficient
conditions in the parallel Ceva calculation.

`constant_amplitude_gate.py/json` verifies the symbolic identity(1),
squarefreeness, tangent factorization, all three H equations and the
guards using exact rational arithmetic. The corrected run completed
0.54seconds under the60-second/384MiB watchdog. An initial syntax error
was fixed before the successful saved receipt.

## Remaining scope

These equations match only the constant coefficients of complementary
quadratics. They do not ensure equality of the values of the two matching
pairs at the remaining nodes. The separate all-plus/linear-coefficient
calculation fixes L0's constant to -7/2 for this fixture and leaves its
linear coefficient to be tested. The parallel exact cross-pattern test
reported no solution for that remaining parameter. Thus the displayed
amplitudes are a valid intermediate algebraic solution, not an eight-word
bank. Variable Ceva edge shapes remain a separate problem.
