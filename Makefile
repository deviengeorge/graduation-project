.PHONY: test serve migrate make-migrations delete-migrations

test:
	python3 manage.py test --failfast --keepdb

serve:
	python3 manage.py runserver

make-migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

delete-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete