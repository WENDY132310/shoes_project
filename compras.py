import Start, pago, registro_pedidos
import csv
import tkinter as tk
from datetime import date
from tkinter import *
from tkinter import messagebox as MessageBox, ttk


class compras:

    def __init__(self, root):

        frame_compras = Toplevel(root)
        frame_compras.configure(bg="#000000")
        global verifica_usuario
        global verifica_clave
        vfr = BooleanVar()
        verifica_usuario = StringVar()
        verifica_clave = StringVar()

        # -------Message box----------
        def no_found(var):
            var_s = str(var)
            MessageBox.showinfo("No se encuentra el registro ",
                                "Usuario " + var_s + ' ' + "Por favor Ingrese correctamente los datos")


        def write_user():
            MessageBox.showinfo("Registro usuario",
                                "Registre los datos para la creacion de el nuevo usuario")

        # --------Funciones auxiliares

        def _clean_inbox(dato1, dato2):
            dato1.delete(0, 'end')
            dato2.delete(0, 'end')

        def _save(user, password):
            s_name = user
            s_phone = password

            with open('Lista_vendedor.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_name, s_phone))

        def _search(var_inboxUser, var_inboxContra, possitionuser, possitioncontra):
            my_list = []
            s_var_inboxuser = str(var_inboxUser)
            var_possitionuser = int(possitionuser)
            s_var_inboxcon = str(var_inboxContra)
            var_possitioncon = int(possitioncontra)
            with open('Lista_vendedor.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if s_var_inboxuser == row[var_possitionuser] and s_var_inboxcon == row[var_possitioncon]:
                        my_list = [row[0], row[1]]
                        break

                    else:
                        continue
            return my_list

        def _check(answer, var_search):
            list_answer = answer
            var_search = var_search
            if not list_answer:
                no_found(var_search)
            elif var_search == "":
                no_found(var_search)
            else:
                vrf = True
                name = str(list_answer[0])
                password = str(list_answer[1])
                if vfr:
                    venta(root)
                    frame_compras.withdraw()

            # -------------funcion boton acceder userlog in

        def search():
            answer = []
            password = inbox_contra.get()
            name = inbox_user.get()
            possition1 = 0
            possition = 1
            if _search(name, password, possition1, possition):

                if name == "" or password == "":
                    vrf = False

                vrf = False
                answer = _search(name, password, possition1, possition)
                _check(answer, name)
            else:
                no_found(name)
                inbox_user.focus()
            _clean_inbox(inbox_user, inbox_contra)

        def volver():
            Start.login(Toplevel(root))
            frame_compras.withdraw()

            # -------- Frame principal logIn---------

        inbox_frame = LabelFrame(frame_compras, bg="#EFEDB1", width=300, height=80, padx=4, pady=5)
        inbox_frame.grid(row=0, column=0)

        button_frame = LabelFrame(frame_compras, bg="#000000")
        button_frame.grid(row=3, column=0)

        Label(inbox_frame, text='Bienvenido a el area de compras ', bg="#EFEDB1",
              font=("Verdana MS", "30", "bold")).grid(row=1,
                                                         column=0)

        Label(inbox_frame, text='Usuario', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=2, column=0)

        inbox_user = Entry(inbox_frame, textvariable=verifica_usuario, font=("Verdana MS", "11", "normal"),
                           width=50)
        inbox_user.grid(row=3, column=0, padx=30, pady=5)
        inbox_user.focus()

        Label(inbox_frame, text='Contraseña', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=5,
                                                                                                       column=0)
        inbox_contra = Entry(inbox_frame, textvariable=verifica_clave, font=("Verdana MS", "11", "normal"),
                             width=50,
                             show='*')
        inbox_contra.grid(row=6, column=0, padx=30, pady=5)

        acceder_button = Button(button_frame, text='Acceder', width=20, command=lambda: search())
        acceder_button.configure(bg="#EFEDB1", cursor='hand2', font=("Verdana MS", "10", "normal"))
        acceder_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        back_button = Button(button_frame, text='Volver', width=20, command=lambda: volver())
        back_button.configure(bg="#EFEDB1", cursor='hand2', font=("Verdana MS", "10", "normal"))
        back_button.grid(row=0, column=0, padx=2, pady=3, sticky=W + E)


class venta:
    global frame_registro

    def __init__(self, root):
        dia = IntVar()
        mes = IntVar()
        year = IntVar()
        dias = IntVar()
        mess = IntVar()
        years = IntVar()
        valor = IntVar()
        cantidad = IntVar()

        frame_venta = Toplevel(root)

        frame_venta.configure(bg="#000000")
        frame_venta.title("Registrar pedido")
        frame_venta.geometry("+350+80")
        frame_venta.resizable(0, 0)

        def write_tipo():
            MessageBox.showinfo("No se encuentra", "por favor escriba un contacto")

        def write_user():

            MessageBox.showinfo("Registro Venta",
                                "Registre los datos para el correcto registro de su habitacion")
            frame_venta.attributes('-topmost', True)

        menubar = Menu(frame_venta)
        frame_venta.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0, bg="#FFBB20")
        filemenu.add_command(label="mostrar registro de pedidos", command=lambda: cont(),
                             font=("Helveltica", "9", "normal"))
        filemenu.add_command(label="User manual", font=("Helveltica", "9", "normal"))
        filemenu.add_separator()
        filemenu.add_command(label="Close", command=frame_venta.quit, font=("Helveltica", "9", "normal"))

        menubar.add_cascade(label="Menu", menu=filemenu)

        inbox_frame = LabelFrame(frame_venta, bg="#EFEDB1", width=300, height=80, padx=4, pady=5)
        inbox_frame.grid(row=1, column=0)
        inbox_ = LabelFrame(frame_venta, bg="#EFEDB1", width=300, height=80, padx=4, pady=5)
        inbox_.grid(row=2, column=0)
        button_frame = LabelFrame(frame_venta, bg="#EFEDB1")
        button_frame.grid(row=3, column=0)

        Label(inbox_frame, text='Realiza tu pedido', bg="#EFEDB1", font=("Verdana MS", "30", "bold")).grid(row=0,
                                                                                                              column=0)

        Label(inbox_, text='Docenas a encargar', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=1,
                                                                                                          column=0,
                                                                                                          padx=30)

        inbox_cant = Entry(inbox_, textvariable=cantidad, font=("Verdana MS", "11", "normal"), width=10, show="")
        inbox_cant.grid(row=1, column=1, padx=30, pady=5)
        inbox_cant.focus()

        Label(inbox_, text='Tipo', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=2,
                                                                                            column=0, padx=30)

        combobox = ttk.Combobox(inbox_, state='readonly', width=17, justify='center',
                                font=("Verdana MS", "10", "normal"))
        combobox["values"] = ['', 'Oxford lisos', 'Botas', 'Broge', 'Mocasines']
        combobox.grid(row=2, column=1, padx=15)
        combobox.current(0)

        Label(inbox_, text='Fecha llegada ', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=3, column=0,
                                                                                                      padx=30)

        Label(inbox_, text='Dia ', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=3, column=1,
                                                                                            padx=30, pady=5)

        inbox_diaent = Entry(inbox_, textvariable=dia, font=("Verdana MS", "11", "normal"), width=10, show="")
        inbox_diaent.grid(row=4, column=1, padx=30, pady=5)
        inbox_diaent.focus()
        Label(inbox_, text='Mes ', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=3, column=2,
                                                                                            padx=30, pady=5)

        inbox_mesent = Entry(inbox_, textvariable=mes, font=("Verdana MS", "11", "normal"), width=10, )
        inbox_mesent.grid(row=4, column=2, padx=30, pady=5)
        inbox_mesent.focus()
        Label(inbox_, text='Año ', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=3, column=3,
                                                                                            padx=30)
        inbox_yearent = Entry(inbox_, textvariable=year, font=("Verdana MS", "11", "normal"), width=10, show="")
        inbox_yearent.grid(row=4, column=3, padx=30, pady=5)
        inbox_yearent.focus()

        Label(inbox_, text='Fecha salida ', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=5, column=0,
                                                                                                     padx=30)

        Label(inbox_, text='Dia ', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=5, column=1,
                                                                                            padx=30, pady=5)

        inbox_diaSal = Entry(inbox_, textvariable=dias, font=("Verdana MS", "11", "normal"), width=10, show="")
        inbox_diaSal.grid(row=7, column=1, padx=30, pady=5)
        inbox_diaSal.focus()
        Label(inbox_, text='Mes ', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=5, column=2,
                                                                                            padx=30, pady=5)

        inbox_mesSal = Entry(inbox_, textvariable=mess, font=("Verdana MS", "11", "normal"), width=10, show="")
        inbox_mesSal.grid(row=7, column=2, padx=30, pady=5)
        inbox_mesSal.focus()
        Label(inbox_, text='Año ', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=5, column=3,
                                                                                            padx=30)
        inbox_yearSal = Entry(inbox_, textvariable=years, font=("Verdana MS", "11", "normal"), width=10, show="")
        inbox_yearSal.grid(row=7, column=3, padx=30, pady=5)
        inbox_yearSal.focus()

        inbox_valor = Entry(inbox_, textvariable=valor, font=("Verdana MS", "11", "normal"), width=10)
        inbox_valor.grid(row=2, column=2, padx=30, pady=5)
        inbox_valor.focus()
        Label(inbox_, text='Total de dias:  ', bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=8,
                                                                                                        column=0,
                                                                                                        padx=30)
        inbox_diases = Entry(inbox_, font=("Verdana MS", "11", "normal"), width=10)
        inbox_diases.grid(row=8, column=1, padx=30, pady=5)
        inbox_diases.focus()

        hab_button = Button(inbox_, text='Confirmar tipo de zapato', width=30, command=lambda: valorservicio_())
        hab_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        hab_button.grid(row=1, column=3, padx=2, pady=3, sticky=W + E)

        pagar_button = Button(button_frame, command=lambda: sel(), text='Pagar', width=30)
        pagar_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        pagar_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        pagar_fecha = Button(inbox_, command=lambda: dias_hab(), text='Confirmar fechas', width=30)
        pagar_fecha.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        pagar_fecha.grid(row=8, column=3, padx=2, pady=3, sticky=W + E)

        def valorservicio_():

            _clean_inbox(inbox_valor)
            valor = StringVar()

            if combobox.get() == "Oxford lisos":
                valor = 90000 * int(inbox_cant.get())
                inbox_valor.insert(tk.END, valor)

            elif combobox.get() == "Botas":
                valor = 120000 * int(inbox_cant.get())
                inbox_valor.insert(tk.END, valor)

            elif combobox.get() == "Broge":
                valor = 80000 * int(inbox_cant.get())
                inbox_valor.insert(tk.END, valor)
            elif combobox.get() == "Mocasines":

                valor = 250000 * int(inbox_cant.get())
                inbox_valor.insert(tk.END, valor)

        def _clean_inbox(dato1):
            dato1.delete(0, 'end')

        def cont():
            registro_pedidos.registros_compras(root)
            frame_venta.withdraw()

        def _save(tipo, valor, fecha):
            s_tipo = tipo
            s_valor = valor
            s_fecha = fecha
            with open('Lista_registros_compras.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_tipo, s_valor, s_fecha))
                print("se guardo la venta :3")
        def dias_hab():
            entrada = fechaen()
            salida = fechasal()
            diasestadia1 = diferencia(entrada, salida)
            inbox_diases.insert(tk.END, str(diasestadia1))

        def sel():
            seleccion = str(combobox.get())

            if seleccion == "":
                write_user()
            else:
                add()
                pago.pagar(root, inbox_valor.get())
                frame_venta.destroy()
        def add():
            tipo = str(combobox.get())
            valor = inbox_valor.get()
            fecha = fechasal()
            contact_check = [tipo, valor, fecha]
            if contact_check == ['', '', '']:
                write_tipo()
            else:
                if tipo == '':
                    tipo = '<Default>'
                if valor == '':
                    valor = '<Default>'
                if fecha == '':
                    email = '<Default>'
                _save(tipo, valor, fecha)

        def fechaen():

            new_date = date(year.get(), mes.get(), dia.get())
            entrada = new_date.strftime('%d/%m/%Y')
            print(entrada)

            return new_date

        def fechasal():

            new_date = date(years.get(), mess.get(), dias.get())
            salida = new_date.strftime('%d/%m/%Y')
            print(salida)
            return new_date

        def diferencia(ent, sal):

            _clean_inbox(inbox_diases)
            diferenciaf = (sal - ent).days
            diasestadia1 = diferenciaf

            return (diasestadia1)

