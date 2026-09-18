# Independent uniform finite DKT certificate for the projected quadratic line

September 18, 2026. **PASS for every prime p≥5**. Primary formulas are DKT ePrint 2026/2056, Proposition 5.10/Eqs. (60)--(64), Lemma 5.6/Eqs. (54)--(56), and ordinary tail Eq. (38), as cached in this repository. This audits the finite substitution and its characteristic assumptions, not the entire primary theorem.

Set N=2(1+p+p²+p³+p⁴), K=3, d=2, A0=2p²+p, B=2A0=4p²+2p, m=4, derivative cap M=2, and H=116B.

## Interpolation

Since mA0=2B, the coefficient count is exactly

    G=sum_(t=0)^B sum_(v=0)^min(t,2) (2(B-t)+v)=3B².

The four local-rank layers are 3,6,8,6, totaling an upper bound of 23. Only t≤5 contributes; the specialization cutoff holds for these terms. This is a rank upper bound valid in all characteristics, not an assumption that all Pascal minors remain nonzero modulo p.

The uniform source margin follows from the exact identity

    5G-116N
     =8(p-5)^4+168(p-5)^3+1148(p-5)²+2648(p-5)+308>0.

Therefore G>(116/5)N, and the graded row test follows from

    (H-B+1)G>(115B+1)(116/5)N>(116B+1)23N.

Proposition 5.10 is characteristic-uniform. Reconstruction/counting only requires p>max(d,M)=2. In particular B>p is harmless.

## Exact counting parameters and safe bounds

The primary definitions give

    tau=1, u=B, v=3,
    Freg=5B-6, S=3B-4, Hs=348B,
    J1=H(16B-21)+10B-12≤1866B².

Choose L=L0=floor(A0/2)=(B-2)/4; here p is odd. Since B≥110 and B≤N,

    lambda=(N-2)/(A0-2)≤3N/B,
    (N-L+1)/(A0-L+1)≤4N/B,
    (N-2)/(L-2)≤8N/B.

The list bound is at most 15N+3B≤18N.

For d=2, Psi_d(S)=8S-12≤24B. Eq. (38) is consequently at most

    2088B²+33411NB+12N≤35511N².

The regular joint-family term in Eq. (55) is at most

    (4N/B)(3N/B)(1866B²)=22392N²,

and the regular accidental-agreement term is at most

    N(8N/B)(5B)=40N².

Thus the full-agreement-set MCA exceptional count is at most 57943N², which certifies the proposed conservative bound **75000N²**. There is no need to change the manuscript constant merely to use this slack.

## Quantifiers and independent replay

These upper bounds apply to every received word and every affine received line on any N distinct evaluation points in the characteristic-p field, with the stated message dimension and agreement threshold. They are not inferred from the special lower-bound construction. The exceptional-count notion is the primary full-agreement-set MCA recovery notion.

`verify_projective_finite_independent.py` directly rebuilds the source coefficients, local-rank bound, graded test, and exact rational primary counting expressions for p=5,7,11,53,101. All five pass; the JSON records exact margins and budgets. The polynomial identity and inequalities above supply uniformity, rather than the finite sample.
