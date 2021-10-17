.PHONY:  all clean test dist upload check_upload

all:
	@echo "Targets:  clean, test, dist, check_upload, upload"

clean:
	rm -f dist/* 
	python setup.py clean --all

test:
	python setup.py build
	python setup.py test

dist: test
	rm -f dist/*
	python setup.py clean
	python setup.py sdist

upload: check_upload
	twine upload dist/*

check_upload:
	twine check dist/*
