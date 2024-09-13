import socket

host = '127.0.0.1'
port = 8080

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket do cliente criado com sucesso')

# Connect to the server
try:
    client_socket.connect((host, port))
    print(f"Conectado ao servidor {host}:{port}")
except socket.error as err:
    print(f"Erro ao conectar ao servidor: {err}")
    exit()

# Send some data to the server
message = input("Digite a mensagem que deseja enviar ao servidor: ")
client_socket.send(message.encode())

# Receive data from the server
response = client_socket.recv(4096).decode()
print(f"Resposta do servidor: {response}")

# Close conection
client_socket.close()