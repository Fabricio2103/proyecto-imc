import openpyxl
from openpyxl import Workbook
from datetime import datetime

def calcular_imc(peso, altura):
    """
    Calcula el índice de masa corporal (IMC).
    :param peso: Peso en kilogramos.
    :param altura: Altura en metros.
    :return: El IMC redondeado a 2 decimales o None si es que la altura no es válida.
    """
    if altura <= 0:
        return None  # Retorna None si la altura es inválida
    imc = peso / (altura ** 2)  # Calcular el IMC
    return round(imc, 2)  # Redondear a dos decimales

def clasificar_imc(imc):
    """
    Clasifica el IMC en rangos establecidos.
    :param imc: Índice de Masa Corporal.
    :return: La clasificación correspondiente o un mensaje de error si el IMC no es válido.
    """
    if imc is None:
        return "IMC no calculable"  # Mensaje si el IMC no es válido
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad ligera"
    elif 35 <= imc < 39.9:
        return "Obesidad"
    else:
        return "Obesidad mórbida"

def generar_recomendacion(clasificacion):
    """
    Genera una recomendación personalizada según la clasificación del IMC.
    :param clasificacion: Clasificación del IMC.
    :return: Una recomendación en formato de texto.
    """
    recomendaciones = {
        "Bajo peso": "Recomendaciones: Come con más frecuencia. Empieza poco a poco a hacer de 5 a 6 comidas más pequeñas durante el día, elige alimentos con más nutrientes, toma agua, haz ejercicio.",
        "Peso normal": "Recomendaciones: Sigue así, mantén tu cuerpo activo y no olvides tomar agua y cuidarte de los azúcares.",
        "Sobrepeso": "Recomendaciones: Toma entre 6 y 8 vasos de agua al día, cuida las bebidas con azúcar, haz ejercicio diario.",
        "Obesidad ligera": "Recomendaciones: Reducir las calorías, tomar entre 6 a 8 vasos de agua al día, evitar azúcares y grasas no saludables, hacer deporte o ejercicio.",
        "Obesidad": "Recomendaciones: Reducir las calorías, tomar entre 6 a 8 vasos de agua al día, evitar azúcares y grasas no saludables, hacer deporte o ejercicio.",
        "Obesidad mórbida": "Recomendaciones: Consultar con un especialista, reducir las calorías drásticamente, mantenerse hidratado y seguir un plan de ejercicio adaptado."
    }
    return recomendaciones.get(clasificacion, "No hay recomendaciones disponibles.")

def guardar_en_excel(datos, archivo='resultados_imc.xlsx'):
    """
    Guarda los datos proporcionados en un archivo Excel.
    :param datos: Diccionario con los datos a guardar.
    :param archivo: Nombre del archivo Excel.
    """
    try:
        # Intenta cargar el archivo existente
        wb = openpyxl.load_workbook(archivo)
        sheet = wb.active
    except FileNotFoundError:
        # Si no existe, crea un nuevo archivo y agrega encabezados
        wb = Workbook()
        sheet = wb.active
        encabezados = ["Nombre", "Edad", "Género", "Actividad Física", "Peso (kg)", "Altura (cm)", "IMC", "Clasificación"]
        sheet.append(encabezados)
    
    # Validar que los datos tengan las claves necesarias
    campos_requeridos = ["nombre", "edad", "genero", "actividad", "peso", "altura", "imc", "clasificacion"]
    for campo in campos_requeridos:
        if campo not in datos:
            raise ValueError(f"Falta el campo requerido: {campo}")
    
    # Agregar los datos a la hoja de cálculo
    fila = [
        datos['nombre'], 
        datos['edad'], 
        datos['genero'], 
        datos['actividad'], 
        datos['peso'], 
        datos['altura'], 
        datos['imc'], 
        datos['clasificacion'], 
    ]
    sheet.append(fila)
    
    # Guardar el archivo
    try:
        wb.save(archivo)
        print(f"Datos guardados correctamente en '{archivo}'.")
    except PermissionError:
        raise PermissionError(f"No se pudo guardar el archivo '{archivo}'. Verifica que no esté abierto.")