import socket
from threading import Thread
from queue import Queue

class Client:

    def __init__(self, port, address = 'localhost'):
        self.address = address
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.address, self.port))

        self.queue = Queue()

        self.client_thread = Thread(target = self.thread, args = (self.queue))
        self.client_thread.start()

    def thread(self, queue):
        pass

    def send(self, message):
        self.sock.sendall(message.encode())

    def close(self):
        self.client_thread.join()
        self.sock.close()
