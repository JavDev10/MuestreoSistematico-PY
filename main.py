import customtkinter
import tkinter as tk
import tkinter.ttk as ttk


estilo = ttk.Style()
estilo.configure("EstiloBoton.TButton", font=("Arial", 12), foreground="black", background="blue")

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


#Ingresar datos
etiqueta_poblacion = tk.Label(ventana, text="Población:")
entrada_poblacion = tk.Entry(ventana)

etiqueta_muestra = tk.Label(ventana, text="Muestra:")
entrada_muestra = tk.Entry(ventana)

boton_calcular = ttk.Button(ventana, text="Calcular", style="EstiloBoton.TButton", command=TomaDeDatos)

etiqueta_resultado = tk.Label(ventana, text="")

etiqueta_poblacion.pack()
entrada_poblacion.pack()

etiqueta_muestra.pack()
entrada_muestra.pack()

boton_calcular.pack()

etiqueta_resultado.pack()

ventana.mainloop()




