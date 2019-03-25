from psycopg2 import pool


# def connect():
#     return psycopg2.connect(user='postgres',
#                             password='1234',
#                             database='learning',
#                             host='localhost',
#                             port=5433)

# コネクションプールは、アプリケーションからのリクエストごとにデータベースへ接続するのではなく、
# アプリケーション側である程度、接続を保持する仕組み
connection_pool = pool.SimpleConnectionPool(1,
                                            10,
                                            database='learning',
                                            user='postgres',
                                            password="1234",
                                            host="localhost",
                                            port=5433)

