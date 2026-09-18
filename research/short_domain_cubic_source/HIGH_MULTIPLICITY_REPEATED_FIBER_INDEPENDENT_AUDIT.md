# Independent audit: repeated (b-1,1) fiber

**PASS.** Independently checked HIGH_MULTIPLICITY_REPEATED_FIBER.md, including
b=2, ramification in positive characteristic, product connectedness, the exact
genus, and the section/agreement counts. No changes are required.

The derivative of y^(b-1)(y+1) is y^(b-2)(by+b-1). Under characteristic zero
or p>b this gives precisely the stated tame branch data. A transitive group
containing a (b-1)-cycle is 2-transitive: the stabilizer of the cycle's fixed
letter is transitive on its complement. Together with a transposition this
gives S_b. The separate b=2 argument is necessary and correctly present.

For three distinct nonzero labels, each unique nonzero finite branch value
supplies an inertia element (1,...,transposition,...,1). Conjugation inside
the compositum group, using its surjection onto each S_b, generates every
individual factor. Thus the joint group really is S_b^3; the degree-b^3
fiber product is irreducible, not merely a union of possible components.

At infinity, diagonal inertia has all cycles of length b. At zero there is
exactly one fixed tuple and all other cycles have length b-1 (including the
trivial b=2 case). The three separate simple branches each have index b^2.
Consequently

  2g-2 = -2b^3 + b^2(b-1)
           + (b^3-1)(b-2)/(b-1) + 3b^2
        = (b-2)(b+1),

so g=b(b-1)/2 is positive for every b>=2. All inertia orders are prime to
the characteristic. There are no omitted wild terms. Rational solutions
would embed this function field into k(X), contradicting Luroth even when
the rational function q(X) has zero derivative. Separability of q is not
an extra hypothesis.

The substitution P=R+(R-S)Y gives the stated equation with no sign error.
There are at most two nonzero labels, at most b sections for each, and at
most two sections at the zero label. Hence 2b+2 is a correct upper bound.
The q-constant and R=S alternatives are genuinely affine pencils, and the
received-word incidence bound L(A-D)<=n is valid. The explicit degree bounds
on R,S in the statement ensure the pencil directions have degree at most D.

This audit verifies only the specified repeated-fiber stratum. It does not
turn arbitrary repeated fibers into that stratum or settle general
higher-degree first-integral banks.
