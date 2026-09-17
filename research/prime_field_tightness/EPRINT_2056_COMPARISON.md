# Comparison with the current public ePrint 2026/2056

Retrieved September 17, 2026 from
https://eprint.iacr.org/2026/2056.pdf?download=1 after the plain PDF URL
returned403. Title: *Reed–Solomon Codes Beyond Johnson: Efficient Decoding
and Smaller Cryptographic Proofs*, Quang Dao, Scott Duke Kominers, Justin
Thaler. 145 pages, September2026.
SHA256: b67c188ec477b6063caf9c1c06b214c71e358ff09b9517adcdb1db212ea2700a.
Read-only local PDF/text: tmp/eprint-2056/ (ignored, not republished).

This supersedes COAUTHOR_DRAFT_COMPARISON_2026-09-10.md for current
quantitative statements. The full145-page proof and Lean development have
not been independently audited here; the statements and relevant formulas
below were read directly.

## Current bounds and material differences

* Theorem1.1/page6: first-order lists O_rho(n/eta1^2) and full-agreement-set
  MCA exceptions O_rho(n^2/eta1^4), at agreement a1(rho)+eta1. These improve
  the September10 draft's eta1^-3 and eta1^-5 powers.
* Theorem5.7/Eq57/page47: the displayed list budget is
  4D*lambda_agr*Bjet*Bpartial+2Bjet*Bpartial+Bjet, with the stronger
  finite-length scale O_rho(n/(eta1+1/n)^2).
* Theorem5.8/Eq58/page48: MCA scale O_rho(n^2/(eta1+1/n)^4). The ordinary
  tail's n*(eta1+1/n)^-5 term is absorbed using n*(eta1+1/n)>=1.
* Proposition5.10/Eqs63--64/pages50--51 allows graded row/column challenge
  budgets, beyond the uniform challenge count used in our legacy cost
  converse. Its truncated graded test need not be monotone in height.
* The first-order counting characteristic guard remains
  char0 or p>max(k-1,Bpartial). The first-order decoder only needs p>k-1.
* Theorem1.2/pages6--7 and Theorem6.8/pages63--64: capacity exponent
  d_delta=ceil(exp(1.5/delta)) for delta<0.24 and d_delta=1 otherwise;
  lists C_delta*n^d_delta, MCA exceptions C_delta*n^(d_delta+1), for
  n>=N_delta, with constants and minimum length depending only on delta.
  The current uniform characteristic requirement is only p>k-1, rather
  than the older stronger p>n comparison. Bounded-degree cases below the
  jet-degree guard are handled separately using Johnson.
* Theorem5.12/page53: Johnson MCA O_rho(n/eta0^3), unchanged from our
  recovered-draft comparison. Section10.4/page102 expressly leaves both
  improvement of this gap dependence and reduction of the first-order
  quadratic n dependence open.
* Page47 expressly acknowledges the high-rate refinement above
  8-3sqrt6 from retaining total jet degree, and further improvement from
  weighted support restrictions. Our restored high-rate note audits this
  phenomenon; it is not a newly discovered improvement absent from the
  current paper's discussion or finite certificate tools.

## What remains valid, and what must not be claimed

The quarter-rate support-threshold theorem and its necessary support
parameters remain useful method statements within their declared rank,
source-space, and characteristic hypotheses. The cubic/fifth-power budget
converse in Section7 of our note applies ONLY to the explicitly displayed
older reconstruction formulas and uniform challenge count. It does NOT
prove optimality of the public ePrint's quadratic/fourth-power gap bounds.
Likewise its legacy rounded-threshold budget costs n^4 and n^7 are not
lower bounds for the current finite budgets, whose upper scales there
are n^3 and n^6. There is no contradiction: the counting formulas changed.

No intrinsic lower bound matching the current first-order n versus n^2
powers is established by this project. The growing Dickson bank lies
below the first-order curve; the new family-specific bound shows that
word/subbank optimization on the same full domain cannot bridge it.
Large gap-dependent constants in a linear-n lower bound still do not
force an exponent of n growing as a fixed capacity gap decreases.

## Better.codes scope in the current paper

Section10.5/page102 confirms n=2^18, k=2^17, p=2130706433, q=p^6 and
eight-row interleaving. It distinguishes the lower-track certified safe
radius and128-query score from the independent2^-128 reduction-error
requirement. Separate supports may bound list and MCA contributions.
The current paper's implemented proof-size reductions and its discussion
of prize submissions do not establish any new benchmark gain from our
counterexample project.
