# A bounded prime-field torsion fixture

The curve y^2=x^3+121 over F1657 has 1587 rational points and full rational
23-torsion of size 529. Its nonzero torsion x-coordinates give n=264, with
k=173 and tested agreement T=213 in the checked parameter window.

`build_fixture.py` checks exactly the six j=0 sextic twists at this one prime.
It verifies all torsion points by scalar multiplication, a bijective F23^2
basis labeling, all 24 cyclic subgroups, 6072 direct normalized Velu evaluations,
and all 24 complete domain factorizations. `fixture.json` stores the coordinates
and ascending polynomial coefficients. This is a verified domain, not a
received-line counterexample.

The fixed extra set used in the sole intersection census is

    Z={7,231,340,411,470}.

It comprises five coordinates in the first subgroup's kernel. The other 23
subgroups have clean kernels. After removing the common five-dimensional
all-far residue space, their generalized spaces are represented by the 18
generators X^j e_i (i=0,1,2; j=0,...,5) in the quotient of the length-259
punctured word space by RS dimension 178. The parity-check matrix has 81 rows.

`check_fixed_extra_intersections.py` uses that parity-check definition directly.
It checks that all 178 code monomials have zero syndrome, each subgroup space
has rank 18, and each of the 253 joined pairs has rank 36. Thus every pairwise
intersection in this quotient is zero. Before removal, their common
intersection is exactly the five-dimensional all-far residue space.

This rules out obtaining a useful common received plane from two clean
subgroups for this fixed extra set. It does not classify all near words on
this domain, all extra sets, extra sets varying with the witness, other curves,
or growing torsion order. No inference about arbitrary larger primes follows.
The fixture and census take under one second each locally; no rental or broad
search was used. The purpose is to check the exact intersection formulation
and prevent common all-far directions from being mistaken for a construction.
