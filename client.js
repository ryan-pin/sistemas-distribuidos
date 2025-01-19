const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const packageDefinition = protoLoader.loadSync('calculadora.proto', {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});
const calculadoraProto = grpc.loadPackageDefinition(packageDefinition).Calculator;


const client = new calculadoraProto('localhost:50051', grpc.credentials.createInsecure());


client.Add({ num1: 5, num2: 3 }, (error, response) => {
  if (error) console.error('Error:', error);
  else console.log('Addition Result:', response.result);
});

client.Subtract({ num1: 10, num2: 4 }, (error, response) => {
  if (error) console.error('Error:', error);
  else console.log('Subtraction Result:', response.result);
});
