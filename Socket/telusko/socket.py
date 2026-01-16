import socket

sock = socket.socket()
print("Socket created")

sock.bind(('localhost', 9999))
sock.listen(3)
print("Socket now listening")
while True:
    conn, addr = sock.accept()
    print("Connection accepted with", addr)
    print("Connection accepted with", conn)

    name = conn.recv(1024).decode()
    print(f"hello {name}")

    conn.send(bytes('Welcome to Telesko', 'utf-8' ))
    conn.close()

