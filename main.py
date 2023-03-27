import tkinter as tk
from tkinter import ttk
import sv_ttk


ventana = tk.Tk()
ventana.title("Muestreo Sistematico")
ventana.geometry("800x480")

#Estilos
style = ttk.Style()
style.configure("TButton", background="#ff1457", foreground="black", font=("Helvetica", 10))

#--------------------------------------------------------------------------------------------------------------------
#Ventana principal
ventana.configure()
frameTitulo = tk.Frame(ventana,bg="#2b2c30")
frameDatos = tk.Frame(ventana,bg="#613c4c")
frameConstArr = tk.Frame(ventana,bg="#453745")
frameResult = tk.Frame(ventana,bg="#35313b")
frameMjs = tk.Frame(ventana,bg="#b0254f")

tituloPrincipal = tk.Label(frameTitulo, text="Muestreo sistematico",bg="#2b2c30",foreground="#fff")
tituloPrincipal.pack(padx=5,pady=5)

frameTitulo.pack(side="top",expand=False,fill="both",ipady=10)
frameMjs.pack(side="bottom",expand=False,fill="both")
frameDatos.pack(side="left",expand=True,fill="both")
frameConstArr.pack(side="left",expand=True,fill="both")
frameResult.pack(side="left",expand=True,fill="both")


#--------------------------------------------------------------------------------------------------------------------
#Agregar datos

# Crear la arraylist y la variable que almacena el siguiente ID
arraylist = []
siguiente_id = 1

entrada_poblacion = tk.Label(frameConstArr)
msj_error = tk.Label(frameMjs)
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

dato = tk.Label(frameDatos, text="Parámetro:")

txtDato = tk.Entry(frameDatos)
boton_agregar = ttk.Button(frameDatos, text="Agregar", command= agregar_a_lista,style="TButton")
lista = tk.Listbox(frameDatos)

dato.pack(padx=5,pady=10)
txtDato.pack(padx=5,pady=10,ipadx=32)
boton_agregar.pack(padx=5,pady=10)
lista.pack(padx=5,pady=5,ipady=40,ipadx=32)
msj_error.pack(padx=5,pady=5)

#--------------------------------------------------------------------------------------------------------------------
#Ventana constante y arranque
poblacion = len(arraylist)
constante = 0

etiqueta_arranque = tk.Label(frameConstArr,text="Esperando valores")
entrada_arranque = tk.Scale(frameConstArr,from_=1,to=constante,orient="horizontal",cursor="dot")

constanteV = tk.IntVar()

def CalConst_Arranque():   
    muestra = int(entrada_muestra.get())
    poblacion = len(arraylist)
    
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
lbl_listaFinal = tk.Label(frameResult,text="Listado")
listaFinal = tk.Listbox(frameResult)

def GetArranque():
    ar =entrada_arranque.get()
    listaFinal.delete(0, tk.END)

    for i in range(ar-1, len(arraylist),constanteV.get()):
        if i < len(arraylist):
            seleccionados.append([arraylist[i]])
    for dato in seleccionados:
        listaFinal.insert(tk.END, dato)
    
#Calcular Constante
etiqueta_poblacion = tk.Label(frameConstArr, text="Población:")

etiqueta_muestra = tk.Label(frameConstArr, text="Muestra:")
entrada_muestra = tk.Entry(frameConstArr)

boton_calcular = ttk.Button(frameConstArr, text="Calcular", command=CalConst_Arranque,style="TButton")

etiqueta_resultado = tk.Label(frameConstArr, text="")

etiqueta_poblacion.pack(padx=5,pady=5)
entrada_poblacion.pack(padx=5,pady=10)

etiqueta_muestra.pack(padx=5,pady=5)
entrada_muestra.pack(padx=5,pady=10)

boton_calcular.pack(padx=5,pady=10)

etiqueta_resultado.pack(padx=5,pady=5)
etiqueta_arranque.pack(padx=5,pady=10)
entrada_arranque.pack(padx=5,pady=10)
#--------------------------------------------------------------------------------------------------------------------
boton_lista = ttk.Button(frameConstArr, text="Generar lista", command=GetArranque,style="TButton")
boton_lista.pack(padx=5,pady=5)
def LimpiarListas():
    lista.delete(0,tk.END)
    listaFinal.delete(0,tk.END)

boton_CleanList = ttk.Button(frameResult, text="Limpiar listas", command=LimpiarListas, style="TButton")

lbl_listaFinal.pack(padx=5,pady=10)
listaFinal.pack(padx=5,pady=15,ipady=50,ipadx=32)
boton_CleanList.pack()
ventana.mainloop()