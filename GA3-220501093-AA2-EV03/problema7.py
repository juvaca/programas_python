import tkinter as tk
from tkinter import messagebox

class ConsumoRestauranteVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Consumo en Restaurante con Descuento")
        
        # Variables para almacenar información
        self.total_pagos = 0.0
        
        # Etiqueta y campo de entrada para consumo del cliente
        self.label = tk.Label(root, text="Ingrese el consumo del cliente en pesos:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # Botón para ingresar consumo
        self.button = tk.Button(root, text="Registrar Consumo", command=self.registrar_consumo)
        self.button.pack(pady=10)
        
        # Etiqueta para mostrar resultados
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        
        # Botón para mostrar el total de pagos
        self.show_total_button = tk.Button(root, text="Mostrar Total de Pagos", command=self.mostrar_total_pagos)
        self.show_total_button.pack(pady=10)
    
    def registrar_consumo(self):
        try:
            consumo_cliente = float(self.entry.get())
            
            # Calcular pago del cliente y aplicar descuento si es necesario
            if consumo_cliente > 50000:
                descuento = consumo_cliente * 0.20
                pago_cliente = consumo_cliente - descuento
                messagebox.showinfo("Descuento Aplicado", f"Descuento del 20% aplicado.\nPago del cliente: {pago_cliente} pesos")
            else:
                pago_cliente = consumo_cliente
                messagebox.showinfo("Pago Realizado", f"Pago del cliente: {pago_cliente} pesos")
            
            self.total_pagos += pago_cliente
            
            # Limpiar campo de entrada
            self.entry.delete(0, tk.END)
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido para el consumo.")
    
    def mostrar_total_pagos(self):
        messagebox.showinfo("Total de Pagos", f"El total de todos los pagos realizados es: {self.total_pagos} pesos")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ConsumoRestauranteVentana(root)
    root.mainloop()
