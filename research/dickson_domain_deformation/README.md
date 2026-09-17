# Free-domain Dickson deformation: two certified finite tests

September 17, 2026. These results do not establish growing lists at a
fixed positive gap. They test the exact incidence banks at p=17 and 41,
allowing every evaluation node, candidate coefficient, and received
symbol to move. The larger seed has an unramified lifting obstruction;
ramified lifts and other incidence patterns remain open.

## Equations and certificates

Set n=p-1, k=n/4, L=n/2, A=3n/8. On x=1,...,p-1 use

    w(x)=(1+chi(x))/2-x^k,
    P_a(X)=sum_{j=0}^{k-1} binom((p+1)/2,2j+1)
                      a^((p+1)/2-2j-1) X^j,
    1 <= a <= (p-1)/2.

Each distinct P_a has A agreements. At each node choose one incident
candidate as reference and impose P_i(x)-P_ref(x)=0 for the other
incident candidates. This eliminates the freely varying received value.
Nodes with no incidences impose no equations. For canonical integer
lifts, the correction equation modulo p is

    sum_t x^t (delta c_i,t-delta c_ref,t)
       +(P_i'(x)-P_ref'(x)) delta x
       = -(P_i(x)-P_ref(x))/p.

The numerator is first evaluated modulo p^2. The generator saves the
original equations, a correction and pivot columns in the positive
case, or a left-kernel obstruction in the negative case. The independent
stdlib verifier reconstructs evaluations directly from the binomial
formula; it does not import generator routines.

## Positive finite case: p=17

There are 32 equations and 48 variables. A saved 32-column Jacobian minor
has determinant 1 modulo 17, independently recomputed. The saved first
correction satisfies every incidence equation modulo 289.

The invertible minor gives a multivariate Hensel lift over Z_17: fix the
remaining variables at their integer representatives and solve for the
32 pivot variables. Nodes stay distinct, candidate polynomials stay
distinct, and every original nonagreement remains a nonagreement,
because these differences are nonzero modulo 17.

Exhaustion of all binom(16,4)=1820 determining supports proves that the
original word has maximum agreement 6 and exactly 22 nearest candidates.
Only the selected EIGHT candidates are lifted here. The maximum agreement
of the lifted word is still 6. Indeed, any degree-at-most-3 polynomial
over Q_17 (or its algebraic closure) agreeing at seven lifted nodes is
determined by four of them. The interpolation denominators are units,
so its coefficients are integral; its reduction gives a polynomial
agreeing at seven distinct original nodes, a contradiction.

This gives a characteristic-zero finite nearest-list example with
n=16, k=4, maximum agreement 6, and at least 8 nearest candidates. To
pass from a Q_17 realization to algebraic numbers, encode distinct nodes,
distinct selected candidates, and failure of every seven-node agreement
by finitely many polynomial inequations, or invert their nonzero minors.
The Q_17 point makes this finite-type Q-locus nonempty; it therefore has
a point over the algebraic closure of Q. All coordinates lie in one
number field. At all sufficiently large completely split primes, clear
denominators and reduce this point. The same incidences, distinctions,
and upper agreement bound survive. Thus the finite example occurs over
arbitrarily large prime fields. No claim is made that all 22 original
nearest candidates lift, or that list size grows with block length.

## Negative unramified case: p=41

There are 260 equations and 240 variables. The generator reports rank
216, but the independent verifier does not need or assert that rank.
Instead it directly checks a saved vector with 178 nonzero entries
annihilates every column of the original Jacobian and has dot product
14 modulo 41 with the correction right side.

Consequently the first correction is inconsistent: there is no lift of
this incidence seed to Z/41^2 with the prescribed reductions, even with
all nodes, candidates, and received symbols free to move. The same
witness excludes corrections after any unramified residue-field
extension. It does not exclude ramified lifts, a different seed, or a
characteristic-zero construction with different incidences.

## Reproduction and next direction

    python3 research/dickson_domain_deformation/verify.py

The generator `pilot.py` requires NumPy; the verifier uses only stdlib.
Both ran under the 384 MiB watchdog. Reports are stored alongside them.
Do not expand this into a prime or ramification census without a new
symbolic reason. The needed result remains a scalable, fixed-gap source
list over sufficiently large prime fields; an isolated lift is not an
exponent-tightness result.

## Subsequent exact-profile strengthening

EXACT_PROFILE.md and verify_extra_supports.py now certify that one can
choose the p17 characteristic-zero deformation with EXACTLY eight
candidates above four agreements, each at six agreements. All208 unwanted
five-supports can be broken on the same smooth branch; all4368 possible
five-supports are independently replayed. The earlier claim of at least
eight nearest candidates is therefore strengthened for a suitable
choice of deformation, not for every possible lift.
