import psycopg2
import psycopg2.extras

import config


class ConnectDB(object):
    conn = None

    def __init__(self):
        self.conn = psycopg2.connect(dbname=config.dbname,
                                     user=config.user,
                                     password=config.password,
                                     host=config.host,
                                     port=config.port)

    def __del__(self):
        if self.conn:
            self.conn.close()

    def cursor(self):
        return self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def find_one(self, query: str) -> dict:
        cursor = self.cursor()
        cursor.execute(query)
        record = cursor.fetchone()
        cursor.close()
        return dict(record)

    def find_all(self, query: str) -> list:
        cursor = self.cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        cursor.close()
        return list(map(lambda row: dict(row), record))

    def find_many(self, query: str, limit: int) -> list:
        cursor = self.cursor()
        cursor.execute(query)
        record = cursor.fetchmany(size=limit)
        cursor.close()
        return list(map(lambda row: dict(row), record))

    def save(self, query: str) -> None:
        cursor = self.cursor()
        cursor.execute(query)
        cursor.close()


if __name__ == '__main__':
    db = ConnectDB()
    query_str = 'SELECT * FROM data.reference_book LIMIT 10'
    print(db.find_one(query_str))
