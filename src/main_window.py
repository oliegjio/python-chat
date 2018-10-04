from tkinter import *

from buttons_row import *
from address_row import *
from client import *

class MainWindow(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)

        self.root = root

        self.server_address = 'localhost'
        self.server_port = 8000

        self.messages = Text(root)
        self.messages.pack(fill = BOTH)

        self.message_entry = Entry(root)
        self.message_entry.pack(fill = BOTH)

        self.buttons_row = ButtonsRow(self)
        self.buttons_row.pack(fill = BOTH)

        self.address_row = AddressRow(self)
        self.address_row.pack(fill = BOTH)

        root.bind('<<Connect>>', self.connect)
        root.bind('<<NewAddress>>', self.new_address)
        root.bind('<<Send>>', self.send)
        root.bind('<<Disconnect>>', self.disconnect)

    def send(self, event):
        self.client.send(self.message_entry.get())

    def connect(self, event):
        self.client = Client(self.server_port, self.server_address)

    def new_address(self, event):
        self.server_address = self.address_row.address_edit.get()
        self.server_port = int(self.address_row.port_edit.get())

    def disconnect(self, event):
        self.client.close()
