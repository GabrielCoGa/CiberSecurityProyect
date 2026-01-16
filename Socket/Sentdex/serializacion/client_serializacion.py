
import socket
import pickle

HEADERSIZE = 10

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 1234))

full_message = b''
new_message = True

while True:
    message = client_socket.recv(16)
    if new_message:
        print(f"new message length: {message[:HEADERSIZE]}")
        messageLength = int(message[:HEADERSIZE])
        new_message = False

    full_message += message

    if len(full_message) - HEADERSIZE == messageLength:
        print("full message received")
        print(full_message[HEADERSIZE:])

        data_dictionary = pickle.loads(full_message[HEADERSIZE:])
        print(f"data_dictionary: {data_dictionary}")

        new_message = True
        full_message = b''

print(full_message)
