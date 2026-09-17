# Removing the factor-two characteristic restriction

September 16, 2026, overnight continuation. This proof supersedes the
p>2D restriction for ordinary lists and fixed-equation MCA in the
initial recovered note. It does NOT assert constant cross ratios under
the weaker guard; the old characteristic-three control remains valid.

## Statements

Let D>=1 and char E=0 or p>D. For a(X)P'=b0+b1P+b2P^2, a!=0,
and degree P<=D:

1. Every ordinary list at agreement threshold A>D on n distinct points
   has M<=floor(n/(A-D)).
2. If b2!=0, the entire candidate set has at most C_D solutions, where
   C_D=D+2 in characteristic zero or p>D+1, and C_D=2D+2 if p=D+1.
3. For one fixed nonlinear equation, full-support bad labels on any
   received line number at most 2n(n+C_D)/(A-D).

The old sharp prime-field list construction still attains item 1.
D+2 is attained by the old split-squarefree Riccati family in its
stated regime. At p=2,D=1, (X^2+X)P'=P^2+P has exactly four solutions
0,1,X,X+1, attaining 2D+2 in this boundary case. At p=3,D=2 the old
five-solution example still rules out a uniform D+2 count.

## A. Candidate counts by initial-value reconstruction

Work over E(t), with t transcendental, so a(t)b2(t)!=0. Write
P'=F(X,P), with F=alpha+beta*u+gamma*u^2, gamma=b2/a!=0, and use
Delta=partial_X+F partial_u. Define F_0=u and F_j=Delta^j u.
For j<p, or in characteristic zero, F_j is polynomial in u of degree
j+1 with leading coefficient j! gamma^j. The recurrence proves this:
F partial_u contributes (j+1)gamma times the old leading coefficient,
whereas partial_X contributes a lower u-degree.

If char E=0 or p>D+1, every polynomial solution satisfies
F_(D+1)(t,P(t))=P^(D+1)(t)=0. This is a nonzero polynomial of degree
D+2 in P(t), proving the count. Different polynomial solutions have
different values at transcendental t.

If p=D+1, reconstruct the truncated Taylor polynomial

    T(U,X)=sum_(j=0)^D F_j(t,U)*(X-t)^j/j!.

Every degree-<=D solution is exactly T(P(t),X). The polynomial T has
U-degree D+1, with leading U-coefficient gamma(t)^D*(X-t)^D.
Consequently the residual

    a(X) partial_X T - b0(X)-b1(X)T-b2(X)T^2

has U-degree exactly 2D+2: its leading coefficient is
-b2(X)*gamma(t)^(2D)*(X-t)^(2D), which is nonzero. Select any nonzero
X-coefficient of this residual. All candidate values P(t) are roots
of a nonzero polynomial of degree at most 2D+2. This proves the
boundary bound and finiteness without assuming constant cross ratios.

## B. The local multiplicity inequality

For M>=2 distinct candidate solutions and a domain coordinate x, put

    C_x=sum_(i<j) ord_x(P_i-P_j).

Then sum_x C_x<=D*binom(M,2). We prove for every received value,
with h matching candidates,

    (h-1)*(M-1) <= 2*C_x.                         (B1)

For characteristic zero, use the original constant-cross-ratio proof.
For positive characteristic p>D, first handle b2=0: differences solve
one homogeneous linear equation, and the ratio of any two nonzero
differences has derivative zero and rational degree <=D<p. It is a
constant. Thus all candidates form P0+cW, and their values at x are
all distinct or all equal. Formula (B1) is immediate.

Assume b2!=0. The total-count result gives M<=2D+2<=2p. Cross ratios
have derivative zero even when they are nonconstant. A nonzero rational
function with derivative zero has every zero order divisible by p.
Choose a colliding pair at x and two solutions outside its value class.
The denominator in their cross-ratio identity is nonzero at x. The
numerator of cross-ratio minus one, up to sign, is the product of the
two within-pair differences. If the two outside values are distinct,
its order is at most D<p, impossible. Therefore a collision with at
least two outside candidates forces exactly two value classes.

If these classes have sizes h and b=M-h, both at least two, let alpha
and beta be the minimum positive vanishing orders of differences
within the respective classes. Every cross-pair choice of two such
differences has total order at least p; hence alpha+beta>=p. Both
alpha,beta are at least one. Write A0=binom(h,2), B0=binom(b,2).
Then C_x>=A0*alpha+B0*beta.

If h<=b, already C_x>=A0+B0 and

    2(A0+B0)-(M-1)(h-1)=(b-1)(b-h+1)>=0.

If h>=b, minimizing subject to alpha,beta>=1 and alpha+beta>=p gives
C_x>=A0+(p-1)B0. Therefore

    2*C_x-(M-1)(h-1)
       >=(b-1)*(p*b-M+1)>=0,

because b>=2 and M<=2p. This proves (B1) for both possible matching
classes. A received value outside the classes has h=0. The remaining
patterns (all distinct, all equal, or one class of size M-1 and one
singleton) satisfy (B1) by the original unweighted inequality.

Summing (B1) gives

    (AM-n)*(M-1) <= 2 sum_x C_x <= D*M*(M-1),

so M(A-D)<=n. The case M=1 is immediate. This proves the ordinary
list bound under p>D, including p=D+1.

## C. Full-support labels

Repeat the original heavy/light proof with C_D in place of D+2.
The heavy count uses the just-proved list bound at threshold
D+(A-D)/2. The light count uses the entire candidate bound C_D.
No nonsingularity assumption on agreement coordinates is used.

## Review points

- The local proof uses zero multiplicities of cross-ratio minus one,
  not a false assertion that the cross ratio is constant.
- All ordinary derivatives and Taylor factorials used in reconstruction
  have order <=D<p; the extra derivative is used only when p>D+1.
- The boundary residual is nonzero by its highest U-degree, not by an
  unsupported genericity assumption.
- The sum C_x counts all pair intersections, including candidates not
  matching the received value; this is essential to (B1).
- The finite candidate bound is used only for nonlinear Riccati equations.
  The affine-linear case is treated separately by its one-dimensional
  homogeneous solution space under the degree guard.
