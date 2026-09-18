# Cubic first-order helpers: a collision bound

Research theorem, proved below; cubic and general-degree statements independently audited. See [CUBIC_ODE_INDEPENDENT_AUDIT.md](CUBIC_ODE_INDEPENDENT_AUDIT.md). This concerns only helpers linear in the first derivative, not general higher-jet helpers or all interpolation kernels.

Let k have characteristic zero, and let distinct P_1,...,P_L in k[X], of degrees at most w, solve

    d(X) P_i'(X) = F(X,P_i(X)),   deg_Y F <= 3,

where d is nonzero. Divide the common gcd of d and all coefficients of F first. Suppose each P_i agrees with one fixed received word on at least A of n distinct nodes. Define

    kappa_L = min_{2 <= b <= L}
      [binom(b,2)+binom(max(L-b-1,0),2)]/(b-1).

Then

    kappa_L (L A - n) <= binom(L,2) w.                 (1)

The same assertion holds in characteristic p > 3w^2. No claim is made here for arbitrary small characteristic.

## Local proof, including denominator singularities

At a node a where d(a) != 0, two distinct polynomial solutions cannot share a value: subtract their equations, and compare the lowest terms of their difference t^h, t=X-a. The derivative has order h-1 and the right side order at least h. Here 1<=h<=w and h is nonzero in the stated characteristics.

At a root a of d, the primitive polynomial F(a,Y) is nonzero, and all solution values are roots of it. If two solutions share c and their difference has order h, subtraction gives

    d (P_i-P_j)' = (P_i-P_j) [F_Y(a,c)+O(t)].

If d has a simple root, it follows that F_Y(a,c)=h d'(a). Thus a repeated-value bucket is a simple root of F(a,Y), with positive integer resonance h. If three different roots supported repeated buckets, F(a,Y) would be a cubic with three simple roots c_1,c_2,c_3. Partial fractions of 1/F(a,Y) give

    sum_j 1/F_Y(a,c_j) = 0,

and hence sum_j 1/h_j=0. This is impossible in characteristic zero. In characteristic p>3w^2, clearing denominators gives the positive integer h_1 h_2+h_1 h_3+h_2 h_3, between 1 and 3w^2, also impossible. Consequently at most two value buckets repeat, and if two do, the remaining bucket has size at most one.

If d has order at least two, the same difference equation forces F_Y(a,c)=0 for every repeated bucket. A polynomial of degree at most three has at most one distinct multiple root. If such a root exists, at most one other root remains. Thus here there is at most one repeated bucket and at most one singleton outside it.

These statements also cover degree drops of F(a,Y). No denominator is evaluated after division by d.

## Global collision count

Let b_a be the number of solutions matching the received value at a, and let T_a count all unordered pairs of solutions sharing any value at a. For b_a>=2, the local classification gives

    T_a >= binom(b_a,2)+binom(max(L-b_a-1,0),2).

Indeed the outside solutions occupy at most two buckets, at least one of which has size at most one (the other bucket is allowed to be a singleton too). For b_a=0 or 1, the inequality T_a>=kappa_L(b_a-1) holds trivially. Summing and using each nonzero P_i-P_j has at most w roots gives (1).

As L grows, kappa_L/L tends to sqrt(2)-1. Thus an unbounded sequence of banks satisfying this common cubic ODE must satisfy asymptotically A/w <= (1+sqrt(2))/2, if n/(Lw) tends to zero. This is a necessary condition, not an existence statement below that ratio.

## Benchmark consequence

For n=262144, w=131071, A=181275 and L=14, kappa_14=21/4 (attained at b=9). The left side of (1) is 23894913/2, while its right side is 11927461; the difference is 39991/2>0. Hence no fourteen nearby polynomial graphs can share such a cubic first-order ODE; every bank in this subclass has at most thirteen members (apply the result to any fourteen-member subset).

For a weighted-contact helper dR-sum_j a_jY^j of weight below mA, substituting each nearby graph gives a polynomial of degree below mA with at least mA zeros, hence the common ODE identity. This applies to a fixed received word and fixed helper; it does not identify codewords attached to different labels on a received line.

## Why the Riccati argument does not extend unchanged

At a simple cubic pole two repeated buckets really are compatible with local resonance. For X Y'=Y^3-Y the values +1 and -1 both have resonance 2, whereas 0 has resonance -1. This gives local formal freedom, not a polynomial solution bank. The present proof explicitly allows the two large buckets.

For four solutions the usual cross-ratio C instead satisfies

    C'/C = (a_3/d)(P_1-P_2)(P_3-P_4),

with C=(P_1-P_3)(P_2-P_4)/((P_1-P_4)(P_2-P_3)). It is generally not constant.

## Literature scope

Calderon, 'Rational solutions and limit cycles of polynomial and trigonometric Abel equations', EJQTDE 2025 No.18, studies normalized equations with polynomial coefficients and bounds rational solutions/invariant curves:
https://www.math.u-szeged.hu/ejqtde/p11345.pdf
Those results do not directly apply to the rational coefficients a_j/d allowed here. The bound above is proved directly and is not attributed to that paper. No novelty claim is made without a fuller literature comparison.


## General degree q >= 3

Let B_s(M) denote the minimum pair collisions when M objects occupy s buckets:
write M=sv+r, 0<=r<s, and put B_s(M)=s*binom(v,2)+rv. Define

    kappa_(L,q) = min_{2<=b<=L}
       [binom(b,2)+B_(q-2)(max(L-b-1,0))]/(b-1).

For deg_Y F<=q, the same proof gives

    kappa_(L,q) (LA-n) <= binom(L,2) w.

Characteristic zero suffices; a uniform safe positive-characteristic condition is p>q*w^(q-1). At a simple denominator pole, if there are q distinct roots and all buckets repeat, the partial-fraction identity forces sum_i 1/h_i=0. Its cleared numerator is a positive integer at most q*w^(q-1). If there are fewer than q roots, add empty buckets instead. Thus in all cases the q padded buckets include one of size at most one. Since the matched bucket has b>=2, that small bucket lies outside it. At a multiple denominator pole a matched repeated bucket requires a multiple root of F(a,Y), so there are at most q-1 distinct roots; again pad an empty bucket. After reserving the small bucket, balance the remaining outside population across q-2 buckets to obtain the displayed bound. Cases b<=1 remain trivial.

Asymptotically kappa_(L,q)/L tends to 1/(1+sqrt(q-1)), so the necessary large-list agreement/degree ratio becomes (1+sqrt(q-1))/2. For q=4 this is about 1.366025, below the benchmark A/w about 1.383. The exact first violating subset size is L=170: kappa_(170,4)=493/8, and the inequality fails by 370719/4. Thus this quartic first-order subclass supports at most 169 benchmark-nearby graphs. This is an agreement bound for a common equation, not a bound on all polynomial solutions without an agreement hypothesis.

## Interpolation cost: these subclasses do not yet give a gain

For the full coefficient-prefix source {1,Y,...,Y^q,R}, strict weighted cap mA and weights (1,w,w-1), the source dimension is

    C = sum_(j=0)^q max(mA-jw,0) + max(mA-w+1,0).

Remove absent highest Y powers before computing local ranks. With q>=1, the full formal coefficient-jet local weighted first-jet row rank is

    r = 2m + max(m-2,0) + sum_(j=2)^q max(m-j,0).

To see this, translate Y by the received value and substitute Y=tR+t^2 E. The coefficient of R^j, j>=2, forces the translated Y^j coefficient to have t-order at least m-j. The constant coefficient has order at least m. The linear coefficient must have order at least m-2, and its tR term can cancel the separate R coefficient, imposing m further conditions on that combination. These are independent triangular coefficient conditions in the full formal coefficient-jet space. For finite global X-prefix caps this is the ordinary local-row ledger, not an assertion that every formal local jet is realized by the truncated global source. Translation changes the global weighted source, but it preserves the local polynomial-in-Y/R support used for this row-rank calculation.

At the benchmark, every q<=4 and every integer m>=1 has C-nr<0. The finitely many initial values m=1,2,3,4, after removing absent powers, have maximal margins respectively -242604, -122659, -275982, -499052. For m>=4 all q<=4 are present and all local truncations stabilize, yielding exactly

    C-nr = (q(q+1)/2+1)(n-w) - (q+2)m(n-A) + 1,

strictly decreasing in m. Thus ordinary dimension counting in these complete-prefix sources never produces a helper at this benchmark. The new ODE bounds would become useful only with a proved list-conditioned rank defect/cancellation or a different admissible source; they do not supply such a defect themselves.
