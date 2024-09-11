from contextlib import contextmanager

import psycopg2
from psycopg2.extras import RealDictCursor

from app.conf import settings


@contextmanager
def cursor_generator():
    conn = psycopg2.connect(database=settings.POSTGRES_DB, user=settings.POSTGRES_USER, password=settings.POSTGRES_PASSWORD, host=settings.POSTGRES_HOST, port=settings.POSTGRES_PORT)
    try:
        cur = conn.cursor(
            cursor_factory = RealDictCursor
        )
        yield cur
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.commit()
        cur.close()
    conn.close()
