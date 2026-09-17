# Paired domains: prospective two-coordinate separation

Internal working proof, September 17, 2026. Not yet integrated or audited.

Simplest route, no moments: pick m nonzero field elements a_i with distinct
squares, core ±a_i. For every D-subset I, H_I(X)=prod_(i in I)(X²-a_i²).
Fix H_0=w and P_I=w-H_I. Then deg P_I<=2D-2, so K=2D-1 suffices.
Each candidate agrees on exactly 2D core nodes. A padding pair ±x with
same nonzero direction at its two nodes adds TWO agreements when its
label matches. Nearby threshold A=2D+2; gap=(A-K)/n=3/n; the zero
parameter is exactly TWO coordinates beyond radius, or 2eta/3.

For uniformly chosen good seed tuples, every support pair has average
outside-orbit collisions <=
 B=(p-1)(p+6sqrt(p)+768)/(2p(p-m²)).
Reason: residual support difference size u=1 has no outside collisions.
For u>=2, expose two unique seed variables a,b on one side and all
other variables. At nonzero outside x, collision becomes
 (x²-a²)(x²-b²)=C !=0.
This affine degree4 curve is absolutely irreducible: as a quadratic in
a, its right-hand side a²=x²-C/(x²-b²) has simple poles at b=±x,
so is not a square over the algebraic closure; its numerator and
denominator are coprime. Gauss's lemma completes the argument.
Cafure–Matera Cor5.6 gives at most p+6sqrt(p)+768 points for p>32.
There are p^(m-2) choices of remaining seed variables and p-1 choices
of nonzero x. Divide by2 to count ±x orbits. Good tuples number at
least p^m(1-m²/p): zero seeds and equal ±pairs are the only exclusions.
Dividing gives B. Bad choices of exposed variables only reduce count.

L=binom(m,D), R=(p-1)/2-m, U=p-1. Average collision energy gives
M=LR/[R+(L-1)B]. A good tuple exists with mean image>=M. Picking q
largest outside-orbit images and random nonzero directions covers all
nonzero labels if U(1-M/U)^q<1. n=2m+2q. Far point follows from
monic degree2D; zero candidate attains2D roots. No correlated agreement.

Half rate: n=2 mod4, K=n/2, D=(K+1)/2. Choose beta>1/2 near1/2,
alpha=(1/2)/beta, n~C log2p, m~alpha n/2. Require
 2/(alpha H(beta)) < C < 3/H(1/2)=3.
Then L>p^(1+epsilon), UB/R→1, q=Theta(logp), giving full punctured
coverage, strict Elias, and n*2^(1/eta)=o(p), with far2eta/3.
Random sampling needs no moment class and has failure bound
 delta/gamma + U*(gamma/(1+gamma))^q,
 delta=U/L+UB/R-1.

Potential generalization for arbitrary numerical constant c2:
choose integer seed nodes with every four signed cubic planes involving
four distinct nodes independent. A greedy choice in [1,O(m^4)] should
exist by avoiding degree<=3 equations from each previous triple and
sign assignment. Map a→phi(a)=a³+ba²+ca and use paired nodes±phi(a).
Match first6s integer moments on D-subsets. Then firsts moments of
phi(a)² agree, so degree P_I<=2D-2s-2, K=2D-2s-1, A=2D+2,
gap=(2s+3)/n, far2/n. For residual u>=2 the 4u-plane arrangement
should be irreducible using smooth triple base points involving three
distinct underlying seed nodes. Same-node signs connect via a different
node on the same side. The forced fourfold intersections on X=0 are
avoided by these paths. u1 gives only noninjective maps. Good maps
at least p²-m²p. Collision multiplier
 [p+(2D-1)(2D-2)sqrtp+3(2D)^4]/[2(p-m²)].
Require 2s+3>2c2. Exact rational rates with odd numerator fit odd K;
even numerator needs a separate dimension/domain adjustment.
This generalization remains unproved until determinant and connectivity
conditions, greedy seed construction, and degree bookkeeping audited.

Exact-rate parity resolution (audited algebraically, pending finite replay):
For rational rho=a/b reduced, take an odd multiple n of b. If a is odd,
K=rho*n is odd; use the paired construction directly, and add coordinate
0 iff n is odd. With no X factor, no selected candidate agrees with w
at 0, since every H_I(0) is nonzero. This extra coordinate does not change
A or the exact far agreement. If a is even then b and n are odd and K
is even. Multiply w and every candidate by X, include coordinate0 with
f=g=0, and take K=2D. Degrees, nearby threshold and exact far agreement
all increase by one; eta remains3/n and separation2/n. On a padding
pair use g(x)=x*h and g(-x)=-x*h. Thus every rational fixed rate is
possible, with at most one extra coordinate and no change to asymptotics.

The simple paired theorem defeats any fixed c1 and c2<3/2, and gives
far separation2eta/3. It does NOT defeat arbitrary c2 by itself. The
existing cubic-moment theorem still supplies that separate conclusion.
