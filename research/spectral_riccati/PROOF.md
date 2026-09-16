# Linear spectral count for a polynomially weighted Riccati family

September 16, 2026. Self-reviewed deduction; finite checks accompany it.
This strengthens `CONSTANT_WEIGHT.md` from a constant challenge
weight to every fixed-degree polynomial weight. It is not a result for
all nonlinear first-order equations.

## Theorem

Work in characteristic zero or characteristic p>D+1. Let R be any monic
polynomial of degree D+1 and let B be nonzero of degree b<=D-2. Consider
nonzero polynomial solutions P of degree at most D to

    R P' - R' P + P^2 - z B P = 0.                         (1)

If D>(b+1)(b+2), the number of distinct nonzero labels z admitting such
a solution is at most

    D-b-1.                                                (2)

No squarefreeness or splitting assumption on R is needed. For every D
there is also the elementary bound binom(2D,D). Thus for each fixed b
the number of nonzero labels is O_b(D), including the finitely many
degrees below the threshold in (2).

For an n-point RS domain with D<n, a received line f+zg, and threshold
A>D, this family has at most n+D-b bad full-MCA labels in the regime
of (2), even when the zero polynomial is allowed. The bound is uniform
over the domain and the received line.

## 1. Degree and root restrictions

As in the constant-weight case, degree comparison in (1) forces P to
have degree D and leading coefficient one. Here b<D is essential: when
deg P<D, the leading term of RP'-R'P has strictly larger degree than
P^2 and zBP. When deg P=D, the degree-2D coefficient forces monicity.

At a root a of P not shared by R, RP' has uniquely lowest local order.
Its leading coefficient is nonzero because each root multiplicity is
between 1 and D<p. Therefore all roots of P are roots of R.

Perform polynomial division

    R=(X+c)P+E,       deg E<=D-1.

Substitution in (1) yields

    E P' - E' P = z B P.                                  (3)

For z!=0, E is nonzero. If s=deg E, comparison at infinity in
E P'/P-E'=zB gives leading coefficient (D-s)lc(E) in degree s-1.
Since 1<=D-s<=D<p, it cannot vanish. Thus

    deg E=b+1.                                            (4)

Moreover gcd(R,P) divides E. If r is the number of distinct algebraic
roots of P, this proves

    r <= deg gcd(R,P) <= b+1.                              (5)

This elementary division argument also shows that no nonzero label is
possible for b=D-1, under the same degree assumptions. If b=0, it
recovers the single-root classification of the companion note.

## 2. Charge labels to high multiplicities of one fixed derivative

Under D>(b+1)(b+2), (5) implies that some root a of P has multiplicity
e>=b+3. Let m=ord_a R. Since gcd(R,P) has degree at most b+1 and
e>b+1, necessarily

    1<=m<=b+1<e.

Write R_m and B_(m-1) for the respective Taylor coefficients at a.
Local comparison in (1) forces ord_a B=m-1 and

    z = (e-m) R_m / B_(m-1).                              (6)

Both coefficients in this ratio are nonzero. For a fixed root a and a
fixed integer e, (6) therefore determines at most one label z, regardless
of the other roots or coefficients of P.

Differentiate R=(X+c)P+E exactly b+2 times. Equation (4) kills E, while
the remaining product has a zero at a of order at least e-b-2. Put

    M_a=ord_a R^(b+2).

Then e belongs to the integer interval

    b+3 <= e <= M_a+b+2,

which has at most M_a values. Choose one solution and one such root for
each distinct nonzero label. No two different labels can receive the same
pair (a,e), by (6). Summing the available pairs gives

    number of labels <= sum_a M_a <= deg R^(b+2)=D-b-1.

The derivative is nonzero and has the displayed degree because p>D+1.
The count can be made over the algebraic closure; it therefore also
bounds labels over the original field.

## 3. Small degrees and full MCA

For any D, all nonzero candidates are monic degree-D polynomials whose
roots belong to the at most D+1 distinct roots of R. There are at most
binom(2D,D) such multiplicity vectors. Each polynomial determines at
most one label in (1), since BP is nonzero. For a fixed b this is an
absolute constant throughout D<=(b+1)(b+2), proving O_b(D) overall.

For full MCA, every label with a nonzero candidate is among the at most
D-b-1 nonzero spectral labels plus possibly z=0. The zero candidate can
produce at most n additional bad labels: if f_i+zg_i=0 at a position
where (f_i,g_i)!=(0,0), that coordinate fixes at most one label. If no
such accidental position is present, the full agreement support has
f=g=0 and the common zero witnesses establish MCA. Thus there are at
most n+(D-b-1)+1=n+D-b bad labels.

The count is for challenge labels, not for the number of candidates at
a label. No interpolation theorem or list bound is required.

## What remains open

The displayed finite bound even allows b to grow subject to
D>(b+1)(b+2). Larger b defeats this argument. General first-order interpolants may have such
growing X-degree in their challenge coefficient. General Riccati
equations and two independently moving root families also remain
outside this theorem. Neither a better.codes improvement nor the target
fixed-gap quadratic proximity-gap lower bound follows.

## Finite verification

The checker examines 248,561 candidates in 1,780 fixtures: random split
R, planted examples with repeated roots, a nonsplit quadratic candidate,
and every split squarefree R over F_11 with degrees four through eight.
For each R it enumerates every monic degree-D polynomial supported on its
irreducible factors with at most b+1 algebraic roots. The written proof
justifies this reduction. It derives the weight polynomial from each
candidate, so it checks all weights of the allowed degree simultaneously.

All 7,191 nonzero solutions satisfy the polynomial identity, remainder
degree, and root-count restriction. The 151 solutions in the large-D
regime pass the high-multiplicity charge, with 158 local identities checked
over algebraic roots (via irreducible-factor remainders). Every label-count
bound passes. Small-degree fixtures provide negative controls showing
that the large-D hypothesis cannot simply be deleted. The largest observed
label group has four labels. Counts and explicit examples are saved in
the JSON; they are finite evidence supporting the general proof.

For example, over F_11 take D=3, B=X, and
R=X(X-1)(X-2)(X-4). The four pairs

    (z,P) = (3, X(X-1)^2), (6, X(X-4)^2),
            (7, (X-2)^3), (9, X(X-2)^2)

solve (1). They violate the bound D-b-1=1 that would result from
incorrectly omitting D>(b+1)(b+2).

The publication checker uses only the Python standard library. Its
low-degree factorization uses modular powers and polynomial gcds, with
separate irreducibility and completeness checks for degrees at most three.
All 1,780 candidate counts and label groups agree exactly with a prior
run using SymPy's independent factorization implementation.
