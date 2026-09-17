# Analytic phase-source bypass diagnostic

Target A=181275, n=262144, w=131071. This work
supports the frontier agent's exact finite tests; it is NOT a finite
phase gate, full propagation, or better.codes certificate. No source
parameters here have been declared valid merely from continuum values.

## Exact leading-order relations

Write lambda=L/m, sigma=s/m, alpha=A/w, rho=n/w,
d=(A-w+1)/w, and gamma=alpha+sigma/w. At fixed singleton
(r,v,z)=(12,43,3206), put y=r+v=55 and t=y+z=3261.
The coefficient-count leading term, divided by w*m^4, is

    C(lambda,sigma)=integral_0^sigma
       [(lambda-j)(alpha-(1-1/w)j)^2/2
                   -(alpha-(1-1/w)j)^3/6] dj.

The local-rank leading term is evaluated exactly by rank() in
continuum.py. Thus normalized source surplus is C-rho*rank.
The thin-loss leading term is

    d * integral_0^end Channel(lambda-u*t,
                              min(gamma-u*y,
                                  max(0,alpha-u*(y+d-r/w))
                                     +(sigma-u*r)/w),
                              sigma-u*r) du,

where end=min(lambda/t,gamma/y,sigma/r), and

    Channel(T,Y,S)=integral_0^min(T,Y) min(S,j)(T-j) dj.

All breakpoints and integrals in continuum.py are exact rational
operations. The w-1 weight and sigma/w shift are retained: dropping
these apparently small terms materially changes the tiny surplus.
Finite coefficient/rank corrections, floor effects, and discrete thin
sums are NOT included. The exact frontier evaluator must decide gates.

## Two different branches, not one global optimum

A local stationary shape near lambda70.9,sigma.30975 has continuum
activation boundary t about3240.07, hence z about3185.07. The frontier's
exact source00-scale candidates activate later because of finite effects
and the characteristic constraint. The local stationary calculation is
not a global exclusion of other parameter shapes.

A second, large-lambda branch exists. Once Y limits every channel,
the normalized gate margin is affine in lambda and total degree t.
Near sigma=.3046214 its formula is approximately

    lambda*(7.78752647e-7) - .00016511905
                    +(t-3261)*(7.56824795e-6).

Consequently continuum activation at z2950 (t3005) would need lambda
about2700. But the actual global characteristic gate uses caps163,9678:

    m*(163*lambda+9678*gamma) < 2130706433,

up to the exact integer Y and strict-bound rounding. At lambda2700 this
forces m only about4700, where the finite correction cannot be assumed
small. This trade, rather than the local lambda70 optimum alone, is the
right feasibility question for the alternative branch.

## Coordinated finite work

The frontier agent owns fast_firstjet_count.py, all exact finite gates,
small legitimate candidate sets, singleton envelopes, and propagation.
This agent supplied stationary ratios and the high-lambda trade above.
The auditor separately optimizes auxiliary geometry; that route is not
duplicated here. Initial simplified-weight continuum values were replaced
in the saved JSON files by the correct w-versus-w-1 formulas.

Run continuum.py for the five local shape probes; analyze.py computes
bounded stationary diagnostics for the two branches. The JSON outputs
explicitly state their continuum-only scope. No new large blind grid
is part of this artifact.
