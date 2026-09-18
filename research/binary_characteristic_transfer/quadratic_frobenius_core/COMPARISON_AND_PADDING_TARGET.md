# Matched comparison and the exact missing padding identity

**Update:** the structured-padding question posed below is now resolved by `scaled_fiber_padding.tex`, with independent audit in `TWO_BLOCK_INDEPENDENT_AUDIT.md`. The original seed/target analysis is retained below as provenance.

Compared against `../projective_quadratic_line.tex`, not against a hypothetical absence of growing agreement gaps. No new scan, manuscript edit, or rental.

| Parameter | Existing projective quadratic line | New Frobenius core only |
|---|---|---|
| Code dimension | 3 | 3 |
| Domain size | 2(p⁴+p³+p²+p+1) | 2(p²−1) |
| Characteristic relative to length | Θ(N^(1/4)) | Θ(N^(1/2)) |
| Evaluation / challenge fields | F_(p⁵) / F_(p¹⁵) | Domain in F_(p⁴); no completed challenge line |
| Source/common agreement | Exactly 2(p+1) | Not established for a completed line; the proposed core direction is zero |
| Exceptional agreement | Exactly 2(p²+p+1) | Core nearest agreement 2p |
| Population | Exactly [5 choose 2]_p=Θ(p⁶)=Θ(N^(3/2)) distinct exceptional labels | p²−1=Θ(N) nearest bank words at one center |
| Completeness | Every qualifying label has a singleton list | Complete maximal core list; secondary canonical list has p+1 words at 2p−2 |
| Above first order, below Johnson | Proved at threshold 2p²+p | No line theorem; no exceptional-label count |

The existing theorem already has an additive source-to-bad agreement gap Θ(√N). Its normalized gap tends to zero. A successful new construction with Θ(p²) fresh coordinates and Θ(p) extra agreement would retain that same gap scale, while improving the characteristic scale to Θ(√N). Both remain vanishing-rate extension-field constructions. The bank size alone is not a count of affine challenge labels.

## Missing identity, in a directly checkable form

Let I={(a,b) in B²: a^(p+1)=1, b^p=−a^p b, b≠0}, so |I|=p²−1. Choose a fresh set S disjoint from D0, of size t=Θ(p²), and values F(x),G(x) with G(x)≠0. Define

    lambda_(a,b)(x)=(a x²+b−F(x))/G(x).

The needed algebraic mechanism is a family of Ω(p³) distinct scalars z, each with some (a,b)∈I such that

    |{x∈S : F(x)+zG(x)=a x²+b}| >= delta*p

for a fixed delta>0. In words: many maps lambda_(a,b) must have many fibers of size Θ(p), with enough distinct fiber values across different bank members. A single large fiber for each bank yields only O(p²) labels and does not meet the target.

The exact incidence budget is

    sum_(a,b) sum_z |lambda_(a,b)^−1(z)| = (p²−1)t.

Hence M distinct labels with d fresh matches necessarily satisfy Md≤(p²−1)t. The target M=Θ(p³), d=Θ(p), t=Θ(p²) uses a constant fraction of this entire budget. It needs systematic fiber compression, not isolated extra roots. At every fresh x≠0, x² is outside B; therefore (a,b)→a x²+b is injective. Thus all bank values, and their labels at that coordinate, are distinct. This is useful for counting, but does not itself create repeated labels across coordinates.

One concrete polynomial formulation is to find fresh polynomials F,G of degree at most p such that many residuals

    F(X)+zG(X)−aX²−b

split with at least delta*p distinct roots in the same fresh set S. For d=p and degree exactly p this asks for proportionality to p-point locators. It must hold for Θ(p) labels per bank on average, together with global label distinctness. Low fixed-degree fresh polynomials cannot do this: a nonzero residual of degree D has at most D roots, so D≥d is necessary. Identically zero residuals are a separate degenerate case, not a general solution to this budget.

## A feasible numerical window, not a construction

Suppose t~tau*p², extra agreement d~delta*p, source/common agreement remains A=2p, and T=(2+delta)p. Then N~(2+tau)p² and K=3. The low-rate first-order leading term is sqrt(3N/2). The strict below-Johnson and above-first-order window is

    2*delta+delta²/2 < tau < ((2+delta)²−3)/(3/2).

For example delta=1, tau=3 gives N~5p², T~3p, with sqrt(7.5)*p<T<sqrt(10)*p. This only demonstrates compatible scales. Nothing here realizes the required fibers.

A full proof must additionally keep the endpoints and common agreement at 2p, control the p+1 secondary b=0 canonical words (which begin at 2p−2), and bound every noncanonical quadratic. Degree-p fresh residuals would give the latter ≤p+p=2p by the proved core classification, unless identically zero. Endpoint avoidance and identity exceptions still require explicit treatment. Singleton lists require controlling collisions of the constructed labels, not just their total incidence count.

Conclusion: the new seed supplies the rich core and a stronger characteristic/length ratio. The missing theorem is the displayed simultaneous large-fiber identity with label separation and endpoint control. No new gap-size novelty or line counterexample follows from the seed alone.
