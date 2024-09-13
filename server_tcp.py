import socket


def tcp_server():
    host = "127.0.0.1"
    port = 8080

    # Create socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket TCP do servidor criado com sucesso")

    # Bind
    try:
        server_socket.bind((host, port))
    except socket.error as error:
        print("Erro ao criar o socket: ", error)
        exit()
    print("Socket bind completo")

    # Listen for connections
    server_socket.listen(10)
    print(f"Servidor TCP começou, escutando em {host}:{port}")

    while True:
        # Accept incoming connections
        client_socket, client_address = server_socket.accept()
        print(f"Nova conexão de {client_address[0]}:{client_address[1]}")

        while True:
            try:
                # Receive data from the client
                data = client_socket.recv(4096).decode()

                if not data:
                    print(f"Conexão encerrada com {client_address}")
                    break  # Conection closed by client

                print(f"Dados recebidos: {data}")

                # Send data back
                client_socket.send(data.upper().encode())

            except socket.error as error:
                print(f"Erro na conexão com {client_address}: {error}")
                break

        client_socket.close()


if __name__ == "__main__":
    tcp_server()


