# Independent-selector Walsh coordinates

The four selector rows are indexed by 0,1,2,4 in F_2^3. Write
r_x = sum_a (-1)^(a dot x) t_a.
This is an invertible change of coordinates in every characteristic other than two.
For a pair of selectors, partition the eight signed roots into their four agreeing
and four disagreeing positions, denoted E and D. Write their monic quartics as
e(Y)+T o(Y), d(Y)+T p(Y), with Y=T^2.
The required old fourfold block forces the odd/odd branch o(Y)=p(Y)=0;
the even/even alternative does not give equal odd parts of the sextic words.
Under distinct signed-leading-coefficient guards, both odd factors have degree one,
and sharing their root is exactly e1(E)e3(D)-e3(E)e1(D)=0.

`independent_selector_gate.py` expands these six identities over the integers.
Each has content64 and a primitive homogeneous quartic with16 terms. Every
quartic is linear in t7. `independent_selector_eliminate.py` records f_i=a_i t7+b_i
and every compatibility minor a_i b_j-a_j b_i. On a_i nonzero, recover
t7=-b_i/a_i. The exceptional chart a_0=...=a_5=0 requires all b_i=0 and is retained.

These equations are necessary conditions, not a valid eight-word bank. All eight
root squares must be nonzero and distinct; the six old edge squares must likewise
be nonzero and distinct, and disjoint from the new nodes. Signed leading
coefficients and the complete locator conditions must still be checked.

Generation took less than a second per script. An optional full factorization of
all minors was stopped after roughly40seconds without an algebraic conclusion;
expanded minors contain52–64 terms and are the saved output. No field search or
characteristic-zero existence claim is made here.
