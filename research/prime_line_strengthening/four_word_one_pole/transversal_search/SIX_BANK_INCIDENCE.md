# The explicit six-word bank is a smooth incidence point

## Exact construction and checks

Starting with the first certified parameter solution modulo97, `six_bank_incidence.py` constructs the complete six-word bank over F_97(theta), theta^2=5. The element5 is a nonsquare modulo97. Field elements are encoded as a+97b for a+b theta, with0<=a,b<97; this encoding is NOT ordinary integer arithmetic modulo97^2.

The intermediate five-word domain has26 core points and the two fresh residual roots24,52, all in F_97. Its five polynomials G_i have degree at most6, each with exactly14 agreements. The second proper rational witness is N(T)/(T-81), where the ascending numerator coefficients are

    (34,54,93,0,84,3,56,70).

It agrees at exactly14 intermediate domain coordinates. Apply the quadratic map T=U^2. Every one of the29 fibers over the intermediate28 coordinates and81 splits over F_97(theta), and none is ramified. Define

    H_i(U)=(U^2-81)G_i(U^2),  i=1,...,5,
    H_6(U)=N(U^2).

The new domain consists of the56 preimages of the intermediate domain, the two roots of U^2=81, and the fresh points0,1. All60 points are distinct. On the56 preimages use word (T-81)w(T), on the new pole fiber use0, and at0,1 use H_6.

Exact pair arithmetic verifies all60 word values, six distinct degree-at-most14 candidates, and EXACTLY30 agreements for every candidate. Thus selecting the guaranteed30 matches per candidate loses no accidental matches. The incidence-degree histogram over the60 nodes is

    degree1:2, degree2:16, degree3:26, degree4:12, degree5:4.

The full encoded domain, word, polynomial coefficients, and selected incidence lists are in `six_bank_incidence.json`.

## Incidence Jacobian

Use six unrestricted degree-at-most14 polynomials,60 node variables, and60 word variables. There are210 variables and180 selected matching equations

    P_i(x_j)-w_j=0.

Every node is covered. At each node choose one incident polynomial as reference and eliminate that node's word variable using its reference equation. The remaining120 equations in150 variables have linearizations

    delta P_i(x_j)-delta P_ref(x_j)
      +(P_i'(x_j)-P_ref'(x_j))*delta x_j=0.

The verifier constructs this120-by150 matrix exactly over F_97(theta). For an entry a+b theta, multiplication on coordinates (u,v) is represented by

    [[a,5b],[b,a]].

Restriction of scalars therefore gives a240-by300 matrix over F_97, whose rank is twice the extension-field rank. Exact modular Gaussian elimination gives

    F_97 block rank240,
    F_97(theta) reduced rank120,
    full incidence Jacobian rank180.

The six-bank point is consequently smooth of raw local dimension210-180=30 in this fixed incidence scheme. Distinctness and all displayed nonzero guards define open conditions, so this is a deformation statement about genuine nearby banks with the selected agreement pattern. It does not prove that any additional seventh candidate exists.

## Gauge dimensions: an important distinction

There are18 independent tangent directions from adding a common degree-at-most14 polynomial (15), affine changes of the node coordinate (2), and common nonzero value scaling (1). Independence follows first from the node-coordinate variations, and then from distinctness of two candidates. Modulo these AFFINE gauges the local dimension is12.

If all natural projective Reed--Solomon equivalences are removed, there is one further direction. For D=14 it is

    delta x_j=x_j^2,
    delta P_i=D X P_i-X^2 P_i',
    delta w_j=D x_j w_j.

The apparent degree-D+1 term in delta P_i cancels. Direct substitution verifies every linearized matching equation. This direction comes from a fractional-linear coordinate change with the corresponding degree-D value multiplier, and is independent of the affine directions because a quadratic cannot equal an affine function at60 distinct nodes.

Thus the full common-polynomial/value-scaling/PGL_2 gauge has dimension19, leaving11 local parameters, not12. This distinction does not change smoothness or the positive30-dimensional raw deformation result. It prevents calling all12 affine-quotient parameters fully gauge-free.

## Reproducibility and scope

The final guarded run completed in0.56seconds under the384MiB/60s watchdog. `six_bank_incidence.resources.json` records the run; the JSON certificate records block pivots and dimensions. The exact field implementation, incidence construction, and modular rank computation are in `six_bank_incidence.py`.

This verifies a concrete six-word bank and its local incidence flexibility. It neither establishes a seven-word deformation nor an indefinitely repeatable one-pole operation. Any next extension must impose and verify its own equations and pole/fresh-root guards.
