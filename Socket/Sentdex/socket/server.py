#https://www.youtube.com/watch?v=Lbfe3-v7yE0&t=20s
import socket
import time

HEADERSIZE = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 1234))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established")

    message = "Welcome to the server!"
    message =f'{len(message):<{HEADERSIZE}}' + message

    client_socket.send(bytes(message,"utf-8"))

    while True:
        time.sleep(3)
        message = f"the time is {time.time()}"
        message = f'{len(message):<{HEADERSIZE}}' + message
        client_socket.send(bytes(message, "utf-8"))

#client_socket.send(bytes("Welcome to the server!", "utf-8"))
#client_socket.close()

