# Constructive scaled-fiber identity: p-cubed distinct labels

The requested structured fresh padding succeeds. See `scaled_fiber_padding.tex` for a self-contained theorem/proof fragment (not a main-paper edit).

Over B=F_(p²), E=F_(p⁴), choose eta=s² outside B. The core has x² in B*, f=x^(2p), g=0. The fresh block has x² in eta B*, f=eta*(x²/eta)^p, g=1. Both blocks have 2(p²−1) points and are disjoint.

For norm-one a, put I_a=Im(y^p−ay), an F_p-line in B. The bank is Q_(a,b)=aX²+b, b in I_a. On the core, b!=0 gives 2p matches. On the fresh block, the received word f+lambda*g agrees at 2p points precisely when

    lambda=b−eta*v,   v in I_a minus {0}.

Restrict b!=0 too. Because 1,eta form a B-basis of E and the p+1 lines I_a are distinct, every such lambda identifies a,b,v uniquely. This gives exactly (p+1)(p−1)² DISTINCT labels, not p³ witness-label pairs collapsing onto fewer labels.

Unscaled translated B fibers would fail here: both b and the fresh image variable would run along the same F_p-line, causing collisions. Scaling outside B turns these into independent coordinates. This is the constructive point absent from that naive model.

The raw two-block length is too short for the desired below-Johnson threshold. Append 5p²+4 neutral points, with f=X³,g=0, avoiding roots of X³−Q for every core bank word. The final length is 9p² and threshold 4p. Field availability follows from p⁴>=12p²+3p. Bank words gain no neutral matches; all other quadratics gain at most three. The complete classification in PROOF.md then gives exactly the asserted singleton labels. Two far source endpoints exist outside the union of the p+1 label planes. After the usual invertible source change there is one extra exceptional parameter with a two-element constant list.

For p>=41 this is above the finite first-order curve and below exact Johnson, in characteristic p=√N/3>K−1=2. Source and common agreement are at most 2p+3; therefore their gaps to 4p are at least 2p−3. The field is an extension, not a prime field. Rate tends to zero. Compared with the earlier projectivized p^5 locator example, the exponent M=Theta(N^(3/2)) is unchanged, but characteristic is now Theta(√N), ambient size is Theta(N²), and the source gap remains Theta(√N). No optimality claim for general first-order proximity bounds is made.
