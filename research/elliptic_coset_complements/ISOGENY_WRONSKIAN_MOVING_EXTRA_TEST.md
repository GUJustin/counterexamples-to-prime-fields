# Isogeny Wronskians do not supply moving extra domain roots

September 18, 2026. Named algebraic test for the moving-quintic target. No construction scan.

**Outcome.** The ramification polynomial of a normalized cyclic isogeny has no roots on the odd-order torsion domain. The Wronskian of two tag-fiber locators has domain zeros precisely at the fixed kernel coordinates, independent of the two tags. Thus this derivative identity does not generate a moving degree-at-most-five locator for extra domain errors. This does not exclude derivatives with shifts, other linear combinations, or a different shared-source identity.

## Exact differential identity

Let \(E:y^2=F(X)=X^3+AX+B\) be nonsingular in characteristic \(p>3\). Assume \(\ell\ge23\) is an odd prime different from \(p\), with full rational \(\ell\)-torsion, and use the domain \(\mathcal D=x(E[\ell]\setminus\{O\})\). Write \(\Phi\) for its locator.

For a subgroup \(H\) of order \(\ell\), use the normalized quotient

\[
Y_H=\frac{N_H}{K_H^2},\qquad t=\deg K_H=(\ell-1)/2,
\qquad B_H=K_H^2.
\]

Define

\[
R_H=N_H'K_H-2N_HK_H'.
\]

Then

\[
Y_H'=\frac{R_H}{K_H^3},\qquad
N_H'B_H-N_HB_H'=K_HR_H.
\tag{1}
\]

The normalized differential relation
\(\varphi_H^*(dx'/(2y'))=dx/(2y)\) gives
\(y(\varphi_H(P))=y(P)Y_H'(x(P))\). If the quotient curve is
\(y'^2=x'^3+A_Hx'+B_H^{\rm curve}\), this yields the polynomial identity

\[
\boxed{
F(X)R_H(X)^2=N_H(X)^3+A_HN_H(X)K_H(X)^4
+B_H^{\rm curve}K_H(X)^6.}
\tag{2}
\]

This is an exact identity of functions and polynomials. The normalization is the Vélu normalization used throughout the preceding quotient notes. The leading coefficient of \(R_H\) is \(\ell-2t=1\), so \(\deg R_H=3t\).

## Its roots miss the torsion domain

At a nonkernel point \(P\in E[\ell]\), both \(P\) and \(\varphi_H(P)\) are nonzero points of odd order. Neither has y-coordinate zero. Equation (2), or the differential relation, therefore gives \(R_H(x(P))\ne0\).

At a kernel coordinate \(q\), coprimality of \(N_H,K_H\) and squarefreeness of \(K_H\) give

\[
R_H(q)=-2N_H(q)K_H'(q)\ne0.
\]

Consequently

\[
\boxed{
\gcd(\Phi,R_H)=1,\qquad
\gcd(\Phi,N_H'B_H-N_HB_H')=K_H.}
\tag{3}
\]

The nonkernel zeros of the x-map derivative arise from preimages of nonzero two-torsion on the quotient curve. They are ramification points, not additional coordinates in the odd-order torsion evaluation set.

## Two omitted tag fibers do not move this critical set

Let \(L_a=N_H-aB_H\) and \(L_b=N_H-bB_H\), with \(a\ne b\). With the sign convention explicitly fixed as

\[
W(L_a,L_b)=L_a'L_b-L_aL_b',
\]

direct expansion gives

\[
\boxed{\quad W(L_a,L_b)=(a-b)(N_H'B_H-N_HB_H')
=(a-b)K_HR_H.\quad}
\tag{4}
\]

Thus its domain gcd is exactly \(K_H\), independent of \(a,b\). The full gcd has degree \(t\ge11\), not at most five. Selecting five of its roots would be an additional arbitrary selection from the subgroup's fixed kernel, not a pair-dependent locator supplied by (4).

More generally, composing \(Y_H\) with a separable rational function of the tag variable can add derivative zeros on the domain only in whole nonkernel tag fibers: away from its poles the new condition is \(M'(a)=0\). Each such fiber has \(\ell>5\) coordinates. This statement concerns the actual critical set of the composition, not a chosen small factor of that set or an arbitrary derivative combination.

## What kernel corrections do and do not accomplish

The pairwise disjointness proof for the existing canonical quotient planes uses only the \(n-\ell+1\) coordinates outside the two kernel sets. It therefore still applies if those two planes may be corrected arbitrarily on their entire kernel sets: clearing denominators has degree at most \(n-\ell\), so the rational identity and pole-divisor contradiction are unchanged. In particular, choosing at most five kernel roots from (4) cannot merge the existing subgroup-specific canonical received planes.

This does **not** exclude arbitrary noncanonical error values supported on two fibers plus selected kernel positions. Such a family still requires the shared split-quintic recurrence of [FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md](FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md). The Wronskian identity supplies neither that recurrence nor its label population. Likewise \(\gcd(\Phi,L_a')\), \(\gcd(\Phi,(L_aL_b)')\), shifted derivatives, and independent linear combinations are not classified here; they would need a new predicted common-line identity before a search is justified.

## Verification and decision

`ell23_fixture/verify_isogeny_wronskian.py` replays (1)–(4) on the already saved \(\ell=23\), \(p=1657\) fixture for all 24 subgroups. It checks the differential identity by recovering the two quotient-curve coefficients, the two exact domain gcds, and the Wronskian sign for a distinct tag pair per subgroup. This is verification of the proved identities, not a search for a new locator or extra set.

**Replay PASS:** all 24 differential identities, all 72 domain-gcd checks (including the pair Wronskian), and all 24 sign checks passed. The receipt is `ell23_fixture/isogeny_wronskian_verified.json`; runtime was approximately 0.25 seconds using standard-library integer polynomial arithmetic.

The natural ramification/Wronskian proposal therefore supplies no moving extra domain roots and no new compiler. The unrestricted point-dependent quintic system remains open. No additional scan or rental follows from this test.
