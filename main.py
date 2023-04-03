import tkinter as tk
from tkinter import ttk
import sv_ttk


ventana = tk.Tk()
ventana.title("CMS")
ventana.resizable(0,0)
ventana.geometry("800x480")

#Estilos
style = ttk.Style()
style.configure("TButton", background="#ff1457", foreground="black", font=("Helvetica", 10))

styleLabelT = ttk.Style()
styleLabelT.configure("T.TLabel", background="#2b2c30", foreground="white", font=("Helvetica", 16, "bold"))
styleLabel1 = ttk.Style()
styleLabel1.configure("TLabel", background="#613c4c", foreground="white", font=("Helvetica", 12))
styleLabel2 = ttk.Style()
styleLabel2.configure("2.TLabel", background="#453745", foreground="white", font=("Helvetica", 12))
styleLabel2 = ttk.Style()
styleLabel2.configure("3.TLabel", background="#35313b", foreground="white", font=("Helvetica", 12))

styleEntry = ttk.Style()
styleEntry.configure("1.TEntry",fg="blue")
#--------------------------------------------------------------------------------------------------------------------
#Ventana principal
ventana.configure()
frameTitulo = tk.Frame(ventana,bg="#2b2c30")
frameDatos = tk.Frame(ventana,bg="#613c4c")
frameConstArr = tk.Frame(ventana,bg="#453745")
frameResult = tk.Frame(ventana,bg="#35313b")
frameMjs = tk.Frame(ventana,bg="#b0254f")

tituloPrincipal = ttk.Label(frameTitulo, text="Muestreo sistematico",style="T.TLabel")
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

entrada_poblacion = ttk.Label(frameConstArr,style="2.TLabel")
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

dato = ttk.Label(frameDatos,text="Parámetro:",style="TLabel")

txtDato = ttk.Entry(frameDatos, justify="center")

txtDato.focus_force()
boton_agregar = ttk.Button(frameDatos, text="Agregar", command= agregar_a_lista,style="TButton")
lista = tk.Listbox(frameDatos)

dato.pack(padx=5,pady=10)
txtDato.pack(padx=5,pady=10,ipadx=32)
boton_agregar.pack(padx=5,pady=10)
lista.pack(padx=5,pady=5,ipady=40,ipadx=32)


#--------------------------------------------------------------------------------------------------------------------
#Ventana constante y arranque
poblacion = len(arraylist)
constante = 0

etiqueta_arranque = ttk.Label(frameConstArr,text="Esperando valores",style="2.TLabel")
entrada_arranque = tk.Scale(frameConstArr,from_=1,to=constante,orient="horizontal",cursor="dot")

constanteV = tk.IntVar()
GenerarLista = tk.BooleanVar()

def CalConst_Arranque():   
    muestra = entrada_muestra.get()
    poblacion = int(len(arraylist))
    
    if(poblacion <= 0):
        msj_error.configure(text="El número de la poblacion es 0")
    else :
        if(int(muestra)<poblacion):
            #Sacar constante
            constante = poblacion/int(muestra)
            etiqueta_resultado.config(text=f"La constante es: {round(constante)}")

            etiqueta_arranque.configure(text=f"Elija un valor entre 1 y {round(constante)}")
            entrada_arranque.configure(from_=1,to=round(constante),orient="horizontal")
            constanteV.set(round(constante))
            GenerarLista.set(True)
        elif (int(muestra)>=poblacion) :
            msj_error.configure(text="La muestra no puede ser mayor o igual a la poblacion")

seleccionados = []
lbl_listaFinal = ttk.Label(frameResult,text="Listado",style="3.TLabel")
listaFinal = tk.Listbox(frameResult)

def GetArranque():
    ar =entrada_arranque.get()
    listaFinal.delete(0, tk.END)

    if(GenerarLista.get()==True):
        msj_error.configure(text="Lista generada!")
        for i in range(ar-1, len(arraylist),constanteV.get()):
            if i < len(arraylist):
                seleccionados.append(arraylist[i])
        for dato in seleccionados:
            listaFinal.insert(tk.END, dato)
    else:
        msj_error.configure(text="Faltan datos para generar lista")
#Calcular Constante
etiqueta_poblacion = ttk.Label(frameConstArr, text="Población:",style="2.TLabel")

etiqueta_muestra = ttk.Label(frameConstArr, text="Muestra:",style="2.TLabel")
entrada_muestra = ttk.Entry(frameConstArr,justify="center")

boton_calcular = ttk.Button(frameConstArr, text="Calcular", command=CalConst_Arranque,style="TButton")

etiqueta_resultado = ttk.Label(frameConstArr, text="",style="2.TLabel")

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
    #Eliminar datos en lista y reinicio de id
    arraylist.clear()
    seleccionados.clear()
    global siguiente_id
    siguiente_id = 1

    #Eliminar datos en pantalla
    lista.delete(0,tk.END)
    listaFinal.delete(0,tk.END)

    msj_error.configure(text="Listas borradas")

boton_CleanList = ttk.Button(frameResult, text="Limpiar listas", command=LimpiarListas, style="TButton")

lbl_listaFinal.pack(padx=5,pady=10)
listaFinal.pack(padx=5,pady=15,ipady=50,ipadx=32)
boton_CleanList.pack()
msj_error.pack(padx=5,pady=5)
ventana.mainloop()