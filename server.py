from socket import *
server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", server_port))
server_socket.listen(1)
print("the server is ready to listen.")
while True:
    connection_socket, address = server_socket.accept()
    inbox = connection_socket.recv(1024).decode()
    print(inbox)
    reply = input("write a reply: ") + "\r"
    connection_socket.send(reply.encode())
    connection_socket.close()
