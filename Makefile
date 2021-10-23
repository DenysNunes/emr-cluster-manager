run:
	poetry run uvicorn main:app --reload

test:
	poetry run pytest tests -v --cov-report term --cov-report html:htmlcov --cov=.
	