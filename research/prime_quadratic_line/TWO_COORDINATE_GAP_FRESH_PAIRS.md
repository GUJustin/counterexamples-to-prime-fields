# Two-coordinate gap by pairing only the fresh domain

This positive construction leaves the original quadratic core unchanged. It improves the loss from a whole-domain double pullback and attains the fresh-incidence bound M=L n_fresh/2 exactly.

Use the original core bank P_i(X)=X²/a_i²+a_i², with N₀=L(L−1) distinct nodes ±a_i a_j and core agreement A=2L−2. Set

    t=(L²+L+2)/2, n=N₀+2t=2L²+2, T=A+2=2L.

Append t disjoint pairs {x,−x}, outside the core and zero. Put f=x⁴ and g=x⁶ on the fresh domain, and retain f=core word, g=0 on the core. The incumbent label is

    λ_i(x)=(P_i(x)−x⁴)/x⁶.

It is even. Choose the pairs greedily so that all tL labels indexed by (i,pair) are different and avoid 0 and 1. This is possible over every sufficiently large prime field: each prescribed label equation P_i−X⁴−λX⁶ has degree at most six and is nonzero (for λ=0 its leading quartic coefficient is −1). For λ≠0 it has degree six. At a fixed new point, two incumbent labels coincide only on the excluded core. At step j<t, the total forbidden-point bound is

    N₀+1+2j+12L+6jL².

Take p>2 max_i a_i² and larger than this bound for j=t−1. This preserves the distinct core and ensures a choice at every step. Both roots of each selected pair are distinct because p is odd.

Each of the M=tL finite exceptional labels has exactly T matches with its unique incumbent. Other incumbents have exactly A. Every nonbank quadratic has at most L core matches and at most six fresh matches, since f+λg−h is a nonzero polynomial of degree four or six on the fresh domain. For L≥8, L+6≤A, proving both completeness and singleton threshold lists. All other finite labels have agreement exactly A.

For common agreement, a nonzero quadratic G explaining g has at most two core zeros and at most six fresh matches with X⁶, hence at most eight simultaneous matches. G=0 is supported only on the core and gives maximum A. Thus CA(f,g)=A for L≥8. Avoiding labels 0 and 1 makes both f and f+g individually have agreement A.

Set F=f and G=f+g. For z≠−1 the label change is λ=z/(1+z), so the M finite exceptions remain distinct, nonzero, and singleton. At z=−1 the word is −g. Its zero candidate matches all N₀ core nodes; every nonzero quadratic matches at most eight coordinates. Consequently infinity contributes exactly one further singleton threshold list. Both endpoint agreements and common agreement are exactly A, a two-coordinate gap below T.

The tested threshold remains strictly below exact Johnson:

    T²=4L²=2n−4.

For L≥25 the usual low-rate first-order estimate gives

    n a₁(3/n) ≤ sqrt(3n/2)+3^(1/4)n^(1/4)/2^(3/4)
                 < (7/4)L+sqrt(L) < 2L=T.

Finally M=L n_fresh/2 exactly, and (M+1)/n^(3/2) tends to 1/(4 sqrt(2)). At gap two this is a factor sqrt(2) better than pulling back the whole gap-one construction by a quadratic map. The rate and normalized gap still vanish. This note makes no claim for arbitrary growing gap d.
