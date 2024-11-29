import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from funciones import calcular_imc, clasificar_imc, guardar_en_excel

# Función para validar entradas
def validar_entrada(valor):
    return valor.strip() != ""

# Funciones para cambiar pantallas
def mostrar_pantalla(pantalla_actual, pantalla_nueva):
    pantalla_actual.pack_forget()
    pantalla_nueva.pack(fill="both", expand=True)

# Funciones específicas para validaciones y cálculos
def validar_genero():
    if not genero_var.get():
        messagebox.showerror("Error", "Debes seleccionar un género")
    else:
        mostrar_pantalla(pantalla_genero, pantalla_datos_personales)

def validar_datos_personales():
    if not validar_entrada(nombre_var.get()) or edad_var.get() <= 0 or not actividad_var.get():
        messagebox.showerror("Error", "Todos los campos son obligatorios y válidos")
    else:
        mostrar_pantalla(pantalla_datos_personales, pantalla_imc)

def calcular_y_mostrar_imc():
    try:
        peso = peso_var.get()
        altura = altura_var.get() / 100  # Convertir cm a m
        if peso <= 0 or altura <= 0:
            raise ValueError("El peso y la altura deben ser mayores que cero")
        
        imc = calcular_imc(peso, altura)
        clasificacion = clasificar_imc(imc)

        datos = {
            'nombre': nombre_var.get(),
            'edad': edad_var.get(),
            'genero': genero_var.get(),
            'actividad': actividad_var.get(),
            'peso': peso,
            'altura': altura_var.get(),
            'imc': imc,
            'clasificacion': clasificacion
        }
        guardar_en_excel(datos)

        # Mostrar el resultado con formato visual
        resumen_texto.set(f"IMC: {imc:.2f}\nClasificación: {clasificacion}")
        categoria_label.config(text=f"Categoría: {clasificacion}", fg=colores_clasificacion[clasificacion])
        mostrar_pantalla(pantalla_imc, pantalla_resumen)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Configuración principal de la ventana
ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("500x600")
ventana.configure(bg="#f0f4fa")

# Variables
genero_var = tk.StringVar()
nombre_var = tk.StringVar()
edad_var = tk.IntVar()
actividad_var = tk.StringVar()
peso_var = tk.DoubleVar()
altura_var = tk.DoubleVar()
resumen_texto = tk.StringVar()

# Colores para clasificaciones
colores_clasificacion = {
    "Delgadez muy extrema": "blue",
    "Delgadez extrema": "blue",
    "Delgadez": "blue",
    "Normal": "green",
    "Sobrepeso": "orange",
    "Obesidad grado I": "red",
    "Obesidad grado II": "darkred",
    "Obesidad grado III": "maroon"
}

# Pantallas
pantalla_inicio = tk.Frame(ventana, bg="#f0f4fa")
pantalla_genero = tk.Frame(ventana, bg="#f0f4fa")
pantalla_datos_personales = tk.Frame(ventana, bg="#f0f4fa")
pantalla_imc = tk.Frame(ventana, bg="#f0f4fa")
pantalla_resumen = tk.Frame(ventana, bg="#f0f4fa")

# Pantalla de inicio
tk.Label(pantalla_inicio, text="Calculadora de IMC", font=("Helvetica", 24, "bold"), bg="#f0f4fa").pack(pady=40)
tk.Label(pantalla_inicio, text="Evalúa tu estado de salud con base en tu índice de masa corporal.", 
         font=("Helvetica", 12), bg="#f0f4fa", fg="gray").pack(pady=10)
tk.Button(pantalla_inicio, text="Comenzar", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=lambda: mostrar_pantalla(pantalla_inicio, pantalla_genero)).pack(pady=20)

# Pantalla de selección de género
tk.Label(pantalla_genero, text="Selecciona tu género", font=("Helvetica", 18, "bold"), bg="#f0f4fa").pack(pady=20)
ttk.Radiobutton(pantalla_genero, text="Hombre", variable=genero_var, value="Hombre").pack(pady=10)
ttk.Radiobutton(pantalla_genero, text="Mujer", variable=genero_var, value="Mujer").pack(pady=10)
tk.Button(pantalla_genero, text="Siguiente", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=validar_genero).pack(pady=20)
tk.Button(pantalla_genero, text="Regresar", font=("Helvetica", 12), bg="#f44336", fg="white", command=lambda: mostrar_pantalla(pantalla_genero, pantalla_inicio)).pack()

# Pantalla de datos personales
tk.Label(pantalla_datos_personales, text="Ingresa tus datos", font=("Helvetica", 18, "bold"), bg="#f0f4fa").pack(pady=20)
tk.Label(pantalla_datos_personales, text="Nombre:", bg="#f0f4fa").pack(pady=5)
tk.Entry(pantalla_datos_personales, textvariable=nombre_var).pack(pady=5)
tk.Label(pantalla_datos_personales, text="Edad:", bg="#f0f4fa").pack(pady=5)
tk.Entry(pantalla_datos_personales, textvariable=edad_var).pack(pady=5)
tk.Label(pantalla_datos_personales, text="¿Actividad física?", bg="#f0f4fa").pack(pady=5)
ttk.Combobox(pantalla_datos_personales, textvariable=actividad_var, values=["Sí", "No"]).pack(pady=5)
tk.Button(pantalla_datos_personales, text="Siguiente", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=validar_datos_personales).pack(pady=20)

# Pantalla de IMC
tk.Label(pantalla_imc, text="Datos corporales", font=("Helvetica", 18, "bold"), bg="#f0f4fa").pack(pady=20)
tk.Label(pantalla_imc, text="Peso (kg):", bg="#f0f4fa").pack(pady=5)
tk.Entry(pantalla_imc, textvariable=peso_var).pack(pady=5)
tk.Label(pantalla_imc, text="Altura (cm):", bg="#f0f4fa").pack(pady=5)
tk.Entry(pantalla_imc, textvariable=altura_var).pack(pady=5)
tk.Button(pantalla_imc, text="Calcular IMC", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=calcular_y_mostrar_imc).pack(pady=20)

# Pantalla de resumen
tk.Label(pantalla_resumen, text="Resultados", font=("Helvetica", 18, "bold"), bg="#f0f4fa").pack(pady=20)
categoria_label = tk.Label(pantalla_resumen, text="", font=("Helvetica", 14), bg="#f0f4fa")
categoria_label.pack(pady=10)
tk.Button(pantalla_resumen, text="Salir", font=("Helvetica", 12), bg="#f44336", fg="white", command=ventana.quit).pack(pady=20)

# Mostrar pantalla inicial
pantalla_inicio.pack(fill="both", expand=True)

ventana.mainloop()
