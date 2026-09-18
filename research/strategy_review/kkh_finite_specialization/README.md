# Direct finite specialization of KKH Appendix A

Scope: the unconditioned subset-bank quotient construction in Appendix A of Krachun–Kazanin–Haböck, ePrint 2026/782, not an upper bound on all constructions inspired by that paper. Primary text read from the restored research archive on September 18, 2026.

Set n=262144, strict dimension k=131072, target agreement A=139782. Let s divide n, m=n/s, and use r-subsets of the subgroup of order s. The displayed Appendix A construction produces quotient witnesses of degree at most (r−2)m and agreement rm. Thus its uniform degree guarantee requires

    r <= floor((k−1)/m)+2.

For s<n, m>=2 and s even, the largest permitted r is s/2+1. Consequently the maximum guaranteed agreement is n/2+n/s. To reach A requires n/s>=8710. Since s is a power of two, this forces s<=16. At s=16, r=9 and the entire subset bank has only C(16,9)=11440 members. For s=n, agreement is only k+1=131073, below target. The smaller s cases are checked exactly in check.py/json.

Therefore even granting injective quotient labels for the entire bank, this literal specialization falls far short of the required 274980728111395088 labels. Passing to the sextic alphabet can improve separation of existing labels; it does not enlarge this bank. This is a finite tradeoff between agreement and bank cardinality, not a failure of KKH's inverse-logarithmic asymptotic theorem.

The maximum-bank assertion here concerns the displayed uniform degree guarantee. Special coefficient cancellations can lower actual degrees for selected supports; exploiting them creates the conditioned coefficient-fiber problem already under investigation. The conclusion does not rule out such conditioning, alternative denominators, multi-row constructions, or a new compiler. In particular, it does not supersede the much closer B1024 conditioned packet guarantee.
