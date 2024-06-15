.PHONY: test clean

test:
	python3 -m unittest discover -s tests

watch-test:
	watch python3 -m unittest discover -s tests

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
