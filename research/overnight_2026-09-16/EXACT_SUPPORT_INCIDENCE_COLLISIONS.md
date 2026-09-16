# Exact support incidences sharpen the prime-field line certificate

September16, 2026. Selected coordinate incidences have a separate formal
division check. The additional third-coefficient refinement has also passed its separate
rational-dual check.

At n82/k9/t12 over F_(2^31-1), the exact-incidence calculation gives
**138752510 labels**, with excess greater than **7.04613 bits**.
Its source class has221190005 supports with

    sum x=486,  sum binomial(x,2)=12792.

The largest two-moment class has221283217 supports at second moment12840,
but the slightly smaller selected class gives a stronger collision bound.
The common locator prefix of the selected class is

    X^12 -486 X^11 +105063 X^10.

The incidence calculation alone gives138752300 labels; the next-coefficient
saving adds210. The result concerns the stated finite interval example. It does not change
the pinned better.codes bound or claim an optimum over arbitrary lines.

## Exact coordinate incidences

For a support class C, let N=|C| and I_x=#{A in C:x in A}. The exact number
of shared support roots, counted over unordered pairs, is

    S = sum_x binomial(I_x,2).

If the common prefix leaves residual degree at most k, the total number of
pairwise collisions at poles outside the domain is at most

    B = k*binomial(N,2)-S.

Thus some pole has at most floor(B/(p-n)) colliding pairs. If P(N,J) is the
minimum number of colliding unordered pairs when N objects occupy J bins,
then the guaranteed label count is the least integer J with

    P(N,J)<=floor(B/(p-n)),
    P(N,J)=J*binomial(a,2)+b*a,  N=a*J+b, 0<=b<J.

The earlier bound replaced S by its balanced-incidence lower bound. Exact
incidences retain the additional saving from nonuniform coordinate counts.
For the selected n82 class,

    S=43128963788215318,
    B=177033617619979772,
    floor(B/(p-n))=82437705.

The same received-line construction and its concurrency upper bound24
apply; common agreement is9.

## Counting and separate verification

For each x, the producer omits x and counts(t-1)-subsets with first sum q-x.
Its entire second-moment histogram gives I_x for every original class at
once. All three identities are checked for every nonempty class:

    sum_x I_x=t*N,
    sum_x x*I_x=q*N,
    sum_x binomial(x,2)*I_x=Y*N.

The selected incidences are separately checked without omitting an item.
Let H(k,q,Y) be the original unconditioned subset coefficient. Formal
division of the subset generating product by(1+z*u^x*v^binomial(x,2)) gives

    I_x=sum_(j=1)^t (-1)^(j-1)
            H(t-j,q-j*x,Y-j*binomial(x,2)).

The verifier computes these coefficients with the original histogram
engine in increasing item order. This is a different recurrence identity
and item order, while sharing the underlying centered histogram engine.
The omitted-item engine also passes350 exhaustive small fixtures.

Programs: conditioned_quadratic_histogram.cpp,
compute_exact_support_incidences.py, verify_exact_support_incidences.py.
The n82 evidence files begin exact_support_incidences_n82_t12_q486.

## Further degree savings from the next coefficient

Write Z=sum binomial(x,3). With q and Y fixed, Newton identities make the
third elementary symmetric coefficient an affine function of Z. Explicitly,

    e_3 = binomial(q,3)+(2-q)*Y+2*Z.

The coefficient 2 is nonzero in the stated odd characteristic. If Z lies
in an integer interval with K entries, there are at most min(K,p) possible
next coefficients. At least P(N,min(K,p)) unordered source pairs share that
coefficient and therefore have difference degree at most k-1. Their degree
budget can be reduced by one before charging shared support roots:

    B <= k*binomial(N,2)-S-P(N,min(K,p)).

An exact min/max subset recurrence proposes intervals. A separate checker
uses rational linear inequalities to certify the final intervals: choose
rational lambda_0,lambda_1,lambda_2, let

    r_x=binomial(x,3)-lambda_0-lambda_1*x-lambda_2*binomial(x,2).

For every incidence vector z_x in{0,1} with the three prescribed sums,

    Z >= lambda_0*t+lambda_1*q+lambda_2*Y+sum_x min(0,r_x).

Negating the cost gives an upper bound. Floating linear optimization only
proposes the rational multipliers; the termwise inequalities certify the
bound with exact fractions. These dual intervals may be wider than the
computed exact extrema, so only the separately certified final bank should
be quoted. Evidence: third_coefficient_collision_verification.json.

## Final next-coefficient certificate

For the selected n82 class, the independent rational dual places Z between
222145 and276503. It forces at least449907051360 pairs to share the next
coefficient, reducing the averaged pair budget to82437495. The guaranteed
bank is138752510, with excess7.046137768370497bits. The tighter extrema
222780 and275868 found by the min/max DP would add five more labels; that
stronger value is not used in the final independently certified headline.

All seven selected parameter cases passed the same separate checks.
The n85 bank is153142746, with excess6.972106342218605bits. Six additional
nearby first sums produced no improvement; their nonrecord incidence scans
are explicitly discovery-only. See nearby_incidence_queue_status.json.

## Further refinement to investigate

The termwise rational dual relaxes the cardinality and first-sum conditions.
One can retain them exactly in a smaller dynamic program: for an integer
denominator d>0 and slope b, minimize

    sum_(x in U) [d*binomial(x,3)-b*binomial(x,2)]

over t-subsets with sum q. If that minimum is M, every member of the
selected two-moment class has Z >= ceil((M+b*Y)/d). Negating the cubic
cost gives an upper bound. This recurrence needs only cardinality and
first sum as state coordinates. It is a possible refinement of the dual
certificate; it is not included in the final numerical claims above.
