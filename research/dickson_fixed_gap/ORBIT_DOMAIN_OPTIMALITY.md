# Orbit averaging optimizes over all domains and received words

September 17, 2026. Elementary optimization lemma for the binomial-section
search; no general list-size upper bound.

Let H be a multiplicative subgroup of F_p^* of order L dividing k. Let
G be a monic degree-k polynomial, and consider the candidate orbit

    P_h(X)=G(hX)-X^k, h in H.

For every coset C of H, let m_C be the largest fiber size of G on C.
Sort these numbers decreasingly. For n=qL<=p-1, the largest possible
minimum agreement of these candidates with a single word, optimized
over ALL n-point domains in F_p and ALL received words, is exactly

    M=m_1+...+m_q.

This assumes the candidates are distinct if interpreted as a list;
nonzero linear coefficient of G is a sufficient condition.

Proof. At any nonzero coordinate x, the multiset of candidate values is
{G(hx)-x^k:h in H}. Its largest multiplicity is m_(xH). Thus the mean
agreement over the L candidates is at most the sum of m_(xH)/L over
the chosen coordinates. Each coset supplies at most L coordinates, so
on a nonzero domain of size qL this sum is at most M.
If the domain contains zero, that coordinate supplies at most one to
the mean, and the best other qL-1 coordinates supply at most
M-m_q/L. Since m_q>=1, the result is strictly below M+1. The minimum
agreement is an integer, and is therefore still at most M.

For attainment, take the q cosets with largest m_C, choose a most
frequent value v_C of G on each, and set w(x)=v_C-x^k there.
Multiplication by every h permutes each coset, so every candidate
agrees at exactly m_C coordinates of C. This proves the claim.

Consequences. Allowing a nonconstant word inside cosets, taking partial
cosets, or adding zero cannot improve the full-orbit minimum agreement
at these lengths. The earlier search's optimization is therefore valid
without its H-invariant-word/domain restriction. It does NOT exclude
an arbitrary proper subset of candidates, changing G, or parameters
outside the scan. Subgroup orbits are separately covered below.

## Subgroup scan

`subgroup_sections.cpp` checks all section indices j=0,...,r-1 for
r=2,...,48 and k=16,32,64,128 at prime p=2rk+1, and every subgroup
order L=4,8,...,k. There are 4,326 cases. It optimizes n=ck for
c=4,8,16,32 whenever n<=p-1. Assertions remain enabled.
`verify_subgroup_sections.py` independently checks coverage, all
full-orbit rows against the earlier census, exact characteristic-Elias
inequalities, and complete candidate lists in selected fixtures using
integer binomial coefficients.

Below-Elias case counts for c=4,8,16,32 are 36,998,1908,2550;
maximum L is respectively 64,8,16,32. The quarter-rate L64 example is
the known r2 construction. Outside r2, all quarter-rate hits have L4
except r33,j0,k32,p2113,L8,n128,A43. Thus reducing the orbit can improve
finite examples, but this scan supplies no growing-list family at one
fixed positive gap on short domains. No main-paper theorem is added.

The independent `verify_orbit_domain_optimality.py` exhausts all 799
small domain fixtures and 10,816 nondominated received words across five
orbit examples over F7 and F13. It includes domains containing zero,
checks the upper bound at every word, and checks attainment of equality.
Symbols absent from every candidate can be omitted because replacing
one by a present value cannot reduce any candidate's agreement.
