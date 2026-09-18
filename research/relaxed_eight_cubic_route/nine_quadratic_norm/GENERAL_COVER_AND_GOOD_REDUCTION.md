# General quadratic covers and a good-reduction lifting consequence

Research note. The finite system census has now been independently replayed in a separate reversed-variable C++ implementation: all4,794,411 refined systems and the literal733 norm vectors agree. See INDEPENDENT_CENSUS_AND_LIFT_AUDIT.md and independent_census.verified.json. Python additionally replays every saved norm and its factor-multiplicity classification.

## Correct input threshold

The residue word on18 nodes over F289 has exactly9 quartics with at least8 matches. Seven have8 and two have9. These are the known9 candidates; the maximum is9, not8. Hence any fresh descended quartic has at most7 matches. The selected characteristic-zero incidence lift retains8 prescribed matches per candidate, even where the special fiber has one accidental ninth match.

## Why the binary norm test covers every separable quadratic map

Work over an algebraically closed field of characteristic17. Let pi:P1_T -> P1_Y be any degree-two map unramified over the18 source nodes. The degree-eight section space is H0(pi*O(4)). The deck involution decomposes it into invariant sections E in H0(O(4)) and anti-invariant sections O sqrt(B2), where O is a binary cubic and B2 is the squarefree binary quadratic defining the branch divisor. Equivalently pi_*O_P1 = O plus O(-1), and tensoring by O(4) gives O(4) plus O(3). The received values on the two lifts are interpreted in the corresponding pulled-back section trivializations.

For a section with nonzero anti-invariant part, a fully matched fiber requires O(x)=0. Therefore there are at most3 full fibers. Its norm relative to the received value w is

    w²+B4(Y)w+C8(Y),  B4=-2E,
    J8=E²-C8=B2 O3².

The binary form J8 consequently has odd-multiplicity divisor of degree exactly2. This statement includes a branch point at infinity, degree drops in affine J, and arbitrary nonmonic affine branch equations. It is stronger than the polynomial-cover form J=(Y-c)O² but is precisely what the original weak filter tests.

The linear norm conditions at hit/full fibers depend only on B4,C8, not the branch map. Thus the same f=0..3 enumeration covers every non-descended section with at least15 matches for ANY such quadratic map. All consistent systems are zero-dimensional affine linear systems over F289, so their unique solutions are already in F289; extension-field coefficients cannot create additional solutions.

The733 saved norms have the following independently recomputed affine degree / finite odd-factor degree distribution:

    (8,0):658; (6,0):44; (4,0):2; (2,0):1;
    (8,6):17; (7,5):1; (8,8):6; (8,4):4.

Add (8-degree J) modulo2 to include infinity. Thus705 have binary odd degree0 (nonzero squares) and28 have binary odd degree4,6,or8. None has binary odd degree2; none is zero. Python also rechecks every norm's hit/full-fiber equations and verifies agreement-count coverage h+min(f,3)>=15. Therefore the fixed residue word admits no NON-DESCENDED degree-eight section with15 matches on any separable quadratic cover unramified over the marked nodes. Descended sections with15 matches must arise from one of the known9 base quartics, since they have at leastceil(15/2)=8 base matches.

This is an algebraic-closure assertion for the fixed residue source, not only for F289-valued quadratic maps.

## Good-reduction lifting lemma

Let R be a complete DVR of mixed characteristic(0,17), permitting arbitrary ramification and residue extension. Suppose:

* the source18 marked sections and word values are integral and specialize to the archived residue word, with distinct reductions;
* nine degree-four sections P_i lift the known candidates and retain their selected8 source incidences;
* pi:P1_R -> P1_R is a degree-two morphism with good reduction, whose special fiber is separable and unramified over the18 marked nodes;
* after a finite extension all36 lifted nodes split and have pairwise distinct reductions.

Then every degree-eight section Q agreeing with the pulled-back word at15 or more marked nodes is one of the nine sections pi*P_i.

Proof. Choose a cover-parameter coordinate chart with infinity away from the36 residue nodes (enlarging the residue field if needed). Nine actual agreements interpolate Q through integral values at unit-separated nodes; the unit Vandermonde determinant implies integral coefficients. Consequently Q reduces to a degree-eight section with at least15 residue agreements. By the finite general-cover assertion it is the pullback of a known residue quartic P_i.

Let S be any15 actual agreement indices of Q. Let T be the16 selected actual agreement indices of pi*P_i. Both are subsets of U, the RESIDUE agreement set of pi*P_i, because reductions of Q and pi*P_i coincide. The archived decoder gives |U|<=18. Hence

    |S intersection T| >= 15+16-18 =13 >8.

The two degree-eight sections therefore agree at more than8 distinct generic-fiber points, so they are identical. This proof uses the small residue support U, not the36-point ambient domain. It works equally for the two residue candidates with accidental ninth base matches and the other seven candidates. It requires no assumption that the characteristic-zero base list is complete.

The lemma excludes fresh15-match candidates for quadratic covers WITH THESE GOOD-REDUCTION HYPOTHESES. It does not exclude covers with coalescing domain nodes, branch points specializing to marked nodes, degeneration of the map's degree, or other bad reduction. Those are genuine remaining charts. No all-covers characteristic-zero claim follows from this note.
