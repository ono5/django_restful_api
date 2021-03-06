from psycopg2 import pool

# コネクションプールは、アプリケーションからのリクエストごとにデータベースへ接続するのではなく、
# アプリケーション側である程度、接続を保持する仕組み


class Database( object ):
    __connection_pool = None

    @classmethod
    def initialise(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool( 1,
                                                           10,
                                                           **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn( connection )

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()


class CursorFromConnectionFromPool(object):
    def __init__(self):
        self.connection = None
        self.cursor = None

    # with 文に入った時に呼ばれる
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    # with 文を抜ける時に呼ばれる
    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None: # e.g. TypeError, AttributeError, ValueError
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        # 接続不要の場合は、コネクションプールに接続を戻す
        Database.return_connection(self.connection)
