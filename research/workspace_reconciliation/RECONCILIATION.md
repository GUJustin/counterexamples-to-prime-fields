# Audit-workspace and published-paper reconciliation

Observed 2026-09-15T18:05:16.118528-04:00. Baseline: published commit `d2dfaa3a40e2f57004152bfc07db1ecf0813da25`.

## Located branch

The user's quoted 32-page draft is `/Users/jthaler/Documents/stwo_audit_2026-09-15/paper/main.pdf`.
Its Dropbox copy is `/Users/jthaler/Dropbox/Stwo_Research_Draft_2026-09-15.pdf`.
They have identical SHA256 `84577fd2e73eaaf531197346f52c6637e95ad48ecaf374a48f93219f17cffa67`.
The Dropbox `.tex` is zero bytes; the modular sources remain present. See
`inputs.json` for hashes, sizes, and modification times.

The modular PDF was written at 17:51:41 EDT; its last main/core source edit
was at 16:35:29 EDT. A later PDF timestamp is not evidence of newer mathematics.
All theorem/section labels found in that branch's `.tex` files already occur
in the repository source. This is a structural cross-check, not a proof that
every line of prose is identical.

## Communication status

`companion_review/PAPER_SYNC_STATUS.md` already recorded the published 57-page
checkpoint at 18:00:05 EDT. No acknowledgment from the independent audit session
was observed. This pass added a prominent root `CANONICAL_PAPER.md`, a copy beside
`paper/main.tex`, and a README pointer. The original status history and all
research notes were preserved. These are shared-file coordination records;
they do not prove the other session read the handoff.

## Agreement-count referee note

`agents/paper_referee_note.md` changed “exactly” to “at least” in two introductory
claims, reasoning that extra roots might exist. The canonical source explicitly
proves exactness: if `P_A=W-F_A` and `F_A=product_(a in A)(X-a)`, then
`W(x)-P_A(x)=F_A(x)`. Over a field this product is zero precisely for `x in A`.
The evaluation points are distinct because `p>n`. Thus its informal theorem,
34-point example, and finite-list lemma may retain “exactly.” The narrower
actual-list result also separately proves its full-list classification.
No mathematical weakening is needed to resolve that referee note.

## Other reported conclusions

The audit synthesis records the saved better.codes incumbent as 139,775
agreements / 116.13 displayed bits, with 139,782 agreements needed for 116.12
plus a complete unsafe-radius suffix. Its bounded searches found no improvement;
this is not an impossibility theorem. These are saved local research conclusions,
not a fresh verification of the live contest leaderboard.

Its statement that both quantitative premises fail needs the qualifiers already
retained by the canonical draft: the numerical list coefficient, selected-witness
versus correlated-agreement definitions, and fixed-gap versus shrinking-gap
families differ. The modular quantifier note's familywise-sublinear qualification
already appears in the canonical application discussion.

The separate privacy report and its qualifications are being handled as a distinct
defensive document. This reconciliation did not execute protocol experiments,
reproduce witness extraction, or establish fixed-verifier acceptance or a real
Fiat–Shamir distribution result.

## Preservation decision

Keep the integrated repository as the manuscript baseline. Preserve the modular
branch as source material and its nonduplicative research notes. Do not replace
the repository paper with the shorter branch. Repairing the empty Dropbox source
should use a verified source snapshot, not the zero-byte artifact.

## Subsequent handoff and source repair

The frontier root later acknowledged authorship of the concurrent Gram/ellipsoid/
Gaussian additions in the repository `INTEGRATION_HANDOFF.md` at 18:11:07 EDT
and yielded canonical-file and Git ownership to the integrating root. This
supersedes the earlier observation that authorship was unidentified.

At 18:14:28 EDT, the empty historical Dropbox source was repaired from the
matching audit modules. Its temporary standalone build produced 32 pages and
byte-identical extracted text to the preserved PDF. See
`historical_source_repair.json` and `HISTORICAL_SOURCE_REPAIR.md`. The initial
empty-file observation in `inputs.json` remains an accurate historical record.
