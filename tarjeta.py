from tkinter import *

class tarjeta:
    def __init__(self, root):
        global frame_tarjeta
        frame_tarjeta = Toplevel(root)
        numero_tarjeta= StringVar()
        cuotas= StringVar()

        frame_tarjeta.configure(bg="#000000")
        frame_tarjeta.title("Pago con tarjeta de credito")
        frame_tarjeta.geometry("+350+80")
        frame_tarjeta.resizable(0, 0)

        inbox_frame = LabelFrame(frame_tarjeta, bg="#EFEDB1", width=300, height=80, padx=4, pady=5)
        inbox_frame.grid(row=1, column=0)

        inbox_ = LabelFrame(frame_tarjeta, bg="#EFEDB1", width=300, height=80, padx=4, pady=5)
        inbox_.grid(row=2, column=0)

        button_frame = LabelFrame(frame_tarjeta, bg="#EFEDB1")
        button_frame.grid(row=3, column=0)

        Label(inbox_frame, text='Ingresa los datos de tu tarjeta', bg="#EFEDB1", font=("Verdana MS", "30", "bold")).grid(
            row=0,
            column=0)

        Label(inbox_, text='Numero de la tarjeta', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(
            row=1,
            column=0)
        Label(inbox_, text='Numero de cuotas', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(
            row=1,
            column=1)

        inbox_user = Entry(inbox_, textvariable=numero_tarjeta, font=("Verdana MS", "11", "normal"), width=10,show='*')
        inbox_user.grid(row=4, column=0, padx=30, pady=5)
        inbox_user.focus()

        inbox_cuo = Entry(inbox_, textvariable=cuotas, font=("Verdana MS", "11", "normal"), width=10)
        inbox_cuo.grid(row=4, column=1, padx=30, pady=5)
        inbox_cuo.focus()

        confir_button=Button(button_frame,text="Confirmar",command=lambda: imprimir(),width=30)
        confir_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        confir_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        def  imprimir():
            print(cuotas.get())
            print(numero_tarjeta.get())
            Label(frame_tarjeta, text="¡Registro completado con éxito!", fg="green", font=("calibri", 15)).grid(row=5,column=0)
            button_frame.destroy()
            inbox_.destroy()
            print("pdf")