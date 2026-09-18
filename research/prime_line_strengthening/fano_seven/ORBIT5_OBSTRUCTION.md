# Global odd-characteristic exclusion of ordered design orbit5

Work over an algebraic closure of characteristic different from two. The ordered incidence design is

    T=123,145,167,246,257,347,356;
    C=123,145,167,247,256,346,357.

The nodes t_L carry the triples T; the nodes b_L carry the quadruples complementary to C. Assume all fourteen nodes are distinct and all seven cubic candidates are distinct. Every pair has exactly three prescribed common nodes, so its difference is a scalar multiple of their cubic locator. In particular, no pair can agree at an additional node. At a quadruple node the other three candidate values must be mutually distinct and different from the quadruple value.

## Complement-node constraints

Normalize the seven b-nodes to

    infinity,0,1,u,v,w,z

in the order of C above. All finite nodes are distinct and different from0,1. Dividing the three difference identities on a T-line by its common triple-node factor gives a necessary dependence of three quadratics in the b-nodes. The three nonzero determinant equations for T123,T145,T167 are

    −uv w−uv z+uv+u w z+v w z−wz=0,
    −uw+u+vz−v+w−z=0,
    uz−vw=0.

The other four determinants vanish identically because those T-triples already lie in a complementary C-quadruple.

Since z,w,z−v,z−w are nonzero, substitute u=vw/z in the first two equations. They become, respectively,

    w(z−v)(vw+vz−v−z)/z=0,
    (z−w)(vw+vz−v−z)/z=0.

Therefore, putting s=w+z−1,

    s!=0, u=w/s, v=z/s.

The distinct-node guards also imply s!=1 and s!=-1, though the contradiction below does not need both extra exclusions.

## All possible cubic candidates

Subtract P1 so P1=0. The pairwise roots at the b-nodes force

    P2=(X−w)(X−z)L0,
    P3=s²(X−u)(X−v)L0,
    P4=(X−z)(X−v)L1,  P5=(X−w)(X−u)L1,
    P6=(X−z)(X−u)L2,  P7=(X−w)(X−v)L2,

where, for some p,q,l,

    L0=pX+q,
    L1=l(X−1)−s(p+q),
    L2=lX+s q.

This parametrization includes every possible candidate family, not only a subfamily. Initially each P_i is its prescribed b-root quadratic times an arbitrary linear polynomial. The quadruple equality at infinity makes the leading coefficients of P4,...,P7 equal. Equality at0 forces the constant terms of the quotient linears for P6,P7 to agree; equality at1 does the same for P4,P5. Equality of P2,P3 at0 and1, using u=w/s,v=z/s, makes their quotient linears differ by the factor s². The remaining equalities at0 and1 give exactly the displayed constant terms of L1,L2.

The leading value of P1 at infinity is0, while the selected quadruple4567 has value l. Since no extra pair equality is possible there,

    l!=0, p−l!=0.

## Two remaining triple conditions suffice

Define

    A=l z+p z s+q s(s+1),
    B=l w+p w s+q s(s+1),
    C_z=l(z−1)+s(w−1)p+s(s−1)q,
    C_w=l(w−1)+s(z−1)p+s(s−1)q,
    F_+=(z−w)l+s(s+1)p+2s²q,
    F_-=(w−z)l+s(s+1)p+2s²q.

The factors A,B,C_z,C_w are all nonzero in an admissible realization. Indeed,

    (P2−P4)(0)=z A/s,   (P2−P5)(0)=w B/s,
    (P2−P6)(1)=(z−1)C_z/s,
    (P2−P7)(1)=(w−1)C_w/s.

At0 the selected quadruple is2367, so P4,P5 cannot share its value. At1 it is2345, so P6,P7 cannot share its value. All displayed scalar multipliers are nonzero.

For T246, all three cubics already agree at the complementary-quadruple node z. After dividing out X−z, the two relevant differences are

    f=(X−w)L0−(X−v)L1,
    g=(X−w)L0−(X−u)L2.

Their additional common root t246 must be finite and different from z. Their resultant, after multiplying each quadratic by s, is the exact identity

    Res_X(s f,s g)=−(p−l)s A C_z F_+.

Thus F_+=0. Similarly, for T257 divide out X−w and use

    f=(X−z)L0−(X−u)L1,
    g=(X−z)L0−(X−v)L2.

The resultant is

    Res_X(s f,s g)=−(p−l)s B C_w F_-,

so F_-=0. Subtracting gives

    2(z−w)l=0.

Since the characteristic is not two and z!=w, this forces l=0, contradicting the no-extra-agreement guard at infinity. Hence orbit5 has no realization in odd characteristic or characteristic zero.

## Verification artifacts and limits

`relative_fano.py 5` derives all seven necessary determinant equations. `orbit5_explicit.py` computes and factors the four remaining quadratic resultants from the complete parametrization. The first two factorizations are all the proof requires; their coefficients can also be checked directly from the two-by-two quadratic resultant formula. The successful symbolic job took8.03seconds under384MiB/60second limits.

A preceding attempt to derive the entire generic nullspace directly timed out at60seconds, as recorded in `orbit5_symbolic_family.resources.json`; it is not a proof dependency. The manual complete parametrization removes that computational bottleneck.

This excludes ordered orbit5 only. Together with the aligned Fano obstruction it closes orbits4 and5. It does not exclude the six remaining enumerated designs or all seven-cubic banks.
