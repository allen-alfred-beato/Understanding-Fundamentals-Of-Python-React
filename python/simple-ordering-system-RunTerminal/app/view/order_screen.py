from tkinter import *
# from tkinter import ttk


class DisplayInterface:
    
    def __init__(self):               
        self.root = Tk()
        self.root.geometry("460x460")
        self.root.title("BENG-POS")
        
    def run(self):
        self.root.mainloop()

    def orderInterface(self):
        label = Label(self.root, text="This is a Label!")
        label.pack()
        entry = Entry(self.root, fg="black")
        entry.insert(0,"What is your name? ")
        
        entry.pack()
        
        self.run()
        
        
