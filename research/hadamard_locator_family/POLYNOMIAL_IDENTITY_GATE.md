# Necessary polynomial identities from distinct nodes

For a valid sign-twisted eight-sextic bank write F_i^±(T)=±A_i(Y)+T B_i(Y), Y=T², with B0=0. At each of the sixteen new nodes the common word V satisfies (V-TBi)²=Ai² for every i. Thus

 H_ij(Y)=Y Bi Bj(Bi-Bj)-Bj(Ai²-A0²)+Bi(Aj²-A0²)=0.

The sixteen new nodes form eight distinct nonzero Y values. H_ij also vanishes at e0i,e0j,eij: the first two use A0=Ai=Bi=0 or its j version; the last uses Ai=Aj=0 and Bi=Bj. All eleven Y values are distinct. Since deg H_ij≤8, every H_ij is identically zero. This is a necessary identity over any field with the stated distinctness, independently of the previous cross-remainder searches.

## Leading coefficient: correct beta convention

Our stored beta=(0,q-bc,q-c,q-b) is NOT the leading coefficient of physical Bi. The physical leading coefficient is sigma(1-ai)+tau beta_i. Therefore one must not set (ai²-1)/beta_i constant.

Put S=sum beta, E2=sum_{i<j} beta_i beta_j, E3=beta1 beta2 beta3, D=S²-4E2, J3=SD+8E3. The internal amplitude line is ai=1+t beta_i(S-2beta_i). The identity's degree8 coefficient implies a constant K with

 ai²-1=K[ sigma(1-ai)+tau beta_i ].

Reduction at the three beta roots gives

 (a(x)²-1)/x = 4E3*t²+2S*t +(t²D-4t)x
 modulo prod(x-beta_i).

Consequently

 tD=4+2K sigma,   K tau=t² J3/2,
 z=sigma²=k(tD-4)/(t²J3), where k=sigma*tau.

These signs were checked independently of the root derivation. J3=-prod(S-2beta_i). Its factors are nonzero in a valid bank: differences ai-aj=t(beta_i-beta_j)(2beta_k-S) and all candidate leading coefficients must be distinct. The stored beta differences and beta values are likewise nonzero by distinct edges. Thus the leading identity fixes z, not h.

`identity_leading.py/json` records its exact substitution into the shifted four-parameter family. Lower H coefficients are the next shape-only constraints. No exclusion follows from the leading coefficient alone.
