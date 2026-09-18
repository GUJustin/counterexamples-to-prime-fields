# Integration note: positive seven-cubic bank

Include `orbit7_appendix.tex` as a standalone appendix section; no main-file edit has been made here. It states the stronger arbitrary fixed pullback parameter m result (n14m, maxdegree3m, agreement7m, complete list7), and singles out m2 for dimension7/n28 exact quarter rate.

The positive proof uses only explicit field identities, not completeness of the preceding Groebner discovery calculations. Primary exact certificate: `orbit7_number_field.py/json/resources.json` (1.66sec). Independent affine and prime checks: `orbit7_prime_realizations.json` and upper agent's independent audit. Eighth-candidate exclusion: `orbit7_eighth.py/json/resources.json` (2.24sec), leading degree6 coefficient `(42w²+81w−30)/8`.

Important pullback detail: after the projective-to-affine change the seven-point interpolant need not remain degree6. It is enough that its degree is between4 and6, since a cubic would contradict the base complete-list proof. Thus `Q−R(psi)` has degree≤6m and7m roots, while R(psi) has degree>3m. This handles every polynomial pullback with14 separable full fibers and avoids an unnecessary parity argument.

Scope: actual complete list7 over arbitrarily large prime fields; no unbounded-list, bad-line, or better.codes improvement claim. For each fixedm the splitting-prime argument may use a different number field. The m1 F97 example has the same exact-list conclusion (interpolation obstruction5mod97).
