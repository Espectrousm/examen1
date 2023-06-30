import tkinter as tk
import statistics



def agregar_elemento():
    elemento = int(entry.get())
    if elemento == 0:
        ordenPorSeleccion(arreglo)
        print(arreglo)
        entry.delete(0, tk.END)
    else:
        arreglo.append(elemento)
        entry.delete(0, tk.END)
        
def ordenPorSeleccion(lista):
    tamaño=len(lista)
    tamaños = tamaño
    for i in range(0,tamaño):
        min=i
        for j in range(i+1,tamaño):
            if lista[min]<lista[j]:
                min=j
        aux=lista[i]
        lista[i]=lista[min]
        lista[min]=aux
    return lista

def tamañoarreglo():
    resultado_label.config(text="El tamaño del arreglo es:{}".format(len(arreglo)))
    

def promedioelementos():
    promedi = statistics.mean(arreglo)
    resultado_label.config(text="El Promedio de los elementos de la lista es:{}".format(promedi))

def sumaelementos():
    sumato = sum(arreglo)
    resultado_label.config(text="La suma de los elementos de la lista es:{}".format(sumato))
    
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

label2 = tk.Label(ventana, text="Advertencia, Es necesario terminar en 0 para usar Funciones,Tamaño , Suma ,Promedio:")
label2.pack()

boton_agreg = tk.Button(ventana, text="Suma Elementos", command=sumaelementos)
boton_agreg.pack()

boton_agre = tk.Button(ventana, text="Promedio Elementos", command=promedioelementos)
boton_agre.pack()

boton_agre = tk.Button(ventana, text="Tamaño del arreglo", command=tamañoarreglo)
boton_agre.pack()

boton_agr = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_agr.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()



ventana.mainloop()


print (arreglo)

print("Arreglo ingresado:",arreglo)
print("Gracias Por Su Visita")


