import tkinter as tk
from tkinter import messagebox

class CalcularNotaPrimerParcialApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcular Nota Primer Parcial")
        
        # Definición de constantes
        self.PESO_TALLERES = 0.1
        self.PESO_QUIZ = 0.2
        self.PESO_PARCIAL = 0.7
        
        # Variables para almacenar las notas
        self.nota_taller1 = tk.DoubleVar()
        self.nota_taller2 = tk.DoubleVar()
        self.nota_quiz = tk.DoubleVar()
        self.nota_examen_parcial = tk.DoubleVar()
        
        # Creación de etiquetas y campos de entrada
        tk.Label(root, text="Nota Taller 1:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.nota_taller1).grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Nota Taller 2:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.nota_taller2).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Nota Quiz:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.nota_quiz).grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Nota Examen Parcial:").grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.nota_examen_parcial).grid(row=3, column=1, padx=10, pady=5)
        
        # Botón para calcular la nota final
        tk.Button(root, text="Calcular Nota Final", command=self.calcular_nota_final).grid(row=4, columnspan=2, padx=10, pady=10)
        
        # Etiqueta para mostrar el resultado
        self.resultado_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.resultado_label.grid(row=5, columnspan=2, padx=10, pady=10)
    
    def calcular_nota_final(self):
        # Obtener las notas ingresadas por el usuario
        try:
            nota_taller1 = self.nota_taller1.get()
            nota_taller2 = self.nota_taller2.get()
            nota_quiz = self.nota_quiz.get()
            nota_examen_parcial = self.nota_examen_parcial.get()
            
            # Calcular promedio de talleres y quiz
            promedio_talleres_quiz = (nota_taller1 + nota_taller2 + nota_quiz) / 3
            
            # Calcular nota final del primer parcial
            nota_primer_parcial = promedio_talleres_quiz * (self.PESO_TALLERES + self.PESO_QUIZ) + nota_examen_parcial * self.PESO_PARCIAL
            
            # Mostrar el resultado
            self.resultado_label.config(text=f"Nota Final del Primer Parcial: {nota_primer_parcial:.2f}")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para las notas.")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = CalcularNotaPrimerParcialApp(root)
    root.mainloop()
