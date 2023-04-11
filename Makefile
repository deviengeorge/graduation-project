.PHONY: test serve

test:
	python3 manage.py test --failfast --keepdb

serve:
	python3 manage.py runserver