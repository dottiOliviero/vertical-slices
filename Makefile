migrate:
	poetry run alembic upgrade head

create_migration:
	poetry run alembic revision --autogenerate -m "$(message)"

start:
	poetry run python app/main.py