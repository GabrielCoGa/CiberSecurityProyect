#Server Side Chart Room
import socket, threading
#https://www.youtube.com/watch?v=7gek0eCnbHs&t=5927s

#Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

#Create two blank lists to store connected client sockets and their names
client_socket_list = []
client_name_list = []

def broadcast_message(message):
    #Send a message to all clients connected to the server
    pass

def recieve_message(client_socket):
    #Recieve an incoming message from a specific client  and forward the message to be broadcast
    pass

def connect_client():
    #Connect an incoming client to the server
    pass


