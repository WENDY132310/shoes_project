from PIL import ImageTk
import tkinter as tk
import Start
import csv
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
import orden
from datetime import date, datetime


class produccion:

    def __init__(self, root):

        frame_produccion = Toplevel(root)
        frame_produccion.configure(bg="#000000")
        vfr = BooleanVar()
        global verifica_usuario
        global verifica_clave
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
            s_nombre_maquina = user
            s_referencia = password

            with open('Lista_prod.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_nombre_maquina, s_referencia))

        def _search(var_inboxUser, var_inboxContra, possitionuser, possitioncontra):
            my_list = []
            s_var_inboxuser = str(var_inboxUser)
            var_possitionuser = int(possitionuser)
            s_var_inboxcon = str(var_inboxContra)
            var_possitioncon = int(possitioncontra)
            with open('Lista_prod.csv', 'r') as f:
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
                nombre_maquina = str(list_answer[0])
                password = str(list_answer[1])
                if vfr:
                    produc(root)
                    frame_produccion.withdraw()

            # -------------funcion boton acceder userlog in

        def search():
            answer = []
            password = inbox_contra.get()
            nombre_maquina = inbox_user.get()
            possition1 = 0
            possition = 1
            if _search(nombre_maquina, password, possition1, possition):

                if nombre_maquina == "" or password == "":
                    vrf = False

                vrf = False
                answer = _search(nombre_maquina, password, possition1, possition)
                _check(answer, nombre_maquina)
            else:
                no_found(nombre_maquina)
                inbox_user.focus()
            _clean_inbox(inbox_user, inbox_contra)

        def volver():
            Start.login(Toplevel(root))
            frame_produccion.withdraw()

            # -------- Frame principal logIn---------

        inbox_frame = LabelFrame(frame_produccion, bg="#EFEDB1", width=300, height=80, padx=4, pady=5)
        inbox_frame.grid(row=0, column=0)

        button_frame = LabelFrame(frame_produccion, bg="#000000")
        button_frame.grid(row=3, column=0)

        Label(inbox_frame, text='Bienvenido al area de produccion ', bg="#EFEDB1",
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


class produc:
    def __init__(self, root):
        Frame_pro = Toplevel(root)
        # -------------------------- GLOBAL FUNCTIONS ------------------------------------------
        Frame_pro.configure(bg="#EFEDB1")

        # ----------- MESAGE BOX ---------------------------------------
        def no_found(var):
            var_s = str(var)
            MessageBox.showinfo("No se encuentra el registro", var_s + ' ' + "no se encuentra el registro")

        def write_nombre_maquina():
            MessageBox.showinfo("No se encuentra registro", "por favor ingrese los datos correctos")

        def write_machine():
            MessageBox.showinfo("Registrar maquina",
                                "Para registrar la informacion de la maquina seleccione la opcion  \"adiccionar maquina\" ")

        def des_machine(var):
            des_mach = str(var)
            MessageBox.showinfo("Descripción de maquina", des_mach, )

        def delete_mesageBox(nombre_maquina):
            var_nombre_maquina = str(nombre_maquina)
            if var_nombre_maquina == '':
                write_nombre_maquina()
            else:
                search = MessageBox.askquestion("Alerta!!", "desea borrar este registro?\n" + var_nombre_maquina)
                if search == "yes":
                    return True
                else:
                    return False

        def modify_mesageBox(contact):
            var_nombre_maquina = str(contact[0])
            var_referencia = str(contact[1])

            search = MessageBox.askquestion("Alerta de modificacion",
                                            "Desea guardar los cambios realizados en este registro?\n" + " Nombre de maquina: " + var_nombre_maquina + "\n referencia: " + var_referencia)
            if search == "yes":
                return True
            else:
                return False

        # ------------------ MENU DECLARATION -----------------

        menubar = Menu(Frame_pro)
        Frame_pro.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0, bg="#EFEDB1")
        filemenu.add_command(label="Mostrar rendimiento ", command=lambda: nav(),
                             font=("Verdana", "10", "normal"))
        filemenu.add_separator()
        filemenu.add_command(label="Close", command=Frame_pro.quit, font=("Verdana", "10", "normal"))
        menubar.add_cascade(label="Menu", menu=filemenu)

        def nav():
            rendimiento(root)
            Frame_pro.withdraw()

        # ---------------- FRAMES DECLARATION -----------------
        inbox_frame = LabelFrame(Frame_pro, bg="#EFEDB1")
        inbox_frame.grid(row=0, column=0)

        button_frame = Frame(Frame_pro, bg="#000000")
        button_frame.grid(row=2, column=0, padx=150)

        three_frame = LabelFrame(Frame_pro, bg="#000000")
        three_frame.grid(row=4, column=0)

        three_button_frame = LabelFrame(Frame_pro, bg="#000000")
        three_button_frame.grid(row=5, column=0)

        # --------------- INBOX WIDGETS ZONE ------------------
        Label(inbox_frame, text='Nombre', bg="#EFEDB1", font=("Verdana", "11", "normal")).grid(row=0,
                                                                                               column=0)
        inbox_nombre_maquina = Entry(inbox_frame, font=("Verdana", "11", "normal"), width=30)
        inbox_nombre_maquina.grid(row=1, column=0)
        inbox_nombre_maquina.focus()

        Label(inbox_frame, text='Referencia', bg="#EFEDB1", font=("Verdana", "11", "normal")).grid(row=0,
                                                                                                   column=1)
        inbox_reference = Entry(inbox_frame, font=("Verdana", "11", "normal"), width=30)
        inbox_reference.grid(row=1, column=1)

        Label(inbox_frame, text='Voltaje', bg="#EFEDB1", font=("Verdana", "11", "normal")).grid(row=0,
                                                                                                column=2)
        inbox_Vol = Entry(inbox_frame, font=("Verdana", "11", "normal"), width=30)
        inbox_Vol.grid(row=1, column=2)

        Label(inbox_frame, text='Potencia general', bg="#EFEDB1", font=("Verdana", "11", "normal")).grid(row=0,
                                                                                                         column=3)
        inbox_potencia = Entry(inbox_frame, font=("Verdana", "11", "normal"), width=30)
        inbox_potencia.grid(row=1, column=3)

        Label(inbox_frame, text='Tamaño mecanico', bg="#EFEDB1", font=("Verdana", "11", "normal")).grid(row=2,
                                                                                                        column=0)
        inbox_size = Entry(inbox_frame, font=("Verdana", "11", "normal"), width=30)
        inbox_size.grid(row=3, column=0)

        Label(inbox_frame, text='Presion de suministro de aire', bg="#EFEDB1", font=("Verdana", "11", "normal")).grid(
            row=2,
            column=1)
        inbox_Pres = Entry(inbox_frame, font=("Verdana", "11", "normal"), width=30)
        inbox_Pres.grid(row=3, column=1)

        Label(inbox_frame, text='Capacidad de produccion', bg="#EFEDB1", font=("Verdana", "11", "normal")).grid(row=2,
                                                                                                                column=2)
        inbox_cap = Entry(inbox_frame, font=("Verdana", "11", "normal"), width=30)
        inbox_cap.grid(row=3, column=2)

        Label(inbox_frame, text='Descripcion', bg="#EFEDB1", font=("Verdana", "11", "normal")).grid(row=2,
                                                                                                    column=3)
        inbox_des = Entry(inbox_frame, font=("Verdana", "11", "normal"), width=30)
        inbox_des.grid(row=3, column=3)

        # --------------- BUTTON WIDGETS ZONE -----------------
        Add_machine_button = Button(button_frame, command=lambda: add(), text='Agregar maquina', width=20)
        Add_machine_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana", "10", "bold"))
        Add_machine_button.grid(row=0, column=0, padx=35, pady=3, sticky=W + E)

        search_button = Button(button_frame, command=lambda: search(), text='Buscar maquina', width=20)
        search_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana", "10", "bold"))
        search_button.grid(row=0, column=1, padx=35, pady=3, sticky=W + E)

        delete_button = Button(button_frame, command=lambda: delete(), text='Borrar maquina', width=20)
        delete_button.configure(bg="#F26262", cursor='hand2', font=("Verdana", "10", "bold"))
        delete_button.grid(row=1, column=0, padx=35, pady=3, sticky=W + E)

        modify_button = Button(button_frame, command=lambda: modify(), text='Modificar maquina')
        modify_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana", "10", "bold"))
        modify_button.grid(row=1, column=1, padx=35, pady=3, sticky=W + E)

        show_contacts_button = Button(button_frame, command=lambda: show_machine(), text='Mostrar todas las maquinas',
                                      width=25)
        show_contacts_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana", "10", "bold"))
        show_contacts_button.grid(row=0, column=2, padx=35, pady=3, sticky=W + E)

        save_changes_button = Button(button_frame, command=lambda: clean(), text='Limpiar', width=20)
        save_changes_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana", "10", "bold"))
        save_changes_button.grid(row=1, column=2, padx=35, pady=3, sticky=W + E)

        # -------------- COMBOBOX WIDGETS ZONE ----------------
        Label(button_frame, text='Realizar busqueda por:', bg="#EFEDB1",
              font=("Verdana", "10", "bold")).grid(
            row=0, column=3, columnspan=3)

        combo = ttk.Combobox(button_frame, state='readonly', width=17, justify='center',
                             font=("Verdana", "10", "bold"))
        combo["values"] = ['Nombre', 'Referencia']
        combo.grid(row=1, column=3, padx=35)
        combo.current(0)

        # --------------- TREE DIRECTORY ZONE -----------------
        # Table for database
        Frame_pro.tree = ttk.Treeview(three_frame, height=20,
                                      columns=("one", "two", "three", "four", "five", "six"))
        Frame_pro.tree.grid(padx=2, pady=5, row=0, column=0)

        Frame_pro.tree.column("#0", width=135, anchor=CENTER)
        Frame_pro.tree.column("one", width=85, anchor=CENTER)
        Frame_pro.tree.column("two", width=85, anchor=CENTER)
        Frame_pro.tree.column("three", width=100, anchor=CENTER)
        Frame_pro.tree.column("four", width=120, anchor=CENTER)
        Frame_pro.tree.column("five", width=150, anchor=CENTER)
        Frame_pro.tree.column("six", width=150, anchor=CENTER)

        Frame_pro.tree.heading("#0", text='Nombre', anchor=CENTER)
        Frame_pro.tree.heading("one", text='Referencia', anchor=CENTER)
        Frame_pro.tree.heading("two", text='voltaje', anchor=CENTER)
        Frame_pro.tree.heading("three", text='Potencia general', anchor=CENTER)
        Frame_pro.tree.heading("four", text='Tamaño mecanico', anchor=CENTER)
        Frame_pro.tree.heading("five", text='Presion de suministro', anchor=CENTER)
        Frame_pro.tree.heading("six", text='Capacidad de produccion', anchor=CENTER)

        # Scroll
        scrollVert = Scrollbar(three_frame, command=Frame_pro.tree.yview)
        Frame_pro.tree.configure(yscrollcommand=scrollVert.set)
        scrollVert.grid(row=0, column=1, sticky="nsew")

        scroll_x = Scrollbar(three_frame, command=Frame_pro.tree.xview, orient=HORIZONTAL)
        Frame_pro.tree.configure(xscrollcommand=scroll_x.set)
        scroll_x.grid(row=2, column=0, columnspan=1, sticky="nsew")

        # -------------------------- COMMAND FUNCTIONS DECLARATION -----------------------------

        # --------------- AUXILIAR FUNCTIONS ------------------
        def _clean_inbox():
            # Delete from first position (0) to the last position ('end')
            inbox_nombre_maquina.delete(0, 'end')
            inbox_reference.delete(0, 'end')
            inbox_Vol.delete(0, 'end')
            inbox_des.delete(0, 'end')
            inbox_size.delete(0, 'end')
            inbox_Pres.delete(0, 'end')
            inbox_cap.delete(0, 'end')
            inbox_potencia.delete(0, 'end')

        def _clean_treeview():
            tree_list = Frame_pro.tree.get_children()
            for item in tree_list:
                Frame_pro.tree.delete(item)

        def _view_csv():
            contacts = orden.alphabetic_order()
            for i, row in enumerate(contacts):
                nombre_maquina = str(row[0])
                reference = str(row[1])
                voltaje = str(row[2])
                potence = str(row[3])
                capacidad = str(row[4])
                presion = str(row[5])
                descripcion = str(row[6])
                size = str(row[7])
                Frame_pro.tree.insert("", 0, text=nombre_maquina,
                                      values=(reference, voltaje, potence, size, presion, capacidad, descripcion))

        def _save(nombre_maquina, reference, voltaje, potence, size, presion, capacidad, descripcion):
            s_nombre_maquina = nombre_maquina
            s_ref = reference
            s_vol = voltaje
            s_pot = potence
            s_cap = capacidad
            s_pres = presion
            s_des = descripcion
            s_size = size
            with open('machine_list.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_nombre_maquina, s_ref, s_vol, s_pot, s_size, s_pres, s_cap, s_des))

        def _search(var_inbox, possition):
            my_list = []
            s_var_inbox = str(var_inbox)
            var_possition = int(possition)
            with open('machine_list.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if s_var_inbox == row[var_possition]:
                        my_list = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
                        break
                    else:
                        continue
                        write_nombre_maquina()

            return my_list

        def _check(answer, var_search):
            list_answer = answer

            if not list_answer:
                write_nombre_maquina()

            else:
                nombre_maquina = str(list_answer[0])
                reference = str(list_answer[1])
                voltaje = str(list_answer[2])
                potence = str(list_answer[3])
                size = str(list_answer[4])
                presion = str(list_answer[5])
                capacidad = str(list_answer[6])
                descripcion = str(list_answer[7])

                Frame_pro.tree.insert("", 0, text="------------------------------",
                                      values=("------------------------------", "------------------------------",
                                              "------------------------------", "------------------------------",
                                              "------------------------------", "------------------------------",
                                              "------------------------------"))
                Frame_pro.tree.insert("", 0, text=nombre_maquina,
                                      values=(reference, voltaje, potence, size, presion, capacidad))

                Frame_pro.tree.insert("", 0, text="------------------------------",
                                      values=("------------------------------", "------------------------------",
                                              "------------------------------", "------------------------------",
                                              "------------------------------", "------------------------------",
                                              "------------------------------"))
                des_machine(descripcion)
                _clean_inbox()

        def _check_1(answer, var_search):
            val_modify = answer
            var = var_search
            if val_modify == []:
                no_found(var)
            else:
                TopLevelModify(Frame_pro, val_modify)

        # ----------------- BUTTON FUNCTIONS ------------------
        def add():
            nombre_maquina = inbox_nombre_maquina.get()
            reference = inbox_reference.get()
            voltaje = inbox_Vol.get()
            potence = inbox_potencia.get()
            capacidad = inbox_cap.get()
            presion = inbox_Pres.get()
            descripcion = inbox_des.get()
            size = inbox_size.get()

            contact_check = [nombre_maquina, reference, voltaje, potence, size, presion, capacidad, descripcion]
            if contact_check == ['', '', '', '', '', '', '', '']:
                write_machine()
            else:
                if nombre_maquina == '':
                    nombre_maquina = '<Default>'
                if reference == '':
                    reference = '<Default>'
                if voltaje == '':
                    voltaje = '<Default>'
                if potence == '':
                    potence = '<Default>'
                if capacidad == '':
                    capacidad = '<Default>'
                if presion == '':
                    presion = '<Default>'
                if descripcion == '':
                    descripcion = '<Default>'
                if size == '':
                    size = '<Default>'
                _save(nombre_maquina, reference, voltaje, potence, size, presion, capacidad, descripcion)

                Frame_pro.tree.insert("", 0, text=str(nombre_maquina), values=(
                    str(reference), str(voltaje), str(potence), str(size), str(presion), str(capacidad),
                    str(descripcion)))
                Frame_pro.tree.insert("", 0, text="------------------------------",
                                      values=("------------------------------", "------------------------------",
                                              "------------------------------", "------------------------------",
                                              "------------------------------", "------------------------------",
                                              "------------------------------"))
            contact_check = []
            _clean_inbox()

        def search():
            answer = []
            var_search = str(combo.get())
            if var_search == 'Nombre':
                var_inbox = inbox_nombre_maquina.get()
                possition = 0
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            elif var_search == 'Referencia':
                var_inbox = inbox_reference.get()
                possition = 1
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            else:
                no_found(inbox_nombre_maquina.get())
            _clean_inbox()

        def modify():
            answer = []
            var_search = str(combo.get())
            if var_search == 'Nombre':
                var_inbox = inbox_nombre_maquina.get()
                possition = 0
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)
            elif var_search == 'Referencia':
                var_inbox = inbox_reference.get()
                possition = 1
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)

            _clean_inbox()

        def show_machine():
            Frame_pro.tree.insert("", 0, text="------------------------------",
                                  values=("------------------------------", "------------------------------",
                                          "------------------------------", "------------------------------",
                                          "------------------------------", "------------------------------",
                                          "------------------------------"))
            _view_csv()
            Frame_pro.tree.insert("", 0, text="------------------------------",
                                  values=("------------------------------", "------------------------------",
                                          "------------------------------", "------------------------------",
                                          "------------------------------", "------------------------------",
                                          "------------------------------"))

        def delete():
            nombre_maquina = str(inbox_nombre_maquina.get())
            a = delete_mesageBox(nombre_maquina)
            if a:
                with open('machine_list.csv', 'r') as f:
                    reader = list(csv.reader(f))
                with open('machine_list.csv', 'w') as f:
                    writer = csv.writer(f, lineterminator='\r', delimiter=',')
                    for i, row in enumerate(reader):
                        if nombre_maquina != row[0]:
                            writer.writerow(row)
            clean()
            show_machine()

        def clean():
            _clean_inbox()
            _clean_treeview()


class rendimiento:
    def __init__(self, root):
        frame_rend = Toplevel(root)
        frame_rend.configure(bg="#000000")
        frame_rend.title("Mantenimiento")

        # ----------- MESAGE BOX ---------------------------------------
        def no_found(var):
            var_s = str(var)
            MessageBox.showinfo("No se encuentra el registro", var_s + ' ' + "no se encuentra el registro")

        def write_nombre_maquina():
            MessageBox.showinfo("No se encuentra", "por favor ingrese los datos correctos")

        def delete_mesageBox(nombre_maquina):
            var_nombre_maquina = str(nombre_maquina)
            if var_nombre_maquina == '':
                write_nombre_maquina()
            else:
                search = MessageBox.askquestion("Alerta!!", "desea borrar este registro?\n" + var_nombre_maquina)
                if search == "yes":
                    return True
                else:
                    return False

        # ---------------- FRAMES DECLARATION -----------------
        inbox_frame = LabelFrame(frame_rend, bg="#EFEDB1")
        inbox_frame.grid(row=0, column=0)

        button_frame = LabelFrame(frame_rend, bg="#EFEDB1")
        button_frame.grid(row=2, column=0)

        three_frame = LabelFrame(frame_rend, bg="#EFEDB1")
        three_frame.grid(row=4, column=0)

        three_button_frame = LabelFrame(frame_rend, bg="#EFEDB1")
        three_button_frame.grid(row=5, column=0)

        # --------------- INBOX WIDGETS ZONE ------------------
        Label(inbox_frame, text='Nombre de maquina', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(row=0,
                                                                                                             column=0)
        inbox_nombre_maquina = Entry(inbox_frame, font=("Verdana MS", "11", "normal"), width=28)
        inbox_nombre_maquina.grid(row=1, column=0)
        inbox_nombre_maquina.focus()

        Label(inbox_frame, text='Referencia', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(row=0,
                                                                                                      column=1)
        inbox_referencia = Entry(inbox_frame, font=("Verdana MS", "11", "normal"), width=20)
        inbox_referencia.grid(row=1, column=1)

        Label(inbox_frame, text='Fecha ultimo mantenimiento', bg="#EFEDB1",
              font=("Verdana MS", "11", "normal")).grid(row=0, column=2)
        inbox_fecha_ult = Entry(inbox_frame, font=("Verdana MS", "11", "normal"), width=30)
        inbox_fecha_ult.grid(row=1, column=2)

        Label(inbox_frame, text='Fecha proximo mantenimiento', bg="#EFEDB1",
              font=("Verdana MS", "11", "normal")).grid(row=0, column=3)
        inbox_fecha_new = Entry(inbox_frame, font=("Verdana MS", "11", "normal"), width=30)
        inbox_fecha_new.grid(row=1, column=3)

        # --------------- BUTTON WIDGETS ZONE -----------------
        Add_contact_button = Button(button_frame, command=lambda: add(), text='Agregar mantenimiento', width=20)
        Add_contact_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        Add_contact_button.grid(row=0, column=0, padx=2, pady=3, sticky=W + E)

        search_button = Button(button_frame, command=lambda: search(), text='Buscar', width=20)
        search_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        search_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        delete_button = Button(button_frame, command=lambda: delete(), text='Borrar registro', width=20)
        delete_button.configure(bg="#F26262", cursor='hand2', font=("Verdana MS", "10", "normal"))
        delete_button.grid(row=1, column=0, padx=2, pady=3, sticky=W + E)

        modify_button = Button(button_frame, command=lambda: modify(), text='Modificar registro')
        modify_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        modify_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        show_contacts_button = Button(button_frame, command=lambda: show_contacts(), text='Mostrar registros',
                                      width=20)
        show_contacts_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        show_contacts_button.grid(row=0, column=2, padx=2, pady=3, sticky=W + E)

        save_changes_button = Button(button_frame, command=lambda: clean(), text='Limpiar ventana', width=20)
        save_changes_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        save_changes_button.grid(row=1, column=2, padx=2, pady=3, sticky=W + E)

        # -------------- COMBOBOX WIDGETS ZONE ----------------
        Label(button_frame, text='Buscar por:', bg="#EFEDB1", font=("Verdana MS", "10", "normal")).grid(
            row=0, column=3, columnspan=3)

        combo = ttk.Combobox(button_frame, state='readonly', width=17, justify='center',
                             font=("Verdana MS", "10", "normal"))
        combo["values"] = ['nombre_maquina', 'referencia']
        combo.grid(row=1, column=3, padx=15)
        combo.current(0)

        # --------------- TREE DIRECTORY ZONE -----------------
        # Table for database
        self.tree = ttk.Treeview(three_frame, height=20, columns=("one", "two", "three", "four"))
        self.tree.grid(padx=5, pady=5, row=0, column=0, columnspan=1)
        self.tree.heading("#0", text='Nombre_maquina', anchor=CENTER)
        self.tree.heading("one", text='Referencia', anchor=CENTER)
        self.tree.heading("two", text='Fecha ultimo mantenimiento', anchor=CENTER)
        self.tree.heading("three", text='Fecha nuevo mantenimiento', anchor=CENTER)
        self.tree.heading("four", text='Dias para el mantenimiento', anchor=CENTER)

        # Scroll
        scrollVert = Scrollbar(three_frame, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollVert.set)
        scrollVert.grid(row=0, column=1, sticky="nsew")

        scroll_x = Scrollbar(three_frame, command=self.tree.xview, orient=HORIZONTAL)
        self.tree.configure(xscrollcommand=scroll_x.set)
        scroll_x.grid(row=2, column=0, columnspan=1, sticky="nsew")

        # -------------------------- COMMAND FUNCTIONS DECLARATION -----------------------------

        # --------------- AUXILIAR FUNCTIONS ------------------
        def _clean_inbox():
            # Delete from first position (0) to the last position ('end')
            inbox_nombre_maquina.delete(0, 'end')
            inbox_referencia.delete(0, 'end')
            inbox_fecha_ult.delete(0, 'end')
            inbox_fecha_new.delete(0, 'end')

        def _clean_treeview():
            tree_list = self.tree.get_children()
            for item in tree_list:
                self.tree.delete(item)

        def dias(proximo):
            fecha=proximo.split('/')
            prox = date(int(fecha[2]), int(fecha[1]), int(fecha[0]))
            entrada = prox.strftime('%d/%m/%Y')
            return entrada

        def dias_man(fecha,now):

            days=(fecha-now).days
            return days

        def _view_csv():
            contacts = orden.alphabetic_order_man()
            for i, row in enumerate(contacts):
                nombre_maquina = str(row[0])
                referencia = str(row[1])
                fecha_ult = str(row[2])
                fecha_new = str(row[3])
                faltan = dias(fecha_new)
                fecha = faltan.split('/')
                prox = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]))
                now = datetime.now()
                Date_for = dias_man(prox, now)
                self.tree.insert("", 0, text=nombre_maquina, values=(referencia, fecha_ult, fecha_new,Date_for))

        def _save(nombre_maquina, referencia, fecha_ult, fecha_new):
            s_nombre_maquina = nombre_maquina
            s_referencia = referencia
            s_fecha_ult = fecha_ult
            s_fecha_new = fecha_new

            with open('registro_mant.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_nombre_maquina, s_referencia, s_fecha_ult, s_fecha_new))

        def _search(var_inbox, possition):
            my_list = []
            s_var_inbox = str(var_inbox)
            var_possition = int(possition)
            with open('registro_mant.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if s_var_inbox == row[var_possition]:
                        my_list = [row[0], row[1], row[2], row[3]]
                        break
                    else:
                        continue
            return my_list

        def _check(answer, var_search):
            list_answer = answer
            var_search = var_search
            if not list_answer:
                no_found(var_search)
            else:
                nombre_maquina = str(list_answer[0])
                referencia = str(list_answer[1])
                fecha_ult = str(list_answer[2])
                fecha_new = str(list_answer[3])
                faltan = dias(fecha_new)
                fecha = faltan.split('/')
                prox = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]))
                now = datetime.now()
                Date_for = dias_man(prox, now)
                self.tree.insert("", 0, text="------------------------------",
                                 values=("------------------------------", "------------------------------",
                                         "------------------------------","------------------------------","------------------------------"))
                self.tree.insert("", 0, text=nombre_maquina, values=(referencia, fecha_ult, fecha_new,Date_for))
                self.tree.insert("", 0, text="------------------------------",
                                 values=("------------------------------", "------------------------------",
                                         "------------------------------","------------------------------","------------------------------"))

        def _check_1(answer, var_search):
            val_modify = answer
            var = var_search
            if not val_modify:
                no_found(var)
            else:
                TopLevelModify(frame_rend, val_modify)

        # ----------------- BUTTON FUNCTIONS ------------------
        def add():
            nombre_maquina = inbox_nombre_maquina.get()
            referencia = inbox_referencia.get()
            fecha_ult = inbox_fecha_ult.get()
            fecha_new = inbox_fecha_new.get()
            contact_check = [nombre_maquina, referencia, fecha_ult, fecha_new]
            if contact_check == ['', '', '', '']:
                write_nombre_maquina()
            else:
                if nombre_maquina == '':
                    nombre_maquina = '<Default>'
                if referencia == '':
                    referencia = '<Default>'
                if fecha_ult == '':
                    fecha_ult = '<Default>'
                if fecha_new == '':
                    fecha_new = '<Default>'
                faltan = dias(fecha_new)
                fecha = faltan.split('/')
                prox = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]))
                now = datetime.now()
                Date_for = dias_man(prox, now)
                _save(nombre_maquina, referencia, fecha_ult, fecha_new)
                self.tree.insert("", 0, text="------------------------------",
                                 values=("------------------------------", "------------------------------",
                                         "------------------------------","------------------------------" , "------------------------------"))
                self.tree.insert("", 0, text=str(nombre_maquina),
                                 values=(str(referencia), str(fecha_ult), str(fecha_new), str(Date_for)))
                self.tree.insert("", 0, text="------------------------------",
                                 values=("------------------------------", "------------------------------",
                                         "------------------------------","------------------------------","------------------------------"))
            contact_check = []
            _clean_inbox()

        def search():
            answer = []
            var_search = str(combo.get())
            if var_search == 'nombre_maquina':
                var_inbox = inbox_nombre_maquina.get()
                possition = 0
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            elif var_search == 'referencia':
                var_inbox = inbox_referencia.get()
                possition = 1
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            _clean_inbox()

        def modify():
            answer = []
            var_search = str(combo.get())
            if var_search == 'nombre_maquina':
                var_inbox = inbox_nombre_maquina.get()
                possition = 0
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)
            elif var_search == 'referencia':
                var_inbox = inbox_referencia.get()
                possition = 1
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)

            _clean_inbox()

        def show_contacts():
            self.tree.insert("", 0, text="------------------------------",
                             values=("------------------------------", "------------------------------",
                                     "------------------------------","------------------------------"))
            _view_csv()
            self.tree.insert("", 0, text="------------------------------",
                             values=("------------------------------", "------------------------------",
                                     "------------------------------","------------------------------"))

        def delete():
            nombre_maquina = str(inbox_nombre_maquina.get())
            a = delete_mesageBox(nombre_maquina)
            if a:
                with open('registro_mant.csv', 'r') as f:
                    reader = list(csv.reader(f))
                with open('registro_mant.csv', 'w') as f:
                    writer = csv.writer(f, lineterminator='\r', delimiter=',')
                    for i, row in enumerate(reader):
                        if nombre_maquina != row[0]:
                            writer.writerow(row)
            clean()
            show_contacts()

        def clean():
            _clean_inbox()
            _clean_treeview()


class TopLevelModify():
    def __init__(self, root, val_modify):
        self.root_window = root
        self.val_modify = val_modify
        self.nombre_maquina = str(self.val_modify[0])
        self.referencia = str(self.val_modify[1])
        self.fecha_ult = str(self.val_modify[2])
        self.fecha_new =str(self.val_modify[3])

        window_modify = Toplevel(self.root_window)
        window_modify.title("Modificar registro")
        window_modify.configure(bg="#000000")
        window_modify.geometry("+400+100")
        window_modify.resizable(0, 0)

        def modify_mesageBox(contact):
            var_nombre_maquina = str(contact[0])
            var_referencia = str(contact[1])
            var_fecha_ult = str(contact[2])
            var_fecha_new = str(contact[3])
            search = MessageBox.askquestion("Alerta de modificacion",
                                            "Desea guardar los cambios realizados en este registro?\n" + " Nombre: " + var_nombre_maquina + "\n Referencia: " + var_referencia + "\n fecha ultimo mantenimiento: " + var_fecha_ult + "\n fecha proximo mantenimiento" + var_fecha_new)
            if search == "yes":
                return True
            else:
                return False

        # ---------------- FRAMES DECLARATION -----------------
        text_frame = LabelFrame(window_modify, bg="#EFEDB1")
        text_frame.grid(row=0, column=0)

        button_frame = LabelFrame(window_modify, bg="#EFEDB1")
        button_frame.grid(row=2, column=0)

        # --------------- LABELS WIDGETS ZONE -----------------
        Label(text_frame, text="Desea modificar este registro?", bg="#EFEDB1",
              font=("Verdana MS", "11", "normal")).grid(row=0, column=0, columnspan=3)
        Label(text_frame, text=self.nombre_maquina, bg="#EFEDB1",
              font=("Verdana MS", "11", "bold")).grid(row=1,
                                                      column=0)
        Label(text_frame, text=self.referencia, bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(
            row=1, column=1)
        Label(text_frame, text=self.fecha_ult, bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(
            row=1, column=2)
        Label(text_frame, text=self.fecha_new, bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(
            row=1, column=3)
        # --------------- INBOX WIDGETS ZONE ------------------
        Label(text_frame, text='ingrese el nombre de la maquina', bg="#EFEDB1",
              font=("Verdana MS", "11", "normal")).grid(
            row=2,
            column=0)
        n_inbox_nombre_maquina = Entry(text_frame, font=("Verdana MS", "11", "normal"), width=28)
        n_inbox_nombre_maquina.grid(row=3, column=0)
        n_inbox_nombre_maquina.focus()

        Label(text_frame, text='Ingrese la referencia', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(row=2,
                                                                                                                column=1)
        n_inbox_referencia = Entry(text_frame, font=("Verdana MS", "11", "normal"), width=20)
        n_inbox_referencia.grid(row=3, column=1)

        Label(text_frame, text='ingrese ultimo mantenimiento', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(
            row=2,
            column=2)
        n_inbox_fecha_ult = Entry(text_frame, font=("Verdana MS", "11", "normal"), width=30)
        n_inbox_fecha_ult.grid(row=3, column=2)

        Label(text_frame, text='ingrese proximo mantenimiento', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(
            row=2,
            column=3)
        n_inbox_fecha_new = Entry(text_frame, font=("Verdana MS", "11", "normal"), width=30)
        n_inbox_fecha_new.grid(row=3, column=3)

        # --------------- BUTTON WIDGETS ZONE -----------------
        yes_button = Button(button_frame, command=lambda: yes(), text='Si', width=20)
        yes_button.configure(bg="#F26262", cursor='hand2', font=("Verdana MS", "10", "normal"))
        yes_button.grid(row=1, column=0, padx=2, pady=3, sticky=W + E)

        no_button = Button(button_frame, command=window_modify.destroy, text='No', width=20, bg="yellow",
                           cursor='hand2')
        no_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        no_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        cancel_button = Button(button_frame, command=window_modify.destroy, text='Cancelar', width=20, bg="green",
                               cursor='hand2')
        cancel_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        cancel_button.grid(row=1, column=2, padx=2, pady=3, sticky=W + E)

        # ----------------- BUTTON FUNCTIONS ------------------
        def yes():
            contact = self.val_modify
            new_nombre_maquina = n_inbox_nombre_maquina.get()
            new_referencia = n_inbox_referencia.get()
            new_fecha_ult = n_inbox_fecha_ult.get()
            new_fecha_new = n_inbox_fecha_new.get()
            a = modify_mesageBox(contact)
            if a:
                _del_old(contact[0])
                _add_new(new_nombre_maquina, new_referencia, new_fecha_ult, n_inbox_fecha_new)
            window_modify.destroy()

        def _add_new(nombre_maquina, referencia, fecha_ult, fecha_new):
            s_nombre_maquina = nombre_maquina
            s_referencia = referencia
            s_fecha_ult = fecha_ult
            s_fecha_new = fecha_new
            with open('registro_mant.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_nombre_maquina, s_referencia, s_fecha_ult, s_fecha_new))

        def _del_old(old_nombre_maquina):
            nombre_maquina = old_nombre_maquina
            with open('registro_mant.csv', 'r') as f:
                reader = list(csv.reader(f))
            with open('registro_mant.csv', 'w') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                for i, row in enumerate(reader):
                    if nombre_maquina != row[0]:
                        writer.writerow(row)
