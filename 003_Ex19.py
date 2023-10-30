import tkinter as tk
from tkinter import messagebox

var_fe = None

def crida(boton):
    global var_fe
    if boton == "info":
        var_fe = messagebox.showinfo("Ventana emergente", "Prueba")
    elif boton == "warning":
        var_fe = messagebox.showwarning("Ventana emergente", "Prueba")
    elif boton == "error":
        var_fe = messagebox.showerror("Ventana emergente", "Prueba")
    elif boton == "question":
        var_fe = messagebox.askquestion("Ventana emergente", "Prueba")
        if var_fe == "yes":
            var_fe = "si"
    elif boton == "ok":
        var_fe = messagebox.askokcancel("Ventana emergente", "Prueba")
        if var_fe == True:
            var_fe = "si"
        elif var_fe == False:
            var_fe = "no"
    elif boton == "yes":
        var_fe = messagebox.askyesno("Ventana emergente", "Prueba")
        if var_fe == True:
            var_fe = "si"
        elif var_fe == False:
            var_fe = "no"
    ventana_prin.configure(text="El usuario ha clicado en " + str(var_fe))

root = tk.Tk()
root.title("Ventanas emergentes")
root.resizable(False,False)

ventana_prin = tk.Label(root, pady="5", padx="140", bg="lightblue")
ventana_prin.grid(row=0)
botonera = tk.LabelFrame(root, text="Botonera", bg="darkblue", fg="white")
botonera.grid(row=1)

info = tk.Button(botonera, text="Show Info", width="12", height="1", command=lambda: crida("info"))
info.grid(row=1,column=0)
warning = tk.Button(botonera, text="Show Warning", width="12", height="1", command=lambda: crida("warning"))
warning.grid(row=1,column=1)
error = tk.Button(botonera, text="Show Error", width="12", height="1", command=lambda: crida("error"))
error.grid(row=1,column=2)
askquest = tk.Button(botonera, text="Ask Question", width="12", height="1", command=lambda: crida("question"))
askquest.grid(row=2,column=0)
askokcancel = tk.Button(botonera, text="Ask Ok Cancel", width="12", height="1", command=lambda: crida("ok"))
askokcancel.grid(row=2,column=1)
askyesno = tk.Button(botonera, text="Ask Yes No", width="12", height="1", command=lambda: crida("yes"))
askyesno.grid(row=2,column=2)

root.mainloop()
