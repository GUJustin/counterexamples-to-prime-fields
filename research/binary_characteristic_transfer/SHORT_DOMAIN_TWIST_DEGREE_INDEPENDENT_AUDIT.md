# Independent short-domain twist-degree audit

PASS, 2026-09-19. Actual source inspected; no corrections needed.

For nonzero F,G and polynomial residual P=ΛF/G of degree below n, degree subtraction forces e=degG>f=degF. With 0<n<p, n+pf<pe. Thus the exact identity G^p−AG=ΛF^p requires cancellation of the leading degree pe, forcing degA=(p−1)e and lc(A)=lc(G)^(p−1). Since e≥1 and n≤p−1, degA≥n. This includes the boundary n=p−1 correctly and does not need separability or native roots.

The varying-twist example is exact: if G divides Λ and degF<degG, define A=G^(p−1)−(Λ/G)F^p. Then P=(Λ/G)F is polynomial of degree below n and the claimed identity holds. Its second summand has strictly smaller degree than the first by the same inequality. Therefore this gate forbids low-degree twists only; it does not forbid high-degree witness-dependent twists or provide a shared received pencil. The source explicitly preserves this distinction and correctly separates fixed-A family bounds.

Frozen source SHA256: `ad0cf8a8e195e42e12488e718f49ceaee5f3fc0fa7174241ec03baa2e7cdc8a8`.
