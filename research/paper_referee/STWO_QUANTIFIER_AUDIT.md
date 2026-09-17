# Direct audit of the whitepaper quantifiers

Primary source: https://eprint.iacr.org/2026/532, March 24, 2026 revision,
downloaded again September 17 UTC. PDF hash and page references are in
stwo_source_provenance.json. This is a mathematical source audit; no
protocol execution or operational exploitation is involved.

## Definition and conjectures

- Definition 24, printed page 56 (PDF page 58), quantifies over every
  choice of nearby witnesses at a set of distinct parameter labels.
  Its concurrency conclusion is equality to one polynomial codeword
  curve at more than the specified concurrency number. The manuscript's
  selected-witness definition at curve degree one matches it, including
  the same parameter z and the strict threshold inequalities.
- Conjecture 1, printed page 80 (PDF page 82), fixes the rate, then
  posits constants c1,c2>=1 for every Reed--Solomon code over every
  prime field at radii up to Elias. It imposes no extra restriction
  relating prime size, length, or evaluation domain. The claimed list
  form is c1*2^(c2*H2(rho)/eta). The interval constructions therefore
  directly contradict its uniform assertion.
- Conjecture 2 on that page uses a=ell(theta)*n+o(n), concurrency n,
  with ell as in Conjecture 1. It extends the alphabet to extension
  fields while keeping the domain of definition in the prime field.
  The text does not specify uniformity of the remainder in the prime
  or the gap. Its examples use c1=c2=1 and discard the remainder.

## Match to the proved statements

1. The exponential interval lists refute every fixed pair of constants
   at a fixed rational rate. The every-large-prime corollary is stronger
   than a subsequence of fields. The newly explicit coefficient-growth
   consequence even allows a prefactor polynomial in p.
2. The logarithmic-length line theorem refutes the finite numerical
   threshold for every sufficiently large prime, with a shrinking gap.
   It does not alone resolve a remainder statement asserted separately
   at each fixed gap.
3. Anchored fixed-gap padding gives genuine failure of correlated
   agreement and the selected-witness conclusion, with more than
   C(rho,eta)*n labels and concurrency at most n. For any proposed
   constants, it chooses a positive gap fixed throughout the family,
   and defeats every remainder sublinear along that increasing-length
   family. The field is allowed to grow. This is the precise numerical
   coefficient obstruction, without supplying missing quantifiers on
   behalf of the whitepaper.
4. The generic-domain actual-list separation is a different result:
   its true maximum list is n-k-1 while the selected line has
   binom(n,k+1) nearby labels. Its gap is 1/n. It does not settle the
   actual-list-size conjecture with a remainder controlled only after
   fixing a positive gap.

## Editorial consequence

The body already states the distinctions, but the abstract previously
said both conjectures were contradicted under their published
quantifiers, without exposing the unspecified remainder convention.
Replaced that sentence with the exact proved claims above. This changes
no theorem or counterexample and avoids an abstract stronger than the
careful application section. No complete-protocol soundness conclusion
is inferred from a coding counterexample alone.
