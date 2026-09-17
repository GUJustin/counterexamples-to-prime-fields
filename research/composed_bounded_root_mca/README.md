# Common-composition closure of the bounded-root MCA bound

`PROOF.md` proves a proposed extension of the existing bounded-root
barrier: P=Q(phi(X)) still has only O(n) bad full-support labels at a
fixed positive rate and gap, uniformly in the degree of the one common
polynomial phi, if Q has boundedly many distinct roots. It retains the
original sufficiently-large-characteristic hypothesis. The received
words need not be constant on fibers. Candidate-dependent phi is not
covered.

The proof uses weighted root counting when n/deg(phi) is large, and a
bounded-dimensional linear-space argument when it is small. In particular
the affine-graph bound is n, not n/deg(phi); full-support badness always
refers to the original degree-D code.

This is an auxiliary research note, not yet part of the ePrint draft.
It is self-reviewed and has no independent-review or priority claim.
It does not supply the desired quadratic lower bound or a new score.

The standard-library checker `verify.py` exhausts 43,545 polynomial-label
pairs in three small spaces with non-fiber-invariant words, checks their
determining-tuple incidences, and verifies five exact families with
7, 13, 25, 49, and 97 bad labels. Composition degrees are 1,2,4,8,16.
These checks supplement the proof and do not instantiate its enormous
asymptotic Wronskian thresholds. Run sequentially under the 384 MiB guard.
