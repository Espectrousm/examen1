import tkinter as tk

def agregar_elemento():
    elemento = int(entry.get())
    if elemento == 0:
        print(arreglo)
    else:
        arreglo.append(elemento)
        entry.delete(0, tk.END)

def buscar_elemento():
    elemento = int(entry_buscar.get())
    if elemento in arreglo:
        resultado_label.config(text="El elemento {} se encuentra en el arreglo.".format(elemento))
        entry_buscar.delete(0, tk.END)
    else:
        resultado_label.config(text="El elemento {} no se encuentra en el arreglo.".format(elemento))
        entry_buscar.delete(0, tk.END)

arreglo = []

ventana = tk.Tk()
ventana.title("Ingreso y búsqueda de elementos")
ventana.geometry("800x400")

# Ingreso de elementos
label = tk.Label(ventana, text="Ingresa un número entero (0 para terminar):")
label.pack()

entry = tk.Entry(ventana)
entry.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack()

# Búsqueda de elementos
label_buscar = tk.Label(ventana, text="Ingresa el número a buscar:")
label_buscar.pack()

entry_buscar = tk.Entry(ventana)
entry_buscar.pack()

boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_elemento)
boton_buscar.pack()

boton_agr = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_agr.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()


ventana.mainloop()

print("Arreglo ingresado:",arreglo)
print("Gracias Por Su Visita")