import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Base import Add_transaction
from PIL import Image, ImageTk
from itertools import count

import datetime
import pandas as pd
from functools import partial

LARGE_FONT = ("bold", 20)
M_FONT = ("Verdana", 12)
A_FONT = ("Verdana", 16)

add_t = Add_transaction()


class Shyam(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "2D Diffusion Equation Solver(CFD)")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Add_transaction,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Add_transaction)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Add_transaction(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="2D Diffusion Equation Solver(CFD)", font=LARGE_FONT)
        label.pack(pady=20, padx=10)

        self.label = tk.Label(self, text="plate_length (pref:50)", font=M_FONT)
        self.label.place(y=200, x=450)
        self.var1 = tk.Entry(self, bd=1, width=50)
        self.var1.place(x=650, y=200)

        self.label = tk.Label(self, text="Alpha (pref:1 or 2) ", font=M_FONT)
        self.label.place(y=250, x=450)
        self.var2 = tk.Entry(self, bd=1, width=50)
        self.var2.place(x=650, y=250)

        self.label = tk.Label(self, text="delta_x (pref: 1)", font=M_FONT)
        self.label.place(y=300, x=450)
        self.var3 = tk.Entry(self, bd=1, width=50)
        self.var3.place(x=650, y=300)

        self.label = tk.Label(self, text="u_initial (<100)", font=M_FONT)
        self.label.place(y=350, x=450)
        self.var4 = tk.Entry(self, bd=1, width=50)
        self.var4.place(x=650, y=350)

        self.label = tk.Label(self, text="u_top (<100)", font=M_FONT)
        self.label.place(y=400, x=450)
        self.var5 = tk.Entry(self, bd=1, width=50)
        self.var5.place(x=650, y=400)

        self.label = tk.Label(self, text="u_left (<100)", font=M_FONT)
        self.label.place(y=450, x=450)
        self.var6 = tk.Entry(self, bd=1, width=50)
        self.var6.place(x=650, y=450)

        self.label = tk.Label(self, text="u_bottom (<100)", font=M_FONT)
        self.label.place(y=500, x=450)
        self.var7 = tk.Entry(self, bd=1, width=50)
        self.var7.place(x=650, y=500)

        self.label = tk.Label(self, text="u_right (<100)", font=M_FONT)
        self.label.place(y=550, x=450)
        self.var8 = tk.Entry(self, bd=1, width=50)
        self.var8.place(x=650, y=550)

        self.label = tk.Label(self, text="Type:", font=M_FONT)
        self.label.place(y=600, x=450)
        self.v = tk.IntVar()
        self.v.set(1)

        R1 = tk.Radiobutton(self, text="Implicit", variable=self.v, value="1")
        R1.place(x=650, y=600)

        R2 = tk.Radiobutton(self, text="Explicit", variable=self.v, value="2")
        R2.place(x=740, y=600)

        self.button3 = ttk.Button(self, text="Run", width=25, command=lambda: self.add_trans())
        self.button3.place(x=660, y=700)

    def add_trans(self):
        # To add transaction to table
        t = add_t.add_transaction(self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get(),
                                  self.var6.get(), self.var7.get(), self.var8.get(), self.v.get())
        # self.controller.frames[LogIn].load('saved.gif')
        # self.controller.show_frame(LogIn)
        # t="";
        # To check if any wrong with transaction
        # if t=="":
        #     # self.var1.delete(0,100)
        #     # self.var2.delete(0,100)
        #     # self.description.delete(0,100)
        #     # self.v.set(1)
        #     messagebox.showwarning("Completed","Transaction added")
        # else:
        #     messagebox.showwarning("Warning",t)


app = Shyam()
app.mainloop()
