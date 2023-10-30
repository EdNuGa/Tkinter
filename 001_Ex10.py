import tkinter as tk

operado = 0
operando = 0
resultado = 0
operacion = ""

def numero(num):
    ventana_calc.config(text=ventana_calc["text"] + str(num))

def operar(op):
    global operacion
    global operado
    operacion = op
    operado = ventana_calc["text"]
    ventana_calc.config(text="")
    ventana_info.config(text=str(operado) + str(operacion))

def reset():
    global resultado
    global operacion
    global operado
    global operando
    ventana_calc.config(text="")
    operacion = ""
    resultado = 0
    operado = 0
    operando = 0

def resolver():
    global resultado
    global operacion
    global operado
    global operando
    operando = ventana_calc["text"]
    if operacion == "+":
        resultado = int(operado) + int(operando)
    elif operacion == "-":
        resultado = int(operado) - int(operando)
    elif operacion == "x":
        resultado = int(operado) * int(operando)
    elif operacion == "/":
        resultado = int(operado) // int(operando)
    ventana_calc.config(text= str(resultado))
    ventana_info.config(text=str(operado) + str(operacion) + str(operando))
    operacion = ""
    resultado = 0
    operado = 0
    operando = 0
    

inicio = tk.Tk()
inicio.title("Calculadora")
inicio.geometry("160x370")
inicio.resizable(False, False)
ventana_prin = tk.Label(inicio, bg="lightblue")
ventana_prin.pack()
ventana_info = tk.Label(ventana_prin, text="", width="15", height="2", bg="#fd9068", relief="solid", borderwidth=1)
ventana_info.pack()
ventana_calc = tk.Label(ventana_prin, text="", width="15", height="2", bg="white", relief="solid", borderwidth=1)
ventana_calc.pack()
botonera = tk.LabelFrame(ventana_prin, text="Calculadora", bg="lightblue")
botonera.pack()


boton1 = tk.Button(botonera, command=lambda: numero("1"), text="1", width="4", height="4", bg="silver", relief="solid", borderwidth=1).grid(row=0, column=0)
boton2 = tk.Button(botonera, command=lambda: numero("2"), text="2", width="4", height="4", bg="silver", relief="solid", borderwidth=1).grid(row=0, column=1)
boton3 = tk.Button(botonera, command=lambda: numero("3"), text="3", width="4", height="4", bg="silver", relief="solid", borderwidth=1).grid(row=0, column=2)
boton4 = tk.Button(botonera, command=lambda: numero("4"), text="4", width="4", height="4", bg="silver", relief="solid", borderwidth=1).grid(row=1, column=0)
boton5 = tk.Button(botonera, command=lambda: numero("5"), text="5", width="4", height="4", bg="silver", relief="solid", borderwidth=1).grid(row=1, column=1)
boton6 = tk.Button(botonera, command=lambda: numero("6"), text="6", width="4", height="4", bg="silver", relief="solid", borderwidth=1).grid(row=1, column=2)
boton7 = tk.Button(botonera, command=lambda: numero("7"), text="7", width="4", height="4", bg="silver", relief="solid", borderwidth=1).grid(row=2, column=0)
boton8 = tk.Button(botonera, command=lambda: numero("8"), text="8", width="4", height="4", bg="silver", relief="solid", borderwidth=1).grid(row=2, column=1)
boton9 = tk.Button(botonera, command=lambda: numero("9"), text="9", width="4", height="4", bg="silver", relief="solid", borderwidth=1).grid(row=2, column=2)
boton0 = tk.Button(botonera, command=lambda: numero("0"), text="0", width="4", height="4", bg="silver", relief="solid", borderwidth=1).grid(row=3, column=1)
botonCer = tk.Button(botonera, command=reset, text="C", width="4", height="4", bg="grey", relief="solid", borderwidth=1).grid(row=3, column=2)
botonSum = tk.Button(botonera, command=lambda: operar("+"), text="+", width="4", height="4", bg="#98ff98", relief="solid", borderwidth=1).grid(row=0, column=3)
botonRes = tk.Button(botonera, command=lambda: operar("-"), text="-", width="4", height="4", bg="#98ff98", relief="solid", borderwidth=1).grid(row=1, column=3)
botonMul = tk.Button(botonera, command=lambda: operar("x"), text="x", width="4", height="4", bg="#98ff98", relief="solid", borderwidth=1).grid(row=2, column=3)
botonDiv = tk.Button(botonera, command=lambda: operar("/"), text="/", width="4", height="4", bg="#98ff98", relief="solid", borderwidth=1).grid(row=3, column=3)
botonRes = tk.Button(botonera, command=resolver, text="=", width="4", height="4", bg="grey", relief="solid", borderwidth=1).grid(row=3, column=0)

inicio.mainloop()
