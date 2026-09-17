# Root review: sharp Dickson transition and polynomial alphabet

September 17, 2026.

Reviewed the sharp upper-bound note, deterministic majority lower bound,
independent audit, and `MAJORITY_QUADRATIC_ALPHABET.md` in full.
The complete-bank classification is already in the preceding manuscript
proposition. The new upper bound applies to every received word, but only
counts members of this bank.

The quadratic-alphabet improvement passes independent review. In particular:

* Completing zero character values by independent random signs gives exactly
  the multilinear extension; independent completions at two coordinates
  reproduce the product of the two conditional expectations.
* The one-parameter pair law is exactly
  `(1 - u_1 u_2/p)/4`, independent of the nonzero coordinate. Thus the
  covariance calculation uses its true marginals, without a dimension-dependent
  approximation to the mean.
* For distinct shifts `s,-s,t,-t`, internal pair moments cancel in the
  centered four-sign distribution. Four cross-pair moments, four triple
  moments, and one quadruple moment give the stated entrywise bound.
  The primary BGKS Lemma 17 supplies the explicit character-sum constants.
* The conditional-expectation operator preserves constants and their
  orthogonal complements. Its tensor product therefore has the same
  upper bound on the nonconstant subspace, rather than a bound multiplied
  by the number of candidates. This justifies the dimension-free variance.
* The two exceptional relations `t=s` and `t=-s` are charged explicitly.
  Chebyshev, followed by Markov on the number of unsuccessful candidates,
  avoids a union bound requiring every sampled candidate to succeed.
* The received word must continue to use all `2L` sampled parameters after
  retaining `L` good candidates. The proof does so. Collision avoidance,
  the marginal bias, and removal of endpoints all fit the displayed
  `p >= 2^36 L^2` condition.

The conclusion is existential in the selected parameters. It does not
prove the same polynomial prime-size condition for parameters `1,...,L`.
The evaluation domain still has length `p-1`, and no improved better.codes
score, superlinear prime-field label count, or general DKT tightness follows.

Root reran the 567 exact subset/bucket checks and 15 deterministic majority
fixtures under the resource wrapper. All passed. Only one of those 15
fixtures meets the earlier exponential sufficient prime-size condition;
these finite checks are not numerical certification of the asymptotic
quadratic-alphabet theorem. That theorem rests on the reviewed proof.
