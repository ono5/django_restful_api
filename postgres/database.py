from psycopg2 import pool

# コネクションプールは、アプリケーションからのリクエストごとにデータベースへ接続するのではなく、
# アプリケーション側である程度、接続を保持する仕組み


class ConnectionPool( object ):
    def __init__(self):
        self.connection_pool = pool.SimpleConnectionPool(1,
                                                         1,
                                                         database='learning',
                                                         user='postgres',
                                                         password="1234",
                                                         host="localhost",
                                                         port=5433 )

    # with 文に入った時に呼ばれる
    def __enter__(self):
        return self.connection_pool.getconn()

    # with 文を抜ける時に呼ばれる
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
