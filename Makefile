run:
	poetry run uvicorn main:app --reload

tests:
	poetry run pytest tests -v --cov-report term --cov-report html:htmlcov --cov=.
	