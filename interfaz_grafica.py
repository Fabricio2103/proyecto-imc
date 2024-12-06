from funciones import calcular_imc, clasificar_imc, generar_recomendacion, guardar_en_excel
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

# Función para validar entradas
def validar_entrada(valor):
    return valor.strip() != ""

# Función para cambiar el fondo
def cambiar_fondo(color):
    ventana.config(bg=color)
    for pantalla in [pantalla_inicio, pantalla_genero, pantalla_datos_personales, pantalla_imc, pantalla_resumen]:
        pantalla.config(bg=color)

# Funciones para cambiar pantallas
def mostrar_pantalla(pantalla_actual, pantalla_nueva):
    pantalla_actual.pack_forget()
    pantalla_nueva.pack(fill="both", expand=True)

# Validación del género
def validar_genero():
    if not genero_var.get():
        messagebox.showerror("Error", "Debes seleccionar un género")
    else:
        mostrar_pantalla(pantalla_genero, pantalla_datos_personales)

# Validación de datos personales
def validar_datos_personales():
    if not validar_entrada(nombre_var.get()) or edad_var.get() <= 0 or not actividad_var.get():
        messagebox.showerror("Error", "Todos los campos son obligatorios y válidos")
    else:
        mostrar_pantalla(pantalla_datos_personales, pantalla_imc)

# Calcular y mostrar IMC
def calcular_y_mostrar_imc():
    try:
        peso = peso_var.get()
        altura = altura_var.get() / 100  # Convertir cm a m
        if peso <= 0 or altura <= 0:
            raise ValueError("El peso y la altura deben ser mayores que cero")
        
        imc = calcular_imc(peso, altura)
        clasificacion = clasificar_imc(imc)
        recomendacion = generar_recomendacion(clasificacion)

        datos = {
            'nombre': nombre_var.get(),
            'edad': edad_var.get(),
            'genero': genero_var.get(),
            'actividad': actividad_var.get(),
            'peso': peso,
            'altura': altura_var.get(),
            'imc': imc,
            'clasificacion': clasificacion,
            'recomendacion': recomendacion
        }
        guardar_en_excel(datos)

        # Mostrar el resultado con formato visual
        resumen_texto.set(f"IMC: {imc:.2f}\nClasificación: {clasificacion}\n\n{recomendacion}")
        categoria_label.config(text=f"Categoría: {clasificacion}", fg=colores_clasificacion[clasificacion])
        mostrar_pantalla(pantalla_imc, pantalla_resumen)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Configuración principal de la ventana
ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("500x600")

# Configurar estilo para el tema del sistema
style = ttk.Style()
style.theme_use("clam")  # Cambia al tema del sistema

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
    "Bajo peso": "blue",
    "Peso normal": "green",
    "Sobrepeso": "orange",
    "Obesidad ligera": "red",
    "Obesidad": "darkred",
    "Obesidad mórbida": "maroon"
}

# Cargar y redimensionar imágenes
def cargar_imagen(ruta, ancho, alto):
    img = Image.open(ruta)
    img = img.resize((ancho, alto), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

imagen_inicio = cargar_imagen("imagenes/1.png", 500, 200)
imagen_genero = cargar_imagen("imagenes/2.png", 500, 200)
imagen_datos = cargar_imagen("imagenes/3.png", 500, 200)
imagen_imc = cargar_imagen("imagenes/4.png", 500, 200)
imagen_resumen = cargar_imagen("imagenes/5.png", 500, 200)

# Pantallas
pantalla_inicio = tk.Frame(ventana)
pantalla_genero = tk.Frame(ventana)
pantalla_datos_personales = tk.Frame(ventana)
pantalla_imc = tk.Frame(ventana)
pantalla_resumen = tk.Frame(ventana)

# Configuración de colores para las pantallas
for pantalla in [pantalla_inicio, pantalla_genero, pantalla_datos_personales, pantalla_imc, pantalla_resumen]:
    pantalla.config(bg="white")

# Pantalla de inicio
tk.Label(pantalla_inicio, image=imagen_inicio, bg="white").pack()
tk.Button(pantalla_inicio, text="Comenzar", font=("Helvetica", 14), bg="lightblue", command=lambda: mostrar_pantalla(pantalla_inicio, pantalla_genero)).pack(pady=20)

# Pantalla de género
tk.Label(pantalla_genero, image=imagen_genero, bg="white").pack()
tk.Label(pantalla_genero, text="Selecciona tu género", font=("Helvetica", 18, "bold"), bg="white").pack(pady=20)
ttk.Radiobutton(pantalla_genero, text="Hombre", variable=genero_var, value="Hombre").pack(pady=10)
ttk.Radiobutton(pantalla_genero, text="Mujer", variable=genero_var, value="Mujer").pack(pady=10)
tk.Button(pantalla_genero, text="Siguiente", font=("Helvetica", 12), bg="lightblue", command=validar_genero).pack(pady=20)

# Pantalla de datos personales
tk.Label(pantalla_datos_personales, image=imagen_datos, bg="white").pack()
tk.Label(pantalla_datos_personales, text="Ingresa tus datos", font=("Helvetica", 18, "bold"), bg="white").pack(pady=20)
tk.Label(pantalla_datos_personales, text="Nombre:", bg="white").pack(pady=5)
tk.Entry(pantalla_datos_personales, textvariable=nombre_var).pack(pady=5)
tk.Label(pantalla_datos_personales, text="Edad:", bg="white").pack(pady=5)
tk.Entry(pantalla_datos_personales, textvariable=edad_var).pack(pady=5)
tk.Label(pantalla_datos_personales, text="¿Actividad física?", bg="white").pack(pady=5)
ttk.Combobox(pantalla_datos_personales, textvariable=actividad_var, values=["Sí", "No"]).pack(pady=5)
tk.Button(pantalla_datos_personales, text="Siguiente", font=("Helvetica", 12), bg="lightblue", command=validar_datos_personales).pack(pady=20)

# Pantalla de IMC
tk.Label(pantalla_imc, image=imagen_imc, bg="white").pack()
tk.Label(pantalla_imc, text="Datos corporales", font=("Helvetica", 18, "bold"), bg="white").pack(pady=20)
tk.Label(pantalla_imc, text="Peso (kg):", bg="white").pack(pady=5)
tk.Entry(pantalla_imc, textvariable=peso_var).pack(pady=5)
tk.Label(pantalla_imc, text="Altura (cm):", bg="white").pack(pady=5)
tk.Entry(pantalla_imc, textvariable=altura_var).pack(pady=5)
tk.Button(pantalla_imc, text="Calcular IMC", font=("Helvetica", 12), bg="lightblue", command=calcular_y_mostrar_imc).pack(pady=20)

# Pantalla de resumen
tk.Label(pantalla_resumen, image=imagen_resumen, bg="white").pack()
tk.Label(pantalla_resumen, text="Resultados", font=("Helvetica", 18, "bold"), bg="white").pack(pady=20)
categoria_label = tk.Label(pantalla_resumen, text="", font=("Helvetica", 14), bg="white")
categoria_label.pack(pady=10)
tk.Label(pantalla_resumen, textvariable=resumen_texto, font=("Helvetica", 12), wraplength=400, bg="white").pack(pady=10)
tk.Button(pantalla_resumen, text="Salir", font=("Helvetica", 12), bg="lightblue", command=ventana.quit).pack(pady=20)

# Menú para cambiar el fondo
menu = tk.Menu(ventana)
ventana.config(menu=menu)
menu_fondo = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Fondo", menu=menu_fondo)
menu_fondo.add_command(label="Claro", command=lambda: cambiar_fondo("white"))
menu_fondo.add_command(label="Oscuro", command=lambda: cambiar_fondo("gray"))
menu_fondo.add_command(label="Celeste", command=lambda: cambiar_fondo("#cce7ff"))
menu_fondo.add_command(label="Rosa", command=lambda: cambiar_fondo("#ffe6e6"))
menu_fondo.add_command(label="Crema", command=lambda: cambiar_fondo("#fffdd0"))

# Mostrar pantalla inicial
pantalla_inicio.pack(fill="both", expand=True)

ventana.mainloop()