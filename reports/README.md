# S-two zero-knowledge disclosure summary

[Read the report](stwo-zk-disclosure-summary.pdf) · [LaTeX source](stwo-zk-disclosure-summary.tex)

This is a disclosure summary derived from the September 15 saved privacy-blinding report. It covers the finding, reported evidence, impact, remediation, and unresolved fixed-verifier and Fiat–Shamir questions. It omits the recovery procedure and executable artifacts. The original report remains in Dropbox.

Build from this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error stwo-zk-disclosure-summary.tex
```

The source report describes exact algebraic checks. Preparing this summary did not rerun those experiments or a native verifier.
