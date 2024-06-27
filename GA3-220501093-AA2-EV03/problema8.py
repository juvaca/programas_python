import tkinter as tk
from tkinter import messagebox

class CalcularHoraSiguiente(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calcular Hora en el Siguiente Segundo")

        # Variables para almacenar la hora
        self.hora = tk.IntVar()
        self.minutos = tk.IntVar()
        self.segundos = tk.IntVar()

        # Crear etiquetas y campos de entrada
        tk.Label(self, text="Hora:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_hora = tk.Entry(self, textvariable=self.hora)
        self.entry_hora.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Minutos:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_minutos = tk.Entry(self, textvariable=self.minutos)
        self.entry_minutos.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Segundos:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_segundos = tk.Entry(self, textvariable=self.segundos)
        self.entry_segundos.grid(row=2, column=1, padx=10, pady=10)

        # Botón para calcular la hora siguiente
        self.button_calcular = tk.Button(self, text="Calcular Hora Siguiente", command=self.calcular_hora_siguiente)
        self.button_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Etiqueta para mostrar el resultado
        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def calcular_hora_siguiente(self):
        try:
            # Obtener los valores ingresados por el usuario
            hora = self.hora.get()
            minutos = self.minutos.get()
            segundos = self.segundos.get()

            # Verificar si los segundos están en rango válido (0 a 59)
            if segundos >= 0 and segundos < 59:
                segundos += 1
            elif segundos == 59:
                segundos = 0
                minutos += 1
                if minutos == 60:
                    minutos = 0
                    hora += 1
                    if hora == 24:
                        hora = 0

            # Determinar si es AM o PM
            periodo = "AM"
            if hora >= 12:
                periodo = "PM"
                if hora > 12:
                    hora -= 12

            # Mostrar la nueva hora calculada
            self.label_resultado.config(text=f"La hora un segundo después es: {hora}:{minutos:02}:{segundos:02} {periodo}")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para la hora, minutos y segundos.")

if __name__ == "__main__":
    app = CalcularHoraSiguiente()
    app.mainloop()
