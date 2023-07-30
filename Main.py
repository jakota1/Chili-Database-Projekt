#import tkinter as tkk       # Documentation: https://www.tutorialspoint.com/python/python_gui_programming.htm#

import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chili Tracker")
        self.geometry("400x300")
        
        # Opret GUI-komponenter her
        self.count = 0
        self.chili_info = "Ingen information"

        self.create_widgets()

    def create_widgets(self):
        # Tilføj GUI-komponenter her
        # F.eks. knapper, tekstfelter osv.

        # Eksempel på en knap
        self.btn_add_chili = tk.Button(self, text="Tilføj Chili", command=self.add_chili)
        self.btn_add_chili.pack()

        # Label til at vise tælleren
        self.lbl_count = tk.Label(self, text="Antal gange trykket: {}".format(self.count))
        self.lbl_count.pack()

        # Tekstfelt til at indtaste chilioplysninger
        self.entry_chili_info = tk.Entry(self)
        self.entry_chili_info.pack()

        # Knappen til at opdatere chili_info
        self.btn_update_info = tk.Button(self, text="Opdater Chili Info", command=self.update_info)
        self.btn_update_info.pack()

        # Label til at vise chili info
        self.lbl_chili_info = tk.Label(self, text="")
        self.lbl_chili_info.pack()

    def add_chili(self):
        # Opdater tælleren
        self.count += 1
        self.lbl_count.config(text="Antal gange trykket: {}".format(self.count))
        
        # Hent indtastet tekst fra tekstfeltet
        chili_info = self.entry_chili_info.get()
        self.lbl_chili_info.config(text="{}".format(self.chili_info))

        # Logik til at tilføje chili
        # F.eks. vis en dialogboks, hvor brugeren kan indtaste chilioplysninger
        messagebox.showinfo("Besked", "Chili tilføjet!")
    
    def update_info(self):
        # Opdater chili_info med den indtastede tekst
        self.chili_info = self.entry_chili_info.get()
        messagebox.showinfo("Besked", "Chili info opdateret!")

if __name__ == "__main__":
    app = Application()
    app.mainloop()