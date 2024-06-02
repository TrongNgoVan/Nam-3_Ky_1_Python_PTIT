from tkinter import *
def main():
    root = Tk()
    hello = Label(root,text="Hello world!")
    hello.grid(row=0,column=0)
    a_label1 = Label(root, text = "A Label widget in a window")
    a_label1.grid(row=1,column=1)
    a_label2 = Label(root, text = "Another one")
    a_label2.grid(row=2,column=1)
    a_label3 = Label(root, text = "And more!")
    a_label3.grid(row=3,column=1)
   
   
    root.mainloop()


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame,text="QUIT", fg="red",command=quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame,text="Hello",command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        print("Tkinter is easy to use!")

root = Tk()
app = App(root)
root.mainloop()