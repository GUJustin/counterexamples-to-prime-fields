# Any fixed monic value degree: the zero-dimensional critical case

Status: complete mathematical derivation for independent audit. This extends the
repeated-H cubic argument. It does NOT classify positive-dimensional critical
components, and it does not apply to arbitrary differential equations.

## Statement

Let k be algebraically closed, of characteristic zero or characteristic p>b,
where b>=2. Let D>=1 and

    F(X,u)=u^b + sum_{j=0}^{b-1} a_j(X) u^j,
    deg a_j <= (b-j)D,

and let H be a nonzero polynomial. Assume the ORIGINAL ideal

    I=(F_u, H F_X-H'F) in k[X,u]

is zero-dimensional (the unit ideal is allowed). Consider ALL polynomial sections
P of degree at most D satisfying F(X,P)=cH for some constant c in k.
On any n distinct evaluation coordinates, for any received word, the number L of
these sections agreeing on at least a coordinates, where a>=D+eta*n and eta>0,
satisfies

    L <= floor[b^2 + (b+3b^2(b-1)^2 D/n)/eta].               (1)

The field may originally be smaller: passing to its algebraic closure only enlarges
the solution set. No characteristic bound involving D is used in this
zero-dimensional case. All polynomial integrations below have degree at most b,
so p>b suffices.

## 1. Critical length

Write N=deg H and r_H for the number of its distinct roots. If there is no
nonzero-label section, there are at most b sections and (1) holds. Otherwise
N<=bD. Put B=H F_X-H'F. The bidegrees in (X,u) obey

    deg F_u <= ((b-1)D,b-1),
    deg B   <= (N+bD-1,b).

Since the affine intersection is zero-dimensional, its scheme length ell is at
most the mixed bidegree intersection bound

    ell <= (b-1)(N+2bD-1).                                (2)

For a direct justification, bihomogenize each nonzero generator to its OWN
actual bidegree in P^1_X times P^1_u. Neither bihomogenization contains either
boundary divisor: actual X-degree prevents a factor defining X=infinity, and
actual u-degree prevents a factor defining u=infinity. Any common projective
curve would therefore meet the affine chart and contradict zero-dimensionality
of the original ideal. The projective intersection is proper, so its total
length is the mixed product of the two actual bidegrees. The affine length is
at most this total, and bounding the actual bidegrees by the displayed caps
gives (2). If a generator is a nonzero constant, the affine length is zero
and the conclusion is immediate.

For any section P, let A=F_u(X,P). This polynomial is nonzero, since otherwise
its whole graph would lie in I: differentiating the section identity gives

    B(X,P)=-H A P'.

At a point (x,P(x)), quotienting the local critical algebra by the graph equation
u-P(X) gives k[X] localized at x modulo A. Thus ord_x A is at most the local
critical-scheme length at that point.

## 2. One valuation lemma handles both ends

Fix a valuation extending the order at a finite point, or the negative of degree
at infinity, to an algebraic closure of k(X). Factor

    F_u(X,P+Z)=b product_{i=1}^{b-1}(Z-delta_i),
    A=b product_i(-delta_i).

A!=0, so every delta_i is nonzero. Choose delta among the delta_i with MAXIMAL
valuation. Write d=v(A). Then v(delta)>=d/(b-1).
In the expansion F_u(X,P+Z)=sum_j c_j Z^j, each summand of
c_j delta^j is A times a product of j ratios delta/delta_i. Its valuation is
at least d. Integration, whose denominators j+1 are units, yields

    v(F(X,P+delta)-F(X,P)) >= d+v(delta) >= b*d/(b-1).       (3)

This proof allows repeated critical roots and ramified valuations. It does not
assume Puiseux expansions, separability of F_u, or absence of cancellation.

At infinity equivalently choose delta of MINIMAL degree. Formula (3) says that
the degree of the correction is at most b*deg(A)/(b-1).
If deg A < (b-1)N/b, then the fixed critical value
F(X,P+delta)/H has residue c at infinity. The critical roots P+delta are roots
of the fixed polynomial F_u, of degree b-1. At most b-1 distinct constant labels
can therefore violate

    deg A >= ceil((b-1)N/b).                              (4)

At a finite root x of H with multiplicity m, if
ord_x A > floor((b-1)m/b), (3) implies that the same fixed critical value is
regular with residue c at x. At most b-1 distinct labels can have this excess
at any fixed x. The chosen valuation extension and all b-1 critical roots are
fixed once at each x, so these statements do not require branches selected
consistently across different x.

## 3. Global excess budget

For each nonzero label not exceptional at infinity, select one section P and set

    cost(P)= sum_{x not in roots(H)} ord_x A
             +sum_{x in roots(H)} max(0,ord_x A-floor((b-1)m_x/b)).

Away from H, a point (x,u) determines c=F(x,u)/H(x), so different chosen labels
have disjoint critical points. At a root of H, at most b-1 labels have positive
excess. Each contribution is bounded by the relevant local critical length.
Consequently

    sum_P cost(P) <= (b-1)ell.                            (5)

By (4), every selected section costs at least

    R=ceil((b-1)N/b)-sum_x floor((b-1)m_x/b)
      >= r_H-floor(N/b) >= r_H-D.                         (6)

The first inequality uses floor((b-1)m/b)<=m-1 for m>=1, and
ceil((b-1)N/b)=N-floor(N/b).
If r_H>D, the total number of sections is therefore at most

    b^2 + b floor((b-1)ell/R)
      <= b^2 + 3b^2(b-1)^2 D/(r_H-D).                    (7)

Here b^2 accounts for the at most b-1 exceptional labels and the zero label,
with at most b polynomial roots of each fiber. Equation (2) and N<=bD justify
the last inequality. In particular b=3 gives exactly the earlier coarse
9+108D/(r_H-D) bound.

## 4. Arbitrary received words

Choose any finite L sections satisfying the agreement threshold. At a coordinate
where H is nonzero, the received value fixes a unique label. At most b sections
belong to that label. At a coordinate where H vanishes, use the trivial bound L.
Counting incidences gives

    L*a <= L*r_H + b*n,
    r_H >= a-b*n/L.                                      (8)

If L<=max(b^2,b/eta), (1) follows immediately. Otherwise (8) implies r_H>D,
and (7) implies, with rho=D/n and C_b=3b^2(b-1)^2,

    (L-b^2)(eta-b/L) <= C_b*rho.

Expanding and dropping the positive term b^3/L gives

    L <= b^2+(b+C_b*rho)/eta,

which proves (1). This reasoning applies to every finite subset and hence also
rules out an infinite high-agreement family under the stated hypotheses.

## Scope

The zero-dimensionality assumption is essential to the present proof: it both
makes ell finite and excludes sections with A identically zero. Positive-dimensional
critical components are not removed, divided out, or silently charged elsewhere.
For b=3 they have a separate classification under additional characteristic
conditions. No such classification is claimed here for general b.


## Structural corollary: exceeding the bound forces a repeated constant fiber

Assume characteristic zero, or p>b(b-1)D. If the high-agreement family exceeds
(1), there exists a constant c in k such that F(X,u)-cH(X) has a repeated
nonconstant factor in k(X)[u]. This is a necessary structural condition, not
a classification of the resulting exceptional pencils.

Indeed the theorem forces a positive-dimensional component of I. It cannot be
vertical: F_u is a polynomial in u with nonzero constant leading coefficient b.
Thus its generic point gives an algebraic critical root r over K=k(X), of degree
d<=b-1. The extension L=K(r) is separable, since d<p in positive characteristic.
The derivation d/dX therefore extends to L. Setting v=F(X,r)/H gives

    v'=(H F_X(X,r)-H'F(X,r))/H^2=0.

A family exceeding (1) includes a nonzero-label section, so N<=bD. The root r
of the monic polynomial F_u/b is integral at every finite place of K. At each
place above infinity, its pole order is at most D times the ramification index:
this follows directly from the weighted bounds on the coefficients of F_u/b.
Therefore F(X,r) has poles only above infinity, of order at most bD times the
ramification index. Division by H allows poles of total degree at most dN at
finite places and at most d*max(bD-N,0) above infinity. Thus the pole-divisor
height satisfies

    h_L(v) <= d*max(N,bD) = dbD <= b(b-1)D.

In characteristic zero, v'=0 makes v constant. In positive characteristic,
the kernel of the nonzero derivation on the one-variable function field L over
the algebraically closed field k is L^p. A nonconstant pth power has pole-divisor
height at least p, contrary to the strict characteristic hypothesis. Thus v=c
is constant in either case. The minimal polynomial of r over K consequently
divides both F_u and F-cH, proving the repeated-factor assertion.

Over a non-algebraically-closed original constant field, the conclusion is stated
after extending constants to its algebraic closure. No rationality of c over the
original field is asserted. The argument does not say the repeated fiber is the
zero fiber, that the repeated factor is linear, or that all such pencils are
isotrivial.
