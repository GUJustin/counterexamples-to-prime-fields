# Independent rank and second-order obstruction audit

PASS. The independent verifier uses F3[t]/Phi7(t^3-t), rather than the solver's tower multiplication tables. It reconstructs the eight polynomials U^2 P_i(U^3-U), all 42 distinct nonzero core nodes and exact masks, the six cube halfsets, all 192 Jacobian rows, and the mixed-characteristic defect. All saved data agree.

The 28 saved tangent vectors annihilate this reconstructed Jacobian. Their free-coordinate submatrix is the identity, proving independence. Separately, an independently reconstructed 164-by-164 minor has nonzero determinant with univariate field encoding 227346939. Hence rank is exactly 164 and the tangent basis is complete.

The saved unramified obstruction annihilates the Jacobian and pairs nontrivially with the defect. For the second-order test, the verifier lifts the saved projected separator through the saved left-kernel vectors to an incidence functional lambda. It checks directly that lambda J=0 and lambda defect is nonzero.

Most importantly, it evaluates every one of the 406 quadratic coefficients on the FULL 28-dimensional tangent basis, using

    Q_ij(v) = F_i^[2](T_j) xi_j^2 + R_i'(T_j) xi_j.

Every coefficient of lambda Q is zero. This avoids any reliance on gauge-quotient invariance or on the twelve-dimensional complement being selected correctly. Thus J correction + Q(v) = defect has no solution, even over an algebraic extension of the residue field. Multiplying the defect by a nonzero unit does not change the obstruction.

Consequences: unramified mixed-characteristic lifts and ramification-index-two lifts through this specified special point are excluded. Arbitrarily distinct marked-node velocities do exist in the tangent space, but fail this mixed-characteristic lifting test. No assertion about higher ramification or all special points follows.

Artifacts: `verify.py`, `verify.json`, `verify_quadratic.json`, `minor_input.py`, `rank_minor.in`, and `verify_minor.json`. The minor verifier reuses the already independent univariate C++ arithmetic in `../char3_deformation/verify_minors.cpp`, unchanged. Python replay completed in 8.95 seconds, peak RSS 82048 KiB, under 60 seconds/384 MiB. The minor replay completed in 0.54 seconds; its shell-wrapped watchdog receipt does not reliably measure child RSS.
