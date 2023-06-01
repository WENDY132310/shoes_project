from tkinter import *
import tkinter as tk
import compras, Produccion

class login:

    def __init__(self, root):
        root.configure(bg="#000000")

        self.window = root

        # -------- Frame principal logIn---------

        inbox_frame = LabelFrame(self.window, bg="white", width=300, height=250, padx=14, pady=15)
        inbox_frame.grid(row=0, column=1)

        button_frame = LabelFrame(self.window, bg="#000000", width=300, height=80, padx=4, pady=15)
        button_frame.grid(row=0, column=0)
        button_frame.configure(width=300, height=200)

        acceder_button = Button(button_frame, text='Compras', width=20, command=lambda: Ventaslog())
        acceder_button.configure(bg="#EFEDB1", cursor='hand2', font=("Verdana", "10", "bold"))
        acceder_button.grid(row=0, column=1, padx=2, pady=6, sticky=W + E)

        produccion_button = Button(button_frame, text='Producción', width=20, command=lambda: Produccionlog())
        produccion_button.configure(bg="#EFEDB1", cursor='hand2', font=("Verdana", "10", "bold"))
        produccion_button.grid(row=1, column=1, padx=2, pady=6, sticky=W + E)



        def Produccionlog():
            Produccion.produccion(root)
            self.window.withdraw()

        def Ventaslog():
            compras.compras(root)
            self.window.withdraw()
