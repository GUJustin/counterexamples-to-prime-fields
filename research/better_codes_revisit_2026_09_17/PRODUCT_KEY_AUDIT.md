# Exact product-key concentration does not supply the missing factor four

For the closest failed packet family, let U range over136-element subsets
of mu_256 excluding1. Its signature consists of six leading nonmonic
coefficients and its root product. Newton identities identify the first
six coefficients with the first six power sums, since p>6.

The generic denominator is256p^6. One possible improvement would first
choose the most populated product class, then pigeonhole its six field
coefficients. We computed every product-class size exactly. The maximum
exceeds the mean by a relative fraction less than10^-35, and the resulting
integer family guarantee remains exactly68579341025511059. The required
count is274980728111395088. Thus even the optimal product class gives no
increase in this guaranteed count.

This is independently verified in two ways:

1. Subset dynamic programming tracks cardinality and sum of exponents
   modulo256 for labels1,...,255.
2. A roots-of-unity filter uses integer Ramanujan sums. For a character
   of order d dividing256, the generating polynomial is

       (1-(-z)^d)^(256/d)/(1+z).

   Its coefficient at z^136 is
   (-1)^(136+floor(136/d))*binomial(256/d-1,floor(136/d)).
   The count at product exponent s is1/256 times the sum of these
   coefficients multiplied by c_d(s), over divisors d of256. Here
   c_1(s)=1 and, for d>1 a power of two, c_d(s) equals d/2 if d divides s,
   -d/2 if d/2 divides s but d does not, and zero otherwise.

The two methods agree for all256 classes. The watchdog records a completed
1.11-second run and peak sampled RSS under20MiB.

This excludes only improvement by optimizing the product key and using
the generic p^6 bound afterward. Joint concentration involving the six
leading coefficients remains open. In particular, the calculation is
not an upper bound on the largest full-signature fiber.

Quotienting by rotations does not automatically repair the deficit:
for the unrestricted domain, rotation acts on both subsets and weighted
signatures, so orbit factors cancel in elementary pigeonholing. The
distinguished omitted label1 further prevents treating the anchored
subset family as invariant under all rotations. A valid symmetry gain
would require an additional count or stabilizer argument.
