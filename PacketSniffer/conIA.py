import socket
import struct

# Paso 1: Crear un socket RAW para capturar paquetes IP
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

# Paso 2: Cambia "TU_IP" por la IP local de tu adaptador de red
s.bind(("192.168.1.100", 0))  # Ejemplo: reemplázala con tu IP

# Paso 3: Incluir cabeceras IP completas
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# Paso 4: Activar captura de todos los paquetes
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# Paso 5: Recibir un paquete
data_recv, _ = s.recvfrom(65565)

# Paso 6: Desempaquetar los primeros 20 bytes de la cabecera IP
ip_header = struct.unpack('6H4s4s', data_recv[:20])

# Paso 7: Convertir IPs de binario a formato legible
ip_origen = socket.inet_ntoa(ip_header[6])
ip_destino = socket.inet_ntoa(ip_header[7])

print("IP Origen:", ip_origen)
print("IP Destino:", ip_destino)

# Paso 8: Desactivar la captura
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
