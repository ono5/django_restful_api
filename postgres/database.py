from psycopg2 import pool

# コネクションプールは、アプリケーションからのリクエストごとにデータベースへ接続するのではなく、
# アプリケーション側である程度、接続を保持する仕組み

connection_pool = pool.SimpleConnectionPool( 1,
                                             1,
                                             database='learning',
                                             user='postgres',
                                             password="1234",
                                             host="localhost",
                                             port=5433 )


class ConnectionFromPool( object ):
    def __init__(self):
        self.connection = None

    # with 文に入った時に呼ばれる
    def __enter__(self):
        self.connection = connection_pool.getconn()
        return self.connection

    # with 文を抜ける時に呼ばれる
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        # 接続不要の場合は、コネクションプールに接続を戻す
        connection_pool.putconn(self.connection)
