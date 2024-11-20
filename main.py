import tkinter as tk
from tkinter import messagebox, filedialog
from conexion import conectar_bd
from crud import crear_encuesta, leer_encuestas, actualizar_encuesta, eliminar_encuesta, exportar_a_excel
import matplotlib.pyplot as plt
import pandas as pd

def mostrar_encuestas():
    resultados_box.delete(0, tk.END)
    encuestas = leer_encuestas(connection)
    for encuesta in encuestas:
        resultados_box.insert(tk.END, encuesta)

def agregar_encuesta():
    try:
        # Recoger datos del formulario
        crear_encuesta(connection, 
                       int(edad_entry.get()), 
                       sexo_entry.get(),
                       int(bebidas_entry.get()), 
                       int(cervezas_entry.get()), 
                       int(fin_semana_entry.get()), 
                       int(destiladas_entry.get()),
                       int(vinos_entry.get()), 
                       int(perdidas_entry.get()), 
                       depende_entry.get(),
                       digestivos_entry.get(), 
                       tension_entry.get(), 
                       cabeza_entry.get())
        mostrar_encuestas()
        messagebox.showinfo("Éxito", "Encuesta agregada correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo agregar la encuesta: {e}")

def eliminar_encuesta_ui():
    try:
        eliminar_encuesta(connection, int(id_encuesta_entry.get()))
        mostrar_encuestas()
        messagebox.showinfo("Éxito", "Encuesta eliminada correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar la encuesta: {e}")

def exportar_excel_ui():
    archivo = filedialog.asksaveasfilename(defaultextension=".xlsx")
    exportar_a_excel(connection, archivo)
    messagebox.showinfo("Exportación completada", f"Datos exportados a {archivo}")

def graficar():
    encuestas = leer_encuestas(connection)
    df = pd.DataFrame(encuestas, columns=["ID", "Edad", "Sexo", "Bebidas", "Cervezas", "Fin de semana", "Destiladas", 
                                          "Vinos", "Control", "Dependencia", "Digestivos", "Tensión", "Cabeza"])
    df.groupby('Edad')['Bebidas'].mean().plot(kind="bar")
    plt.xlabel("Edad")
    plt.ylabel("Consumo promedio")
    plt.title("Consumo promedio por grupo de edad")
    plt.show()

connection = conectar_bd()

ventana = tk.Tk()
ventana.title("Sistema de Encuestas")
ventana.geometry("600x600")

# Campos de entrada
tk.Label(ventana, text="ID Encuesta").grid(row=0, column=0)
id_encuesta_entry = tk.Entry(ventana)
id_encuesta_entry.grid(row=0, column=1)

tk.Label(ventana, text="Edad").grid(row=1, column=0)
edad_entry = tk.Entry(ventana)
edad_entry.grid(row=1, column=1)

tk.Label(ventana, text="Sexo").grid(row=2, column=0)
sexo_entry = tk.Entry(ventana)
sexo_entry.grid(row=2, column=1)

tk.Label(ventana, text="Bebidas/Semana").grid(row=3, column=0)
bebidas_entry = tk.Entry(ventana)
bebidas_entry.grid(row=3, column=1)

tk.Label(ventana, text="Cervezas/Semana").grid(row=4, column=0)
cervezas_entry = tk.Entry(ventana)
cervezas_entry.grid(row=4, column=1)

tk.Label(ventana, text="Bebidas Fin de Semana").grid(row=5, column=0)
fin_semana_entry = tk.Entry(ventana)
fin_semana_entry.grid(row=5, column=1)

tk.Label(ventana, text="Bebidas Destiladas/Semana").grid(row=6, column=0)
destiladas_entry = tk.Entry(ventana)
destiladas_entry.grid(row=6, column=1)

tk.Label(ventana, text="Vinos/Semana").grid(row=7, column=0)
vinos_entry = tk.Entry(ventana)
vinos_entry.grid(row=7, column=1)

tk.Label(ventana, text="Pérdidas de Control").grid(row=8, column=0)
perdidas_entry = tk.Entry(ventana)
perdidas_entry.grid(row=8, column=1)

tk.Label(ventana, text="Dependencia de Alcohol").grid(row=9, column=0)
depende_entry = tk.Entry(ventana)
depende_entry.grid(row=9, column=1)

tk.Label(ventana, text="Problemas Digestivos").grid(row=10, column=0)
digestivos_entry = tk.Entry(ventana)
digestivos_entry.grid(row=10, column=1)

tk.Label(ventana, text="Tensión Alta").grid(row=11, column=0)
tension_entry = tk.Entry(ventana)
tension_entry.grid(row=11, column=1)

tk.Label(ventana, text="Dolor de Cabeza").grid(row=12, column=0)
cabeza_entry = tk.Entry(ventana)
cabeza_entry.grid(row=12, column=1)

# Lista para mostrar resultados
resultados_box = tk.Listbox(ventana, width=80)
resultados_box.grid(row=15, column=0, columnspan=3)

# Botones
tk.Button(ventana, text="Agregar Encuesta", command=agregar_encuesta).grid(row=14, column=0)
tk.Button(ventana, text="Eliminar Encuesta", command=eliminar_encuesta_ui).grid(row=14, column=1)
tk.Button(ventana, text="Mostrar Encuestas", command=mostrar_encuestas).grid(row=14, column=2)
tk.Button(ventana, text="Exportar a Excel", command=exportar_excel_ui).grid(row=16, column=0)
tk.Button(ventana, text="Graficar", command=graficar).grid(row=16, column=1)

ventana.mainloop()
