from threading import *
import socket

class ConnectionThread(Thread):

    def __init__(self, connection, client_address):
        Thread.__init__(self)

        self.connection = connection
        self.client_address = client_address

    def run(self):
        while True:
            data = self.connection.recv(1024)

            if data:
                data = data.decode()
                print(data)

                if data == 'e':
                    self.connection.close()
                    break
