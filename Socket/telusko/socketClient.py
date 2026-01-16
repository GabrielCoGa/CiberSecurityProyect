import socket
sockClient = socket.socket()
sockClient.connect(('localhost', 9999))

name = input("Enter your name: ")

sockClient.send(bytes(name, "utf-8"))

print(sockClient.recv(1024).decode('utf-8'))