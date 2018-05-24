TESTS=$(wildcard tests/*.py)

.PHONY: test
test:	
	@- $(foreach TEST,$(TESTS), \
			echo === Running test: $(TEST); \
			python -m unittest $(TEST); \
		)

test_create_table:
	python -m unittest tests/create_table.py
