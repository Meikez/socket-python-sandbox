# TCP CLIENT SIDE
import socket
CONFIG = (socket.gethostbyname(socket.gethostname()), 4000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socketto a server located at a given IP and Port

client_socket.connect(CONFIG) # Is the same CONFIG of the server because is the same device

#Recieve a message from the server ... You must specify the max number of bytes to recieve
message = client_socket.recv(1024)
print(message.decode("utf-8"))


#close the client socket
client_socket.close()