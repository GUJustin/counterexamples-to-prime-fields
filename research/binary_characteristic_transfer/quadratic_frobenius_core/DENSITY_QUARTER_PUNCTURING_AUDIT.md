# Quarter-density second block: exact profile and scope

September 18, 2026. The proposed puncturing is valid for every prime
`p >= 257`. Integration-ready proof: `density_quarter_puncturing.tex`.
It uses the existing Frobenius quadratic classification; it does not
introduce a new prime-field transfer.

Keep all `2(p²−1)` points of `D0` and exactly `(p²+3)/2` points of `D1`.
The length is `(5p²−1)/2`. The random subset is only an existence proof;
no explicit subset or finite census is claimed. Every one of the
`p(p+1)` canonical second-block fibers can simultaneously retain at
least `ceil(p/4)` points: the failure probability is at most
`p(p+1) exp(−(p−1)/16) < 1`.

The onset is certified without floating-point approximations:

* `257·258 < 16^6/6! + 16^7/7! < exp(16)`.
* The logarithm of the displayed failure bound has negative derivative
  on `[257,infinity)`.
* `sqrt(15/4) < 31/16`, `(15/16)^(1/4) < 1`, and `sqrt(p) < p/16`
  for `p > 256`, proving first order is strictly below `2p`.
* `2p−2+ceil(p/4) >= floor(11p/5)` for `p >= 40`.
* `floor(11p/5)^2 < 5p²−1` for `p >= 3`.

At the advertised threshold `T=floor(11p/5)`, the complete raw-label
profile is `(p+1)(p²−1)` singleton labels, zero with `p+1` witnesses,
and no others. The larger count includes the formerly omitted cases
with exactly one of `b,v` zero. Two raw labels outside all parameter
planes have exact source and common agreement `A=2p`; affine endpoint
normalization `lambda=alpha+z(beta−alpha)` preserves the profile.
This convention avoids introducing the separate direction word that
occurs in an unnormalized `r+zs` pencil.

The actual canonical agreement is not asserted to equal `T`: it is
`2p−2·1[b=0]` plus the retained size of the relevant second-block fiber.
The list classification at `T` is exact nonetheless.

The bank size divided by length tends to infinity. The normalized
source/common loss divided by the advertised capacity margin tends
to `(T−2p)/(T−3)=1/11`. Both the rate `3/n` and the absolute normalized
gap tend to zero. The domain remains inside `Fp4`, with its two full
`Fp2`-derived blocks; `p=Theta(sqrt(n))`. This strengthens the existing
extension-field profile but does not solve the requested prime-alphabet
or prescribed short base-field-domain transfer.

## Smallest advertised characteristic

At p=257, the theorem gives n=165122, message dimension3, A=514,
tested T=565, and17040384 singleton labels over F_(257^4).
There is one additional label with258 witnesses. The proximity loss is
51/165122 and the capacity margin is562/165122; their ratio is51/562.
These parameters are exact consequences of the existence proof, not an
enumerated evaluation-domain or received-word certificate.
