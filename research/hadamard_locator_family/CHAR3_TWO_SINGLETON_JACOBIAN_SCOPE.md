# Why two added singleton nodes do not give a full-rank Hensel point

Start at a characteristic-three realization of eight cubics on fourteen
distinct nodes with seven agreements each and four agreements at every
node. Its full incidence system has56 equations and60 variables:
32 polynomial coefficients,14 nodes,14 received values.

There are eight independent infinitesimal gauge directions in
characteristic three: four common-polynomial additions, one common
scaling, and three PGL2 parameter directions with the O(3) action.
The latter are independent because the domain has at least three
distinct points; after those are removed, common-polynomial and scaling
directions are independent because the candidates are distinct.
Hence the original Jacobian has rank at most52.

Delete two old incidence equations and append two new singleton nodes
with two new equations. The enlarged system has64 variables and56
selected equations. Its old54-row submatrix still has rank at most52;
its two additional rows increase rank by at most two. Its Jacobian rank
is therefore at most54, not56. Thus this unchanged seed cannot provide
an ordinary full-row-rank implicit-function/Hensel certificate merely
by replacing two old incidences with fresh singleton incidences.

Fresh nodes cannot carry two old candidates at this unchanged seed:
each pair difference already has its three distinct roots on the
original fourteen-node domain. This also rules out replacing four old
incidences by two fresh double incidences at the same seed.

This is a rank bound, not a mixed-characteristic nonexistence theorem.
A singular or ramified lifting branch, or a deformation to another
special-fiber point before lifting, remains possible. Smoothness of a
lower-codimension component with genuine equation dependencies would
need an additional argument; it is not supplied by the naive full-row-
rank Jacobian test.
