import socket

def client_tcp():

    #Create the socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to the server
    server_ip = '127.0.0.1'
    port = 8080

    try:
        client_socket.connect((server_ip, port))
        print(f"Conectado ao servidor {server_ip}:{port}")

        while True:
            # Request the user to input a message
            message = input("Digite a mensagem que deseja enviar ao servidor: ")

            # Send the message to the server
            client_socket.sendall(message.encode('utf-8'))

            # Receive the response from the server
            data = client_socket.recv(4096)
            print(f"Resposta do servidor: {data.decode()}")

    except socket.error as err:
        print(f"Erro ao conectar ao servidor: {err}")

    finally:
        print("Fechando a conexão")
        client_socket.close()

if __name__ == '__main__':
    client_tcp()