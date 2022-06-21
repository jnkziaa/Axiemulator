from tkinter import *
from tkinter import font
from PIL import ImageTk,Image

root = Tk()
root.title("Sign In")
root.geometry("600x420")

class one:

    def __init__(self, root):
        self.root = root
        self.img = ImageTk.PhotoImage(Image.open("img.png"))  # label image (frame background)
        self.label = Label(self.root, image = self.img, width=800, height=400)  # frame parent

        self.frame = Frame(self.label, bg="", width=800, height=400)  # main widget, clear background
        self.frame.place(x=0, y=0, width=800, height=400)   # required for correct z-index
        root.geometry("800x400")
        self.header = Label(self.root, bg="brown", fg="white", font=("Times New Roman", 30, "bold"))
        self.header.pack(fill=X)
        self.heading = Label(self.root, text="First One", bg="brown", fg="white", font=("Times New Roman", 30, "bold"))
        self.heading.place(x=10, y=0)
        self.q = Button(self.frame, text="Quit", bg="brown", fg="white", font=("Times New Roman", 10), command=self.root.destroy)
        self.q.place(x=650, y=320, width=120, height=20)
        self.label.pack()  # pack bottom widget

obj = one(root)
root.mainloop()