start:
	poetry run python app/main.py

migrate:
	sqitch deploy db:pg://test:test@localhost:5432/test --cd migrations
