# Local sharpness at the binding flags

This is a local model only, not a factor universal for the full interpolation kernel or a global all-node construction.

In characteristic zero (or safely p>3261), put

    F0=R^12 Y^43+X^19(Y-XR)^12,
    F=F0+X^42(Y-XR)Z^3260.

At X=0 with received value zero, substituting Y=tR+t^2 E gives

    F=t^43(R^55+E^12)+higher t-order terms.

Thus contact is exactly43, while the exact caps are (r,y,t)=(12,55,3261) and contact weight55w-12. The polynomial solution P=0 is regular generically:

    F_R(X,0,0,Z)=-X^43 Z^3260 !=0.

The leading R coefficient is A=Y^43+X^31, so A(X,P,Z)=X^31. In particular leading-coefficient contact loss r=12 is attained despite the leading Y coefficient being constant. Full local contact does not force high vanishing of A along the selected regular solution beyond a-r.

For irreducibility, over k(X,Y) the fractional substitution T=R/(Y-XR) transforms F0 into a unit times T^12 Y^43+X^19. Its Y-adic Newton polygon has slope43/12, in lowest terms, so this degree12 polynomial is irreducible. F0 is primitive in R: its constant and leading coefficients X^19Y^12 and Y^43+X^31 are coprime. Hence F0 is an irreducible polynomial. Viewed as a Z-polynomial, F is Eisenstein at the prime F0; its leading coefficient X^42(Y-XR) is not divisible by F0 and its constant coefficient is exactly F0. Primitivity gives irreducibility in the full polynomial ring, and localization gives irreducibility over k(Z).

The parent independently checked this example. It rules out an attempted local transfer lemma, but says nothing by itself about the global one-dimensional own-system condition.
