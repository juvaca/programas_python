import tkinter as tk
from tkinter import messagebox

class TablaMultiplicarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla de Multiplicar Decreciente")
        
        # Etiqueta y entrada para el número
        self.label = tk.Label(root, text="Ingrese un número para generar su tabla de multiplicar:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # Botón para generar la tabla
        self.button = tk.Button(root, text="Generar Tabla", command=self.generar_tabla)
        self.button.pack(pady=10)
        
        # Área de texto para mostrar la tabla de multiplicar
        self.text_area = tk.Text(root, height=15, width=30)
        self.text_area.pack(pady=10)
        
    def generar_tabla(self):
        try:
            numero = int(self.entry.get())
            if numero <= 0:
                messagebox.showerror("Error", "El número debe ser un entero positivo.")
                return
            
            self.text_area.delete(1.0, tk.END)  # Limpiar el área de texto
            self.text_area.insert(tk.END, f"Tabla de multiplicar decreciente del número {numero}:\n")
            
            for i in range(10, 0, -1):
                resultado = numero * i
                self.text_area.insert(tk.END, f"{numero} x {i} = {resultado}\n")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TablaMultiplicarApp(root)
    root.mainloop()
