import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)

host = input("Enter the IP you want to scan: ")
port = int(input("Enter the port you want to scan: "))

def scan_port(port):
    if s.connect_ex((host, port)):
        print(f"The port is closed on host: {host} and port: {port}")
    else:
        print(f"The port is opened on host: {host} and port: {port}")


scan_port(port)
