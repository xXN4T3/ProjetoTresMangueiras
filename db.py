import psycopg2 as postgresql
from psycopg2.extras import DictCursor


class Database():

    def __init__(self) -> None:
        try:
            self.connection = postgresql.connect("""dbname='ONG'
                                                    host='localhost'
                                                    port=5432
                                                    user='postgres'
                                                    password='root'
                                                    """)
            self._cursor = self.connection.cursor(
                cursor_factory=DictCursor)
        except Exception as E:
            print(f'Erro: {str(E)}')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close(False)

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self._cursor.execute(sql, params or ())

    def fetchone(self):
        return self._cursor.fetchone()

    def fetchall(self):
        return self._cursor.fetchall()

    def queryone(self, sql, params=None):
        self._cursor.execute(sql, params or ())
        return self.fetchone()

    def query(self, sql, params=None):
        self._cursor.execute(sql, params or ())
        return self.fetchall()
