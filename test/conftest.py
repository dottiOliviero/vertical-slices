from contextlib import contextmanager

import psycopg2
import pytest
from fastapi.testclient import TestClient
from psycopg2.extras import RealDictCursor

from app.conf import settings
from app.server.factory import create_server


@pytest.fixture
def client():
    app = create_server()
    with TestClient(app) as c:
        yield c


@pytest.fixture
def get_cursor_generator_test():
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
            conn.rollback()
            cur.close()
        conn.close()
    return cursor_generator
