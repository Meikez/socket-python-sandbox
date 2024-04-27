# TCP SERVER SIDE

import socket

#Create a server side socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# See how to get IP address dynamically

print(socket.gethostname()) # my hostname
print(socket.gethostbyname(socket.gethostname()))
CONFIG = (socket.gethostbyname(socket.gethostname()), 4000)


#Bind our new socke to a tuple (IP Address, Port address)
server_socket.bind(CONFIG)

#Put the socket into listening modo to listen for any possible conections
server_socket.listen()

#Listen forever to accept ANY coonection
while True:
    #Accept every single connection and store two pieces of information
    client_socket, client_address = server_socket.accept()
    print(type(client_socket))
    print(client_socket)
    print(type(client_address))
    print(client_address)

    print(f"[ CONNECTED TO {client_address} ]")

    #Send a message to the client that just connected
    client_socket.send("Your connection was success!".encode("utf-8"))

    #Close the connection
    server_socket.close() # it would be an error because the loop continues an the accept() will fail
    break # Fix the .close() stopping the loop

