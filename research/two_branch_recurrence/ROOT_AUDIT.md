# Independent root-agent review of the triangular Riccati proof

September 17, 2026. Reviewed PROOF.md independently of its author. The
stated fixed-T theorem and its unnormalized two-branch corollary pass.
This is a mathematical proof review, not formal verification or human
refereeing. Later generalizations require their own review.

The coefficient of X^(t+j-1) has no P^2 term because t>2D, and no
constant-message contribution because deg_X R<=t-2. The descending
recurrence has pivot j, nonzero in the stated characteristic. Its
challenge degree bound D-j+2 follows by induction.

After substitution the constant-X equation is monic quadratic in c;
all other equations are linear in c. The nonzero-resultant and
nonproportional-linear-equation cases count all labels, including
vanishing leading coefficients. If all determinants and the resultant
vanish identically, the locus on B!=0 is a persistent graph, so isolated
points lie above roots of B. These cases justify the 4D+4 bound without
regularity assumptions. Monicity of the constant equation excludes
vertical curve factors.

The incidence proof counts actual matches, rather than formal solution
parameters. Substitution of each matching graph c=f(x)+zg(x)-Q(x,z)
into an irreducible component has degree at most its z-degree plus
(D+1) times its c-degree. Summed over components this is at most
3(D+1). A component with more than D persistent coordinates is forced
by interpolation to be a base-field affine codeword pencil; its other
coordinates add at most n exceptional labels. The remaining components
need A-D nonpersistent incidences per nearby candidate. This gives the
claimed total bound, including singular points.

For the domain-locator corollary, degrees above n+D-1 can only come
from the branch product, giving at most two labels if a coefficient is
nonzero. Otherwise two branches of degrees greater than D each have
degree at most n-2, so the triangular theorem applies. If a branch has
degree at most D, every other solution agrees with the other branch
on n-D coordinates. Pairwise uniqueness needs n>3D; the three-label
interpolation argument needs n>4D, exactly as assumed. It places all
remaining solutions on a second affine codeword pencil.

Scope: this is not a general first-order interpolation theorem. In
particular it does not cover arbitrary derivative degree, arbitrary
leading-X coefficients, or every resonance pattern. No intrinsic
lower bound or better.codes improvement follows from the result alone.
