# Mixed Hermite singular covers for quadratic derivative equations

September 17, 2026. Working theorem for independent audit. This is an
actual-solution theorem; covering all nearby candidates requires one
identity containing them. No irreducibility or squarefreeness assumption
is required for the stated conclusion.

## 1. A weighted singular-cover theorem

Let Q(X,z,u,v) be nonzero, of total jet degree B>=1 and challenge degree
H>=0. Let D>=1, char(F)=0 or p>D, and fix n distinct coordinates, a
received line f+zg, and integer D<A<=n. A pair (z,P), deg P<=D, is bad
if it has at least A agreements and no degree-D direction polynomial
agrees with g on its full support.

Suppose disjoint fixed coordinate sets S0,S1 have sizes u,s. At S1,
every singular agreement of any candidate under consideration satisfies

    P'(x)=h_x+z k_x,                              (1)

where h_x,k_x are fixed field elements. At S0 there is no derivative
condition. Outside at most E labels, assume each bad candidate has at
most e singular agreements outside S0 union S1. Define

    N=u+s,
    kappa=min(N, floor((D+2u+2s)/3),
                 floor((D+5u+4s)/6)),
    L=A-e-kappa>=1.

Let C be the fixed-coordinate nonsingular bound from
quasilinear_first_order/REGULAR_AGREEMENTS.md:

    tau=max(0,2D-3), b0=1+tau(B-1), T0=b0+tau H,
    K0=H+B T0, q0=B+H,
    C=q0 K0+q0 T0*(n-D)/(A-D)+q0 n.

Then the number of bad labels is at most

    E+(n/L)C+n.                                  (2)

If kappa=N the final n may be omitted. For u=0,

    kappa=min(s,floor((2s+floor(D/2))/3)),

so the pure Hermite cover replaces D by floor(D/2) in the ordinary
singular-cover threshold. For s=0 this recovers the ordinary cover.

Proof. The nonsingular theorem removes at most nC/L labels possessing
a bad witness with at least L nonsingular agreements. Outside those
and the E exceptional labels, select one bad witness per label. Each
has at least A-(L-1)-e=kappa+1 SINGULAR agreements in S0 union S1.
If kappa=N this is impossible. Otherwise put b=kappa+1<=N.

For three selected supports, at most 3(N-b) distinct core coordinates
are missing from their intersection. Give weight1 to S0 and weight2
to S1. To minimize the remaining weight, remove weight2 coordinates
first. The minimum intersection weight is

    W(b)=max(0,N-3(N-b))+max(0,s-3(N-b)).          (3)

If 3(N-b)>=s this is max(0,3b-2N); otherwise it is
6b-5u-4s. Solving W(b)>D gives precisely b>kappa. The same lower bound
also applies to two supports, which omit no more coordinates.

At three distinct labels, form the polynomial affine dependence of the
three candidates using the labels. It vanishes at all common coordinates,
and its derivative vanishes at the common S1 coordinates by (1).
Its total zero multiplicity therefore exceeds D, forcing it to vanish
identically. The analogous two-candidate argument gives uniqueness at
each label. Thus if three or more labels remain their witnesses all
lie on one affine codeword pencil. Its bad labels number at most n,
because each bad witness needs a nonpersistent coordinate agreement,
and each such coordinate contributes at most one label. With at most
two labels the same n bound holds. This proves (2).

The use of SINGULAR agreement supports is essential: condition (1) is
not asserted at nonsingular matches inside S1. Those were counted in
the removed L-1 budget before selecting the supports.

## 2. Exact core decomposition for a quadratic derivative equation

Now assume characteristic zero or p>max(D,2), and consider

    Q(X,u,v)=a(X)v^2+(b(X)u+d(X))v
                         +c(X)u^2+e(X)u+f0(X),               (4)

with arbitrary X-degrees and Q nonzero. All coefficients are challenge
independent. One may require a!=0 to describe genuine quadratic
v-dependence, but the theorem also allows a=0. Squarefreeness of Q is
not needed: even a repeated-square identity obeys the same constraints.
If the aim is to exhibit a new singular mechanism, repeated squares
should of course be reduced before interpreting them as evidence.

For each domain coordinate x put w_x(z)=f(x)+zg(x), and define

    ell_x(z)=b(x)w_x(z)+d(x),
    m_x(z)=c(x)w_x(z)^2+e(x)w_x(z)+f0(x).

The fixed core S1 consists of coordinates where a(x)!=0 and

    Delta_x(z)=ell_x(z)^2-4a(x)m_x(z)

vanishes identically. Every singular agreement there satisfies

    P'(x)=-ell_x(z)/(2a(x)),

which is affine in z as required. The ordinary core S0 consists of
coordinates where

    a(x)=0, ell_x(z) identically0, m_x(z) identically0.

At S0 the specialized equation Q(x,w_x(z),v) vanishes identically in
both z,v, so it imposes no derivative data.

Outside S0 union S1, a coordinate supports singular agreements at at
most TWO distinct labels, uniformly over all candidates:

* if a(x)!=0, singular agreement forces Delta_x(z)=0, and this is a
  nonzero polynomial of degree at most2;
* if a(x)=0 and ell_x is not identically zero, singular agreement
  forces ell_x(z)=0, with at most one label;
* if a(x)=0 and ell_x is identically zero, then m_x is nonzero, and
  actual agreement with Q=0 forces m_x(z)=0, with at most two labels.

This explicitly handles all leading-coefficient degeneracies. Hence
the total singular coordinate-label incidences outside the cores are
at most 2n, independently of the X-degree of the equation.

## 3. Linear bound and quantitative gain

Compute kappa from the actual sizes u=|S0|,s=|S1| above. Assume

    A-D>=eta*n, A-kappa>=lambda*n,

with fixed positive eta,lambda. Choose e=floor(lambda*n/2). At most
2n/(e+1)<=4/lambda labels have more than e singular coordinates outside
the cores. All other labels obey the weighted cover, with
L>=lambda*n/2. In (2) use B=2,H=0, so

    T0=1+max(0,2D-3),
    C=4T0+2T0*(n-D)/(A-D)+2n.

This proves O_{eta,lambda}(n) bad labels for actual polynomial solutions
of (4). No candidate-independent separant was assumed: Q_v=2aP'+bP+d
can vary with the candidate. The exact leading-coefficient and
persistent-discriminant conditions above are the substitute.

If u=0, the condition is approximately

    s < (3A-D/2)/2 - positive linear slack.

At quarter-rate first-order agreement A/D about1.87517, this permits
s/D below about2.56275, versus about2.31275 for value-only singular
information. This is an actual improvement in the allowable persistent
singular core. It is not a general first-order proximity theorem: a
large ordinary core or a still larger Hermite core remains outside it.

More generally the two sharp triple-intersection thresholds are
(D+2u+2s)/3 and (D+5u+4s)/6, and one uses their minimum. The second
improves the first exactly when u<D. When the ordinary core is already
larger than D, all the derivative information can be absent from the
worst triple intersection, so this argument gives no extra benefit.
