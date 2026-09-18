# Independent audit of the cubic first-order collision bound

Status: PASS. Scope: one common rational cubic first-order ODE for distinct degree-at-most-w polynomial solutions, and one fixed received word. Characteristic zero or p>3w^2 is sufficient. No novelty claim or general higher-jet conclusion is made.

## Local pole audit

Divide the common gcd of d and all Y-coefficients of F before analyzing a node. Then F(a,Y) is nonzero whenever d(a)=0, even after extending the constant field. All polynomial solution values at such a node are roots of this nonzero degree-at-most-three polynomial.

For a pair with difference t^h times a unit, 1<=h<=w. Subtracting the ODEs and dividing their difference gives d*(P_i-P_j)'/(P_i-P_j)=F_Y(a,c)+O(t). If d is a unit, the left side has a nonzero simple pole, contradicting the regular right side. If ord_a(d)=1, its constant term is h*d'(a), so F_Y(a,c)=h*d'(a) is nonzero. If ord_a(d)>=2, its constant term is zero, so F_Y(a,c)=0. These comparisons remain valid in the stated characteristic because h is nonzero.

At a simple pole, three repeated value buckets would give three simple roots of the cubic F(a,Y). The partial-fraction identity sum_c 1/F_Y(a,c)=0 then gives sum_j 1/h_j=0. In characteristic zero the three positive rational numbers cannot sum to zero. In characteristic p>3w^2, clearing the nonzero denominators gives a positive integer h1*h2+h1*h3+h2*h3 at most 3w^2, again impossible. At a higher-order pole, a repeated bucket is a multiple root, so there is at most one such root and at most one other root for a cubic. Degree drops only strengthen these conclusions.

## Bucket bound and minor wording repair

For a matched bucket of size b>=2, the outside solutions occupy at most two root buckets, at most one of which can have size greater than one. Consequently, writing M=L-b, their collision contribution is at least binom(max(M-1,0),2). This includes the case of two outside singleton buckets (M=2), whose contribution is zero. The original prose claiming literally at most one outside singleton should be read with this qualification; the displayed inequality is correct.

Therefore T_a>=binom(b,2)+binom(max(L-b-1,0),2). For b=0 or 1, T_a>=kappa_L*(b-1) is automatic. Sum over nodes, use total carried incidence at least L*A, and bound all pairwise polynomial intersections by binom(L,2)*w. This gives precisely the claimed global inequality.

## Exact benchmark arithmetic

For L=14 the minimum is kappa_14=21/4, attained at b=9. With n=262144, A=181275, w=131071,

    kappa_14*(14*A-n) = 23894913/2,
    binom(14,2)*w    = 11927461,
    difference      = 39991/2 > 0.

Thus every bank in this common-cubic-ODE subclass has at most thirteen members, by applying the contradiction to any fourteen-member subset. The earlier saved values 23895213/2 and 40291/2 were arithmetic typos; they are not the correct certificate.

The free-E weighted-contact specialization into (P,P') remains legitimate: P(a+t)-P(a)-tP'(a+t) is divisible by t^2. Original weight below mA makes the restricted polynomial degree below mA, while A matching nodes give order at least m each. Hence the helper indeed forces the ODE identity for each candidate at the same received-word label.

## Cross-ratio and scope

For the displayed cross-ratio, logarithmic differentiation of four differences leaves (a3/d)*(P1-P2)*(P3-P4), with the sign as stated. Thus the earlier constant-cross-ratio Riccati proof cannot be reused unchanged. The cubic proof instead relies on the positive-integer resonances at simple denominator roots. It permits two large local value buckets and does not assert that this local freedom produces a global polynomial bank.

## General q extension and exact quartic threshold

Independent audit: PASS for the appended extension to every q>=3. At a simple pole, if F(a,Y) has exactly q distinct roots and every root bucket repeats, all q resonance orders h_i are positive integers at most w, and sum_i 1/h_i=0. In characteristic zero this is impossible. In positive characteristic, its numerator is the positive integer sum_i product_(j!=i) h_j, at most q*w^(q-1), so p greater than this bound is sufficient. If the polynomial has fewer distinct roots, padding to q root slots introduces an empty bucket. At a higher-order pole, the matched repeated bucket must be a multiple root, so at most q-1 distinct roots exist, again providing an empty slot. Thus when the received bucket has size b>=2, at least one of the q-1 outside slots has size zero or one.

For M=L-b outside solutions, occupying the reserved small slot with one object whenever possible leaves max(M-1,0) objects for q-2 unrestricted slots. Convexity of binomial(u,2) makes balanced allocation minimize their total collision count. If the actual reserved slot is empty, it only increases this minimum. This proves the claimed B_(q-2)(max(L-b-1,0)) lower bound with no assumption that the other slots repeat or are all occupied.

The asymptotic minimization sets b/L=x and minimizes one half of [x^2+(1-x)^2/(q-2)]/x. Its minimizer is x=1/sqrt(q-1), and the minimum is 1/(1+sqrt(q-1)), confirming the stated limiting constant.

An independent exact rational evaluation for every L=2,...,170 at q=4 finds its first positive violation at L=170, with kappa=493/8, b=97, excess370719/4. At L=169 the minimum is 5881/96 and excess -96325/96. All rows are saved in `quartic_ode.independent.json`. Applying the L=170 contradiction to a subset proves the at-most-169 benchmark statement for arbitrary larger banks as well.

## Provenance and novelty assessment

The proof is self-contained, but its ingredients are elementary local ODE resonance, the partial-fraction identity for reciprocal polynomial derivatives, convex bucket allocation, and the polynomial pair-root bound. The note should describe a derived fixed-word collision bound, not claim a new general Abel-equation theorem. The specific agreement inequality may be a useful application, but independent derivation is not evidence of literature novelty. The separately inspected normalized polynomial-coefficient Abel literature does not automatically cover rational coefficients with denominator poles, so it also does not by itself establish that the present statement is already a quoted theorem. The current explicit no-novelty-claim wording is appropriate. No manuscript expansion is justified merely by the numerical quartic cutoff absent an actual interpolation gain.
