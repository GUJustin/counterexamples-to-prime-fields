# A distinct positive target: quadratic cover, one pole, quadratic pullback

Status: exact construction reduction, not a found eighth word. No scan is proposed without first exploiting the two-parameter algebraic structure below. A text search of the existing seven-bank research found direct one-pole and cubic-cover one-pole gates, but no test of this specific quadratic-cover route.

## The missing rate-compatible alternative

Start with the seven-cubic bank of length14, degree<=3 and agreement7. Take a degree-m cover, add a proper one-pole witness, and append one old-only pole point and one new-only fresh point. This gives length14m+2, degree<=3m+1, agreement>=7m+1. A subsequent degree-r polynomial pullback gives

    n=r(14m+2), D=r(3m+1), A=r(7m+1).

Exact quarter rate (D+1)/n=1/4 is equivalent to r(m-1)=2. There are two positive integer solutions:

    (m,r)=(3,1), the previously investigated cubic route;
    (m,r)=(2,2), the new target here.

Thus a proper degree(7,1) rational witness with14 matches on a quadratic lift of the seven-cubic bank would produce EIGHT words at n60,D14,k15,A30 over a number field, and hence over arbitrarily large split primes. The intermediate eight-word bank is n30,D7,A15. This is a concrete positive payoff beyond the seven-word construction, without requiring log removal.

## Exact sufficient construction

Choose a separable rational quadratic map psi=R/S whose fibers above the14 original nodes consist of28 distinct finite points, disjoint from zeros of S. Old words are H_i(U)=S(U)^3 P_i(R(U)/S(U)), degree<=6; the received value on a fiber above x is S(U)^3 w_x.

Find ell(U)=U-b and N(U), deg N<=7, with b off the28-point core, N(b)!=0, and N/ell agreeing with this received word at least14 times on the core. Multiply the old bank and core word by ell. At the new point b set the word to0: all seven old polynomials ell H_i agree, while N does not. Choose one further point c off the29-point domain and set its word to N(c). Each old word now has at least15 agreements and the new word at least15. Properness at b makes the new polynomial distinct from every old one.

Finally choose a quadratic polynomial map unramified over these30 nodes, and take all60 inverse images over a number-field extension. Pulling back doubles degrees and agreements, giving n60,D14,A30. All coefficients and nodes are algebraic; splitting primes outside the finite collision/denominator set preserve every identity and distinctness condition. This is an existence-of-primes descent, not a uniform small-prime bound.

## A two-parameter exact gate

Up to source PGL2, a generic rational quadratic cover has the form

    psi(U)=(a U²+b)/(U²+1), a!=b.

The two parameters are the branch values. For a base node x the squared fiber coordinate is t_x=(b-x)/(x-a), and the scaled word is v_x=(t_x+1)^3 w_x. This is the standard degree-three projective transport of the original seven-cubic bank.

Write the candidate numerator as N(U)=E(U²)+U O(U²), with deg E,deg O<=3, and write its denominator U-beta. A match at u²=t_x is exactly

    E(t_x)+beta v_x+u(O(t_x)-v_x)=0.

Both points of that fiber match exactly when O(t_x)=v_x and E(t_x)=-beta v_x. The cubic L=E+beta O therefore vanishes at every full fiber. If L is identically zero the candidate is improper; otherwise at most3 fibers are full. At a single matched point, eliminating u gives

    (E(t_x)+beta v_x)^2=t_x(O(t_x)-v_x)^2.

These equations, their sign choices, and explicit noncollision/properness guards define the exact positive-construction target. They live over the small coefficient field of the seven-bank; roots need only be adjoined after finding the cover/witness parameters. They are different from the excluded cubic-cover three-root gate.

There is also a useful incidence constraint before elimination. If T and Q count candidate matches over the seven original triple and seven original quadruple coordinates, then T+Q>=14 and 3T+4Q<=49: each difference N-ell H_i has degree<=7 and contributes at most7 common matches. Thus T>=7. This helps select support patterns but does not by itself classify them.

A generic degree-two rational cover has2 moduli after source PGL2, and a degree(7,1) witness has9 parameters after common scaling. Fourteen matches therefore have expected deficit3, compared with deficit5 for the cubic-cover route. This dimension comparison is a prioritization heuristic only; it proves neither existence nor nonexistence. The recommended next mathematical step is to use the cubic L and the seven-bank incidence identities to identify a support pattern for which several single-fiber norm equations become dependent, rather than run another random-cover census.
