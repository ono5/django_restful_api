import grpc
import hello_pb2
import hello_pb2_grpc


def run(message):
    # Create channel to access to server
    channel = grpc.insecure_channel('localhost:50051')
    # Adopt hello stub
    stub = hello_pb2_grpc.HelloStub(channel)
    response = stub.Reply(hello_pb2.sayHello(msg=message))
    print('Greeter client received: ', response.msg)


if __name__ == '__main__':
    run('hello')
