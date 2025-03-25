#DEPENDENCIAS
import customtkinter as ctk # Importarmos CustomTKinter (Estética)
from customtkinter import *
from PIL import Image
#END DEPENDENCIAS------------------------------------------------------------

#OBJETOS
#Fuente
import EstiloFuente as EF
Default = EF.EstiloFuente() #Fuente por defecto

#Driver Conexión
import Conexion# Conexion a BD

#Imagenes
RT_User = "Assets/Imagenes/User.png"  # Ajusta la ruta de la imagen según tu estructura de carpetas
imagen = ctk.CTkImage(light_image=Image.open(RT_User), 
                      dark_image=Image.open(RT_User), size=(170, 170))  # Usar (light/dark)_image y especificar el tamaño
#END OBJETOS-----------------------------------------------------------------

#FUNCIONES
def acceder():
    resultado = Conexion.conectarse(ETY_Usuario.get(), ETY_Contrasena.get())

    if isinstance(resultado, str):  # Si el resultado es texto, es un mensaje de error
        LBL_Aviso.configure(text=resultado, text_color="red")  # Errores
    else:
        LBL_Aviso.configure(text="Conexión Exitosa.", text_color="green") #OK
        conexion = resultado

#END FUNCIONES---------------------------------------------------------------

#CONTENEDOR
ctk.set_appearance_mode("light")

VentanaSesion = ctk.CTk() #Herencia Apariencia
VentanaSesion.title("Iniciar Sesión - Mila Concept") #Necesito documentar esto?
VentanaSesion.resizable(False,False) #Evitamos que la ventana cresca en ambas direcciones
VentanaSesion.geometry("400x500") #Tamaño del contenedor (ventana)

#END CONTENEDOR--------------------------------------------------------------

#CONTENIDOS==================================================================

#FRAMES----------------------------------------------------------------------
# Frame superior
FRM_Superior = CTkFrame(master=VentanaSesion, corner_radius=0, fg_color=VentanaSesion.cget("fg_color"))
FRM_Superior.pack(side="top", fill="x", padx=0, pady=(10,0))

# Frame central
FRM_Central = CTkFrame(master=VentanaSesion, corner_radius=0,fg_color="pink")
FRM_Central.pack(side="top", fill="both", expand=True, padx=0, pady=10)

# Frame inferior
FRM_Inferior = CTkFrame(master=VentanaSesion, corner_radius=0, fg_color=VentanaSesion.cget("fg_color"))
FRM_Inferior.pack(side="bottom", fill="x", padx=0, pady=(0,10))

#END FRAMES------------------------------------------------------------------
#WIDGETS---------------------------------------------------------------------

#Imagen Usuario
LBL_imagen = ctk.CTkLabel(FRM_Superior, text="", image=imagen)
LBL_imagen.place(relx=0.5, rely= 0.5,
                 anchor= "center")

#Letrero Usuario
LBL_Usuario = CTkLabel(FRM_Central,  #Objeto Contenedor
                       text= "Usuario", 
                       font=Default.font, #Tipo de Fuente
                       text_color= Default.text_color
                       )
LBL_Usuario.place(relx=0.25, rely = 0.15,
                  anchor= "w")

#Entrada Usuario
ETY_Usuario = CTkEntry(FRM_Central, #Objeto Contenedor
                       placeholder_text="", #Texto por Defecto
                       width= 200, #Ancho Objeto
                       border_width= 0, #Eliminamos el borde haciendolo 0 de ancho
                       fg_color= "white",
                       text_color= "black") #Color del Texto
ETY_Usuario.place(relx=0.5, rely = 0.3, #Ubicación 0 a 1
                  anchor = "center") #Alineación

#Letrero Contraseña
LBL_Contrasena = CTkLabel(FRM_Central, 
                       text= "Contraseña",
                       font=Default.font, #Tipo de Fuente
                       text_color= Default.text_color
                       )
LBL_Contrasena.place(relx=0.25, rely = 0.5,
                  anchor= "w")

#Entrada Contraseña
ETY_Contrasena = CTkEntry(FRM_Central, #Objeto Contenedor
                       placeholder_text="", #Texto por Defecto
                       width= 200, #Ancho Objeto
                       border_width= 0, #Eliminamos el borde haciendolo 0 de ancho
                       fg_color= "white",
                       text_color= "black") #Color del Texto
ETY_Contrasena.place(relx=0.5, rely = 0.65, #Ubicación 0 a 1
                  anchor = "center") #Alineación

#Label AVISO
LBL_Aviso = CTkLabel(FRM_Central,
                     text="",
                     text_color=("red"))
LBL_Aviso.place(relx = 0.5, rely = 0.85, #Ubicación 0 a 1
                anchor = "center") #Alineación
#Boton Acceso
BTN_Acceso = CTkButton(FRM_Inferior, #Objeto Contenedor
                       width = 80, #Ancho Objeto
                       font=Default.font, #Tipo de Fuente
                       fg_color="orange",
                       text_color= Default.text_color,
                       text = "Acceder",
                       command=acceder) #Texto del Botón
BTN_Acceso.place(relx = 0.5, rely = 0.5, #Ubicación 0 a 1
                 anchor = "center") #Alineación

#END WIDGETS--------------------------------------------------------
#END CONTENIDOS=====================================================

VentanaSesion.mainloop()#Ejecutar Ventana


