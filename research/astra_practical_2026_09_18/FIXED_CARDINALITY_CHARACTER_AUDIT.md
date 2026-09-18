# Independent audit: fixed-cardinality affine-line products cover E*

The character argument passes. For E=F_(p^5), any b of degree5 over Fp,
and A={b−a:a in Fp*}, every element of E* is a product of exactly
(p−1)/2 distinct elements of A whenever p is an odd prime at least181.
The two-deleted-tag variant needed by the arbitrary-dimension compiler
also passes, with the explicit sufficient threshold191 both near half
cardinality and at the exact-half-code-dimension parameters below.
These are product-surjectivity statements; the coding
compiler and benchmark transfer are separate claims.

This independently checks the first-character-sum/Cauchy proof supplied by
the root agent. It does not rely on a distinct-coordinate cycle-index bound
with omitted character-order exceptions.

## 1. Katz's hypothesis covers every nontrivial character

Katz's Theorem1 applies to an extension E/F of degree d, an element b with
F(b)=E, and any nontrivial complex multiplicative character chi of E*.
It bounds the absolute affine-line sum by(d−1)sqrt(|F|). There is no
requirement that chi restrict nontrivially to F*. The latter restriction
appears only in a later remark permitting the generating-element hypothesis
to be dropped. [Katz, *An Estimate for Character Sums*, JAMS2(1989),
Theorem1, p.197](https://web.math.princeton.edu/~nmk/old/estcharsums.pdf).

Replacing a−b by b−a multiplies the sum by the unit chi(−1). Delete any
e base-field tags and put s=p−e. Since b is outside Fp, every remaining
factor is nonzero. For every nontrivial chi,

    |sum_{a remaining} chi(b−a)| <= B=(d−1)sqrt(p)+e.

This includes quadratic characters and characters of every other possible
order. For the original A, e=1; deleting0 and one additional nonzero tag
gives e=2.

## 2. Exact-cardinality coefficient bound from the first power sum

Let v_1,...,v_s be complex numbers of modulus1 with |sum v_i|<=B, and
let E_r be the coefficient of z^r in product_i(1+z v_i). Assume0<r<s.
For any t>0 and real theta,

    |1+t exp(i theta)v_i|^2
      =(1+t)^2−2t[1−Re(exp(i theta)v_i)].

Applying log(1−u)<=−u and summing gives

    |product_i(1+t exp(i theta)v_i)|
      <=(1+t)^s exp[−t(s−B)/(1+t)^2].

If a factor is zero, the product bound holds directly. Cauchy's coefficient
estimate therefore gives

    |E_r| <=t^(−r)(1+t)^s exp[−t(s−B)/(1+t)^2].

Set rho=r/s and t=r/(s−r). The index r is a mode of Binomial(s,r/s),
so its probability is at least1/(s+1). Equivalently,

    C(s,r) >=t^(−r)(1+t)^s/(s+1).

Since t/(1+t)^2=rho(1−rho), division yields the uniform bound

    |E_r|/C(s,r)
      <=(s+1) exp[−rho(1−rho)(s−B)].                 (1)

The generating product selects each coordinate zero or one times, so it
already counts distinct elements at exactly the required cardinality. No
claim is made that higher power sums obey a nontrivial-character estimate:
chi^j can be trivial when ord(chi) divides j, but no such sum is used.

## 3. Fourier inversion and the exact sufficient inequality

For c in E*, let N_r(c) count the r-subsets of remaining tags whose product
of b−a equals c. Character orthogonality gives

    (p^d−1)N_r(c)
      =C(s,r)+sum_{chi nontrivial} chi(c^−1) E_r(chi).

There are p^d−2 nontrivial characters. Applying(1) to each separately
proves positivity for every c if

    (p^d−2)(p−e+1)
      *exp[−rho(1−rho)(p−2e−(d−1)sqrt(p))] <1.     (2)

This is uniform in the generating b and in the deleted tags. There are
no exceptional multiplicative characters. For fixed d,e and rho bounded
away from0 and1, the exponential suppression beats the polynomial factor
as p grows. Thus degree5 is not special to the character argument.

The resulting lower bound on every product multiplicity is explicitly

    N_r(c) >= C(s,r)/(p^d−1)
       *[1−(p^d−2)(s+1) exp(−rho(1−rho)(s−B))].

## 4. Rigorous half-cardinality threshold181

Take d=5, e=1, and r=(p−1)/2. A slightly stronger sufficient condition
than(2) is

    H(p)=(p−2−4sqrt(p))/4−6 log(p)>0,

because(p^5−2)p<p^6. Its derivative is

    H'(x)=(sqrt(x)−6)(sqrt(x)+4)/(4x)>0    for x>36.

The endpoint is certified using rational bounds only:

    sqrt(181)<134537/10000,
    log(181)<10397/2000,
    H(181)>1053/10000>0.

The logarithm bound follows because the degree40 Taylor partial sum for
exp(10397/2000) already exceeds181. Its terms and comparison are rational.
Therefore every odd prime p>=181 satisfies(2). The verifier also proves
H(179)<−1/5; that only means this sufficient criterion fails there, not
that product surjectivity fails.

## 5. Two deleted tags and the threshold191

For d=5, e=2, put s=p−2 and r=(p−3)/2 or(p−1)/2. Both choices have

    rho(1−rho)=[1−1/(p−2)^2]/4 = c(p).

It suffices that

    H_2(p)=c(p)[p−4−4sqrt(p)]−6 log(p)>0.

At p=191, rational upper bounds sqrt(191)<138203/10000 and
log(191)<52523/10000 give

    H_2(191)>252722171/178605000>0.

For x>=191, c(x)>6/25, c'(x)>0, and x−4−4sqrt(x)>0. Hence

    H_2'(x) > (6/25)(11/13)−6/191
             =10656/62075>0.

Here sqrt(x)>13 was used. This proves the two-deleted-tag criterion
uniformly for every odd prime p>=191 at either nearest half cardinality.

The exact code dimension J=floor(p^5/2) uses different parameters. If
m=(p^5−1)/(p−1), then

    J−1=((p−3)/2)m+(m−1),

so the padded compiler needs r=(p+1)/2 among s=p−2 available tags. Thus

    rho(1−rho)=[1−9/(p−2)^2]/4,

not the nearest-half value above. The same threshold191 still holds:
at p=191 the density product is96*93/189^2=992/3969, and the identical
rational square/log bounds give

    H_exact_half(191)>27933887/19845000>0.

This density product also exceeds6/25 for p>=191 and increases with p,
so the same derivative lower bound proves the full suffix p>=191.

`verify_character_half_onset.py/json` checks the rational square, Taylor,
and endpoint inequalities. No search over fields, subsets, or characters
is needed. This audit proves the product lemma and these explicit onsets;
it does not by itself identify a construction on the prescribed better.codes
domain or certify a practical leaderboard improvement.
