# What a second-moment improvement would have to establish

Let N=binomial(255,136), S=256*p^6, and let L_s be the actual fibers
of the six-leading-coefficient plus product signature map. Then

    max_s L_s >= (sum_s L_s^2)/N.

Writing L_required=274980728111395088, a sufficient exact collision
certificate is

    sum_s L_s^2 >= N*(L_required-1)+1.

The universal Cauchy-Schwarz guarantee is only ceil(N^2/S). The required
collision count is about4.01 times that guarantee, not a small additive
improvement. Numerically, log2 N is about250; the required ordered-pair
count has logarithm about308. An actual excess-collision theorem is
needed. Reexpressing Cauchy-Schwarz through Fourier characters or
quotienting both domain and signature by rotations does not supply it.

This diagnostic does not claim the target collision count is necessary
for a large fiber: a single exceptional fiber may be proved directly
without raising the global second moment by this much. It identifies
the precise sufficient inequality for the proposed averaging route.

Support banks invariant under small root-of-unity subgroups force
several power sums to vanish, but the elementary counting tradeoff is
already the coarser-packet tradeoff. For example, opposite-pair supports
are root polynomials in Y^2. Their extra vanished odd coefficients do
not count as independent new savings on top of the change of packet
size; the parameter scan must be redone at that coarser size, as in the
existing exact frontier. No new coefficient-image theorem or favorable
collision lower bound was obtained in this pass.

Status: explicit research target, not a proof of concentration and not
a better.codes improvement.
