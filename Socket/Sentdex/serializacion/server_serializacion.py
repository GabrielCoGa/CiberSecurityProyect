#https://www.youtube.com/watch?v=WM1z8soch0Q
import socket
import pickle

HEADERSIZE = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 1234))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established")

    data_dictionary = {1: "Hey", 2: "There"}
    message = pickle.dumps(data_dictionary)

    message =bytes(f'{len(message):<{HEADERSIZE}}',"utf-8" ) + message

    client_socket.send(message)
