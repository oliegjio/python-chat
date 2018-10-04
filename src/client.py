import socket

class Client:

    def __init__(self, port, address = 'localhost'):
        self.address = address
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (address, port)
        self.sock.connect(server_address)

    def send(self, message):
        self.sock.sendall(message.encode())

    def close(self):
        self.sock.close()
