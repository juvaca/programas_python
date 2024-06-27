import tkinter as tk

def convertir_a_fahrenheit():
    celsius = float(entry_celsius.get())
    fahrenheit = (9 / 5) * celsius + 32
    resultado_label.config(text=f"Grados Fahrenheit: {fahrenheit:.2f}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Conversión de Celsius a Fahrenheit")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Grados Celsius:").grid(row=0, column=0)
entry_celsius = tk.Entry(frame)
entry_celsius.grid(row=0, column=1)

convertir_button = tk.Button(frame, text="Convertir", command=convertir_a_fahrenheit)
convertir_button.grid(row=1, columnspan=2, pady=10)

resultado_label = tk.Label(frame, text="")
resultado_label.grid(row=2, columnspan=2)

root.mainloop()
