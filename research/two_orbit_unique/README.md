# Unique witnesses with two padding orbits

The paper includes `two_orbit.tex`, `function_field.tex`, and `finite.tex`.
`PROOF_AUDIT.md` records the proof checks and scope.

The construction beats every fixed exponent constant c2 < 2+1/d,
with far separation 2d/(2d+1) of the gap. Thus c2=2 is compatible
with arbitrarily close to full-gap separation and unique nearby
witnesses. The integer version has a polynomial-time decoder given
roots over sufficiently large splitting primes. The function-field
version works at logarithmic length, without that decoder or an
efficient sampler.

Verification:

- `verify_finite.py`: independent exact replay of the five finite
  existence rows, including Lucas–Lehmer, strict Elias, and ratios.
- `check_exhaustive.py`: all parameters of two million-element-field
  fixtures, then independent all-codeword interpolation classification.
- `check_negative.py`: extra-coordinate fixtures and a small field
  where all root-admitting parameters have a forbidden root relation.
- `check_formal.py`: finite-characteristic series, rotation-class count,
  and distinct product polynomials.
- `check_integer.py`: actual splitting-root fixtures satisfying the
  conservative norm and no-wrap bounds, plus witness recovery.

Run numerics sequentially under the repository's 384 MiB watchdog.
`finite.py` generates parameter candidates; its stored rows are
existence certificates, not particular domains. The smaller explicit
fixtures audit geometry but are not numerical-bound violations.
No better.codes improvement or global list upper bound is claimed.
