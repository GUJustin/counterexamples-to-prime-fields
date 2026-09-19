# Independent audit of the fixed polynomial twist gate

PASS, 2026-09-19. Actual frozen source read in full. No corrections or manuscript edits.

The degree-space argument handles both F≠0 and F=0 correctly. For nonzero G of degree e, the regimes degA<(p−1)e, >, and = give respectively impossibility, one degree residue modulo p, and the unique cancellation degree. Since 0≤e≤g₀<n<p, the noncancellation residue occurs at most once. Prime-field leading coefficients permit elimination to a basis with distinct degrees, so dimension≤2 follows. If both degrees occur, the lower is exactly h=g+n−p; consequently g₀<p−n forces dimension≤1. Constants and the A=0 or A=1 edge cases do not invalidate this reasoning. The conclusion in this section concerns G∈Fp[X], not arbitrary extension-coefficient polynomials.

For scaled monic divisors G_i=γ_iV_i, 2g₀<n ensures a native point outside both root sets. Evaluation there gives γ_i^(p−1)=γ_j^(p−1), whence γ_i/γ_j∈Fp*. Dividing G and F by one common γ and replacing A by Aγ^(1−p) is the correct normalization. This justifies the extension-scaling conclusion under the stated complement-intersection condition, including F=0. It does not silently extend the prime-coefficient dimension bound to all extension polynomials.

The low-degree-twist exclusion is stronger and valid: degA<n<p gives degA≤p−2, so for every positive degree e, G^p uniquely dominates AG and degree comparison forces p|n, a contradiction. Constant or zero G cannot yield F≠0 either. The assertion expressly requires F≠0 and does not discard possible zero-right-side solutions.

The independent monomial calculation also checks. Modulo X^n−1, coefficient Frobenius fixes G because p≡1 mod n and degG<n. Quotient chains occupy disjoint residue classes modulo n. Length≥2 cannot have every exponent divisible by p, length one q=ui−1 is invalid, and q=ui+1 gives exactly −X^(pi). For u≥2 no canceled index q=uj can coexist; u=1 is separately acknowledged. Thus the split-locator conclusion has the claimed scope.

The final varying-A residual identity is correct. Arbitrary witness-dependent twists remain outside the fixed-A bound and are not presented as impossible. The note does not prove a general received-line or rational-compiler obstruction.

Frozen source SHA256: `930e14acc13c42f1dc585b6cdc435234cf499f282bd7aa40d74013a247fb5647`.
