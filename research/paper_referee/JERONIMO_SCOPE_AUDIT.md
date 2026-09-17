# Scope of TR26-169 versus the remaining lower-bound target

Primary source checked September 17, 2026:
https://eccc.weizmann.ac.il/report/2026/169/
PDF: https://eccc.weizmann.ac.il/report/2026/169/download/
Fernando Granha Jeronimo, September 5, 2026, 37 pages.

Theorem 1.1 (page 3) states a list bound n^{C_list(gamma,L)} for
fixed positive additive slack gamma and bounded input-list size L,
uniform over prescribed domains and prime q>=n, once n exceeds a
slack-dependent threshold. Theorem 1.2 (page 4) states at most
n^{C(gamma,ell)} bad parameters for fixed-degree received curves.
Its exact-support MCA definition appears in Section 2.3: a nearby
witness is bad when its full support is not a maximal jointly
explained support. Ordinary correlated-agreement failure implies
badness in this sense.

These are polynomial, not linear, block-length bounds. Section 8.5
(page 32) explicitly disclaims competitive numerical exponents and
small-length certificates. The title's optimality concerns the
capacity radius; it does not supply an exponent-one exception bound.
Our fixed-gap linear lower bounds and shrinking-gap results are
compatible with the stated theorems. A superlinear lower bound at
one exact fixed positive gap, with n=o(p), remains a meaningful target.

This is a quantifier and scope audit, not an independent verification
of the upper-bound proof. No concrete better.codes improvement follows.
