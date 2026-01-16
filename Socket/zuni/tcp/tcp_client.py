#TCP Client Side
import socket

#Create a cliente side IPV4 (AF_INET) and TCP (SOCKET_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to a server located at a given IP and Port
client_socket.connect((socket.gethostbyname(socket.gethostname()),12345))

#Recieve a message from the server... you must specify the max number of bytes to recieve
message = client_socket.recv(1024)

print(f"Object type: {type(message)}")
print(f"fron Server: {message.decode('utf-8')}")

client_socket.close()

