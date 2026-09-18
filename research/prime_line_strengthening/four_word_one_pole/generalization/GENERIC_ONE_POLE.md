# The first one-pole step is a generic algebraic operation

## Positive theorem

Work in characteristic different from two. Choose four nonzero parameters a_i with distinct squares, and assume their six pair products are distinct up to sign. Put

    H_i(X)=X^2/a_i^2+a_i^2,
    Omega={+a_i*a_j,-a_i*a_j : i<j}.

At either node belonging to the pair ij, the two candidates H_i,H_j have common value a_i^2+a_j^2. No third candidate shares it, because the squares are distinct. This defines a length-twelve word with six matches per quadratic.

Let e_1,e_2,e_3,e_4 be the elementary symmetric functions of the four a_i. Define

    D(X)=e_1*e_4-e_3*X,
    N(X)=e_1*X^3+(e_3-e_1*e_2)*X^2
                  +(e_2*e_3-e_1*e_4)*X-e_3*e_4.

Assume e_3 is nonzero and D has no zero in Omega. Then N/D is a proper one-pole function, of numerator degree at most three, agreeing at all six positive pair nodes. These assumptions hold on a nonempty Zariski-open parameter set; for instance (a_1,a_2,a_3,a_4)=(1,2,5,13) has e_1=21,e_3=231,e_4=130, and pole130/11 outside all twelve nodes.

Consequently the existing degree-two pullback/pole-clearing construction gives a five-word length-28 bank with degree cap6 and at least14 agreements per word for a generic family of four-word seeds. This is not an induction to arbitrarily many words.

## Exact identity proving the theorem

For each i, set

    A_i(X)=product_(j!=i)(X-a_i*a_j),
    k_i=product_(j!=i)(a_i+a_j)/a_i^2.

Then

    N(X)-D(X)*H_i(X)=k_i*A_i(X).                 (1)

To verify it, write a=a_i and use the quartic equation

    a^4-e_1*a^3+e_2*a^2-e_3*a+e_4=0.

It gives

    A_i=X^3+(a^2-e_1*a)*X^2+(e_3*a-e_4)*X-a^2*e_4,
    k_i=e_1+e_3/a^2.

Comparing coefficients yields (1). Thus all six required agreement identities hold.

Every k_i is nonzero since the squares are distinct. If N and D shared a root, (1) would force it to lie among the three positive pair nodes incident to every i, impossible. Equivalently the pole cannot be a root of A_i when D avoids Omega. Hence the rational function is proper.

At a positive node x=a_i*a_j, with complementary pair k,l,

    D(x)=-x*(a_k+a_l)*(x-a_k*a_l).

Thus pole avoidance on the selected six nodes follows already from the domain assumptions. Avoidance on the other six nodes is an additional, genuine open condition. The nonzero example above verifies the open conditions are consistent.

## Complete support combinatorics and sign obstruction

A proper numerator-degree3/denominator-degree1 function matching six word coordinates intersects each old quadratic in at most three coordinates. Double-counting the twelve incidences shows it meets each old candidate exactly three times.

Let m_ij in {0,1,2} count selected signs on edge ij. The degree-three condition at all four vertices forces opposite-edge multiplicities equal and their three values to sum to three. Therefore they are either (1,1,1), or a permutation of (2,1,0).

The latter is impossible for a proper one-pole function. Write its numerator N(X)=N_e(X^2)+X*N_o(X^2), with deg N_e,deg N_o at most one, and normalize its denominator to X-alpha. Matching both signs over x^2=q of an even received word gives

    N_e(q)+alpha*N_o(q)=0.

This polynomial in q has degree at most one. It is not identically zero, since otherwise N=(X-alpha)*N_o(X^2), contradicting properness. A (2,1,0) pattern has two doubled edges, with distinct squared nodes, and is therefore impossible. Every saturated proper witness chooses exactly one sign per edge.

Write its signs epsilon_ij. Vertex switching a_i -> sigma_i*a_i sends epsilon_ij to epsilon_ij*sigma_i*sigma_j. Normalize the three signs incident to vertex1 to +. There remain eight classes. The homogeneous six-point interpolation matrix has rows

    (1,x,x^2,x^3,-w*x,-w).

An exact determinant expansion in `determinant.py` proves that its determinant is identically zero only for the remaining signs (+,+,+) and (-,-,-). For the other six it factors as ±2abcd times products of a_i-a_j and a_i+a_j, with some factors repeated, so it never vanishes under the distinct-square assumptions. Full factors are in `determinant.json`.

Thus the only possible supports are balanced signs epsilon_ij=sigma_i*sigma_j and antibalanced signs epsilon_ij=-sigma_i*sigma_j. Formula (1), after vertex switching and possibly X -> -X, constructs these supports whenever the corresponding pole guards hold. There are sixteen such sign supports in total; the cyclotomic example's twelve proper witnesses reflect its special guards, not the absence of a generic operation.

## Verification and scope

The determinant computation sums all720 permutation terms exactly for each of eight classes and independently compares each expression with a direct rational6x6 determinant at (1,2,5,13). It completed under the repository watchdog in1.12seconds, peak62MiB. The formula (1) is proved by the displayed quartic reduction, independently of that computation. The six nonzero determinant factorizations are a finite exact polynomial certificate rather than a sampled generic-rank claim.

This family has algebraic coefficients and nodes; after the established pullback, excluding finitely many bad primes and taking completely splitting primes realizes the finite bank over prime fields. It remains a fixed five-word bank. No superlinear bad-label or unbounded-list conclusion is asserted.
