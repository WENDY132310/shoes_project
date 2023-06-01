from tkinter import *

import tkinter as tk
from tkinter import messagebox as MessageBox
import tarjeta


class pagar:

    def __init__(self, root, val):
        global frame_pago
        frame_pago = Toplevel(root)

        frame_pago.configure(bg="#000000")
        frame_pago.title("Pago")
        frame_pago.geometry("+350+80")
        frame_pago.resizable(0, 0)

        def metodopago(met):
            metodos = met
            print("salida es: " + metodos)
            return metodos

        def write_user():
            MessageBox.showinfo("Registro usuario",
                                "Registre los datos para la creacion de el nuevo usuario")

        total = IntVar()

        inbox_frame = LabelFrame(frame_pago, bg="#EFEDB1", width=300, height=80, padx=4, pady=5)
        inbox_frame.grid(row=1, column=0)
        inbox_frame_val = LabelFrame(frame_pago, bg="#EFEDB1", width=300, height=80, padx=4, pady=5)
        inbox_frame_val.grid(row=2, column=0)

        inbox_frame_ab = LabelFrame(frame_pago, bg="#EFEDB1", width=300, height=80, padx=4, pady=5)
        inbox_frame_ab.grid(row=4, column=0)

        button_frame = LabelFrame(frame_pago, bg="#EFEDB1")
        button_frame.grid(row=3, column=0)
        Label(inbox_frame, text='Asegura tu pedido', bg="#EFEDB1", font=("Verdana MS", "30", "bold")).grid(
            row=0,
            column=0)
        Label(inbox_frame_val, text='Valor a cancelar: ', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(
            row=1,
            column=0)

        inbox_servicio = Entry(inbox_frame_val, textvariable=total, font=("Verdana MS", "11", "normal"), width=15)
        inbox_servicio.grid(row=1, column=2, padx=30, pady=5)
        inbox_servicio.focus()

        Label(inbox_frame, text='Selecciona metodo de pago', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(
            row=2,
            column=0)

        pagarefec_button = Button(button_frame, command=lambda: continuar(), text='Efectivo', width=30)
        pagarefec_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        pagarefec_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        pagartar_button = Button(button_frame, command=lambda: continuartar(), text='Tarjeta de credito', width=30)
        pagartar_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        pagartar_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        abono = StringVar()

        def continuar():
            metodo = "Efectivo"
            metodopago(metodo)
            Label(inbox_frame_ab, text='Cantidad abono', bg="#EFEDB1",
                  font=("Verdana MS", "20", "bold")).grid(row=12, column=0)
            inbox_abonar = Entry(inbox_frame_ab, textvariable=abono, font=("Verdana MS", "11", "normal"),
                                 width=50)
            inbox_abonar.grid(row=13, column=0, padx=30, pady=5)

            inbox_abonar.focus()

            confir_button = Button(inbox_frame_ab, text="Confirmar", command=lambda: registro_user(), width=30)
            confir_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
            confir_button.grid(row=15, column=0, padx=2, pady=3, sticky=W + E)

            def _save(abonoreliazado):
                abn = abonoreliazado

            def registro_user():

                abono = inbox_abonar.get()

                print(abono)
                contact_check = [abono]
                if contact_check == ['']:
                    write_user()
                else:
                    _save(abono)

                contact_check = []
                _clean_inbox(inbox_abonar)

                Label(frame_pago, text="¡Registro completado con éxito!", fg="green", font=("calibri", 15)).grid(row=5,
                                                                                                                 column=0)
                imprimir()

        def valorpago():
            _clean_inbox(inbox_servicio)


            inbox_servicio.insert(tk.END, str(val))
            print(val)
            return val

        def _clean_inbox(dato1):
            dato1.delete(0, 'end')

        valorpago()

        def continuartar():
            metodo = "Tarjeta de credito"
            metodopago(metodo)
            abono = valorpago()
            tarjeta.tarjeta(root)
            inbox_frame_ab.grid_forget()
            frame_pago.destroy()

        def imprimir():
            print("pdf2")
            inbox_frame_ab.destroy()
