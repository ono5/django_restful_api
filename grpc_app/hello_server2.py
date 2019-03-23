import time

import grpc
import psycopg2

from concurrent import futures
from hello_pb2 import returnHello
from hello_pb2_grpc import HelloServicer, add_HelloServicer_to_server

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class PersonHelloServicer(HelloServicer):
    def save_to_db(self, msg):
        with psycopg2.connect(user='postgres',
                              password='1234',
                              database='learning',
                              host='localhost',
                              port=5433) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO grpc_app_hello (message) VALUES ('{msg}')")

    """Create Service"""
    def Reply(self, request, context):
        print('replay!')
        self.save_to_db(request.msg)
        return returnHello(msg='OK')

def serve():
    # Create worker with 10
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add custom service to original service
    add_HelloServicer_to_server(
        PersonHelloServicer(), server)
    # Define port to accept request from client
    server.add_insecure_port('localhost:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
