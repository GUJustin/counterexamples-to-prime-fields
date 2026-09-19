# Exact first-lift test of a binary near-Johnson incidence fixture

**Result: no unramified mod-4 lift through this particular binary point.**
An independently replayed linear combination of234 original incidence equations, belonging to the first13 bank words, gives the linearized contradiction0=1. This does not rule out ramified characteristic-zero branches, another binary fixture, or an unrelated odd-characteristic realization. No wider fixture census was run.

## Actual fixture and parameters

The residue field is F_(2^21), represented by t^21+t^2+1. The generator routine verifies that t has multiplicative order2^21-1, proving the modulus is primitive. Its order127 subgroup supplies the subfield D=F128, including0. Put theta=t and shift=theta^2. Over the base subfield,1,theta,theta^2 are independent.

Use n=128,k=8 and the received words

f(x)=x^63+theta*x^31+theta^2*x^15,  g(x)=x^15.

These are the shifted quadratic-near-Johnson construction in the read-only binary repository, `sections/constructions/quadratic-near-johnson.tex`. Both source agreements and ordinary common agreement are15 by that construction's projection and remainder argument.

Enumerate all2667 codimension-two binary subspaces of D through their dual two-planes; shuffle with the saved C++ seed20260918 and select129. For each locator

L_W=X^32+a X^16+b X^8+V,

use label z=a^3+b^2+theta*a+theta^2 and witness

h_W=((a^2+theta)*(b X^8+V)+V^2)/X,

of degree<8. The generator checks every witness at every one of the128 nodes: its exact agreement set is W minus0, of size31. All129 labels are distinct. Select29 of those31 incidences per witness, with the same deterministic shuffle. The plain-text fixture saves every node, word value, label, witness coefficient and selected incidence, so replay does not depend on reproducing the shuffle.

Threshold T=29 is below the finite Johnson count sqrt(128*7)=sqrt896 and above the first-order curve. The standard bound gives

128*a1(8/128) <= sqrt512 + 8192^(1/4)/sqrt3 < 23+6=29.

Thus the test uses a genuinely relevant threshold rather than the lower half-rate tree threshold. The binary source loss is29-15=14, versus capacity margin29-8=21. The129 selected labels exceed the128-node count, but this finite fixture alone is not an asymptotic superlinear theorem.

## All-variable first-lift equations

Lift the field to the unramified ring

R=(Z/4Z)[t]/(t^21+t^2+1).

Every residue element is initially lifted using its binary coefficient vector. This is only a convenient section: all possible lifts are obtained by adding2 times an arbitrary residue-field element.

For every retained incidence use

h_W(x_i)-f_i-z_W*g_i=0.

Allow ALL evaluation nodes x_i, both received-word entries f_i,g_i, all labels z_W, and all eight witness coefficients to vary. In particular, g is NOT constrained to remain a monomial after lifting. There are1545 residue-field correction variables and3741 equations. The linearized row has coefficients h'_W(x_i) at the node variable,1 at f_i,z_W at g_i,g_i at the label variable, and x_i^j at each witness coefficient. Its right side is the original ring residual divided by2.

Each witness's nine local variables have rank9. Eliminating them leaves2580 equations in384 global variables. The coefficient rank is347 and augmented rank348. `witness.cpp` independently eliminates in reverse column order and exports an original-equation contradiction, using the saved local-elimination relations.

## Independent certificate replay

`independent_verify.py` uses only Python's standard library. It reads `fixture.txt` and `contradiction.bin`; it does NOT trust the generated field tables, reduced matrix, or either elimination implementation. It recomputes:

* residue multiplication by carryless polynomial arithmetic;
* mod-4 products by ordinary coefficient convolution and polynomial reduction;
* every used binary incidence and its mod-4 obstruction;
* all1545 coefficients of the weighted original Jacobian.

It verifies every weighted coefficient is0 and the weighted obstruction is1. The result and source/fixture hashes are saved in `independent_verified.json`. The certificate has234 nonzero weights, on13 of the129 bank words. These13 words already obstruct this specific first lift; no minimality is claimed.

The generator took approximately0.25 seconds, and the independent certificate check approximately0.12 seconds. No rental or large search was used. `reduced_matrix.bin` and `local_relations.bin` preserve the intermediate calculation; only the fixture and contradiction are needed for the independent checker.

## What the failure means

This rules out a deformation over this unramified mod-4 coefficient ring reducing to the saved binary point, even with arbitrary word and node perturbations. It does NOT rule out a characteristic-zero point with ramification at2, a component not passing through this residue point, a different selection of supports/incidences, or a different prime-field compiler. Consequently it closes this concrete first-lift attempt, not the requested binary-to-prime transfer in general.

## Ramification-index-two continuation (bounded, completed)

The unramified obstruction alone did not settle ramified lifting. For a uniformizer u with u²=2, modulo u³, an arbitrary lift has a tangent v and second correction w satisfying

Jv=0,  Jw=r+Q(v),

where r is the saved divided-by2 residual. For each original incidence, its Hasse quadratic is

Q_i(v)=dx_i * sum_(j odd) dh_j*x_i^(j-1)
       +dx_i² * sum_j binom(j,2)*h_j*x_i^(j-2)
       +dz*dg_i.

No node, source, label or witness variable is fixed. `ramified.cpp` constructs the full37-dimensional tangent kernel. The first saved unramified certificate does NOT obstruct this ramification: its restricted quadratic has16 nonzero diagonal coefficients. All666 cross coefficients vanish, but that one nonzero square form can cancel its right side; no conclusion was drawn from it alone.

`full_ramified.cpp` then computes all703 quadratic coefficients in the FULL Jacobian cokernel. All cross terms vanish there. The37 square-coordinate columns have rank3, whereas adjoining r gives rank4. Since squaring is bijective in the finite residue field, this is an inconsistent semilinear system and excludes an index-two lift through the saved point.

For a direct check independent of those ranks, `ramified_witness.cpp` exports `ramified_contradiction.bin`, a combination of258 ORIGINAL equations. `independent_full_ramified_verify.py` recomputes ordinary ring arithmetic, verifies all37 full-kernel vectors, verifies their independence through a literal identity minor, and evaluates ALL703 quadratic coefficients. The combination annihilates every original Jacobian column and every Hasse-quadratic coefficient on that kernel, while its divided-by2 residual equals1. Thus applying it to Jw=r+Q(v) gives0=1 for EVERY tangent v.

The independent rank-completeness audit separately reconstructs all2580 reduced coefficient rows from the original fixture and local relations, verifies every local rank9, and obtains global rank347 using reverse-column/bottom-pivot elimination. This gives original rank1508 and kernel dimension37; together with the verified independent37-vector basis it prevents accidentally checking only a proper tangent subspace. See `independent_rank_completeness.cpp` and its JSON receipt supplied by the independent agent.

The final scope is **no ramification-index-two lift through this saved binary point**, including after residue-field extension. The coefficient identities and complete kernel remain valid under such extension. If2=epsilon*u² modulo u³ with epsilon a nonzero residue unit rather than exactly u², the same certificate yields0=epsilon, so the unit does not evade the obstruction. This does not exclude higher ramification, other binary points, or unrelated prime-field configurations. No further ramification orders or fixtures were tested.
