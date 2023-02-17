from app.database import cursor_generator
from psycopg2.sql import SQL, Identifier
from .models import CreateCatRequestBody

CREATE_CAT_BASE_QUERY = "INSERT INTO {} (name, age, color) VALUES (%s,%s,%s) RETURNING *"

def create_cat(cat:CreateCatRequestBody):
    created_cat = None
    with cursor_generator() as cursor:
        print('going to insert cat {cat}'.format(cat=cat))
        cursor.execute(SQL(CREATE_CAT_BASE_QUERY).format(Identifier('cat')), tuple(cat.values()))
        created_cat = cursor.fetchone()
    return created_cat
