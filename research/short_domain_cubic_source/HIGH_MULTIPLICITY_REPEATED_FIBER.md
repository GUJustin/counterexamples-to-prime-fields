# A repeated (b-1,1) fiber: uniform section bound in every fixed degree

Status: independent audit of root's proposed extension PASS. This classifies one
explicit positive-critical stratum, not all repeated fibers or all first integrals.
The proof includes b=2,3,4 and permits an inseparable rational function q(X).

## Statement

Work over an algebraically closed field k of characteristic zero or p>b, b>=2.
Suppose a monic degree-b polynomial in u has a constant fiber

    F(X,u)-c0 H(X)=(u-R(X))^(b-1)(u-S(X)),

where H is nonzero and R,S are polynomials of degree at most D. Consider all
polynomial sections P of degree at most D satisfying F(X,P)=cH for a constant c.
Then either the whole section bank lies in one affine polynomial pencil, or
it contains at most 2b+2 sections. Consequently, on any n distinct coordinates,
for any received word, the number of sections agreeing at at least D+eta*n
coordinates is at most

    max(2b+2, floor(1/eta)),    eta>0.

No characteristic restriction involving D is required for this conditional
repeated-fiber statement. Over a smaller original field, extend constants and
bound the enlarged section bank.

## 1. A three-cover lemma

Let f(Y)=Y^(b-1)(Y+1). If q(X) is a nonconstant rational function, then there
are at most TWO distinct nonzero constants lambda for which

    f(Y_lambda(X))=lambda*q(X)

has a rational-function solution. This assertion holds in characteristic zero
or p>b, whether or not q is separable as a map of curves.

### Branch points and individual monodromy

Write

    kappa=(-1)^(b-1)(b-1)^(b-1)/b^b !=0.

The degree-b map t=f(Y)/lambda has the following branch data:

* Above infinity: one point of ramification index b.
* Above zero: Y=0 has ramification index b-1 and Y=-1 is unramified.
  For b=2 this means zero is NOT a branch point.
* Above kappa/lambda: Y=-(b-1)/b has ramification index two;
  the remaining b-2 points are unramified.

Indeed f'(Y)=Y^(b-2)(bY+b-1), and the characteristic assumption makes all
these ramification indices tame. There are no other branch points.

The geometric monodromy group is S_b. It is transitive because the cover is
connected. For b>=3 it contains a (b-1)-cycle fixing one letter; the stabilizer
of that letter is transitive on the other letters. Transitivity of the whole
group therefore makes it 2-transitive. The simple branch point supplies a
transposition, and conjugating it in a 2-transitive group gives all
transpositions, which generate S_b. For b=2, transitivity already gives S_2.
This proof has no exceptional normal-subgroup cases at b=3 or b=4.

### Independence of three covers

Suppose lambda_1,lambda_2,lambda_3 are distinct and nonzero. Let G be the Galois
group of the compositum of the three Galois closures over k(t). It embeds as a
subdirect subgroup of S_b^3. At t=kappa/lambda_i, the other two Galois closures
are unramified. Inertia therefore supplies an element whose ith coordinate is
a transposition and whose other coordinates are identities. Since the projection
G to the ith S_b is surjective, its conjugates generate the whole ith factor
inside G. Repeating for i=1,2,3 proves

    G=S_b^3.

This directly proves the needed independence; no assertion that arbitrary
covers with partially disjoint branch sets are linearly disjoint is used.
The fiber product of the three degree-b covers is consequently irreducible:
S_b^3 acts transitively on the product of their b-element fibers. Its normalized
function field has degree N=b^3 over k(t).

### Genus of the normalized fiber product

At infinity, every inertia orbit on the b^3 sheets has size b. Its index is

    I_infinity=N(1-1/b).

At zero, each factor fixes one letter and cycles the other b-1 letters. There
is one all-fixed tuple; every other tuple has orbit length b-1. Thus

    I_zero=(N-1)(b-2)/(b-1).

This formula also gives zero for b=2, as required. At each of the three distinct
simple branch values, a transposition in one factor pairs b^2 pairs of sheets,
so the index is N/b=b^2. All ramification is tame. Riemann-Hurwitz gives

    2g-2=-2N+I_infinity+I_zero+3N/b
         =(b-2)(b+1),
    g=b(b-1)/2 >0.

For b=2,3,4 the genera are 1,3,6 respectively.

If three rational solutions Y_i(X) existed, substituting t=q(X) would embed
this connected fiber-product function field into k(X), since q is nonconstant.
Luroth's theorem says every intermediate one-variable field in k(X) is rational,
contradicting positive genus. This reasoning does not assume q'(X)!=0:
inseparable rational parametrizations cannot evade Luroth's theorem either.
This proves the three-cover lemma.

## 2. Reducing the section bank

First suppose h=R-S is nonzero. Put

    Y=(P-R)/h,    lambda=c-c0,    q=H/h^b.

Then the section identity is precisely

    Y^(b-1)(Y+1)=lambda*q.

If q is nonconstant, the three-cover lemma allows at most two nonzero labels.
Each label supplies at most b polynomial sections, being roots of a monic
polynomial of degree b over k(X). The lambda=0 fiber contributes only P=R
or P=S. Thus the complete section bank has at most 2b+2 members.

If q is constant, f(Y) is constant, so Y itself is constant: a nonconstant
rational Y would make f(Y) nonconstant. All sections lie in the affine pencil
R+t h, t in k. Both coefficient polynomials have degree at most D.

If R=S, the equation is (P-R)^b=(c-c0)H. If there is no section with c!=c0,
there is only P=R. Otherwise choose one such section P0 and put h=P0-R.
Its identity expresses H as a constant multiple of h^b. Every other section
then has ((P-R)/h)^b constant, so (P-R)/h is constant. This again gives an
affine pencil with coefficient degrees at most D. This argument does not
require extracting a polynomial bth root of H in advance.

## 3. Agreement count for the affine alternative

For distinct members R+t h of a nonconstant pencil, h!=0 has at most D zeros
among the evaluation coordinates. At every other coordinate the values are
distinct as t varies, so any received symbol agrees with at most one member.
If L members each have at least A agreements, incidence counting gives

    L*A <= L*D+n,
    L <= n/(A-D) <=1/eta.

A constant pencil contains only one polynomial. Combining this with the finite
bank alternative proves the statement.

## Scope

For b=3 this recovers the repeated-double-linear cubic stratum already used in
the full cubic theorem. For general b it handles exactly a fiber with one root
of multiplicity b-1 and one further linear root (including their coincidence).
It says nothing about, for example, a quartic fiber with one double linear
factor and two unrelated simple roots, or higher-degree repeated factors whose
normalizations have different branch patterns. Existence of a repeated fiber
alone does not imply the displayed factorization. No full higher-degree
positive-critical classification or new benchmark improvement is claimed.


# Extension: every fiber supported on two distinct linear roots

The following strengthens the preceding (b-1,1) statement. The preceding proof
is retained as an independently audited special case.

## General statement

Suppose, in characteristic zero or p>b=r+s, with r,s>=1,

    F(X,u)-c0H(X)=(u-R(X))^r(u-S(X))^s,
    deg R,deg S<=D,   H!=0.

Put d=gcd(r,s) and b0=b/d. Then the whole degree<=D polynomial section bank
F(X,P)=cH is either contained in one affine polynomial pencil, or has size at
most 2b0+2. In particular every received word on n distinct coordinates has
at most

    max(2b0+2, floor(1/eta))

sections agreeing on at least D+eta*n coordinates. This statement covers ALL
constant fibers supported on at most two distinct roots, with arbitrary positive
multiplicities. It remains conditional on this explicit factorization; it is
not a classification of all repeated fibers.

## A. The coprime two-cycle cover

Assume first gcd(r,s)=1 and let

    h(Y)=Y^r(Y+1)^s,  b=r+s,
    kappa=(-1)^r r^r s^s/b^b !=0.

The degree-b map h(Y)/lambda has inertia cycles (r)(s) at zero, a b-cycle at
infinity, and a transposition at kappa/lambda. This follows from

    h'(Y)=Y^(r-1)(Y+1)^(s-1)(bY+r).

The remaining critical point -r/b is simple and distinct from zero and -1.
Ramification is tame under p>b. Zero may be unramified when r=s=1.

### Polynomial indecomposability

Suppose h=A(B(Y)) with both polynomial degrees greater than one. If A has at
least two distinct roots alpha,beta, the disjoint nonempty root sets of
B-alpha and B-beta are contained in the two-element set {0,-1}. Each must
therefore be supported on exactly one point. Up to interchanging the two,

    B-alpha=cY^m,    B-beta=c(Y+1)^m,    m=deg B>1.

Their leading coefficients are the same. But their difference cannot be a
constant: its coefficient of Y^(m-1) is a nonzero multiple of m, since m<=b<p
in positive characteristic. This is a contradiction. If A has only one root,
write A=c(U-alpha)^e. Then every root multiplicity of h is divisible by e,
so e divides both r and s, contradicting their coprimality.

This also rules out a nontrivial rational decomposition: the polynomial map
has a unique, totally ramified point above infinity. In an intermediate cover
there is likewise only one point above infinity; the intermediate function
field is rational by Luroth, and choosing that point as its infinity makes
both maps polynomial. Thus h is indecomposable as a cover.

### Monodromy is S_b

The geometric monodromy is transitive and primitive. For completeness, an
imprimitivity block corresponds by Galois correspondence to an intermediate
field between k(h(Y)) and k(Y); Luroth and the preceding paragraph would give
a nontrivial polynomial decomposition. The simple branch point supplies a
transposition. Form the graph on the b letters whose edges are all its
conjugates. The connected components form a block system for the monodromy
group. Primitivity and the existence of an edge force this graph to be
connected. Transpositions along a connected graph generate S_b. Hence the
monodromy group is S_b, without invoking a classification of primitive groups.
The proof includes b=2 and all exceptional normal-subgroup cases in small degrees.

## B. Three scaled covers and their genus

For three distinct nonzero lambda_i, their unique simple branch values
kappa/lambda_i are distinct. The same inertia/conjugation argument in the
preceding proof gives G=S_b^3 for the compositum of the Galois closures.
In particular the normalized threefold fiber product is connected of degree
N=b^3. Its inertia orbit counts are:

* Infinity: b^2 orbits.
* Each of the three unique simple branch points: index b^2.
* Zero: r^2+s^2+3(r+s) orbits.

To check the last count, triples with all entries in the r-cycle give r^2
orbits; those all in the s-cycle give s^2. Triples with two r entries and one
s entry give 3r orbits, and those with one r and two s entries give 3s, because
the mixed orbit length is lcm(r,s)=rs. This is precisely where coprimality is
used in the genus calculation. The generator may act by different primitive
powers of each cycle in different factors; the orbit lengths are unchanged.

Riemann-Hurwitz therefore yields

    2g-2=-2N+[N-b^2]+[N-r^2-s^2-3b]+3b^2
         =2b^2-r^2-s^2-3b
         =b^2+2rs-3b.

Since rs>=b-1, the last expression is at least (b-2)(b+1)>=0. Thus g>=1.
For r=1 this specializes to g=b(b-1)/2, agreeing with the previous proof.
Luroth again excludes three rational solutions h(Y_i)=lambda_i q(X) for any
nonconstant rational q, including inseparable q. Thus at most two distinct
nonzero labels have rational solutions when r,s are coprime.

## C. Removing the coprimality assumption

For arbitrary r,s, write d=gcd(r,s), r=d*r0, s=d*s0, and
h0(Y)=Y^r0(Y+1)^s0, so h=h0^d and gcd(r0,s0)=1.
Suppose q is nonconstant. If there are no nonzero-label solutions, only the
zero fiber remains. Otherwise fix one solution Y_* with label lambda_*, and put

    q0=h0(Y_*),    q=q0^d/lambda_*.

The function q0 is nonconstant. For any solution h(Y)=lambda*q with nonzero
lambda, one has

    (h0(Y)/q0)^d=lambda/lambda_*.

A rational function whose dth power is constant is constant. Over algebraically
closed k it therefore equals some mu in k, and EVERY solution in the original
bank satisfies

    h0(Y)=mu*q0.

The coprime-cover lemma allows at most two nonzero mu. Each equation has at
most b0=r0+s0 rational-function roots. Consequently the entire nonzero-label
bank has at most 2b0 solutions, regardless of collisions among the values
lambda=lambda_*mu^d. The zero fiber contributes only Y=0,-1. This proves
2b0+2, rather than the weaker 2b+2.

## D. Applying the cover lemma to polynomial sections

When R!=S put a=R-S, Y=(P-R)/a, and q=H/a^b. The section equation becomes

    Y^r(Y+1)^s=(c-c0)q.

For nonconstant q the preceding bound applies, and P-to-Y is injective.
If q is constant then every Y is constant, giving the affine pencil R+t a.
If R=S, the previous pure-power argument again yields an affine pencil after
choosing one noncritical section, or a singleton if none exists. The same
agreement incidence calculation then gives the stated list bound.

This extension includes squared-quadratic fibers when their quadratic splits
into two polynomial linear factors, but does not replace the separate squared-
quadratic reduction when that quadratic is irreducible over k(X). It does not
handle fibers supported on three or more distinct roots.
