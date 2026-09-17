# Focused primary-source audit: interval moment lists

Date: 2026-09-17. Independent priority assessment; no main-paper edits.

## Finding

The almost-quadratic reciprocal-gap list exponent is an immediate coding-theoretic adaptation of an old integer moment pigeonhole proof. It remains a valid, useful quantitative obstruction to the proposed uniform bound. It should not be presented as a newly discovered counting mechanism, or used by itself to justify a strong technical-novelty claim.

The closest checked primary source is Borwein, Erdelyi, and Kos, *Littlewood-type problems on [0,1]*, Theorem 2.7 and its proof (PDF pages 7 and 20):
https://people.tamu.edu/~terdelyi/papers-online/PLMS.pdf

That theorem constructs a nonzero {-1,0,1}-coefficient polynomial of degree at most n vanishing at 1 to order at least c sqrt(n/log(n+1)). Its proof counts the integer derivative vectors at 1 of 0/1 polynomials and applies pigeonhole. Keeping a whole fiber, rather than two polynomials, and fixing the number of nonzero coefficients gives our needed exponential equal-moment bank. The source calls this result well known and references Bloch--Polya (1932). I have not checked that original paper directly; the exact earliest attribution needs a separate bibliographic check.

The old theorem's statement alone only provides two equal-moment subsets. The implication for our asymptotic list theorem comes from its proof with the elementary modifications below. No inspected source states our exact prime-field/Elias-radius corollary verbatim. Absence from this bounded search is not evidence of priority.

## Independent derivation of the coding consequence

Fix rational rho in (0,1), n with k=rho n integral, and
s=floor(c sqrt(n/log_2 n)), t=k+s. For each t-subset A of {0,...,n-1}, form the binary polynomial B_A(Z)=sum_{a in A} Z^a. Its normalized derivative B_A^(j)(1)/j! is the integer binomial moment sum_{a in A} binom(a,j).

A deliberately crude bound suffices: for each j=1,...,s the moment has at most n^(j+1)+1 values. Consequently the number of signatures is at most

    exp_2((s^2/2+O(s)) log_2 n)
      = exp_2((c^2/2+o(1)) n).

There are binom(n,t)=exp_2((H_2(rho)+o(1))n) subsets. Choose c^2<2H_2(rho). A fiber therefore has exp_2(Omega_rho(n)) members. This is exactly the large-fiber, fixed-weight adaptation of the classical pigeonhole argument; no new number-theoretic input is required.

For any prime p>n, equal binomial moments give equal power sums, then equal first s elementary symmetric functions by Newton identities. The locators F_A(X)=prod_{a in A}(X-a) share their degree >=k part W. Thus P_A=W-F_A has degree <k and agrees with W at exactly the t coordinates of A. Distinct subsets give distinct codewords. This produces the exponential list in the interval RS code.

Take eta=s/n and choose log_2 p=C sqrt(n log_2 n)+O(1), with cC>H_2(rho); Bertrand's postulate provides such primes. Then p>n and

    H_p(1-rho-eta)
       <= 1-rho-eta + H_2(1-rho-eta)/log_2 p
       < 1-rho

for large n. The radius is strictly below the characteristic-based Elias radius. Finally eta^(-2)=Theta(n log n) and log(1/eta)=Theta(log n), so

    log L = Omega_rho(eta^(-2)/log(1/eta)).

This proves the manuscript's asymptotic exponent, the huge-prime regime, and the exclusion of every uniform exp(O_rho(1/eta)) bound from the classical proof plus the standard locator bridge. The manuscript's sharper binomial-range count improves the constant c^2/2 here to c^2/4 and supplies exact finite certificates; that is a quantitative refinement, not a different asymptotic exponent.

## Focused coding-theory comparisons

* Rudra thesis, Chapter 6, Section 6.4.3, Theorem 6.10 (printed page 106): p=aL+1, t=bL, code dimension (b-1)L+1, list at least binom(a,b) at agreement t. The multiplicative-coset construction is prime-field and uses the locator/moment bridge explicitly. At fixed rate its agreement surplus is (L-1)/(aL), and log of this supplied bank is O(a)=O(1/eta). It does not itself give the interval exponent. Primary: https://cse.buffalo.edu/faculty/atri/papers/coding/thesis-chaps/chap6.pdf

* Ben-Sasson, Kopparty, and Radhakrishnan, *Subspace Polynomials and List Decoding of Reed--Solomon Codes*: the inspected constant-rate Corollary 2.3 is over binary extension fields and uses subspaces. Its discussion also gives the general counting bound binom(N,T)/N^(T-K) for the relevant full-length setting. The general alphabet-q pigeonhole analogue binom(n,t)/q^(t-k) loses its exponential lower bound once eta log_2 q exceeds H_2(t/n), whereas the integer-domain count above is independent of p. Primary: https://www.math.utoronto.ca/swastik/rsld.pdf

* Guruswami--Rudra, *Limits to List Decoding Reed--Solomon Codes*: inspected relevant full-field/random-subset constructions; no interval theorem identified in that inspection. This is not a claim of exhaustive non-implication from every result in the paper. Primary: https://www.cs.cmu.edu/~venkatg/pubs/papers/rs-limits.pdf

* Gandikota--Ghazi--Grigorescu, *NP-Hardness of Reed--Solomon Decoding, and Prouhet--Tarry--Escott*: inspected abstract, introduction, main hardness statement and moment formulation. It establishes the old coding/moment connection in the hardness setting, not our list-size statement. Primary: https://arxiv.org/abs/1611.03069

Justesen--Hoholdt (MDS list bounds) was encountered through primary-source citations but its original paper was not directly checked. Roth--Ruckenstein was screened at the publisher abstract only. Neither is counted as a fully audited source. The search stops here because the exact classical counting mechanism has already been located; a broad keyword crawl would not strengthen the principal finding.

## Recommended interpretation

Credit the moment bank as a quantitative version of classical integer moment pigeonholing, with the older proof cited alongside the existing RS/moment references. State the new application to the precise proposed bound and the finite binomial-range refinements separately. Do not claim that an old theorem explicitly states the full coding corollary; do not imply that no older work does so.

This finding lowers the technical-novelty weight assigned to the interval result in CORE_RESULTS_NOVELTY_STRENGTH_AUDIT.md. The exact prime-field affine distance profile and the true ordinary-common-agreement quadratic-extension construction need separate novelty assessments and are not subsumed by this counting observation. For a strong venue case, those structural results should carry the argument rather than treating the interval exponent as an independent new technique.
