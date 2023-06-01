from tkinter import messagebox as MessageBox
from tkinter import *
from tkinter import ttk
import csv, orden



def no_found(var):
    var_s = str(var)
    MessageBox.showinfo("No se encuentra el registro", var_s + ' ' + "no se encuentra el registro")

def write_tipo():
    MessageBox.showinfo("No se encuentra", "por favor escriba los datos correctos")

def delete_mesageBox(tipo):
    var_tipo = str(tipo)
    if var_tipo == '':
        write_tipo()
    else:
        search = MessageBox.askquestion("Alerta!!", "desea borrar este registro?\n" + var_tipo)
        if search == "yes":
            return True
        else:
            return False


def modify_mesageBox(contact):
    var_tipo = str(contact[0])
    var_valor = str(contact[1])
    var_fecha = str(contact[2])
    search = MessageBox.askquestion("Alerta de modificacion",
                                    "Desea guardar los cambios realizados en este registro?\n" + " tipo de zapato: " + var_tipo + "\n Valor a pagar: " + var_valor + "\n fecha de entrega: " + var_fecha)
    if search == "yes":
        return True
    else:
        return False


# --------------------  APP CLASS USUARIO-------------------------------
class registros_compras:
    def __init__(self, root):
        frame_reg = Toplevel(root)

        frame_reg.configure(bg="#000000")
        frame_reg.title("Registrar pedido")
        frame_reg.geometry("+350+80")
        frame_reg.resizable(0, 0)

        # ---------------- FRAMES DECLARATION -----------------
        inbox_frame = LabelFrame(frame_reg, bg="#EFEDB1")
        inbox_frame.grid(row=0, column=0)
        button_frame = LabelFrame(frame_reg, bg="#EFEDB1")
        button_frame.grid(row=2, column=0)
        three_frame = LabelFrame(frame_reg, bg="#EFEDB1")
        three_frame.grid(row=4, column=0)
        three_button_frame = LabelFrame(frame_reg, bg="#EFEDB1")
        three_button_frame.grid(row=5, column=0)


        # --------------- INBOX WIDGETS ZONE ------------------
        Label(inbox_frame, text='Tipo de zapato', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(row=0, column=0)
        inbox_tipo = Entry(inbox_frame, font=("Verdana MS", "11", "normal"), width=28)
        inbox_tipo.grid(row=1, column=0)
        inbox_tipo.focus()

        Label(inbox_frame, text='Valor a pagar', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(row=0, column=1)
        inbox_valor = Entry(inbox_frame, font=("Verdana MS", "11", "normal"), width=20)
        inbox_valor.grid(row=1, column=1)

        Label(inbox_frame, text='Fecha de entrega', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(row=0, column=2)
        inbox_fecha = Entry(inbox_frame, font=("Verdana MS", "11", "normal"), width=30)
        inbox_fecha.grid(row=1, column=2)

        # --------------- BUTTON WIDGETS ZONE -----------------

        search_button = Button(button_frame, command=lambda: search(), text='Buscar registro', width=20)
        search_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        search_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        delete_button = Button(button_frame, command=lambda: delete(), text='Borrar registro', width=20)
        delete_button.configure(bg="#F26262", cursor='hand2', font=("Verdana MS", "10", "normal"))
        delete_button.grid(row=1, column=0, padx=2, pady=3, sticky=W + E)

        modify_button = Button(button_frame, command=lambda: modify(), text='Modificar registro')
        modify_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        modify_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        show_contacts_button = Button(button_frame, command=lambda: show_contacts(), text='Mostrar todos los registros', width=20)
        show_contacts_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        show_contacts_button.grid(row=0, column=2, padx=2, pady=3, sticky=W + E)

        save_changes_button = Button(button_frame, command=lambda: clean(), text='limpiar', width=20)
        save_changes_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        save_changes_button.grid(row=1, column=2, padx=2, pady=3, sticky=W + E)

        # -------------- COMBOBOX WIDGETS ZONE ----------------
        Label(button_frame, text='Buscar por:', bg="#EFEDB1", font=("Verdana MS", "10", "normal")).grid(
            row=0, column=3, columnspan=3)

        combo = ttk.Combobox(button_frame, state='readonly', width=17, justify='center',
                             font=("Verdana MS", "10", "normal"))
        combo["values"] = ['Tipo de zapato', 'Valor a pagar', 'Fecha de entrega']
        combo.grid(row=1, column=3, padx=15)
        combo.current(0)

        # --------------- TREE DIRECTORY ZONE -----------------
        # Table for database
        self.tree = ttk.Treeview(three_frame, height=20, columns=("one", "two"))
        self.tree.grid(padx=5, pady=5, row=0, column=0, columnspan=1)
        self.tree.heading("#0", text='Tipo de zapato', anchor=CENTER)
        self.tree.heading("one", text='Valor a pagar', anchor=CENTER)
        self.tree.heading("two", text='Fecha de entrega', anchor=CENTER)

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
            inbox_tipo.delete(0, 'end')
            inbox_valor.delete(0, 'end')
            inbox_fecha.delete(0, 'end')

        def _clean_treeview():
            tree_list = self.tree.get_children()
            for item in tree_list:
                self.tree.delete(item)

        def _view_csv():
            contacts = orden.alphabetic_order_ped()
            for i, row in enumerate(contacts):
                tipo = str(row[0])
                valor = str(row[1])
                fecha = str(row[2])
                self.tree.insert("", 0, text=tipo, values=(valor, fecha))



        def _search(var_inbox, possition):
            my_list = []
            s_var_inbox = str(var_inbox)
            var_possition = int(possition)
            with open('Lista_registros_compras.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if s_var_inbox == row[var_possition]:
                        my_list = [row[0], row[1], row[2]]
                        break
                    else:
                        continue
            return my_list

        def _check(answer, var_search):
            list_answer = answer
            var_search = var_search
            if list_answer == []:
                no_found(var_search)
            else:
                tipo = str(list_answer[0])
                valor = str(list_answer[1])
                fecha = str(list_answer[2])
                self.tree.insert("", 0, text="------------------------------",
                                 values=("------------------------------", "------------------------------"))
                self.tree.insert("", 0, text=tipo, values=(valor, fecha))
                self.tree.insert("", 0, text="------------------------------",
                                 values=("------------------------------", "------------------------------"))

        def _check_1(answer, var_search):
            val_modify = answer
            var = var_search
            if val_modify == []:
                no_found(var)
            else:
                TopLevelModify(frame_reg, val_modify)

        # ----------------- BUTTON FUNCTIONS ------------------
       

        def search():
            answer = []
            var_search = str(combo.get())
            if var_search == 'Tipo de zapato':
                var_inbox = inbox_tipo.get()
                possition = 0
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            elif var_search == 'Valor a pagar':
                var_inbox = inbox_valor.get()
                possition = 1
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            else:
                var_inbox = inbox_fecha.get()
                possition = 2
                answer = _search(var_inbox, possition)
                _check(answer, var_search)
            _clean_inbox()

        def modify():
            answer = []
            var_search = str(combo.get())
            if var_search == 'Tipo de zapato':
                var_inbox = inbox_tipo.get()
                possition = 0
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)
            elif var_search == 'Valor a pagar':
                var_inbox = inbox_valor.get()
                possition = 1
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)
            else:
                var_inbox = inbox_fecha.get()
                possition = 2
                answer = _search(var_inbox, possition)
                _check_1(answer, var_search)
            _clean_inbox()

        def show_contacts():
            self.tree.insert("", 0, text="------------------------------",
                             values=("------------------------------", "------------------------------"))
            _view_csv()
            self.tree.insert("", 0, text="------------------------------",
                             values=("------------------------------", "------------------------------"))

        def delete():
            tipo = str(inbox_tipo.get())
            a = delete_mesageBox(tipo)
            if a == True:
                with open('Lista_registros_compras.csv', 'r') as f:
                    reader = list(csv.reader(f))
                with open('Lista_registros_compras.csv', 'w') as f:
                    writer = csv.writer(f, lineterminator='\r', delimiter=',')
                    for i, row in enumerate(reader):
                        if tipo != row[0]:
                            writer.writerow(row)
            clean()
            show_contacts()

        def clean():
            _clean_inbox()
            _clean_treeview()


# ------------------------- TOP LEVE WINDOW ----------------------------------------------

class TopLevelModify():
    def __init__(self, root, val_modify):
        self.root_window = root
        self.val_modify = val_modify
        self.tipo = str(self.val_modify[0])
        self.valor = str(self.val_modify[1])
        self.fecha = str(self.val_modify[2])

        window_modify = Toplevel(self.root_window)
        window_modify.title("Modificar registro de venta")
        window_modify.configure(bg="#EFEDB1")
        window_modify.geometry("+400+100")
        window_modify.resizable(0, 0)

        # ---------------- FRAMES DECLARATION -----------------
        text_frame = LabelFrame(window_modify, bg="#EFEDB1")
        text_frame.grid(row=0, column=0)

        button_frame = LabelFrame(window_modify, bg="#EFEDB1")
        button_frame.grid(row=2, column=0)

        # --------------- LABELS WIDGETS ZONE -----------------
        Label(text_frame, text="Desea modificar este registro ?", bg="#EFEDB1",
              font=("Verdana MS", "11", "normal")).grid(row=0, column=0, columnspan=3)
        Label(text_frame, text=self.tipo, bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=1, column=0)
        Label(text_frame, text=self.valor, bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=1, column=1)
        Label(text_frame, text=self.fecha, bg="#EFEDB1", font=("Verdana MS", "11", "bold")).grid(row=1, column=2)

        # --------------- INBOX WIDGETS ZONE ------------------
        Label(text_frame, text='Escriba el tipo de zapato', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(row=2,
                                                                                                              column=0)
        n_inbox_tipo = Entry(text_frame, font=("Verdana MS", "11", "normal"), width=28)
        n_inbox_tipo.grid(row=3, column=0)
        n_inbox_tipo.focus()

        Label(text_frame, text='Ingrese el valor a pagar', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(row=2,
                                                                                                               column=1)
        n_inbox_valor = Entry(text_frame, font=("Verdana MS", "11", "normal"), width=20)
        n_inbox_valor.grid(row=3, column=1)

        Label(text_frame, text='Escriba la fecha de entrega', bg="#EFEDB1", font=("Verdana MS", "11", "normal")).grid(row=2,
                                                                                                               column=2)
        n_inbox_fecha = Entry(text_frame, font=("Verdana MS", "11", "normal"), width=30)
        n_inbox_fecha.grid(row=3, column=2)

        # --------------- BUTTON WIDGETS ZONE -----------------
        yes_button = Button(button_frame, command=lambda: yes(), text='Yes', width=20)
        yes_button.configure(bg="#F26262", cursor='hand2', font=("Verdana MS", "10", "normal"))
        yes_button.grid(row=1, column=0, padx=2, pady=3, sticky=W + E)

        no_button = Button(button_frame, command=window_modify.destroy, text='No', width=20, bg="yellow",
                           cursor='hand2')
        no_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        no_button.grid(row=1, column=1, padx=2, pady=3, sticky=W + E)

        cancel_button = Button(button_frame, command=window_modify.destroy, text='Cancel', width=20, bg="green",
                               cursor='hand2')
        cancel_button.configure(bg="#FFBB20", cursor='hand2', font=("Verdana MS", "10", "normal"))
        cancel_button.grid(row=1, column=2, padx=2, pady=3, sticky=W + E)

        # ----------------- BUTTON FUNCTIONS ------------------
        def yes():
            contact = self.val_modify
            new_tipo = n_inbox_tipo.get()
            new_valor = n_inbox_valor.get()
            new_fecha = n_inbox_fecha.get()
            a = modify_mesageBox(contact)
            if a:
                _del_old(contact[0])
                _add_new(new_tipo, new_valor, new_fecha)
            window_modify.destroy()

        def _add_new(tipo, valor, fecha):
            s_tipo = tipo
            s_valor = valor
            s_fecha = fecha
            with open('Lista_registros_compras.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                writer.writerow((s_tipo, s_valor, s_fecha))

        def _del_old(old_tipo):
            tipo = old_tipo
            with open('Lista_registros_compras.csv', 'r') as f:
                reader = list(csv.reader(f))
            with open('Lista_registros_compras.csv', 'w') as f:
                writer = csv.writer(f, lineterminator='\r', delimiter=',')
                for i, row in enumerate(reader):
                    if tipo != row[0]:
                        writer.writerow(row)


