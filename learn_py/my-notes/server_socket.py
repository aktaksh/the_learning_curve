import socket 
HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen((1))
print(f"Server listning in {HOST}, {PORT}")
client_socket, client_address = server.accept()
message = client_socket.recv(1024).decode()
print("Received:", message)
client_socket.send(message.encode())
client_socket.close()
server.close()