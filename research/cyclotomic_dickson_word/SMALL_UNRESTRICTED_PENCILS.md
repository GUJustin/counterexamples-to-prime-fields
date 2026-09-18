# Complete W9 and W10 gates

For W=(X^k−1)^2/2 on μ_(4k), seek degree<k candidates with A matches. A nonconstant candidate has m≤k−1 matches in any constant-word coset. Some coset has m≥ceil(A/4). Fix its m matching roots, factor P−v=G R, and put d=k−1−m. Split the other3k nodes into halves of sizes ceil(3k/2),floor(3k/2). If ceil((A−m)/2)≥d, one half contains d matching anchors. Enumerating those anchors gives R=R0+tL; each other node supplies a scalar t. A bucket of size A−k+1 completes A matches. Quotient the initial m-subsets by rotations in μ_k, then retain all four choices of constant coset. Constants themselves have only k<A matches.

This inequality holds for every m≥3 for (k,A)=(9,12), and every m≥4 for (10,13). Thus no balanced branch is needed. The reusable source generator coset_pencil_generate.py checks the inequality and specializes the audited W12 scanner. Empty-anchor pencils are counted once.

W9: F1009, primitive36th root41. All271,252 pencils,0.059seconds. One orbit of size3, each with12matches. Nonzero coefficient degrees0,3,6 only.

W10: F1201, primitive40th root15. All903,212 pencils,0.224seconds. Two orbits of size10, each with13matches. Both have generic degree9 coefficients. These are finite-field survivors pending exact cyclotomic replay, not characteristic-zero constructions.

Each retained evaluation vector was independently Fourier-interpolated, verifying degree<k and its full support. Every characteristic-zero candidate is integral at this split prime by interpolation at k unit-separated matching nodes. Since modular survivors have exactly A matches, its support is exactly the modular support. Exact interpolation on any k of those nodes, followed by all4k checks over Q(ζ_(4k)), therefore exhausts all characteristic-zero candidates.
