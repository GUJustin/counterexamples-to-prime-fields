PYTHON ?= python3

.PHONY: all paper reports verify clean

all: paper

paper:
	latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex

reports:
	cd reports && latexmk -pdf -interaction=nonstopmode -halt-on-error stwo-zk-disclosure-summary.tex

verify:
	$(PYTHON) checks/actual_list_tightened_check.py
	$(PYTHON) checks/actual_list_chain_check.py
	$(PYTHON) checks/actual_list_chain_conditional_audit.py
	$(PYTHON) checks/astra_rs_all_surplus_check.py
	$(PYTHON) checks/actual_list_global_small_check.py
	$(PYTHON) checks/verify_puncturing_bound.py
	$(PYTHON) checks/verify_curve_puncturing.py
	$(PYTHON) checks/astra_syndrome_determinants_check.py
	$(PYTHON) checks/verify_conditional_moments.py
	$(PYTHON) moment_certificates/verify_weights.py
	$(PYTHON) moment_certificates/verify_concentration.py
	$(PYTHON) checks/check_gram_ellipsoid.py
	$(PYTHON) research/gram_norm/verify_gram_norm.py
	$(PYTHON) research/ellipsoid_bound/verify_lattice_bound.py
	$(PYTHON) research/gaussian_bound/verify_gaussian_hypotheses.py
	$(PYTHON) research/growing_m/verify_growing_m.py
	$(PYTHON) research/growing_m/verify_wide_regime.py
	$(PYTHON) research/curve_audit/verify_curve_endpoint.py
	$(PYTHON) research/curve_audit/verify_formal_degree.py
	$(PYTHON) research/puncturing_improvement/verify_support_incidence.py
	$(PYTHON) research/structured_domains/verify_transfer_limits.py
	$(PYTHON) research/structured_domains/frobenius_index/verify_rational_frobenius_index.py
	$(PYTHON) research/structured_domains/frobenius_index/verify_balanced_rational_pencils.py
	$(PYTHON) research/structured_domains/frobenius_index/check_near_balanced.py
	$(PYTHON) research/structured_domains/general_cubic_packets/verify.py
	$(PYTHON) research/fixed_gap_padding/verify_anchored_padding.py
	$(PYTHON) research/fixed_gap_padding/verify_prescribed_gap.py
	$(PYTHON) research/fixed_gap_padding/verify_unique_padding.py
	$(PYTHON) research/fixed_gap_padding/verify_unique_far_padding.py
	$(PYTHON) research/fixed_gap_padding/verify_multi_match_far_padding.py
	$(PYTHON) research/fixed_gap_padding/verify_far_concurrency.py
	$(PYTHON) research/fixed_gap_padding/verify_multi_match_finite.py
	$(PYTHON) research/fixed_gap_padding/verify_gap_scale_far.py
	$(PYTHON) research/fixed_gap_padding/verify_density_separation_tradeoff.py
	$(PYTHON) research/fixed_gap_padding/verify_slow_separation.py
	$(PYTHON) research/paired_domain_warp/verify_geometry.py
	$(PYTHON) research/paired_domain_warp/verify_finite.py
	$(PYTHON) research/paired_domain_warp/verify_parity.py
	$(PYTHON) research/paired_domain_warp/verify_joint_images.py
	$(PYTHON) research/paired_domain_warp/verify_multiblock_finite.py
	$(PYTHON) research/paired_domain_warp/audit_multiblock_independent.py
	$(PYTHON) research/paired_domain_warp/verify_sample.py
	$(PYTHON) research/paired_domain_warp/verify_completion.py
	$(PYTHON) research/paired_domain_warp/audit_completion_independent.py
	$(PYTHON) research/paired_domain_warp/audit_optimized_completion.py
	$(PYTHON) research/paired_domain_warp/verify_translate_identity.py
	$(PYTHON) research/paired_domain_warp/check_small_completion.py
	$(PYTHON) research/paired_domain_warp/verify_completed_sample.py
	$(PYTHON) research/paired_domain_warp/verify_extension_profile.py
	$(PYTHON) research/paired_domain_warp/check_far_inputs.py
	$(PYTHON) research/paired_domain_warp/check_far_mixtures.py
	$(PYTHON) research/paired_domain_warp/check_curve_profiles.py
	$(PYTHON) research/paired_domain_warp/m31_exact/verify.py
	$(PYTHON) research/paired_domain_warp/m31_exact/verify_local_lists.py
	$(PYTHON) research/paired_domain_warp/verify_unique_geometry.py
	$(PYTHON) research/paired_domain_warp/powers_two/check.py
	$(PYTHON) research/paired_domain_warp/powers_two/verify.py
	$(PYTHON) research/paired_domain_warp/powers_two/check_two_levels.py
	$(PYTHON) research/paired_domain_warp/powers_two/check_two_adic.py
	$(PYTHON) research/orbit_unique/verify_parameters.py
	$(PYTHON) research/orbit_unique/check_small.py
	$(PYTHON) research/orbit_unique/verify.py
	$(PYTHON) research/orbit_unique/verify_random.py
	$(PYTHON) research/orbit_unique/check_random_geometry.py
	$(PYTHON) research/orbit_unique/verify_kummer.py
	$(PYTHON) research/orbit_unique/check_kummer_small.py
	$(PYTHON) research/two_orbit_unique/verify_finite.py
	$(PYTHON) research/two_orbit_unique/verify_short.py
	$(PYTHON) research/two_orbit_unique/verify_short_rate.py
	$(PYTHON) research/two_orbit_unique/check_exhaustive.py
	$(PYTHON) research/two_orbit_unique/check_negative.py
	$(PYTHON) research/two_orbit_unique/check_formal.py
	$(PYTHON) research/two_orbit_unique/check_concentration.py
	$(PYTHON) research/two_orbit_unique/check_tradeoff.py
	$(PYTHON) research/two_orbit_unique/check_degree_cutoff.py
	$(PYTHON) research/two_orbit_unique/check_integer.py
	$(PYTHON) research/cubic_domain_warp/verify_geometry.py
	$(PYTHON) research/cubic_domain_warp/verify_finite_certificate.py
	$(PYTHON) research/cubic_domain_warp/audit_finite_independent.py
	$(PYTHON) research/cubic_domain_warp/verify_randomized_bound.py
	$(PYTHON) research/cubic_domain_warp/verify_sampling_identity.py
	$(PYTHON) research/cubic_domain_warp/verify_sample.py
	$(PYTHON) research/fixed_gap_padding/verify_vanishing_rate_density.py
	$(PYTHON) research/fixed_gap_padding/verify_constant_code_density.py
	$(PYTHON) research/fixed_gap_padding/verify_polynomial_fields.py
	$(PYTHON) research/fixed_gap_padding/verify_average_padding.py
	$(PYTHON) research/fixed_gap_padding/verify_dense_padding.py
	$(PYTHON) research/fixed_gap_padding/verify_near_unit_density.py
	$(PYTHON) research/fixed_gap_padding/audit_density_independent.py
	$(PYTHON) research/fixed_gap_padding/verify_dense_half_rate.py
	$(PYTHON) research/fixed_gap_padding/verify_far_point_padding.py
	$(PYTHON) research/linear_differential_mca/verify.py
	$(PYTHON) research/spectral_riccati/verify_constant.py
	$(PYTHON) research/spectral_riccati/verify_weighted.py
	$(PYTHON) research/power_family_mca/verify_family.py
	$(PYTHON) research/power_family_mca/verify_wronskian.py
	$(PYTHON) research/power_family_mca/verify_mca.py
	$(PYTHON) research/power_family_mca/verify_parameters.py
	$(PYTHON) research/bounded_root_mca/verify_wronskian.py
	$(PYTHON) research/bounded_root_mca/verify_clusters.py
	$(PYTHON) research/first_order_actual_components/verify_reconstruction.py
	$(PYTHON) research/first_order_actual_components/verify_curve_family.py
	$(PYTHON) research/first_order_actual_components/verify_isolated_family.py
	$(PYTHON) research/quasilinear_first_order/verify.py
	$(PYTHON) research/isolated_solution_sharpness/verify_reconstruction.py
	$(PYTHON) research/isolated_solution_sharpness/verify_family.py
	$(PYTHON) research/actual_higher_order_components/verify.py
	$(PYTHON) research/actual_higher_order_components/verify_fixed_fiber.py
	$(PYTHON) research/inverse_bernoulli/verify.py
	$(PYTHON) research/riccati_cross_ratio/verify.py
	$(PYTHON) research/riccati_cross_ratio/verify_multiplicities.py
	$(PYTHON) research/riccati_cross_ratio/verify_boundary_extension.py
	$(PYTHON) research/riccati_cross_ratio/boundary_search/verify_family.py
	$(PYTHON) research/logarithmic_length_lines/verify.py
	$(PYTHON) research/prime_exponent_coefficients/verify.py
	$(PYTHON) research/dickson_fixed_gap/verify.py
	$(PYTHON) research/binary_affine_locator/verify.py
	$(PYTHON) research/binary_affine_locator/check_codimension_two_transfer.py
	$(PYTHON) research/binary_affine_locator/check_multiplicative_orbit_transfer.py
	$(PYTHON) research/binary_affine_locator/check_multiplicative_label_rigidity.py
	$(PYTHON) research/structured_domains/verify_balanced_fibers.py
	$(PYTHON) research/gram_norm/verify_balanced_fibers.py
	$(PYTHON) research/structured_domains/verify_galois_fibers.py
	$(PYTHON) research/gram_norm/verify_galois_boundaries.py
	$(PYTHON) research/finite_weights/verify_chebyshev.py
	$(PYTHON) research/finite_weights/verify_certificates.py
	$(PYTHON) radial_certificates/verify_publication.py

clean:
	latexmk -c paper.tex

.PHONY: verify-overnight
verify: verify-overnight
verify-overnight:
	$(PYTHON) research/overnight_2026-09-16/verify.py

.PHONY: verify-rational-envelope verify-projective-envelope verify-rational-path verify-proth-frontier
verify: verify-rational-envelope verify-projective-envelope verify-rational-path verify-proth-frontier
verify-rational-envelope:
	$(PYTHON) research/prime_field_tightness/check_rational_envelope.py
verify-projective-envelope:
	$(PYTHON) research/prime_field_tightness/check_projective_envelope.py
verify-rational-path:
	$(PYTHON) research/prime_field_tightness/check_rational_path.py
verify-proth-frontier:
	$(PYTHON) research/two_orbit_unique/verify_proth_frontier.py

.PHONY: verify-cyclic-boundary verify-prime-list-amplification
verify: verify-cyclic-boundary verify-prime-list-amplification
verify-cyclic-boundary:
	$(PYTHON) research/prime_field_tightness/check_cyclic_boundary.py
verify-prime-list-amplification:
	$(PYTHON) research/prime_field_tightness/check_prime_boundary_amplification.py

.PHONY: verify-two-coset-candidates
verify: verify-two-coset-candidates
verify-two-coset-candidates:
	$(PYTHON) research/two_coset_candidate_lists/verify.py

.PHONY: verify-binomial-branch-classification verify-binomial-branch-fixtures
verify: verify-binomial-branch-classification
verify-binomial-branch-classification:
	$(PYTHON) research/two_coset_candidate_lists/check_branch_classification.py
# Optional research fixtures use NumPy; FFT output is diagnostic only.
verify-binomial-branch-fixtures:
	$(PYTHON) research/two_coset_candidate_lists/check_branches.py
