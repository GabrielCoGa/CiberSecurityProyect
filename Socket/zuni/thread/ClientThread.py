#Client Side Chat Rooms
import socket,threading
#https://www.youtube.com/watch?v=7gek0eCnbHs&t=5927s

#Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

def send_message():
    #Send a message to the server to be broadcast
    pass

def receive_message():
    #Recieve an incoming message from the server
    pass

