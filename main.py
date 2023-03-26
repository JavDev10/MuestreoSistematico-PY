import tkinter as tk

ventana = tk.Tk()
ventana.title("Muestreo Sistematico")
ventana.geometry("700x420")

#--------------------------------------------------------------------------------------------------------------------
#Ventana principal
ventana.configure()
tituloPrincipal = tk.Label(ventana, text="Muestreo sistematico",bg="#2e2633",foreground="#fff")
tituloPrincipal.grid(column=0,row=0,columnspan=4)

#--------------------------------------------------------------------------------------------------------------------
#Agregar datos

# Crear la arraylist y la variable que almacena el siguiente ID
arraylist = []
siguiente_id = 1

entrada_poblacion = tk.Label(ventana)
msj_error = tk.Label(ventana)
# Función que se ejecuta cuando se presiona el botón "Agregar"
def agregar_a_lista():
    # Obtener los valores del Textbox
    parametro1 = txtDato.get()
    
    if(len(parametro1)>0):
        # Agregar los valores a la arraylist
        global siguiente_id
        arraylist.append(f"{siguiente_id}. {parametro1}")
        siguiente_id += 1

        poblacion = 0
        poblacion = (len(arraylist))
        
        entrada_poblacion.config(text=poblacion)
        
        # Actualizar la lista de la GUI
        actualizar_lista()
    else:
        msj_error.configure(text="Ingrese datos")

# Función que actualiza la lista en la GUI
def actualizar_lista():
    # Limpiar la lista actual
    lista.delete(0, tk.END)
    txtDato.delete(0, tk.END)
    # Agregar cada elemento de la arraylist
    for i, elemento in enumerate(arraylist):
        lista.insert(tk.END, elemento)

dato = tk.Label(ventana, text="Parámetro:")

txtDato = tk.Entry(ventana)
boton_agregar = tk.Button(ventana, text="Agregar", command= agregar_a_lista)
lista = tk.Listbox(ventana)

dato.grid(column=0,row=1)
txtDato.grid(column=0,row=2)
boton_agregar.grid(column=0,row=3)
msj_error.grid(column=0,row=3)
lista.grid(column=0,row=4,rowspan=2)

#--------------------------------------------------------------------------------------------------------------------
#Ventana constante y arranque
poblacion = len(arraylist)
constante = 0

etiqueta_arranque = tk.Label(ventana,text="Esperando valores")
entrada_arranque = tk.Scale(ventana,from_=1,to=constante,orient="horizontal",cursor="dot")

constanteV = tk.IntVar()

def CalConst_Arranque():   
    muestra = int(entrada_muestra.get())
    poblacion = len(arraylist)
    print(poblacion)
    
    if(int(poblacion)>1 & muestra<int(poblacion)):
        
        #Sacar constante
        constante = int(poblacion)/muestra
        etiqueta_resultado.config(text=f"La constante es: {round(constante)}")

        etiqueta_arranque.configure(text=f"Elija un valor entre 1 y {round(constante)}")
        entrada_arranque.configure(from_=1,to=round(constante),orient="horizontal")

        constanteV.set(round(constante))
    else :
        etiqueta_resultado.config(text=f"Ingrese datos válidos")

seleccionados = []
listaFinal = tk.Listbox(ventana)

def GetArranque():
    ar =entrada_arranque.get()
    listaFinal.delete(0, tk.END)
    
    print(constanteV.get())
    for i in range(ar-1, len(arraylist),constanteV.get()):
        if i < len(arraylist):
            seleccionados.append([arraylist[i]])
    for dato in seleccionados:
        listaFinal.insert(tk.END, dato)
    
#Calcular Constante
etiqueta_poblacion = tk.Label(ventana, text="Población:")

etiqueta_muestra = tk.Label(ventana, text="Muestra:")
entrada_muestra = tk.Entry(ventana)

boton_calcular = tk.Button(ventana, text="Calcular", command=CalConst_Arranque)

etiqueta_resultado = tk.Label(ventana, text="")

etiqueta_poblacion.grid(column=1,row=1)
entrada_poblacion.grid(column=1,row=2)

etiqueta_muestra.grid(column=1,row=3)
entrada_muestra.grid(column=1,row=4)

boton_calcular.grid(column=1,row=5)

etiqueta_resultado.grid(column=1,row=6)
etiqueta_arranque.grid(column=2,row=1)
entrada_arranque.grid(column=2,row=3)
#--------------------------------------------------------------------------------------------------------------------
boton_lista = tk.Button(ventana, text="Generar lista", command=GetArranque)

boton_lista.grid(column=3,row=4)
listaFinal.grid(column=4,row=2)
ventana.mainloop()