# Independent audit of the complete ten-cubic list

**PASS.** `verify_ten_cubic.py` independently enumerates all 1,820 four-point subsets of the sixteen rational source nodes using Fraction arithmetic and Newton divided differences. It obtains 1,516 distinct exact rational cubics. Exactly sixteen have at least five old matches: the eight seven-match source cubics and eight fresh five-match cubics. There are no six-match old candidates.

Append the two roots of g(U)=358U²+125U−25. Its discriminant is 55²·17, so the roots are distinct, nonrational, and equal to (−125±55 sqrt(17))/716. Direct rational evaluation verifies that neither is an old node. Assign the new received value by the common residue

    Q(U) mod g = (−51075−104594U)/32041,
    Q(U)=−9U−34U²−32U³.

The independent verifier performs polynomial division in the quadratic quotient ring without SymPy. Exactly two of the sixteen old candidates have zero difference remainder with Q modulo g: Q and the cubic with ascending coefficients

    (−225/242, −1453/242, −1503/121, −1008/121).

Each had five old matches and now has seven. The original eight cubics have zero new matches and retain seven. Every other old candidate has five old matches and zero new matches. The complete candidate/remainder table is saved in `ten_cubic_certificate.verified.json`.

Completeness holds even over the algebraic closure of Q. Any cubic with at least seven matches on the eighteen nodes has at least five old matches. Four of those rational old points determine its coefficients over Q, so it belongs to the enumerated set of sixteen. For a rational cubic, matching either new root forces the rational remainder modulo the irreducible quadratic g to vanish; hence it matches both or neither. Thus the maximum agreement is exactly seven and the complete nearest list has exactly ten elements.

For specialization, exclude the finitely many primes dividing denominators, node differences, the quadratic discriminant, or the nonzero evaluation differences of the finite old interpolation census. Also exclude the norms of the nonzero remainders at the two new roots. At arbitrarily large rational primes splitting in Q(sqrt(17)), the construction is over a prime field and the same complete list persists. A modulus-17 specialization is neither needed nor valid for separating the new roots, since 17 ramifies in this quadratic field.

This is a fixed finite construction (n=18,k=4,A=7,L=10), not an unbounded-list theorem. No obstruction proved for covers of the original fixed sixteen-node word applies automatically to this new eighteen-node received word.
