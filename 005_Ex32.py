import tkinter as tk
import sqlite3
from tkinter import filedialog as quelcom
import os

#Función para mostrar los datos de la base de datos.
def verDatos():
    #Conexión.
    conectar = sqlite3.connect("db/basquet.db")
    cursor = conectar.cursor()
    #Query.
    cursor.execute("SELECT * FROM jugadors")
    #Cargar información en datos.
    datos = cursor.fetchall()
    #Cerrar base de datos.
    conectar.close()
    #Actualiza el panel informativo para el usuario.
    infoLabel.config(text="Nombre | apellido | altura | edad", fg="black")
    #Muestra la información en la aplicación.
    dblabel.config(text="\n".join([str(fila) for fila in datos]))

def insertarDatos():
    #Variables globales donde se almacena los datos a introducir.
    global nomEnt
    global apeEnt
    global altEnt
    global edadEnt
    #Conexión.
    conectar = sqlite3.connect("db/basquet.db")
    cursor = conectar.cursor()
    #Mientras no haya ningún campo vacío.
    if nomEnt.get() and apeEnt.get() and altEnt.get() and edadEnt.get():
        #Intenta conectar.
        try:
            #Envía los datos.
            cursor.execute("INSERT INTO jugadors (nombre, apellido, altura, edad) VALUES (?, ?, ?, ?)",
                           (nomEnt.get(), apeEnt.get(), altEnt.get(), edadEnt.get()))
            conectar.commit()
            infoLabel.config(text="Datos insertados correctamente", fg="green")
            #Borra los campos.
            nomEnt.delete(0,tk.END)
            apeEnt.delete(0,tk.END)
            altEnt.delete(0,tk.END)
            edadEnt.delete(0,tk.END)
        #Si el nombre ya existe, salta excepción (Por ser clave primaria).
        except sqlite3.IntegrityError:
            infoLabel.config(text="El nombre ya existe en la base de datos", fg="red")
            dblabel.config(text="")
    else:
        infoLabel.config(text="Completa todos los campos", fg="red")
        dblabel.config(text="")
    conectar.close()

def borrarDatos():
    global nomEnt
    conectar = sqlite3.connect("db/basquet.db")
    cursor = conectar.cursor()
    nomBorrar = nomEnt.get()
    if nomBorrar:
        #Verifica si el usuario existe en la base de datos.
        cursor.execute("SELECT nombre FROM jugadors WHERE nombre = ?", (nomBorrar,))
        resultado = cursor.fetchone()
        
        if resultado:
            #Si el usuario existe, proceder a borrarlo.
            try:
                #Borrar datos.
                cursor.execute("DELETE FROM jugadors WHERE nombre = ?", (nomBorrar,))
                conectar.commit()
                infoLabel.config(text=f"Datos de " + nomBorrar + " borrados correctamente", fg="green")
                nomEnt.delete(0, tk.END)
            except sqlite3.IntegrityError:
                infoLabel.config(text=f"No se pudo borrar el registro " + nomBorrar, fg="red")
                dblabel.config(text="")
        else:
            infoLabel.config(text=f"El usuario " + nomBorrar + " no existe en la base de datos", fg="red")
            dblabel.config(text="")
    else:
        infoLabel.config(text="Ingresa un nombre para borrar", fg="red")
        dblabel.config(text="")
    
    conectar.close()

def salir():
    root.destroy()

root = tk.Tk()
root.title("Base de dades")
root.geometry("300x250")
root.resizable(True, True)

#Creación de los diferentes frames en la ventana principal.
#Frame para introducir los datos en la aplicación.
datosDB = tk.LabelFrame(root, text="Datos a introducir", padx="19", bg="lightblue")
datosDB.pack()
#Frame para enviar los datos a la base de datos o salir de la aplicación.
botoneraDatos = tk.LabelFrame(root, text="Gestionar base de datos", padx="30", bg="lightyellow")
botoneraDatos.pack()
#Frame para unir los datos a mostrar.
infoFrame = tk.LabelFrame(root, text="Información")
infoFrame.pack()
#Label para imprimir detalles al usuario.
infoLabel = tk.Label(infoFrame, )
infoLabel.pack()
#Label para ver los datos.
dblabel = tk.Label(infoFrame, text="", padx="20")
dblabel.pack()

#Creació de entry para los datos a insertar en la base de datos.
nomLab = tk.Label(datosDB, text = "Nombre: ", bg="lightblue")
nomLab.grid(row=0,column=0)
nomEnt = tk.Entry(datosDB, )
nomEnt.grid(row=0,column=1)
apeLab = tk.Label(datosDB, text = "Apellido: ", bg="lightblue")
apeLab.grid(row=1,column=0)
apeEnt = tk.Entry(datosDB, )
apeEnt.grid(row=1,column=1)
altLab = tk.Label(datosDB, text = "Altura: ", bg="lightblue")
altLab.grid(row=2,column=0)
altEnt = tk.Entry(datosDB, )
altEnt.grid(row=2,column=1)
edadLab = tk.Label(datosDB, text = "Edad: ", bg="lightblue")
edadLab.grid(row=3,column=0)
edadEnt = tk.Entry(datosDB, )
edadEnt.grid(row=3,column=1)

#Creación de botones para enviar los datos a la base de datos o salir de la aplicación.
enviarBot = tk.Button(botoneraDatos, text="Enviar datos", command=insertarDatos)
enviarBot.grid(row=0, column=0)
salirBot = tk.Button(botoneraDatos, text="Salir", padx="25", command=salir)
salirBot.grid(row=0, column=1)
conectBot = tk.Button(botoneraDatos, text="Ver datos ", padx="7", command=verDatos)
conectBot.grid(row=1, column=0)
borrarBot = tk.Button(botoneraDatos, text="Borrar", padx="20", command=borrarDatos)
borrarBot.grid(row=1, column=1)

root.mainloop()
