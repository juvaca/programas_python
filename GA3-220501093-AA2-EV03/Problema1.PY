import tkinter as tk
from tkinter import messagebox

def calcular_tiempo_medio():
    distancia = 42.195
    tiempo_horas = 2
    tiempo_minutos = 25
    
    tiempo_total_minutos = tiempo_horas * 60 + tiempo_minutos
    tiempo_medio = tiempo_total_minutos / distancia
    
    messagebox.showinfo("Resultado", f"El tiempo medio en minutos por kilómetro es: {tiempo_medio}")

root = tk.Tk()
root.title("Tiempo medio en minutos por kilómetro")

btn_calcular = tk.Button(root, text="Calcular tiempo medio", command=calcular_tiempo_medio)
btn_calcular.pack(pady=20)

root.mainloop()
