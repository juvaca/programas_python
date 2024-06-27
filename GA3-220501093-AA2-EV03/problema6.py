import tkinter as tk
from tkinter import messagebox

class SumaPreciosVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Suma de Precios de Camisas")
        
        # Variables para almacenar precios
        self.precio_camisas = []
        self.contador = 0
        
        # Etiqueta y campo de entrada para precios
        self.label = tk.Label(root, text=f"Ingrese el precio de la camisa {self.contador + 1} en dólares:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # Botón para ingresar precio
        self.button = tk.Button(root, text="Ingresar Precio", command=self.ingresar_precio)
        self.button.pack(pady=10)
        
        # Botón para calcular y mostrar el total en pesos
        self.calcular_button = tk.Button(root, text="Calcular Total en Pesos", command=self.calcular_total)
        self.calcular_button.pack(pady=10)
        
        # Etiqueta para mostrar el resultado
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
    
    def ingresar_precio(self):
        try:
            precio = float(self.entry.get())
            self.precio_camisas.append(precio)
            self.contador += 1
            
            if self.contador < 5:
                self.label.config(text=f"Ingrese el precio de la camisa {self.contador + 1} en dólares:")
                self.entry.delete(0, tk.END)  # Limpiar campo de entrada
            else:
                self.label.config(text="Ingreso completado")
                self.button.config(state=tk.DISABLED)
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
    
    def calcular_total(self):
        if len(self.precio_camisas) < 5:
            messagebox.showerror("Error", "Por favor, ingrese todos los precios de las camisas.")
        else:
            CAMBIO_DOLAR_PESO = 3800
            total_venta_pesos = sum(self.precio_camisas) * CAMBIO_DOLAR_PESO
            self.result_label.config(text=f"El total de la venta en pesos Colombianos  es: ${total_venta_pesos} gracias por su compra")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = SumaPreciosVentana(root)
    root.mainloop()
