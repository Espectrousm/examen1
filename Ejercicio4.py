import tkinter as tk

def agregar_elemento():
    elemento = int(entry.get())
    if elemento == 0:
        ordenBurbuja(arreglo)
        print(arreglo)
        entry.delete(0, tk.END)
    else:
        arreglo.append(elemento)
        entry.delete(0, tk.END)
        
        
def ordenBurbuja(lista):
    n = len(lista)
    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

            
def sacarmayor():
    mayorsacado = max(arreglo)
    resultado_label.config(text="El Valor Maximo de la lista es:.{}".format(mayorsacado))
    
def sacarmenor():
    menorsacado = min(arreglo)
    resultado_label.config(text="El Valor Maximo de la lista es:.{}".format(menorsacado))
 
def tamañoarreglo():
    resultado_label.config(text="El tamaño del arreglo es:.{}".format(len(arreglo)))
    


        
arreglo = []

ventana = tk.Tk()
ventana.title("Ingreso y búsqueda de elementos")
ventana.geometry("800x400")

# Ingreso de elementos
label = tk.Label(ventana, text="Ingrese numeros enteros de forma desordenada  (0 para terminar):")
label.pack()

entry = tk.Entry(ventana)
entry.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack()

label2 = tk.Label(ventana, text="Advertencia, Debe de ingresarlos de forma desordenada y terminar en 0 para usar las demas funciones:")
label2.pack()


boton_agrega = tk.Button(ventana, text="tamaño de arreglo", command=tamañoarreglo)
boton_agrega.pack()

boton_agreg = tk.Button(ventana, text="Mayor Numero", command=sacarmayor)
boton_agreg.pack()

boton_agre = tk.Button(ventana, text="Menor Numero", command=sacarmenor)
boton_agre.pack()

boton_agr = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_agr.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

print("Arreglo ingresado:",arreglo)

ventana.mainloop()

print("Gracias Por Su Visita")

