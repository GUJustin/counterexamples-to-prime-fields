# Linear differential constraints: a linear full-MCA bound

September 16, 2026. Proof self-reviewed twice, with passing exact finite
checks. No independent mathematical review or novelty claim.

## A polynomial-matrix statement

Let D<n and D<A<=n, and evaluate degree-<=D polynomials at n distinct
points x_i of a field F. A received line has coordinate values f_i+z g_i.
Write M=D+1. Suppose the coefficient vector v of an allowed polynomial
satisfies an affine linear system

    T(z) v = b(z),

where every entry has degree <=H in z. The number of rows is arbitrary.
Let r be the rank of T over F(z), and put ell=M-r. Assume ell<=d for
some fixed d. A nearby candidate is bad when its full agreement support,
of size at least A, has no degree-<=D polynomial agreeing with g there.
Equivalently it has no full coefficientwise common witnesses for f,g.
Indeed, if G agrees with g on that support, take F=P-zG. Every common
agreement of F,G is then an agreement of P, so the common support equals
the candidate's full support.

If the system is generically inconsistent, all challenges with any
allowed candidate number at most H(r+1).

If it is generically consistent, put

    E=Hr+1,
    Q=max(n-D-1, floor(E(n-D)/(A-D))).

Then the number of bad challenge labels is at most

    Hr + floor((n)_ell * Q / (A-D)^ell),                 (1)

where (n)_ell=n(n-1)...(n-ell+1), and (n)_0=1.
In particular, for fixed H,d and A-D>=delta*n with delta>0 fixed,
this is O_{H,d,delta}(n). The statement holds in every characteristic.

The rank condition, bounded z-degree, and fixed positive gap are essential
hypotheses. This is not a general Reed--Solomon proximity-gap theorem.

## 1. Generic inconsistency or a bounded exceptional set

If the augmented matrix [T|b] has generic rank r+1, choose a nonzero
(r+1)-minor Gamma. Its degree is at most H(r+1). At every consistent
specialization the augmented rank is at most r, since all (r+1)-minors
of T vanish identically. Hence Gamma(z)=0 at every such challenge.

Otherwise choose r rows and r columns with nonzero minor Delta(z).
For r=0 set Delta=1. There are at most Hr roots of Delta. Outside those
roots the selected r rows span all rows, the affine system is consistent,
and its homogeneous kernel W_z has dimension ell. Generic consistency
ensures that augmented row dependence specializes correctly wherever
Delta is nonzero.

## 2. Many coordinate tuples determine each nearby candidate

Fix z outside Delta=0 and one bad candidate with agreement set S,
|S|>=A. The space W_z consists of degree-<=D polynomials. Choose ordered
coordinates in S greedily whose evaluations on W_z are independent.

After j<ell independent evaluations, their common kernel in W_z has
positive dimension. Take any nonzero polynomial in that kernel. It has
at most D roots, so at least |S|-D>=A-D coordinates of S evaluate it
nontrivially. Every such coordinate extends the independent evaluations.
Thus at least (A-D)^ell ordered ell-tuples from S determine the candidate
uniquely within the affine solution space. Previously selected coordinates
are zeros of the chosen kernel polynomial, so the new coordinates are
distinct. The case ell=0 has one empty tuple.

## 3. Each determining tuple supplies a rational codeword curve

Fix one ordered tuple J of ell distinct coordinates. Append its
coefficient-evaluation rows (1,x_i,...,x_i^D) to the selected r operator
rows. The resulting M by M matrix C_J(z) has determinant delta_J(z) of
degree at most Hr. If the determinant is identically zero, the tuple is
never determining and contributes nothing.

Otherwise solve the M equations, using b on the operator rows and
f_i+z g_i on the evaluation rows. By Cramer's rule the resulting polynomial
P_J(z,X) has coefficient denominators delta_J and numerators N_j of
degree at most Hr+1. Indeed each determinant term has r operator entries
of degree <=H; replacing one column by the right side adds at most one
factor of degree one from an evaluation row. The operator right side
itself has degree <=H. The bound also covers ell=0.

For each coordinate x let

    R_x(z)=sum_{j=0}^D N_j(z)x^j-delta_J(z)(f_x+z g_x).

Every R_x has degree at most E=Hr+1. Let h count the identically zero
residuals. At any determining challenge covered by this tuple,
delta_J(z)!=0, and the candidate is exactly P_J(z,X).

If h<=D, every nearby label is a root of at least A-h nonzero residuals.
Consequently their number is at most

    E(n-h)/(A-h) <= E(n-D)/(A-D).

The ratio increases with h because A<=n.

If h>=D+1, interpolate degree-<=D polynomials F,G from f,g on any D+1
identically agreeing coordinates. Over F(z), the polynomial
P_J(z,X)-F(X)-zG(X) has D+1 distinct roots, so it vanishes identically.
Every identically agreeing coordinate therefore agrees with F and G
separately. At every other coordinate the remaining received-line
residual is a nonzero affine polynomial in z. Any bad full support must
contain such an accidental zero; otherwise F,G explain its full support.
Thus at most n-h<=n-D-1 labels are bad.

This proves the bound Q for the determining labels of every tuple.
Roots of delta_J need not be added: that tuple is not determining there.

## 4. Count labels against determining tuples

Select one bad allowed candidate per bad label outside Delta=0. Each
supplies at least (A-D)^ell determining tuples. There are (n)_ell total
ordered tuples, each covering at most Q bad labels. Double counting gives
the second term of (1), and adding the <=Hr excluded labels proves it.

## Consequence for affine-linear differential equations

Suppose allowed polynomials solve

    sum_{j=0}^d a_j(X,z) P^{(j)}(X) = c(X,z),

with a_d nonzero, 0<=d<=D, and all coefficients of a_j,c having z-degree
at most H. Their X-degrees may be arbitrary. Equating X-coefficients is
a system of the preceding type, with the same z-degree bound H.

Assume characteristic zero or p>D. The homogeneous polynomial solution
space over F(z) has dimension at most d. For otherwise d+1 independent
polynomial solutions of degree <=D would have nonzero ordinary Wronskian:
a constant change of basis gives distinct leading degrees e_0,...,e_d,
and its leading coefficient is the product of their nonzero leading
coefficients times the Vandermonde product of the e_i. This is nonzero
because all e_i are distinct integers in [0,D] and p>D. But the differential
equation expresses the d-th derivative row in terms of the earlier rows
over F(z)(X), forcing that Wronskian to vanish. For d=0 a nonzero
multiplication operator has zero kernel directly.

Therefore ell<=d and (1) gives O_{H,d,delta}(n) bad challenges at every
fixed gap A-D>=delta*n. This covers arbitrary fixed derivative order for
constraints affine-linear in the jets, including a challenge-dependent
inhomogeneous term. Any quadratic example within the intended fixed-H,
fixed-order, large-characteristic regime must use a genuinely nonlinear
joint differential constraint, or fall outside these hypotheses.

This proof uses elementary polynomial root counts, linear algebra, and
the standard polynomial Wronskian criterion. It does not assume a
constant list-size bound or invoke the bounded-root restriction from
the preceding research notes.


## Verification and relation to prior work

`verify.py` passed 24 system fixtures and 88
received-line fixtures. These check generic polynomial minors, consistent
and inconsistent rank drops, homogeneous and inhomogeneous equations,
6,608 Cramer residual degree bounds, 87 determining-tuple counts, and
both branches of the proof (955 root-count cases and 29 affine-graph
cases). All allowed coefficient vectors and nearby labels in each small
field are enumerated. A characteristic-three negative control has two
independent degree-<=4 solutions of P'=0, confirming that the differential
kernel bound cannot simply omit its characteristic condition.
The finite tests supplement the general proof; they do not replace it.

The bounded dimension of polynomial solutions of a linear differential
equation is classical in this coding context. Guruswami and Wang prove
the corresponding statement by coefficient recurrence in *Optimal rate
list decoding via derivative codes*, Lemmas 4--5 (2011):
https://arxiv.org/abs/1106.3951
The elementary Wronskian argument above gives the version needed here.
This note's moving-parameter count is stated with its full-support
conclusion and explicit quantifiers; no literature priority is claimed.
