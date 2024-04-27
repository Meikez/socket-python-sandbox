import  socket

#Create a server side socket IPv4 (AD_INET) and UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind our new socket to a tuple (ip address, por address)

CONFIG = (socket.gethostbyname(socket.gethostname()), 5000)

server_socket.bind(CONFIG)

#We are not listening or accepting connectios isnce UDP is a connectionless protocol

message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
print(address)



