# Uniform small-excess rigidity

## Stronger characteristic-free exclusion for regular carriers

Let a>=1,e>=0, and let F have weight at most aw+e and uniform
first-jet contact at least a at n nodes. If

    e < w-a-1,          e < n-w-a+1,              (R)

then F_R=0 in EVERY characteristic. This conclusion is about the
formal derivative: in small characteristic it does not imply that F
is independent of R, because R^p has zero derivative.

To prove it, the first inequality bounds total jet degree by a.
Section 1 below and the second inequality exclude degree less than a.
The top-piece argument in Section 2 (which divides by no integer)
then gives F_a=A(X)Y^a: deg A_j<=e+j<n suffices to kill every j>=1.
Consequently F_R has total jet degree at most a-2. If a=1 this means
F_R=0 immediately. For a>=2, differentiate the formal local identity
with respect to Epsilon and R. The identities are

    partial_Epsilon F_sub=t^2*(F_Y)_sub,
    partial_R F_sub=t*(F_Y)_sub+(F_R)_sub.

Both left sides retain contact at least a. Therefore F_Y has contact
at least a-2 and F_R has contact at least a-1. Also

    wt(F_R)<=(a-1)w+e+1.

Apply the lower-jet-degree exclusion in Section 1 with contact a-1
and excess E=e+1. Its required inequality is exactly

    e+1<n-w-(a-1)+1,

which is equivalent to the second inequality in (R). It forces F_R=0.
All steps are formal polynomial identities, so no characteristic
restriction or factorial division is involved.

Thus a uniform-contact regular factor (F_R nonzero), of actual
weight aw+e, necessarily has

    e>=min(w-a-1,n-w-a+1).                        (RG)

At the proposed benchmark n=262144,w=131071, this is e>=131070-a.
The nonnegative additive resource and wt(F)<mA=21390450 imply
0<=a<=163 for uniform-contact factors. Thus each regular one has
charge at least130907 (for a=0 use wt(F)>=w-1 directly). Since the
total charge is strictly below5924072, there are at most45 such
factors counted with multiplicity. This counts only UNIFORM-CONTACT
regular factors, not arbitrary factors and not their individual
first-tail components. The count45 is WEAKER than the existing total
R-degree cap36, so it is not a numerical improvement or benchmark
progress; the new content is the structural per-factor excess gap.

## Stronger structural conclusion under additional hypotheses

Let k be any coefficient field (including k(Z)). Let n distinct nodes
carry symbols w_x. Assign weights (1,w,w-1) to (X,Y,R), with w>=2.
Suppose a>=1 and e>=0 are integers satisfying

    e < w-a-1,          a*e < n-w-a+1,            (1)

and the characteristic is zero or greater than a. If a nonzero F has
weighted degree at most aw+e and formal first-jet contact at least a at
every node, then there are A(X) nonzero and B(X) with

    deg A<=e,   deg B<=w+e,
    a*A(x)*w_x+B(x)=0 at every node,
    A^(a-1)*F=(A*Y+B/a)^a.                       (2)

In particular F is independent of R. If F is irreducible with positive
jet degree in k[X,Y,R], it is a primitive rational graph: a=1 and
F=A(X)Y+B(X). Its denominator A has no zero at the domain nodes.
Every carrier with F_R nonzero is therefore excluded by these bounds.

## 1. Lower-jet-degree exclusion

We first prove that a nonzero polynomial J of weight at most aw+E,
uniform contact a, and total jet degree b<a cannot exist if

    E < n-w-a+1.                                 (3)

Its highest homogeneous jet piece J_b inherits zero-word contact a:
this is the highest homogeneous (R,Epsilon) part after substituting
Y=w_x+tR+t^2 Epsilon. Let Lambda be the squarefree domain locator.
At X=x+t, write Lambda=t*l(t). The substitution

    Y=Lambda U,       R=Lambda' U+Lambda V

corresponds to regular local variables

    R=(l+t*l')U+t*l*V,
    Epsilon=-l' U-l V.

Its determinant is -l^2, a unit at the node. Thus every coefficient
of J_b(X,Lambda U,Lambda'U+Lambda V) is divisible by Lambda^a.

Write J_b=sum_j A_j(X)Y^(b-j)R^j. For the largest j with A_j nonzero,
the coefficient of U^(b-j)V^j is Lambda^b A_j. Therefore
Lambda^(a-b) divides A_j. But

    deg A_j <= aw+E-wb+j <= (a-b)w+E+b
              < (a-b)n,

where the last inequality follows from (3), b<=a-1, and n>w.
This is impossible. Descending j, or simply using the largest nonzero
one, proves the exclusion. No characteristic assumption enters this step.

## 2. Top two jet pieces

The first condition in (1) implies floor((aw+e)/(w-1))<=a, so total
jet degree is at most a. The second condition gives e<n-w-a+1;
Section 1 forces that degree to be exactly a.

Write its top piece sum_j A_j(X)Y^(a-j)R^j, with deg A_j<=e+j.
In the contact substitution the coefficient of R^a Epsilon^0 is
sum_j A_j(x+t)t^(a-j). Descending j>=1 forces A_j(x)=0 at all nodes.
As n>w+e+a-1>e+j, all such A_j vanish identically. Thus the top piece
is A(X)Y^a, with A nonzero and deg A<=e.

Write the next piece sum_j B_j(X)Y^(a-1-j)R^j, where
deg B_j<=w+e+j. The R^(a-1) Epsilon^0 coefficient is

    a*A(x+t)*w_x*t^(a-1)+sum_j B_j(x+t)t^(a-1-j).

Again descending j>=1 kills B_j, since n>w+e+a-1. Its final coefficient
gives a*A(x)w_x+B_0(x)=0, including nodes where A(x)=0. Set B=B_0.

## 3. Clearing the rational graph without deleting nodes

The polynomial L=A Y+B/a has contact at least one at EVERY node,
by the last relation, even at zeros of A. Hence

    J=A^(a-1)F-L^a

has contact at least a at all n nodes, weight at most aw+a e, and
total jet degree less than a. Apply Section 1 with E=a e. The second
condition in (1) forces J=0, proving (2).

Over k(X), equation (2) makes F a scalar times the a-th power of a
linear polynomial in Y and independent of R. If F is primitive and
irreducible with positive jet degree, Gauss's lemma therefore forces
a=1. For a=1, a domain zero of A also zeros B and gives an X-content
factor, contradicting primitive irreducibility. This proves the graph
and denominator claims.

## 4. Scope for actual solutions and benchmark budgets

If this irreducible graph has a polynomial solution P over the same
coefficient field k (or a constant extension), A P+B=0 forces A constant
by coprimality. When its actual contact is one, its actual excess is
then wt(F)-w=0 whenever deg P<=w.

This generic-polynomial implication does NOT apply to a single
specialized challenge. For example F=XY-Z, on nonzero nodes with
received word Z/x, has uniform contact one and excess one, but at Z=0
it admits the polynomial solution P=0. Thus one must use the safe
conclusion F_R=0 to exclude regular derivative-dependent carriers,
or explicitly require a generic polynomial solution for the preceding
corollary.

For an irreducible regular carrier with uniform actual contact a and
actual excess e=wt(F)-aw>=0, a sufficient exclusion is (1). Therefore,
in the stated characteristic range, such a carrier must have

    e >= min(w-a-1, ceil((n-w-a+1)/a)).            (4)

This is a factor charge bound for UNIFORM contact only. It does not
cover nonuniform positive-contact profiles or individually charge the
first-tail intersection components of a factor. The zero-charge result
for nonuniform contacts remains a separate theorem.
