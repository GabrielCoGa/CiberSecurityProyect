# UDP Server side
import socket

#Create a server side socket IPV4 (AF_INET) and UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bindour new socket to a tuple (Ip address, por address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# we are not listening or accepting connections since UPD is a conectionless protocol
message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
print(address)

#server_socket.close()

