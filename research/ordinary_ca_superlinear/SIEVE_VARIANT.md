Superseded by the stronger quadratic proof in PROOF.md. This earlier
argument remains valid but is no longer needed in the manuscript.

# Superlinear ordinary-CA failures in quadratic extensions

September 17, 2026. Pure coding theory. No novelty claim. This deduction
uses the previously verified nearest-list orbit argument and boundary
padding, and a standard sieve input for its quantitative exponent.
It is NOT a result over prime ambient fields or at a fixed exact gap.

## Coding statement

For every 0<epsilon<1/8, there are unbounded lengths n and primes p with
p=(12/13)n+5, and RS codes over F_(p^2), of exact rate3/13, such that a
received affine line has Omega_epsilon(n^(5/4-epsilon)) nearby labels
at an agreement threshold M, but NO ordinary correlated agreement of
size M. The capacity gap M/n-3/13 is greater than3/26. In particular it
stays uniformly positive. The radius is strictly below the
characteristic-p Elias radius for all sufficiently large members.

The actual maximum M is not computed or asserted to be a fixed fraction
of n. This statement rules out a linear ordinary-CA bound uniform for
gaps bounded below at this rate. It does not address a hypothetical
bound with arbitrary constants chosen separately at each exact gap,
and it makes no first-order-regime or better.codes claim.

## 1. Rough shifted primes (standard sieve input)

Put theta=1/4-epsilon. There are infinitely many primes p=41 mod48 such
that every odd prime divisor of (p-1)/4 is at least p^theta.
Here is the reduction to the standard lower linear sieve, including the
fixed progression so that no extra prime-distribution assumption is hidden.

For a large x sift the integers m=(p-1)/8 with x/2<p<=x and p=41 mod48.
Such m are5 mod6. For squarefree d coprime to6, the condition d|m is one
reduced residue class for p modulo48d. Thus the sequence has size
X=(Li(x)-Li(x/2))/16 and local density g(d)=1/phi(d). Set g(2)=g(3)=0.
Bombieri--Vinogradov gives total absolute remainders O_A(x/log^A x)
through level D=x^(1/2-epsilon); the fixed factor48 is harmless, and
subtraction of the counts at x and x/2 handles the dyadic interval.

Sift to z=x^(1/4-epsilon). The sieve parameter
s=log(D)/log(z)=(1/2-epsilon)/(1/4-epsilon) lies strictly between2 and3.
The lower linear sieve has f(s)=2 exp(gamma) log(s-1)/s>0, and its
local product is asymptotic to a positive constant divided by log z.
It follows that there are Omega_epsilon(x/log^2 x) such primes with
no prime divisor below z in m. Since p<=x, this implies the assertion.

This is an application of standard theorems, not a new sieve result.
Primary sources: D.R. Heath-Brown, *Lectures on sieves*, arXiv:math/0209360,
Section5, Example3, pp.36--37;
and T. Tao, *254A, Supplement5: The linear sieve and Chen's theorem*,
Theorem2, equation(11), and the Bombieri--Vinogradov application in Section2.

https://arxiv.org/pdf/math/0209360
https://terrytao.wordpress.com/2015/01/29/254a-supplement-5-the-linear-sieve-and-chens-theorem-optional/

## 2. A quantitatively large true nearest list

Set k=(p-1)/4, N=4k, and use W(X)=(1+X^(2k))/2-X^k on F_p^*.
The Dickson bank guarantees maximum degree-<k agreement M>=3k/2.
Also M<=2k, by the degree of W-P. The word is invariant under
H=mu_k acting by multiplication on the domain.

Every orbit of a nearest polynomial therefore consists of nearest
polynomials. Its size r divides k. Since p=41 mod48, v_2(k)=1 and
k=1 mod3. The roughness assertion implies either r=1 or2, or r>=p^theta.
The small cases cannot be nearest: they force P=a+b X^(k/2) (including
b=0), which has at most k agreements with W. To see this, pass to
Y=X^(k/2) on mu_8; each fiber has k/2 points, and no affine polynomial
agrees at three points with (1+Y^4)/2-Y^2 when p>17.

The last finite fact has an exact integral certificate in
../dickson_fixed_gap/verify_two_orbit.py and two_orbit_verification.json:
the56 triple determinants in Z[zeta_8] are all nonzero, and their norms
have prime divisors only2,3,5,7,17. Thus reduction at p>17 preserves
nonvanishing. It also holds for affine polynomials over extension fields.

Consequently the true nearest list has at least p^theta members.
Select L=floor(p^theta) of them; for sufficiently large p, L<=k.
Maximum agreement stays M over F_(p^2), since any degree-<k polynomial
matching at least k base-field coordinates and values has coefficients
in F_p by interpolation.

## 3. Boundary padding and exact parameters

Choose an agreement anchor incident to ell>=ML/N selected candidates.
On the remaining N-1 coordinates divide both candidates and word minus
the anchor value by X-anchor. The quotients have degree<=k-2 and exactly
M-1 old agreements. No degree<=k-2 polynomial over F_(p^2) has M old
agreements: restoring the anchor would contradict the old maximum M.

Let q=(k-10)/3, a positive integer for k>10. Set Q=p^2. From the Q-N
unused field points choose q with largest numbers s_x of distinct
quotient evaluations. Pairwise polynomial root counting and
Cauchy--Schwarz give average diversity at least

    mu=ell*(Q-N)/(Q-N+(ell-1)*(k-2)).

Since Q>=2NL and ell<=L, we have mu>=ell/2. Independent uniform
translations of the chosen value sets give an expected union of at least
Q[1-(1-mu/Q)^q]. Using q<=N and Q>=2NL yields at least q*ell/4, hence
at least q*M*L/(4N) distinct labels for a suitable choice of translations.
This is the already proved boundary compiler, applied to the extension
field as the ambient finite field; no prime-only step is used.

Put direction zero on old coordinates and one on the q new ones. Every
counted label has at least M agreements. Suppose a correlated witness
pair F,G of degree<=k-2 agreed jointly on M coordinates. If G=0, its
joint agreements are confined to the old domain, where at most M-1
are possible. If G!=0, there are at most k-2 old zeros and at most q
new agreements. Since q<=M-k+1, the total is at most M-1. Contradiction.
This excludes ordinary/subset CA, not only full-support MCA.

The resulting dimension and length are

    K=k-1, n=N-1+q=13(k-1)/3, K/n=3/13.

The agreement gap satisfies

    (M-K)/n >= (k/2+1)/n >3/26.

For k>=20, q>=k/6. Therefore

    J >= q*M*L/(4N) >= k*L/64 >= 3*n*L/832 >= n*L/300.

Since p=(12/13)n+5 and L=floor(p^theta), this is the claimed exponent.
The characteristic guard p>K-1 is immediate. Finally
H_p(1-M/n)<=1-M/n+1/log_2 p<1-K/n for large p, proving strict Elias.

## Weaker version without quantitative sieve estimates

The existing Dirichlet/CRT proof in UNBOUNDED_BOUNDARY_LISTS.md already
suffices for J/n unbounded, at the same exact rate and positive gap lower
bound. For any R>=3 choose arbitrarily large p=9 mod16 and p=-1 modulo
all odd primes <=R, then select R+1 nearest candidates and apply Step3.
In particular the qualitative conclusion does not depend on an exponent
being extracted correctly from the sieve input.
