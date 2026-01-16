#Server chat Side
import socket

#Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

#Create a server socket, bind it to a ip/port, and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

#Accept any incoming connectio and let then know they are connected
print('Server listening...')
client_socket, client_address = server_socket.accept()
#client_socket.send(ENCODER.encode('utf-8'))
client_socket.send("You are connected to the server....\n".encode(ENCODER))

#Send/recieve messages
while True:
    #Recive information from the client
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding thechat...goodbye!")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

#Close socket
server_socket.close()





