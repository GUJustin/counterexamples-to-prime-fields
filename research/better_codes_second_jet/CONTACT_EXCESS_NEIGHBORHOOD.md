# A bounded-neighborhood extension of the contact-subset argument

Let integer contacts u_i>=0 have weighted mean mu=(w/n)sum u_i.
Suppose a polynomial of weighted degree V forces at most
d=floor(V/(w-1)) w-subsets with sum greater than V. Set

    e=V-mu, N=w(n-w), M=max_(|T|=w) sum_T u_i.

If M>V, take a maximizing T and its N one-element-swap neighbors.
Their sums add to

    N*M-n*(M-mu).

At most d neighbors exceed V (using d rather than d-1 is conservative),
and every neighbor sum is at most M. Hence their total is at most

    d*M+(N-d)*V.

Subtracting proves

    (N-n-d)*(M-V)<=n*e.                           (1)

If N-n-d>0 and e<(N-n-d)/n, integrality M-V>=1 shows that M>V
is impossible. Thus ALL w-subset sums are at most V in this range.
This is stronger than merely bounding the number of exceptional subsets.

For a nonconstant integer contact vector, there is also the elementary
bound

    M-mu>=min(w,n-w)/n.                           (2)

Sort the entries and let T comprise the w largest. Then n(M-mu) is
the sum of all w(n-w) cross differences between a top and a bottom entry.
If the smallest top entry exceeds the largest bottom entry, all these
differences are at least one. Otherwise their common boundary value c
has either a top entry strictly above c or a bottom entry strictly below
c; this gives respectively n-w or w cross differences at least one.
This proves (2). Therefore when all subset sums are <=V, nonconstant
integer contacts require e>=min(w,n-w)/n.

The argument is exact and requires no genericity or characteristic
assumption. Its small constant positive-charge gap does not presently
improve the benchmark: it neither associates charges to individual
first-tail components nor supplies a strong count of nonuniform factors.
