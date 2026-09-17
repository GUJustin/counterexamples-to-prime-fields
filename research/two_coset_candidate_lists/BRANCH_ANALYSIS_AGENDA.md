# Proposed branch analysis of binomial sections — not yet a theorem

September17, research agenda. The following algebra suggests why the
quadratic r2,j1 construction is exceptional. It needs a complete local
audit, explicit character-sum constants and independent finite checks
before being advertised as an upper bound. No manuscript claim uses it.

Let p=2rk+1, 0<=j<r, e=(p-1)/2+j, and omega a primitive rth root in F_p.
The root filter gives

    G(t^r)=1/(r*t^j) sum_a omega^(-aj)*(1+omega^a*t)^e.

On an rth-power class choose t=tau*s, s in F_p, where tau^p=omega^b*tau.
Writing u_a=(1+omega^a*t)^((p+1)/2), one has

    u_a^2=(1+omega^a*t)*(1+omega^(a+b)*t),
    G(t^r)=1/(r*t^j) sum_a omega^(-aj)*(1+omega^a*t)^(j-1)*u_a.

Thus each class is described by finitely many branches in a multiquadratic
function field over the s-line. The radicand square classes correspond
to edges (a,a+b) of a cycle graph on the r roots. If b is neither0 nor
r/2, these nontrivial square classes are distinct, suggesting linear
independence of their radicals over the rational function field and no
constant branches. For b=r/2, edges occur twice; cancellation can occur
only for j1, because the coefficients (1+omega^a*t)^(j-1) and
(1-omega^a*t)^(j-1) are proportional only then (j0 needs denominator
clearing and separate verification). The constant value is then0.

For b0, every branch has signs sigma_a in{+1,-1}, and is

    1/(r*t^j) sum_a sigma_a*omega^(-aj)*(1+omega^a*t)^j.

A constant branch must have every lower coefficient vanish; its value
is (1/r)sum_a sigma_a. For j0 all patterns are constant. The largest
number of patterns producing one value is at most binom(r,floor(r/2)).
For r4,j1, the lower Fourier constraint forces sigma0=sigma2 and
sigma1=sigma3; the largest value multiplicity is2 patterns, not6.

For b=r/2,j1, the zero branch corresponds to all r/2 quadratic norms
1-omega^(2a)*tau^2*s^2 being squares. This suggests density2^(-r/2).
Standard character-pattern counting on each of the two mu_k cosets
within an rth-power class would give the expected densities with an
error of size O_r(sqrt(p)).

For nonconstant branches, clear denominators and multiply G-v over
the sign choices, excluding identically constant branches when needed.
The proposed norm degree is at most r*2^r in s, hence at most about2^r
exceptional x-values per class/value after the r-to-one map. The
invariance of the excluded-branch product and treatment of all base
points must be checked; do not assume this bound without that audit.

If these steps hold, the full-orbit modal agreement on c mu_k cosets
would have a leading coefficient at most

    2*binom(r,floor(r/2))/2^r
      + 1_{r even,j1}*2^(1-r/2),

times k, with O_{r,c}(sqrt(k)) errors. For r4,j1 the refined first
term is1/4 and the second1/2. For r>=3 this would be at most7/8,
whereas r2,j1 permits3/2, matching the known mechanism. This would
rule out growing fixed-gap FULL-ORBIT lists for every separately fixed
r>=3 in this family, but would not by itself address r growing with k.

A possible extension to arbitrary candidate subsets needs multiplicative
Fourier mixing of the constant-branch masks. If nontrivial Fourier
coefficients are O_r(sqrt(p)), a subset of L candidates would have
average agreement at most the full-orbit leading term plus
O_{r,c}(k/sqrt(L)+k/L). This too remains unproved here. It could explain
why non-subgroup subsets do not persist asymptotically, but is not a
general prime-field list-size upper bound.
