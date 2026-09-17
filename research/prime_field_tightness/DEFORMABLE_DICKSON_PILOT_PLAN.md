# One bounded domain-deformation pilot

Executed September 17. See ../dickson_domain_deformation/README.md and
its independently replayed certificates: finite smooth lift at p=17,
unramified first-correction obstruction at p=41. No growing-family claim.

The existing Dickson cyclotomic-lift checks keep the evaluation domain
fixed. A different possibility is to deform nodes, the received word,
and every candidate polynomial simultaneously while preserving the
agreement incidence graph. A characteristic-zero realization of a
growing fixed-gap graph would give arbitrarily large split-prime source
lists and address the actual exponent-tightness target.

The archive already explored this strategy for ternary additive locator
banks. It found a finite smooth lift at n81 and an unramified obstruction
at the next tested seed. Do not restart that census. References:
mca_exponent_one/rounds/codex_night_2026-09-13/optimality/
DIGEST_INTRINSIC_CYCLE46.md and RESULT_TERNARY_JACOBIAN_OBSTRUCTION.md.
Those concern different equations; their negative result does not
automatically exclude free-domain Dickson deformations.

Only two initial Dickson fixtures are proposed: p17 and p41, with
n=p-1, k=n/4, L=n/2 and A=3n/8. Use all candidates indexed by nonzero
a modulo sign, with the same supports as the full-length proposition.
Allow all n nodes and all L*k polynomial coefficients to vary.
Eliminate the received symbols by selecting, at each node x, one
incident candidate P_ref and imposing P_i(x)-P_ref(x)=0 for the others.
This is equivalent to allowing all received symbols to vary freely.

For canonical integer lifts, form the first p-adic correction system:

    sum_t x^t*(delta c_i,t-delta c_ref,t)
       +(P_i'(x)-P_ref'(x))*delta x
        = -(P_i(x)-P_ref(x))/p mod p.

Evaluate the right side modulo p^2 before division. A full-row-rank
Jacobian would prove a finite unramified all-orders lift. Mere consistency
would establish only a first correction. If inconsistent, preserve a
left-kernel vector annihilating the original Jacobian but not the right
side, and verify it independently using the defining evaluations.
Such a certificate excludes only an unramified p^2 lift of this exact
incidence seed, not ramified lifts or arbitrary characteristic-zero
configurations.

Use the384MiB watchdog, sequentially. Do not expand to a large prime or
ramification census without a new symbolic reason. The main objective
is a scalable construction, not accumulating more isolated lift tests.
