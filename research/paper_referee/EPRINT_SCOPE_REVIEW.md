# ePrint scope and length review, September 16 evening

User direction: full-page article with one-inch margins, not LNCS.
The separate submission/ draft is shelved. Preserve the full manuscript;
the user has asked about its length but has not instructed removal of
specific results.

## Verified history

PDF page counts read directly from the Git objects:

| Commit | UTC time | Pages |
|---|---|---:|
| 73d4661fc8 | 2026-09-16 13:07 | 71 |
| 656066069c | 2026-09-16 13:43 | 74 |
| 776da63d1a | 2026-09-16 14:41 | 77 |
| 2f787e45a2 | 2026-09-16 15:17 | 79 |
| c9b2f08bf9 | 2026-09-16 17:23 | 86 |
| c9574712c0 | 2026-09-16 18:06 | 92 |
| 887653470c | 2026-09-16 19:05 | 101 |
| 540a9853b2 | 2026-09-16 19:44 | 104 |
| 748302f606 | 2026-09-17 02:51 | 109 |

The 104-page GitHub version predates this laptop continuation. The
109-page build has 48 pages before the appendices, 59 appendix pages,
and 2 reference pages. These are pagination observations, not a claim
that the material is equally central. Subsequent builds may shift pages.

The separate LNCS draft has 19 main-text pages and 22 total pages.
It is an abridgment with unfinished supporting material, not a
109-to-19-page editing improvement. No part of the full manuscript was
deleted to make it.

## Dependency map for an editorial decision

1. Core list counterexamples: equal-moment construction, growing-moment
   estimates, strict Elias check, and rate/gap/field quantifiers. Required.
2. Core line counterexamples: rational division, collision counting,
   logarithmic-length all-large-prime theorem, anchored fixed-gap lift,
   and actual-list separation. Required. The preliminary unanchored
   fixed-gap construction is useful exposition but has weaker scope than
   the anchored theorem; it must not be substituted for that theorem.
3. Finite circle claims: both circle-space constructions and the exact
   numerical inequalities supporting the stated parameters. Required
   whenever those concrete claims remain in the abstract and application.
4. Finite interval certificate refinements: support the strongest concrete
   numbers. Earlier weaker certificates can be presented more compactly,
   but their removal requires checking later dependencies rather than
   merely deleting paragraphs mentioning smaller numbers.
5. Raw quotient calculations: distinct from the pure coding theorems.
   Do not expand archived implementation/exploit workflows. Retain the
   distinction between coding counts and complete-protocol conclusions.
6. Construction barriers and differential-equation results: independent
   additional research toward the open fixed-gap question, not premises
   of the main list/line disproofs. Potential companion-note material if
   the author wants a narrower paper. No removal is authorized by the
   current formatting correction alone.

Immediate editorial change: explicitly distinguish the last group in the
introduction's organization paragraph. Keep all mathematical sources and
proofs in the full ePrint draft while the author considers scope.
