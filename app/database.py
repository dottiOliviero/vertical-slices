import psycopg2
import psycopg2.extras
from app.conf import settings
from contextlib import contextmanager

@contextmanager
def cursor_generator():
    conn = psycopg2.connect(database=settings.POSTGRES_DB, user=settings.POSTGRES_USER, password=settings.POSTGRES_PASSWORD, host='localhost')
    try:
        cur = conn.cursor(
            cursor_factory = psycopg2.extras.RealDictCursor
        )
        yield cur
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.commit()
        cur.close()
    conn.close()
