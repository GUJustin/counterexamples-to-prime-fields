# Coprime zero-excess rigidity for nonuniform contacts

## 1. A cyclic-window combinatorial lemma

Let u_1,...,u_n be real numbers, 1<=w<n, and gcd(n,w)=1. Write
V=(w/n)sum_i u_i. If the vector is nonconstant, then

    #{T: |T|=w, sum_T u_i>V} >= binom(n,w)/n.      (1)

**Proof.** In any cyclic ordering of the n entries, the n consecutive
length-w window sums have average V. If all equal V, subtract adjacent
window sums to obtain u_i=u_(i+w), with indices modulo n. Coprimality
makes this a single cycle, so every entry is equal. For a nonconstant
vector, therefore, at least one window exceeds V in EVERY ordering.
Average over uniform random permutations. Each specified window is a
uniform w-subset, so the expected number of windows exceeding V is
n times the number of positive subsets divided by binom(n,w).
It is at least one, proving (1). No integrality is needed here.

## 2. Applying the contact-subset bound at equality

Let F be a nonzero first-jet polynomial of weighted degree V for weights
(1,w,w-1,0), and let a_x be its actual formal contacts at the n nodes.
Assume gcd(n,w)=1 and zero average contact excess:

    V=(w/n)sum_x a_x.

The universal subset bound from PRIMARY_FACTOR_CONTACT_BUDGET.md says
at most floor(V/(w-1)) w-subsets have contact sum greater than V.
Consequently, if

    binom(n,w)>n*floor(V/(w-1)),                    (2)

the contacts must all be the same integer a. It follows that V=aw.
Alternatively, integrality and coprimality already imply w divides V
and n divides the total contact, before proving uniformity.

For 1<=a<w-1, n>w+a, and characteristic zero or p>a, the independently
proved uniform equality theorem now gives

    F=c(Z)(Y-P(X,Z))^a,   deg_X P<=w.             (3)

If a=0, then V=0 and F is independent of X,Y,R, so it is only a scalar
over k(Z). The zero-weight case must be distinguished from graph factors.

For affine received symbols f_x+Zg_x, interpolate at w+1 nodes. This
forces P=P_0(X)+ZP_1(X), with P_0,P_1 over the original field and degree
at most w. Thus no challenge poles or exceptional specializations are
introduced in this graph description. If F is originally polynomial,
its Y^a coefficient c(Z) is polynomial. A non-scalar irreducible F in
the original polynomial ring is consequently a scalar multiple of
Y-P_0-ZP_1, with a=1.

## 3. Benchmark scope

At n=262144 and w=131071, gcd(n,w)=1. For any factor of the proposed
primary source, V<mA=21390450, so V<2^25 and floor(V/(w-1))<2^9.
Thus the right side of (2) is less than 2^27, whereas
binom(n,w)>=binom(n,5)>2^75. If V=aw, then a<=163, so a<w-1,
n>w+a, and the characteristic condition p>a hold with substantial room.
Every zero-charge factor is therefore either challenge-only or a
received-line graph factor. This removes the nonuniform equality gap
from the nonnegative additive resource theorem.

This does NOT yet yield a useful lower bound on a positive charge, or
charge individual first-tail intersection components. Also deg P<=w
is intentional: it does not automatically give membership in a code
whose degree convention is strict degree<w.
