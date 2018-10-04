from tkinter import *


class AddressRow(Frame):

    default_address = 'localhost'
    default_port = '8000'

    def __init__(self, root):
        Frame.__init__(self, root)

        self.root = root

        self.address_label = Label(self, text = 'Address: ')
        self.address_label.pack(side = LEFT)

        self.address_edit = Entry(self)
        self.address_edit.insert(0, self.default_address)
        self.address_edit.pack(side = LEFT, expand = True, fill = BOTH)

        self.port_label = Label(self, text = 'Port: ')
        self.port_label.pack(side = LEFT)

        self.port_edit = Entry(self)
        self.port_edit.insert(0, self.default_port)
        self.port_edit.pack(side = LEFT, expand = True, fill = BOTH)

        self.save_button = Button(self, text = 'Save')
        self.save_button.bind('<Button-1>', self.save_button_click)
        self.save_button.pack(side = LEFT)

    def save_button_click(self, event):
        self.root.event_generate('<<NewAddress>>')
