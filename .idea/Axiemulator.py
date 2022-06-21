from tkinter import *
from tkinter import font
from PIL import ImageTk,Image

root = Tk()
root.title("Axiemulator")
root.geometry("1080x720")

class one:
    def __init__(self, root):
        q = 1
        def energy_use():
            n = self.energy_counters.get()
            update = int(n) - 1
            print(update)
            if update < 0:
                update = 0
            self.energy_counters.delete(0, END)
            self.energy_counters.insert(0, update)
            self.energy_counter.delete(0, END)
            self.energy_counter.insert(0, f'Energy: {self.energy_counters.get()}')
        def energy_gain():
            n = self.energy_counters.get()
            update = int(n) + 1
            if update > 10:
                update = 10
            self.energy_counters.delete(0, END)
            self.energy_counters.insert(0, update)
            self.energy_counter.delete(0, END)
            self.energy_counter.insert(0, f'Energy: {self.energy_counters.get()}')
        def end_turn():
            m = self.rounds.get()
            m = int(m) + 1

            n = self.energy_counters.get()
            update = int(n) + 2
            if update > 10:
                update = 10
            self.energy_counters.delete(0, END)
            self.energy_counters.insert(0, update)
            self.energy_counter.delete(0, END)
            self.energy_counter.insert(0, f'Energy: {self.energy_counters.get()}')

            self.rounds.delete(0, END)
            self.rounds.insert(0, m)
            self.frame_label.config(text = f'Round {self.rounds.get()}')



        self.root = root
        self.img = ImageTk.PhotoImage(Image.open("1608431136510.jpg"))  # label image (frame background)
        self.label = Label(self.root, image = self.img, width=1080, height=500)  # frame parent

        self.frame = Frame(self.label, bg="", width=800, height=400)  # main widget, clear background
        self.frame.place(x=0, y=0, width=800, height=400)   # required for correct z-index
        root.geometry("1080x500")
        self.header = Label(self.root, bg="#FF6103", fg="white", font=("Times New Roman", 30, "bold"))
        self.header.pack(fill=X)
        self.heading = Label(self.root, text="Axie Infinity Energy Calculator", bg="#FF6103", fg="white", font=("Times New Roman", 30, "bold"))
        self.heading.place(x=10, y=0)
        self.label.pack()

        ###########Frame
        self.wframe = LabelFrame(self.root,padx = 5, pady = 5)
        self.wframe.place(x = 0, y = 50, width = 350, height = 430)

        self.rounds = Entry()
        self.rounds.insert(0,1)
        self.frame_label = Label(self.wframe, text = f'Round {self.rounds.get()}',bg="#ED9121", fg="white", font = ("Time new Roman", 20))
        self.frame_label.grid(row = 0, column = 0, sticky = "w")


        self.energy_counters = Entry()
        self.energy_counters.insert(0,3)
        self.energy_counter = Entry(self.wframe,bg="#008B8B", fg="black", font = ("Time new Roman", 25), justify = 'center')
        self.energy_counter.insert(0, f"Energy: {self.energy_counters.get()}")
        self.energy_counter.grid(row = 2, column = 0, columnspan = 1, ipadx = 5, ipady = 5, sticky = "w")


        self.used = Button(self.wframe, text="Energy Used",height = 3, width = 30, bg="brown", fg="white", font=("Times New Roman", 15), command = energy_use)
        self.used.grid(row = 5, column = 0, sticky = SW)

        self.gained = Button(self.wframe, text="Energy Gained", height = 3, width = 30, bg="brown", fg="white", font=("Times New Roman", 15), command=energy_gain)
        self.gained.grid(row = 6, column = 0, sticky = SW)

        self.destroyed = Button(self.wframe, text=" Energy Destroyed", height = 3, width = 30, bg="brown", fg="white", font=("Times New Roman", 15), command=energy_use)
        self.destroyed.grid(row = 7, column = 0, sticky = SW)


        self.q = Button(self.wframe, text="End Turn", bg="brown",height = 3, width = 30, fg="white", font=("Times New Roman", 15), command = end_turn)
        self.q.grid(row = 8, column = 0, sticky = SW)



obj = one(root)
root.mainloop()