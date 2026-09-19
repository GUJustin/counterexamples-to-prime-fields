# Exactly five or six extra errors in the fixed elliptic window

September 19, 2026. Exact parameter calculation, not a counterexample.

Fix an integer ell>=23 and

    n=(ell^2-1)/2, k=n-4ell+1, rho=k/n,
    T_d=n-2ell-d, alpha_d=T_d/n.

For the torsion setting ell is an odd prime. Among integer d>=0 with T_d>=0, exactly d=5 and d=6 satisfy both

    n*a_1(rho) < T_d < sqrt(n*(k-1)),

where a_1 is the full first-order agreement bound used in the paper. In particular, six extras are a legitimate remaining option; arbitrarily increasing the extra budget at these fixed n,k would weaken the target below the existing first-order bound.

## Finite Johnson side

The exact strict Johnson slack is

    J_d = n*(k-1)-T_d^2
        = -d^2+d*ell^2-4*d*ell-d-4*ell^2.

At d=4 this is -16ell-20<0. It is increasing for 0<=d<=4 when ell>=23, so no smaller nonnegative d qualifies. At d=5 it is ell^2-20ell-30>0, and at d=6 it is 2ell^2-24ell-42>0. Both inequalities hold at ell=23 and increase thereafter.

## Full first-order side

The rate rho=1-(8ell-2)/(ell^2-1) is increasing for ell>=23 and starts at 173/264, above the high-branch transition 11-3sqrt(13). On this branch, for 0<=alpha<=1, agreement is strictly above a_1(rho) exactly when

    F(alpha,rho)=(8-rho)*alpha^2-6rho*alpha+rho*(4rho-5)>0.

The other root is negative, since rho*(4rho-5)<0. Exact substitution gives

    F(alpha_5,rho)
      =4(6ell^4-4ell^3+387ell^2+196ell-291)/(ell^2-1)^3,

    F(alpha_6,rho)
      =8(ell^4-4ell^3+256ell^2+140ell-201)/(ell^2-1)^3,

    F(alpha_7,rho)
      =-4(2ell^4+12ell^3-651ell^2-380ell+531)/(ell^2-1)^3.

The first two expressions are positive for ell>=23. For the last numerator, writing x=ell-23 gives

    2x^4+196x^3+6525x^2+86054x+353098,

which is positive for x>=0. Thus alpha_7<a_1(rho). Every larger d with nonnegative T_d has even smaller agreement, so it also fails this side of the target window.

For ell=23, the two eligible agreement counts are T_5=213 and T_6=212, with n=264,k=173. Their strict finite Johnson slacks are 39 and 464 respectively.

## Consequence for research, with scope

The existing norm-quintic route uses functions in L(5O). A six-extra route can instead consider L(6O), whose generic normalized functions have the form A_3(x)+y B_1(x), with A_3 monic cubic and B_1 linear. Their norms A_3(x)^2-f_curve(x)B_1(x)^2 are monic sextics. This supplies one additional normalized parameter compared with the quintic family, but does not supply native split roots, challenge labels, source farness, or a shared received line.

The earlier arbitrary-extra fixed-base lemma still applies at d=6 because the punctured minimum distance 2ell is greater than 18. It gives at most seven labels per fixed pair of full fibers. Therefore using only O(n) such pairs cannot produce superlinear growth merely by changing quintics to sextics.

This calculation holds at the stated fixed code dimension. Retuning k to accommodate a growing extra budget changes the problem and requires new witness-degree, first-order, and source-distance proofs. No such construction is asserted here.
