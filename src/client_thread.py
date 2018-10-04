from threading import *
import socket

class ClientThread(Thread):

    def __init__(self, socket):
        Thread.__init__(self)

        self.socket = socket

    def run(self):
        while True:
            data = self.socket.recv(1024)

            
