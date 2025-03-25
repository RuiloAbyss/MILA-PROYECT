#DEPENDENCIAS
import customtkinter as ctk # Importarmos CustomTKinter (Estética)
from customtkinter import *

#END DEPENDENCIAS-------------------------------------------

#CONTENEDOR
VentanaSesion = ctk.CTk() #Herencia Apariencia
VentanaSesion.title("Mila") #Necesito documentar esto?
VentanaSesion.geometry("500x400")

#CONTENIDO
#Entrada Usuario
ETY_Usuario = CTkEntry(master = VentanaSesion, #Objeto Contenedor
                       placeholder_text="", #Texto por Defecto
                       width= 200, #Ancho Objeto
                       text_color= "000000") #Color del Texto
ETY_Usuario.place(relx=0.5, rely = 0.2, #Ubicación 0 a 1
                  anchor = "center") #Alineación

#Entrada Contraseña


#Boton Acceso
BTN_Acceso = CTkButton(master = VentanaSesion, #Objeto Contenedor
                       text = "Acceder") #Texto del Botón
BTN_Acceso.place(relx = 0.5, rely = 0.5, #Ubicación 0 a 1
                 anchor = "center") #Alineación
#CONFIGURACION DEL TEMA

#--------------------------------------------------------
VentanaSesion.mainloop()#Ejecutar Ventana


