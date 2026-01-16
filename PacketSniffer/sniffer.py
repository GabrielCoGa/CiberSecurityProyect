# https://youtu.be/O9oryV-lGEI?si=ALrYjG1_4Fjl1tSh

import socket
import os
import struct
import sys
import binascii

sock_created = False
sniffer_socket = 0


def analyze_tcp_header(data_recv):
    tcp_hdr = struct.unpack('2H2I4H', data_recv[:20])
    # https://en.wikipedia.org/wiki/Transmission_Control_Protocol


def analyze_ip_header(data_recv):
    # https://en.wikipedia.org/wiki/IPv4
    ip_hdr = struct.unpack('6H4s4s', data_recv[:20])
    ver = ip_hdr[0] >> 12  # Version
    ihl = (ip_hdr[0] >> 8) & 0x0f  # Header Length
    tos = ip_hdr[0] & 0x00ff  # Service Type
    tot_len = ip_hdr[1]  # Total Length
    ip_id = ip_hdr[2]  # Identification
    flags = ip_hdr[3] >> 13  # Flags
    frag_offset = ip_hdr[3] & 0x1fff  # Fragment Offset
    ip_ttl = ip_hdr[4] >> 8  # ttl
    ip_proto = ip_hdr[4] & 0x00ff  # Protocol
    checksum = ip_hdr[5]  # checksum
    # https://docs.python.org/3/library/socket.html
    src_address = socket.inet_ntoa(ip_hdr[6])
    dst_address = socket.inet_ntoa(ip_hdr[7])
    data = data_recv[20:]

    print('__________________IP HEADER__________________')
    print("Version: %hu " % ver)
    print("IHL: %hu " % ihl)
    print("TOS: %hu " % tos)
    print("Length: %hu " % tot_len)
    print("ID: %hu " % ip_id)
    print("Offset: %hu " % frag_offset)
    print("TTL: %hu " % ip_ttl)
    print("Proto: %hu " % ip_proto)
    print("Checksum: %hu " % checksum)
    print("Source Ip: %s " % src_address)
    print("Destination IP: %s " % dst_address)

    # https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers
    if ip_proto == 6:
        tcp_udp = "TCP"
    elif ip_proto == 17:
        tcp_udp = "UDP"
    else:
        tcp_udp = "OTHER"

    return data, tcp_udp


def analyze_ether_header(data_recv):
    ip_bool = False
    # https://en.wikipedia.org/wiki/Ethernet_frame
    eth_hdr = struct.unpack('!6s6sH', data_recv[:14])
    dest_mac = binascii.hexlify(eth_hdr[0])  # Dest. Addr.(6 byte)
    src_mac = binascii.hexlify(eth_hdr[1])  # Source Addr (6 byte)
    proto = eth_hdr[2] >> 8  # Ethernet type
    data = data_recv[14:]  # data (42- 1497 byte)

    print('__________________ETHERNET HEADER__________________')
    print("Destination MAC: %s:%s:%s:%s:%s:%s" % (dest_mac[0:2], dest_mac[2:4], dest_mac[4:6], dest_mac[6:8],
                                                  dest_mac[8:10], dest_mac[10:12]))
    print("Source MAC: %s:%s:%s:%s:%s:%s" % (src_mac[0:2], src_mac[2:4], src_mac[4:6], src_mac[6:8], src_mac[8:10],
                                             src_mac[10:12]))
    print("PROTOCOL: %hu" % proto)

    if proto == 0x08:
        ip_bool = True

    return data, ip_bool


def main():
    global sock_created
    global sniffer_socket
    if sock_created == False:
        # para Linux:
        # sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
        # para windows:
        sniffer_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        # socket.PF_PACKET es solo para linux, para windows usamossockets RAW con AF_INET,
        # pero solo para capturar paquetes IP (no Ethernet). usar scapy
        # El valor socket.htons(0x0003) representa todos los protocolos Ethernet (ETH_P_ALL),
        # lo cual es correcto, pero asegúrate de que tu entorno lo interprete adecuadamente.
        """
        import socket

        # Crear socket RAW
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        s.bind(("TU_IP_LOCAL", 0))
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        print("Escuchando paquetes...")
        while True:
            print(s.recvfrom(65565))
        """
        sock_created = True

    data_recv = sniffer_socket.recv(2048)
    os.system('clear')
    data_recv, ip_bool = analyze_ether_header(data_recv)
    analyze_ether_header(data_recv)
    if ip_bool == True:
        data_recv, tcp_udp = analyze_ip_header(data_recv)
    else:
        return

    """if tcp_udp == "TCP":
        data_recv = analyze_tcp_header(data_recv)
    elif tcp_udp == "UDP":
        data_recv = analyze_udp_header(data_recv)
    else:
        return"""


while True:
    main()


