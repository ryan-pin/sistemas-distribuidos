import grpc
from concurrent import futures
import calculadora_pb2
import calculadora_pb2_grpc

class CalculatorService(calculadora_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculadora_pb2.OperationResponse(result=result)

    def Subtract(self, request, context):
        result = request.num1 - request.num2
        return calculadora_pb2.OperationResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculadora_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server is running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
