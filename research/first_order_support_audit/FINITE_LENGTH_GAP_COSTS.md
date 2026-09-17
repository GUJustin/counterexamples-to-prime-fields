# Exact finite-length inverse-margin costs

September 17, 2026. This extends the leading-coefficient cost converse
using the already audited exact finite-length reduction. It concerns
full-coefficient-prefix monomial sources, not arbitrary nonmonomial
global sources or actual list sizes.

Let N>=12 be divisible by four, D=N/4-1, k=N/4<A<=N, and m>=1.
Retain all X^x Y0^u Y1^b with x+Du+(D-1)b<mA from a downward-Y0 jet
support. Let G be the number of coefficients and R the exact local rank.
Suppose Delta=G/N-R>0. Put

    a*=(AN-8)/(N(N-8)), epsilon*=a*-a0.

If 0<epsilon*<=1/2000, all four cost inequalities hold exactly:

    m>c0/epsilon*, U>m/4, V>m/4-1,
    R/Delta>=1/(8epsilon*).

Here U,V bound the retained source's two jet degrees. Consequently the
exact uniform challenge count

    (ell+1)G > N(ell+beta+1)R, beta>=U

requires ell=Omega((epsilon*)^-2). The unchanged reconstruction budgets
therefore cost Omega(D/(epsilon*)^3) and Omega(D^2/(epsilon*)^5).

Proof: discard final total-degree diagonals with Lq=mA-(D-1)q<m.
The half-rank inequality shows their surplus is nonpositive. The retained
source S0 is downward, has saturated local rank R0<=R and positive
surplus Delta0=G0/N-R0>=Delta. Its leading benefit at a* satisfies
B*>=G0/N, with all individual benefits positive. Thus

    R/Delta >= R0/Delta0 >= R0/(B*-R0) >=1/(8epsilon*).

Apply the monomial cost theorem to S0 to obtain m and its coordinate
degree lower bounds, which also lower-bound the original source degrees.
The remaining challenge and reconstruction calculations are unchanged.

This is uniform in m and exact in N. It does not require m to stay fixed.
For a=A/N=a0+epsilon,

    epsilon*=(N epsilon+8a0-8/N)/(N-8).

Thus epsilon*=Theta(epsilon) when epsilon>=1/N and N is large.
At A=ceil(N a0), 0<epsilon*<5/(N-8), so the necessary multiplicity is
Omega(N), the uniform challenge budget Omega(N^2), and the displayed
list/MCA budgets Omega(N^4) and Omega(N^7), respectively. These are costs
of using this proof framework at the threshold rounded up to an integer
number of agreements, not lower bounds on true lists or exceptions.
