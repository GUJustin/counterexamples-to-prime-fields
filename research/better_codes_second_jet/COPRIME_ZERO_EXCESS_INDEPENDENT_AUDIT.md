# Independent audit of coprime zero-excess rigidity

Verdict: **PASS** for COPRIME_ZERO_CONTACT_EXCESS.md, including the challenge-only exception and the degree<=w endpoint. The cyclic-window proof was independently obtained before reading that note.

For any permutation, the n cyclic w-window sums have average (w/n)sum u_i. If none is above this average then all equal it. Adjacent differences give u_(i+w)=u_i. Coprimality gcd(n,w)=1 makes this one cycle and forces the original vector constant. Hence every ordering of a nonconstant vector has at least one positive window. Averaging over uniform permutations yields

    #positive w-subsets >=ceil(binom(n,w)/n).

This proof uses labeled entries, so repetitions among their numerical values cause no counting issue. The window always contains w distinct indices. Strict positivity and equality are treated correctly; no integrality or probabilistic approximation is used.

The contact-subset upper bound is floor(V/(w−1)), and can even be replaced by deg_R(F). Under binom(n,w)>n floor(V/(w−1)), zero charge therefore forces actual contacts to be a common integer a and V=aw. For 1<=a<w−1, n>w+a and characteristic zero or p>a, the independently audited uniform-contact theorem gives F=c(Y−P)^a. For affine received data the unique degree<=w interpolant is P0+ZP1. If F is a positive-weight irreducible polynomial over the original field, c is a nonzero scalar and a=1. Weight-zero factors depend only on Z and must be retained as the separate exception.

At n262144,w131071, gcd(n,w)=1. The primary strict weight bound V<21390450 gives a<=163 at equality, so all small-contact and characteristic hypotheses hold. The binomial inequality has enormous slack. Thus every positive-weight zero-charge primary factor is a received-line graph factor; it cannot be treated as a new regular slope-dependent carrier.

## Additional exact exchange bound for small positive charge

This is a separate strengthening, not needed for the zero-charge theorem. Let integer contacts u_i be given, let V be an integer, set

    Mbar=(w/n)sum_i u_i,  e=V−Mbar,

and suppose at most B w-subsets have sum>V. If at least one does, then

    e >= [w(n−w)−B+1−n]/n,                       (1)

provided the bracket is nonnegative.

To prove this, sort the u_i and take a top-w subset T with sum S>V. Put Delta=S−V>=1. It has w(n−w) distinct one-exchange neighbors; at most B−1 of them can also exceed V. For every other exchange i in T, j outside T,

    u_i−u_j >=Delta.

All cross differences are nonnegative by the choice of T. Summing them gives the identity

    n(S−Mbar)=sum_(i in T,j outside T)(u_i−u_j)
             >=[w(n−w)−B+1]Delta.

Subtracting Delta and using Delta>=1 proves (1). This is an elementary exchange argument, not an invocation of a subset-sum extremal conjecture.

For the pinned factor weight cap, B=floor(V/(w−1))<=163. Formula (1) therefore gives

    e >=17179606877/262144

whenever ANY exceptional subset exists. Thus a factor of charge below approximately65535 has no exceptional w-subsets at all. This can be useful input for a future near-equality classification, but it does not currently bound the number or normal cost of its first-tail components.
