import psycopg2


def connect():
    return psycopg2.connect( user='postgres',
                      password='1234',
                      database='learning',
                      host='localhost',
                      port=5433 )