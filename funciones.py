import openpyxl
from openpyxl import Workbook

def calcular_imc(peso, altura):
    """Calcula el índice de masa corporal (IMC)."""
    if altura <= 0:
        return None  # Retorna None si la altura es inválida
    imc = peso / (altura ** 2)  # Calculo del IMC
    return round(imc, 2)  # Redondear a dos decimales

def clasificar_imc(imc):
    """Clasificación del Índice de Masa Corporal."""
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

def guardar_en_excel(datos, archivo='resultados_imc.xlsx'):
    """Guarda los datos en un archivo Excel utilizando openpyxl."""
    try:
        wb = openpyxl.load_workbook(archivo)  # Intenta cargar el archivo existente
    except FileNotFoundError:
        wb = Workbook()  # Si no existe, crea uno nuevo
        sheet = wb.active
        # Agregar encabezados solo si se crea un nuevo archivo
        sheet.append(["Nombre", "Edad", "Género", "Actividad Física", "Peso", "Altura", "IMC", "Clasificación"])

    sheet = wb.active
    # Agregar los datos a la hoja
    sheet.append([datos['nombre'], datos['edad'], datos['genero'], datos['actividad'], datos['peso'], datos['altura'], datos['imc'], datos['clasificacion']])
    wb.save(archivo)  # Guardar el archivo