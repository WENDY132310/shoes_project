from tkinter import *
import Start


def main():
    # ----------------- declaracion de root ------------------
    root = Tk()
    root.title('Fabrica de calzado')
    root.configure(bg="#000000")
    root.geometry("+350+80")
    root.resizable(0, 0)
    Start.login(root)  # Llamado app

    root.mainloop()




if __name__ == "__main__":
    main()

