#Client chat Side
import socket
from symtable import Class

#Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

#Creatge a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

#Send/Recieve message
while True:
    #Recieve information from the server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    #Quit if the connected server wants to quit, else keep sending messages
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat....goodbye!")
        break
    else:
        print("\n" + message)
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

#Close the cliente socket
client_socket.close()




