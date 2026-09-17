# Linear lower examples with entirely singular agreement supports

Let n distinct elements x_i lie in F_q, char(F_q)>D, and let S be a
fixed subset of s coordinates with D<s<n. Put A=s+1 and
R0(X)=product_{x in S}(X-x). Choose nonzero scalars u_i outside S.
Define the received line by

    f(x)=0, g(x)=x^D                         (x in S),
    f(x_i)=-u_i x_i, g(x_i)=x_i^D+u_i       (x_i outside S).

At each of the n-s distinct labels z=x_i outside S, the candidate
P_z(X)=zX^D agrees on exactly S union {x_i}. Its full agreement support
has no common direction polynomial of degree at most D: the s>D core
coordinates force that polynomial to be X^D, which fails at x_i.
Thus these are n-s bad full-support witnesses, for every choice of u_i.

Set U=v-zD X^(D-1) and use the implicit first-order identity

    Q(X,z,u,v)=R0(X)(X-z) U+U^2.

It has total jet degree 2 and challenge degree at most 2. Every P_z
satisfies it. Its separant is R0(X)(X-z)+2U; on these candidates it is
R0(X)(X-z), so EVERY agreement coordinate is singular. Outside S there
is at most one singular coordinate, giving e=1 with no exceptional
labels. In fact every degree-at-most-D solution is zX^D+c: writing
h=P'-zD X^(D-1), the identity is h(h+R0(X)(X-z))=0, and the second factor
cannot vanish identically because deg h<=D-1<s+1. The characteristic
hypothesis then integrates h=0. For arbitrary u_i we do not claim that
only c=0 can be nearby; the displayed witnesses suffice.

## Strengthening to absence of any ordinary common agreement

Choose the u_i independently and uniformly from F_q^*. If

    2^n q^{-(s-D)} (1-1/q)^{-(n-s)} < 1,                 (1)

there exists a choice for which NO degree-at-most-D polynomial agrees
with g on A coordinates. Consequently the line has no ordinary
A-coordinate common agreement, regardless of its intercept f, while
still possessing the n-s entirely singular nearby witnesses above.

Proof: subtract X^D from a prospective direction polynomial. The zero
polynomial matches exactly the s core coordinates. A nonzero polynomial
H of degree at most D matching a chosen A-subset with m core coordinates
must vanish at those m coordinates. If m>D this is impossible. Otherwise
there are at most q^(D+1-m) such H, and each matches the remaining
A-m independent random nonzero values with probability at most
(q-1)^(-(A-m)). For this subset the union bound is at most
q^(D-s)(1-1/q)^(-(n-s)). There are at most 2^n subsets. Condition (1)
makes their combined probability strictly less than one.

For fixed positive (s-D)/n, (1) holds for all sufficiently large primes
q>n. This is an existence proof, not an explicit deterministic direction.
For example n=100m, D=25m-1, s=48m-1, A=48m gives quarter-rate codes,
agreement .48 above the quarter-rate first-order curve, and 52m+1 bad
labels. In fact every prime q>100m suffices: q>=101 and
-log(1-1/q)<=1/(q-1)<=1/100 give the logarithmic bound
100m log 2-23m log 101+(52m+1)/100<0. The fixed-cover theorem has kappa=floor((121m-3)/3) and
L=48m-1-kappa, which is positive and linear in n. Thus its O(n) order
is sharp in this subclass; this does not establish a quadratic lower
bound for general first-order proximity gaps.

## Small deterministic fixture and threshold boundary

With F_7, D=1, all seven coordinates, S={0,1,2,3}, and u_i=1,
there are exactly three A=5 nearby pairs: (z,P)=(4,4X),(5,5X),(6,6X).
Every one has zero nonsingular agreements. This fixture only certifies
full-support badness; the probabilistic construction above supplies the
stronger ordinary-common-agreement exclusion.

The strict triple-intersection inequality is necessary for its stated
conclusion. In F_7 take S={0,1,2,4}, D=1, labels 0,1,2 and candidates
0,X,1. Received values f=(6,0,0,0), g=(1,4,2,4) in that coordinate order
give each candidate exactly three S-agreements, while they do not form
an affine polynomial pencil in the labels. Here 3*3-2*4=D, equality.
