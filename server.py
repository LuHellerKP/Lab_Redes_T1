import socket

host = '127.0.0.1'
port = 8080

#socket.AF_INET = IPV4
#socket.SOCK_STREAM = TCP -> socket type
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket do servidor criado com sucesso")

#bind
#Associate host/IP address and port number
try:
    server_socket.bind((host, port))
except socket.error as e:
    print("Erro ao criar o socket: ", e)
    exit()
print("Socket bind completo")

#listen for connections
server_socket.listen(10)
print(f"Server começou, escutando em {host}:{port}")


#accept incoming connections
#accept() returns a new socket object representing the connection and a tuple holding the address of the client
client_socket, client_address = server_socket.accept()
print(f"Nova conexão de {client_address[0]}:{client_address[1]}")

#recieve data from client
#max buffer size
buffer_size = 4096
data = client_socket.recv(4069).decode()

print(f"Dados recebidos {data}")

#send back the same message to the client
client_socket.send(data.upper().encode())
server_socket.close()