#https://www.youtube.com/watch?v=Lbfe3-v7yE0&t=20s
import socket

HEADERSIZE = 10

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 1234))

full_message = ''
new_message = True

while True:
    message = client_socket.recv(16)
    if new_message:
        print(f"new message length: {message[:HEADERSIZE]}")
        messageLength = int(message[:HEADERSIZE])
        new_message = False

    full_message += message.decode("utf-8")

    if len(full_message) - HEADERSIZE == messageLength:
        print("full message received")
        print(full_message[HEADERSIZE:])
        new_message = True
        full_message = ''

print(full_message)



