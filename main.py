import customtkinter
import tkinter as tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Tomar info 
def TomaDeDatos():
    poblacion = int(entrada_poblacion.get())
    muestra = int(entrada_muestra.get())

    if(poblacion>1 & muestra<poblacion):
        
        #Sacar constante
        constante = poblacion/muestra
        etiqueta_resultado.config(text=f"La constante es: {constante}")

        #Elegir valor arranque
        print("Elija un valor entre 1 y",constante,":")
        valor_arranque= input()
        
        if(int(valor_arranque) > 1 & int(valor_arranque) < int(constante)):
            print("Valor de arranque:",valor_arranque)
        else:
            print("Se tiene que ingresar un un valor entre 1 y",constante)
    else :
         etiqueta_resultado.config(text=f"Ingrese datos válidos")

ventana = tk.Tk()
ventana.geometry("500x350")

titulo = tk.Label(ventana, text="Muestreo Sistemático",bg="#3f324d",foreground="#fff")

#Ingresar datos
etiqueta_poblacion = tk.Label(ventana, text="Población:")
entrada_poblacion = tk.Entry(ventana)

etiqueta_muestra = tk.Label(ventana, text="Muestra:")
entrada_muestra = tk.Entry(ventana)

boton_calcular = tk.Button(ventana, text="Calcular", command=TomaDeDatos)

etiqueta_resultado = tk.Label(ventana, text="")

#Mostrar en pantalla
titulo.pack(side=tk.TOP, fill = tk.X)
etiqueta_poblacion.pack(side= tk.LEFT)
entrada_poblacion.pack(side= tk.LEFT)

etiqueta_muestra.pack(side= tk.LEFT)
entrada_muestra.pack(side= tk.LEFT)

boton_calcular.pack(side= tk.BOTTOM)

etiqueta_resultado.pack(side= tk.BOTTOM)

ventana.mainloop()




