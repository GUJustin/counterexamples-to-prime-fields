# Quarter-rate inverse-gap costs of the unchanged first-order ledger

September 17, 2026. New consequence of the audited support converse.
This establishes sharp orders for a specified proof ledger, not for
actual Reed–Solomon list sizes or exceptional-challenge counts.

Let a0=(3+sqrt(133))/31, c0=(1-2a0)/8, and a=a0+epsilon with
0<epsilon<=1/2000. Let S be any nonempty finite downward-Y0 monomial
support with positive leading benefits ma-(u+b)/4. Put

    B=sum_S(ma-(u+b)/4), R=r_m(S), Delta=B-R>0,
    U=max_S u, V=max_S b, J=max_S(u+b), s=|S|.

Then

    m>c0/epsilon, U>m/4, V>m/4-1,
    R/Delta >=1/(8epsilon).                            (1)

In particular V>=m/8 for this epsilon range. Thus multiplicity, both
jet-degree budgets, and the total jet-degree budget must all grow at
least as epsilon^-1.

## Proof of the four inequalities

The multiplicity inequality is the already audited finite-m theorem.
Since a0<469/1000, we have c0>3/400; our epsilon range forces m>15 and a<47/100.

For the Y0 degree, if U>=m/2 there is nothing to prove. Otherwise every
homogeneous diagonal has at most U+1 monomials, all active for ell>=U.
For U<=ell<=m-U-1 the row capacity m-ell is at least U+1. The exact
rank formula therefore gives R>=(m-2U)s. Since B<=ma*s and B>R,
U>m(1-a)/2>m/4.

For the Y1 degree, apply the audited height sorting and diagonal
compression. They do not increase the largest second exponent. If the
compressed support has C columns, then C<=V+1. Its one-sided continuum
lift at agreement a has strictly positive surplus and width at most C/m,
even after trimming nonpositive benefit outside the triangle.
Prefix completion improves surplus without increasing width. Hence
there is a positive quarter-rate cap of width at most C/m.

For 0<Bcap<=1/4 and a0<=a<=47/100, its surplus divided by Bcap is

    2a^2-1/2+(1-a)*Bcap/2-7*Bcap^2/24.

This expression increases in both a and Bcap on that rectangle. At its
upper-right corner it equals -2443/240000<0. Thus no such narrow cap
has positive surplus. We must have C/m>1/4, proving V>m/4-1.
Because m>=16, this also gives V>=m/8.

Finally, on a compressed column of height h<=2m, the rank marginal is
at least (m-u)_+/2. If h<=m, its column sum is at least mh/4. If
m<=h<=2m, the sum is at least m(m+1)/4>=mh/8. Summing columns and
using rank domination under rearrangement yields R>=ms/8 for the
original support. At a0 every support has nonpositive surplus, including
supports with some negative benefits there: discard those monomials if
necessary. Hence

    Delta=B(a)-R <= B(a)-B(a0)=m*epsilon*s.

Combining the two inequalities proves R/Delta>=1/(8epsilon).

## Challenge-degree cost

Suppose the uniform challenge-coefficient budget ell is chosen through

    (ell+1)*B > (ell+beta+1)*R,

where beta is a declared local-equation degree bound at least U. This
includes the coauthor ledger's beta=Bjet>=J. It requires

    ell >= floor(beta*R/Delta)
         > m/(32epsilon)-1
         > c0/(32epsilon^2)-1.

Thus this sufficient count cannot certify ell=o(epsilon^-2), regardless
of the monomial support. This does not rule out a smaller-degree actual
kernel vector obtained using global dependencies or a different matrix
or coefficient-degree accounting scheme.

## Cubic and fifth-power budgets

The recovered coauthor draft uses declared bounds Bpartial>=V and
Bjet>=max(J,Bpartial), and the reconstruction budget

    Brec=(Bjet-Bpartial)*Bpartial*(Bpartial+1)
         +Bpartial*(Bpartial+1)*(2Bpartial+1)/6.

Its second summand alone is at least Bpartial^3/3. By (1), every
positive-surplus support has Brec=Omega(epsilon^-3). For message degree
D and lambda_agr=(n-D)/(A-D)>=1, the unchanged list budget contains
2D*lambda_agr*Brec. Its MCA budget contains
24D^2*ell*lambda_agr^2*Brec. Consequently these displayed budgets have
unavoidable orders

    Omega(D/epsilon^3), Omega(D^2/epsilon^5),

respectively. At rate1/4, D is Theta(n). Together with the draft's
matching upper orders, these establish sharp epsilon powers for this
interpolation-plus-reconstruction ledger, even when the monomial
support is optimized arbitrarily within the stated source class.

The source formulas were checked in recovered version7, Theorem1.1 and
Equation(23), pages7 and22. This is not a claim that every conceivable
first-order proof has these costs. In particular, sparse-support root
counting, lower actual degrees, global constraint dependencies, or a
new agreement argument could improve the ledger. The conclusion also
uses leading normalized coefficients; it is not a uniform exact
finite-length lower bound when epsilon shrinks with n.
