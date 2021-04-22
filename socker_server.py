###################################################################################MODULES
import socket
import threading
##########################################################################################
#
#
#
# Constant Variables
QUEUE_LIMIT = 5
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

# Creating and binding a socket server
def create_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(ADDR)

        return server

    except socket.error as error:
        print(f'[ERROR] {error}')

# Handling client connections
def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{addr}] {msg}')
            conn.send(f"Message received".encode(FORMAT))

    conn.close()

# Starting the socket server
def start():
    try:
        server = create_server()
        server.listen(QUEUE_LIMIT)

        print(f'[STARTED] Server is listening on {SERVER}:{PORT}')

        while True:
            conn, addr = server.accept()
            
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

            print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

    except socket.error as error:
        print(f'[ERROR] {error}')

print(f'[STARTING] Server is starting...')

start()