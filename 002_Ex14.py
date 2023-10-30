import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def siguiente():
    ventana1.quit()
    global imagen
    global num
    num = num +1
    imagen = Image.open(mi_lista[num])
    imagen = ImageTk.PhotoImage(imagen)
    ventana1.configure(image=imagen)
    ventana1.image = imagen
    contador.configure(text="Imagen " + str(num+1) + " de " + str(len(mi_lista)))
    if num == len(mi_lista) - 1:
        boton_siguiente.config(state="disabled")
    else:
        boton_siguiente.config(state="normal")
        boton_anterior.config(state="normal")

def anterior():
    ventana1.quit()
    global imagen
    global num
    num = num -1
    imagen = Image.open(mi_lista[num])
    imagen = ImageTk.PhotoImage(imagen)
    ventana1.configure(image=imagen)
    ventana1.image = imagen
    contador.configure(text="Imagen " + str(num+1) + " de " + str(len(mi_lista)))
    if num == 0:
        boton_anterior.config(state="disabled")
    else:
        boton_anterior.config(state="normal")
        boton_siguiente.config(state="normal")

def salir():
    root.destroy()

root = tk.Tk()
root.title("Mostrar imagenes")

mi_lista = ["./Imagenes/icon.png","./Imagenes/icon2.png","./Imagenes/icon3.png"]

num = 0
imagen = Image.open(mi_lista[num])
imagen = ImageTk.PhotoImage(imagen)

ventana1 = tk.Label(root, image=imagen)
ventana1.grid(row=0, column= 0)

boton_siguiente = tk.Button(root, command= siguiente ,text="Siguiente")
boton_siguiente.grid(row=1, column=2)
boton_anterior = tk.Button(root, command=anterior, text="Anterior", state=tk.DISABLED)
boton_anterior.grid(row=1, column=1)
boton_exit = tk.Button(root, command= salir ,text="Salir")
boton_exit.grid(row=1, column=0, sticky="w")

contador = tk.Label(root, bd=4, relief="sunken" ,text="Imagen " + str(num+1) + " de " + str(len(mi_lista)))
contador.grid(row=2 , column=2, sticky="e")

root.mainloop()
