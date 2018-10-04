import sys
import socket

from connection_thread import *

def main(argv):
    port = int(argv[0])

    if len(argv) > 1:
        address = argv[1]
    else:
        address = 'localhost'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (address, port)
    sock.bind(server_address)
    sock.listen(1)

    threads = []

    while True:
        connection, client_address = sock.accept()

        new_thread = ConnectionThread(connection, client_address)
        new_thread.start()

        threads.append(new_thread)

    sock.close()

if __name__ == '__main__': main(sys.argv[1:])
