#DEPENDENCIAS
import customtkinter as ctk # Importarmos CustomTKinter (Estética)
from customtkinter import *
from PIL import Image
#END DEPENDENCIAS-------------------------------------------

#OBJETOS
#Fuente
import EstiloFuente as EF
Default = EF.EstiloFuente() #Fuente por defecto

import Conexion# Conexion a BD

#Imagenes
RT_User = "Assets/Imagenes/User.png"  # Ajusta la ruta de la imagen según tu estructura de carpetas
imagen = ctk.CTkImage(light_image=Image.open(RT_User), 
                      dark_image=Image.open(RT_User), size=(170, 170))  # Usar (light/dark)_image y especificar el tamaño
#END OBJETOS-------------------------------------------------

#FUNCIONES
def acceder():
    Conexion.conectarse(ETY_Usuario.get, ETY_Contrasena.get())

#END FUNCIONES-----------------------------------------------

#CONTENEDOR
VentanaSesion = ctk.CTk() #Herencia Apariencia
VentanaSesion.title("Iniciar Sesión - Mila Concept") #Necesito documentar esto?
VentanaSesion.resizable(False, False) #Evitamos que la ventana cresca en ambas direcciones
VentanaSesion.geometry("400x500") #Tamaño del contenedor (ventana)
VentanaSesion.configure(fg_color="pink")

#CONTENIDO


#Imagen Usuario
LBL_imagen = ctk.CTkLabel(master= VentanaSesion, text="", image=imagen)
LBL_imagen.place(relx=0.5, rely= 0.3,
                 anchor= "center")

#Letrero Usuario
LBL_Usuario = CTkLabel(master= VentanaSesion,  #Objeto Contenedor
                       text= "Usuario", 
                       font=Default.font, #Tipo de Fuente
                       text_color= Default.text_color
                       )
LBL_Usuario.place(relx=0.25, rely = 0.55,
                  anchor= "w")

#Entrada Usuario
ETY_Usuario = CTkEntry(master = VentanaSesion, #Objeto Contenedor
                       placeholder_text="", #Texto por Defecto
                       width= 200, #Ancho Objeto
                       border_width= 0, #Eliminamos el borde haciendolo 0 de ancho
                       fg_color= "white",
                       text_color= "black") #Color del Texto
ETY_Usuario.place(relx=0.5, rely = 0.6, #Ubicación 0 a 1
                  anchor = "center") #Alineación

#Letrero Contraseña
LBL_Contrasena = CTkLabel(master= VentanaSesion, 
                       text= "Contraseña",
                       font=Default.font, #Tipo de Fuente
                       text_color= Default.text_color
                       )
LBL_Contrasena.place(relx=0.25, rely = 0.67,
                  anchor= "w")

#Entrada Contraseña
ETY_Contrasena = CTkEntry(master = VentanaSesion, #Objeto Contenedor
                       placeholder_text="", #Texto por Defecto
                       width= 200, #Ancho Objeto
                       border_width= 0, #Eliminamos el borde haciendolo 0 de ancho
                       fg_color= "white",
                       text_color= "black") #Color del Texto
ETY_Contrasena.place(relx=0.5, rely = 0.72, #Ubicación 0 a 1
                  anchor = "center") #Alineación

#Label AVISO
LBL_Aviso = CTkLabel(master= VentanaSesion,
                     text="",
                     text_color=("red"))
LBL_Aviso.place(relx = 0.5, rely = 0.8, #Ubicación 0 a 1
                anchor = "center") #Alineación
#Boton Acceso
BTN_Acceso = CTkButton(master = VentanaSesion, #Objeto Contenedor
                       width = 80, #Ancho Objeto
                       font=Default.font, #Tipo de Fuente
                       fg_color="orange",
                       text_color= Default.text_color,
                       text = "Acceder",
                       command=acceder) #Texto del Botón
BTN_Acceso.place(relx = 0.5, rely = 0.87, #Ubicación 0 a 1
                 anchor = "center") #Alineación

#--------------------------------------------------------
VentanaSesion.mainloop()#Ejecutar Ventana


