# Three old double fibers: complete fixed-seed test

This tests a different correction pattern from the previous notes. Let a be the first one-pole witness's pole, and let

    A(y)=G_i(y)+h L(y), B(y)=lambda L(y),
    L(y)=(y−r)(y−s)(y−t),

where r,s,t are three of the six old coordinates matching H_i. In particular the first pole fiber is not among the three double fibers. All polynomials retain the correct cubic-in-y degree bounds. On each nonmatching base coordinate define

    z_y=L(y)/[(y−a)(w(y)−H_i(y))].

The six desired single matches force

    y=c+[b+lambda z_y/(1−h z_y)]².

A necessary condition is a nonzero vector in the kernel of the six rows (1,z,z²,−y,−yz,−yz²), with denominator nonvanishing at every tested node and square discriminant zero.

The exact fixed-cyclotomic test evaluates all 4*C(6,3)=80 choices using the first pole displayed in `PROOF.md`. Seventy-six matrices have zero kernel. The remaining four have one-dimensional kernel; every such denominator has nonzero discriminant. More decisively, all four maps are undefined at three of the six required nodes. These are not candidate rational maps.

The four exceptional root triples are:

    old index0: {2,4,5}; index1: {1,3,5};
    index2: {0,3,4}; index3: {0,1,2}.

They are precisely the intersections of the first witness's six-node support {0,1,2,3,4,5} with each old polynomial's matching set.

## Why these four kernels cannot be rescued generically

The generic reciprocal-seed identity gives

    N−D H_i=k_i A_i,
    D(y)=−e3(y−a), A_i=product_(j!=i)(y−a_i a_j).

If the correction roots are exactly these three selected incident edges, then at each of the other three selected edges the first rational witness agrees with w, and therefore

    z_y=A_i(y)/[(y−a)(w(y)−H_i(y))]=−e3/k_i.

Thus three distinct base coordinates y have exactly the same z. No defined rational function of z can return all three. The interpolation vectors only survive by making numerator and denominator simultaneously zero there. This excludes this aligned support pattern for all admissible generic seeds, independently of its denominator discriminant.

The other 76 fixed-seed patterns are excluded only for the tested cyclotomic specialization; no generic classification is asserted for them. No second one-pole witness has been constructed or ruled out outside these restricted patterns.

Files `second_step_three_old.py`, `second_step_three_old.json`, and `second_step_three_old_resources.json` retain exact kernel vectors, denominator discriminants, undefined-node guards, and resource data. The computation used the repository watchdog with 384-MiB/60-second limits and completed in under two seconds. No larger parameter enumeration was run.
