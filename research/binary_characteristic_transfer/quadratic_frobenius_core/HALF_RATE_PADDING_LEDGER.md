# An exact half-rate transformation, with its remaining gap limitation

September 18, 2026. Research only; no manuscript changes. This uses the
quarter-density theorem as currently stated in `density_quarter_puncturing.tex`
and the already-audited conjugate-avoiding padding lemma in
`../../prime_quadratic_line/TRANSLATED_GRID_RS_TRANSFORM_AUDIT.md`, Section 3.
The distinct full-domain locator construction in
`../GROWING_CHARACTERISTIC_FULL_DOMAIN_PADDING.md` was also checked first:
it already gives fixed rate, but its fractional gap vanishes and it does not
turn this quartic, dimension-three bank into a constant-gap result.

For a prime \(p\ge257\), the present seed has

\[
 n_0=(5p^2-1)/2,\quad k_0=3,\quad A_0=2p,
 \quad T_0=\lfloor\sqrt{5p^2-2}\rfloor,
 \quad B=(p+1)(p^2-1),\quad q_0=p^4.
\]

The endpoint and common agreements are exactly \(A_0\); all \(B\)
specified nonzero-plane labels have singleton lists at \(T_0\).

There is a rigorous transformation to **exact rate one half**, preserving
these labels and exact far-source agreements for the full enlarged RS code.
Append a total of \(t=n_0-6\) common-root padding coordinates in blocks
of size at most \(h=2p-2\). At each block replace the current field \(K\)
by its quadratic extension, choose roots outside \(K\) disjoint from their
Frobenius conjugates, multiply both words and old witnesses by their locator,
and put zero at the new coordinates. The resulting ledger is

\[
 \begin{aligned}
 N&=5p^2-7,& K_{
m dim}&=N/2,\\
 A'&=n_0-6+2p,& T'&=n_0-6+T_0,\\
 B'&\ge B,& q'&=p^{4\cdot2^L},
 \end{aligned}
 \qquad
 L=\left\lceil\frac{n_0-6}{2p-2}\right\rceil.
\]

Here \(B'\ge B\) means the old certified singleton labels survive; newly
available labels in the enlarged field are not classified. In particular,
the certified count remains \(\Theta(N^{3/2})\).

The padding lemma controls **every** new witness. If a witness misses
\(u\) padding roots, divide out those it matches. On old coordinates it
becomes a rational function with numerator degree less than \(k+u\) and
denominator degree \(u\). Its conjugate has the same values wherever it
matches the old word. At the near threshold, the conjugate cross difference
has degree less than \(k+2u\) and at least \(T+u\) roots. The inequality
\(u\le T-k\) forces it to vanish. Disjoint conjugate pole sets then force
the rational function to be a polynomial of degree less than \(k\).
The same argument excludes more than \(A+h\) endpoint agreements when
\(u\le A-k+1\). Both allowances remain unchanged by each padding block:

\[
 A-k+1=2p-2,\qquad T-k=T_0-3\ge2p-2.
\]

Thus each block preserves the exact endpoint/common agreement and the old
threshold lists. This is not an assertion only about the subcode of
locator-multiplied old polynomials.

The achieved scaling falls short of the requested constant fractional loss:

\[
 \frac{T'-A'}N=rac{T_0-2p}{5p^2-7}
 \sim\frac{\sqrt5-2}{5p}\longrightarrow0,
 \qquad
 \frac{T'-A'}{T'-K_{\rm dim}}
 =\frac{T_0-2p}{T_0-3}
 \longrightarrow1-\frac2{\sqrt5}.
\]

The second ratio is a constant **relative to a vanishing capacity margin**.
It is not a constant absolute fractional proximity gap. Moreover,

\[
 \frac{T'}N=\frac12+\frac{T_0-3}{N}<\frac23
 <a_1(1/2)=\frac{1+\sqrt6}{5}.
\]

For the first strict inequality use \(T_0<(5/2)p\) and
\(15p-18<5p^2-7\) for \(p\ge3\). Thus this exact rate-raising
construction loses first-order placement. Its extension degree is also
\(4\cdot2^{\Theta(p)}\), rather than four, and the new message degree
exceeds the characteristic.

For the finite seed \(p=257\), the ledger is

\[
 (n_0,A_0,T_0,B)=(165122,514,574,17040384),
\]
\[
 (N,K_{\rm dim},A',T',L)=(330238,165119,165630,165690,323).
\]

The absolute fractional gap is \(60/330238\), while the
loss-to-capacity-margin ratio is \(60/571\). The alphabet is
\(257^{4\cdot2^{323}}\). No such huge field was instantiated.

Even granting an ideal full-fiber pullback of multiplicity \(M\), followed
by arbitrary exact common-root padding, its fractional source-to-near loss
would be

\[
 \frac{M(T_0-A_0)}{Mn_0+t}\le\frac{T_0-A_0}{n_0}=\Theta(1/p).
\]

This inequality is deliberately favorable to the transformation: it does
not claim the quarter-density seed's complete lists automatically survive
arbitrary non-composed RS witnesses. Holding \(p\) fixed instead keeps a
positive fractional gap, but leaves the inherited label population fixed
while length grows.

**Bounded outcome:** an exact all-witness half-rate transform exists, but it
does not satisfy the requested gap or alphabet scaling. The missing step is
a new source/support identity that supplies \(\Omega(N)\) extra agreements
over the actual far-source maximum at fixed rate, together with a count of
superlinearly many scalar labels. Neither the existing bank nor its ordinary
padding ledger supplies that amplification. No further standard-transform
survey or quintic scan is needed for this assessment.

`verify_half_rate_padding.py` and `half_rate_padding_receipt.json` record the
exact finite arithmetic; the all-witness proof is the descent argument above.
