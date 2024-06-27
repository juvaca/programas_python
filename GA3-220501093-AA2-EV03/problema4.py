import tkinter as tk
from tkinter import messagebox

class DuplicarCapitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcular Años para Duplicar Capital")
        
        # Variables para almacenar el capital inicial y la tasa de interés anual
        self.capital_inicial = tk.DoubleVar()
        self.tasa_interes_anual = tk.DoubleVar()
        
        # Creación de etiquetas y campos de entrada
        tk.Label(root, text="Capital Inicial:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.capital_inicial).grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Tasa de Interés Anual (%):").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.tasa_interes_anual).grid(row=1, column=1, padx=10, pady=5)
        
        # Botón para calcular años para duplicar el capital
        tk.Button(root, text="Calcular Años", command=self.calcular_años_duplicar).grid(row=2, columnspan=2, padx=10, pady=10)
        
        # Etiqueta para mostrar el resultado
        self.resultado_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.resultado_label.grid(row=3, columnspan=2, padx=10, pady=10)
    
    def calcular_años_duplicar(self):
        try:
            # Obtener los valores ingresados por el usuario
            capital_inicial = self.capital_inicial.get()
            tasa_interes_anual = self.tasa_interes_anual.get()
            
            # Validar que los valores sean positivos
            if capital_inicial <= 0 or tasa_interes_anual <= 0:
                messagebox.showerror("Error", "Por favor, ingrese valores positivos para el capital inicial y la tasa de interés.")
                return
            
            # Inicialización de variables
            capital = capital_inicial
            años = 0
            
            # Calcular años para duplicar el capital
            while capital < capital_inicial * 2:
                capital *= (1 + tasa_interes_anual / 100)
                años += 1
            
            # Mostrar el resultado
            self.resultado_label.config(text=f"El capital se duplicará en {años} años")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el capital inicial y la tasa de interés.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {str(e)}")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = DuplicarCapitalApp(root)
    root.mainloop()
