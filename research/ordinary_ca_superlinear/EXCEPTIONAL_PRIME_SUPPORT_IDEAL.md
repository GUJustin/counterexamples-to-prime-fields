# Exceptional split primes for a short cyclic nearest source

## The existing Dickson ODE cannot generate a large-characteristic short source

For fixed r consider the archived ODE

`4X(2G²−1−X^(2r))G′+G(4G²−1−3X^(2r))=0`.

Any degree-below-r candidate P for the shifted word gives a monic degree-r polynomial G=X^r+P. The coefficient of X^(3r) in the ODE is exactly4r+1 over the integers. Therefore any such solution in characteristic p requires p dividing4r+1. If the full domain μ_(4r) is in F_p, then p≡1 modulo4r and p≥4r+1, forcing **p=4r+1**. There is no exceptional-prime sequence p/r→infinity inside this fixed differential equation.

Furthermore every nonzero member of the classified Dickson bank at p=4r+1 has a nonzero X coefficient: its binomial formula has upper index2r+1<p and nonzero parameter. Hence its stabilizer under X↦ζX, ζ∈μ_r, is trivial. The known bank itself always has full orbit r=(p−1)/4; it cannot supply the short orbit required by prime-field line amplification. A nearest polynomial with a larger stabilizer, if one exists, must lie outside the classified bank. This statement does not classify all nearest polynomials of the cyclic received word.

## A denominator-free criterion for every support

Let ζ be primitive of order4r, and let S be an M-element subset of μ_(4r), where r<M≤2r. Write

`A_S(X)=∏_{a∈S}(X−a)`, `k=2r−M`, and `∏_{a∈S}(1−at)^(-1)=Σ h_j(S)t^j`.

There exists a degree-below-r polynomial P agreeing with

`W_r(X)=(1+X^(2r))/2−X^r`

on S if and only if

`h_(k+1)(S)=…=h_(r−1)(S)=0`, and `h_r(S)=2`.

This holds in characteristic zero and every odd characteristic in which the selected roots remain distinct. To prove it, make 2(W_r−P) monic of degree2r and divide by A_S. Its reciprocal has first coefficients1,0,…,0,−2 through degree r. The reciprocal of the monic quotient has degree k and is therefore the degree-k truncation of Σh_jt^j. Successive vanishing of the product coefficients from k+1 through r−1 is equivalent to the first equations above; the degree-r product coefficient is then −h_r. Conversely those identities construct a monic quotient with exactly the required top r+1 coefficients; its lower coefficients define P. There are no Vandermonde denominators or unspecified interpolation choices in this test.

Define the cyclotomic ideal

`I_S=(h_(k+1),…,h_(r−1),h_r−2) ⊂ Z[ζ_(4r)]`.

A good split prime admits this support precisely when some prime ideal over p contains I_S. A large prime factor of ONE determinant or ONE h-value is insufficient: the same prime ideal must divide every generator. This simultaneous divisibility is the missing arithmetic input in a primitive-prime approach.

If a support is not already a characteristic-zero solution, one generator α is nonzero. At each complex embedding,

`|α|≤binom(3r−1,r)+2`.

Thus every exceptional rational prime for that support is bounded above by

`(binom(3r−1,r)+2)^(φ(4r)) = exp(O(r²))`.

This is only an upper bound. It neither forces a prime much larger than r nor proves an O(r) upper bound. For prime r the exponent is2(r−1). Norm-factor growth alone does not solve the simultaneous ideal-divisibility requirement.

## Complete r=3 pilot: no larger prime, with no prime cutoff

For r=3 and target agreement5, k=1 and the only equations are h₂=0,h₃=2 in Z[ζ12], whose defining polynomial is X⁴−X²+1. There are exactly792 five-subsets. The script `exceptional_r3_supports.py` computes both algebraic integer norms for every subset and factors their integer gcd. Every possible prime p≡1 modulo12 is retained, and a polynomial gcd modulo p tests whether BOTH equations vanish at the same primitive root.

Result: there are no characteristic-zero supports, and the only exceptional split prime is13. Twelve support/embedding pairs realize it. Thus **for every prime p≡1 modulo12 other than13, no degree-at-most-two polynomial agrees with W₃ at five points of μ12**. This is a complete all-prime finite-r classification, not a bounded prime scan, and includes candidates outside the Dickson ODE family.

The exact computation uses degree-four integer resultants and finishes in about0.007 seconds. Its JSON records the exceptional supports, their two norms (both13), and the common linear factors selecting the primitive-root embeddings. Independent verification is appropriate before manuscript use.

## Remaining route

The new support criterion turns a vague search for large exceptional characteristics into a precise problem: exhibit supports S_r with a common prime-ideal divisor of I_(S_r), split rational characteristic p_r, p_r/r→infinity, and M_r≥ceil(3r/2). When r is prime and P is nonconstant, its μ_r orbit automatically has size r; after replacing P by a nearest polynomial, the same orbit conclusion holds because a constant has at most r matches when the four received buckets are distinct. This would supply the desired short-domain nearest sources.

Neither the classified ODE nor the complete r3 pilot supplies such a sequence. An unbounded prime scan would not establish it. The useful next theoretical object is the support ideal, with its simultaneous divisibility and split-prime conditions kept intact.

## Complete r=5 pilot

For r=5,M=8, the equations are h₃=h₄=0 and h₅=2 in Z[ζ20]. The safe support symmetry group is

`j ↦ a*j+4b (mod20), a∈(Z/20)×, b∈Z/5`.

Galois conjugation preserves simultaneous vanishing, while the shift by4b multiplies h_j by a root-of-unity factor and fixes h₅. Arbitrary one-step rotations are not used. The125,970 eight-subsets form3326 such orbits. Their norm gcds suggest possible split primes41,61,101,181,401; polynomial gcds show that none is a common prime-ideal divisor of all three equations. No characteristic-zero support exists either. Therefore **no prime p≡1 modulo20 admits eight agreements with W₅ by a polynomial of degree below5**. Files `exceptional_r5_supports.py/json/resources.json` provide the complete orbit coverage, all exact norms, and all-prime result. Runtime is about0.195seconds.

## Prime-order characteristic-zero obstruction (new theoretical deduction)

**Theorem.** If r>5 is prime, every polynomial of degree below r over characteristic zero agrees with W_r on μ_(4r) at at most r+2 coordinates.

Suppose M≥r+3. The polynomial `F=X^(2r)−2X^r+1−2P` is monic and is divisible by the monic support locator A_S of degree M. Its monic quotient has degree k=2r−M<r. The coefficients of that quotient are determined successively by the coefficients above degree r in F, which are zero apart from the leading1. Thus they are cyclotomic integers, explicitly the complete homogeneous coefficients h₀,…,h_k. Consequently F=A_S Q is integral and P is integral after inverting2. This argument does not use Vandermonde denominators, which would fail at the ramified prime r.

Reduce at a prime of the cyclotomic ring above r. All μ_(4r) roots collapse to the four distinct fourth roots of unity, with at most r original roots at any one. If their selected multiplicities are n_c, then the reduced F is divisible by the product of `(X−i^c)^(n_c)`, and sum n_c=M. Its derivative is `−2P′`, of degree at most r−2. If nonzero, it has multiplicity at least n_c−1 at each occupied root, hence at least M−t≥M−4≥r−1 zeros, contradiction. Therefore P′=0. Since deg P<r in characteristic r, the reduced P is constant.

At the four fourth roots the values of W_r are the four distinct elements0,2,i,−i (permuted according to r modulo4); they are distinct for r>5. A constant can match only one bucket. Each bucket contains at most r original support roots, contradicting M>r. This proves the theorem.

In particular, a sequence of prime r cannot provide the proposed characteristic-zero cyclic source with M≥(1+c)r for any fixed c>0. This does NOT bound exceptional split characteristics p≠r, where the domain stays separable. It explains why replacing the target1.5r by4r/3 does not rescue prime-order characteristic-zero sources for large r. Composite orders, including the known r6,M8 bank, are not covered by this prime-order theorem.
