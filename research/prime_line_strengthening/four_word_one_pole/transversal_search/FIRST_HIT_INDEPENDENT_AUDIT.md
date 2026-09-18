# Independent exact audit of the first p=97 transversal hit

**PASS.** The first saved hit gives an actual proper degree-seven/linear
rational function with14 agreements on a five-word28-point bank over F97.
It therefore gives a six-word length60, degree<=14, agreement>=30 bank after
the established quadratic extension over a finite extension of F97. This
audit does not independently verify the separate smooth-lifting/Jacobian claim.

## Independent reconstruction

The stdlib-only script `independent_first_hit.py` reconstructs the numerator
by ordinary Lagrange interpolation from ONLY the first eight values
(t_i-81)*w_i. It does not use the searcher's barycentric pole formula or the
other agent's parity/Jacobian method. The resulting polynomial, in ascending
coefficient order over F97, is

    N=[34,54,93,0,84,3,56,70].

It then regenerates the original four-parameter seed from a=(48,1,31,32),
checks the first pole53, and reconstructs the entire26-point split core and
its received values. All12 recorded nodes, base images, and values are valid.
The rational function N(T)/(T-81) has exactly12 core agreements and

    N(81)=48 !=0.

The second pole81 lies outside the FULL26-point core, not merely outside
the selected12 interpolation nodes. The run completed in0.58seconds with
peak RSS11904KiB under the384MiB/60second watchdog.

## Residual factor and the two fresh points

The normalized fifth polynomial is

    G5(T)=86+17T^4+93T^6.

The exact difference numerator D=N-(T-81)G5 has ascending coefficients

    [16,65,93,0,6,83,23,74].

Its roots on the26-point core are exactly33,56,57,79,88. Dividing by their
monic locator leaves

    74T^2+2T+8=74(T-24)(T-52).

The discriminant is61, nonzero modulo97. Both fresh roots24 and52 already
belong to F97; they are distinct and avoid the entire core and the pole81.
The script also verifies these guards via polynomial gcds, independently
of listing roots.

Set the received values at these two fresh points equal to G5. Then the
new rational function agrees there by the displayed residual identity, so
it has exactly14 agreements on the resulting28-point domain and remains
proper with its pole off that full domain. The four old polynomial words
each already have14 matches on the core, while G5 has12 core matches plus
these two fresh matches. Thus the complete five-word input bank is genuine.

## Finite-extension consequence and remaining lift scope

Apply the quadratic pullback/pole-clearing operation again, using T^2 and
pole81. The28 old coordinates are nonzero, so this pullback is unramified
there. Over the algebraic closure their56 preimages, the two pole preimages,
and two further fresh coordinates give60 distinct points. The six resulting
polynomials have degree at most14 and at least30 matches each. All needed
coordinates lie in a finite extension of F97.

This proves an actual second operation at characteristic97. A smooth
Jacobian certificate is needed to transport this finite-field incidence
pattern to characteristic zero and arbitrarily large split primes. That
certificate is being audited separately; it is not inferred merely from
this exact finite-field witness. No unbounded induction or superlinear
bad-label theorem is claimed.
