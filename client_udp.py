import socket

def client_udp():
    #Create the socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #IP address and port number of the server
    server_ip = '127.0.0.1'
    port = 8080

    try:
        while True:
            # Request the user to input a message
            message = input("Digite a mensagem que deseja enviar ao servidor: ")

            # Send the message to the server
            client_socket.sendto(message.encode('utf-8'), (server_ip, port))

            # Receive the response from the server
            data, server_ip = client_socket.recvfrom(4096)
            print(f"Resposta do servidor: {data.decode()}")
    
    except socket.error as err:
        print(f"Erro ao enviar/receber dados: {err}")
    
    finally:
        print("Fechando a conexão")
        client_socket.close()

if __name__ == '__main__':
    client_udp()