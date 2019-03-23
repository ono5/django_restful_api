import django
import os
import sys
import time

import grpc
from concurrent import futures
from hello_pb2 import returnHello
from hello_pb2_grpc import HelloServicer, add_HelloServicer_to_server

sys.path.append('/Users/hono/Desktop/django_restful_api')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfeapi.settings')

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class PersonHelloServicer(HelloServicer):
    """Create Service"""
    def Reply(self, request, context):
        django.setup()
        from models import Hello
        print('replay!')
        print(request.msg)
        Hello.objects.create(message=request.msg)
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
