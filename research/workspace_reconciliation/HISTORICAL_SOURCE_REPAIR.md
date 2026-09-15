# Historical 32-page source repair — 2026-09-15T18:14:28.051098-04:00

The zero-byte Dropbox `Stwo_Research_Draft_2026-09-15.tex` has been repaired by
recursively inlining the five local modules of this workspace's `paper/main.tex`.
A temporary standalone build passed and produced 32 pages. Its complete
`pdftotext -layout` output matches the preserved Dropbox PDF byte for byte.
The saved PDF itself was not changed. The empty destination was checked again
immediately before writing.

Repaired source SHA256: `fcbb681e3a97e6af999a196be4cfff61553ad42f93778695a50fd7e461a9a9d0`.
Preserved PDF SHA256: `84577fd2e73eaaf531197346f52c6637e95ad48ecaf374a48f93219f17cffa67`.

This repairs a **historical 32-page checkpoint**. The current integrated paper
remains https://github.com/GUJustin/counterexamples-to-prime-fields and local
`/Users/jthaler/Documents/counterexamples-to-prime-fields/paper.tex`.
The shorter draft is not the latest manuscript.
