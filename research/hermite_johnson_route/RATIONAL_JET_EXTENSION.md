# Bounded-complexity quadratic equations with rational singular jets

This extends the interpolation and singular-core transfer in `PROOF.md`. It uses the same specialization-safe algebraic-root lemma. The original equation may depend on the challenge and nonlinearly on the value variable; no X-degree bound is imposed.

Write

`Q(X,z,u,v)=a(X,z,u)v²+b(X,z,u)v+c(X,z,u)`,

where Q is nonzero, its total degree in (u,v) is at most B0, and its z-degree is at most H0. Put `d=B0+H0` and assume characteristic not two. At a domain coordinate x set `w_x(z)=f_x+zg_x` and substitute it into a,b,c, obtaining polynomials `a_x,b_x,c_x` of degree at most d. Put `Delta_x=b_x²−4a_x c_x`.

## Exact core and exceptional-incidence decomposition

The **ordinary core S0** consists of coordinates where all three polynomials a_x,b_x,c_x vanish identically. There the equation supplies no jet information on the received line.

The **Hermite core S1** consists of coordinates where a_x is not the zero polynomial and Delta_x vanishes identically. At any label with a_x(z)≠0, every singular agreement forces

`P'(x)=−b_x(z)/(2a_x(z))`.

The right side is a fixed rational function of challenge degree at most d in numerator and denominator. Roots of a_x on S1 are declared exceptional coordinate-label incidences.

Outside S0∪S1:

- If a_x is nonzero, singular agreement forces the nonzero Delta_x(z) to vanish, giving at most 2d labels.
- If a_x is identically zero and b_x is nonzero, singular agreement forces b_x(z)=0, giving at most d labels.
- If a_x and b_x are identically zero and c_x is nonzero, any actual agreement must satisfy c_x(z)=0, again at most d labels.

Including the denominator roots on S1, the total number of exceptional singular coordinate-label incidences is at most **2dn**. This bound is uniform over all candidates. Thus at most `2dn/(e+1)` labels have more than e such coordinates.

## Interpolation after clearing denominators

Retain the finite parameters M,T,B,V,c_M from `PROOF.md`, with `V>s*c_M`. For a coordinate in S1, expand

`R(x+t,z,w_x(z)−b_x(z)t/(2a_x(z))+U)`

and multiply the whole expansion by `(2a_x(z))^B`. Each constrained coefficient with local weight `a+2j<M` is now a polynomial in z of degree at most

`H+B(d+1)`.

To see this bound term by term, a source Y-power j contributes a numerator of degree at most j(d+1), and its clearing factor has degree at most (B−j)d; the source coefficient contributes at most H. Hence the sum is at most H+Bd+j≤H+B(d+1).

There are at most `s*c_M*(H+B(d+1)+1)` scalar constraints. Therefore the explicit choice

`H=floor(s*c_M*B(d+1)/(V−s*c_M))`

ensures a nonzero interpolant. At nonexceptional labels division by `(2a_x(z))^B` is valid, so matching the rational first jet still gives a zero of multiplicity at least M. Every candidate with b* good singular matches satisfies `R(X,z,P)=0` exactly as before.

## Result and scope

Let u=|S0|,s=|S1|. At fixed positive rate, bounded B0,H0, and signed margins

`A−D≥ηn`, `A−u≥sqrt(D*s/2)+εn`,

the number of full-support bad labels among actual degree-D solutions of Q is O(n), once the algebraic-root lemma is applied with the bounded interpolation degrees. The regular-incidence contribution uses the existing theorem with **the original** B0,H0. Its singular exception term becomes `2dn/(e+1)`. All final incidence counting still uses original full value-agreement supports.

In particular, **an empty ordinary core suffices**, even if every coordinate belongs to the persistent Hermite core and its derivative prescription is rational rather than affine in z. The conclusion does not assume that a_x is nonzero at every label; its finitely many roots were counted explicitly. An arbitrary large ordinary core remains outside the assertion unless the signed margin survives its loss.

The characteristic assumptions are those of the base proof and its algebraic-root lemma, together with characteristic not two. This note does not claim a completed Lean implementation or an unconditional first-order proximity theorem: it requires one common bounded-complexity quadratic-in-v equation containing the candidates.
