# Hermite control of quadratic and cubic derivative identities

The audited result is integrated as Appendix R of the full-page paper.

For actual degree-D polynomial solutions of one common differential equation with derivative degree at most three, bounded value/challenge degree, and arbitrary coefficient degree in X, the number of bad full-support labels is O(n) under the signed margin

    A-D >= eta*n,
    A-u >= sqrt(D*s/2) + epsilon*n.

Here u counts coordinates where the entire received-line specialization is the zero polynomial in derivative and challenge; s counts persistent repeated-derivative-root coordinates. At fixed positive degree rate, constants depend on the margins and equation degrees. If u=0, the sufficient threshold is A>=sqrt(D*n/2)+epsilon*n. The characteristic is zero or exceeds D, three, and the bounded auxiliary interpolation Y-degree.

The proof combines classical Hermite interpolation with an explicit specialization-safe polynomial-root lemma and a full-support incidence count. Quadratic and cubic persistent repeated roots prescribe a unique rational derivative. No claim is made that every first-order interpolant has derivative degree at most three, or that the interpolation threshold itself is new.

Main sources: appendix.tex, root_lemma.tex, cubic_corollary.tex. Independent audits: ROOT_INTERPOLATION.md, ROOT_SPECIALIZATION_AUDIT.md, SPECIALIZATION_INDEPENDENT_AUDIT.md, CUBIC_INDEPENDENT_AUDIT.md. The generic-branch pole bound is an optional sharpening; the manuscript uses the simpler direct coefficient-curve degree bound.

Exact checks include the finite interpolation gate and 18 cubic fixtures over three primes, checking 234 singular pairs including leading-coefficient drops. These checks supplement the proofs; they do not certify a better.codes score. No benchmark improvement or new unconditional prime-field lower bound is claimed.
