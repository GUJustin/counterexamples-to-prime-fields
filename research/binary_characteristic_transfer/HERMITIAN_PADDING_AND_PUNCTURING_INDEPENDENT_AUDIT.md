# Independent audit: Hermitian padding and puncturing transfer

2026-09-19. **PASS** for the actual research note hashed below. No manuscript edits or scans.

## Positive fixed-rate padding

The evaluation domain S is contained in E and avoids beta, which is essential for the coefficient projection onto E⊕omega E. Matching either endpoint forces the omega-component codeword to match 1/(X−beta); the nonzero polynomial denominator argument gives at most k positions on ANY such S. Independent interpolation gives exact individual agreement k, and reciprocal subtraction plus simultaneous interpolation gives exact common agreement k.

Every original displayed residual P_G has all its roots in B. Enlarging S therefore preserves its EXACT D−1 witness matches. The shifted affine parameter lambda=omega+t retains all M=p²(p−1) distinct bank labels, none at the endpoints. The conclusion is correctly a lower bound on exceptional labels, not a complete-list assertion after padding.

At the smallest allowed length n=p²+1, Johnson slack is p²−4p−2>0 for p≥5; it increases with n. For each fixed rho∈(0,1), n=ceil(k/rho) eventually obeys both length bounds. Then M=Theta(n^(3/2)), the normalized margin is Theta(n^(−1/2)), and both individual losses equal the full margin. Since T/n→rho<a1(rho), the construction remains below first order. Fixed rate does not mean fixed positive margin.

## Support-preserving puncturing and affine-corrected shortening

Subtracting two distinct-label witnesses gives a reciprocal explanation on the complement of their two error sets, so r_i+r_j≥m−k' is necessary. Distinct nonzero-radius norm circles intersect in at most two points, since their difference is a trace line and the norm restricted to a nonzero line direction has nonzero quadratic coefficient.

The incidence second moment yields exactly b(bar_r²−2m)≤m(bar_r−2). Under Delta²>8m, bar_r≥Delta/2 lies above sqrt(2m). The derivative of (u−2)/(u²−2m) has numerator −(u−2)²+4−2m<0 for the relevant m≥3. Substitution therefore gives the stated bound (2mDelta−8m)/(Delta²−8m), and its fixed-rate limit 2/(1−rho). It permits replacement witnesses but requires their errors to stay inside their original circles, as explicitly stated.

For affine corrections on deleted coordinates, two zero canonical errors force all errors there to vanish. Otherwise the coordinate lies on at least b−1 circles. Pair counting gives v≤2b/(b−2), hence at most two such coordinates when b≥7. The reduction to common-agreement shortening is therefore sound with the stated hypotheses.

## What is and is not available over the quartic alphabet

The positive proof uses degree eight for a concrete reason: all evaluation coordinates, f and g lie in E, and an independent coefficient omega forces a reciprocal component at every possible match. Within E this projection is unavailable.

A bound on the native c* endpoint alone would NOT prove the same padded result for the existing quartic pair (f,f+c*g). First, the native cofactor-descent proof uses roots in B; it does not bound matches on added E\B coordinates. Second, agreement of f cannot decrease when coordinates are added at fixed code dimension. The audited Möbius competitor gives native agreement at least D−e for every beta on its Dirichlet families. At the padded threshold D−1 its gap is therefore at most e−1. Along the diagonal with e/p→0 this is a vanishing fraction of p−1, regardless of padding. Thus the existing quartic pair cannot uniformly attain the degree-eight theorem's exact agreement k or full-margin individual losses merely by settling c*.

This does not rule out a different quartic endpoint pair with a new source-distance proof, carefully selected padding supporting weaker gaps, or a separate c* improvement. None follows from the current transfer. The unconditional positive statement remains the degree-eight fixed-rate padding proved above.

Source SHA256: `8a7a17abfdab071492ad3ade94a09964b06b7948d612232b120ca3393f65c8ee`.
