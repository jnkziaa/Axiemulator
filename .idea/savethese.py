def energy_use():
    n = energy_counter.get()
    update = int(n) - 1
    if update < 0:
        update = 0
    energy_counter.delete(0, END)
    energy_counter.insert(0, update)
def energy_gain():
    n = energy_counter.get()
    update = int(n) + 1
    if update > 10:
        update = 10
    energy_counter.delete(0, END)
    energy_counter.insert(0, update)


    # UI options
paddings = {'padx': 5, 'pady': 5}
entry_font = {'font': ('Helvetica', 35)}




# configure the grid
self.columnconfigure(0, weight=1)
self.columnconfigure(1, weight=3)

username = tk.StringVar()
password = tk.StringVar()

# heading
heading = ttk.Label(self, text='Round 1', style='Heading.TLabel')
heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)


energy_counter = Entry(self, **entry_font, justify = 'center')
energy_counter.insert(0,3)
energy_counter.grid(column=0, row=1, columnspan=2, pady=1, sticky=tk.N)

#enegy used
energy_used = ttk.Label(self, text='Energy Used', style='Heading.TLabel')
energy_used.grid(column=0, row=2, columnspan=2, pady = 5, sticky=tk.N)
used_button = tk.Button(self, text=" + ", command = energy_use)
used_button.grid(column=0, row=3, columnspan = 2,padx = 2 , pady = 2, sticky=tk.N)

#energy gained
energy_gained = ttk.Label(self, text='Energy Gained', style='Heading.TLabel')
energy_gained .grid(column=0, row=4, columnspan = 2, pady = 5, sticky=tk.N)
gained_button = tk.Button(self, text=" + ", command = energy_gain)
gained_button.grid(column=0, row=5, columnspan = 2,padx = 2 , pady = 2, sticky=tk.N)

#energy destroyed
energy_destroyed = ttk.Label(self, text='Energy Destroyed / Stolen', style='Heading.TLabel')
energy_destroyed.grid(column=0, row=6, columnspan = 2, pady=5, sticky=tk.N)
destroyed_button = tk.Button(self, text=" + ", command = energy_use)
destroyed_button.grid(column=0, row=7, columnspan = 2, ipadx = 2 , ipady = 2, sticky=tk.N)





#End Round
end_round = ttk.Button(self, text="End Round")
end_round.grid(column=0, row=8, columnspan=2, pady=5, sticky=tk.N)

# configure style
self.style = ttk.Style(self)
self.style.configure('TLabel', font=('Helvetica', 11))
self.style.configure('TButton', font=('Helvetica', 11))

# heading style
self.style.configure('Heading.TLabel', font=('Helvetica', 12))