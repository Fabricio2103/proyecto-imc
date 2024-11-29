import tkinter as tk
from tkinter import messagebox, ttk
from funciones import calcular_imc, clasificar_imc, guardar_en_excel

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Aplicación de Índice de Masa Corporal')
ventana.geometry("400x500")
ventana.configure(bg="#f0f0f0")

# Variables
genero_var = tk.StringVar()
peso_var = tk.DoubleVar()
altura_var = tk.DoubleVar()
nombre_var = tk.StringVar()
edad_var = tk.IntVar()
actividad_var = tk.StringVar()

# Pantallas
pantalla_inicio = tk.Frame(ventana, bg="#f0f0f0")
pantalla_genero = tk.Frame(ventana, bg="#f0f0f0")
pantalla_datos_personales = tk.Frame(ventana, bg="#f0f0f0")
pantalla_resultados = tk.Frame(ventana, bg="#f0f0f0")

# Funciones para manejar pantallas
def mostrar_inicio():
    pantalla_inicio.pack(fill="both", expand=True)
    pantalla_genero.pack_forget()
    pantalla_datos_personales.pack_forget()
    pantalla_resultados.pack_forget()

def mostrar_genero():
    pantalla_genero.pack(fill="both", expand=True)
    pantalla_inicio.pack_forget()

def mostrar_datos_personales():
    if not genero_var.get():
        messagebox.showerror("Error", "Debes seleccionar un género.")
        return
    pantalla_genero.pack_forget()
    pantalla_datos_personales.pack(fill="both", expand=True)

def mostrar_resultados():
    try:
        # Validar entradas
        nombre = nombre_var.get().strip()
        edad = edad_var.get()
        peso = peso_var.get()
        altura = altura_var.get()

        if not nombre or edad <= 0 or peso <= 0 or altura <= 0:
            messagebox.showerror("Error", "Todos los campos deben ser completados correctamente.")
            return

        altura_m = altura / 100  # Convertir cm a metros
        imc = calcular_imc(peso, altura_m)
        clasificacion = clasificar_imc(imc)

        datos = {
            'nombre': nombre,
            'edad': edad,
            'genero': genero_var.get(),
            'actividad': actividad_var.get(),
            'peso': peso,
            'altura': altura,
            'imc': imc,
            'clasificacion': clasificacion
        }

        guardar_en_excel(datos)

        # Mostrar resultados
        label_resultado.config(text=f"IMC: {imc}\nClasificación: {clasificacion}")
        pantalla_datos_personales.pack_forget()
        pantalla_resultados.pack(fill="both", expand=True)
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")

# Pantalla de inicio
tk.Label(pantalla_inicio, text="Bienvenido a la Calculadora de IMC", bg="#f0f0f0", font=("Helvetica", 16)).pack(pady=20)
tk.Button(pantalla_inicio, text="Comenzar", command=mostrar_genero, bg="#4CAF50", fg="white", width=15).pack(pady=10)

# Pantalla de género
tk.Label(pantalla_genero, text="Selecciona un género:", bg="#f0f0f0", font=("Helvetica", 14)).pack(pady=20)
ttk.Radiobutton(pantalla_genero, text="Masculino", variable=genero_var, value="Masculino").pack(pady=5)
ttk.Radiobutton(pantalla_genero, text="Femenino", variable=genero_var, value="Femenino").pack(pady=5)
tk.Button(pantalla_genero, text="Siguiente", command=mostrar_datos_personales, bg="#4CAF50", fg="white", width=15).pack(pady=10)
tk.Button(pantalla_genero, text="Regresar", command=mostrar_inicio, bg="#f44336", fg="white", width=15).pack(pady=5)

# Pantalla de datos personales
tk.Label(pantalla_datos_personales, text="Datos Personales", bg="#f0f0f0", font=("Helvetica", 16)).pack(pady=20)
tk.Label(pantalla_datos_personales, text="Nombre:", bg="#f0f0f0").pack(pady=5)
tk.Entry(pantalla_datos_personales, textvariable=nombre_var).pack(pady=5)

tk.Label(pantalla_datos_personales, text="Edad:", bg="#f0f0f0").pack(pady=5)
tk.Entry(pantalla_datos_personales, textvariable=edad_var).pack(pady=5)

tk.Label(pantalla_datos_personales, text="Peso (kg):", bg="#f0f0f0").pack(pady=5)
tk.Entry(pantalla_datos_personales, textvariable=peso_var).pack(pady=5)

tk.Label(pantalla_datos_personales, text="Altura (cm):", bg="#f0f0f0").pack(pady=5)
tk.Entry(pantalla_datos_personales, textvariable=altura_var).pack(pady=5)

tk.Button(pantalla_datos_personales, text="Calcular", command=mostrar_resultados, bg="#4CAF50", fg="white", width=15).pack(pady=10)
tk.Button(pantalla_datos_personales, text="Regresar", command=mostrar_genero, bg="#f44336", fg="white", width=15).pack(pady=5)

# Pantalla de resultados
label_resultado = tk.Label(pantalla_resultados, text="", bg="#f0f0f0", font=("Helvetica", 14))
label_resultado.pack(pady=20)
tk.Button(pantalla_resultados, text="Regresar al inicio", command=mostrar_inicio, bg="#4CAF50", fg="white", width=20).pack(pady=10)

# Iniciar con pantalla de inicio
mostrar_inicio()
ventana.mainloop()
