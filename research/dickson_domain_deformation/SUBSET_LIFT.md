# A ten-candidate subset of the characteristic-41 bank does lift

September 17, 2026. This is a finite positive example, not an asymptotic
list lower bound. It complements the all-ramification obstruction for
the complete twenty-candidate incidence seed.

In the binomial formula from README.md, retain precisely the labels

    a=3,8,10,11,12,13,16,17,18,20.

At the forty nodes x=1,...,40 over F_41, each selected degree-at-most-nine
polynomial has exactly fifteen agreements with the original received
word. Every node belongs to at least one selected agreement support.
Eliminating the freely moving received values produces110 equations in
140 variables (40 nodes and100 candidate coefficients).

The verifier finds a110-column Jacobian minor with determinant29 modulo41.
It independently recomputes that determinant, solves the linear correction,
and directly evaluates the lifted polynomial incidences modulo1681.
All original selected agreement and nonagreement supports are preserved.
The pivot columns, correction, lifted nodes, and lifted coefficients are
saved in subset_lift_verification.json.

The unit minor gives a multivariate Hensel lift over Z_41, fixing the
remaining thirty variables at their canonical representatives. Distinct
nodes and candidate polynomials stay distinct. Define each received
value by a selected incident polynomial; the equations ensure it is
well-defined. Every selected candidate still has exactly fifteen
agreements, since its original nonagreements remain units.

This supplies a characteristic-zero code with

    n=40, k=10, rate=1/4, agreement=3/8, gap=1/8,
    list size at least10.

Encode the incidences, distinctness, and selected nonagreements by
polynomial equations and inequations over Q. Their41-adic realization
makes this finite-type locus nonempty, hence it has an algebraic-number
point. Clearing denominators and taking sufficiently large completely
split primes preserves the same finite data. Thus the selected bank
occurs over arbitrarily large prime fields. No prime-size bound is given.

We have NOT proved that these ten candidates are the entire list, or
that fifteen is the maximum agreement. This differs from the stronger
complete-profile conclusion proved for the smaller characteristic-17
seed. The agreement3/8 is below the coauthor first-order curve at rate1/4,
so this example is not first-order exponent tightness. Generic lifting
can enlarge its length but does not turn the fixed bank into growing
lists at a fixed gap.

The ten-candidate lift shows that the characteristic-41 obstruction is
sensitive to the incidence bank, rather than excluding all useful
subsets of that source. A bounded exploratory search found this subset;
no claim is made that ten is the largest liftable subset or that the
unsuccessful tested subsets cannot lift.

Reproduce with verify_subset_lift.py. The run passes under the384MiB
watchdog in about half a second.
