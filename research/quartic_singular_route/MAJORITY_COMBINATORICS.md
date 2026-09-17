# Independent audit of the Dickson majority combinatorics

Let (xi_i,eta_i), i=1,...,L, be independent pairs of independent uniform signs. Put

    S=sum_i(xi_i+eta_i),
    sigma=+1 if S>=0, and sigma=−1 if S<0.

Candidate i succeeds when xi_i=eta_i=sigma. The deterministic positive tie rule is sufficient; no random tie breaking or parameter sampling is needed.

## Exact common success probability

Let N+ and N− count the pairs (+1,+1) and (−1,−1). Then

    N+−N−=S/2,
    successes=max(N+,N−)=(N++N−)/2+|S|/4.

A tie gives N+=N−, so either sign achieves exactly the same number of successes. Since E(N++N−)=L/2,

    E(successes)=L/4+E|S|/4.

The full joint law AND the chosen tie rule are invariant under permutations of the L pair indices. Therefore every candidate has the same success probability, including at ties, and

    p_L=1/4+E|S|/(4L).                           (1)

For S the sum of 2L independent signs,

    E|S|=2L*binom(2L,L)/4^L.                     (2)

For completeness, binomial symmetry gives

    E|S|=(4/4^L) sum_{j=L+1}^{2L}(j−L)binom(2L,j).

The identity

    (j−L)binom(2L,j)
      =L[binom(2L−1,j−1)−binom(2L−1,j)]

telescopes the sum to L*binom(2L−1,L)=(L/2)binom(2L,L), proving (2). Combining (1),(2),

    p_L=1/4+binom(2L,L)/(2*4^L).                 (3)

Thus index symmetry is exact; an average over candidates is not being substituted for an individual-candidate guarantee.

## Explicit lower constant

Write b_L=binom(2L,L)/4^L. Then b_1=1/2 and

    b_(L+1)/b_L=(2L+1)/(2L+2) >= sqrt(L/(L+1)),

because (2L+1)^2>=4L(L+1). Induction gives b_L>=1/(2sqrt L), so

    p_L >= 1/4+1/(4sqrt L).                      (4)

If half the domain is a nonsquare block on which each candidate has agreement fraction 1/2, while the square half realizes this sign experiment, the total ideal agreement is

    1/4+p_L/2 = 3/8+b_L/4 >= 3/8+1/(8sqrt L).    (5)

The exact asymptotic gain is 1/(4sqrt(pi L)), but (5) needs no asymptotic estimate. A finite-field realization whose TOTAL agreement error is at most 1/(16sqrt L) retains agreement at least 3/8+1/(16sqrt L). Upper agent's separate note must establish that error uniformly for each chosen candidate; independent signs alone do not prove the finite-field construction.

## Descent from square roots and exceptional coordinates

For p=1 modulo 8 and distinct nonzero parameters a_i modulo sign, use

    xi_i(s)=chi(s+a_i), eta_i(s)=chi(s−a_i).

For s away from 0 and the 2L endpoints ±a_i these are signs. Under s→−s, chi(−1)=1 makes xi_i and eta_i swap. Consequently S, sigma, and each candidate-success event are invariant. The majority word is therefore well-defined at the square coordinate x=s², not dependent on its choice of square root.

At the finitely many endpoints a character is zero, so the independent-sign formula must NOT be applied literally. One may define the word arbitrarily there and debit those coordinates in the finite-field error. Similarly, distribution estimates over all s must explicitly remove s=0. These are realization errors, not changes to the exact formula (3).

## Audit conclusion

The combinatorial ingredient passes, with the exact individual success probability (3), fixed positive tie rule, and explicit constant (5). It supports the proposed epsilon^(-2) lower scale once the separate character-pattern realization is proved. No claim about arbitrary Reed--Solomon lists or prime-field line amplification follows from this calculation alone.

## Fourier reduction of the finite-field error (conditional only on the standard character-sum bound)

Let F_i be the Boolean success indicator on the 2L signs, and write its real multilinear Fourier expansion. Parseval and Cauchy give

    sum_{I nonempty}|hat F_i(I)|
      <= sqrt((4^L−1)(p_L−p_L²)) <= 2^(L−1).

For distinct shifts ±a_i, the usual squarefree quadratic-character estimate for a product of |I| distinct linear factors is (|I|−1)sqrt p. Applying it termwise gives complete-sum error at most

    E_L=2^(L−1)(2L−1)sqrt p.

There is no exponential endpoint debit: setting some Fourier-input coordinates equal to zero averages F_i over all completions of those signs, so the multilinear extension remains in [0,1]. Removing the at most 2L zero-character endpoints and s=0 therefore costs at most 2L+1. The number of good square-coordinate successes for each candidate is at least

    [p p_L−E_L−(2L+1)]/2.

Consequently its total agreement fraction is at least

    3/8+b_L/4 − [E_L+2L+1]/[2(p−1)].

This calculation checks the exact conversion of the character estimate to individual-candidate agreement; the primary attribution and hypothesis statement for the character estimate belong in the construction note.
