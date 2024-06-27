import tkinter as tk
from tkinter import messagebox

class ProductoNumerosVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Producto desde 1 hasta N")
        
        # Etiqueta y entrada para ingresar N
        self.label = tk.Label(root, text="Ingrese un número N:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # Botón para calcular el producto
        self.button = tk.Button(root, text="Calcular Producto", command=self.calcular_producto)
        self.button.pack(pady=10)
        
        # Etiqueta para mostrar el resultado
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
    
    def calcular_producto(self):
        try:
            # Obtener el valor de N desde la entrada
            N = int(self.entry.get())
            
            # Validar que N sea un entero positivo
            if N <= 0:
                messagebox.showerror("Error", "N debe ser un número entero positivo.")
                return
            
            # Calcular el producto de todos los números desde 1 hasta N
            producto = 1
            for i in range(1, N + 1):
                producto *= i
            
            # Mostrar el resultado del producto
            self.result_label.config(text=f"El producto de todos los números desde 1 hasta {N} es: {producto}")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")

# Función principal para inicializar la interfaz gráfica
def main():
    root = tk.Tk()
    app = ProductoNumerosVentana(root)
    root.mainloop()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
