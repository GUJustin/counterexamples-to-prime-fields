# Independent root audit of the subgroup Casorati obstruction

Status: PASS of the analytic theorem in SUBGROUP_CASORATI_OBSTRUCTION.md.

The root independently derived the determinant at infinity using row finite differences followed by column finite differences. The Laurent coefficient of order a in f_i is polynomial in i of degree at most a, with leading coefficient (-1)^a(3/2)_a/a!. Row differences therefore give leading terms (-1)^i(3/2)_i x^(-i). Column differences at step n give the rising-factorial evaluation determinant. Its leading constant is n^(h(h-1)/2) times the product of (3/2)_i i!, which is nonzero for p>2h. Multiplication by the common denominator gives exact numerator degree h(h-1), without needing coprimality with that denominator.

The q-h+1 contiguous windows are distinct, have no denominator poles, and are all singular if the final q high coefficients vanish. The root count contradicts q>=h². This checks the endpoint and characteristic conditions as well as the determinant identity.

For index11 the root separately expanded the cleared difference of adjacent ratios: 24n[16j²+(16n+28)j+14n+11]. At n8,j6,p89 the bracket is33 modulo89. The two other small q cases give composite p. Thus the index11 conclusion is complete.

The existing h2,3,4 determinant computation is a supplemental consistency check. The result excludes this literal subgroup-reduction construction; it is not a new proximity-gap lower bound, a better.codes improvement, or an obstruction to arbitrary constructions.
