# Generic quadratic towers cannot create growing fixed-gap lists

September 17, 2026. This extends the earlier fixed-dimension profile
argument to arbitrary degree caps, which may vary with tower height.
It is a limitation of this generic lifting construction, not a universal
list bound for arbitrary Reed--Solomon domains.

## Statement

Start with any word on N0 distinct characteristic-zero nodes. Form a
generic tower of s quadratic fibers, repeating the source symbol on both
roots at every step. Thus n=B*N0 with B=2^s. Fix ANY degree cap D<n
and agreement threshold D<A<=n. Put Delta=A-D, and let C be the largest
power of two not exceeding min(B,Delta).

Every degree-at-most-D candidate with at least A agreements descends
through log2(C) quadratic steps. Consequently its list size satisfies

    L <= binom(n/C, floor(D/C)+1)
      <= 2^(n/C)
      <= 2^max(N0, 2*n/(A-D)).                         (1)

The descent uses the last log2(C) maps of the tower; it need not reach
the original N0-node word. For a fixed positive capacity gap
eta=(A-(D+1))/n, (1) is at most 2^max(N0,2/eta), independently of s.
Thus choosing a different rate or degree cap at each lift does not
produce an unbounded list at a fixed positive gap from one fixed seed.

For each fixed tower height, suitable algebraic specializations and
arbitrarily large splitting primes preserve the statement simultaneously
for all D and A. This is an existence claim without a field-size bound.
It is not asserted for every specialization of the tower parameters.

## One step at an arbitrary degree

Let K contain the source nodes a_i and symbols w_i, and let t be
transcendental over K. The new nodes are the roots of X^2=t+a_i.
The splitting field has independent involutions on the root pairs:
the distinct prime divisors t+a_i show that their square classes are
independent in K(t)^*/K(t)^{*2}.

Suppose deg P<=D and P has h>=D+2 agreements. Its coefficients lie
in the splitting field, by interpolation on D+1 agreeing nodes.
For any single-pair involution, P and its conjugate share at least
h-1 agreements. Indeed a pair with both agreements keeps both, a pair
with no agreements loses none, and a pair with one agreement loses
at most that one. Since h-1>D, the two polynomials coincide. All
involutions fix P, so its coefficients lie in K(t).

A single agreement now forces the second root in the pair to agree.
Write

    P(X)=Q0(X^2-t)+X*Q1(X^2-t),
    deg Q0<=floor(D/2), deg Q1<=floor((D-1)/2).

At each agreeing pair Q1(a_i)=0. There are h/2>deg Q1 such pairs,
so Q1=0. The remaining Q0 is determined by its agreeing source nodes,
which also shows its coefficients lie in K, rather than merely K(t).
The degree cap becomes floor(D/2), and the exact agreement count halves.

The extra agreement beyond the interpolation dimension matters:
h=D+1 alone does not force conjugates to coincide.

## Iterating only as far as the agreement surplus allows

After j descents, the degree is at most floor(D/2^j), and the actual
agreement count equals h/2^j. Before the last of log2(C) steps,

    h/2^j-floor(D/2^j) >= (A-D)/2^j >= 2.

Thus every claimed step meets the one-step hypothesis. At the end,
the residual word has n/C nodes and candidate degree at most floor(D/C).
Each candidate has at least floor(D/C)+1 agreements, so it is uniquely
determined by one such subset. Composition is injective, giving the
binomial bound in (1).

If C=B, the residual length is N0. Otherwise Delta<2C, so its length
is less than 2n/Delta. This proves the final inequality. Notice that
D+1 is the code dimension, whereas Delta uses D. In terms of capacity
gap, Delta=eta*n+1; no extra agreement is lost in that conversion.

## Specialization

For fixed n there are only finitely many D, A and determining supports.
Each generically inconsistent agreement support has a nonzero augmented
Vandermonde minor. Avoid their zero sets, all node collisions, and the
denominators of these finite algebraic calculations. This is a nonempty
open set in the finite splitting cover of the parameter space. Choose
algebraic parameters there and then exclude the finitely many primes
destroying these certificates. Completely split primes realize all nodes
in the prime field and preserve the bound. As before, this supplies no
quantitative bound on a prime realizing the chosen specialization.

## Exhaustive finite example: the intermediate level is necessary

The existing tower with p=1000000007, t1=63, t2=1556, and base nodes
(-2,-1,0,1,2) with symbols (2,1,0,1,2) has n=20. At degree cap D=4,
the complete list with at least A=6 agreements has 70 members:

* 64 have six agreements;
* four have eight agreements;
* two have twelve agreements.

All descend one step to degree-at-most-two candidates on the ten-node
intermediate word. These are exactly its 70 distinct interpolants
determined by triples. The general bound here is binom(10,3)=120.
Only the two twelve-agreement candidates necessarily descend all the
way to the original word. This illustrates why the previous complete
profile statement at dimension eight cannot simply be reused unchanged
at dimension five.

verify_variable_degree.py exhausts all15504 five-node supports, obtaining
13382 distinct interpolants. It checks every above-dimension candidate's
composition identity and exact halved agreement count, and independently
exhausts the120 residual determining triples. The bounded replay passes
in about half a second. The all-height assertion follows from the
algebraic argument, not from this finite enumeration.
