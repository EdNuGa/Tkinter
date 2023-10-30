import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as quelcom
import os

def openWindow():
    filetypes = (("Tots els arxius", "*.*"), ("Imatges tipus jpg", "*.jpg"))
    initialdir = os.getcwd()
    archivo = quelcom.askopenfilename(initialdir=initialdir, filetypes=filetypes)
    imatge1_crua = Image.open(archivo)
    imatge1_tk = ImageTk.PhotoImage(imatge1_crua)
    if archivo:
        ventana_top = tk.Toplevel()
        ventana_top.title("Imagen")
        frame_top = tk.Frame(ventana_top, bg="lightblue")
        frame_top.pack()
        ventana1 = tk.Label(frame_top, image=imatge1_tk)
        ventana1.image = imatge1_tk
        ventana1.pack()
        texto = tk.Label(frame_top, text="El path es: " + archivo, bg="orange")
        texto.pack()
        botonSave = tk.Button(ventana_top, text="Guardar foto", command= lambda: saveImg(imatge1_crua))
        botonSave.pack()
        

def saveImg(img):
    file = quelcom.asksaveasfile(defaultextension=".jpg", filetypes=[("Imatges tipus jpg", "*.jpg"), ("Imatges tipus png", "*.png"),("Tots els arxius", "*.*")])
    if img.format != ".jpg":
        img_rgb = img.convert("RGB")
        img_rgb.save(file.name)
    else:
        img.save(file.name)
    

root = tk.Tk()
root.geometry("30x25")
root.title("Buscador de imágenes")

boton = tk.Button(root, text="Abrir foto", command=openWindow)
boton.pack()

root.mainloop()
