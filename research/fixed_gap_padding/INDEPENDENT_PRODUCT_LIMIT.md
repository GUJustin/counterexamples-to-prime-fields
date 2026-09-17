# Independent products cannot amplify indefinitely at a fixed gap

September 17, 2026. Elementary degree constraint, valid over every field.

For i=1,...,r, let F_i be a nontrivial family of monic degree-A_i
locator polynomials. Consider ALL independent products

    product_i F_i,  F_i chosen independently from its family.

Their common degree is A=sum A_i. Suppose every product agrees in
coefficients of degrees A,A-1,...,K, so subtracting a common received
polynomial produces degree-<K codewords. Write s=A-K>0.

For one factor family define d_i=max deg(F-F') over distinct members.
Then the maximum degree of a difference of full products is exactly

    D=max_i (A-A_i+d_i).

The lower bound follows by varying ONLY factor i; multiplication by
the other monic factors adds exactly A-A_i to the difference degree.
For the upper bound, telescope an arbitrary difference of products,
changing one factor at a time. Every summand has degree at most D.
Thus the longest common leading prefix has surplus exactly A-D-1,
and any allowed s satisfies

    s <= min_i (A_i-d_i-1) <= min_i(A_i-1).

If the root domain has length n>=A and eta=s/n, this forces

    r(s+1)<=A<=n,  hence r<1/eta.

This rules out a particular tempting amplification: at one fixed
positive gap, one cannot take more and more independent nontrivial
locator factors. Scaling each factor by polynomial composition does
not change the obstruction; apply the same degree argument after
composition. The statement does not bound the size of an individual
factor family or cover correlated choices that cancel leading terms.

## Explicit family illustrating the cost

For block i=0,...,r-1, choose either pair of integer roots

    {10i+1,10i+4} or {10i+2,10i+3}.

Their locators have the same leading and linear coefficients and
differ by2. Substitute X^B in each locator and multiply independently.
There are2^r distinct products, all of degree A=2Br, on a potential
split-fiber domain of length n=4Br. Their maximum difference degree
is exactly2B(r-1), so the maximal common-prefix surplus is2B-1,
independent of r. One may choose dimension K=B(2r-1), giving exact
rate(2r-1)/(4r) and exact gap1/(4r). The selected-list logarithm is
r=1/(4eta), only reciprocal in the gap.

The formal polynomial identities hold over the integers. Arbitrarily
large splitting primes realize the fibers as distinct prime-field
evaluation points. The checker verifies all products for r1..6 and
B1,2,3, and verifies every candidate agreement directly over F101 for
B1. This does not assert that the selected list is the entire list.

The existing nearly quadratic construction gets its strength from
coupled moment collisions. A product construction would need a new
coupling mechanism, or an already-growing single factor family, to
improve that result.

## A tempting two-pencil line is automatically explained

Another tempting variant starts with factors A(X)+uC(X) and
B(X)+vD(X), sets z=uv, and takes

    f=AB,  g=CD,  Q_{u,v}=-uCB-vAD.

Their difference is the factored locator. Suppose deg A=a, deg B=b,
a+b=T>K, and both cross terms CB and AD have degree<K, so the
displayed candidates automatically fit the code. Then

    deg(CD) <= 2(K-1)-(a+b) < K.

Thus the direction g is itself a codeword. Whenever Q is nearby at z,
the two codewords Q-zg and g explain the received coefficient words
on the entire agreement support. This ansatz has no bad proximity-gap
parameters at all, irrespective of how many factor pairs split.
The conclusion assumes the individual cross terms fit the code; it
does not cover exceptional cancellation between high-degree cross
terms or arbitrary nonlinear parameter couplings.
