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
