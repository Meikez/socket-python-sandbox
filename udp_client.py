#UDP CLIENT SIDE
import socket

#Create a UDP Ipv4 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send some information via a connectinsless protocol
address_to = (socket.gethostbyname(socket.gethostname()), 5000)
client_socket.sendto("Hello are you there?".encode("utf-8"), address_to)
