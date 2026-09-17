# Target scalar-list arm: exact seedless repair

At agreement181275, the practical replacement is multiplicity117, seedless total cap161, slope cap35, and weighted cutoff21209175=117*181275.

The exact seedless coefficient count is49731373644; the seedless local-rank bound is189708. With n262144, the kernel dimension lower bound is559692>0. These are the RCN279/RCN285 seedless formulas, not the larger seed-dependent source counts.

The list argument gives capY42204863 and capR9043899. Its exact numerator is384468854750148, and gap50204. Therefore listBudget7658131917 satisfies the required strict inequality, with slack10920. This increases the previous listBudget7561644282 by96487635.

All numerical side gates hold: 0<slopeCap<2130706433, total cap and w below the characteristic, positive weighted cutoff, w<agreements<=n, and D=m*agreements. The list proof needs only the positive seedless kernel gate and these degree/characteristic conditions; no large-nullity obstruction is involved. The seedless fourth-variable degree remains zero.

The bounded search checked30888 tuples: m95..160,s20..55, and total capY in[floor(mA/w)−12,floor(mA/w)], withY>=s. The displayed candidate minimizes the resulting list budget in that bounded search. No global optimum is claimed.

The code evaluates the exact defining seedless box counts, including truncated total-degree diagonals, and independently reproduces the incumbent coefficient47864396310,rank182580,nullity2144790. The old shape's target surplus is-3164760. Resource use was2.82seconds and below19MiB under the384MiB/60second guard.

Files: scalar_list_repair.py/json/resources. Root owns updating the protocol allowance after subtracting this new scalar-list budget. This arithmetic is not a Lean port/build or a completed improved protocol certificate.
