PYTHON ?= python3

.PHONY: all paper verify clean

all: paper

paper:
	latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex

verify:
	$(PYTHON) checks/actual_list_tightened_check.py
	$(PYTHON) checks/actual_list_chain_check.py
	$(PYTHON) checks/actual_list_chain_conditional_audit.py
	$(PYTHON) checks/astra_rs_all_surplus_check.py
	$(PYTHON) checks/actual_list_global_small_check.py
	$(PYTHON) checks/verify_puncturing_bound.py
	$(PYTHON) checks/astra_syndrome_determinants_check.py
	$(PYTHON) checks/verify_conditional_moments.py
	$(PYTHON) moment_certificates/verify_weights.py
	$(PYTHON) moment_certificates/verify_concentration.py

clean:
	latexmk -c paper.tex
