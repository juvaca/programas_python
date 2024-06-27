import tkinter as tk
from tkinter import messagebox

class NumerosMenoresVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Números Menores o Iguales a 25")
        
        # Variables para almacenar los números
        self.numeros = []
        self.cantidad_numeros = 20
        self.contador = 0
        
        # Creación de etiquetas y campo de entrada
        self.label = tk.Label(root, text=f"Ingrese el número {self.contador + 1}:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # Botón para ingresar número
        self.button = tk.Button(root, text="Ingresar", command=self.ingresar_numero)
        self.button.pack(pady=10)
        
        # Etiqueta para mostrar los resultados
        self.result_label = tk.Label(root, text="Los números menores o iguales a 25 son:")
        self.result_label.pack(pady=10)
        
        # Frame para mostrar los números
        self.numbers_frame = tk.Frame(root)
        self.numbers_frame.pack(pady=10)
        
        # Botón para mostrar resultados
        self.show_button = tk.Button(root, text="Mostrar Resultados", command=self.mostrar_resultados)
        self.show_button.pack(pady=10)
        
    def ingresar_numero(self):
        try:
            numero = int(self.entry.get())
            self.numeros.append(numero)
            self.contador += 1
            
            if self.contador < self.cantidad_numeros:
                self.label.config(text=f"Ingrese el número {self.contador + 1}:")
                self.entry.delete(0, tk.END)  # Limpiar campo de entrada
            else:
                self.label.config(text="Ingreso completado")
                self.button.config(state=tk.DISABLED)
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")
    
    def mostrar_resultados(self):
        for numero in self.numeros:
            if numero <= 25:
                tk.Label(self.numbers_frame, text=str(numero)).pack()

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = NumerosMenoresVentana(root)
    root.mainloop()
