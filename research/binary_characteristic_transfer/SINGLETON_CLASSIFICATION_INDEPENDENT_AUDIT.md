# Independent audit of the exact singleton classification

**Superseded threshold scope:** the stronger coefficient-elimination audit in `SINGLETON_BELOW_JOHNSON_INDEPENDENT_AUDIT.md` extends classification to every threshold >p², including A0. The finite-difference proof below remains correct at its stated threshold.

September 18, 2026. **PASS** for `EXACT_SINGLETON_LIST_CLASSIFICATION.md`. The proof is algebraic and exhaustive; a field enumeration is unnecessary.

## Quantifiers and finite difference

Fix p≥3, B=F_(p^5), any finite containing field F with theta outside B, and any z in F. The candidate h may have arbitrary coefficients in F. Define

    R=X^(p⁴)+theta X^(p³)+zX^(p²)-Xh.

Every matching coordinate is a root of R, including zero if it matches. Zero is always a root of R even if it does not match; this only helps the lower bound. Thus ≥p³-1 agreements gives ≥p³-1 roots in B.

For the root set S, sum over nonzero t in B of |S intersect (S-t)| equals |S|(|S|-1). The strict inequality

    (p³-1)(p³-2)-(p-1)(p^5-1)=p³(p²-3)+p+1>0

forces at least p overlaps for some t≠0. Each high Frobenius power has constant finite difference, and Xh has degree at most p, so Δ_tR has degree at most p-1. It is zero. Among degrees 2,...,p-1 in Xh, a largest nonzero degree j would contribute a nonzero top finite-difference coefficient j*t. The possible X^p term contributes only a constant and cannot cancel it. Hence h=alpha X^(p-1)+beta. This uses neither genericity of z nor any restriction on coefficient-field extensions.

Now R is additive, so its roots in B form an F_p-subspace. Their cardinality is a power of p at least p³-1, hence at least p³.

## Projection and exact locator recovery

Choose a B-basis of F extending 1,theta. Each other coordinate of R is a polynomial of degree at most p², since the two high heads lie in B+Btheta. Its ≥p³ roots force it to be zero. This proves z,alpha,beta in B+Btheta; it does not assume them there in advance.

The theta coordinate of R is monic of degree p³ and vanishes on its entire root space. It therefore has exactly p³ distinct roots, equals the monic locator L_W of a three-dimensional subspace W, and has nonzero X coefficient v. The B coordinate is forced to equal L_W^p-a^p L_W: their difference has degree at most p² and vanishes on W. All coefficient signs in the proposed note check:

    z=c^p-a^(p+1)+theta a,
    alpha=a^p c-v^p-theta c,
    beta=(a^p-theta)v.

In particular beta≠0. Thus zero is never a match of this classified candidate, and its exact agreement set is W minus zero, of size p³-1. No candidate over F at any z can exceed that agreement threshold: such a candidate is also subject to the same exhaustive argument.

Given z, its theta component recovers a and its B component recovers c uniquely under Frobenius. Two possible locators then differ only by a scalar times X. Two three-dimensional subspaces of a five-dimensional space intersect nontrivially, so that scalar is zero. This proves one and only one candidate at every qualifying label.

Consequently the qualifying challenge set over the **whole field F**, not merely a selected affine slice, consists of exactly [5 choose 2]_p Gaussian labels. There are no omitted zero, infinity, or denominator charts: R/X is a polynomial and the zero coordinate was explicitly checked. The challenge parameter here is affine z in F; no projective infinity challenge is claimed.

Replacing f by f+s g translates the entire qualifying label set by -s. Taking s outside B+Btheta (requiring extension degree at least three over B) makes every qualifying label nonzero and, by the separately audited coordinate projection, makes both individual source agreements exactly p²-1. The classification remains valid unchanged.

## Main-admission comparison

Closest existing result: the fixed-characteristic locator compiler in the binary manuscript, specialized to this five-dimensional domain, already supplies the Gaussian population, its exact constructed supports, label injectivity, and common-agreement control. The new part here is **exhaustiveness over all z and all candidates**, hence exact count and singleton nearest lists. The finite-difference step is specific to the small message degree and should not be generalized to larger locator tails without a new argument.

At matched length N=p^5, dimension K=p, field F_(p^15), and actual threshold A=p³-1, the strengthening is:

* previously: at least [5 choose 2]_p constructed bad labels;
* now: exactly that many qualifying/bad labels, each with exactly one nearest candidate and exact maximum agreement A; every other label has agreement at most A-1.

The source gaps and field do not change. This clarifies that the superlinear exceptional count is **not** caused by large individual lists at those exceptional words. It gives a short proof worth considering alongside the existing explicit large-characteristic comparison; it should replace an ambiguous comparison with the square of a Johnson list upper bound, rather than create a second nearly identical construction section.

Limits: A is above the exact finite Johnson threshold. The lower advertised A0=p³-p² is below Johnson and above the first-order curve, but at A0 only the already-proved lower count and the separate explicit upper budget apply. There may be more qualifying labels or larger lists there. The new theorem does not show singleton lists at A0, does not control the largest list over all received words, and does not prove fixed-rate or prime-ambient tightness. Rate and margin still vanish as p grows.

Proof status: independently verified all identities, counting inequalities, projection quantifiers, and the source shift. No numerical approximation or conjectural lifting is used. Expected exposition cost is approximately one proposition and its short finite-difference proof. No main manuscript files were edited.
