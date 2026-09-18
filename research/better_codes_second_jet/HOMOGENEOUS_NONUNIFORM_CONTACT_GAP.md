# A sharp nonuniform derivative-degree contact gap

**Proved, characteristic-free.** Fix n distinct nodes, w>=2, and weights
(X,Y,R)=(1,w,w-1). Work over any coefficient field, including k(Z).
For an actual contact profile a_x(F), write

    charge(F)=wt(F)-(w/n)sum_x a_x(F).

The following statements require n>=2w.

1. For a polynomial homogeneous in (Y,R), at ANY received word,

       charge(F)>=deg_R(F)*(w-1).

2. For an ARBITRARY polynomial F at the zero received word, the same inequality
   holds. More generally it holds at a received word given by a polynomial P
   of degree at most w, using its jet translation.

3. At an arbitrary word and for arbitrary F, the degree in R of its highest
   total-jet homogeneous piece can replace deg_R(F) in the inequality.

These statements use degree in R, not nonvanishing of the formal derivative
F_R. In small characteristic they still apply to R^p terms. They do not assert
the full deg_R(F) bound for arbitrary received words and nonhomogeneous F.

## 1. A local weighted-Taylor inequality

Let G(X,Y,R) be homogeneous of degree r in (Y,R), and suppose
B(X)=G(X,0,1) is nonzero. At a fixed node x, set

    g(t,Y)=G(x+t,Y,1)=sum_j c_j(t)*(Y-t)^j.

Every c_j is a polynomial in t. Substituting Y=tR+t^2E in G gives

    sum_j c_j(t)*t^(2j)*E^j*R^(r-j).

The distinct monomials imply that its actual zero-word contact is

    a=min_j(ord_t c_j+2j).

On the other hand B(x+t)=sum_j c_j(t)*(-t)^j. Each summand has order

    ord_t c_j+j >= (ord_t c_j+2j)/2 >= a/2,

since ord_t c_j>=0. Therefore

    a<=2*ord_(X-x) B.                             (1)

Cancellation in the sum for B can only increase its order. This proof uses
no root extraction, factorials, separability, or characteristic restriction.

## 2. Homogeneous global bound

Let F be homogeneous of total jet degree b and put r=deg_R F. Factor

    F=Y^(b-r)*G,

where G is homogeneous of degree r and B(X)=G(X,0,1) is nonzero. Write
d=deg B. At the zero word the Y factor has contact one at every node, so
(1) gives

    sum_x a_x(F)<=n*(b-r)+2d.

The coefficient B of Y^(b-r)R^r also gives wt(F)>=bw-r+d. Consequently

    charge(F)>=r*(w-1)+(1-2w/n)*d.                (2)

For n>=2w this proves the claimed derivative-degree gap.

At an arbitrary received word, the highest homogeneous (R,E) part of the
local substitution F(x+t,r_x+tR+t^2E,R) is exactly the zero-word substitution
of F. Thus the actual contact is no larger than its zero-word contact.
This proves (2), and hence statement1, without a zero-word assumption.

The bound is sharp: F=Y^(b-r)R^r has charge r(w-1) at the zero word. More
generally, for a squarefree B0 supported on h domain nodes,

    F=Y^(b-r)*(B0 R-B0'Y)^r

attains (2) with d=rh. It has contacts b+r at those h nodes and b-r elsewhere.
This verifies sharpness on genuinely nonuniform profiles as well.

## 3. General polynomials and the role of the received word

At the zero word, the local substitution preserves total homogeneous degree
in the formal variables (R,E). Therefore each nonzero homogeneous jet piece
F_b has contact at least a_x(F) at every node; different pieces cannot cancel
one another. Select a piece containing a monomial of maximal R-degree r.
Applying (2) to that piece and using wt(F)>=wt(F_b) proves statement2.

If the word is P(x) with deg P<=w, use the invertible jet translation

    Y_old=Y_new+P(X),   R_old=R_new+P'(X).

Both it and its inverse preserve weighted-degree bounds, so the actual weight
is unchanged; degree in R is unchanged as well. Locally the extra term
P(x)+tP'(x+t)-P(x+t) is divisible by t^2, and can be absorbed by a translation
of the formal E variable. Thus actual contacts are unchanged and the word
becomes zero. This proves the polynomial-word extension, also in arbitrary
characteristic.

For a completely arbitrary received word, only the highest homogeneous jet
piece automatically inherits zero-word contact. Its weight is at most that
of F, so (2) proves statement3. Lower homogeneous pieces may mix after the
received-symbol translation; they cannot be treated independently without
an additional argument. This is the exact remaining obstruction to extending
the full R-degree bound to all inputs.

## Benchmark scope

The explicit binding model has received word Z, a polynomial word. Its charge
5898195 is greater than12*(w-1)=1572840, so it satisfies the new inequality.
The result does not remove that carrier or its simple first-tail component.
Even aggregating the new degree charge under the primary resource gives a
weaker derivative-degree bound than the existing primary R-degree cap36.
No benchmark improvement or individual tail-component cost bound follows.

## 4. Local bridge for arbitrary nonhomogeneous carriers

There is a characteristic-free local extension without a homogeneous or
polynomial-word assumption. Write

    F(x+t,r_x+Y,R)=sum_(j=0)^r A_j(t,Y)R^j,
    A_r!=0,

and define v_(2,1) on K[t,Y] by assigning t weight2 and Y weight1. Then

    a_x(F)<=v_(2,1)(A_r).                        (3)

Indeed, after translating r_x to zero, decompose F into homogeneous pieces
in (Y,R). The local substitution preserves their homogeneous degree in the
formal (R,E) variables, so the contact of the full polynomial is the minimum
of their contacts. Write

    A_r(t,Y)=sum_k B_k(t)Y^k.

For every nonzero B_k, the homogeneous piece of degree k+r has R-degree
exactly r. Strip its factor Y^k and apply the local inequality (1): its
contact is at most k+2ord_t B_k. Hence the full contact is at most the minimum
of these numbers, which is precisely v_(2,1)(A_r).

Thus the proposed local leading-coefficient inequality is PROVED for every
polynomial and every received symbol. To turn it into the unrestricted global
R-degree gap one still needs a global weighted-degree bound for the sum of
these anisotropic orders of the bivariate polynomial A_r at arbitrary
received points. That separate global assertion is not proved by (3) alone.
