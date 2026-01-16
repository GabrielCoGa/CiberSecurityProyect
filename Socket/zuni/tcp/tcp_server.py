#TCP Server Side
import socket

#Create a server side socket using IPV4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#See how to get IP address dynamically
print(f"Socket Server name:{ server_socket.getsockname()}")
print(f"Host Server name: {socket.gethostname()}")

print(f"IP Address Server: {socket.gethostbyname(socket.gethostname())}")

#Bind our new socket to a tuple (IP Address, Port Address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

#Put the socket into listening mode to listen for any possible connections
server_socket.listen()

#Listen forever to ANY connection
while True:
    #Accept every single conecction and store two pieces of information
    client_socket, client_address = server_socket.accept()
    print(type(client_socket))
    print(f"Client Socket: {client_socket}")
    print(type(client_address))
    print(f"Client address: {client_address}")
    print(f"Server received from: {client_address}")

    #Send a message to the just connected
    client_socket.send("Hello, client!".encode("utf-8"))

    server_socket.close()
    break

