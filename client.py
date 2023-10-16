from socket import *
while True:
    server_name = "your ip"
    server_port = 12000
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    to_be_sent = input("write a message: ") + "\r"
    client_socket.send(to_be_sent.encode())
    reply = client_socket.recv(1024)
    print(f"from your friend: {reply.decode()}")
