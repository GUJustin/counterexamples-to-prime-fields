# Generic-parameter audit of the second-step correction ansatz

The first one-pole step is generic, as proved in `GENERIC_ONE_POLE.md`. However, varying the four seed parameters cannot make the specific old-polynomial-part correction from `../SECOND_STEP_STRUCTURAL_TEST.md` succeed. The obstruction below is an exact identity, not a parameter scan. It leaves general cubic polynomial parts and other double-match patterns open.

Work in characteristic zero (the displayed algebra also works in characteristic different from two). Fix four nonzero parameters a,b,c,d with distinct squares and the requisite distinct signed pair nodes. Choose H_a(X)=X²/a²+a² as the old polynomial used in the correction. Its six matching coordinates are ±ab,±ac,±ad. The six nonmatching coordinates are ±bc,±bd,±cd; on an edge uv the received value minus H_a equals

    C_uv=−(a²−u²)(a²−v²)/a².

As in the preceding test, choose two matching coordinates r,s, and define

    z_x=(x−r)(x−s)/C_uv  at x=±uv.

Success requires constants alpha,beta,gamma satisfying

    x=alpha+beta z_x+gamma z_x²                 (1)

at all six nonmatching coordinates. The constants include the freely chosen quadratic critical value and prospective pole, so failure of (1) cannot be repaired by those choices or by choosing the two fresh coordinates differently.

If r=−s, z_x is even in x and (1) immediately fails at the two opposite nonzero nodes. Otherwise sign changes of seed parameters and relabeling let us assume r=ab,s=ac. These changes preserve all hypotheses and signed node sets.

For t=uv write

    U_uv=(u²v²+a²bc)/C_uv,
    V_uv=−a(b+c)uv/C_uv,
    z_(+uv)=U_uv+V_uv, z_(−uv)=U_uv−V_uv.

Subtracting the two versions of (1) gives

    C_uv=−a(b+c)(beta+2gamma U_uv).

Therefore the three points (U_uv,C_uv), for uv=bc,bd,cd, must be collinear. Their exact determinant is

    −a²(a²+bc)(b²−c²)(b²−d²)(c²−d²)
    / ((a²−b²)(a²−c²)(a²−d²)).

All factors other than a²+bc are nonzero. Thus necessarily c=−a²/b.

Under this necessary relation the difference equations uniquely force

    beta=(a²−b²)/(ab),
    gamma=−(a²−b²)(a²−d²)/(2a⁵b).

Adding the two versions of (1) then forces, separately at each edge,

    alpha_uv=−beta U_uv−gamma(U_uv²+V_uv²).

But substitution gives

    alpha_cd−alpha_bc = a(b²−d²)/(2b) != 0.

This contradiction excludes the ansatz for every admissible parameter choice. The other difference is

    alpha_bd−alpha_bc = −(a⁴−b²d²)/(2ab),

but it is not needed.

The determinant and both simplifications were obtained and checked with exact symbolic rational arithmetic in `second_step_symbolic.py`; full expressions and watchdog records are saved beside it. The bounded computation completed in under one second under 384-MiB/60-second limits. No broad numerical search was run.

The generic first step remains a positive algebraic construction. What fails is the attempt to preserve an old lifted polynomial as the next rational witness's polynomial part while forcing double matches at the first pole fiber and two old matching fibers. A successful repeatable identity must change at least one of these choices.
