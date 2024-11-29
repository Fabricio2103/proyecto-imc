import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import funciones

# Función para validar si el campo no está vacío
def validar_entrada(valor):
    return valor.strip() != ""

# Funciones para cada pantalla
def mostrar_inicio():
    pantalla_inicio.pack_forget()
    pantalla_genero.pack()

def regresar_inicio():
    pantalla_genero.pack_forget()
    pantalla_inicio.pack()

def mostrar_genero():
    if genero_var.get() == '':
        messagebox.showerror("Error", "Debes seleccionar un género")
        return
    pantalla_genero.pack_forget()
    pantalla_datos_personales.pack()

def regresar_genero():
    pantalla_datos_personales.pack_forget()
    pantalla_genero.pack()

