from tkinter import *


class ButtonsRow(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)

        self.root = root

        self.connect_button = Button(self, text = 'Connect')
        self.connect_button.pack(side = LEFT, fill = BOTH, expand = True)
        self.connect_button.bind('<Button-1>', self.connect_button_click)

        self.disconnect_button = Button(self, text = 'Disconnect')
        self.disconnect_button.bind('<Button-1>', self.disconnect_button_click)
        self.disconnect_button.pack(side = LEFT, fill = BOTH, expand = True)

        self.send_button = Button(self, text = 'Send')
        self.send_button.bind('<Button-1>', self.send_button_click)
        self.send_button.pack(side = LEFT, fill = BOTH, expand = True)

    def connect_button_click(self, event):
        self.root.event_generate('<<Connect>>')

    def send_button_click(self, event):
        self.root.event_generate('<<Send>>')

    def disconnect_button_click(self, event):
        self.root.event_generate('<<Disconnect>>')
