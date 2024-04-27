import socket
import threading
HEADER = 64
PORT = 5000
# SERVER = "192.168.0.7"
SERVER = socket.gethostbyname(socket.gethostname()) # GETS THE NAME AUTOMATICALLY
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONECT"



socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # STREAM DATA THROUGH THE SOCKET
socket_server.bind(ADDR) #We bound the socket with the ADDR

def handle_client(conn, addr):
    print(f" [NEW CONNECTION ] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decoder(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decoder(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
        print(f"[{addr}] {msg}")

    conn.close()
def start():
    socket_server.listen()
    print(f" LISTENING  Server is on {SERVER}")
    while True:
        conn, addr = socket_server.accept()  # Waits for an incoming connection
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

print("[STARTING] server is starting...")
start()