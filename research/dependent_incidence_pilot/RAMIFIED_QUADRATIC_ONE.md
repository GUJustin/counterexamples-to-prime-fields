# One bounded ramified quadratic compatibility check

## Scope and outcome

The earlier complete twenty-member Dickson seed already has an all-ramification obstruction in `../dickson_domain_deformation/RAMIFIED_OBSTRUCTION.md`. This experiment does not revisit or weaken that theorem.

The separate 24-pattern pilot here contains sixteen nearest polynomials per pattern, including candidates outside the original Dickson bank. Its saved certificates previously excluded only lifts to Z/41² and unramified extensions. They explicitly left ramified lifts open. We tested exactly ONE of those saved patterns: choose the smallest saved Jacobian rank, breaking ties by the saved order. This selects pattern index 11, clustered trial 3, rank 181. No additional seeds were generated or searched.

**Outcome:** this pattern has no mixed-characteristic DVR lift of ramification index two, over any residue-field extension. Its quadratic corrections vanish in the Jacobian cokernel, while the constant characteristic obstruction remains nonzero. Higher ramification is not excluded, and no characteristic-zero incidence bridge was found.

## Normalized tangent calculation

There are 200 variables: forty nodes and sixteen degree-at-most-nine coefficient vectors. Normalize the same fourteen geometric freedoms as in the previous full-seed proof: three nodes to their canonical values 1,2,3; all ten coefficients of the first polynomial; and one coefficient of the second polynomial whose difference from the first is nonzero modulo41. The selected columns are

    0,26,15,40,41,42,43,44,45,46,47,48,49,50.

Fractional-linear changes of the evaluation coordinate, the induced degree-nine polynomial action, common scaling, and addition of a common polynomial justify this normalization over a hypothetical DVR lift exactly as in the prior proof. Every operation reduces to the identity and uses units.

Let F be the incidence equations plus these linear normalization equations, z0 the integer seed, J its Jacobian modulo41, and Q(v) the homogeneous quadratic Taylor term. The exact calculation gives:

    number of equations =216,
    rank J=195,
    dim ker J=5,
    dimension of cokernel J=21.

Write the saved kernel basis as v=Zt with five tangent variables. There are fifteen quadratic monomials in t. Every column of Q(Zt) lies in im J: equivalently, the quadratic map into coker J is identically zero. This is verified independently by

    rank[J | quadratic-coefficient columns]=195.

A saved row vector lambda satisfies

    lambda J=0,
    lambda Q(Zt)=0 identically,
    lambda[-F(z0)/41]=18 mod41.

Thus the ramified second-order compatibility equation

    Jw + Q(v) = −u F(z0)/41,  Jv=0,

has no solution for any nonzero residue-field unit u. In a DVR with uniformizer pi and ramification index two, u is the residue of 41/pi².

## Why this excludes index two, but not all ramification

Suppose a normalized lift is z0+delta. If some component of delta has valuation one, reduction modulo pi² first gives its leading vector v in ker J. Projecting the next coefficient with lambda kills the linear and quadratic contributions but leaves the nonzero constant 18 times u. If every component has valuation at least two, the projected constant term already has strictly smaller valuation than all correction terms. Either case is impossible.

More generally the same argument excludes a hypothetical normalized lift whose smallest deformation valuation r satisfies 2r≥e, where e is the ramification index. It does NOT address 2r<e. In contrast to the old full-bank certificate, all five tangent directions here have zero quadratic obstruction, so no quadratic equation forces that leading vector to vanish. Cubic or higher terms may matter at greater ramification. This experiment therefore does not certify verticality of the incidence component, a universal lift obstruction, or nonexistence of a different characteristic-zero incidence source.

## Reproducibility and stopping rule

`ramified_quadratic_one.py` is the NumPy generator; `ramified_quadratic_one.json` stores the kernel and obstruction vector. `verify_ramified_quadratic_one.py` is an independent stdlib replay. It reconstructs the incidence Jacobian and integer residuals, independently computes ranks, expands the quadratic coefficient by truncated polynomial arithmetic, and verifies every saved certificate identity. It does not import the generator.

The generator and verifier each completed in about0.55 seconds under the384MiB/60-second guard. Reports and the PASS result are saved alongside them. The experiment stops at this prescribed one-pattern quadratic test. There is no positive lift to propagate and no basis for claiming that prime-label restriction or a square-norm parameter selection solves the field-size obstruction.
