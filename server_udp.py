import socket


def udp_server():
    host = "127.0.0.1"
    port = 8080

    # Create socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket UDP do servidor criado com sucesso")

    # Bind
    try:
        server_socket.bind((host, port))
    except socket.error as error:
        print("Erro ao criar o socket: ", error)
        exit()
    print("Socket bind completo")

    print(f"Servidor UDP começou, escutando em {host}:{port}")

    while True:
        try:
            # Receive data from the client
            data, client_address = server_socket.recvfrom(4096)
            print(f"Dados recebidos de {client_address}: {data.decode()}")

            # Send the response back to the client
            server_socket.sendto(data.upper(), client_address)
            
        except socket.error as error:
            print(f"Erro ao receber dados: {error}")
            break
        


if __name__ == "__main__":
    udp_server()
