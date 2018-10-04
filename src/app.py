import tkinter
import platform

from main_window import *

def main():

    root = Tk()
    root.title('Python Chat')
    root.geometry('800x600')

    main_window = MainWindow(root)
    main_window.pack(expand = True, fill = BOTH)

    root.mainloop()

if __name__ == '__main__': main()
