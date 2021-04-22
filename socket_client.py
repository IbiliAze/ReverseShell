import socket



class Socket:
    def __init__(self, header, port, format_type, disconnect_message, server):
        self.HEADER = header
        self.PORT = port
        self.FORMAT = format_type
        self.DISCONNECT_MESSAGE = disconnect_message
        self.SERVER = server
        self.ADDR = (self.SERVER, self.PORT)

    def connect(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(self.ADDR)
        return client
    
    def send(self, msg):
        client = self.connect()

        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        client.send(send_length)
        client.send(message)

        return_msg = client.recv(2048).decode(self.FORMAT)
        # print(return_msg)
        return(return_msg)



# HEADER = 64
# PORT = 5050
# FORMAT = 'utf-8'
# DISCONNECT_MESSAGE = '!DISCONNECT'
# SERVER = '169.254.225.208'
# ADDR = (SERVER, PORT)

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)

# def send(msg):
#     message = msg.encode(FORMAT)
#     msg_length = len(message)
#     send_length = str(msg_length).encode(FORMAT)
#     send_length += b' ' * (HEADER - len(send_length))
    
#     client.send(send_length)
#     client.send(message)

#     print(client.recv(2048).decode(FORMAT))

# send('hello world')
# send(DISCONNECT_MESSAGE)