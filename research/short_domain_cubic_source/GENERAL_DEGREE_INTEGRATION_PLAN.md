# Consolidation applied to the manuscript

Draft: general_degree_first_integral.tex. Insert its input immediately before the existing general_cubic_list.tex input. It proves the arbitrary-degree zero-dimensional theorem, its bank intermediate bound, and the repeated-constant-fiber corollary. The cubic theorem retains its stronger unconditional conclusion and sharper p>max(3,2D) characteristic hypothesis by keeping its existing positive-dimensional classification.

## Exact replacement 1 in general_cubic_list.tex

Keep the proof opening through the definition

    B=HF_X-H'F, I=(F_u,B) subset k[X,u].

Replace everything from `First suppose $I$ is zero-dimensional` through the paragraph ending equation `eq:cubic-root-bank-bound` (immediately before `\emph{Positive-dimensional critical loci.}`) with:

```tex
If $I$ is zero-dimensional, including the unit-ideal case,
Theorem~\ref{thm:general-first-integral-zero-dimensional} with $b=3$
gives the asserted bound directly.  Its characteristic hypothesis
$p>3$ follows from the present one.  We therefore assume that $I$
has a positive-dimensional component.
```

The following existing sentence `We next treat the case excluded above.` can be removed as redundant. Keep every substantive part of the positive-dimensional analysis unchanged, including the p>2D Frobenius root-budget argument, irreducible quadratic critical-component argument, repeated-fiber classification, and genus-three cover proof.

## Exact replacement 2

After `This completes the positive-dimensional case.`, delete the entire final subsection starting `\emph{From the total-bank bound to arbitrary received words.}` through the sentence `All preceding small-bank and affine-family cases satisfy the same bound.` Replace it by:

```tex
The bounds obtained in this case---at most $3/\eta$ in the Frobenius
case, at most $1/\eta$ for an affine family, or a bank of at most eight
sections---are all bounded by the stated expression.  This completes
the proof.
```

Keep `\end{proof}` and the complete following Dickson-family distinction unchanged. The cubic theorem label `thm:weighted-cubic-first-integral-list` and all introduction references remain unchanged.

## Label and scope checks

The removed labels eq:cubic-critical-length, eq:cubic-critical-correction, eq:cubic-infinity-cost, and eq:cubic-root-bank-bound occur only inside the material being removed; repository search found no outside references. New labels are thm:general-first-integral-zero-dimensional, eq:general-critical-length, eq:general-critical-correction, eq:general-root-bank-bound, and cor:general-first-integral-repeated-fiber.

The new theorem assumes D>=1. The existing cubic proof already handles D=0 before the proposed reference, so this is compatible. The original cubic proof's N<=3D reduction remains in place and is used by its positive-dimensional classification. Do not replace that classification by the coarser general repeated-fiber corollary: the latter needs p>b(b−1)D and does not classify repeated fibers.

The input and cubic-proof replacements below have now been applied, built, and visually inspected. This consolidation replaces the old zero-dimensional proof rather than retaining both versions. The new draft attributes no novelty priority; its scope is the stated first-integral section class, not arbitrary differential equations or all Reed–Solomon codewords.

Applied and verified: general theorem R.7, repeated-fiber corollary R.8, cubic theorem R.9. The rebuilt article has 193 pages. The instructions above document the consolidation that was performed.
