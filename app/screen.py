# Import libraries and modules / Importar librerias y modulos.
import os
import sys
import tkinter as tk
from app.test import pd_test

# This class redirects the standard output to a text widget of the tkinter library / Esta clase para redirigir la salida estándar hacia un widget de texto de la biblioteca tkinter.
class StdOutRedirect:
    def __init__(self,  text: tk.Text) -> None:
        self._text = text

    def write(self,  out: str) -> None:
        self._text.insert(tk.END,  out)

# This class create a GUI / Esta clase crea una GUI:
class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent,  *args, **kwargs)
        self.stdout_text = tk.Text(
            self,  bg="#000000",  fg="#149414",  font=("Helvetica", 15), padx=40, pady=10 )
        self.stdout_text.pack(expand=True, fill=tk.BOTH)
        sys.stdout = StdOutRedirect(self.stdout_text)

# Function to clear the console / Funcion para limpiar consola
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funtion to execute an App isntance to print the test / Funcion que crea una isntnacia de App para imprimir la prueba.
def tk_console():
    # If console is shown, clear all before / De mostrase la consola, borra todo lo anterior impreso.
    clear_screen()
    # Setting root
    root = tk.Tk()
    # Name / Nombre.
    root.title("Probando la libreria pandas.")
    # Logo
    root.iconbitmap("pd.ico") 

    # Get screen size of the user / Obtener tamaño de la pantalla del usuario.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size to the size of the screen / Establecer el tamaño de la ventana al tamaño de la pantalla.
    root.geometry(f"{screen_width}x{screen_height}")  

    # Set the window's geometry to center it / Establecer la geometría de la ventana para centrarla.
    root.geometry(f"+{-8}+{0}")

    # App instance
    App(root).pack(expand=True, fill=tk.BOTH)

    # Printable thanks to App instance
    pd_test()
    # Infinite screen loop
    root.mainloop()

# Powered by Cesar Albornoz - All right reserved.