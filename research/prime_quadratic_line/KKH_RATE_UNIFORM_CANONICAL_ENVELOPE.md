# A rate-uniform envelope for the basic KKH canonical bank

Date: 2026-09-18. Pure coding-theory parameter audit; no manuscript changes.

**Conclusion.** In the basic KKH full-fiber construction, write

\[
 n=sm,\qquad k=(r-2)m+1,\qquad T=rm,\qquad 2\le r<s.
\]

Here \(k\) is the **message dimension**, and the number of canonical subset
witnesses is \(M=\binom{s}{r}\). If \(s\ge16\) and
\(T/n>a_1(k/n)\), then \(M<4n\), for arbitrary positive integers \(s,m\).
When \(s,m\) are powers of two, as in the primary construction, the stronger
bound \(M<2n\) holds, including the remaining small values of \(s\).
Thus shrinking the rate or distance cannot make this canonical bank enter the
first-order window with a superlinear number of labels. This is an upper bound
on the number of labels supplied by the canonical subsets, **not** an upper
bound on every nearby label or every possible witness on the received line.

The same conclusion applies if the code is enlarged or the tested agreement is
lowered: if \(k'\ge k\), \(T'\le T\), and
\(T'/n>a_1(k'/n)\), monotonicity implies \(T/n>a_1(k/n)\).

## Primary sources and exact ledger

Krachun--Kazanin--Haböck, [*Failure of proximity gaps close to
capacity*](https://eprint.iacr.org/2026/782), Section 2.1 and Appendix A,
equations (5)--(6), explicitly use degree cap \((r-2)m\), not dimension
\((r-2)m\). The primary cached text read for this audit is

`/Users/jthaler/Dropbox/Documents-full-2026-09-16/Documents/stwo_audit_2026-09-15/sources/actual_list_literature/kkh2026_782.txt`

with SHA-256
`de6e244b8e7d86c88b133a0f85bfacb76c460b4de5e38cd58c6b8f6293599d78`.
Appendix A has \(s,n\) powers of two and \(m=n/s\). It uses binary entropy
\(c=H_2(\rho)\) in \(\eta\sim c/(\tau\log n)\).

The first-order curve is equation (31) of the cached DKT source
`tmp/eprint-2056/paper.txt`; its definitions use rate \(k/n\) for degree-\(<k\)
messages. The original source is [ePrint 2026/2056](https://eprint.iacr.org/2026/2056).
This note compares exact finite parameters to that curve. It does not claim
that mere placement above the curve is an independent finite interpolation
certificate.

Let \(G\) be the \(s\) distinct tags, and suppose every tag has an
\(m\)-point power fiber in the domain. Put \(Y=X^m\). The canonical locator
\(V_S(Y)=\prod_{a\in S}(Y-a)\), \(|S|=r\), supplies exactly \(rm\)
agreement coordinates. Both the direct two-head pencil and the Appendix A
quotient have witness degree cap \((r-2)m\). Their direction has exact
agreement cap

\[
 A=(r-1)m.
\]

For the quotient direction \(1/(Y-b)\), the upper bound follows after clearing
the denominator; it is attained by interpolating on any \(r-1\) full fibers.
Both received words can be interpolated on those same fibers, so the common
agreement is also exactly \(A\). This does not assert that both particular
source words are individually far. The canonical loss-to-capacity-margin
ratio is

\[
 \frac{T-A}{T-k}=\frac{m}{2m-1}.
\]

The envelope below already fails the desired superlinear count while retaining
this constant ratio; no asymptotic prime-existence hypothesis is needed.

## Curve facts

Write \(\rho_c=11-3\sqrt{13}<3/16\). For \(0<\rho<\rho_c\), put
\(b=\sqrt{\rho/2}\), and let \(u>0\) solve
\(u^2(u+3)=b\). Then \(a_1(\rho)=b(1+u)\). For
\(\rho_c\le\rho<1\),

\[
 a_1(\rho)=\frac{3\rho+2\sqrt{\rho(5-\rho)(2-\rho)}}{8-\rho},
\]

the unique positive root of

\[
 F(a,\rho)=(8-\rho)a^2-6\rho a+\rho(4\rho-5).
\]

The curve is strictly increasing. The low branch is increasing directly; on
the high branch \(a_1>\rho\), \(F_a>0\), and
\(F_\rho=8\rho-a^2-6a-5<0\). The branches meet continuously. Also

\[
 a_1(\rho)>\sqrt{\rho/2}\qquad(0<\rho<1).
\]

For the high branch this follows from
\(F(\sqrt{\rho/2},\rho)=\rho(7b+1)(b-1)<0\); for the low
branch it is immediate. In every use of the high-branch polynomial below,
the supplied rate is checked to be in that branch.

## Interior ranks cannot reach the curve

Assume \(s\ge16\), \(3\le r\le s-3\), and lower the rate to
\(\rho_0=(r-2)/s<k/n\). It suffices to show \(r/s<a_1(\rho_0)\).

**High branch.** Put \(t=s-r\), so \(3\le t\le s-3\). Exact expansion gives

\[
 F((s-t)/s,(s-t-2)/s)=-H_s(t)/s^3,
\]
\[
 H_s(t)=4s^2(t-2)-3st^2-16s-t^3-2t^2.
\]

This polynomial is strictly concave in \(t\), since
\(H_s''(t)=-6s-6t-4<0\). Its endpoint values are

\[
 H_s(3)=4s^2-43s-45>0,
 \qquad H_s(s-3)=5s^2-58s+9>0
 \quad(s\ge16).
\]

Thus \(F<0\), and the target lies below the positive root.

**Low branch.** It suffices to prove \(2r^2\le s(r-2)\), because equality
still gives \(r/s=\sqrt{\rho_0/2}<a_1(\rho_0)\).
For \(r\ge6\), the low-branch hypothesis yields

\[
 s>16(r-2)/3\ge 2r^2/(r-2),
\]

where the latter inequality is equivalent to
\(5r^2-32r+32\ge0\), valid for \(r\ge6\).
For \(r=4\), use \(s\ge16\). For \(r=5\), the low-branch
hypothesis forces \(s\ge17\), and \(3s>50\). For \(r=3\), use
\(s\ge18\). The only remaining cases are \(r=3\), \(s=16,17\).
Here put \(b=1/\sqrt{2s}\) and \(u_0=6b-1>0\), so that
\(r/s=b(1+u_0)\). Direct computation gives

\[
 b-u_0^2(u_0+3)=b(19-108/s)-2>0,
\]

because \(19s-108>0\) and
\((19s-108)^2-8s^3\) is respectively \(5648\) and \(6921\).
The positive cubic root is therefore larger than \(u_0\), completing the
interior exclusion.

## The two nontrivial endpoints give only linear banks

For \(r=2\), the dimension is \(k=1\). If \(2/s>a_1(1/(sm))\), then
\(2/s>\sqrt{1/(2sm)}\), hence \(m>s/8\). Consequently

\[
 \binom{s}{2}/n=(s-1)/(2m)<4.
\]

This use of the curve for a constant code is just an algebraic necessary
condition; the DKT treatment of constant codes itself is separate. Any code
enlargement only makes the curve condition harder.

For \(r=s-2\), the actual rate is \(\rho=((s-4)m+1)/(sm)\ge3/4\).
An exact identity, retaining the one-dimensional correction, is

\[
 F((s-2)/s,((s-4)m+1)/(sm))=-\frac{4E(s,m)}{m^2s^3},
\]
\[
 E(s,m)=ms^2-7m^2s+4ms-4m^2+m-s.
\]

If \(m\le s/7\), then

\[
 E=ms(s-7m)+3s-3+(m-1)(4s-4m-3)>0.
\]

So crossing above the curve requires \(m>s/7\), and
\(\binom{s}{2}/n<7/2\). The remaining rank \(r=s-1\) has only
\(s\le n\) subsets. Together with the interior exclusion this proves
\(M<4n\) for every integer \(s\ge16\).

If \(s,m\) are powers of two, either endpoint condition implies
\(m\ge s/4\), giving \(M<2n\). For the remaining powers \(s\le8\),
\(s=4\) is immediate. At \(s=8\), cases with \(M\ge2n\) require
\(m\in\{1,2,4\}\). There are exactly nine such cases. The case
\((m,r)=(1,2)\) has \(r/s=\sqrt{(k/n)/2}<a_1(k/n)\); the other eight
have \(k/n\ge3/16>\rho_c\) and strictly negative \(F\), as recorded in
the verifier. Thus the strict \(M<2n\) bound holds for all admissible powers
of two. (The primary construction further requires \(m\ge2\).)
For arbitrary integers \(s<16\), the constant bound \(M\le6435\) is
already enough to exclude superlinear growth along a family with \(n\to\infty\).

## Why shrinking-distance substitution fails

At the high endpoint \(r=s-2\),

\[
 k=n-4m+1,\quad T=n-2m,\quad
 T^2-n(k-1)=4m^2>0.
\]

Thus the canonical agreement is above exact Johnson. It cannot be lowered
into the above-first-order window unless it is already above first order.
As \(m/n\to0\), the exact dimension gives

\[
 n a_1(k/n)=T+\tfrac12-
 \frac{7(4m-1)^2}{32n}+O((4m-1)^3/n^2).
\]

If \(m^2/n\to0\), the positive half-coordinate correction wins and
\(T<n a_1(k/n)\). Conversely, the exact calculation above forces
\(m^2/n=m/s>1/7\) to cross the curve. Since
\(M/n=(s-1)/(2m)\), a superlinear bank and crossing cannot coexist.
Replacing dimension by degree would silently remove the decisive term.

At the low endpoint, the entropy constant in the primary theorem is not
uniformly positive: \(H_2(\rho)\sim\rho\log_2(1/\rho)\).
In a formally uniform substitution,

\[
 \frac{\eta}{\sqrt\rho}\sim
 \frac{H_2(\rho)}{\tau\sqrt\rho\log_2 n}\longrightarrow0
 \qquad(\rho\to0,\ n\to\infty).
\]

Thus the suggested scaling \(\rho\asymp\eta^2\) is incompatible with
that formula. More importantly, the exact integer ledger above handles cases
where this asymptotic substitution or its rounding is not justified: every
interior \(r\ge3\) is excluded, and \(r=2\) gives only a linear bank.

## A scoped leading-coefficient cancellation gate

Could the one-dimensional correction be removed while retaining the same
quadratic-size high-rate bank? Consider an affine polynomial correction to
the existing received pencil, \(f+\lambda g\mapsto
f-C_0+\lambda(g-C_1)\), that cancels the top coefficient of its canonical
witnesses. This includes an affine change of endpoints followed by a fixed
polynomial translation. We show it preserves at most \(s\) canonical
supports when \(r=s-2\), even for arbitrary distinct tags \(G\).

Write \(S=G\setminus\{\alpha,\beta\}\),
\(\sigma=\sum_{a\in G}a\), and \(P_G(Y)=\prod_{a\in G}(Y-a)\).
In the quotient compiler use the harmless translated parameterization

\[
 f=(Y^r-b^r)/(Y-b),\quad g=1/(Y-b),\quad
 \lambda_S=V_S(b)=\frac{P_G(b)}{(b-\alpha)(b-\beta)},\qquad b\notin G.
\]

The canonical witness is
\((Y^r-b^r+V_S(b)-V_S(Y))/(Y-b)\), whose top coefficient is
\(e_1(S)=\sigma-\alpha-\beta\). Canceling that coefficient means
\(e_1(S)=A+B\lambda_S\) for fixed field elements \(A,B\), hence

\[
 (\sigma-\alpha-\beta-A)(b-\alpha)(b-\beta)-BP_G(b)=0.
\]

For each fixed \(\alpha\), this is a polynomial of degree exactly two in
\(\beta\), with leading coefficient \(b-\alpha\ne0\). There are at
most \(2s\) ordered pairs, hence at most \(s\) unordered supports.

For the direct Section 2 pencil, the top witness coefficient is
\(-e_2(S)\), and the challenge is affine in \(e_1(S)\). Let
\(\tau=e_2(G)\), \(u=\alpha+\beta\), \(v=\alpha\beta\). Then

\[
 e_1(S)=\sigma-u,\qquad e_2(S)=\tau-\sigma u+u^2-v.
\]

An affine cancellation requires \(e_2(S)=A+B e_1(S)\). After fixing
\(\alpha\), the resulting polynomial in \(\beta\) has leading
coefficient one, again leaving at most \(s\) supports. Since canonical
witnesses are polynomials in \(X^m\), canceling their highest coefficient
actually drops a whole \(m\)-sized degree block; it does not offer a free
single-degree reduction for all \(\binom{s}{2}\) witnesses.

This gate does not rule out new witnesses, a different support compiler,
non-affine source constructions, or a different denominator architecture.
It closes the specified degree-saving repair to the existing pencils.

## Verification and relation to previous work

`verify_kkh_rate_uniform_envelope.py` checks the displayed polynomial
identities, the finite low-branch inequalities, all nine small power-of-two
cases, the endpoint expansion, and both genuine-quadratic cancellation
coefficients. Its exact receipt is `kkh_rate_uniform_envelope_receipt.json`.
It performs no growing parameter scan.

This result is consistent with
`KKH_R2_QUADRATIC_ENLARGEMENT.md`: that earlier finite construction supplies
a **linear** number of singleton labels after enlarging the code. The present
envelope explains why merely moving the same canonical subset bank to a
shrinking rate or shrinking distance cannot upgrade that count to
\(B/n\to\infty\) in the first-order window.
