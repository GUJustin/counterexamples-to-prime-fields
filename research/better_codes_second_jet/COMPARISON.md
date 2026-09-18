# Second hidden derivative: source gate and downstream scope

The plain dense second-jet source does **not** pass the target dimension gate in the bounded experiment below. This does not exclude a source with carefully restricted first- and second-derivative exponents. Even a positive source would require a new downstream counting argument; it cannot be inserted into the present first-order receipt unchanged.

## Relation to the primary paper

[Brakensiek–Chen–Putterman–Zhang–Zheng, arXiv:2609.08005](https://arxiv.org/html/2609.08005v1), Section 3, uses the backward Taylor relation with hidden higher Hasse derivatives. Specializing that construction to order two gives

`P(x+t) = P(x) + t P^[1](x+t) − t² P^[2](x+t) + O(t³)`.

The paper's asymptotic theorem chooses a much larger derivative order depending on its low-agreement parameters; it does not assert a useful numerical order-two source at this benchmark. The following gate is an independent exact specialization, not an invocation of that asymptotic theorem.

## Exact sufficient gate

Use variables X,Y,R,V,Z, with R=P^[1], V=P^[2], and Z the affine-line challenge. Let n=262144, w=131071, A=181275, D=mA. Take source monomials

`X^e Y^i R^j V^k Z^z`,

subject to `e+w i+(w−1)j+(w−2)k < D`, `i+j+k <= J`, and `i+j+k+z <= L`. Assume L>=J. Their number is exactly

`C(L)=Σ_(i+j+k<=J) (L+1−i−j−k) max(D−w i−(w−1)j−(w−2)k,0)`.

At a coordinate x, put t=X−x and write its received affine value as f_x+Z g_x. Set

`U=Y−f_x−Z g_x−t R+t² V`.

The substitution and its inverse preserve the nested caps (jet degree <=J, jet-plus-challenge degree <=L): replacing Y by the received term can decrease jet degree while increasing challenge degree by at most the same amount. On any actual agreeing polynomial, U is divisible by t³. Thus it suffices to annihilate the coefficients of `t^a U^b R^j V^k Z^z` with a+3b<m.

In the ambient module allowing arbitrary t powers, the exact number of these independent coefficient conditions is

`R(L)=Σ_(b+j+k<=J) max(m−3b,0) (L+1−b−j−k)`.

Restriction to the actual source can only reduce rank. Hence `C(L)−n R(L)>0` is a valid source-existence gate, uniform in all received words and lines. This upper bound does not assume that every ambient constraint is attained by the weighted source. All substitutions and coefficient counts are valid in the pinned prime characteristic; no division by factorials is used.

Grouping by ell=i+j+k gives

`c_ell=Σ_(j+k<=ell) max(D−w ell+j+2k,0)`,

`r_ell=Σ_(0<=b<=min(ell,floor((m−1)/3))) (m−3b)(ell−b+1)`.

Consequently the gate is affine in L. Testing its value at L=J and its slope decides this sufficient gate for every L>=J, not merely sampled challenge degrees.

## Bounded result

`dense_gate.py/json` checks all possible nonempty jet caps J at m=4,8,16,32,64,128: **353 cases**, all with negative slope and negative L=J value. Increasing L cannot repair any of these gates. The watchdog reports 0.59 seconds and 18 MiB. This is failure of a sufficient dimension certificate, not proof that every corresponding actual kernel is zero.

For scale, writing alpha=A/w, q=n/w, J≈c m with 1/3<=c<=alpha, the leading coefficient of the challenge-degree slope, divided by w m⁴, is

`alpha c³/6 − c⁴/8 − q(c²/12−c/54+1/648)`.

The rational sample values in the JSON are negative. They are diagnostic, not a claimed global optimization. The extra free jet direction costs local rank; simply adding a variable does not reproduce the incumbent's carefully slope-capped advantage.

## What a positive refinement would still need

The next source-level question would be a jointly restricted R/V support with a proved rank calculation respecting the coupled term t²V. Reusing the old block kernel `(a−b)^h` after adding V is unjustified: the second-order relation mixes adjacent t blocks. No such unproved saving was used here.

The pinned helper and factor machinery counts factors in Y,R,Z and uses first-order derivative geometry. A source depending on V introduces another jet coordinate and another degree profile; differentiation along actual solutions also introduces P^[3]. The old pair, singular-factor, characteristic, packing, and challenge-label bounds therefore do not automatically apply. The generic polynomial-root list bound from the new paper is far too coarse to replace the benchmark ledger and does not itself control affine-line bad labels. A viable proposal needs both a positive restricted-source gate and a quantitative second-jet factor/routing theorem before any score claim.

No better.codes improvement or full certificate is claimed.
